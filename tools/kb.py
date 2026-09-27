#!/usr/bin/env python3
"""Domain knowledge base tooling for the engineering-kit (stdlib only).

  kb.py validate [domain ...]        check schemas, references, cycles, paths
  kb.py build                        regenerate domains/{catalog,features,search-index}.json and INDEX.md
  kb.py find [--domain D] [--tag T] [--platform P] [--role R] [--entity E]
             [--integration I] [--compliance C] [--classification C] [--text S]
  kb.py order FEATURE_ID ... [--with-enhances]
                                     dependency closure in build order
  kb.py order --domain D [--classes core,common]
  kb.py matrix DOMAIN --requested ID,ID [--json]
                                     starting feature matrix with scope levels
  kb.py check-sources                cross-check MANIFEST.json, catalog.json, SOURCE.md, and disk
  kb.py gaps [domain ...] [--json]   per-domain quality-gate facts and what is missing
  kb.py check-selection FILE         check a project's feature-selection.json

Contract: domains/_schema/SCHEMA.md.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent
DOMAINS = KIT / "domains"
STANDARDS = KIT / "knowledge" / "standards" / "standards.json"
SHARED = DOMAINS / "shared-features.json"

DOMAIN_FILES = ["DOMAIN.md", "FEATURES.md", "feature-map.json", "entities.json", "roles.json",
                "workflows.json", "integrations.json", "compliance.json", "dependencies.json",
                "implementation-map.json", "sources.md"]
CLASSIFICATIONS = {"core", "common", "recommended", "optional", "premium", "compliance",
                   "integration", "platform", "infrastructure"}
LEVELS = {"none", "low", "medium", "high", "core"}
CONFIDENCE = {"high", "medium", "low"}
SOURCE_TYPES = {"authoritative", "implementation", "secondary"}
IMPL_STATUS = ["unknown", "missing", "not_required", "reference", "partial", "curated",
               "tested", "production_ready"]
# "available" in prose = any of partial/curated/tested/production_ready (a real kit path exists).
IMPL_AVAILABLE = {"partial", "curated", "tested", "production_ready"}
MATURITY = {"researching", "partial", "curated", "reviewed"}
DEP_TYPES = {"requires", "enhances"}
REL_TYPES = {"has_one", "has_many", "belongs_to", "many_to_many"}
EXPERIENCES = {"customer", "staff", "management", "administration", "partner", "system"}
COMPLIANCE_KINDS = {"regulation", "standard", "certification", "guideline"}
PLATFORM_KEYS = ["web", "mobile", "admin", "customer_portal", "backend", "ai", "real_time"]
IMPL_KEYS = ["web", "backend", "mobile", "ai"]
FOUNDATION = ["shared.auth", "shared.users", "shared.permissions"]
# Project scope levels (product-builder/PRODUCT-BUILDER.md §2). DOMAIN_EXPECTED is "the industry usually
# has this", which is never the same as "the client asked for it".
SCOPES = {"IN_SCOPE", "DEPENDENCY", "DOMAIN_EXPECTED", "PROPOSED", "OPTIONAL", "OUT_OF_SCOPE", "BLOCKED"}


def load(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def domain_ids() -> list[str]:
    return sorted(p.name for p in DOMAINS.iterdir()
                  if p.is_dir() and not p.name.startswith("_") and (p / "feature-map.json").exists())


def domain_md_maturity(d: str) -> str | None:
    """The maturity asserted by a '## Maturity: <value>' heading in DOMAIN.md, if it has one."""
    path = DOMAINS / d / "DOMAIN.md"
    if not path.exists():
        return None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## Maturity:"):
            return line.split(":", 1)[1].strip().strip("`").lower()
    return None


def has_files(rel: str) -> bool:
    """Whether a kit path holds real content. `.gitkeep` markers on the not-yet-promoted
    directories don't count, or every empty area would read as implemented."""
    p = KIT / rel
    if p.is_file():
        return True
    return p.is_dir() and any(f.is_file() and not f.name.startswith(".") for f in p.rglob("*"))


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def err(self, where: str, msg: str) -> None:
        self.errors.append(f"{where}: {msg}")

    def warn(self, where: str, msg: str) -> None:
        self.warnings.append(f"{where}: {msg}")


def load_domain(d: str, rep: Report) -> dict | None:
    out = {}
    for name in DOMAIN_FILES:
        p = DOMAINS / d / name
        if not p.exists():
            rep.err(d, f"missing {name}")
            continue
        if name.endswith(".json"):
            try:
                out[name] = load(p)
            except json.JSONDecodeError as e:
                rep.err(f"{d}/{name}", f"invalid JSON: {e}")
    return out if "feature-map.json" in out else None


def check_shared_candidates(shared: dict, rep: Report) -> None:
    """source_candidates must point at real source folders, and on_disk must not be stale."""
    for f in shared.get("features", []):
        for c in f.get("source_candidates", []):
            w = f"shared/{f['id']}/candidate/{c.get('source')}"
            src = KIT / c.get("source", "")
            if not src.is_dir():
                rep.err(w, "source folder does not exist")
                continue
            if not (src / "SOURCE.md").exists():
                rep.err(w, "source folder has no SOURCE.md")
            on_disk = (src / "source").is_dir()
            if c.get("on_disk") != on_disk:
                rep.err(w, f"on_disk is {c.get('on_disk')} but source/ {'exists' if on_disk else 'does not exist'}")
            for rel in c.get("paths", []):
                if not (src / rel).exists():
                    rep.err(w, f"verified path {rel} does not exist")
            for rel in c.get("unverified_paths", []):
                if (src / rel).exists():
                    rep.err(w, f"{rel} is listed unverified but now exists - move it to paths")


def all_feature_ids(domains: dict[str, dict], shared: dict) -> set[str]:
    ids = {f["id"] for f in shared["features"]}
    for data in domains.values():
        ids |= {f.get("id") for f in data["feature-map.json"].get("features", [])}
    return ids


def check_provenance(where: str, item: dict, source_ids: set[str], rep: Report) -> None:
    prov = item.get("provenance")
    if not isinstance(prov, dict):
        rep.err(where, "missing provenance")
        return
    if prov.get("confidence") not in CONFIDENCE:
        rep.err(where, f"bad confidence {prov.get('confidence')!r}")
    srcs = prov.get("sources") or []
    if not srcs:
        rep.err(where, "provenance.sources is empty")
    for s in srcs:
        if s not in source_ids:
            rep.err(where, f"unknown source {s!r}")


def find_cycle(nodes: set[str], edges: list[tuple[str, str]]) -> list[str] | None:
    graph: dict[str, list[str]] = {n: [] for n in nodes}
    for a, b in edges:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, [])
    color: dict[str, int] = {}
    stack: list[str] = []

    def visit(n: str) -> list[str] | None:
        color[n] = 1
        stack.append(n)
        for m in graph[n]:
            if color.get(m) == 1:
                return stack[stack.index(m):] + [m]
            if m not in color and (c := visit(m)):
                return c
        stack.pop()
        color[n] = 2
        return None

    for n in graph:
        if n not in color and (c := visit(n)):
            return c
    return None


