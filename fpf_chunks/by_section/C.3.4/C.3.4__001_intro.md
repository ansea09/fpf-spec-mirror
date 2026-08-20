---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__001_intro.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:intro — Intro"
line_start: 45270
line_end: 45276
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

## C.3.4 - KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning

> **One-line summary.** A `KindUseAdaptationDeclaration` is a C.2.1 declaration episteme for one named local use of an exact base kind. It pins the base `KindSignature` edition, candidate-feature constraints, vocabulary bindings, intended guard use, and definedness. Applying it yields a `KindUseAdaptationJudgment` with value `true`, `false`, or `unknown`; it creates neither a new kind nor a membership relation. Cross-context use needs an obtaining `KindBridge`, a target declaration, and a separate `KindUseAdaptationCorrespondenceDeclaration` when constraints or bindings differ.

**Status.** Normative in **Part C**. Identifier **C.3.4**.
**Audience.** Engineering managers, architects, reviewers, and editors.

