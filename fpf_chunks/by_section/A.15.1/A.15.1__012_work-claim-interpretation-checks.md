---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:10"
section_title: "Work-claim interpretation checks"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__012_work-claim-interpretation-checks.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:10 — Work-claim interpretation checks"
line_start: 24944
line_end: 24953
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
  - "U.Role"
  - "U.RoleAssignment"
  - "U.System"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "actual performer U.System"
  - "admitted U.Work kind"
  - "containing system"
  - "covering U.RoleAssignment"
  - "enacted method"
  - "optional direct bindings and resource use"
  - "performedUnderAssignment"
  - "separate result or consequence"
  - "temporal extent"
  - "world-side dated occurrence"
---

### A.15.1:10 - Work-claim interpretation checks

When another decision relies on a work occurrence, perform three quick checks:

1. **Method-description interpretation.** Does `methodDescriptionRef`, when current, resolve to the exact `U.MethodDescription` edition under the effective `U.ReferenceScheme` used by the receiving claim? If not, repair the reference or relate the exact local senses through F.9 when a real cross-locality claim is current.
2. **Performer and assignment coverage.** Is the exact admitted `U.System` named as performer the holder of every `U.RoleAssignment` cited by an obtaining F.6 `performedUnderAssignment(W, RA)` attribution, and does each assignment's obtaining extent cover the occurrence or exact performed part attributed to that system? If not, keep the Work occurrence, performer claim, and defective assignment or attribution claim separate until A.2.1 and F.6 admit or repair them.
3. **Evaluation boundary.** Has separately performed evaluation or acceptance work applied the current criterion edition to the exact independently obtaining relations involving the Work occurrence, changed subject, measurement results, or delivered entity required by that criterion? If not, no acceptance verdict follows. If yes, keep the evaluation work, result episteme, verdict content, evidence, and acceptance relation separately governed.

These checks recover exact governing objects. They neither create one judgment-context object nor make acceptance part of work identity.

