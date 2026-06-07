---
chunk_kind: "child"
pattern_id: "F.5"
pattern_title: "Naming Discipline for U.Types & Roles"
section_id: "F.5:7"
section_title: "Twin rules"
source_path: "FPF-Spec.md"
output_path: "by_section/F.5/F.5__008_twin-rules.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "F.5 — Naming Discipline for U.Types & Roles"
  - "F.5:7 — Twin rules"
line_start: 70337
line_end: 70343
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

