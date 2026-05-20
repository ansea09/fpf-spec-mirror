---
chunk_kind: "child"
pattern_id: "A.6.H"
pattern_title: "Wholeness Language Unpacking — RPR-WHOLE"
section_id: "A.6.H:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.H/A.6.H__008_conformance-checklist.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "A.6.H — Wholeness Language Unpacking — RPR-WHOLE"
  - "A.6.H:7 — Conformance Checklist"
line_start: 17633
line_end: 17649
dependencies:
  - "A.14"
  - "A.15"
  - "A.6.5"
  - "A.6.P"
  - "A.7"
  - "B.1.1"
  - "B.1.4"
  - "F.18"
keywords:
  - "boundary"
  - "completeness"
  - "environment"
  - "integrity"
  - "mereology"
  - "order/time"
  - "part-of"
  - "publication-carrier and describedEntity distinction"
  - "role-method-work"
  - "wholeness"
---

### A.6.H:7 - Conformance Checklist

| ID                                         | Requirement                                                                                                                                                                                                                  | Purpose                                                          |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **CC-A6H-1 (Trigger discipline).**         | Authors of normative or Working-Model text SHALL treat WHOL triggers as disambiguation triggers and apply the facet rewrite or attach a Candidate-Set Note.                                                                  | Prevents “whole/part” from becoming a typed relation definition.          |
| **CC-A6H-2 (Typed parthood).**             | When “part-of/contains/composed-of” is meant as inclusion, authors SHALL choose a typed relation kind consistent with the edge selection guide (ComponentOf / ConstituentOf / PortionOf; MemberOf if collective). If the prose is actually asserting temporal slicing/versioning, authors SHALL use PhaseOf + Γ_time and SHALL NOT encode it as inclusion. | Eliminates universal “part-of” dumping.                          |
| **CC-A6H-3 (No order/time in mereology).** | Authors SHALL NOT express step order, concurrency, or temporal coverage as structural inclusion; they SHALL use ordered relations and Γ_ctx/Γ_method or PhaseOf and Γ_time.                                                  | Blocks the structure-as-sequence and history-as-structure traps. |
|                                            | *Note:* ConstituentOf is allowed when the claim is about a publication-unit or episteme-content structure, such as step descriptions inside a method document; StepOf, SerialStepOf, and ParallelFactorOf are for the procedure graph itself.            |                                                                         |
| **CC-A6H-4 (Membership separation).**      | Authors SHALL keep MemberOf claims distinct from ComponentOf/ConstituentOf and SHALL NOT infer composition from membership without an explicit construction claim.                                                           | Prevents accidental upgrade from set to assembly.                |
| **CC-A6H-5 (Completeness routing).**       | When “complete/end-to-end/turnkey” is used, authors SHALL state whether the claim is about capability coverage, specification coverage, or evidence coverage, and route terms to A.15 vocabulary.                            | Prevents wholeness-as-rhetoric in method/role discourse.         |
| **CC-A6H-6 (Boundary clarity).**           | If “whole/integrity/environment” is asserted at holon-level, authors SHALL name the relevant boundary and at least one interface/interaction/dependency/constraint concern, or explicitly state that boundary is out of scope for the claim. | Makes inside/outside explicit and reviewable.                    |
| **CC-A6H-7 (Change-class narration).**     | When a wholeness story changes across editions, authors SHOULD use the change lexicon (reboundary/recompose/rephase/reorder/recomplete) rather than reusing “whole” rhetoric.                                                | Keeps evolution auditable.                                       |
| **CC-A6H-8 (Review lint).**                | Reviewers and validators SHOULD flag un-unpacked WHOL triggers on normative surfaces as nonconformant, unless an explicit Candidate-Set Note exists.                                                                         | Makes the discipline enforceable at low cost.                    |
| **CC-A6H-9 (Term-of-art override).**       | If a WHOL trigger appears inside a defined term-of-art, authors SHALL cite or inline the definition and SHALL NOT treat the occurrence as a WHOL trigger unless the definition itself contains unresolved WHOL triggers.       | Prevents linter noise and misrouting.                            |
| **CC-A6H-10 (Integrity classification).**  | When “integrity” appears, authors SHALL explicitly classify it as (a) wholeness/coherence, (b) security/data integrity quality, or (c) another defined term-of-art, and route the rewrite accordingly.                      | Avoids integrity-as-wholeness category errors.                    |
| **CC-A6H-11 (Reference level).**           | On normative or Working-Model surfaces, authors SHALL state whether a wholeness claim is about the referent holon, a description episteme, a publication unit or carrier, a work occurrence, or an evidence carrier whenever that distinction affects relation choice, completeness meaning, or validation. | Prevents description-publication and referent drift plus A.15 level errors.          |

