# MARCHETTI PROJECT OS — CHANGE CONTROL

**Document ID:** MPO-GOV-004
**Version:** 1.0.0
**Status:** ACTIVE
**Owner:** Tara Nelson
**Proposed date:** 2026-07-13
**Approved date:** 2026-07-14
**Authority level:** 4 — Approved governance policy (subordinate to the Constitution)
**Governed by:** `00_GOVERNANCE/PROJECT_CONSTITUTION.md` §10, §19, §23
**Related:** `APPROVAL_POLICY.md` governs *permission for actions*; this file governs *how changes to files, structure, and versions are made*.

---

## 1. Purpose

This policy defines how changes enter the repository: change tiers, the proposal process for material changes, versioning rules, protected files, Git conventions, and rollback.

---

## 2. Change Tiers

Every repository change falls into one tier. When uncertain, use the higher tier.

### Tier 1 — Routine update

Content updates that record reality without changing rules or structure: log entries, state updates (`ACTIVE_WORK.md`, `NEXT_ACTIONS.md`), calendar entries, adding items to banks/queues, metadata records.

- Process: make the change per an approved task; commit under Class A/B approval.
- No proposal, no version bump.

### Tier 2 — Content change to an authoritative file

Substantive edits to a governed document that do not change project structure or authority: expanding a template, clarifying a workflow, adding a QC rule, refining a prompt library.

- Process: brief in-session proposal (what/why/files affected) → owner approval (Class B, or Class C if the file is protected) → change → version bump per §4 → commit referencing the change.

### Tier 3 — Structural or authority change

Changes to folder structure, file responsibilities, authority hierarchy, schemas that other files depend on, locked canon, governance policies, or the Constitution.

- Process: full material change proposal per Constitution §19 (problem, change, affected files, benefits, risks, migration, validation/rollback, approval) → Class C approval recorded in `DECISIONS.md` → coordinated update of **all** dependent files in one controlled change → version bumps → commit(s) referencing the decision ID.

### Tier 4 — Destructive or irreversible change

Deleting authoritative files, rewriting Git history, migrations without certain recovery, removing an integration that holds data.

- Process: Tier 3 process, plus explicit confirmation of the recovery method *before* execution. If recovery is uncertain, the default answer is no (Constitution §9.2).

---

## 3. Protected Files

Changes to these files are always Tier 3 minimum and always Class C:

- `00_GOVERNANCE/PROJECT_CONSTITUTION.md` (also requires the §23 amendment process)
- All files in `00_GOVERNANCE/`
- `01_IDENTITY/KAIA_MASTER_CANON.md` and all locked canon files (also require Constitution §7.3 canon change control)
- Any schema in `02_PIPELINE/SCHEMAS/` once another file or workflow depends on it
- `06_AUTOMATION/AGENT_REGISTRY.md` and `SKILL_REGISTRY.md` entries for *active* agents/skills

A tool that finds itself editing a protected file without a recorded Class C approval must stop and escalate.

---

## 4. Versioning Rules

Governed documents carry a semantic version in their header (Constitution §23 pattern):

- **PATCH (x.x.+1):** clarification, typo, formatting — no behavioral change.
- **MINOR (x.+1.0):** compatible addition — new rule, new section, expanded scope that breaks nothing.
- **MAJOR (+1.0.0):** breaking change — altered authority, removed rule, changed meaning, structural reorganization.

Rules:
1. Version bumps happen in the same commit as the change.
2. Every bump adds a row to the document's Amendment History table.
3. Tier 1 files (logs, state, banks, queues) are **not semantically versioned** — they carry no version header; Git history is their record.
4. JSON files carry a `"version"` field following the same rules.
5. Documents remain `PROPOSED` at 1.0.0 until first owner approval, then become `ACTIVE`. Subsequent approved changes keep status `ACTIVE` and bump the version.

---

## 5. Git Conventions

Extends Constitution §10.4.

**Branching:** work happens on `main` while the project is single-operator. Branches are introduced only when a change is risky enough to warrant isolation (Tier 3–4 migrations) or when automation begins committing — at which point agents commit to branches and only the owner (or an owner-approved process) merges to `main`. Introducing branch protection is itself a Tier 3 change.

**Commit messages:**
```
<area>: <what changed>

[optional body: why, scope notes]
[Ref: D-### when executing a recorded decision]
```
Areas: `governance`, `control`, `identity`, `pipeline`, `prompts`, `content`, `assets`, `automation`, `analytics`, `repo` (structure/meta).

Examples:
- `governance: ratify constitution v1.0.0 [Ref: D-001]`
- `identity: add wardrobe canon winter collection (minor 1.1.0)`
- `control: session log 2026-07-13`

**Commit hygiene:**
- One coherent purpose per commit; do not mix tiers in a commit.
- Never commit a file whose header status/version contradicts its content.
- Verify push success before reporting completion (Constitution §10.4).

---

## 6. Dependency Discipline

Before changing any authoritative file, identify its dependents. Minimum checks:

1. Search the repo for references to the file's path and its key terms.
2. Update every dependent file in the same controlled change (Tier 3) or flag dependents explicitly in the proposal.
3. Never leave a reference pointing to a renamed, moved, or superseded rule.

A change is not complete while a known stale reference remains (Constitution §18).

---

## 7. Rollback

- **Tier 1–2:** revert via `git revert` (preferred — preserves history) referencing the original commit.
- **Tier 3:** revert the change *and* its dependent updates together; record the rollback and reason in `DECISIONS.md` if the original change was a recorded decision.
- **Tier 4:** rollback method must have been defined before execution; execute that method exactly.
- `git reset`/history rewriting is not a rollback tool; it is a Tier 4 destructive action.

---

## 8. Supersession Instead of Deletion

Authoritative content is superseded, not silently deleted:

- When a rule or file is replaced, mark the old location `SUPERSEDED by <path>` in the same change, or delete the file only under Tier 3–4 process with the replacement already in place.
- Never leave two files claiming authority over the same question (Constitution §10.2).

---

## Amendment History

| Version | Date | Status | Summary | Approved by |
|---|---|---|---|---|
| 1.0.0 | 2026-07-14 | Active | Initial change control policy for Marchetti Project OS | Tara Nelson |
