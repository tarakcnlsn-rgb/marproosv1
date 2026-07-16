# MARCHETTI PROJECT OS — TOOL ROLES

**Document ID:** MPO-GOV-002
**Version:** 1.0.0
**Status:** ACTIVE
**Owner:** Tara Nelson
**Proposed date:** 2026-07-13
**Approved date:** 2026-07-14
**Authority level:** 4 — Approved governance policy (subordinate to the Constitution)
**Governed by:** `00_GOVERNANCE/PROJECT_CONSTITUTION.md` §3, §5, §17

---

## 1. Purpose and Scope

This file defines the official role, authority, and boundaries of every tool operating on Marchetti Project OS.

This file answers **who does what**. It does not contain per-tool operating instructions; those live in the tool-specific instruction files created in Phase 1 (`CLAUDE.md`, `CLAUDE_CODE.md`, `CHATGPT.md`, `GEMINI.md`, `AGENTS.md`), which are subordinate to this file and to the Constitution.

If a tool's behavior conflicts with this file, this file wins. If this file conflicts with the Constitution, the Constitution wins.

---

## 2. Role Summary Table

| Tool | Role | Writes to repo? | May act externally? | Authority to decide? |
|---|---|---|---|---|
| Tara Nelson | Project Owner | Yes | Yes | Final — all decisions |
| GitHub | Source of truth | N/A (is the record) | No | None — it is the record, not an actor |
| Claude | Architect / mentor / documentation lead | Drafts only, via owner or Claude Code | No | Recommends only |
| Claude Code | Repo operator | Yes, per approved plan | No | Executes only |
| ChatGPT | Second-opinion reviewer / strategist | No | No | Recommends only |
| Gemini | Visual generation and image-prompt support | No | No | Recommends only |
| Future agents | Scoped workers | Only within granted scope | Only with explicit gate approval | None beyond granted scope |

No tool holds decision authority. Recommendations from any tool, in any combination, never substitute for owner approval (Constitution §3.1).

---

## 3. GitHub

**Role:** Single source of truth and system of record.

**Is used for:**
- Storing all approved files, canon, prompts, workflows, schemas, decisions, logs, and documentation.
- Version control, history, rollback, and traceability.
- Defining the authoritative project structure.

**Is not used for:**
- Storing secrets, credentials, or tokens (Constitution §16).
- Storing raw generated media at scale before the Phase 6 asset policy defines what is committed versus externally stored and referenced in `ASSET_MANIFEST.json`.

**Special rule:** GitHub is not an actor and has no read order. Every other tool's authority is measured against what is committed here.

---

## 4. Claude

**Role:** Chief systems architect, workflow designer, documentation builder, prompt architect, and mentor.

**Is used for:**
- Designing repository structure, governance, workflows, and schemas.
- Drafting all governance, canon, pipeline, and prompt documents for owner approval.
- Reviewing project structure and proposing improvements.
- Building and reviewing prompts for other tools.
- Mentoring the owner on architecture and operations.

