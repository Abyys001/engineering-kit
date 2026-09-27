# GS1 EPCIS 2.0 and Core Business Vocabulary (CBV)

- **Title**: EPCIS (Electronic Product Code Information Services) and CBV (Core Business Vocabulary), development repository
- **Publisher**: GS1
- **URL(s) actually downloaded**: `https://github.com/gs1/EPCIS` (sparse, shallow clone; `.claude/`, `CLAUDE.md`, `AGENTS.md`, `.mcp.json`, `.cursor/`, `.github/copilot-instructions.md` excluded per policy)
- **Git SHA**: `6f71468231838e424bb5dfa836e006e8dc69615c` (default branch at retrieval time)
- **License**: No OSI license file; the repo carries a GS1 **Disclaimer** (file `Disclaimer`, reproduced in full below) instead of a code license, consistent with GS1's IP Policy model (royalty-free/RAND licensing to "Necessary Claims" for participants, standard provided "AS IS"). Preserve this disclaimer verbatim wherever content from this repo is redistributed.
- **Version**: Repository content is labelled "Draft files being shared for EPCIS 2.0 development" (`README.md`) and includes a `public_review_2_1/` folder — i.e. this mirrors GS1's EPCIS/CBV 2.0 **development and public-review** artifacts, not a separately re-hosted "final ratified PDF". The event-type names, CBV bizstep/disposition vocabularies, and JSON-LD/schema shapes captured here match the ratified EPCIS 2.0 / CBV 2.0 standard (GS1 ratified EPCIS/CBV 2.0 in 2022); no substantive vocabulary drift after public review was found. If exact clause numbers of the ratified PDF are needed, cross-check against GS1's published PDF at gs1.org rather than this repo.
- **Retrieved**: 2026-09-26
- **File list** (representative — full listing via `find` in the folder):
  - `Ontology/EPCIS.ttl`, `Ontology/EPCIS.jsonld`, `Ontology/EPCIS-SHACL.ttl` — the EPCIS ontology/schema, machine-readable entry points for event/field structure.
  - `Ontology/CBV.ttl`, `Ontology/CBV.jsonld` — the Core Business Vocabulary ontology.
  - `JSON-LD-Context/cbv-context-bizstep.jsonld`, `cbv-context-disposition.jsonld`, `cbv-context-biztransaction-type.jsonld`, `cbv-context-sourcedest-type.jsonld`, `cbv-context-error-reason.jsonld`, `cbv-context-component.jsonld` — CBV code lists as JSON-LD contexts (machine-readable, one file per vocabulary).
  - `epcis-context.jsonld`, `epcis-context-simple.jsonld` — EPCIS JSON-LD contexts.
  - `EPCIS-JSON-Schema.json`, `JSON-Schema/EPCIS-Document-JSON-Schema.json`, `JSON-Schema/EPCIS-Event-JSON-Schema.json` — JSON Schema definitions.
  - `XSD/EPCglobal-epcis-2_0.xsd` and related — XML Schema (legacy binding).
  - `REST Bindings/openapi.yaml` / `openapi.json` — the EPCIS REST API as an OpenAPI document.
  - `Disclaimer`, `LICENSE`, `README.md`.
  - Total size: 8.9 MB (diagrams as PNG kept — small; no large binaries).
- **What it's useful for**: Supply-chain event model and vocabulary (what/when/where/why/how) for the `logistics`/`manufacturing`/`ecommerce` kit domains.
- **Redistribution/attribution notes**: preserve the `Disclaimer` file text (below) and the "GS1® and the GS1 logo are registered trademarks of GS1 AISBL" notice wherever content is copied out.

## GS1 Disclaimer (verbatim, from the repo's `Disclaimer` file)

> GS1®, under its IP Policy (https://www.gs1.org/standards/ip), seeks to avoid uncertainty regarding intellectual property claims by requiring the participants in the Work Group that developed the GS1 Standards to agree to grant to GS1 members a royalty-free licence or a RAND licence to Necessary Claims, as that term is defined in the GS1 IP Policy. Furthermore, attention is drawn to the possibility that an implementation of one or more features of the GS1 Standards may be the subject of a patent or other intellectual property right that does not involve a Necessary Claim. Any such patent or other intellectual property right is not subject to the licencing obligations of GS1. Moreover, the agreement to grant licences provided under the GS1 IP Policy does not include IP rights and any claims of third parties who were not participants in the Work Group.
>
> Accordingly, GS1 recommends that any organization developing an implementation designed to be in conformance with GS1 Standards should determine whether there are any patents that may encompass a specific implementation that the organisation is developing in compliance with the relevant GS1 Standards and whether a licence under a patent or other intellectual property right is needed. Such a determination of a need for licencing should be made in view of the details of the specific system designed by the organisation in consultation with their own patent counsel.
>
> THE GS1 STANDARDS ARE PROVIDED "AS IS" WITH NO WARRANTIES WHATSOEVER, INCLUDING ANY WARRANTY OF MERCHANTABILITY, NONINFRINGMENT, FITNESS FOR PARTICULAR PURPOSE, OR ANY WARRANTY OTHER WISE ARISING OUT OF THE GS1 STANDARDS. GS1 disclaims all liability for any damages arising from use or misuse of the GS1 Standards, whether special, indirect, consequential, or compensatory damages, and including liability for infringement of any intellectual property rights, relating to use of information in or reliance upon the GS1 Standards.
>
> GS1 retains the right to make changes to the GS1 Standards at any time, without notice. GS1 makes no warranty for the use of the GS1 Standards and assumes no responsibility for any errors which may appear in the GS1 Standards, nor does it make a commitment to update the information contained herein.
>
> GS1 and the GS1 logo are registered trademarks of GS1 AISBL.

See `SUMMARY.md` for event types, dimensions, CBV vocabularies, and the machine-readable entry points.
