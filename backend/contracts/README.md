# contracts

Contract lifecycle state machine: `draft → sent → in_progress → completed | declined | voided | expired`; `sent → draft` via `correct`. Terminal states are immutable. Original code; states are a starting point derived from the research — trim/extend per product (approvals, per-recipient states are separate machines).

Persist transitions with compare-and-set on `(id, state, version)`; see the trailing comment in `contract-state-machine.ts`. Final-signer race: lock the contract row (`FOR UPDATE`), count remaining signers, transition — exactly one transaction sees "last". Dedupe the completion job with `jobId = complete:<contractId>`, but treat DB state as the guarantee.
