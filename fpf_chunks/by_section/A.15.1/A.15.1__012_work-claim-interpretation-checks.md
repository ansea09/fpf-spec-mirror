---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work: Dated Performed Work Occurrence"
section_id: "A.15.1:10"
section_title: "Work-claim interpretation checks"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__012_work-claim-interpretation-checks.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "A.15.1 — U.Work: Dated Performed Work Occurrence"
  - "A.15.1:10 — Work-claim interpretation checks"
line_start: 29538
line_end: 29547
dependencies:
  - "A.1"
  - "A.10"
  - "A.13"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "B.1.4"
  - "B.1.6"
  - "B.3"
  - "C.2.1"
  - "C.27.TA"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ROLE"
  - "E.17"
  - "F.6"
  - "U.Method"
  - "U.MethodDescription"
  - "U.ReferenceScheme"
  - "U.WorkPlan"
keywords:
  - "A.13-qualified actual performer U.System"
  - "F.6 only after admission for precise assignment-bound attribution"
  - "conditional agency profile"
  - "containing System"
  - "enacted Method"
  - "exact performance history"
  - "independent U.Work admission"
  - "optional direct bindings and resource use"
  - "separate result or consequence"
  - "temporal extent"
  - "world-side dated occurrence"
---

### A.15.1:10 - Work-claim interpretation checks

When another decision relies on Work, apply only the following checks that its claims consume; reuse an established result while its basis remains applicable:

1. **Method-description interpretation, when used.** Does `methodDescriptionRef` resolve to the selected `U.MethodDescription` episteme under the effective `U.ReferenceScheme` used by the receiving claim? If the claim also says this is an edition of an earlier description, does the exact C.2.1 `EpistemeEditionRelation` obtain? If two local senses must be related, test an F.9 Bridge and state the bounded use separately rather than treating the reference change as a Bridge.
2. **Performer and conditional assignment coverage.** For every admitted `U.System` named as performer, does section 4.0 recover its A.13 basis? If this receiving check expressly consumes precise assignment-bound attribution, does the account also cite the exact directly declared assignment species and the same obtaining occurrence `RA` already recovered through A.2.1 and A.13, and does F.6 obtain for the already admitted Work and that `RA`? Does `RA` carry the actual participant values, have that System as holder, and cover the Work or exact performed part? If no attribution is current, stop after the performer and Work checks. If the conditional attribution branch fails, repair or reject the unsupported attribution. Retain independently grounded Work and performer claims; under §4.1, recheck any admission premise also affected by that finding.
3. **Evaluation or acceptance, when claimed.** Identify the criterion, its application to the required subject facts, returned value and evidence. Assert acceptance only under its own predicate and actual participants. Identify evaluation Work separately when its dated occurrence is claimed; keep result content and acceptance distinct. Historical criterion continuity requires the C.2.1 relation.

These checks tell the reader which description, assignment, criterion, evaluation, and relation to cite. They neither create one judgment-context object nor make acceptance part of work identity.

