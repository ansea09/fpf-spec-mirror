---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__002_problem-frame.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:1 — Problem frame"
line_start: 52822
line_end: 52876
dependencies:
  - "A.10"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3.3"
  - "B.2.5"
  - "B.3"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.TGA-FLOW-REL"
  - "E.18"
  - "G.6"
keywords:
  - "control layer"
  - "control-structure view"
  - "controller/plant"
  - "layered control architecture"
  - "proof overread"
  - "rate band"
  - "supervisor loop"
---

### C.30.LCA:1 - Problem frame

Use this pattern when an architecture description uses a control-stack, supervisor-loop, controller/plant, planner/regulator, observer/estimator, feedback-loop, multi-rate control, or Layered Control Architecture cue to explain how a grounded holon is controlled, observed, regulated, supervised, or protected.

The first-minute working situation is ordinary engineering talk: a diagram says the supervisor watches a subsystem, a controller regulates a plant, an observer estimates state, a planner gives references to a lower-rate controller, or a policy/control relation changes allowed controller behavior. The useful first move is not to accept the diagram as proof. The useful first move is to recover a `ControlStructureView@Context`: which architecture claim is being described, which control roles and relations are present, which rates or declared control layers are live, which feedback or externality boundaries are named, and which exact governing FPF pattern carries any stability, safety, evidence, gate, causal, or assurance claim kind.

What goes wrong if C.30.LCA is missed: a control diagram becomes proof of stability, safety, causality, evidence sufficiency, gate validity, or assurance; layer and level labels start carrying undeclared scope; and `B.2.5`, Transduction Graph Architecture (TGA), or Layered Control Architecture (LCA) prose is overread as control adequacy.

What C.30.LCA buys in practice: the practitioner can keep useful controller, plant, observer, regulator, supervisor, feedback, rate, and control-layer language while recovering the control-structure view and the exact governing pattern that carries any proof or exact claim.

Not this pattern when the live issue is only a general TGA path slice, a function description, a module boundary, a measurement head, a causal intervention, or a safety case. Use `C.30.TGA-FLOW-REL` for flow/transduction structure relation, `A.6.F` for function wording repair, the exact module/interface repair pattern for module-interface structure, `C.16` or an admitted characteristic/measurement receiving pattern for measured characteristics, `C.28` for causal-use claims, and `B.3`/`A.10`/`G.6` for assurance or evidence claim.

The governed object is one control-structure view of `ArchitectureOf@Context`, not the controlled holon itself, not a proof, and not the architecture as a whole. Ordinary use may stop with a typed control-structure view note:

```text
ControlStructureViewNote ordinary minimum:
  architecture claim or described holon plus context:
  one control relation:
  loop posture: closed | one-way | unclear:
  layer or rate label live?: yes | no:
  proof, evidence, causal, gate, or assurance governing pattern if live:
  stop condition:
```

The full `ControlStructureView@Context` opens when the live control claim needs declared roles, relations, rates, control-layer labels, boundary refs, or explicit exact governing pattern applications beyond that note.

Use a `SafetyLossControlStructureNote` when safety wording is live but the practitioner first needs the architecture-side loss-control structure, not a safety-case verdict:

```text
SafetyLossControlStructureNote:
  lossOrHarm:
  hazardOrUnsafeState:
  unsafeControlActionOrMissingControl:
  controlledProcessOrPlantRef:
  controlConstraintRef:
  feedbackOrObservabilityBoundary:
  timingOrRateBoundary:
  operationalDesignScopeOrMisuseScope:
  foreseeableMisuseRefs?:
  architectureStructureKindRefs:
    ControlStructure | ConstraintRequirementStructure |
    SecurityTrustBoundaryStructure | InformationDataStructure |
    EvidenceAssuranceStructure
  governingPatternApplicationRefs:
    A.3.3 dynamics, C.27 temporal or rate,
    C.28 causal-use, A.10/G.6 evidence,
    B.3 assurance, A.20/A.21 gate
  nonAdmissibleUse:
    not safety proof, not safety-case verdict, not regulatory acceptance
```

The note gives a positive first architecture move: find the loss-control structure, controlled process or plant, constraint, foreseeable misuse, operational design scope, and action-relevant boundary. It does not replace evidence, assurance, gate, causal, dynamics, or temporal support.



