---
chunk_kind: "child"
pattern_id: "A.6"
pattern_title: "Signature Stack: Classify and Place Boundary Claims"
section_id: "A.6:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6/A.6__003_problem.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "A.6 — Signature Stack: Classify and Place Boundary Claims"
  - "A.6:2 — Problem"
line_start: 13659
line_end: 13673
dependencies:
  - "A.10"
  - "A.15"
  - "A.2.8.PER"
  - "A.6"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.5"
  - "A.6.6"
  - "A.6.B"
  - "A.6.C"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.26"
  - "C.28"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.19"
  - "E.8"
  - "F.18"
  - "F.9"
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
  - "reference predicates by ID or canonical location from CC when needed"
  - "separate result"
  - "signature and mechanism declarations"
  - "six-way authority-word branch"
  - "undermines auditability"
  - "“MUST” appears inside Definition: blocks"
---

### A.6:2 - Problem

The following confusions change the interpretation or use of a boundary claim:

1. **Laws vs admissibility.** Authors encode runtime gate predicates as “laws”, or write invariants using RFC‑style deontic verbs, blurring “what is true or defined” with “what is allowed to be applied”. FPF explicitly separates these: operational guard predicates belong to mechanisms (A.6.1), not signatures (A.6.0).
   *Common mistake #0 — Applicability ≠ Admissibility (informative):* Signature `Applicability` scopes declared admissible use and bounded context; it is not a runtime entry gate. Runtime entry checks belong in `U.Mechanism.AdmissibilityConditions` as `A-*`. Such a predicate may consume the direct object selected by one `A6-AW-*` row as input, but it neither creates that object nor proves gate passage. A generic prescription states what one exact policy or other normative episteme requires; it does not create an individual duty bearer or commitment occurrence. A claim that one actual System or separately governed party has that duty instead cites one separately obtaining A.2.8 `U.Commitment`. Either branch can reference the `A-*` gate by ID or canonical location without becoming the gate.

2. **Admissibility vs deontics.** `MUST`, `SHOULD`, `MAY`, and authority-looking words do not reveal whether a statement is a duty, one `A6-AW-*` permission branch, or an entry predicate. Classify the claim by its job; neither the word, selected subject pattern, nor kind of direct object decides the quadrant.

3. **Contract talk category errors.** If “the interface promises…” leaves a consequential ambiguity about the claim or its participant, use A.6.C to recover it before treating the wording as an agency error. Use A.2.3 for promise content, A.2.9 for the instituting speech-act Work, A.2.8 and A.2.8.PER for the commitment or grant, and A.15.1 only to identify the dated Work occurrence. An application result, production, delivery/transfer, acceptance, and evidence use each follows its own row in `A.15.1:4.6` and is omitted when that claim is absent. F.18 only names recovered terms when durable naming is current.

4. **Effect claims without an actual occurrence.** A description, diagram, log or metric can state or support an effect claim. Establish the actual occurrence under its subject pattern. Use the Work conditions in 4.1 when a dated Work is claimed; natural, spontaneous or formal change can use A.3.4 without a Work claim. Name the observation and A.10 evidence path when the receiving use relies on that support.

These confusions can defeat substitution behind a stable signature: an implementation change may unexpectedly alter a hidden gate, duty or evidence requirement. Make each applicable constraint recoverable under its own claim.

