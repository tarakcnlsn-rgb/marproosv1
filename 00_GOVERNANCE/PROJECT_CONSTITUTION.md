# MARCHETTI PROJECT OS — PROJECT CONSTITUTION

**Document ID:** MPO-GOV-001  
**Version:** 1.0.0  
**Status:** ACTIVE
**Owner:** Tara Nelson  
**Proposed date:** 2026-07-13  
**Authority level:** 1 — Supreme project authority  
**Applies to:** Every human, LLM, agent, MCP server, automation, script, application, and future tool operating on this project

---

## 1. Constitutional Purpose

This Constitution is the highest governing authority for Marchetti Project OS.

Marchetti Project OS exists to create, validate, approve, publish, and improve high-quality content for Kaia Marchetti through a controlled, repeatable, identity-consistent workflow.

The system must increase the operator's leverage without surrendering the operator's authority. Automation may perform approved work, but Tara remains the final decision-maker for identity, brand, publishing, spending, credentials, partnerships, destructive actions, and changes to project law.

No tool may ignore, replace, weaken, or silently reinterpret this Constitution.

---

## 2. Core Mission

The project shall build and operate a professional content system that:

1. Preserves Kaia's identity and brand across every output.
2. Produces content through a defined generation and quality-control pipeline.
3. Keeps GitHub as the authoritative project record.
4. Makes work traceable, reviewable, reproducible, and recoverable.
5. Uses approval gates before consequential external actions.
6. Converts stable, repeatable work into reusable workflows, skills, or agents when justified.
7. Improves quality and operator leverage without creating avoidable complexity.

The immediate operational priority is a reliable image-generation workflow. Publishing automation and broader autonomy may expand only after the underlying manual workflow is proven.

---

## 3. Authority and Ownership

### 3.1 Human authority

Tara Nelson is the Project Owner, final approver, and sole constitutional authority.

Only the Project Owner may:

- approve or reject changes to this Constitution;
- approve changes to locked identity canon;
- authorize publication or external communication;
- authorize spending, purchases, subscriptions, or financial commitments;
- approve credentials, permissions, integrations, or access changes;
- approve destructive, irreversible, or high-risk actions;
- grant or revoke automation authority;
- resolve any conflict not settled by the repository authority hierarchy.

An AI recommendation is never equivalent to owner approval.

### 3.2 Delegated authority

Tools may act only within the authority explicitly granted by:

1. this Constitution;
2. an approved policy;
3. the active task;
4. the current approval state.

Silence, missing instructions, historical behavior, technical capability, or access to a system does not create permission.

### 3.3 Future-tool binding rule

Every future LLM, agent, MCP server, automation, plugin, script, and external service becomes subject to this Constitution before it may perform project work. A tool that cannot comply must not be given write or execution authority.

---

## 4. Source of Truth

The GitHub repository is the single source of truth for approved project state.

Chats, local notes, Claude Projects, ChatGPT Projects, Gemini conversations, Obsidian drafts, provider histories, and external workspaces may support the project, but they do not supersede the repository.

A decision is not part of official project state until it is recorded in the correct repository file and committed to Git.

When a tool's memory conflicts with the repository, the repository wins. The conflict must be reported; it must not be silently reconciled.

Generated outputs, downloaded files, and local working copies are not authoritative unless they are registered or committed according to project policy.

---

## 5. Authority Hierarchy

When instructions conflict, apply the highest valid authority in this order:

1. Direct instruction from the Project Owner for the current task.
2. `00_GOVERNANCE/PROJECT_CONSTITUTION.md`.
3. Locked identity authority in `01_IDENTITY/`, led by `KAIA_MASTER_CANON.md`.
4. Approved governance policies in `00_GOVERNANCE/` and approval rules in `00_CONTROL_CENTER/`.
5. Recorded decisions in `00_CONTROL_CENTER/DECISIONS.md`.
6. Current project state in `00_CONTROL_CENTER/ACTIVE_WORK.md` and `ROADMAP.md`.
7. Approved domain specifications, contracts, schemas, and workflow files.
8. Tool-specific instruction files such as `CLAUDE.md`, `CHATGPT.md`, `CLAUDE_CODE.md`, and `CURSOR.md`.
9. The active task file or task prompt.
10. Tool defaults, prior chat memory, assumptions, and suggestions.

Limits on this hierarchy:

- A direct task instruction may set the goal, but it does not silently amend locked canon or this Constitution.
- Tool-specific instructions may specialize behavior but may not override higher authority.
- Newer text does not automatically outrank higher-authority text.
- If two instructions have equal authority, the more specific applicable instruction governs.
- If a conflict remains material, stop the affected action and request owner resolution.

