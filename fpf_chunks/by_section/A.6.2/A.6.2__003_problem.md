---
chunk_kind: "child"
pattern_id: "A.6.2"
pattern_title: "Effect-Free Episteme Morphing: Laws for Mathematical Relations Between Epistemes"
section_id: "A.6.2:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.2/A.6.2__003_problem.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "A.6.2 — Effect-Free Episteme Morphing: Laws for Mathematical Relations Between Epistemes"
  - "A.6.2:2 — Problem"
line_start: 18011
line_end: 18028
dependencies:
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "F.9"
  - "U.Mechanism"
  - "U.Signature"
keywords:
---

### A.6.2:2 - Problem

Without EFEM:

1. **No single place for “effect‑free” discipline.**
   The laws for mathematical relations between epistemes are otherwise scattered or implicit; any operation application remains separate.

2. **Endpoint EntityOfConcern identity or difference is unclear.**
   Some arrow families have endpoint epistemes about the same EntityOfConcern; others have endpoints about independently different entities. Without a common `EntityOfConcernChangeMode` classification, a relation that looks like a representation change can hide a different receiving EntityOfConcern.

3. **No functorial backbone.**
   To compose arrows from MVPK, KD-CAL or E.18, the receiving use needs compatible identity, composition, purity, conservativity and formal-domain conditions. Any repeat law must also be stated for the arrow family.

4. **Slot/Ref confusion.**
   C.2.1 identifies an episteme through claim content, one EntityOfConcern, and one effective ReferenceScheme. A.6.5 SlotSpecs apply only inside a reusable relation declaration. Laws for projection or retargeting that rely on unnamed fields or tuple positions therefore hide which parts of the source and receiving epistemes are being compared and which separately obtaining facts the rule reads.

The result: engineers and tool builders can no longer tell whether a mathematical relation keeps the same EntityOfConcern, identifies a different receiving one, or merely accompanies an operation. For a receiving-use claim about an arrow whose endpoints concern different entities, state the separate A.6.4 bounded-use assertion. When judging a current case, compare its facts with that assertion.

