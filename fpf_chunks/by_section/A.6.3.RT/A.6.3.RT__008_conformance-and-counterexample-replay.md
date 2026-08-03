---
chunk_kind: "child"
pattern_id: "A.6.3.RT"
pattern_title: "Representation-Scheme Transition: EntityOfConcern-Preserving Representation-Scheme Transition"
section_id: "A.6.3.RT:7"
section_title: "Conformance and counterexample replay"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.RT/A.6.3.RT__008_conformance-and-counterexample-replay.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "A.6.3.RT — Representation-Scheme Transition: EntityOfConcern-Preserving Representation-Scheme Transition"
  - "A.6.3.RT:7 — Conformance and counterexample replay"
line_start: 14763
line_end: 14794
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.20"
  - "A.21"
  - "A.3.3"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.3.NAR"
  - "A.6.4"
  - "A.7"
  - "B.3"
  - "B.5.2"
  - "C.2.1"
  - "C.2.7"
  - "C.26"
  - "C.27"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.18"
  - "F.18"
  - "F.9"
  - "F.9.1"
keywords:
---

### A.6.3.RT:7 - Conformance and counterexample replay

A check is retained only if it changes the next admissible use, blocks a concrete overclaim, or preserves an exact source or return relation.

#### A.6.3.RT:7.1 - RT-Core

1. **CC-RT-1 — Exact endpoints.** `X` and `Y` are independently constituted C.2.1 epistemes; each exact claim content, EntityOfConcern, and effective `U.ReferenceScheme` is recoverable. A model label, graph, display, publication occurrence, form, carrier, or readable output substitutes for neither.
2. **CC-RT-2 — Same EntityOfConcern, no hidden retargeting.** `EntityOfConcern(X)=EntityOfConcern(Y)` exactly. Otherwise apply A.6.4.
3. **CC-RT-3 — Exact construction.** The declaration states `v : X -> Y`, the claim-content rule, relation between effective schemes, preservation, loss, prohibited strengthening, and applicability.
4. **CC-RT-4 — Six-participant occurrence only at its trigger.** A positive `RepresentationSchemeTransitionRelation@Context` has the exact A.1.1 `BoundedModelUseStructure`, preserved EntityOfConcern, `X`, `Y`, and exact two scheme-description epistemes, plus actual representation-transformation Work satisfying section 4.1.a.1. No discarded generic context kind/reference, description-context field, scheme label, or Work record fills a participant.
5. **CC-RT-5 — Occurrence, Work, and description stay distinct.** The participant tuple identifies the relation occurrence; system, role assignment, Work, method, operation bindings, and production claim stay with their direct owners; the transition-description episteme has its own C.2.1 identity.
6. **CC-RT-6 — Exact correspondence dependencies.** Every correspondence-mediated dependency resolves to exact source epistemes and governed relations. Similar content, graph adjacency, a correspondence model, or scheme difference proves none.
7. **CC-RT-7 — Use and return.** Preserved content, explicit loss or recoverability, admissible use, non-admissible downstream use, and return to exact `X` or governed source relations are visible.
8. **CC-RT-8 — Neighbors remain separate.** C.29 representation is opened only for a current mathematical lens; viewpoint and `U.View` membership require E.17.0; grounding, publication occurrence, form, carrier, evidence, assurance, bridge, gate, and receiving use keep their direct owners.

#### A.6.3.RT:7.2 - Counterexample replay

| Case | Required result |
| --- | --- |
| Preserve vs retarget | Equal exact EntityOfConcern permits the A.6.3 test; a changed EntityOfConcern exits to A.6.4 even when labels or content overlap. |
| Same scheme | If effective scheme and reasoning medium are unchanged and only wording changes, use A.6.3.CR; do not invent RT. |
| Different scheme | Scheme difference is explicit but does not itself establish `v`, correspondence, Work, Bridge, or the six-participant occurrence. |
| Candidate vs `U.View` | A valid receiving episteme and RT construction may still fail E.17.0 conformance and remain a non-View candidate. |
| Publication/form/carrier | Making `X` or `Y` available, changing its form, or replacing its carrier does not replace an endpoint or reidentify an unchanged construction or occurrence. |
| Work without conservativity | A system may actually produce `Y`, yet unsupported strengthening or unreported loss blocks the RT construction and relation occurrence. |
| Grounded source, ungrounded receiver | Grounding of `X` does not transfer through `v`; `Y` has an `EpistemeEmpiricalGroundingRelation` only when its own exact covered claims and grounding conditions make one obtain. |
| Selected structure overread | The exact `BoundedModelUseStructure` is one participant only in the triggered `...@Context` occurrence; it is not the transformer, viewpoint, `U.View`, representation, publication, or EntityOfConcern. |
| Cross-scheme dependency without transition or Bridge | If neither the exact six-participant transition occurrence required by that dependency use nor an exact applicable F.9 Bridge and bounded-use/reliance path exists, block the cross-scheme dependency. Scheme difference, similar content, a description, or C.29 output cannot fill the gap. |
| Description or C.29 output | Editing the transition-description episteme or mathematical output does not change the occurrence unless one of the exact six participants changes. |

Reopen only the affected item. After a bounded repair, replay its local counterexample and then run this complete table once for the final package; do not restart the full file after every local correction.

