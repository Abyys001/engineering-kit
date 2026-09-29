# audit-log

Per-contract, hash-chained, append-only event log. **Origin:** original. Complements the kit's Refine audit-log provider contract (`sources/dashboards/refine`), which is UI-side.

## Tradeoff
Hash chaining is tamper *evidence*. It does not stop a DB admin rewriting the whole chain, and truncation of the tail is invisible unless the head hash is anchored elsewhere (put it in the completion certificate, or a third-party timestamp). Prevention is the database's job. Chain **per contract**, never globally: a global chain serializes every write.

## Postgres hardening (apply in your migration)
```sql
REVOKE UPDATE, DELETE, TRUNCATE ON audit_events FROM app_role;
CREATE FUNCTION audit_events_immutable() RETURNS trigger LANGUAGE plpgsql AS
$$ BEGIN RAISE EXCEPTION 'audit_events is append-only'; END $$;
CREATE TRIGGER audit_events_no_mutation BEFORE UPDATE OR DELETE ON audit_events
  FOR EACH ROW EXECUTE FUNCTION audit_events_immutable();
CREATE UNIQUE INDEX audit_events_chain ON audit_events (contract_id, seq);
```
Append inside the transaction holding `SELECT … FROM contracts WHERE id = $1 FOR UPDATE`; `unique (contract_id, seq)` is the backstop.