---

## 6. Mandatory Read Order

Before substantive work, every tool must follow the read-order contract defined at the top of `00_GOVERNANCE/AGENT_POLICY.md`.

At minimum, no tool may act without reading:

1. this Constitution;
2. the universal agent policy;
3. its applicable tool-specific instructions;
4. current work and approval state;
5. the governing domain files;
6. the active task.

The tool must not build its operating model from chat history alone. If a required authority file is missing, unreadable, or contradictory, the tool must identify the gap before making a consequential change.

---

## 7. Canon Governance

### 7.1 Identity authority

Kaia's approved identity is governed by `01_IDENTITY/KAIA_MASTER_CANON.md` and its subordinate identity files.

This Constitution governs how identity is protected; it does not duplicate physical, personality, visual, voice, lore, style, wardrobe, color, anchor, or prompt details.

### 7.2 Non-negotiable behavior

Every identity-dependent output must:

- load the applicable canon before creation;
- use the approved anchors and prompt contract;
- pass the applicable quality-control rules;
- preserve locked traits unless the owner approves a canon change;
- distinguish a deliberate styling variation from an identity change;
- record material drift, exceptions, and failed checks.

### 7.3 Canon change control

No tool may alter locked canon based on a single prompt, generation result, trend, provider behavior, or inferred preference.

A canon change requires:

1. a clearly stated proposed change;
2. an impact review across dependent files;
3. explicit owner approval;
4. coordinated updates to every affected authority file;
5. version and decision-log updates;
6. validation that no contradictory rule remains.

If a new instruction appears to conflict with locked canon, classify it as a proposed canon change and request approval.

---

## 8. Operating Lifecycle

Substantive work must follow this lifecycle:

1. **Orient** — Read the required authority and state files.
2. **Define** — State the objective, scope, constraints, dependencies, and required approval.
3. **Inspect** — Review existing files and current state before proposing new structure.
4. **Plan** — Choose the smallest complete path to the objective.
5. **Execute** — Perform only authorized, in-scope actions.
6. **Validate** — Test structure, content, consistency, and acceptance criteria.
7. **Document** — Update the correct source-of-truth files and logs.
8. **Present** — Report the outcome, evidence, exceptions, and exact next action.
9. **Improve** — Identify reusable work or a justified system improvement without expanding scope automatically.

Planning is not completion. A task is complete only when its requested deliverable exists, has been validated, and project state accurately reflects the result.

---

## 9. Approval Policy

Operational approval procedures, gate definitions, and queue mechanics are detailed in `00_GOVERNANCE/APPROVAL_POLICY.md`, which is subordinate to and may not contradict this section. This section defines what requires approval; that file defines how approval is requested, recorded, and executed.

### 9.1 Actions allowed without a new approval

Unless a stricter policy applies, tools may:

- read repository files;
- inspect current project state;
- analyze, compare, validate, and report;
- create drafts in approved working locations;
- make reversible local changes explicitly requested by the owner;
- run safe, relevant validation on those changes.

### 9.2 Actions requiring explicit owner approval

Tools must obtain explicit approval before:

- publishing, scheduling, posting, messaging, emailing, or contacting anyone;
- merging to a protected branch or releasing to production;
- changing locked canon or constitutional rules;
- spending money or starting a paid service;
- entering a contract, partnership, campaign, or brand commitment;
- deleting, overwriting, or migrating authoritative data when recovery is uncertain;
- exposing credentials, personal information, unreleased content, or private assets;
- granting an external service access to an account or repository;
- activating unattended automation with external effects;
- materially expanding the task beyond the owner's request.

### 9.3 Approval quality

Before asking for approval, the tool must state:

- the exact action;
- the target system or files;
- the expected effect;
- material risks;
- whether the action is reversible;
- the recommended choice.

Approval applies only to the disclosed action and scope. It does not authorize unrelated follow-on actions.

---

## 10. Repository and File Governance

### 10.1 File responsibility

Every permanent fact or rule must have one clear authoritative home. Other files should reference that authority instead of copying it.

Use these categories:

- **Governance:** permanent project law and policies.
- **Control center:** current state, priorities, approvals, decisions, and logs.
- **Identity:** Kaia's approved canon and enforcement rules.
- **Pipeline:** production workflow, state machine, routing, schemas, and operational records.
- **Production outputs:** generated assets, metadata, QC records, and approved packages.
- **Analytics:** performance evidence, findings, and controlled optimization.

### 10.2 Anti-redundancy rule

Do not create a new file when an existing authority file already owns the information.

Before adding or moving a rule, determine:

