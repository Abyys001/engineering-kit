# NACE Rev. 2.1 — Statistical classification of economic activities in the EU

- **Title**: Statistical classification of economic activities in the European Community, Rev. 2.1 (NACE Rev. 2.1)
- **Publisher**: Eurostat (Statistical Office of the European Union)
- **URL(s) actually downloaded**:
  - `https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/codelist/ESTAT/NACE_R2_1/latest` (SDMX-ML 2.1 Codelist, full structure with hierarchy annotations) → `NACE_R2_1_codelist_ESTAT_v13.2.xml`
- **License**: Eurostat's standard reuse policy for statistical data/metadata (CC BY 4.0 per the "Copyright notice and free re-use of data" page at `https://ec.europa.eu/eurostat/web/main/help/copyright-notice`, quote: "Reuse is authorised, provided the source is acknowledged... under the [Creative Commons Attribution 4.0 International (CC BY 4.0) licence](https://creativecommons.org/licenses/by/4.0/)"). SDMX registry content is Eurostat's own dissemination data and metadata, covered by the same policy.
- **Version**: NACE_R2_1, SDMX Codelist version 13.2, `LAST_UPDATED` annotation = 2026-09-17 (per the file's own header). This is the classification "adopted by Commission Delegated Regulation (EU) 2023/137" and in force for EU statistics from 2025 onward.
- **Retrieved**: 2026-09-26
- **File list**:
  - `NACE_R2_1_codelist_ESTAT_v13.2.xml` — 1.2 MB, raw SDMX-ML 2.1 Codelist as returned by the API, unmodified.
  - `build_csv.py` — stdlib-only converter (xml.etree) from the raw XML to a flat CSV.
  - `nace-rev2.1-structure.csv` — 1331 rows: `sdmx_id, ec_corporate_code, level, name_en, is_standard_code`. `level` 1=section (letter), 2=division, 3=group, 4=class; `AGG` = Eurostat dissemination aggregate (not part of the pure hierarchy, e.g. `TOTAL`, `G-I`).
- **What it's useful for**: Industry taxonomy for classifying kit domains/products by economic activity (`knowledge/industry-references/nace-domain-map.json`); not a feature catalog.
- **Redistribution/attribution**: CC BY 4.0 requires attribution to Eurostat as source. Any downstream reuse of this file or derivatives should credit "Eurostat, NACE Rev. 2.1" and link back to `https://ec.europa.eu/eurostat/web/nace`.

## Why this artifact and not RAMON/ShowVoc/an XLSX

Eurostat's legacy RAMON nomenclature server (`ec.europa.eu/eurostat/ramon/...LST_CLS_DLD...`) returns 404 for `NACE_REV2_1` — RAMON appears to be retired/redirected for this classification. The EU Vocabularies / ShowVoc dataset landing pages (`op.europa.eu/en/web/eu-vocabularies/eurostat`, `showvoc.op.europa.eu`) are JS single-page apps with no stable direct-download URL discoverable without a browser session. No public structure XLSX/CSV was found linked from `ec.europa.eu/eurostat/web/nace` or its correspondence-tables/guidance sub-pages (those pages are also JS-rendered; no static `.xlsx`/`.csv` href was present in the fetched HTML).

The Eurostat SDMX 2.1 API (`ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/...`), by contrast, is Eurostat's own documented, stable, machine-readable API (see `https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines/sdmx2-1/structure-queries`). The codelist ID for NACE Rev. 2.1 is `NACE_R2_1` (not `CL_NACE2_1`, which does not exist — confirmed by a `ERR_NOT_FOUND_4` SOAP fault). The returned codelist's own `<c:Name>` confirms it is "Statistical classification of economic activities in the European Community (NACE Rev. 2.1)", `agencyID="ESTAT"`, `isFinal="true"`. Each code carries a `LEVEL` annotation (1-4) and an `EC_CORPORATE_CODE` annotation giving the human-facing numeric NACE code (e.g. SDMX id `A0111` ↔ official code `0111`, i.e. NACE class 01.11) — this is the authoritative hierarchy, taken directly from the file, not inferred.

## Does Rev. 2.1 renumber section letters vs Rev. 2? Yes.

Comparing the section list extracted from this file against the well-known NACE Rev. 2 section list shows the single-letter section codes shift starting at J:

- Rev. 2: `J` = Information and communication (58 Publishing, 59 Motion picture, 60 Broadcasting, 61 Telecom, 62 Computer programming, 63 Information service) — one section covering 58-63.
- Rev. 2.1 (this file): `J` = "Publishing, broadcasting, and content production and distribution activities" (58-60 only); `K` = "Telecommunication, computer programming, consulting, computing infrastructure and other information service activities" (61-63) — the old J is split into two sections, which pushes every subsequent letter down by one:
  - old K (64-66, Financial/insurance) → new **L**
  - old L (68, Real estate) → new **M**
  - old M (69-75, Professional/scientific/technical) → new **N**
  - old N (77-82, Administrative/support) → new **O**
  - ... through old T (97-98) → new **U**, old U (99) → new **V**.

Numeric division/group/class codes are largely preserved for continuing activities (e.g. 62.01 Computer programming is still 62.01), but several classes were substantively redefined, most notably a new family of "intermediation service activities" codes for platform/marketplace business models (e.g. `47.91`/`47.92` replace Rev 2's `47.91` "Retail sale via mail order houses or via Internet" with a broader definition; `55.40`, `68.31`, `86.97` are new). **Do not assume a Rev 2 code and a Rev 2.1 code with the same digits mean the same thing** — verify against this file's `name_en` before using a code from memory or from older (Rev 2) documentation.

## Uncertain / not verified

- Whether SDMX codelist version 13.2 is the definitive "final" Rev 2.1 structure or will still receive corrections was not independently cross-checked against the EU Official Journal legal text (Commission Delegated Regulation (EU) 2023/137); the file's own `isFinal="true"` and status "NACE Rev. 2.1 classification is now official" (Eurostat news, 2023-02-10) support treating it as authoritative for kit purposes.
