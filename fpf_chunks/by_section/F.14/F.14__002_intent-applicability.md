---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti‑Explosion Control (Roles & Statuses)"
section_id: "F.14:1"
section_title: "Intent & applicability"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__002_intent-applicability.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "F.14 — Anti‑Explosion Control (Roles & Statuses)"
  - "F.14:1 — Intent & applicability"
line_start: 73744
line_end: 73751
dependencies:
  - "F.1"
  - "F.10"
  - "F.11"
  - "F.12"
  - "F.13"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.7"
  - "F.8"
keywords:
  - "bundles"
  - "guard-rails"
  - "reuse"
  - "separation-of-duties"
  - "vocabulary growth"
---

### F.14:1 - Intent & applicability

**Intent.** Prevent the uncontrolled growth of **Roles** and **Statuses** by privileging **reuse**, **bundling**, **explicit separation‑of‑duties (SoD)**, and **applicability windows** over minting new names. Keep the vocabulary **small, crisp, and composable** while remaining faithful to local meanings fixed by Contexts (F.1) and SenseCells (F.3).

**Applicability.** Whenever a new Role or Status is proposed, a team merges two lines of work, or a domain shifts its jargon. Use this pattern before adding rows to the Concept‑Set Table (F.7) or new Role Descriptions (F.4).

**Non‑goals.** No org charts, no RBAC policies, no process roles. This pattern describes **mental moves** for architectural naming, not governance machinery.