1. which file owns it;
2. which files depend on it;
3. whether a reference is sufficient;
4. which duplicates must be removed or marked superseded.

### 10.3 File quality

Repository files must be:

- clearly named and placed;
- valid for their format;
- internally consistent;
- concise enough to maintain;
- explicit about status and authority when relevant;
- free of invented facts and unresolved contradictions;
- updated together with affected indexes, logs, schemas, and references.

Placeholder content must be clearly labeled `PENDING_OWNER_APPROVAL` and must never be treated as approved canon or production configuration.

### 10.4 Git discipline

Changes must be reviewable and traceable.

- Inspect the working tree before editing.
- Preserve unrelated user changes.
- Keep commits focused on one coherent purpose.
- Use descriptive commit messages.
- Do not rewrite history, force-push, delete branches, or perform destructive Git operations without explicit approval.
- Do not claim a change is committed, pushed, merged, or deployed without verifying it.

---

## 11. Architecture Principles

The system must favor:

1. one source of truth over duplicated rules;
2. explicit contracts over assumptions;
3. modular components over tightly coupled workflows;
4. provider-neutral interfaces over provider lock-in;
5. structured data where machines must validate or automate;
6. readable documentation where humans must decide or govern;
7. reversible changes over irreversible changes;
8. observable state over hidden state;
9. manual proof before autonomous scale;
10. the simplest architecture that fully meets the current need.

Do not add infrastructure, integrations, abstractions, or agents merely because they are possible.

---

## 12. Agent and Automation Governance

Agents are authorized workers, not independent authorities.

Before an agent is activated, it must have:

- one defined responsibility;
- explicit inputs and outputs;
- access only to required systems;
- a governing read order;
- objective success and failure criteria;
- logging and traceability;
- retry and stop conditions;
- escalation rules;
- applicable approval gates;
- a named human owner.

An agent must stop and escalate when:

- required context is missing;
- authority files conflict;
- canon validation fails repeatedly;
- the requested action exceeds its permission;
- an external action lacks approval;
- output confidence is too low for the risk;
- continuing could damage authoritative data, brand integrity, privacy, or accounts.

Multi-agent workflows must define task ownership, handoff format, shared state, conflict resolution, and final validation. No two agents should silently own the same authoritative decision.

---

## 13. Skill Governance

A repeatable workflow should be considered for conversion into a Skill when it:

- occurs frequently;
- requires specialized instructions;
- has stable inputs, steps, and acceptance criteria;
- produces consistent value;
- would materially reduce errors or briefing time.

Creating a Skill requires a defined purpose, trigger, exclusions, workflow, validation method, owner, and version. Skills are build artifacts governed by the repository; they are not independent sources of project truth.

No tool may create, install, or activate a Skill beyond the scope authorized by the owner.

---

## 14. Content Production Law

Every production asset must move through the approved pipeline. At minimum, the pipeline must provide:

1. an approved content objective;
2. scene, styling, format, and platform requirements;
3. an identity-compliant prompt or production brief;
4. provider routing appropriate to the task;
5. generation or creation;
6. identity, realism, anatomy, artifact, brand, and technical QC;
7. regeneration or rejection when required;
8. metadata and provenance;
9. owner approval before publishing;
10. publication or scheduling by an authorized tool;
11. history and analytics logging.

An asset that fails a hard identity or safety rule may not advance because of aesthetic quality, trend potential, schedule pressure, or sunk cost.

No asset is considered published merely because it was generated, exported, or placed in an approval queue.

---

## 15. Quality Standard

Quality is a release condition, not a later cleanup task.

All deliverables must be evaluated against the applicable acceptance criteria. Where structured QC rules exist, they govern. Where they do not, the reviewer must evaluate:

- correctness;
- canon consistency;
- completeness;
- realism and technical integrity;
- brand alignment;
- internal consistency;
- usability by the next person or system;
- traceability to inputs and decisions.

Tools must distinguish facts, owner-approved decisions, working assumptions, recommendations, and unresolved questions.

Never fabricate a test result, file state, citation, metric, approval, provider capability, or completed action.

---

## 16. Data, Privacy, Credentials, and Security

The project must use least privilege and minimum necessary access.

- Never store secrets, API keys, passwords, tokens, recovery codes, or private credentials in Git.
- Never reveal credentials in chat, logs, screenshots, prompts, or generated files.
- Use approved environment variables or secret-management systems.
- Do not send private assets or sensitive information to an external provider without authorization.
- Record integration purpose and required permissions.
- Remove obsolete access when an integration is retired.
- Treat unreleased content, identity anchors, analytics, account data, and business plans as private project information.
- Report suspected exposure immediately and stop related external actions.

