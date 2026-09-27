#!/usr/bin/env python3
"""Domain knowledge base tooling for the engineering-kit (stdlib only).

  kb.py validate [domain ...]        check schemas, references, cycles, paths
  kb.py build                        regenerate domains/{catalog,features,search-index}.json and INDEX.md
  kb.py find [--domain D] [--tag T] [--platform P] [--role R] [--entity E]
             [--classification C] [--text S]
  kb.py order FEATURE_ID ... [--with-enhances]
                                     dependency closure in build order
  kb.py order --domain D [--classes core,common]
  kb.py matrix DOMAIN --requested ID,ID [--json]
                                     starting feature matrix with scope levels
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
IMPL_STATUS = ["unknown", "reference", "partial", "curated", "tested", "production_ready"]
MATURITY = {"researching", "partial", "curated", "reviewed"}
DEP_TYPES = {"requires", "enhances"}
REL_TYPES = {"has_one", "has_many", "belongs_to", "many_to_many"}
EXPERIENCES = {"customer", "staff", "management", "administration", "partner", "system"}
COMPLIANCE_KINDS = {"regulation", "standard", "certification", "guideline"}
PLATFORM_KEYS = ["web", "mobile", "admin", "customer_portal", "backend", "ai", "real_time"]
IMPL_KEYS = ["web", "backend", "mobile", "ai"]
FOUNDATION = ["shared.auth", "shared.users", "shared.permissions"]


def load(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def domain_ids() -> list[str]:
    return sorted(p.name for p in DOMAINS.iterdir()
                  if p.is_dir() and not p.name.startswith("_") and (p / "feature-map.json").exists())


def has_files(rel: str) -> bool:
    p = KIT / rel
    return p.is_file() or (p.is_dir() and any(f.is_file() for f in p.rglob("*")))


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
            if m.get("status") in {"partial", "curated", "tested", "production_ready"} and not paths:
                rep.err(w, f"status {m['status']} needs implementation paths")
            if m.get("status") == "reference" and not m.get("references"):
                rep.err(w, "status reference needs references")
        for fid in dfeats - mapped:
            rep.warn(f"{d}/impl", f"{fid} has no implementation-map entry")
    return rep


# ---------- build ----------

def impl_status_shared(f: dict) -> str:
    return "partial" if any(has_files(p) for p in f.get("kit_paths", [])) else "unknown"


def build() -> None:
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
        roles = load(DOMAINS / d / "roles.json")["roles"]
        ents = load(DOMAINS / d / "entities.json")["entities"]
        wfs = load(DOMAINS / d / "workflows.json")["workflows"]
        comp = load(DOMAINS / d / "compliance.json")["items"]
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
            "compliance_count": len(comp),
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


# ---------- query ----------

def load_features_index() -> dict:
    p = DOMAINS / "features.json"
    if not p.exists():
        sys.exit("domains/features.json missing: run `kb.py build`")
    return load(p)


def cmd_find(a: argparse.Namespace) -> None:
    data = load_features_index()
    rows = data["domain_features"] + ([{**f, "platforms": {}, "users": [], "entities": []} for f in data["shared"]]
                                      if not (a.role or a.entity or a.platform) else [])
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
    order: list[str] = []
    state: dict[str, int] = {}
    why: dict[str, str] = {r: "selected" for r in roots}

    def visit(n: str) -> None:
        if state.get(n) == 2:
            return
        if state.get(n) == 1:
            sys.exit(f"cycle at {n}")
        state[n] = 1
        for m, t in graph.get(n, []):
            if t == "requires" or a.with_enhances:
                why.setdefault(m, f"{t} by {n}")
                visit(m)
        state[n] = 2
        order.append(n)

    for r in roots:
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
        elif cls in {"core", "common"} or fid in enhancing:
            scope, reason = "PROPOSED", f"{cls} for {a.domain}" + (" · enhances in-scope work" if fid in enhancing else "")
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
    for k in ("domain", "tag", "platform", "role", "entity", "classification", "text"):
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
    elif a.cmd == "check-selection":
        cmd_check_selection(a)


if __name__ == "__main__":
    main()
