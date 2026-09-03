---
chunk_kind: "child"
pattern_id: "E.10.ARCH"
pattern_title: "Wording-Use Ontological Precision Restoration Architecture"
section_id: "E.10.ARCH:6"
section_title: "Admission and extraction criterion"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.ARCH/E.10.ARCH__012_admission-and-extraction-criterion.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "E.10.ARCH — Wording-Use Ontological Precision Restoration Architecture"
  - "E.10.ARCH:6 — Admission and extraction criterion"
line_start: 77441
line_end: 77457
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.PROD"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.SPR"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "A.3.4"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.F"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "C.16"
  - "C.2.1"
  - "C.2.P"
  - "C.2.P.DR"
  - "C.25"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.P"
  - "C.30.STRAT"
  - "E.10"
  - "E.10.DEV"
  - "E.10.MOVE"
  - "E.11"
  - "E.18"
  - "E.19"
  - "E.2"
  - "E.20"
  - "E.21"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.8"
  - "F.18"
  - "F.19"
  - "I.2"
keywords:
---

### E.10.ARCH:6 - Admission and extraction criterion

Add or retain a `WordingUseRestorationApplicabilityRow` when all of the following are true:

- the wording recurs across FPF-governed texts or project text deliberately using FPF-governed terms, pattern references, relation names, or conformance claims;
- the hidden primary-EntityOfConcern use field set is stable;
- the recovery apparatus or field set is stable enough to teach;
- repeated in-place repair distracts from the subject pattern's primary EntityOfConcern and first useful move;
- a useful remaining reader use survives the repair and the row helps recover it;
- no existing subject pattern already carries the row without duplicating repair-only doctrine inside subject patterns.

Do not add a new realization pattern when an existing subject pattern such as `A.6.F`, `A.6.A`, `A.6.M`, `A.15.4`, `A.6.6`, `A.6.3.CSC`, `A.10`, `B.3`, `A.20`, `A.21`, `A.15`, `C.11`, `C.28`, or another subject pattern already contains the rule that defines, constrains, or tests the EntityOfConcern under repair, relation, claim, or field. Record the PatternID that locates that rule as `subjectPatternLocator` and state the rule's contribution.

Extract repair-only material from a subject pattern when the material is only wording-recognition lists, false-friend rows, anti-umbrella prose, or repair fields that must run before the subject pattern can state its own invariant. Leave a narrow first-use cue or subject-pattern relation in the subject pattern.

Keep material in the subject pattern when it states the subject pattern's own invariant, worked case, conformance condition, characteristic construction, structural construction, mathematical lens, source-return condition, or user action.