def validate(only: list[str]) -> Report:
    rep = Report()
    shared = load(SHARED)
    standards = load(STANDARDS)
    std_ids = {f"std:{s['id']}" for s in standards["standards"]}
    for s in standards["standards"]:
        if s.get("status") in {"acquired", "partial"} and not (s.get("local_path") and has_files(s["local_path"])):
            rep.err(f"standards/{s['id']}", f"status {s['status']} but {s.get('local_path')} is empty")
    check_shared_candidates(shared, rep)
    seen_shared: set[str] = set()
    for f in shared["features"]:
        if f["id"] in seen_shared:
            rep.err("shared-features", f"duplicate {f['id']}")
        seen_shared.add(f["id"])
        if not f["id"].startswith("shared."):
            rep.err("shared-features", f"{f['id']} must start with shared.")
        if f.get("classification") not in CLASSIFICATIONS:
            rep.err(f"shared/{f['id']}", "bad classification")

    domains: dict[str, dict] = {}
    for d in domain_ids():
        data = load_domain(d, rep)
        if data:
            domains[d] = data
    for p in DOMAINS.iterdir():
        if p.is_dir() and not p.name.startswith("_") and p.name not in domains and not (p / "feature-map.json").exists():
            rep.warn(p.name, "domain folder has no feature-map.json yet")

    features_all = all_feature_ids(domains, shared)
    entities_all = {f"{d}:{e['id']}" for d, x in domains.items()
                    for e in x.get("entities.json", {}).get("entities", [])}
    seen_features: set[str] = set(seen_shared)
    targets = only or list(domains)

    for d in targets:
        if d not in domains:
            rep.err(d, "unknown or unloadable domain")
            continue
        x = domains[d]
        fm = x["feature-map.json"]
        for name, doc in x.items():
            if doc.get("schema") != 1:
                rep.err(f"{d}/{name}", "schema must be 1")
            if doc.get("domain") != d:
                rep.err(f"{d}/{name}", f"domain must be {d!r}")
            if not doc.get("last_reviewed"):
                rep.err(f"{d}/{name}", "missing last_reviewed")
        if fm.get("maturity") not in MATURITY:
            rep.err(f"{d}/feature-map", f"bad maturity {fm.get('maturity')!r}")
        # DOMAIN.md is the prose twin of feature-map.json; a stale "## Maturity: x" heading there
        # is how an over-claim survives a re-review, so the two must agree.
        doc_maturity = domain_md_maturity(d)
        if doc_maturity and doc_maturity != fm.get("maturity"):
            rep.err(f"{d}/DOMAIN.md", f"'## Maturity: {doc_maturity}' contradicts "
                                     f"feature-map maturity {fm.get('maturity')!r}")
        local_src = {}
        for s in fm.get("sources", []):
            if s.get("id") in local_src:
                rep.err(f"{d}/sources", f"duplicate source {s.get('id')}")
            local_src[s.get("id")] = s
            if s.get("source_type") not in SOURCE_TYPES:
                rep.err(f"{d}/sources/{s.get('id')}", f"bad source_type {s.get('source_type')!r}")
            for k in ("title", "url", "license"):
                if not s.get(k):
                    rep.warn(f"{d}/sources/{s.get('id')}", f"missing {k}")
            if s.get("local_path") and not (KIT / s["local_path"]).exists():
                rep.err(f"{d}/sources/{s.get('id')}", f"local_path {s['local_path']} does not exist")
        source_ids = set(local_src) | std_ids

        roles = {r["id"] for r in x.get("roles.json", {}).get("roles", [])}
        ents = {e["id"] for e in x.get("entities.json", {}).get("entities", [])}
        wfs = {w["id"] for w in x.get("workflows.json", {}).get("workflows", [])}
        ints = {i["id"] for i in x.get("integrations.json", {}).get("integrations", [])}
        comps = {c["id"] for c in x.get("compliance.json", {}).get("items", [])}

        feats = fm.get("features", [])
        if fm.get("maturity") in {"curated", "reviewed"} and (len(feats) < 10 or len(local_src) < 3):
            rep.err(f"{d}/feature-map", "curated/reviewed needs >=10 features and >=3 sources")
        low = sum(1 for f in feats if f.get("provenance", {}).get("confidence") == "low")
        if fm.get("maturity") in {"curated", "reviewed"} and feats and low / len(feats) > 0.3:
            rep.err(f"{d}/feature-map", f"curated/reviewed needs <=30% low-confidence features ({low}/{len(feats)})")
        for f in feats:
            fid = f.get("id", "?")
            w = f"{d}/{fid}"
            if not fid.startswith(f"{d}."):
                rep.err(w, f"id must start with {d}.")
            if fid in seen_features:
                rep.err(w, "duplicate feature id")
            seen_features.add(fid)
            if f.get("classification") == "requested":
                rep.err(w, "'requested' is per-project, never in the catalog")
            elif f.get("classification") not in CLASSIFICATIONS:
                rep.err(w, f"bad classification {f.get('classification')!r}")
            for k in ("name", "description"):
                if not f.get(k):
                    rep.err(w, f"missing {k}")
            for k in ("ai_relevance", "real_time_relevance"):
                if f.get(k) not in LEVELS:
                    rep.err(w, f"bad {k} {f.get(k)!r}")
            plat = f.get("platforms", {})
            for k in PLATFORM_KEYS:
                if not isinstance(plat.get(k), bool):
                    rep.err(w, f"platforms.{k} must be bool")
            for u in f.get("users", []):
                if u not in roles:
                    rep.err(w, f"unknown role {u!r}")
            for e in f.get("entities", []):
                if e not in ents and e not in entities_all:
                    rep.err(w, f"unknown entity {e!r}")
            for wf in f.get("workflows", []):
                if wf not in wfs:
                    rep.err(w, f"unknown workflow {wf!r}")
            for i in f.get("integrations", []):
                if i not in ints:
                    rep.err(w, f"unknown integration {i!r}")
            for c in f.get("compliance", []):
                if c not in comps:
                    rep.err(w, f"unknown compliance item {c!r}")
            if "implementation_status" in f or "dependencies" in f:
                rep.err(w, "dependencies/implementation_status belong in their own files")
            check_provenance(w, f, source_ids, rep)
            srcs = f.get("provenance", {}).get("sources", [])
            if f.get("provenance", {}).get("confidence") == "high":
                authoritative = any(s.startswith("std:") or local_src.get(s, {}).get("source_type") == "authoritative" for s in srcs)
                impls = sum(1 for s in srcs if local_src.get(s, {}).get("source_type") == "implementation")
                if not authoritative and impls < 3:
                    rep.err(w, "high confidence needs an authoritative source or >=3 implementations")

        dfeats = {f.get("id") for f in feats}

        def check_features(where: str, refs) -> None:
            for r in refs or []:
                if r not in features_all:
                    rep.err(where, f"unknown feature {r!r}")

        for e in x.get("entities.json", {}).get("entities", []):
            w = f"{d}/entity/{e.get('id')}"
            for r in e.get("relationships", []):
                if r.get("type") not in REL_TYPES:
                    rep.err(w, f"bad relationship type {r.get('type')!r}")
                t = r.get("target", "")
                if t not in ents and t not in entities_all:
                    rep.err(w, f"unknown relationship target {t!r}")
            check_features(w, e.get("related_features"))
            for m in e.get("standard_mapping", []):
                if m.get("source") not in source_ids:
                    rep.err(w, f"unknown standard_mapping source {m.get('source')!r}")
            check_provenance(w, e, source_ids, rep)
        for r in x.get("roles.json", {}).get("roles", []):
            w = f"{d}/role/{r.get('id')}"
            if r.get("experience") not in EXPERIENCES:
                rep.err(w, f"bad experience {r.get('experience')!r}")
            check_features(w, r.get("related_features"))
            check_provenance(w, r, source_ids, rep)
        for wf in x.get("workflows.json", {}).get("workflows", []):
            w = f"{d}/workflow/{wf.get('id')}"
            if wf.get("actor") not in roles:
                rep.err(w, f"actor {wf.get('actor')!r} is not a role")
            for e in wf.get("entities", []):
                if e not in ents and e not in entities_all:
                    rep.err(w, f"unknown entity {e!r}")
            for i in wf.get("integrations", []):
                if i not in ints:
                    rep.err(w, f"unknown integration {i!r}")
            check_features(w, wf.get("features"))
            sm = wf.get("state_machine")
            if sm:
                states = set(sm.get("states", []))
                if sm.get("entity") not in ents:
                    rep.err(w, f"state_machine.entity {sm.get('entity')!r} unknown")
                if sm.get("initial") not in states:
                    rep.err(w, "state_machine.initial not in states")
                for t in sm.get("terminal", []):
                    if t not in states:
                        rep.err(w, f"terminal {t!r} not in states")
                for t in sm.get("transitions", []):
                    if t.get("from") not in states or t.get("to") not in states or not t.get("event"):
                        rep.err(w, f"bad transition {t}")
            check_provenance(w, wf, source_ids, rep)
        for i in x.get("integrations.json", {}).get("integrations", []):
            w = f"{d}/integration/{i.get('id')}"
            if i.get("classification") not in CLASSIFICATIONS:
                rep.err(w, f"bad classification {i.get('classification')!r}")
            check_features(w, i.get("related_features"))
            check_provenance(w, i, source_ids, rep)
        comp = x.get("compliance.json", {})
        if comp and not comp.get("disclaimer"):
            rep.err(f"{d}/compliance", "missing disclaimer")
        for c in comp.get("items", []):
            w = f"{d}/compliance/{c.get('id')}"
            if c.get("kind") not in COMPLIANCE_KINDS:
                rep.err(w, f"bad kind {c.get('kind')!r}")
            if not c.get("jurisdiction"):
                rep.err(w, "missing jurisdiction")
            if not isinstance(c.get("requires_human_review"), bool):
                rep.err(w, "requires_human_review must be bool")
            check_features(w, c.get("affected_features"))
            check_provenance(w, c, source_ids, rep)

        edges = []
        for e in x.get("dependencies.json", {}).get("edges", []):
            w = f"{d}/dependency {e.get('from')}->{e.get('to')}"
            if e.get("type") not in DEP_TYPES:
                rep.err(w, f"bad type {e.get('type')!r}")
            if e.get("from") not in dfeats:
                rep.err(w, "'from' must be a feature of this domain")
            if e.get("to") not in features_all:
                rep.err(w, "unknown 'to' feature")
            if e.get("from") == e.get("to"):
                rep.err(w, "self-dependency")
            if e.get("type") == "requires":
                edges.append((e["from"], e["to"]))
        if cyc := find_cycle(dfeats, edges):
            rep.err(f"{d}/dependencies", "requires-cycle: " + " -> ".join(cyc))

        fmd = DOMAINS / d / "FEATURES.md"
        if fmd.exists() and x.get("feature-map.json") and x.get("implementation-map.json"):
            want = features_md(d, x["feature-map.json"],
                               {m["feature"]: m for m in x["implementation-map.json"]["mappings"]})
            if fmd.read_text(encoding="utf-8") != want:
                rep.err(f"{d}/FEATURES.md", "out of date - it is generated; run `kb.py build`")
        smd = DOMAINS / d / "sources.md"
        if smd.exists() and x.get("feature-map.json"):
            if smd.read_text(encoding="utf-8") != sources_md(d, x):
                rep.err(f"{d}/sources.md", "out of date - it is generated; run `kb.py build`")

        mapped = set()
        for m in x.get("implementation-map.json", {}).get("mappings", []):
            w = f"{d}/impl/{m.get('feature')}"
            mapped.add(m.get("feature"))
            if m.get("feature") not in dfeats:
                rep.err(w, "unknown feature")
            if m.get("status") not in IMPL_STATUS:
                rep.err(w, f"bad status {m.get('status')!r}")
            paths = [p for k in IMPL_KEYS for p in m.get("implementations", {}).get(k, [])]
            for p in paths:
                if not has_files(p):
                    rep.err(w, f"implementation path {p} has no files")
            for p in m.get("references", []):
                if not (KIT / p).exists():
                    rep.err(w, f"reference path {p} does not exist")
            if m.get("status") in IMPL_AVAILABLE and not paths:
                rep.err(w, f"status {m['status']} needs implementation paths")
            if m.get("status") == "reference" and not m.get("references"):
                rep.err(w, "status reference needs references")
            if m.get("status") in {"missing", "not_required"} and paths:
                rep.err(w, f"status {m['status']} must not carry implementation paths")
            if m.get("status") == "not_required" and not m.get("notes"):
                rep.err(w, "status not_required needs notes saying why")
        for fid in dfeats - mapped:
            rep.warn(f"{d}/impl", f"{fid} has no implementation-map entry")
    return rep


