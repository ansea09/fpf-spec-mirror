---
chunk_kind: "child"
pattern_id: "A.6"
pattern_title: "Signature Stack & Boundary Discipline"
section_id: "A.6:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6/A.6__003_problem.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "A.6 — Signature Stack & Boundary Discipline"
  - "A.6:2 — Problem"
line_start: 8250
line_end: 8264
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.2.3"
  - "A.2.8"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.6"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.B"
  - "A.6.C"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.26"
  - "C.26.1"
  - "C.28"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.EFP"
  - "E.19"
  - "E.8"
  - "F.18"
  - "F.9"
  - "U.EpistemicViewing"
  - "U.Mechanism"
  - "U.MultiViewDescribing"
  - "U.Signature"
  - "U.View"
  - "U.Viewpoint"
  - "U.Work"
keywords:
  - "A.6.B L/A/D/E claims"
  - "Confuses deontics with mathematical admissibility"
  - "MUST"
  - "Rewrite as declarative predicate"
  - "SHOULD"
  - "and MAY)"
  - "authority-wording split"
  - "boundary"
  - "boundary claim-classification fields"
  - "in invariants"
  - "probe/order/frame/export/state-reading claims"
  - "promise/commitment/API/policy wording"
  - "reference predicate IDs from CC when needed"
  - "register-backed status boundary"
  - "signature stack"
  - "undermines auditability"
  - "“MUST” appears inside Definition: blocks"
---

### A.6:2 - Problem

When boundaries are described without an L/A/D/E claim-classification discipline, four confusions dominate:

1. **Laws vs admissibility.** Authors encode runtime gate predicates as “laws”, or write invariants using RFC‑style deontic verbs, blurring “what is true or defined” with “what is allowed to be applied”. FPF explicitly separates these: operational guard predicates belong to mechanisms (A.6.1), not signatures (A.6.0).
   *Common mistake #0 — Applicability ≠ Admissibility (informative):* Signature `Applicability` scopes declared admissible use and bounded context; it is not a runtime entry gate. Runtime entry checks and permission predicates belong in `U.Mechanism.AdmissibilityConditions` as `A-*`. If an accountable role assignment or admitted acting system is obligated to satisfy or enforce such a gate, express that as a `D-*` duty that references the `A-*` claim ID (per A.6.B), not by rewriting the gate as “X MUST …”.

2. **Admissibility vs deontics.** The RFC keywords `MUST`, `SHOULD`, and `MAY` are used both for role-assignment or acting-system obligations and for world‑state admissibility predicates. E.8 already demands keeping deontics distinct from admissibility and definitions and recommends predicate‑style constraints for admissibility rather than RFC keywords.

3. **Contract talk category errors.** “The interface promises…” is a metaphor. Promise content, speech act, commitment, and delivered work are different FPF objects: promise content is governed by A.2.3, a speech act is work governed by A.2.9, a commitment is a deontic commitment relation governed by A.2.8, and a running service is delivered work with evidence. A.6.C unpacks the boundary case; F.18 only names recovered terms when durable naming is current.

4. **Effects without evidence or carriers.** Effects happen only in work; therefore, “effect claims” must be anchored to observation and carriers. Without A.7’s EntityOfConcern and Description-episteme / publication-carrier discipline, writers conflate the published description with runtime traces or treat a file as the system itself.

These confusions destroy evolvability: you cannot swap implementations behind a stable signature if the signature already smuggles mechanism‑gates, audit logistics, or role-assignment commitments into “laws”.

