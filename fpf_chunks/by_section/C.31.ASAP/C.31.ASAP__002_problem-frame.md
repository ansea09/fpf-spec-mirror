---
chunk_kind: "child"
pattern_id: "C.31.ASAP"
pattern_title: "Which Architecture Is Preferable Under Scale? (Scale Amenability)"
section_id: "C.31.ASAP:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31.ASAP/C.31.ASAP__002_problem-frame.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "C.31.ASAP — Which Architecture Is Preferable Under Scale? (Scale Amenability)"
  - "C.31.ASAP:1 — Problem frame"
line_start: 79337
line_end: 79399
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
  slopeEvidenceRef, scaleProbeEvidenceRef, or noProbeReason:
  expectedStableOrImprovingStructure:
  exceptionGrowthRisk:
  sourceReturnCondition?:
  relatedClaimGovernanceIfClaimed:
  stopCondition:
```

Ordinary use starts by naming:

- the alternatives and described holon;
- the `U.ClaimScope` and relevant A.2.6 `U.ContextSlice` membership;
- the scale variable and scale window;
- the claimed preference under scale;
- the available slope or scale-probe evidence or no-probe reason;
- the expected stable or improving structure; and
- the exception-growth risk.

Name `modelUseStructureRef` only when one independently selected `BoundedModelUseStructure` changes this receiving interpretation; it never replaces the claim scope.

Use `ArchitectureScaleAuditRecord@Project` when those distinctions help retain or examine the preference for its receiving use. Sharing an already adequate account needs no new form.

What goes wrong if C.31.ASAP is missed:

- "modular", "platform", "product line", "reusable", "general", "open", "coarse-grained", or "RG-like" becomes a shortcut for a scale-preference claim;
- a locally hand-engineered solution is called debt even when safety, law-domain, or mission constraints justify it;
- exception growth is hidden until the architecture is already expensive to change; and
- coarse descriptions keep losing lower-scope safety or semantic distinctions without a source-return condition.

What C.31.ASAP buys in practice: the practitioner can say what is being scaled, where the scale claim holds, what structure is expected to remain stable or improve, what exceptions are allowed, what evidence or no-probe reason exists, which scale-preference claim stays in C.31.ASAP, and which pattern defines or tests any lens-use, evidence, assurance, selection, or decision claim being made.

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

