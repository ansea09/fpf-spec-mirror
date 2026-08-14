---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:2"
section_title: "Context"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__004_context.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:2 — Context"
line_start: 45319
line_end: 45330
dependencies:
  - "A.2.6"
  - "C.2.1"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.A"
  - "F.9"
keywords:
  - "base KindSignature"
  - "candidate-feature constraint"
  - "correspondence declaration"
  - "kind-use adaptation declaration"
  - "three-valued judgment"
  - "vocabulary binding"
---

### C.3.4:2 - Context

C.3.1 and C.3.2 are used to say what claims quantify over. A.2.6 is used to say where claims hold. A procedure may still need a local use of a kind for, for example, a compliance procedure, product line, or cohort. `KindUseAdaptationDeclaration` supplies that tailoring without changing the kind or its Scope.

Three objects remain distinct:

1. `KindUseAdaptationDeclaration` states one named local use of a base kind.
2. `KindUseAdaptationJudgment` is the three-valued result for one candidate under pinned declaration and signature editions.
3. `KindUseAdaptationCorrespondenceDeclaration` states deterministic correspondence and loss between two exact adaptation declarations when their constraints or vocabulary bindings differ.

The third object is a C.2.1 declaration episteme. It is not an executable adapter, mapping Method, representation correspondence, obtaining F.9 Bridge, or target judgment.

