---
chunk_kind: "child"
pattern_id: "A.6.3"
pattern_title: "Episteme viewing - EntityOfConcern-preserving episteme construction"
section_id: "A.6.3:5"
section_title: "Worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3/A.6.3__006_worked-cases.md"
commit_sha: "423f9d3fef92bafec7b092b910e8ce056a0f607d"
heading_path:
  - "A.6.3 — Episteme viewing - EntityOfConcern-preserving episteme construction"
  - "A.6.3:5 — Worked cases"
line_start: 18675
line_end: 18704
dependencies:
  - "A.13"
  - "A.15.1"
  - "A.15.PROD"
  - "A.6.0"
  - "A.6.2"
  - "A.6.3.CR"
  - "A.6.3.RT"
  - "A.6.4"
  - "C.2.1"
  - "C.29"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "E.24.PUB"
keywords:
---

### A.6.3:5 - Worked cases

#### A.6.3:5.1 - Safety-focused system description

The reviewer of plant S needs to know which hazards have a documented mitigation for the configuration under review. The source description X covers several configurations. Construct Y by selecting the hazards for the requested configuration and tracing each proposed mitigation to the conditions under which X links it to that hazard. A mitigation listed solely for another configuration leaves support open in this one. Y can report that gap. Both epistemes concern plant S. The selection rule and its conditions explain what the resulting account establishes. If the reviewer also commissions a `U.View` under safety viewpoint P, resolve P and establish `EpistemeViewpointConformanceRelation(Y,P)`.

#### A.6.3:5.2 - Directly authored view

Architecture episteme E is authored directly against maintainability viewpoint P and passes E.17.0 conformance. E is a `U.View` on that basis; no source-to-E viewing claim is needed for this result. A mathematical viewing relation may be established separately, including identity viewing on E. Any claim that the authoring used a source needs its own historical basis; the mathematical arrow does not supply it.

#### A.6.3:5.3 - Query result that fails conformance

Query Q constructs Y from source X while preserving the same system and making only licensed claims. Y omits one concern required by viewpoint P. A.6.3 construction is valid; E.17.0 conformance fails, so Y is not a view under P.

#### A.6.3:5.4 - Normalized publication card

X and Y are separately identified epistemes about morphism f. Y reorders claims and normalizes names without changing their interpretation. `NormalizeTechCard : X -> Y` is a direct viewing. For a repeat claim under the same scheme and normalization rules, identify the next normalization arrow `n_Y : Y -> Z`; establish `Z = Y` under C.2.1 and `compose(n_Y, NormalizeTechCard) ≃ NormalizeTechCard` under the substrate's declared arrow equivalence, with a fixture or proof.

A later publication occurrence makes Y available through a TechCard form. Y is called `U.View` only if it conforms to the publication viewpoint; the form and carrier remain separate.

#### A.6.3:5.5 - Cross-model coverage

Requirements episteme R and design episteme D concern system S. Realization relations connect requirements to design elements. A correspondence assertion episteme states those occurrences.

Receiving episteme Y selects only requirements with an obtaining realization relation. A.6.3 records the correspondence-mediated construction from the sources to Y; the assertion episteme and matrix representation remain separate from the realization occurrences.

#### A.6.3:5.6 - Retargeting boundary

X concerns pump P-14. A proposed Y concerns the whole cooling skid. Even if every Y claim is derived from X plus neighboring descriptions, A.6.3 does not apply because the EntityOfConcern changed. If declaring a retargeting arrow, use A.6.4. For a claimed receiving use, separately state its invariant, visible loss, use conditions and affirmative or negative proposition; assess that proposition against case facts when a current-case judgement is needed.