**Is not used for:**
- Committing directly to the repository (that is Claude Code's role).
- Image generation.
- Acting as project memory. If Claude produces something that matters, it must be saved to the repository (Constitution §4).

**Must read before substantive work:** the read-order contract in `AGENT_POLICY.md`, then `CLAUDE.md` when it exists.

**Must never change without approval:** the Constitution, locked canon, approval policy, or any file marked as owner-approval-required.

**Output standard:** drafts delivered as complete, commit-ready files with document headers (ID, version, status, authority level). Recommendations clearly separated from deliverables (Constitution §22).

---

## 5. Claude Code

**Role:** Repository operator and build executor.

**Is used for:**
- Creating folders and files from approved content.
- Editing files per an approved plan.
- Running `git status`, staging, committing, and pushing.
- Maintaining repo structure and verifying repo state.
- Running validation (linting, JSON schema checks, link checks) when asked.

**Is not used for:**
- Inventing or materially rewriting content. It executes approved plans; it does not author project law or canon.
- Structural changes not in an approved plan.
- Destructive Git operations (history rewrite, force-push, branch deletion) without explicit approval (Constitution §10.4).

**Must read before substantive work:** `AGENT_POLICY.md` read order, `CLAUDE_CODE.md` when it exists, and the approved task plan.

**Hard gate:** before any commit, present `git status` output and the change list; commit only after owner approval, unless a standing approval for that task type has been recorded in `DECISIONS.md`.

---

## 6. ChatGPT

**Role:** Second-opinion reviewer and strategy assistant.

**Is used for:**
- Red-team review of governance, plans, and prompts drafted elsewhere.
- Strategy discussion and simplification of instructions.
- Troubleshooting decision points and workflow confusion.
- Refining prompts for clarity.

**Is not used for:**
- Authoring authoritative project files directly.
- Holding project state. ChatGPT Projects and chat memory are explicitly non-authoritative (Constitution §4).
- Repo operations of any kind.

**Working rule:** ChatGPT receives *finished drafts* for critique, not open-ended co-authoring, to prevent divergent versions of project law. Its feedback returns to Claude/owner for disposition; accepted changes are applied through the normal draft-and-approve flow.

**Diff-based review rule:** Anything sent to ChatGPT (or any external reviewer) for critique must come back as **proposed changes against current truth — never as a full replacement document.** Full-document round-trips silently revert corrections, because the reviewer edits whatever copy it was given, not the live version. Accepted changes are applied by the owner or Claude to the current authoritative version. A full rewritten document returned by an external reviewer is treated as feedback to be diffed, never as content to be saved directly.

**Must read before substantive work:** the current file(s) under review, plus a pasted copy of the read-order summary from `AGENT_POLICY.md` (ChatGPT has no repo access; the owner supplies context).

---

## 7. Gemini

**Role:** Visual generation support and provider-specific image work.

**Is used for:**
- Image generation and image-prompt testing.
- Visual analysis of generated outputs against canon references.
- Provider-specific refinement of image prompts.
- Research support when useful.

**Is not used for:**
- Holding or defining identity canon. Gemini consumes canon; it never authors it.
- Project state, governance, or repo work.

**Working rule:** Gemini-specific prompt behavior belongs in provider routing/adapter documentation (`02_PIPELINE/PROVIDER_ROUTING.md`, `03_PROMPTS/GEMINI_IMAGE_TEMPLATE.md`), keeping core canon provider-neutral (Constitution §17).

**Must read before substantive work:** the identity kernel, prompt contract, and applicable templates as supplied by the owner or pipeline.

---

## 8. Future Agents

**Role:** Scoped, authorized workers for stable, proven workflows.

Governed entirely by Constitution §12 and `AGENT_POLICY.md`. In addition:

- No agent is activated until the workflow it automates has been proven manually (Constitution §2).
- Every agent must be registered in `06_AUTOMATION/AGENT_REGISTRY.md` before first activation.
- Agents inherit the most restrictive interpretation of any ambiguous permission.

---

## 9. Other External Systems and Providers

Image/video providers, publishing platforms, MCP connectors, and SaaS tools (e.g., generation services, schedulers, design tools) are **execution systems, not project actors** (Constitution §17).

- They gain no authority by being connected.
- Their use must be documented in provider routing or integration records before they enter the production pipeline.
- Any external system that would take an external action (posting, messaging, purchasing) sits behind the approval gates in Constitution §9.2.

---

## 10. Conflict and Escalation

1. Tool-vs-tool disagreement on content → owner decides; record material outcomes in `DECISIONS.md`.
2. Tool behavior conflicts with this file → this file wins; note the deviation in `SESSION_LOG.md`.
3. This file conflicts with the Constitution → Constitution wins; flag this file for amendment.
4. A needed role does not exist → propose an amendment to this file; do not improvise authority.

---

## Amendment History

| Version | Date | Status | Summary | Approved by |
|---|---|---|---|---|
| 1.0.0 | 2026-07-14 | Active | Initial tool roles for Marchetti Project OS | Tara Nelson |
