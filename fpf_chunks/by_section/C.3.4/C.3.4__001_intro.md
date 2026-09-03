---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__001_intro.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:intro — Intro"
line_start: 46057
line_end: 46063
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

> **One-line summary.** Use a `KindUseAdaptationDeclaration` when a procedure needs a narrower or differently named use of an existing kind without defining another kind. The declaration pins the base `KindSignature` edition, local candidate constraints or vocabulary bindings, intended guard use, and applicability. Check admissibility before returning `true`, `false`, or `unknown`. A locality change first triggers kind-identity comparison: the same kind needs no `KindBridge`; distinct kinds need one only when its exact correspondence predicate obtains.

**Status.** Normative in **Part C**. Identifier **C.3.4**.
**Audience.** Engineering managers, architects, reviewers, and editors.

