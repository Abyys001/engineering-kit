#!/usr/bin/env python3
"""Convert the official Eurostat SDMX-ML NACE_R2_1 codelist into a flat CSV.

Input:  NACE_R2_1_codelist_ESTAT_v13.2.xml (raw SDMX-ML 2.1 Codelist, as downloaded)
Output: nace-rev2.1-structure.csv

stdlib only (xml.etree.ElementTree). Run from this directory:
    python3 build_csv.py
"""
from __future__ import annotations

import csv
import xml.etree.ElementTree as ET
from pathlib import Path

NS = {
    "m": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message",
    "s": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure",
    "c": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common",
}

HERE = Path(__file__).resolve().parent
SRC = HERE / "NACE_R2_1_codelist_ESTAT_v13.2.xml"
OUT = HERE / "nace-rev2.1-structure.csv"


def main() -> None:
    tree = ET.parse(SRC)
    root = tree.getroot()
    codelist = root.find(".//s:Codelist", NS)
    rows = []
    for code in codelist.findall("s:Code", NS):
        sdmx_id = code.get("id")
        name_en = code.findtext('c:Name[@{http://www.w3.org/XML/1998/namespace}lang="en"]', namespaces=NS)
        level = None
        ec_code = None
        is_standard = "N"
        for ann in code.findall(".//c:Annotation", NS):
            atype = ann.findtext("c:AnnotationType", namespaces=NS)
            atitle = ann.findtext("c:AnnotationTitle", namespaces=NS)
            if atype == "LEVEL":
                level = atitle
            elif atype == "EC_CORPORATE_CODE":
                ec_code = atitle
            elif atype == "IS_STANDARD_CODE":
                is_standard = atitle or "N"
        rows.append({
            "sdmx_id": sdmx_id,
            "ec_corporate_code": ec_code or "",
            "level": level or "",
            "name_en": name_en or "",
            "is_standard_code": is_standard,
        })

    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["sdmx_id", "ec_corporate_code", "level", "name_en", "is_standard_code"])
        w.writeheader()
        w.writerows(rows)

    print(f"wrote {len(rows)} rows -> {OUT}")


if __name__ == "__main__":
    main()
