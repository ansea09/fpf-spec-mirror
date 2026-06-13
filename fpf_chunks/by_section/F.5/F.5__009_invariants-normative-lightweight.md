---
chunk_kind: "child"
pattern_id: "F.5"
pattern_title: "Naming Discipline for U.Types & Roles"
section_id: "F.5:8"
section_title: "Invariants (normative, lightweight)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.5/F.5__009_invariants-normative-lightweight.md"
commit_sha: "cb17c555f343780e31e5fea236a74adc69295736"
heading_path:
  - "F.5 — Naming Discipline for U.Types & Roles"
  - "F.5:8 — Invariants (normative, lightweight)"
line_start: 72580
line_end: 72593
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

### F.5:8 - Invariants (normative, lightweight)

**INV-F5-1 (Pair).** Every Role Description card and every U.Type **MUST** carry **Tech** and **Plain** labels; symbol is optional and informative.

**INV-F5-2 (Context fidelity for Role Descriptions).** `Tech(T)` **MUST** be idiomatic for its Context; `Plain(T)` **MUST NOT** broaden `sense(T)`.

**INV‑F5‑3 (Neutrality for U.Types).** `Tech(U)` **MUST** be discipline‑neutral with respect to the witness Contexts in its Concept‑Set row.

**INV‑F5‑4 (senseFamily honesty).** Role Description **Role** labels are **behavioural masks**; Role Description **Status** labels are **states/badges**; neither sneaks in the other senseFamily.

**INV‑F5‑5 (Minimality).** Labels **MUST** reflect the **minimal generality** supported by invariants (F.4 for Role Description, F.7 for U.Types).

**INV-F5-6 (No Context tags).** Names **MUST NOT** embed Context/edition tags; that information resides in SenseCells (Role Description) and Concept-Set rows (U.Types).