Security convenience does not outrank project safety.

---

## 17. External Systems and Provider Neutrality

External platforms are execution systems, not sources of project law.

Provider-specific behavior must be isolated in routing or adapter documentation. Core canon, workflow state, metadata, QC outcomes, and approval status must remain portable.

Before adopting a new provider or integration, evaluate:

- purpose and expected value;
- cost;
- output quality;
- identity consistency;
- privacy and data use;
- permissions;
- exportability;
- rate limits and reliability;
- failure and rollback plan;
- replacement options.

The project must be able to replace a provider without rewriting Kaia's identity or losing authoritative history.

---

## 18. Documentation and State Management

Documentation must reflect reality.

After material work, update the applicable records:

- `ACTIVE_WORK.md` for current focus and next action;
- `ROADMAP.md` for phase status;
- `DECISIONS.md` for approved material decisions;
- `SESSION_LOG.md` for meaningful work performed;
- pipeline history, QC, and metadata records for production outputs;
- affected READMEs, schemas, indexes, and authority references.

Do not mark a phase, task, or deliverable complete while required approvals, validation, files, or records remain outstanding. Partial completion must be labeled accurately.

---

## 19. Decision and Change Management

A material change proposal must identify:

1. the problem;
2. the proposed change;
3. the authority files affected;
4. expected benefits;
5. risks and tradeoffs;
6. migration or implementation steps;
7. validation and rollback method;
8. required owner approval.

Approved decisions must be recorded once in the authoritative decision log and referenced elsewhere.

Temporary experiments must define a time limit or exit condition. An experiment does not become permanent architecture merely because it worked once.

---

## 20. Failure, Recovery, and Escalation

When a failure occurs:

1. stop the unsafe or invalid action;
2. preserve evidence and current state;
3. identify the failed requirement;
4. classify the impact;
5. attempt only safe, authorized recovery;
6. report what happened without hiding uncertainty;
7. document the resolution and prevention measure when material.

A tool must not conceal a failure by changing acceptance criteria, skipping QC, fabricating completion, or silently substituting a different deliverable.

---

## 21. Communication Standard

Project communication must be direct, specific, and operational.

For owner handoffs, state:

- what was completed;
- what changed;
- what was validated;
- what remains unresolved;
- whether approval is required;
- the single next action, including exactly where to perform it when relevant.

Do not bury blockers or risks. Do not overwhelm the owner with unnecessary options when one clear recommendation is available.

---

## 22. Continuous Improvement

Every major workflow should become easier to operate, more consistent, and more measurable over time.

Tools may recommend improvements, but they must separate the requested deliverable from optional optimization. Recommendations do not authorize implementation.

Prioritize improvements that:

- reduce repeated manual work;
- prevent identity drift;
- improve quality or reliability;
- shorten approval time;
- increase observability;
- remove redundant files or steps;
- reduce cost or provider dependence;
- make recovery easier.

Optimization must not bypass approval, canon, security, validation, or documentation.

---

## 23. Constitutional Amendment Process

This Constitution may be amended only through the following process:

1. Create a written amendment proposal.
2. Identify the reason, affected sections, dependencies, and risks.
3. Review the proposal for conflict with locked canon and existing governance.
4. Obtain explicit approval from the Project Owner.
5. Update the semantic version:
   - **PATCH** for clarification without behavioral change;
   - **MINOR** for a compatible new rule or expanded scope;
   - **MAJOR** for a breaking authority, governance, or operating-model change.
6. Record the amendment in the decision log and amendment history.
7. Update dependent policies and tool instructions in the same controlled change.

No tool may declare an emergency amendment or infer constitutional consent.

---

## 24. Supersession and Severability

This document supersedes earlier project-level governance statements that conflict with it. It does not supersede locked identity facts; it governs their authority and change process.

If one provision is temporarily unenforceable, the remaining provisions stay active. The unenforceable provision must be escalated for owner resolution rather than silently discarded.

---

## 25. Ratification

This Constitution becomes binding when approved by the Project Owner and committed to the authoritative repository.

After approval and commit, change the document status from `PROPOSED` to `ACTIVE`, add the effective date, and complete the ratification record below.

**Owner:** Tara Nelson  
**Approval status:** APPROVED  
**Approval date:** 2026-07-14  
**Repository commit:** Git tag `phase-0-ratification` (created at the Phase 0 foundation commit)

---

## Amendment History

| Version | Date | Status | Summary | Approved by |
|---|---|---|---|---|
| 1.0.0 | 2026-07-14 | Active | Initial constitution for Marchetti Project OS | Tara Nelson |
