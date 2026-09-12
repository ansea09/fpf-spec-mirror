---
chunk_kind: "child"
pattern_id: "A.6.6"
pattern_title: "Base Declaration Discipline - Direct relation first; reusable declaration only when needed"
section_id: "A.6.6:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.6/A.6.6__012_sota-echoing.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "A.6.6 — Base Declaration Discipline - Direct relation first; reusable declaration only when needed"
  - "A.6.6:11 — SoTA-Echoing"
line_start: 20168
line_end: 20191
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

### A.6.6:11 - SoTA-Echoing

1. **RDF-star and statement qualification.**
   **Adopt/Adapt.** RDF-star/SPARQL-star explored attaching qualifiers/provenance to statements and edges. RDF 1.2's Candidate Recommendation Snapshot of 7 April 2026 distinguishes representing a proposition from asserting that it holds. We adopt the “qualified statement” intuition, but adapt it by requiring an explicit relation kind and by making `Γ_time` and USM scopes explicit when the direct relation or receiving use needs them.
   *Primary sources:* [Hartig and Thompson, *Foundations of an Alternative Approach to Reification in RDF* (first submitted 2014)](https://arxiv.org/abs/1406.3399), retained as history and marked obsolete by its authors; [RDF 1.2 Concepts and Abstract Data Model, Candidate Recommendation Snapshot, 7 April 2026](https://www.w3.org/TR/2026/CR-rdf12-concepts-20260407/).

2. **Wikidata-style statements with qualifiers and references.**
   **Adopt/Adapt.** Wikidata statements separate a core statement from optional qualifiers and references. We adopt that separation and adapt it by making decision-relevant basis requirements explicit through exact evidence-use relations, with slots only for a genuinely reused declaration, and explicit scope/time where the assertion or time-dependent use needs them.
   *Primary source:* [Wikidata, Help:Statements](https://www.wikidata.org/wiki/Help:Statements).

3. **Metrology traceability and calibration competence.**
   **Adopt/Adapt.** Calibration is an operation relating a standard's quantity values and uncertainties to indications, then using that information to obtain measurement results. Metrological traceability is a property of a measurement result related to a reference through a documented calibration chain. We retain the need for documented calibration evidence and adapt time-dependent applicability through explicit `Γ_time` and the witnesses or pinned calibration records required by the assertion or receiving use.
   *Primary sources:* [JCGM VIM, calibration (2.39)](https://jcgm.bipm.org/vim/en/2.39.html) and [metrological traceability (2.41)](https://jcgm.bipm.org/vim/en/2.41.html); [ISO/IEC 17025:2017](https://www.iso.org/standard/66912.html), edition confirmed in 2023.

4. **Assurance case metamodels for claim–evidence structure.**
   **Adopt/Adapt.** SACM formalises claim/evidence structures and emphasises structured support relations. We adopt the idea that decision-relevant admissibility links should be explicit, and adapt it by using FPF’s scope/time discipline and by treating relation-kind elision as a first-order defect.
   *Primary source:* [OMG Structured Assurance Case Metamodel (SACM), version 2.3, October 2023](https://www.omg.org/spec/SACM/2.3).

5. **Objects over a base as a stable mathematical lens.**
   **Adopt/Adapt.** Modern category-theory texts make “objects over a base” (slice categories) a reusable pattern for “X relative to B”. We adopt that lens as the stable abstraction behind base declarations, and adapt it with explicit scope/time and witness semantics needed for engineering governance.
   *Primary source:* Riehl, *Category Theory in Context* (2016).

**SoTA binding note (informative):** the “object over a base” lens is the abstraction used to keep the pattern stable across domains (item 5).

