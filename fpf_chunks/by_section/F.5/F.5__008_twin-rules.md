---
chunk_kind: "child"
pattern_id: "F.5"
pattern_title: "Naming Discipline for U.Types & Roles"
section_id: "F.5:7"
section_title: "Twin rules"
source_path: "FPF-Spec.md"
output_path: "by_section/F.5/F.5__008_twin-rules.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "F.5 — Naming Discipline for U.Types & Roles"
  - "F.5:7 — Twin rules"
line_start: 70613
line_end: 70619
dependencies:
  - "A.11"
  - "A.7"
  - "D.CTX"
  - "E.10"
  - "E.10.D1"
  - "E.10.D2"
  - "F.0.1"
  - "F.1"
  - "F.13"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "U.Type naming"
  - "lexical rules"
  - "morphology"
  - "naming conventions"
  - "twin registers"
---

### F.5:7 - Twin rules

**Mandatory Tech name.** Every `U.Type`/Role **MUST** declare a Tech name; plain twin is optional.
**Role suffix invariant.** Role Tech names **MUST** end with `Role`; plain twin **MUST** keep “(role)” on first use.
**No head elision.** Head terms **MUST NOT** be dropped in a way that changes expected Kind (e.g., _“Approval”_ ≠ _“Approver (role)”_).
**One twin, one context.** At most one plain twin per Context; register in **E.10.P**.

