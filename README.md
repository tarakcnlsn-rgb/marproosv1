# The Marchetti Project OS

**The operating system for Kaia Marchetti** — a professional AI influencer operating system that uses this GitHub repository as the single source of truth and coordinates work across Claude, Claude Code, ChatGPT, Gemini, and future agents.

**Owner:** Tara Nelson
**Status:** Phase 0 — Repository Foundation
**Governing law:** [`00_GOVERNANCE/PROJECT_CONSTITUTION.md`](00_GOVERNANCE/PROJECT_CONSTITUTION.md)

---

## Start Here

**If you are an AI tool or agent:** you are bound by the [Constitution](00_GOVERNANCE/PROJECT_CONSTITUTION.md) and must complete the read-order contract in [`AGENT_POLICY.md`](00_GOVERNANCE/AGENT_POLICY.md) §1 before substantive work. Your role and boundaries are defined in [`TOOL_ROLES.md`](00_GOVERNANCE/TOOL_ROLES.md). Chat history is not project truth; this repository is.

**If you are the owner:** current state lives in [`00_CONTROL_CENTER/ACTIVE_WORK.md`](00_CONTROL_CENTER/ACTIVE_WORK.md) and the next step is always in [`00_CONTROL_CENTER/NEXT_ACTIONS.md`](00_CONTROL_CENTER/NEXT_ACTIONS.md).

---

## What This System Does

Creates, validates, approves, publishes, and improves content for Kaia Marchetti through a controlled, repeatable, identity-consistent workflow:

- **Identity** — one locked canon for who Kaia is and how she looks, sounds, and behaves
- **Generation** — a defined pipeline from content objective to identity-compliant output
- **Quality control** — hard identity rules that outrank aesthetics, trends, and schedule pressure
- **Approval gates** — the owner decides everything consequential; tools recommend and execute
- **Traceability** — every decision, change, and asset is recorded, versioned, and recoverable

## Repository Map

| Folder | Owns | Changes |
|---|---|---|
| `00_GOVERNANCE/` | Project law: constitution, roles, approval, change control, agent policy | Rarely — protected |
| `00_CONTROL_CENTER/` | Live state: active work, roadmap, decisions, session log, next actions | Constantly |
| `01_IDENTITY/` | Kaia's canonical identity — locked canon and enforcement rules | Only via canon change control |
| `02_PIPELINE/` | Generation workflow, state machine, provider routing, QC, schemas | Per approved plan |
| `03_PROMPTS/` | Reusable prompt templates and libraries | Per approved plan |
| `04_CONTENT/` | Calendar, briefs, caption/hashtag banks, draft and approval queues | Daily |
| `05_ASSETS/` | Generated media tracking, references, manifest | Per pipeline output |
| `06_AUTOMATION/` | Agent registry, skill registry, automation roadmap | Per approved activation |
| `07_ANALYTICS/` | Performance, QC failures, drift log, lessons learned | Per review cycle |

Authority between files is resolved by the hierarchy in [Constitution §5](00_GOVERNANCE/PROJECT_CONSTITUTION.md). Every permanent fact has exactly one authoritative home; other files reference it.

## Core Rules (Pointers, Not Copies)

- **Source of truth:** the repository. A decision is not official until committed — [Constitution §4](00_GOVERNANCE/PROJECT_CONSTITUTION.md)
- **What needs approval:** [Constitution §9](00_GOVERNANCE/PROJECT_CONSTITUTION.md); how approval works: [`APPROVAL_POLICY.md`](00_GOVERNANCE/APPROVAL_POLICY.md)
- **How changes land:** tiers, versioning, Git conventions — [`CHANGE_CONTROL.md`](00_GOVERNANCE/CHANGE_CONTROL.md)
- **How every tool must behave:** [`AGENT_POLICY.md`](00_GOVERNANCE/AGENT_POLICY.md)
- **Kaia's identity:** governed by `01_IDENTITY/KAIA_MASTER_CANON.md` (Phase 2)

## Build Status

Full phase plan and status: [`00_CONTROL_CENTER/ROADMAP.md`](00_CONTROL_CENTER/ROADMAP.md)

---

*This README is a map, not an authority. When this file and a governance file disagree, the governance file wins and this file gets fixed.*
