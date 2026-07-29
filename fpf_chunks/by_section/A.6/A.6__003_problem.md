---
chunk_kind: "child"
pattern_id: "A.6"
pattern_title: "Signature Stack & Boundary Discipline"
section_id: "A.6:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6/A.6__003_problem.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "A.6 — Signature Stack & Boundary Discipline"
  - "A.6:2 — Problem"
line_start: 8897
line_end: 8911
dependencies:
  - "A.10"
  - "A.15"
  - "A.2.3"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
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
  - "C.28"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.19"
  - "E.8"
  - "F.18"
  - "F.9"
  - "U.Mechanism"
  - "U.Signature"
  - "U.View"
keywords:
  - "Confuses deontics with mathematical admissibility"
  - "Rewrite as declarative predicate"
  - "Work versus non-Work effect"
  - "acceptance"
  - "actual occurrence"
  - "and evidence"
  - "atomic L/A/D/E claims"
  - "delivery"
  - "in invariants"
  - "publication face"
  - "reference predicate IDs from CC when needed"
  - "separate result"
  - "signature and mechanism declarations"
  - "six-way authority-word branch"
  - "undermines auditability"
  - "“MUST” appears inside Definition: blocks"
---

### A.6:2 - Problem

When boundaries are described without an L/A/D/E claim-classification discipline, four confusions dominate:

1. **Laws vs admissibility.** Authors encode runtime gate predicates as “laws”, or write invariants using RFC‑style deontic verbs, blurring “what is true or defined” with “what is allowed to be applied”. FPF explicitly separates these: operational guard predicates belong to mechanisms (A.6.1), not signatures (A.6.0).
   *Common mistake #0 — Applicability ≠ Admissibility (informative):* Signature `Applicability` scopes declared admissible use and bounded context; it is not a runtime entry gate. Runtime entry checks belong in `U.Mechanism.AdmissibilityConditions` as `A-*`. Such a predicate may consume the direct object selected by one `A6-AW-*` row as input, but it neither creates that object nor proves gate passage. An accountable duty to enforce the gate is a separate `D-*` claim referencing the `A-*` ID.

2. **Admissibility vs deontics.** `MUST`, `SHOULD`, `MAY`, and authority-looking words do not reveal whether a statement is a duty, one `A6-AW-*` permission branch, or an entry predicate. Classify the claim by its job; the word and owner family decide nothing.

3. **Contract talk category errors.** “The interface promises…” is a metaphor. A.2.3 owns promise content; A.2.9 owns the instituting speech-act Work; A.2.8 and A.2.8.PER own the commitment or grant; A.15.1 owns only the dated Work occurrence. An application result, production, delivery/transfer, acceptance, and evidence use each follows its own row in `A.15.1:4.6` and is omitted when that claim is absent. A.6.C unpacks the boundary case; F.18 only names recovered terms when durable naming is current.

4. **Effect claims without an actual occurrence.** A description, diagram, log, or metric can state or support an effect claim, but none creates the effect. Ground the exact actual occurrence first: use `U.Work` only when role-method-work facts obtain; use A.3/A.3.4 or the exact interaction or causal owner for natural, spontaneous, formal, or other non-Work change. Then name the observation and A.10 evidence path needed for reliance.

These confusions destroy evolvability: you cannot swap implementations behind a stable signature if the signature already smuggles mechanism‑gates, audit logistics, or role-assignment commitments into “laws”.

