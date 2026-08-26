---
chunk_kind: "child"
pattern_id: "E.4.PFIP"
pattern_title: "Principle-Framework Publication Integration and Preservation"
section_id: "E.4.PFIP:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFIP/E.4.PFIP__002_problem-frame.md"
commit_sha: "d064720b072b822cbb2f1d41e555cf08e2904f11"
heading_path:
  - "E.4.PFIP — Principle-Framework Publication Integration and Preservation"
  - "E.4.PFIP:1 — Problem frame"
line_start: 70244
line_end: 70262
dependencies:
  - "C.2.1"
  - "C.33"
  - "C.34"
  - "E.11"
  - "E.17"
  - "E.24.PUB"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.4.FPF"
  - "E.4.PFIP"
  - "E.8"
keywords:
---

### E.4.PFIP:1 - Problem frame

Use this pattern when accepted changes are being assembled into a candidate FPF, DPF, or LPF publication and the maintainer must answer either of two questions:

1. Did the candidate faithfully incorporate every accepted source contribution?
2. Did the candidate preserve the useful content and selected structure of the predecessor publication outside accepted changes?

Use it especially when a publication form is replaced, split, merged, added, retired, or assigned another bounded use. A clean build, matching source files, or a readable candidate cannot answer the second question.

The primary working reader is a framework maintainer or integrator preparing one candidate publication. The primary `EntityOfConcern` is one candidate FPF, DPF, or LPF edition being assembled for one declared publication use. The method returns a preservation conclusion about that edition; files and build results are construction means or evidence rather than the edition being assessed.

**First useful move.** Name the candidate framework edition and publication use, identify every accepted source contribution for this candidate, and list the predecessor and candidate publication-form expressions whose continuity or change is claimed. Then select the source-to-candidate comparison and the applicable predecessor-preservation branch.

The first useful result is a bounded preservation conclusion. It names losses, repairs, accepted content changes or retirements, unexpected additions, blockers, and unresolved correspondences or content decisions. Ordinary retained content needs no positive prose row, but the complete comparison must remain checkable.

**What this buys.** An accepted change can be incorporated without erasing unrelated predecessor content, and a changed publication form can be assessed without confusing form, carrier, edition, or content.

**Not this pattern when.** Use `E.8` to author one pattern, `E.24.PUB` to identify publication, expression, and bearing relations, `E.17` to select reader-facing forms, `E.11` to design the public entry, `E.4.DPF.DA` to evaluate a DPF or LPF package, and `E.2.DA` to evaluate whole-FPF adequacy. A responsible maintainer uses the local construction and release methods for repository operations and decisions to accept, admit, release, or land a publication. A new publication with no predecessor uses only the accepted-source comparison, complete candidate inventory, and applicable package evaluation.

