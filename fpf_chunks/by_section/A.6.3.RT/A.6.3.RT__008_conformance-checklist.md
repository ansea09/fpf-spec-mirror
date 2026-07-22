---
chunk_kind: "child"
pattern_id: "A.6.3.RT"
pattern_title: "Representation-Scheme Transition: EntityOfConcern-Preserving Representation-Scheme Transition"
section_id: "A.6.3.RT:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.RT/A.6.3.RT__008_conformance-checklist.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.6.3.RT — Representation-Scheme Transition: EntityOfConcern-Preserving Representation-Scheme Transition"
  - "A.6.3.RT:7 — Conformance Checklist"
line_start: 13786
line_end: 13825
dependencies:
  - "A.10"
  - "A.15"
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

### A.6.3.RT:7 - Conformance Checklist

A conformance check is retained only if it changes the next admissible use of the shifted representation, blocks a concrete overclaim, or preserves a source relation or exact return condition needed for the declared admissible use.

#### A.6.3.RT:7.1 - RT-Core ordinary checks

1. **CC-RT-1 — Same EntityOfConcern remains explicit.**
   The case preserves `entityOfConcernRef` without special pleading.
2. **CC-RT-2 — Representation shift is the right family.**
   The result is genuinely a representation-scheme or reasoning-medium shift rather than mere textual rewrite, explanation work, carrier work, or changed EntityOfConcern.
3. **CC-RT-3 — Admissible and non-admissible use are visible.**
   The ordinary use field set states the source representation or publication, the receiving representation or rendering, preservation of the same `entityOfConcernRef`, the source claim or commitment preserved for the intended use, the representation-scheme or reasoning-medium change, the admissible user action, and the downstream use not made admissible by this representation shift.
4. **CC-RT-3a — Relation, transition description, and source-relation reference remain distinct.**
   The `RepresentationSchemeTransitionRelation@Context` carries its exact RelationSignature and source-to-receiving direction. `RepresentationSchemeTransitionDescription@Context` has that relation as its EntityOfConcern and carries deltas, loss or recoverability, use, and return claims. Each `RepresentationTransitionSourceRelationReference@Context` instead has one source relation instance as its EntityOfConcern and carries its exact kind, signature, and governing-pattern reference.
5. **CC-RT-8 — Preserve-vs-retarget governing pattern is explicit.**
   If the case fails the ordinary checks, the governing pattern for the changed claim is named explicitly (A.6.3.CR, E.17.EFP, A.6.3.CSC, A.6.4, carrier work under A.7, or another governing pattern).
6. **CC-RT-14 — Functional-description publication overread is blocked.**
   Functional diagrams, tables, screens, exports, parser results, and OCR results are kept separate from performed `U.Work`, gate passage, evidence, engineering justification, supervisory architecture, control architecture, and carrier work. OCR-style extraction and parsing-style extraction start with `A.7`; same-entity representation work stays here only when source-relation chain, same EntityOfConcern, representation-scheme change, and loss notes remain visible.

#### A.6.3.RT:7.2 - RT-Conditional checks

1. **CC-RT-4 — Factor, reasoning-medium, and mode deltas are explicit when claim-bearing.**
   `representationFactorDelta`, `inferenceRegimeDelta`, and any claim-bearing `semioticModeShift` are explicit when they materially shape review or misuse risk.
2. **CC-RT-5 — Extended delta factors are explicit when claim-bearing.**
   `salienceShift`, `topologyShift`, `admissibleUseShift`, `calibrationShift`, and `interactivityShift` are named whenever they materially shape review or misuse risk.
3. **CC-RT-6 — Decode-mediated cases carry additional recoverability evidence.**
   If the case is decode-mediated, latent-representation-facing, or distributed-representation-facing, the pinned source claim or publication, decoding relation or access relation, recoverability evidence, admissible-use value, and remaining user action are explicit.
4. **CC-RT-7 — Loss, provenance, pinning, and reliability are explicit when needed.**
   Losses, provenance, pinning, and reliability transport are stated or inherited by visible pinned reference when external reliance, dispute, gate, assurance, evidence, or cross-context use is being claimed.
5. **CC-RT-9 — Direct vs correspondence split is explicit when correspondence is doing work.**
   The case states whether it is direct or correspondence-mediated; if correspondence-mediated, `CorrespondenceModelRef` is explicit.
6. **CC-RT-10 — Non-default face and rendering admissibility is explicit.**
   Any `InteropCard`, `AssuranceLane`, gate-bearing, or decode-bounded use states governing publication-face admissibility and keeps same-EntityOfConcern continuity visible.
7. **CC-RT-11 — Decode-mediated same-entity source-relation chain is explicit.**
   A decode-mediated case states the source-relation chain from the receiving rendering back to already pinned and provenance-bearing source `U.Episteme` claim graph for the same EntityOfConcern.
8. **CC-RT-12 — No hidden bridge or face-family inflation.**
   The case makes clear that representation work does not by itself grant bridge, substitution, or comparative-review licence and does not create a new face family.
9. **CC-RT-13 — Reopen triggers are explicit when recoverability, admissibility, or primary mode changes.**
   If recoverability assumptions, pins, provenance, correspondence witness, publication-face admissibility, or the primary semiotic mode change, the case records the reopen trigger explicitly.

