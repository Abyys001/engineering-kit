# Chatwoot

| Field | Value |
|---|---|
| Source URL | https://github.com/chatwoot/chatwoot |
| GitHub repository | `chatwoot/chatwoot` |
| Category | domains/support |
| License | MIT — root `LICENSE` (verbatim: "Content outside of the above mentioned directories or restrictions above is available under the 'MIT Expat' license"); the `enterprise/` directory is explicitly carved out ("licensed under the license defined in `enterprise/LICENSE`") and is **not** covered by the MIT grant |
| Author / organization | Chatwoot Inc. |
| Acquired | 2026-09-27 |
| Revision | `b8eb7766f2735d6e3bf5ed3a69cf453b289a4411` (develop — chatwoot has no `main` branch; `develop` is its default/HEAD branch, confirmed via `git ls-remote --symref`) |
| Attribution required | MIT notice retention if code were reused (it is not — reference-only) |
| Status | extraction-safe — for the paths actually checked out (`app/models`, `app/controllers/api/v1`, `app/controllers/api/v2`, `db/schema.rb`, root `LICENSE`/`README.md`). License verified directly from the root `LICENSE` file in this checkout, which is the MIT Expat license for everything except `enterprise/`. `enterprise/` was excluded from the sparse checkout entirely and is confirmed absent from disk. |

