#!/usr/bin/env python3
"""Extract a compact resource-type index from the official FHIR R6 (6.0.0-snapshot1)
definitions bundle.

Input:  profiles-resources.json (Bundle of StructureDefinition/OperationDefinition/
        CompartmentDefinition/CapabilityStatement, as downloaded from
        https://hl7.org/fhir/6.0.0-snapshot1/definitions.json.zip)
Output: ../../entities/fhir-r6-resources.json

For each StructureDefinition with kind == "resource" and derivation == "specialization"
(i.e. a base resource type, not a profile), record:
  - name, description (short - first sentence of StructureDefinition.description)
  - standards_status (R6 does not use numeric FMM; the closest analog is the
    structuredefinition-standards-status extension, e.g. "normative", "trial-use")
  - category (structuredefinition-category extension, e.g. "Clinical.Summary")
  - working_group (structuredefinition-wg extension)
  - key_elements: top-level (depth-1) elements from the snapshot, with
    cardinality (min..max) and type code(s)

stdlib only. Run from this directory: python3 extract.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "profiles-resources.json"
OUT = HERE.parent.parent / "entities" / "fhir-r6-resources.json"

CATEGORY_EXT = "http://hl7.org/fhir/StructureDefinition/structuredefinition-category"
STATUS_EXT = "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status"
WG_EXT = "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg"


def short_description(desc: str) -> str:
    if not desc:
        return ""
    m = re.match(r"(.+?[.!?])(\s|$)", desc.strip())
    return (m.group(1) if m else desc.strip())[:300]


def ext_value(sd: dict, url: str) -> str | None:
    for e in sd.get("extension", []):
        if e.get("url") == url:
            return e.get("valueString") or e.get("valueCode")
    return None


def key_elements(sd: dict) -> list[dict]:
    name = sd["name"]
    out = []
    for el in sd.get("snapshot", {}).get("element", []):
        path = el.get("path", "")
        if path == name or "." not in path:
            continue
        rest = path[len(name) + 1:]
        if "." in rest:
            continue  # only depth-1 (top-level) elements
        types = [t.get("code") for t in el.get("type", []) if t.get("code")]
        out.append({
            "name": rest,
            "cardinality": f"{el.get('min', '?')}..{el.get('max', '?')}",
            "type": types,
        })
    return out


def main() -> None:
    bundle = json.loads(SRC.read_text(encoding="utf-8"))
    resources = []
    for entry in bundle.get("entry", []):
        sd = entry["resource"]
        if sd.get("resourceType") != "StructureDefinition":
            continue
        if sd.get("kind") != "resource" or sd.get("derivation") != "specialization":
            continue
        resources.append({
            "name": sd["name"],
            "description": short_description(sd.get("description", "")),
            "standards_status": ext_value(sd, STATUS_EXT),
            "category": ext_value(sd, CATEGORY_EXT),
            "working_group": ext_value(sd, WG_EXT),
            "key_elements": key_elements(sd),
        })
    resources.sort(key=lambda r: r["name"])

    out_doc = {
        "schema": 1,
        "source": "std:fhir-r6",
        "source_file": "knowledge/standards/fhir-r6/profiles-resources.json",
        "generated_by": "knowledge/standards/fhir-r6/extract.py",
        "note": "R6 (6.0.0-snapshot1) is pre-release; most production FHIR servers implement R4 (4.0.1). R6 does not carry numeric FMM levels - standards_status (normative/trial-use/informative) is the closest analog in this snapshot.",
        "last_reviewed": "2026-09-27",
        "resource_count": len(resources),
        "resources": resources,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out_doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {len(resources)} resources -> {OUT}")


if __name__ == "__main__":
    main()
