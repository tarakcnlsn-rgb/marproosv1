# ROADMAP

**Purpose:** Phase-level plan and status. This file answers "where are we in the build, and what comes next."
**Type:** State file — Tier 1, not semantically versioned — Git history is the record. Phase *definitions* changes are Tier 3 (structure); status updates are Tier 1.
**Authority:** Level 6 (Constitution §5).

---

## Build Phases

| Phase | Name | Purpose | Status |
|---|---|---|---|
| 0 | Repository Foundation | Governance + control center | **IN PROGRESS** |
| 1 | Project Instructions | Per-tool instruction files | Not started |
| 2 | Identity System | Kaia canon source of truth | Not started |
| 3 | Generation Pipeline | Daily content generation system | Not started |
| 4 | Prompt System | Reusable prompt infrastructure | Not started |
| 5 | Content Operations | Planning, calendar, banks, queues | Not started |
| 6 | Asset Library | Media tracking and manifest | Not started |
| 7 | Automation & Agents | Agent/skill registries, automation prep | Not started |
| 8 | Analytics & Optimization | Performance, drift, and QC tracking | Not started |

## Sequencing Rules

1. Phases build in order; a phase is COMPLETE only when its deliverables exist, are validated, and are committed (Constitution §8).
2. The critical path to first Kaia content is **0 → 1 → 2 → 4 → 3** (prompt system before full pipeline, since prompts are the pipeline's raw material). Phases 5–8 deepen operations after generation is proven.
3. Partial early starts (e.g., drafting canon ideas during Phase 1) are allowed as drafts but do not change phase status.

## Milestones

- **M1:** Phase 0 committed — governance active. Target: current session block.
- **M2:** First identity-compliant Kaia image generated and QC-passed. Requires Phases 2 + 4 core files.
- **M3:** First full content packet (image + caption + metadata) through the manual pipeline.
- **M4:** First standing daily operating loop executed end to end.