## Useful for
- **Ticket/conversation model** (`app/models/conversation.rb`): `enum status: { open: 0, resolved: 1, pending: 2, snoozed: 3 }`, `enum priority: { low, medium, high, urgent }`, `belongs_to :assignee` (User), `:team`, `:campaign`; `sla_policy_id` column present on the model/schema. Grounds `support.ticket_management` and `support.assignment`.
- **Queues/inboxes**: `app/models/inbox.rb` (polymorphic `belongs_to :channel`, one inbox per channel) and `app/models/team.rb` (`allow_auto_assign`, has_many members/conversations). Grounds `support.ticket_queues`.
- **Channels** (`app/models/channel/*.rb`): `Email`, `WebWidget`, `Sms`, `TwilioSms`, `FacebookPage`, `Instagram`, `Line`, `Telegram`, `Tiktok`, `TwitterProfile`, `Whatsapp`, `Api`. Grounds `support.email_channel`, `support.chat_channel`, and (via `Inbox`'s polymorphic `channel_type` plus `ContactInbox` linking many channels to one `Contact`) `support.multichannel_unification`. There is **no** core voice/phone channel model in this list — `app/models/enterprise/call.rb`-style call handling is enterprise-only and was not present in this checkout, so it does not ground `support.voice_channel`.
- **Knowledge base** (`app/models/article.rb`, `portal.rb`, `category.rb`, `folder.rb`): `Article` belongs to `Portal` and optional `Category`, has draft/published `status`, `locale`. `Portal` has `custom_domain`, `config` (jsonb). Grounds `support.knowledge_base`, and (via `Portal` + `app/controllers/api/v1/widget/conversations_controller.rb#index`, which lets a contact fetch their own conversation) partially grounds `support.customer_portal`.
- **Macros / canned responses** (`app/models/macro.rb`, `canned_response.rb`): `Macro` has `visibility` (personal/global) and a JSONB `actions` array (`send_message`, `add_label`, `assign_team`, `assign_agent`, `change_status`, `resolve_conversation`, `send_webhook_event`, `add_private_note`, …). `CannedResponse` is a separate, simpler `short_code` → `content` template model. Grounds `support.macros_canned_responses`.
- **CSAT** (`app/models/csat_survey_response.rb`): `rating` (1-5, validated), `feedback_message`, `csat_review_notes`, linked to `conversation`/`message`/`contact`/`assigned_agent`. Grounds `support.csat_surveys`.
- **Internal notes** (`app/models/message.rb`): boolean `private` column plus `enum message_type: { incoming, outgoing, activity, template }`; `scope :chat` explicitly filters `private: false`. Grounds `support.internal_notes`. (There is also a separate `Note` model, but it is `belongs_to :contact` — a contact-level note, not a conversation/ticket-level one — so `Message.private` is the actual internal-notes mechanism for tickets.)
- **Tags** (`app/models/label.rb`): account-scoped `Label` with `title`/`color`, joined to conversations via `acts_as_taggable`-style tagging (`account.conversations.tagged_with(title)`). Grounds `support.tagging_categorization`.
- **Business hours** (`app/models/working_hour.rb`): per-`inbox` `day_of_week`, `open_hour`/`open_minutes`, `close_hour`/`close_minutes`, `open_all_day`/`closed_all_day` booleans, `.open_now?`/`.open_at?`. This is core (not enterprise) and grounds `support.business_hours` directly — stronger grounding here than the domain's existing zammad-only citation.
- **Automation** (`app/models/automation_rule.rb`): core, fully-automatic rule engine — `event_name`, JSONB `conditions`, JSONB `actions` (`send_message`, `add_label`, `assign_team`, `change_status`, `send_webhook_event`, …), optional `execution_delay`. Grounds `support.ticket_automation_rules` — and more strongly than the domain's existing note (which only cites the agent-triggered `Macro` for chatwoot; `AutomationRule` is chatwoot's actual trigger-based equivalent to zammad's `Trigger`).
- **Reporting** (`app/controllers/api/v2/accounts/{reports,live_reports,summary_reports,year_in_reviews}_controller.rb`): confirmed core, not under `enterprise/`. Grounds `support.reporting_analytics`.
- **SLA — partial/negative finding**: `db/schema.rb` (core) has `conversations.sla_policy_id`, a full `applied_slas` table, and `sla_events`/`sla_policies` tables — so the SLA *data model* is present in the open schema. However, the ActiveRecord classes that implement it (`SlaPolicy`, `AppliedSla`, `SlaEvent`) live under `enterprise/app/models/` (verified via the GitHub API before excluding `enterprise/` from the sparse checkout) and are **not** in this checkout — they are enterprise-licensed, not MIT. The one core artifact touching SLA is `app/models/concerns/sla_activity_message_handler.rb`, which only builds an activity-message string when `sla_policy_id` changes; it does not implement escalation or breach detection. This grounds `support.sla_management` narrowly (schema-level only, via `db/schema.rb`) and does **not** ground `support.escalation` (the actual escalation/breach logic is enterprise-only and out of this checkout).

## Where things live
- `source/app/models/` — all core ActiveRecord models (flat, plus `channel/`, `concerns/`, `integrations/` subdirectories).
- `source/app/controllers/api/v1/accounts/` — agent-facing REST API (conversations, contacts, inboxes, teams, macros, canned_responses, articles, categories, portals, automation_rules, csat_survey_responses, …).
- `source/app/controllers/api/v1/widget/` — unauthenticated/contact-facing widget API (`conversations_controller.rb`, `contacts_controller.rb`, `messages_controller.rb`).
- `source/app/controllers/api/v2/accounts/` — reporting endpoints only (`reports_controller.rb`, `live_reports_controller.rb`, `summary_reports_controller.rb`, `year_in_reviews_controller.rb`).
- `source/db/schema.rb` — full core DB schema (1,738 lines), including tables whose owning model classes are enterprise-only (`applied_slas`, `sla_policies`, `sla_events`).
- `source/LICENSE`, `source/README.md` — root license and readme.

## Do not copy
- No Chatwoot code is copied into the kit; this clone is reference-only for domain-model research (`domains/support`), per the research brief.
- `enterprise/` was deliberately excluded from the sparse checkout and is confirmed absent on disk — never fetch or reference it for this domain; it is under a separate commercial license (`enterprise/LICENSE`, viewed via GitHub's raw API, not present in this checkout), not MIT.

## Notes
- Chatwoot has no `main` branch; the sparse checkout pins the SHA directly (`git fetch --depth 1 origin <sha>`), so the `branch: develop` field in `sources/MANIFEST.json` is informational/fallback only.
- Sparse-checkout gotcha found and fixed during acquisition: unanchored patterns (`LICENSE`, `README.md`, no leading slash) are gitignore-style basename matches in git's non-cone sparse-checkout mode and initially leaked `enterprise/LICENSE`, `spec/fixtures/data_import/freshdesk/README.md`, and `tests/playwright/README.md` into the checkout. Fixed by anchoring both patterns with a leading slash (`/LICENSE`, `/README.md`) in `sources/MANIFEST.json` and re-fetching with `FORCE=1`. Final checkout (1.1M) contains only `LICENSE`, `README.md`, `app/models/**`, `app/controllers/api/v1/**`, `app/controllers/api/v2/**`, `db/schema.rb` — verified by `find sources/domains/chatwoot/source -type f` and by `find … -iname "*enterprise*"` returning nothing.
- No `node_modules`, JavaScript/Vue frontend, or build artifacts were pulled in; checkout is Ruby source (models/controllers) plus one generated schema file.
