# Hospitality sources

Sources cited in this domain's provenance fields.

| ID | Title | Type | License | Retrieved | Local path |
|---|---|---|---|---|---|
| `frappe-hospitality` | [Frappe Hospitality](https://github.com/frappe/hospitality) | implementation | GPL-3.0 | 2026-09-26 | `sources/domains/frappe-hospitality/source` |
| `qloapps` | [QloApps (PrestaShop-based hotel booking engine + channel manager)](https://github.com/Qloapps/QloApps) | implementation | OSL-3.0 | 2026-09-26 | — |
| `opentravel-alliance` | [OpenTravel Alliance (OTA) message specifications](https://opentravel.org/category/specification/) | authoritative | OTA user license — free to use, may not redistribute/modify the specification text | 2026-09-26 | — |
| `htng` | [HTNG (Hotel Technology Next Generation) interface specifications](https://htng.org/) | authoritative | HTNG member/vendor-gated specification access | 2026-09-26 | — |
| `pci-dss` | [PCI Data Security Standard v4.0.1](https://www.pcisecuritystandards.org/document_library/) | authoritative | PCI SSC copyright; free to read/download with registration | 2026-09-26 | — |
| `eu-gdpr` | [EU General Data Protection Regulation (Regulation (EU) 2016/679)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679) | authoritative | EU public document, free reuse per Commission Decision 2011/833/EU | 2026-09-26 | — |
| `wikipedia-night-audit` | [Wikipedia: Night audit](https://en.wikipedia.org/wiki/Night_audit) | secondary | CC BY-SA 4.0 | 2026-09-26 | — |
| `wikipedia-housekeeping` | [Wikipedia: Housekeeping](https://en.wikipedia.org/wiki/Housekeeping) | secondary | CC BY-SA 4.0 | 2026-09-26 | — |
| `wikipedia-yield-management` | [Wikipedia: Yield management](https://en.wikipedia.org/wiki/Yield_management) | secondary | CC BY-SA 4.0 | 2026-09-26 | — |
| `wikipedia-loyalty-program` | [Wikipedia: Loyalty program](https://en.wikipedia.org/wiki/Loyalty_program) | secondary | CC BY-SA 4.0 | 2026-09-26 | — |
| `wikipedia-customer-review` | [Wikipedia: Customer review](https://en.wikipedia.org/wiki/Customer_review) | secondary | CC BY-SA 4.0 | 2026-09-26 | — |
| `wikipedia-hotel` | [Wikipedia: Hotel](https://en.wikipedia.org/wiki/Hotel) | secondary | CC BY-SA 4.0 | 2026-09-26 | — |

## Notes

- **`frappe-hospitality`** (2003ff8db7d7fbc453a9d14da0f971b9186a0b4b): Reference-only (GPL-3.0). ERPNext hotel module: Hotel Room, Hotel Room Type, Hotel Room Amenity, Hotel Room Pricing (+Item/Package), Hotel Room Reservation (+Item), Hotel Settings doctypes. Shared with domains/restaurant.
- **`qloapps`** (develop branch, 2026-09-26 snapshot): Not cloned (inspected via gh api git tree + raw.githubusercontent.com; 132MB repo, PrestaShop e-commerce core + hotelreservationsystem module). OSL-3.0 verified from actual LICENSE.md — a network/external-deployment copyleft license (section 5), treated with the same caution as AGPL: reference-only, no code copied. modules/hotelreservationsystem/classes/ has ~35 Hotel*/RoomType*/ServiceProduct* classes covering branches, room types, rooms, feature-based rate pricing + restrictions, booking detail + status history (Assigned/CheckedIn/CheckedOut/NoShow/Cancelled), advanced payment, refund rules, connected rooms, channel manager + ARI (Availability-Rate-Inventory) webservice, add-on service products, and PDF booking vouchers.
- **`opentravel-alliance`** (public mirror through 2017B; current releases through 2024A are member/download-gated): Verified organizational facts and access status only (public mirror stops at 2017B; the OpenTravel site's download form lists newer releases behind registration). Did not obtain and read the full current message schema text in this pass, so this source is NOT treated as sufficient alone for 'high' confidence on any feature — cited for terminology (e.g. OTA_HotelResRQ/RS, availability/rate/inventory message families) that is independently well documented in secondary literature, not for message-level detail.
- **`htng`** (active as of January 2025 release cycle; organization merged into AHLA in 2022): Verified via secondary reporting (Hospitality Technology, AltexSoft, Wikipedia) that HTNG is still active and that its interfaces frequently carry OpenTravel message payloads; did not access gated specification text directly. Cited for the channel-manager/PMS-interface concept only, at low/medium confidence.
- **`pci-dss`** (4.0.1): Card payment security standard; applies to any property accepting card payments or deposits.
- **`eu-gdpr`** (consolidated text): EU-jurisdiction personal data protection requirement for guest profile data (identity documents, contact details, stay history).
- **`wikipedia-night-audit`** (2026-09-26 snapshot): General background for the night-audit process; not found in either inspected implementation.
- **`wikipedia-housekeeping`** (2026-09-26 snapshot): General background for housekeeping/room-turnover status tracking; not found in either inspected implementation as a dedicated module.
- **`wikipedia-yield-management`** (2026-09-26 snapshot): General background for demand-based dynamic pricing, distinct from the rule/season-based rate plans both implementations have.
- **`wikipedia-loyalty-program`** (2026-09-26 snapshot): General background for guest loyalty/rewards; not present in either inspected implementation.
- **`wikipedia-customer-review`** (2026-09-26 snapshot): General background for guest review collection; not present in either inspected implementation.
- **`wikipedia-hotel`** (2026-09-26 snapshot): General background only; no single authoritative cross-jurisdiction source on guest ID/passport registration requirements was found in this pass.
