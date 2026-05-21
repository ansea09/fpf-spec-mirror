---
chunk_kind: "child"
pattern_id: "A.2.6"
pattern_title: "Unified Scope Mechanism (USM): Context Slices & Scopes"
section_id: "A.2.6:3"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.6/A.2.6__004_problem.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "A.2.6 — Unified Scope Mechanism (USM): Context Slices & Scopes"
  - "A.2.6:3 — Problem"
line_start: 4067
line_end: 4075
dependencies:
  - "A.1.1"
  - "A.2.2"
  - "A.2.3"
  - "B.3"
keywords:
  - "& guard style)"
  - "ClaimScope (G)"
  - "WorkScope"
  - "applicability"
  - "scope"
  - "set-valued"
---

### A.2.6:3 - Problem

1. **Synonym soup.** *Applicability, envelope, generality, capability envelope*—different labels for the **same mechanism** led to mismatches in gating, review, and reuse.
2. **Abstraction confusion.** Calling G “generality” invited teams to treat “more abstract wording” as “broader scope,” silently masking unstated assumptions.
3. **Split mechanics.** Episteme vs system text used different algebra and guard language, though **the same set operations** were meant.
4. **Cross‑context opacity.** Transfers between Contexts lacked a shared carrier and a rule for what changes (trust) vs what stays (scope).
5. **Overloaded words.** *Validity* clashed with **Validation Assurance (LA)**; *operation/operational* clashed with **Work/Run** in A.15, producing governance ambiguity.


