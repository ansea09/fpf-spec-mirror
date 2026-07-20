---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:10"
section_title: "Work-claim interpretation checks"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__012_work-claim-interpretation-checks.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:10 — Work-claim interpretation checks"
line_start: 24056
line_end: 24065
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.6"
  - "A.2.8.PER"
  - "A.3.1"
  - "A.3.2"
  - "B.1"
  - "B.1.6"
  - "B.3"
  - "C.2.1"
  - "C.27.TA"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
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
  - "EpisodeOf_work"
  - "TemporalPartOf_work"
  - "actuals"
  - "concurrent work part"
  - "operational work part"
  - "performed enactment"
  - "trace"
  - "work occurrence"
---

### A.15.1:10 - Work-claim interpretation checks

When another decision relies on a work occurrence, perform three quick checks:

1. **Method-description interpretation.** Does `methodDescriptionRef`, when current, resolve to the exact `U.MethodDescription` edition under the effective `U.ReferenceScheme` used by the receiving claim? If not, repair the reference or relate the exact local senses through F.9 when a real cross-locality claim is current.
2. **Role-assignment coverage.** Does `performedBy` resolve to one `U.RoleAssignment` whose interval covers the occurrence? If not, keep the work and attribution claim separate until A.2.1 admits the assignment.
3. **Evaluation boundary.** Has separately performed evaluation or acceptance work applied the current criterion edition to the exact work facts, changed subject, measurement results, or delivered entity required by that criterion? If not, no acceptance verdict follows. If yes, keep the evaluation work, result episteme, verdict content, evidence, and acceptance relation separately governed.

These checks recover exact governing objects. They neither create one judgment-context object nor make acceptance part of work identity.

