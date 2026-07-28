---
chunk_kind: "child"
pattern_id: "C.31.ASAP"
pattern_title: "Architecture Scale-Amenability Preference"
section_id: "C.31.ASAP:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31.ASAP/C.31.ASAP__002_problem-frame.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "C.31.ASAP — Architecture Scale-Amenability Preference"
  - "C.31.ASAP:1 — Problem frame"
line_start: 63060
line_end: 63087
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
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
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "RG"
  - "ScaleClaimTriage"
  - "architecture alternatives"
  - "architecture scale preference"
  - "coarse-graining"
  - "platform scale claim"
  - "scale amenability"
  - "scale variable"
  - "scale window"
  - "source-return condition"
  - "waiver reason"
---

### C.31.ASAP:1 - Problem frame

Use this pattern when a practitioner compares architecture alternatives under a declared scale variable or scale window and needs to avoid treating a modularity label, platform label, product-line label, reusable-structure share, or coarse-graining metaphor as an automatic scale-preference claim.

The first useful move is `ScaleClaimTriage`:

```text
ScaleClaimTriage:
  architectureAlternativeSetRef:
  scaleVariableRef:
  scaleWindowRef:
  claimedPreferenceUnderScale:
  slopeEvidenceRef, scaleProbeEvidenceRef, or noProbeReason:
  expectedStableOrImprovingStructure:
  exceptionGrowthRisk:
  sourceReturnCondition:
  relatedClaimGovernanceIfClaimed:
  stopCondition:
```

Ordinary use starts by naming the alternatives, the scale variable, the scale window, the claimed preference under scale, the available slope or scale-probe evidence or no-probe reason, the expected stable or improving structure, and the exception growth risk. Use `ArchitectureScaleAuditRecord@Project` only when the scale preference is being used to affect a comparison, selected set, publication, assurance input, or architecture decision.

What goes wrong if C.31.ASAP is missed: "modular", "platform", "product line", "reusable", "general", "open", "coarse-grained", or "RG-like" becomes a shortcut for a scale-preference claim; a locally hand-engineered solution is called debt even when safety, law-domain, or mission constraints justify it; exception growth is hidden until the architecture is already expensive to change; and coarse descriptions keep losing lower-scope safety or semantic distinctions without a source-return condition.

What C.31.ASAP buys in practice: the practitioner can say what is being scaled, where the scale claim holds, what structure is expected to remain stable or improve, what exceptions are allowed, what evidence or no-probe reason exists, which scale-preference claim stays in C.31.ASAP, and which governing pattern governs any lens-use, evidence, assurance, selection, or decision claim being made.

Not this pattern when the question under repair is only module-interface relation repair, modularity-characteristic selection, reusable-structure accounting, mathematical-lens use, scale-law adequacy, method preference under general BLP, candidate architecture generation, selected-set return, or final local choice. Use `A.6.M`, `C.31`, `C.31.RSA`, `C.29`, `C.18.1`, `C.19.1`, `C.32`, `G.5`, `G.9`, or `C.11` as appropriate. C.31.ASAP governs architecture scale-preference claims; it does not select the architecture, prove the scale law, or certify the project.