# ---------- build ----------

def impl_status_shared(f: dict) -> str:
    """Same honesty rule as a domain feature: kit files mean partial, an on-disk source means reference."""
    if any(has_files(p) for p in f.get("kit_paths", [])):
        return "partial"
    if any(c.get("paths") or (KIT / c["source"] / "source").is_dir()
           for c in f.get("source_candidates", [])):
        return "reference"
    return "missing"


def regen_features_md() -> None:
    """FEATURES.md is generated, so rewrite it before validating - otherwise the drift check
    the validator performs would block the very build that fixes the drift."""
    for d in domain_ids():
        fm = load(DOMAINS / d / "feature-map.json")
        impl = {m["feature"]: m for m in load(DOMAINS / d / "implementation-map.json")["mappings"]}
        (DOMAINS / d / "FEATURES.md").write_text(features_md(d, fm, impl), encoding="utf-8")
        x = {n: load(DOMAINS / d / n) for n in DOMAIN_FILES if n.endswith(".json")}
        (DOMAINS / d / "sources.md").write_text(sources_md(d, x), encoding="utf-8")


def build() -> None:
    regen_features_md()
    rep = validate([])
    if rep.errors:
        print("refusing to build: validation errors (run `kb.py validate`)", file=sys.stderr)
        sys.exit(1)
    shared = load(SHARED)
    standards = {s["id"]: s for s in load(STANDARDS)["standards"]}
    today = date.today().isoformat()
    catalog, features, index = [], [], []
    shared_domains: dict[str, set[str]] = {f["id"]: set() for f in shared["features"]}
    for d in domain_ids():
        fm = load(DOMAINS / d / "feature-map.json")
        deps = load(DOMAINS / d / "dependencies.json")["edges"]
        impl = {m["feature"]: m for m in load(DOMAINS / d / "implementation-map.json")["mappings"]}
        (DOMAINS / d / "FEATURES.md").write_text(features_md(d, fm, impl), encoding="utf-8")
        roles = load(DOMAINS / d / "roles.json")["roles"]
        ents = load(DOMAINS / d / "entities.json")["entities"]
        wfs = load(DOMAINS / d / "workflows.json")["workflows"]
        comp = load(DOMAINS / d / "compliance.json")["items"]
        ints = load(DOMAINS / d / "integrations.json")["integrations"]
        for e in deps:
            if e["to"] in shared_domains:
                shared_domains[e["to"]].add(d)
        feats = fm["features"]
        by_class: dict[str, int] = {}
        for f in feats:
            by_class[f["classification"]] = by_class.get(f["classification"], 0) + 1
        coverage = {k: sum(1 for f in feats if impl.get(f["id"], {}).get("implementations", {}).get(k)) for k in IMPL_KEYS}
        std_refs = sorted({s for f in feats for s in f["provenance"]["sources"] if s.startswith("std:")})
        catalog.append({
            "id": d, "name": fm.get("name", d), "aliases": fm.get("aliases", []),
            "description": fm.get("description", ""), "nace": fm.get("nace", []),
            "maturity": fm["maturity"], "last_reviewed": fm["last_reviewed"],
            "feature_count": len(feats), "features_by_classification": by_class,
            "features_by_confidence": {c: sum(1 for f in feats if f["provenance"]["confidence"] == c) for c in ("high", "medium", "low")},
            "entity_count": len(ents), "role_count": len(roles), "workflow_count": len(wfs),
            "state_machine_count": sum(1 for w in wfs if w.get("state_machine")),
            "compliance_count": len(comp), "integration_count": len(ints),
            "standards": std_refs + [f"{s['id']}" for s in fm.get("sources", []) if s["source_type"] == "authoritative"],
            "implementation_references": [s["id"] for s in fm.get("sources", []) if s["source_type"] == "implementation"],
            "source_count": len(fm.get("sources", [])),
            "implementation_coverage": coverage,
        })
        role_names = {r["id"] for r in roles}
        for f in feats:
            m = impl.get(f["id"], {})
            rec = {
                "id": f["id"], "name": f["name"], "domain": d, "classification": f["classification"],
                "description": f["description"], "tags": f.get("tags", []),
                "platforms": f["platforms"], "users": [u for u in f.get("users", []) if u in role_names],
                "entities": f.get("entities", []), "workflows": f.get("workflows", []),
                "integrations": f.get("integrations", []), "compliance": f.get("compliance", []),
                "ai_relevance": f["ai_relevance"], "real_time_relevance": f["real_time_relevance"],
                "depends_on": [e["to"] for e in deps if e["from"] == f["id"] and e["type"] == "requires"],
                "enhanced_by": [e["to"] for e in deps if e["from"] == f["id"] and e["type"] == "enhances"],
                "implementation_status": m.get("status", "unknown"),
                "confidence": f["provenance"]["confidence"],
                "path": f"domains/{d}/feature-map.json",
            }
            features.append(rec)
            index.append({"kind": "feature", "id": f["id"], "domain": d,
                          "keys": sorted(set(f.get("tags", []) + f.get("users", []) + f.get("entities", [])
                                             + f.get("workflows", []) + f.get("capabilities", [])
                                             + f.get("integrations", []) + f.get("compliance", [])
                                             + [k for k, v in f["platforms"].items() if v]
                                             + [f["classification"], m.get("status", "unknown")]
                                             + [s for s in f["provenance"]["sources"]]))})
        for r in roles:
            index.append({"kind": "role", "id": f"{d}:{r['id']}", "domain": d, "keys": [r["experience"]] + r.get("related_features", [])})
        for e in ents:
            index.append({"kind": "entity", "id": f"{d}:{e['id']}", "domain": d,
                          "keys": e.get("related_features", []) + [m["concept"] for m in e.get("standard_mapping", [])]})
        for w in wfs:
            index.append({"kind": "workflow", "id": f"{d}:{w['id']}", "domain": d, "keys": w.get("features", []) + w.get("entities", [])})
        for i in ints:
            index.append({"kind": "integration", "id": f"{d}:{i['id']}", "domain": d,
                          "keys": sorted(set([i.get("category", ""), i.get("classification", "")]
                                             + i.get("protocols", []) + i.get("related_features", [])))})
        for c in comp:
            index.append({"kind": "compliance", "id": f"{d}:{c['id']}", "domain": d,
                          "keys": sorted(set([c.get("kind", ""), c.get("jurisdiction", "")]
                                             + c.get("affected_features", [])))})
        for s in fm.get("sources", []):
            index.append({"kind": "source", "id": f"{d}:{s['id']}", "domain": d, "keys": [s["source_type"], s.get("license", "")]})
    shared_out = []
    for f in shared["features"]:
        shared_out.append({**f, "domain": "shared", "domains": sorted(shared_domains[f["id"]]),
                           "implementation_status": impl_status_shared(f)})
    for sid, s in standards.items():
        index.append({"kind": "standard", "id": f"std:{sid}", "domain": "*", "keys": s.get("domains", []) + [s["status"], s.get("license", "")]})

    def dump(name: str, obj) -> None:
        (DOMAINS / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    dump("catalog.json", {"schema": 1, "generated": today, "generator": "tools/kb.py build", "domains": catalog})
    dump("features.json", {"schema": 1, "generated": today, "generator": "tools/kb.py build",
                           "shared": shared_out, "domain_features": features})
    dump("search-index.json", {"schema": 1, "generated": today, "generator": "tools/kb.py build", "entries": index})
    write_index_md(catalog, shared_out, standards, today)
    print(f"built: {len(catalog)} domains, {len(features)} domain features, {len(shared_out)} shared, {len(index)} index entries")
    for w in rep.warnings:
        print("warning:", w)


CLASS_ORDER = ["core", "common", "recommended", "optional", "premium",
               "compliance", "integration", "platform", "infrastructure"]


def features_md(d: str, fm: dict, impl: dict[str, dict]) -> str:
    """FEATURES.md is a pure view of feature-map.json, so it is generated, never hand-edited."""
    feats = fm["features"]
    lines = [
        f"# {fm.get('name', d)} features",
        "",
        f"Generated by `tools/kb.py build` from `feature-map.json` — do not edit by hand. "
        f"{len(feats)} features. Narrative context: [`DOMAIN.md`](DOMAIN.md). Contract: "
        f"[`../_schema/SCHEMA.md`](../_schema/SCHEMA.md).",
        "",
        "A feature here is domain knowledge, not project scope. `Impl` is the kit's reuse status from "
        "`implementation-map.json`: `missing` and `reference` both mean there is nothing to reuse yet.",
    ]
    known = [c for c in CLASS_ORDER if any(f["classification"] == c for f in feats)]
    for c in known + sorted({f["classification"] for f in feats} - set(known)):
        rows = [f for f in feats if f["classification"] == c]
        if not rows:
            continue
        lines += ["", f"## {c.replace('_', ' ').title()} ({len(rows)})", "",
                  "| Feature | Description | Confidence | Platforms | RT | AI | Impl | Sources |",
                  "|---|---|---|---|---|---|---|---|"]
        for f in sorted(rows, key=lambda x: x["id"]):
            plat = ", ".join(k for k, v in f.get("platforms", {}).items() if v) or "—"
            pv = f["provenance"]
            lines.append(
                f"| `{f['id']}` {f['name']} | {f['description']} | {pv['confidence']} | {plat} | "
                f"{f.get('real_time_relevance', '—')} | {f.get('ai_relevance', '—')} | "
                f"{impl.get(f['id'], {}).get('status', 'unknown')} | {', '.join(pv['sources']) or '—'} |")
    return "\n".join(lines) + "\n"


def sources_md(d: str, x: dict) -> str:
    """sources.md is a pure view of feature-map.json's sources array, so it is generated too.

    The "Informed" column is computed by walking every provenance block in the domain, which is
    what makes an uncited source visible instead of quietly decorative.
    """
    fm = x["feature-map.json"]
    srcs = fm.get("sources", [])
    used: dict[str, set[str]] = {s["id"]: set() for s in srcs}
    buckets = [("feature-map.json", "features", "id"), ("entities.json", "entities", "id"),
               ("roles.json", "roles", "id"), ("workflows.json", "workflows", "id"),
               ("integrations.json", "integrations", "id"), ("compliance.json", "items", "id")]
    kinds = {"feature-map.json": "", "entities.json": "entity:", "roles.json": "role:",
             "workflows.json": "workflow:", "integrations.json": "integration:",
             "compliance.json": "compliance:"}
    for fname, key, idk in buckets:
        for it in x.get(fname, {}).get(key, []):
            label = kinds[fname] + str(it.get(idk, "?")).removeprefix(f"{d}.")
            for sid in it.get("provenance", {}).get("sources", []):
                if sid in used:
                    used[sid].add(label)
    lines = [
        f"# {fm.get('name', d)} sources",
        "",
        "Generated by `tools/kb.py build` from `feature-map.json` — do not edit by hand. "
        "Class, license, and what each source informed. A source with an empty **Informed** column is cited "
        "nowhere and should be removed or used.",
        "",
        "| ID | Title | Type | License | Version | Retrieved | Local clone | Informed |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for s in srcs:
        sid = s["id"]
        lp = s.get("local_path") or ""
        disk = f"`{lp}`" + ("" if (KIT / lp / "source").is_dir() else " (not on disk)") if lp else "—"
        inf = ", ".join(f"`{u}`" for u in sorted(used[sid])) or "**—**"
        lines.append(f"| `{sid}` | [{s.get('title', sid)}]({s.get('url', '')}) | {s.get('source_type', '')} | "
                     f"{s.get('license', '—')} | {s.get('version') or '—'} | {s.get('retrieved') or '—'} | {disk} | {inf} |")
    notes = [s for s in srcs if s.get("notes")]
    if notes:
        lines += ["", "## Notes", ""]
        for s in notes:
            lines.append(f"- **`{s['id']}`**: {s['notes']}")
    std = sorted({sid for u in used.values() for sid in ()} |
                 {sid for fname, key, _ in buckets for it in x.get(fname, {}).get(key, [])
                  for sid in it.get("provenance", {}).get("sources", []) if sid.startswith("std:")})
    if std:
        lines += ["", "## Registered standards cited", "",
                  "Records live in [`../../knowledge/standards/standards.json`](../../knowledge/standards/standards.json).",
                  "", ", ".join(f"`{s}`" for s in std)]
    return "\n".join(lines) + "\n"


def write_index_md(catalog: list[dict], shared: list[dict], standards: dict, today: str) -> None:
    lines = [
        "# Domain index",
        "",
        f"Generated by `tools/kb.py build` on {today} — do not edit by hand. Contract: [`_schema/SCHEMA.md`](_schema/SCHEMA.md). "
        "How the product builder uses this: [`../product-builder/PRODUCT-BUILDER.md`](../product-builder/PRODUCT-BUILDER.md).",
        "",
        "Read a domain's `DOMAIN.md` → `FEATURES.md` → `feature-map.json` → `dependencies.json` first; open raw standards or `sources/` only for detail.",
        "A catalog feature is domain knowledge, not client scope.",
        "",
        "| Domain | Description | Features | Core | Common | Standards | Implementation refs | Maturity | Reviewed |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for c in catalog:
        bc = c["features_by_classification"]
        lines.append(f"| [{c['name']}]({c['id']}/DOMAIN.md) | {c['description']} | {c['feature_count']} | {bc.get('core', 0)} | "
                     f"{bc.get('common', 0)} | {', '.join(c['standards']) or '—'} | {', '.join(c['implementation_references']) or '—'} | "
                     f"{c['maturity']} | {c['last_reviewed']} |")
    lines += ["", "## Shared capabilities", "",
              "Defined in [`shared-features.json`](shared-features.json); implementation lives in the kit paths listed.", "",
              "| ID | Name | Kit paths | Status | Used by |", "|---|---|---|---|---|"]
    for f in shared:
        lines.append(f"| `{f['id']}` | {f['name']} | {', '.join(f'`{p}`' for p in f['kit_paths']) or '—'} | "
                     f"{f['implementation_status']} | {', '.join(f['domains']) or '—'} |")
    lines += ["", "## Standards", "", "Registry: [`../knowledge/standards/standards.json`](../knowledge/standards/standards.json).", "",
              "| ID | Title | Version | Status | Local path |", "|---|---|---|---|---|"]
    for sid, s in standards.items():
        lines.append(f"| `std:{sid}` | {s['title']} | {s.get('version') or '—'} | {s['status']} | "
                     f"{('`' + s['local_path'] + '`') if s.get('local_path') else '—'} |")
    (DOMAINS / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


# ---------- gap analysis ----------

PRIORITY = ["exchange", "fintech", "restaurant", "hospitality", "logistics", "ecommerce", "crm",
            "booking", "support", "healthcare", "real-estate", "education", "project-management",
            "manufacturing", "general-saas"]


def gate(d: str) -> dict:
    """Quality-gate facts for one domain. Every number is counted, never asserted."""
    fm = load(DOMAINS / d / "feature-map.json")
    feats = fm["features"]
    ents = load(DOMAINS / d / "entities.json")["entities"]
    roles = load(DOMAINS / d / "roles.json")["roles"]
    wfs = load(DOMAINS / d / "workflows.json")["workflows"]
    ints = load(DOMAINS / d / "integrations.json")["integrations"]
    comp = load(DOMAINS / d / "compliance.json")["items"]
    edges = load(DOMAINS / d / "dependencies.json")["edges"]
    impl = {m["feature"]: m for m in load(DOMAINS / d / "implementation-map.json")["mappings"]}
    srcs = fm.get("sources", [])

    fids = {f["id"] for f in feats}
    low = [f["id"] for f in feats if f["provenance"]["confidence"] == "low"]
    single = [f["id"] for f in feats if len(f["provenance"]["sources"]) < 2]
    no_wf = [f["id"] for f in feats if not f.get("workflows")]
    no_ent = [f["id"] for f in feats if not f.get("entities")]
    no_user = [f["id"] for f in feats if not f.get("users")]
    no_dep = sorted(fids - {e["from"] for e in edges} - {e["to"] for e in edges})
    unmapped = sorted(fids - set(impl))
    ent_no_rel = [e["id"] for e in ents if not e.get("relationships")]
    wf_no_sm = [w["id"] for w in wfs if not w.get("state_machine")]
    by_class: dict[str, int] = {}
    for f in feats:
        by_class[f["classification"]] = by_class.get(f["classification"], 0) + 1
    st: dict[str, int] = {}
    for m in impl.values():
        st[m["status"]] = st.get(m["status"], 0) + 1
    # A domain cites a registered standard as "std:<id>" from knowledge/standards/standards.json
    # rather than duplicating it into its own sources array - those count too (SCHEMA.md, "IDs").
    std_refs = sorted({s for it in list(feats) + list(ents) + list(wfs) + list(ints) + list(comp)
                       for s in it.get("provenance", {}).get("sources", []) if s.startswith("std:")})
    authoritative = [s["id"] for s in srcs if s["source_type"] == "authoritative"] + std_refs
    on_disk = [s["id"] for s in srcs if s.get("local_path") and has_files(s["local_path"])]
    total_sources = len(srcs) + len(std_refs)

    pct_low = round(100 * len(low) / len(feats), 1) if feats else 0.0
    blockers = []
    if len(feats) < 10:
        blockers.append(f"only {len(feats)} features (gate: >=10)")
    if total_sources < 3:
        blockers.append(f"only {total_sources} sources (gate: >=3)")
    if pct_low > 30:
        blockers.append(f"{pct_low}% low-confidence features (gate: <=30%)")
    if not wfs:
        blockers.append("no workflows")
    if not ents:
        blockers.append("no entities")
    if not roles:
        blockers.append("no roles")
    if not edges:
        blockers.append("no dependency edges")
    if not ints:
        blockers.append("no integrations")
    if unmapped:
        blockers.append(f"{len(unmapped)} features with no implementation-map entry")
    if not authoritative:
        blockers.append("no authoritative source")
    return {
        "domain": d, "maturity": fm["maturity"], "last_reviewed": fm["last_reviewed"],
        "features": len(feats), "by_classification": by_class,
        "entities": len(ents), "roles": len(roles), "workflows": len(wfs),
        "state_machines": sum(1 for w in wfs if w.get("state_machine")),
        "integrations": len(ints), "compliance": len(comp), "dependency_edges": len(edges),
        "requires_edges": sum(1 for e in edges if e["type"] == "requires"),
        "sources": total_sources, "domain_sources": len(srcs), "standard_refs": std_refs,
        "authoritative_sources": authoritative, "sources_on_disk": on_disk,
        "impl_status": st, "impl_available": sum(v for k, v in st.items() if k in IMPL_AVAILABLE),
        "pct_low_confidence": pct_low,
        "features_single_source": single, "features_low_confidence": low,
        "features_without_workflow": no_wf, "features_without_entities": no_ent,
        "features_without_users": no_user, "features_without_dependency_edge": no_dep,
        "features_unmapped": unmapped,
        "entities_without_relationships": ent_no_rel, "workflows_without_state_machine": wf_no_sm,
        "gate_blockers": blockers, "gate_pass": not blockers,
    }


def cmd_gaps(a: argparse.Namespace) -> None:
    ids = a.domains or [d for d in PRIORITY if d in domain_ids()]
    rows = [gate(d) for d in ids]
    if a.json:
        print(json.dumps({"schema": 1, "generated": date.today().isoformat(),
                          "generator": "tools/kb.py gaps", "domains": rows}, indent=2))
        return
    print("| # | Domain | Mat | Feat | Ent | Role | WF | SM | Intg | Comp | Dep | Src | Disk | Impl avail | Low-conf | Gate |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(rows, 1):
        print(f"| {i} | {r['domain']} | {r['maturity'][:4]} | {r['features']} | {r['entities']} | {r['roles']} | "
              f"{r['workflows']} | {r['state_machines']} | {r['integrations']} | {r['compliance']} | "
              f"{r['dependency_edges']} | {r['sources']} | {len(r['sources_on_disk'])} | {r['impl_available']} | "
              f"{r['pct_low_confidence']}% | {'PASS' if r['gate_pass'] else 'BLOCKED'} |")
    for r in rows:
        if a.verbose or not r["gate_pass"]:
            print(f"\n### {r['domain']} — {r['maturity']}")
            for b in r["gate_blockers"]:
                print(f"  blocker: {b}")
            for k in ("features_without_workflow", "features_without_entities", "features_without_users",
                      "features_without_dependency_edge", "features_unmapped", "features_low_confidence",
                      "entities_without_relationships", "workflows_without_state_machine"):
                v = r[k]
                if v:
                    shown = ", ".join(v[:6]) + (f" … (+{len(v) - 6})" if len(v) > 6 else "")
                    print(f"  {k}: {len(v)} — {shown}")
            print(f"  impl_status: {r['impl_status']}")


# ---------- query ----------

def load_features_index() -> dict:
    p = DOMAINS / "features.json"
    if not p.exists():
        sys.exit("domains/features.json missing: run `kb.py build`")
    return load(p)


def cmd_find(a: argparse.Namespace) -> None:
    data = load_features_index()
    rows = data["domain_features"] + ([{**f, "platforms": {}, "users": [], "entities": []} for f in data["shared"]]
                                      if not (a.role or a.entity or a.platform or a.integration or a.compliance) else [])
    for f in rows:
        if a.domain and f["domain"] != a.domain and a.domain not in f.get("domains", []):
            continue
        if a.tag and a.tag not in f.get("tags", []):
            continue
        if a.platform and not f["platforms"].get(a.platform):
            continue
        if a.role and a.role not in f["users"]:
            continue
        if a.entity and a.entity not in f["entities"]:
            continue
        if a.integration and a.integration not in f.get("integrations", []):
            continue
        if a.compliance and a.compliance not in f.get("compliance", []):
            continue
        if a.classification and f["classification"] != a.classification:
            continue
        if a.text and a.text.lower() not in (f["name"] + " " + f["description"]).lower():
            continue
        print(f"{f['id']:<48} {f['classification']:<14} impl={f['implementation_status']:<10} {f['name']}")


def dependency_graph() -> tuple[dict[str, list[tuple[str, str]]], dict[str, dict]]:
    graph: dict[str, list[tuple[str, str]]] = {}
    feats: dict[str, dict] = {f["id"]: {**f, "domain": "shared"} for f in load(SHARED)["features"]}
    for d in domain_ids():
        for f in load(DOMAINS / d / "feature-map.json")["features"]:
            feats[f["id"]] = {**f, "domain": d}
        for e in load(DOMAINS / d / "dependencies.json")["edges"]:
            graph.setdefault(e["from"], []).append((e["to"], e["type"]))
    return graph, feats


def cmd_order(a: argparse.Namespace) -> None:
    graph, feats = dependency_graph()
    roots = list(a.features)
    if a.domain:
        classes = set(a.classes.split(",")) if a.classes else {"core"}
        roots += [fid for fid, f in feats.items() if f["domain"] == a.domain and f.get("classification") in classes]
    unknown = [r for r in roots if r not in feats]
    if unknown:
        sys.exit(f"unknown features: {', '.join(unknown)}")
    why: dict[str, str] = {r: "selected" for r in roots}

    # Two passes, because `enhances` says "better with", not "needed first". It widens the
    # selection but must not constrain order: a mutual pair (kitchen_display *requires*
    # dine_in_orders, dine_in_orders *enhanced by* kitchen_display) is correct modelling and
    # must not read as an unbuildable cycle. Only `requires` cycles are real.
    selected: set[str] = set()
    stack = list(roots)
    while stack:
        n = stack.pop()
        if n in selected:
            continue
        selected.add(n)
        for m, t in graph.get(n, []):
            if t == "requires" or a.with_enhances:
                why.setdefault(m, f"{t} by {n}")
                stack.append(m)

    order: list[str] = []
    state: dict[str, int] = {}

    def visit(n: str) -> None:
        if state.get(n) == 2:
            return
        if state.get(n) == 1:
            sys.exit(f"requires cycle at {n} — fix dependencies.json")
        state[n] = 1
        for m, t in graph.get(n, []):
            if t == "requires" and m in selected:
                visit(m)
        state[n] = 2
        order.append(n)

    for r in sorted(selected):
        visit(r)
    shared_first = [n for n in order if n.startswith("shared.")] + [n for n in order if not n.startswith("shared.")]
    for i, n in enumerate(shared_first, 1):
        print(f"{i:>3}. {n:<48} [{why[n]}]")


def requires_closure(graph: dict[str, list[tuple[str, str]]], roots: list[str]) -> dict[str, list[str]]:
    """Features pulled in by requires-edges, mapped to the features that required them."""
    pulled: dict[str, list[str]] = {}
    stack = list(roots)
    while stack:
        n = stack.pop()
        for m, t in graph.get(n, []):
            if t != "requires" or m in roots:
                continue
            if m not in pulled:
                stack.append(m)
            pulled.setdefault(m, [])
            if n not in pulled[m]:
                pulled[m].append(n)
    return pulled


def impl_statuses() -> dict[str, str]:
    out = {f["id"]: impl_status_shared(f) for f in load(SHARED)["features"]}
    for d in domain_ids():
        out.update({m["feature"]: m["status"] for m in load(DOMAINS / d / "implementation-map.json")["mappings"]})
    return out


def cmd_matrix(a: argparse.Namespace) -> None:
    graph, feats = dependency_graph()
    requested = [r for r in (a.requested or "").split(",") if r]
    unknown = [r for r in requested if r not in feats]
    if unknown:
        sys.exit(f"unknown features: {', '.join(unknown)} (unmatched asks become custom.* in feature-selection.json)")
    if a.domain not in domain_ids():
        sys.exit(f"unknown domain {a.domain!r}")
    pulled = requires_closure(graph, requested)
    # Domain files rarely spell out auth edges; every product with users needs them.
    for fid in FOUNDATION:
        if fid not in requested:
            pulled.setdefault(fid, []).append("foundation")
    in_scope = set(requested) | set(pulled)
    enhancing = {m for n in in_scope for m, t in graph.get(n, []) if t == "enhances"}
    status = impl_statuses()
    rows = []
    order = requested + sorted(pulled) + sorted(fid for fid, f in feats.items()
                                                 if (f["domain"] == a.domain or fid in enhancing) and fid not in in_scope)
    for fid in order:
        f = feats[fid]
        cls = f.get("classification", "")
        if fid in requested:
            scope, reason = "IN_SCOPE", "requested"
        elif fid in pulled:
            scope, reason = "DEPENDENCY", "required by " + ", ".join(sorted(pulled[fid]))
        elif cls in {"core", "common"}:
            # The industry usually has it. Still not requested: propose, never assume.
            scope, reason = "DOMAIN_EXPECTED", f"{cls} for {a.domain}" + (" · enhances in-scope work" if fid in enhancing else "")
        elif fid in enhancing:
            scope, reason = "PROPOSED", f"{cls} · enhances in-scope work"
        else:
            scope, reason = "OPTIONAL", cls
        plat = [k for k, v in f.get("platforms", {}).items() if v]
        rows.append({"id": fid, "name": f["name"], "domain_classification": cls, "requested": fid in requested,
                     "scope": scope, "reason": reason, "required_by": sorted(pulled.get(fid, [])), "platforms": plat,
                     "real_time": f.get("real_time_relevance", ""), "ai": f.get("ai_relevance", ""),
                     "compliance": f.get("compliance", []),
                     "implementation": {"status": status.get(fid, "unknown"), "plan": "build"}})
    if a.json:
        print(json.dumps({"schema": 1, "project": a.project or "", "features": [
            {k: v for k, v in r.items() if k not in {"real_time", "ai", "compliance"}} for r in rows]}, indent=2))
        return
    print("| Feature | Scope | Domain class | Requested | Existing impl | Platforms | RT | AI | Compliance |")
    print("|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        print(f"| {r['name']} (`{r['id']}`) | {r['scope']} | {r['domain_classification']} | {'yes' if r['requested'] else 'no'} | "
              f"{r['implementation']['status']} | {', '.join(r['platforms'])} | {r['real_time']} | {r['ai']} | "
              f"{', '.join(r['compliance']) or '—'} |")


def cmd_check_sources(a: argparse.Namespace) -> None:
    """Cross-check sources/MANIFEST.json, catalog.json, each SOURCE.md, and what is on disk."""
    man = {s["path"]: s for s in load(KIT / "sources" / "MANIFEST.json")["sources"]}
    cat = {e["path"]: e for e in load(KIT / "catalog.json")["sources"]}
    rep = Report()

    for p in sorted(set(man) - set(cat)):
        rep.err(p, "in sources/MANIFEST.json but not catalog.json")
    for p in sorted(set(cat) - set(man)):
        rep.err(p, "in catalog.json but not sources/MANIFEST.json")

    for p in sorted(set(man) & set(cat)):
        for f in ("repo", "revision"):
            if man[p].get(f) != cat[p].get(f):
                rep.err(p, f"{f} differs: manifest {man[p].get(f)!r} vs catalog {cat[p].get(f)!r}")

    for p, s in sorted(man.items()):
        d = KIT / p
        rev = s.get("revision") or ""
        if len(rev) != 40 or not all(c in "0123456789abcdef" for c in rev):
            rep.err(p, f"revision {rev!r} is not a 40-char commit sha")
        sm = d / "SOURCE.md"
        if not sm.exists():
            rep.err(p, "no SOURCE.md")
        elif rev and rev not in sm.read_text(encoding="utf-8"):
            rep.err(p, "SOURCE.md does not carry the manifest revision")
        # A source with no license at all legitimately has no LICENSE.txt; anything else must.
        lic = (s.get("license") or "").lower()
        if not (d / "LICENSE.txt").exists() and "none" not in lic and lic:
            rep.err(p, "no LICENSE.txt")
        on_disk = (d / "source").is_dir()
        if s.get("fetch") is False and on_disk:
            rep.warn(p, 'fetch:false but source/ is on disk')
        if s.get("acquired") is False and on_disk:
            rep.warn(p, 'acquired:false but source/ is on disk - update the manifest')

    for sm in sorted((KIT / "sources").rglob("SOURCE.md")):
        rel = sm.parent.relative_to(KIT).as_posix()
        if rel not in man:
            rep.err(rel, "has a SOURCE.md but no manifest entry")
    for stub in sorted((KIT / "sources").rglob(".revision")):
        rep.err(stub.parent.relative_to(KIT).as_posix(),
                ".revision stub left behind - the revision belongs in SOURCE.md and MANIFEST.json")

    for w in rep.warnings:
        print("warning:", w)
    for e in rep.errors:
        print("error:", e)
    print(f"{len(rep.errors)} error(s), {len(rep.warnings)} warning(s)")
    sys.exit(1 if rep.errors else 0)


def cmd_check_selection(a: argparse.Namespace) -> None:
    graph, feats = dependency_graph()
    sel = load(Path(a.file))
    errors = []
    items = {f["id"]: f for f in sel.get("features", [])}
    active = {fid for fid, f in items.items() if f.get("scope") in {"IN_SCOPE", "DEPENDENCY"}}
    for fid, f in items.items():
        if fid not in feats and not fid.startswith("custom."):
            errors.append(f"{fid}: not in the catalog (use custom.<name> for asks without a match)")
        if f.get("requested") and f.get("scope") not in {"IN_SCOPE", "BLOCKED", "OUT_OF_SCOPE"}:
            errors.append(f"{fid}: requested but scope is {f.get('scope')}")
        if f.get("scope") not in SCOPES:
            errors.append(f"{fid}: unknown scope {f.get('scope')!r} (expected one of {', '.join(sorted(SCOPES))})")
        if f.get("scope") == "DEPENDENCY" and not f.get("required_by"):
            errors.append(f"{fid}: DEPENDENCY needs required_by")
        if f.get("scope") == "BLOCKED" and not f.get("blocked_by"):
            errors.append(f"{fid}: BLOCKED needs blocked_by")
    for fid in active:
        for m, t in graph.get(fid, []):
            if t == "requires" and m not in active and items.get(m, {}).get("scope") != "BLOCKED":
                errors.append(f"{fid}: requires {m}, which is not IN_SCOPE/DEPENDENCY")
    for e in errors:
        print("error:", e)
    print(f"{len(errors)} error(s)")
    sys.exit(1 if errors else 0)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("validate")
    v.add_argument("domains", nargs="*")
    v.add_argument("--quiet-warnings", action="store_true")
    sub.add_parser("build")
    f = sub.add_parser("find")
    for k in ("domain", "tag", "platform", "role", "entity", "integration", "compliance",
              "classification", "text"):
        f.add_argument(f"--{k}")
    o = sub.add_parser("order")
    o.add_argument("features", nargs="*")
    o.add_argument("--domain")
    o.add_argument("--classes", help="comma-separated classifications (default: core)")
    o.add_argument("--with-enhances", action="store_true")
    m = sub.add_parser("matrix")
    m.add_argument("domain")
    m.add_argument("--requested", help="comma-separated feature ids explicitly asked for")
    m.add_argument("--json", action="store_true", help="emit feature-selection.json-shaped output")
    m.add_argument("--project")
    sub.add_parser("check-sources")
    g = sub.add_parser("gaps")
    g.add_argument("domains", nargs="*", help="default: all domains in priority order")
    g.add_argument("--json", action="store_true")
    g.add_argument("--verbose", action="store_true", help="per-domain detail even when the gate passes")
    c = sub.add_parser("check-selection")
    c.add_argument("file", help="a project's feature-selection.json")
    a = ap.parse_args()
    if a.cmd == "validate":
        rep = validate(a.domains)
        if not a.quiet_warnings:
            for w in rep.warnings:
                print("warning:", w)
        for e in rep.errors:
            print("error:", e)
        print(f"{len(rep.errors)} error(s), {len(rep.warnings)} warning(s)")
        sys.exit(1 if rep.errors else 0)
    elif a.cmd == "build":
        build()
    elif a.cmd == "find":
        cmd_find(a)
    elif a.cmd == "order":
        cmd_order(a)
    elif a.cmd == "matrix":
        cmd_matrix(a)
    elif a.cmd == "gaps":
        cmd_gaps(a)
    elif a.cmd == "check-sources":
        cmd_check_sources(a)
    elif a.cmd == "check-selection":
        cmd_check_selection(a)


if __name__ == "__main__":
    main()
