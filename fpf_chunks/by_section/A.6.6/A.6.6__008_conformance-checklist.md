---
chunk_kind: "child"
pattern_id: "A.6.6"
pattern_title: "Base Declaration Discipline - Direct relation first; reusable declaration only when needed"
section_id: "A.6.6:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.6/A.6.6__008_conformance-checklist.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "A.6.6 — Base Declaration Discipline - Direct relation first; reusable declaration only when needed"
  - "A.6.6:7 — Conformance Checklist"
line_start: 19888
line_end: 19905
dependencies:
  - "A.10"
  - "A.14"
  - "A.2.4"
  - "A.2.6"
  - "A.6.0"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "A.6.6"
  - "A.6.REL"
  - "A.7"
  - "C.2.1"
  - "C.3.3"
  - "E.10"
  - "E.18"
  - "E.24.UK"
  - "E.8"
  - "F.0.1"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.9"
  - "U.KindBridge"
  - "U.Transfer"
keywords:
---

### A.6.6:7 - Conformance Checklist

An A.6.6 use conforms when the checks for its selected branch pass:

1. **CC-BD-1 - Direct assertion first.** The actual dependent, base, direct relation, and readable affirmative or negative assertion are recoverable. The direct pattern supplies the predicate; a record or label does not.
2. **CC-BD-2 - Ordinary stop.** If that assertion answers the receiving question, no SlotSpecs, declaration record, witnesses, edition, occurrence identity, or assurance package is required.
3. **CC-BD-3 - Reusable declaration is demand-driven.** A `RelationSignature` satisfies the reuse test in A.6.6:4.3 and applies only to an already admitted relation kind.
4. **CC-BD-4 - Assertion and occurrence stay separate.** A scoped witnessed record, when used, is a C.2.1 assertion or description episteme. It neither is nor creates the world-side relation occurrence.
5. **CC-BD-5 - Qualifiers are local.** Scope and time are explicit when the selected predicate or named receiving use depends on them; they are not a universal field kit. `Gamma_time` is not used as a proxy for evidence freshness.
6. **CC-BD-6 - Evidence ontology is direct.** Evidence use follows A.2.4 and A.10. Work, operation result, result episteme, carrier, provenance, evidence-use relation, and reliance remain separate; no generic `verifiedBy` or `validatedBy` edge is minted.
7. **CC-BD-7 - Crossings are conditional.** An actual relation between two exact F.17 cells uses F.9 only when its predicate obtains and keeps the bounded-use claim separate. A ReferencePlane crossing uses its applicable plane relation. One creates neither the other.
8. **CC-BD-8 - No silent retyping or direction flip.** Participant kinds and direction follow the direct relation. A mismatch is repaired by the applicable narrowing, Bridge, retargeting, or direct relation rule, not by renaming an endpoint.
9. **CC-BD-9 - Plain language remains sufficient.** Ordinary relation-specific prose is preferred. Functional or arrow notation is optional and may not replace the readable assertion.
10. **CC-BD-10 - Metaphors do not become ontology.** `anchor`, `ground`, `attach`, and `support` remain source-word triggers unless they name an already reserved primitive; no metaphor-headed fallback kind or relation is minted.
11. **CC-BD-11 - Meaning lane stays separate.** Source-local meaning starts with F.0.1 and uses F.17 only when a durable sense address or basis relation is needed; it is not a base-declaration record.
12. **CC-BD-12 - Change claims name the changed object.** Editing an assertion or reusable declaration changes that episteme. An actual relation change requires the direct relation's own change predicate and any separately current Work.
13. **CC-BD-13 - Optional history is proportional.** `declareBase`, `rebase`, `rescope`, `retime`, or `refreshWitnesses` is used only when a named receiver needs that declaration history. The label establishes no world-side fact.

