---
chunk_kind: "child"
pattern_id: "F.1"
pattern_title: "Question-Relative Source Selection"
section_id: "F.1:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/F.1/F.1__008_conformance-checklist.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "F.1 — Question-Relative Source Selection"
  - "F.1:7 — Conformance Checklist"
line_start: 93354
line_end: 93381
dependencies:
  - "A.10"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "F.0.1"
  - "F.0.2"
  - "F.17"
  - "F.9"
keywords:
  - "SourceCutNote"
  - "answer-changing source role"
  - "exact source and edition"
  - "finite source cut"
  - "intended use"
  - "receiving question"
  - "reopen condition"
---

### F.1:7 - Conformance Checklist

#### F.1:7.1 - Static checks

- **SCR-F1-S01 (Question and use).** The receiving question is independently identified as the note's exact EntityOfConcern; the intended use and the source difference that can change the answer remain in its ClaimGraph.
- **SCR-F1-S02 (Exact sources).** Every retained source and edition is recoverable.
- **SCR-F1-S03 (Answer-changing roles).** Every retained source has an inspected role; exclusions and source gaps are explicit.
- **SCR-F1-S04 (Finite and inspectable).** The cut can be held in view without dropping a known answer-changing source merely to satisfy a count.
- **SCR-F1-S05 (C.2.1 identity and one result).** The `SourceCutNote`'s ClaimGraph, exact receiving-question EntityOfConcern, and effective ReferenceScheme are all recoverable. The scheme resolves the question, exact source editions, and role claims. A file, source list, one-screen form, or question-and-use bundle supplies none of these values by form and does not become another result kind.
- **SCR-F1-S06 (Locality).** No cross-source equivalence, merge, or relation is asserted by selection.
- **SCR-F1-S07 (Temporal honesty).** Designed and performed source claims remain distinct when the difference affects the answer.
- **SCR-F1-S08 (Family neutrality).** No meaning, relation, or membership decision relies on a domain-family label.
- **SCR-F1-S09 (Named search policy).** Any material search aid has a recoverable policy, corpus, method or model edition, and interpretation.
- **SCR-F1-S10 (No algorithmic gate).** A search reading changes the cut only after inspection of source claims.
- **SCR-F1-S11 (Reopen conditions).** The result says which question, use, edition, rival, counterexample, or transfer-boundary change reopens it.
- **SCR-F1-S12 (Domain-method boundary).** A required systematic or appraisal-bearing review remains with its domain method.
- **SCR-F1-S13 (SoTA source roles).** A cut used for a SoTA claim assigns every retained source one of the comparison roles defined in `E.8:11`, records it in plain wording, and says which retained contributions can change the answer. F.1 does not restate or supersede the E.8 definition.
- **SCR-F1-S14 (No authority or currentness laundering).** Official status, popularity, maintained status, citation count, publication date, freshness, or academic praise does not promote a source into the best-known line. An official or widespread source may still earn that role from its substantive comparison. Catalogue and publisher pages support identity/currentness only unless their substantive claims independently enter the comparison.
- **SCR-F1-S15 (SoTA one-source guard and gap).** A one-source SoTA cut is used only when that source critically synthesizes the serious alternatives and no known action-changing rival or counterexample remains hidden. Otherwise the cut retains the necessary comparison or returns a source gap.

#### F.1:7.2 - Regression checks

- **RSCR-F1-E01 (Edition change).** Recheck only answer-changing claims that used the changed edition.
- **RSCR-F1-E02 (Use change).** Recheck which sources, rivals, counterexamples, and limits matter when the question or use changes.
- **RSCR-F1-E03 (New false friend).** Add a concise warning when recurrent wording confusion changes the receiving answer.
- **RSCR-F1-E04 (Bounded cut).** Remove non-changing sources or split genuinely different questions when the active cut can no longer be inspected together.
- **RSCR-F1-E05 (Search drift).** A changed taxonomy, corpus, model, descriptor, scale, distance, threshold, or rank cannot silently change membership.

