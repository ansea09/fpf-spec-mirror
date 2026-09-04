---
chunk_kind: "child"
pattern_id: "E.10.ARCH"
pattern_title: "Wording-Use Ontological Precision Restoration Architecture"
section_id: "E.10.ARCH:7"
section_title: "Subject-pattern thin-pointer rule"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.ARCH/E.10.ARCH__013_subject-pattern-thin-pointer-rule.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "E.10.ARCH — Wording-Use Ontological Precision Restoration Architecture"
  - "E.10.ARCH:7 — Subject-pattern thin-pointer rule"
line_start: 77459
line_end: 77476
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

### E.10.ARCH:7 - Subject-pattern thin-pointer rule

Subject patterns keep the minimum local first-use cues needed to resolve independent hidden questions about the EntityOfConcern, relation, claim, or field, then name the selected precision-restoration pattern through ordinary references or `Relations`. They do not turn that reference into local reference boilerplate, and they do not copy:

- the full `E.10` wording-recognition table;
- this shared algorithm;
- the `WordingUseRestorationApplicabilityTable`;
- broad false-friend lists whose only job is first-stage repair;
- past placement or repair history written in place of current architecture prose.

A thin pointer is acceptable when it helps the working reader choose the right first move. Illustrative cases:

- Use `E.10.ROLE` while bare claim-bearing *role* hides its work-facing or use-facing object; return to the object's rule once it is clear.
- Use `C.30.STRAT` while a stratification source label hides the FPF kind, relation, or claim-use; return the recovered claim to its defining or testing rule.
- Use `A.6.P.WMR` only while an exact Method or Work boundary relation remains hidden after generic relation recovery. Use `C.2.P` first for an epistemic source side and bypass restoration when the direct rule is clear.

The full routing conditions remain in `E.10:0.2a` and the applicability table in section 4. A subject pattern keeps only the pointer needed for its current ambiguity.

