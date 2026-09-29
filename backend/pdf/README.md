# pdf

Field geometry for signing. Stored form = fractions of the CropBox in displayed (post-`/Rotate`) orientation, top-left origin. `toPdfRect` / `toRelativeRect` convert for server-side stamping. Tested for all four rotations and an offset CropBox.

## Library split (do not mix)
| Concern | Where | Choice |
|---|---|---|
| Render, thumbnails, field placement | browser | `pdfjs-dist` (Apache-2.0) via `react-pdf` (MIT) |
| Stamp / merge / flatten | server | `@cantoo/pdf-lib` (MIT; `pdf-lib` is unmaintained since 2022) |
| Certificate PDF | server | `pdfkit` (MIT) |
| PAdES + RFC 3161 | server | `@signpdf/signpdf` (MIT) + `pkijs` (BSD-3); keys in KMS/HSM. Never `node-forge` (GPL option, CVE history) |
| Rejected | | `mupdf` (AGPL), Syncfusion (commercial), Chromium for certificates |

Not implemented here: stamping, sealing, certificate rendering — no fake signatures. Preflight uploads (magic bytes, `qpdf --check`, reject `/JavaScript`, `/OpenAction`, `/Launch`, `/EmbeddedFiles`), parse in a worker with time/memory limits. Any change after a cryptographic signature must be an incremental update.
