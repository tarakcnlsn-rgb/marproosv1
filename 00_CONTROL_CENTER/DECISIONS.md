# DECISIONS

**Purpose:** Authoritative log of owner-approved material decisions and Class C approvals. This file answers: "What was decided, by whom, and why?"
**Type:** Append-only log — Tier 1, not semantically versioned — Git history is the record. Entries are added per `APPROVAL_POLICY.md` §5. Existing entries are never edited; corrections are added as new superseding entries.
**Authority:** Level 5, per `PROJECT_CONSTITUTION.md` §5. A decision recorded here outranks state files and task prompts.

---

## Entry Format

```md
### D-### — <short title>
**Date:** YYYY-MM-DD
**Class:** C / Material decision
**Decision:** <what was approved, exact scope>
**Reason:** <why, one or two sentences>
**Affected files:** <paths>
**Conditions / limits:** <any>
**Approved by:** Tara Nelson
**Status:** ACTIVE / SUPERSEDED by D-###
```

---

## Decisions

### D-001 — Ratify Project Constitution v1.0.0
**Date:** 2026-07-14
**Class:** C / Constitutional
**Decision:** Ratify `00_GOVERNANCE/PROJECT_CONSTITUTION.md` v1.0.0 as supreme project authority. Status flips `PROPOSED` → `ACTIVE` at the Phase 0 commit.
**Reason:** Establishes governing law before any production work.
**Affected files:** `00_GOVERNANCE/PROJECT_CONSTITUTION.md`
**Conditions / limits:** —
**Approved by:** Tara Nelson
**Status:** ACTIVE

---

### D-002 — Canonical identity file name
**Date:** 2026-07-14
**Class:** Material decision
**Decision:** The master identity file is `01_IDENTITY/KAIA_MASTER_CANON.md`. The Phase 2 file list is amended from `MASTER_CANON.md` accordingly.
**Reason:** Explicit naming survives multi-persona futures and aligns the plan with `PROJECT_CONSTITUTION.md` §7.1 references.
**Affected files:** `01_IDENTITY/KAIA_MASTER_CANON.md` future file; Phase 2 plan
**Conditions / limits:** —
**Approved by:** Tara Nelson
**Status:** ACTIVE

---

### D-003 — Standing approval SA-01: control-center state commits
**Date:** 2026-07-14
**Class:** C / Standing approval
**Decision:** Claude Code may commit and push updates to `00_CONTROL_CENTER/SESSION_LOG.md`, `00_CONTROL_CENTER/NEXT_ACTIONS.md`, and `00_CONTROL_CENTER/ACTIVE_WORK.md` that accurately reflect work performed in an approved session, without per-commit approval.
**Reason:** Prevents approval fatigue on routine, reversible, low-risk state updates under `APPROVAL_POLICY.md` §6.
**Affected files:**
- `00_CONTROL_CENTER/SESSION_LOG.md`
- `00_CONTROL_CENTER/NEXT_ACTIONS.md`
- `00_CONTROL_CENTER/ACTIVE_WORK.md`
**Conditions / limits:** Content must reflect work actually performed. Any other file included in the same commit voids this standing approval for that commit. Review at Phase 7 activation.
**Approved by:** Tara Nelson
**Status:** ACTIVE
