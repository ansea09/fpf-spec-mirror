---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:10"
section_title: "Work-claim interpretation checks"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__012_work-claim-interpretation-checks.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:10 — Work-claim interpretation checks"
line_start: 24327
line_end: 24336
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
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
  - "E.10.ARCH"
  - "E.17"
  - "F.6"
  - "U.Capability"
  - "U.Method"
  - "U.MethodDescription"
  - "U.ReferenceScheme"
  - "U.System"
  - "U.SystemRoleAssignment"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "actual performer U.System"
  - "admitted U.Work kind"
  - "containing System"
  - "covering U.SystemRoleAssignment"
  - "enacted Method"
  - "optional direct bindings and resource use"
  - "performedUnderAssignment"
  - "separate result or consequence"
  - "temporal extent"
  - "world-side dated occurrence"
---

### A.15.1:10 - Work-claim interpretation checks

When another decision relies on a work occurrence, perform three quick checks:

1. **Method-description interpretation.** Does `methodDescriptionRef` resolve to the selected `U.MethodDescription` episteme under the effective `U.ReferenceScheme` used by the receiving claim? If the claim also says this is an edition of an earlier description, does the exact C.2.1 `EpistemeEditionRelation` obtain? If two local senses must be related, test an F.9 Bridge and state the bounded use separately rather than treating the reference change as a Bridge.
2. **Performer and assignment coverage.** For every admitted `U.System` named as performer, does F.6 recover the exact directly declared assignment species and one obtaining occurrence `RA` of that species? Does `RA` carry the actual participant values, have that System as holder, and cover the Work or exact performed part? If not, keep the Work occurrence, performer claim, assignment occurrence, and attribution claim separate until A.2.1 and F.6 repair them.
3. **Evaluation boundary.** Has separately performed evaluation or acceptance work applied the selected criterion episteme to the independently obtaining relations involving the Work occurrence, changed subject, measurement results, or delivered entity that the criterion actually requires? If not, no acceptance verdict follows. If yes, keep the evaluation work, result episteme, verdict content, evidence, and acceptance relation separate. Claim edition continuity only when the exact C.2.1 relation obtains.

These checks tell the reader which description, assignment, criterion, evaluation, and relation to cite. They neither create one judgment-context object nor make acceptance part of work identity.

