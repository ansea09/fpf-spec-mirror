---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:2"
section_title: "Context"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__004_context.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:2 — Context"
line_start: 45793
line_end: 45804
dependencies:
  - "A.2.6"
  - "C.2.1"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.A"
  - "F.9"
keywords:
---

### C.3.4:2 - Context

C.3.1 and C.3.2 say what claims classify; A.2.6 says where claims hold. A procedure may still tailor use for a compliance procedure, product line, or cohort without changing the kind.

Three objects remain distinct:

1. `KindUseAdaptationDeclaration` states one named use of a base kind.
2. `KindUseAdaptationJudgment` is the three-valued result for one admissible candidate under pinned declaration and signature editions.
3. `KindUseAdaptationCorrespondenceDeclaration` records how one exact source declaration corresponds to one exact target declaration when their constraints or vocabulary bindings differ.

The third object is a C.2.1 declaration episteme. Its effective scheme makes source, target, and rule designations interpretable. It is not an executable adapter, mapping Method, representation correspondence, obtaining F.9 relation, `KindBridge`, or target judgment.

