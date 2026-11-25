---
chunk_kind: "child"
pattern_id: "C.31.ASAP"
pattern_title: "Which Architecture Is Preferable Under Scale? (Scale Amenability)"
section_id: "C.31.ASAP:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31.ASAP/C.31.ASAP__002_problem-frame.md"
commit_sha: "423f9d3fef92bafec7b092b910e8ce056a0f607d"
heading_path:
  - "C.31.ASAP — Which Architecture Is Preferable Under Scale? (Scale Amenability)"
  - "C.31.ASAP:1 — Problem frame"
line_start: 79823
line_end: 79884
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.2.6"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18.1"
  - "C.19.1"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.31"
  - "C.31.RSA"
  - "C.32"
  - "C.32.PAD"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "architecture alternatives"
  - "architecture scale preference"
  - "coarse-graining"
  - "exception growth"
  - "scale amenability"
  - "scale probe"
  - "scale variable"
  - "scale window"
  - "waiver"
---

### C.31.ASAP:1 - Problem frame

Use this pattern when a practitioner compares architecture alternatives under a declared scale variable or scale window and needs to avoid treating a modularity label, platform label, product-line label, reusable-structure share, or coarse-graining metaphor as an automatic scale-preference claim.

First identify the alternatives, the scale variable and its window, and the grounds and limits of the proposed preference. An adequate ordinary account can finish; `ScaleClaimTriage` can retain it:

```text
ScaleClaimTriage:
  architectureAlternativeSetRef:
  describedHolonRef:
  claimScopeRef:
  selectedContextSliceRefs:
  modelUseStructureRef?:
  scaleVariableRef:
  scaleWindowRef:
  claimedPreferenceUnderScale:
  slopeEvidenceRef, scaleProbeEvidenceRef, comparisonBasisRef, or noProbeReason:
  expectedStableOrImprovingStructure?:
  exceptionGrowthRisk?:
  sourceReturnCondition?:
  relatedClaimGovernanceIfClaimed:
  stopCondition:
```

Ordinary use starts by naming:

- the alternatives and described holon;
- the `U.ClaimScope` and relevant A.2.6 `U.ContextSlice` membership;
- the scale variable and scale window;
- the claimed preference under scale and whose price, effort or other outcome the commission asks you to compare;
- the observations or derivation supporting the proposed scale behavior, or what remains open in their absence;
- the structural feature or exception behavior on which that preference depends, when it calls for either.

Name `modelUseStructureRef` only when one independently selected `BoundedModelUseStructure` changes this receiving interpretation; it never replaces the claim scope.

Use `ArchitectureScaleAuditRecord@Project` when those distinctions help retain or examine the preference for its receiving use. Sharing an already adequate account needs no new form.

What goes wrong if C.31.ASAP is missed:

- "modular", "platform", "product line", "reusable", "general", "open", "coarse-grained", or "RG-like" becomes a shortcut for a scale-preference claim;
- a locally hand-engineered solution is called debt even when safety, law-domain, or mission constraints justify it;
- exception growth is hidden until the architecture is already expensive to change; and
- coarse descriptions keep losing lower-scope safety or semantic distinctions without a source-return condition.

A practitioner can use the resulting account to say which architecture is preferable for the planned scale and criterion, which conditions support that judgement, and what could reverse it.

For questions limited to the following concerns, use the corresponding patterns instead of C.31.ASAP:

| Question | Pattern |
| --- | --- |
| Module-interface relation repair | `A.6.M` |
| Modularity-characteristic selection | `C.31` |
| Reusable-structure accounting | `C.31.RSA` |
| Mathematical-lens use | `C.29` |
| Scale-law adequacy | `C.18.1` |
| Method preference under general BLP | `C.19.1` |
| Candidate architecture generation | `C.32` |
| Selected-set return | `G.5` |
| Final local choice | `C.11` |

C.31.ASAP governs architecture scale-preference claims; it does not select the architecture, prove the scale law, or certify the project.

