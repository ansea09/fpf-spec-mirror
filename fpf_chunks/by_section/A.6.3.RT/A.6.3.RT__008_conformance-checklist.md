---
chunk_kind: "child"
pattern_id: "A.6.3.RT"
pattern_title: "RepresentationTransduction — same-described-entity representation-scheme transition"
section_id: "A.6.3.RT:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.RT/A.6.3.RT__008_conformance-checklist.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "A.6.3.RT — RepresentationTransduction — same-described-entity representation-scheme transition"
  - "A.6.3.RT:7 — Conformance Checklist"
line_start: 11379
line_end: 11416
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.3.3"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.CSC"
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
  - "E.17.ID.CR"
  - "E.18"
  - "F.18"
  - "F.9"
  - "F.9.1"
  - "U.EffectFreeEpistemicMorphing"
  - "U.EpistemicRetargeting"
  - "U.EpistemicViewing"
keywords:
  - "diagram"
  - "notation shift"
  - "reasoning medium"
  - "recoverability"
  - "representation transduction"
  - "same-described-entity representation change"
  - "source tether"
  - "state-representation shortcut"
  - "table"
---

### A.6.3.RT:7 - Conformance Checklist

A conformance check is retained only if it changes the next admissible use of the shifted representation, blocks a concrete overclaim, or preserves a source/reopen path needed for the declared admissible use.

#### A.6.3.RT:7.1 - RT-Core ordinary checks

1. **CC-RT-1 — Same described entity remains explicit.**
   The case preserves `describedEntityRef` without special pleading.
2. **CC-RT-2 — Representation shift is the right family.**
   The result is genuinely a representation-scheme or reasoning-medium shift rather than mere textual rewrite, explanation work, carrier work, or changed described entity.
3. **CC-RT-3 — Admissible and non-admissible use are visible.**
   The ordinary use path states the source described entity, receiving described entity or preservation claim, the source claim or commitment preserved for the intended use, the representation-scheme or reasoning-medium change, the admissible reader action, and the downstream use not made admissible by this representation shift.
4. **CC-RT-8 — Preserve-vs-retarget handoff is explicit.**
   If the case fails the ordinary checks, the handoff target is explicit (`A.6.3.CR`, `E.17.EFP`, `A.6.3.CSC`, `A.6.4`, carrier work under `A.7`, or another governing pattern).
5. **CC-RT-14 — Functional-description publication overread is blocked.**
   Functional diagrams, tables, screens, exports, and parser/OCR results are kept separate from performed `U.Work`, gate passage, evidence, engineering justification, supervisory/control architecture, and carrier work. OCR/parsing starts with `A.7`; same-entity representation work stays here only when source tether, same described entity, representation-scheme change, and loss notes remain visible.

#### A.6.3.RT:7.2 - RT-Conditional checks

1. **CC-RT-4 — Factor, reasoning-medium, and mode deltas are explicit when load-bearing.**
   `representationFactorDelta`, `inferenceRegimeDelta`, and any load-bearing `semioticModeShift` are explicit when they materially shape review or misuse risk.
2. **CC-RT-5 — Extended delta factors are explicit when load-bearing.**
   `salienceShift`, `topologyShift`, `admissibleUseShift`, `calibrationShift`, and `interactivityShift` are named whenever they materially shape review or misuse risk.
3. **CC-RT-6 — Decode-mediated cases carry additional recoverability evidence.**
   If the case is decode-mediated or latent/distributed, the pinned source claim or publication, decode path or access route, recoverability evidence, admissible use-support value, and remaining reader action are explicit.
4. **CC-RT-7 — Loss, provenance, pinning, and reliability are explicit when needed.**
   Losses, provenance, pinning, and reliability transport are stated or inherited by visible pinned reference when external reliance, dispute, gate, assurance, evidence, or cross-context use is live.
5. **CC-RT-9 — Direct vs correspondence split is explicit when correspondence is doing work.**
   The case states whether it is direct or correspondence-mediated; if correspondence-mediated, `CorrespondenceModelRef` is explicit.
6. **CC-RT-10 — Non-default face/rendering admissibility is explicit.**
   Any `InteropCard`, `AssuranceLane`, gate-bearing, or decode-bounded use states governing publication-face admissibility and keeps same-entity support visible.
7. **CC-RT-11 — Decode-mediated same-entity entry tether is explicit.**
   A decode-mediated case states how the target rendering is tethered back to already pinned and provenance-bearing source `U.Episteme` claim graph for the same described entity.
8. **CC-RT-12 — No hidden bridge or face-family inflation.**
   The case makes clear that representation work does not by itself grant bridge, substitution, or comparative-reading licence and does not create a new face family.
9. **CC-RT-13 — Reopen triggers are explicit when recoverability, admissibility, or primary mode changes.**
   If recoverability assumptions, pins, provenance, correspondence support, target-face admissibility, or the primary semiotic mode change, the case records the reopen trigger explicitly.

