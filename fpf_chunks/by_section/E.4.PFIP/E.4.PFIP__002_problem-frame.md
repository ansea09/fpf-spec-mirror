---
chunk_kind: "child"
pattern_id: "E.4.PFIP"
pattern_title: "Principle-Framework Publication Integration and Preservation"
section_id: "E.4.PFIP:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFIP/E.4.PFIP__002_problem-frame.md"
commit_sha: "6226816d8005a4c8ee3af338bb3752f6732449a9"
heading_path:
  - "E.4.PFIP — Principle-Framework Publication Integration and Preservation"
  - "E.4.PFIP:1 — Problem frame"
line_start: 102116
line_end: 102138
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

Use this pattern during assembly of accepted changes into a candidate FPF, DPF, or LPF publication when the maintainer must answer either of these questions:

1. Did the candidate incorporate every accepted source contribution with its intended meaning and use?
2. Did the candidate preserve the useful content and selected structure of the predecessor publication outside accepted changes?

Use it especially when a publication form is replaced, split, merged, added, retired, or assigned another bounded use. A clean build, matching source files, or a readable candidate cannot answer the second question.

The primary reader is a framework maintainer or integrator preparing one candidate publication. The primary `EntityOfConcern` is one candidate FPF, DPF, or LPF edition being assembled for one declared publication use. The method returns a preservation conclusion about that edition. Files and build results are construction means or evidence.

**Begin here.** Identify the edition and the publication question. For incorporation of a named contribution, follow its meaning into the expressions and receiving uses on which that conclusion depends. For predecessor preservation, compare the expressions whose continuity is claimed. For a full edition these sets cover the candidate, all accepted contributions and its predecessor under the declared publication use.

The first result is a preservation conclusion for the declared use. It names losses, repairs, accepted content changes or retirements, unexpected additions, blockers, and unresolved correspondences or content decisions. Keep the complete comparison checkable. Ordinary retained content needs no positive prose row.

A maintainer can incorporate an accepted change while preserving unrelated predecessor content and assess a changed form while distinguishing the form, carrier, edition, and content.

**Related work.** Use `E.8` to author one pattern, `E.24.PUB` to identify publication, expression, and bearing relations, `E.17` to select reader-facing forms, `E.11` to design the public entry, `E.4.DPF.DA` to evaluate a DPF or LPF package, and `E.2.DA` to evaluate whole-FPF adequacy.

A responsible maintainer uses the local construction and release methods for repository operations and decisions to accept, admit, release, or land a publication.

For a whole first publication, compare its accepted sources, inspect its complete inventory, check changed public entries and direct consumers, and apply the package evaluation. A request about incorporation of one contribution has the narrower comparison stated above.

