---
chunk_kind: "child"
pattern_id: "A.6.6"
pattern_title: "Base Declaration Discipline - Direct relation first; reusable declaration only when needed"
section_id: "A.6.6:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.6/A.6.6__006_archetypal-grounding.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "A.6.6 — Base Declaration Discipline - Direct relation first; reusable declaration only when needed"
  - "A.6.6:5 — Archetypal Grounding"
line_start: 19828
line_end: 19877
dependencies:
  - "A.10"
  - "A.14"
  - "A.2.4"
  - "A.6.0"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "A.6.6"
  - "A.6.REL"
  - "C.2.1"
  - "E.10"
  - "F.17"
  - "F.18"
  - "F.9"
keywords:
---

### A.6.6:5 - Archetypal Grounding

#### A.6.6:5.1 - System archetype: calibration to a standard

**Tell.** A lab instrument channel `TC‑17` is described as “anchored to ITS‑90”. Later, the reference standard is swapped, the phrase “still anchored” is kept, and the applicability window silently expands. Downstream work disagrees and nobody can reconstruct what changed.

**Show.** First state the direct assertion: `TC-17 is calibrated to ITS-90 for rig R3 over 0–200 °C during the stated calibration interval.` Apply the calibration predicate and stop there if this answers the use. When a later publication or comparison needs the exact assertion edition, show the same claim in an optional scoped record:

```
BD#Calib_TC17_v5 :=
〈 dependent    = ThermocoupleChannelRef(TC-17),
base         = StandardRef(ITS-90 / CalStd-2025-09),
directRelationKind = calibratedTo,
assertionPolarity  = affirmative,
scope        = WorkScope{rig=R3, range=[0..200]°C},
gammaTime          = interval[2025-09-01, 2026-03-01] 〉
```

When a later decision relies on this assertion, cite the exact A.2.4 evidence-use relation from the calibration-certificate episteme to the assertion. Use A.10 only if that decision also needs the producing Work, operation result, carrier, provenance, or currentness path. Then distinguish changes by what actually changed:

* New standard ⇒ **rebase** + **refreshWitnesses**.
* Wider applicability window ⇒ **retime** and likely **refreshWitnesses**.
* Relation-kind change (“not calibration, just normalisation”) ⇒ **changeDirectRelationKind** is not an edit; mint a new assertion or declaration and relate it to the prior one through continuity.

#### A.6.6:5.2 - Episteme archetype: an evaluation result used as evidence

**Tell.** A report says that model M improved accuracy by 4%. The team points to `EvalRun-2025-10-12`, but that Work occurrence is neither the claim nor an evidence relation, and its log carrier does not become evidence merely by being attached.

**Show.** First identify the result episteme that states the measured comparison and the target claim about the 4% improvement. State the exact A.2.4 evidence-use relation between that episteme and claim, including the relevant ClaimScope, polarity, window, and receiving use. If the decision also needs replayable source, carrier, provenance, currentness, or bounded-reliance information, use A.10 to cite the evaluation Work, its actual operation-result binding, the result episteme, the log carrier, and their independently obtaining direct relations.

Stop with the short evidence-use statement when it answers the question. No `validatedBy(claim, Work)` edge or scoped base-declaration record is required. If a project later needs a reusable evidence-relation declaration, that direct relation must first have its own participant meanings, predicate, applicability, and occurrence-identity rule.

#### A.6.6:5.3 - Structural archetype: constructive grounding of a model edge

**Tell.** A structural edge is published (“A componentOf B”) without a constructor trace. It becomes treated as “obvious”, while the construction chain is not recoverable.

**Show.** First state and test the direct `tv:groundedBy` assertion between the model edge and constructor trace. Stop when that assertion answers the use. If a publication needs a stable assertion edition with its current qualifiers, it may represent that C.2.1 episteme as:

```
BD#EdgeGrounding_ComponentOf_17 :=
〈 dependent    = WMEdgeRef(Edge:componentOf#17),
base         = TraceRef(Γ_m:ComposeCAL#c17),
directRelationKind = tv:groundedBy,
assertionPolarity  = affirmative,
scope        = PublicationScope{view=WMCardLite, system=S, line=L3},
gammaTime          = snapshot(2025-11-02) 〉
```

The exact trace reference names the relevant constructor trace. If another use relies on the assertion that the grounding relation obtains, cite its exact evidence-use and provenance relations separately. This example shows why “grounding” must be disambiguated: here it is a declared constructive relation with an explicit base (trace), not a vague claim of “stability”.

