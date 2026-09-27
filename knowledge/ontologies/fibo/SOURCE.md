# FIBO — Financial Industry Business Ontology

- **Title**: Financial Industry Business Ontology (FIBO)
- **Publisher**: EDM Council (Enterprise Data Management Council)
- **URL(s) actually downloaded**: `https://github.com/edmcouncil/fibo` (sparse, shallow clone; `.claude/`, `CLAUDE.md`, `AGENTS.md`, `.mcp.json`, `.cursor/`, `.github/copilot-instructions.md` excluded per policy)
- **Git SHA**: `08322e9ec08a32f37038178e10dc12e7a7de6ab5` (default branch `master` at retrieval time)
- **License**: MIT. Verified from `LICENSE` in the repo root: "The MIT License (MIT) — Copyright (c) 2020 Enterprise Data Management Council ... Permission is hereby granted, free of charge...". Individual `.rdf` files additionally embed their own copyright/license block in the `owl:Ontology` header (e.g. "Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc." plus the same MIT permission text) — preserve that header if a file is copied elsewhere.
- **Version**: `versionIRI` in `AboutFIBOProd.rdf` is dated `20260701` (2026-07-01 quarterly production release).
- **Retrieved**: 2026-09-26
- **File list**: full sparse checkout of the repo (RDF/OWL/TTL ontology modules) minus `etc/source/` (62 MB of CameoMagicDraw/Sparx Enterprise Architect binary model files — build tooling, not ontology content, dropped to stay small) and `.git/` (removed after recording the SHA above). Final size: 15 MB, 295 `.rdf` files across 11 top-level domain directories (`ACTUS BE BP CAE DER EXMP FBC FND IND LOAN MD SEC`) plus `etc/` (vocabulary/testing/CI config, kept — small) and root metadata/about files.
- **What it's useful for**: Financial domain terminology, entities, and relationships (currency, accounts, parties, payments, contracts, exchange rates) for the `fintech`/`exchange` kit domains.
- **Redistribution/attribution notes**: MIT requires the copyright notice and permission text to be preserved in copies — see `LICENSE` and per-file `owl:Ontology` headers.

See `SUMMARY.md` for the module map and the key classes most relevant to a fintech/currency-exchange product.
