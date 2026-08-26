---
chunk_kind: "child"
pattern_id: "A.6.2"
pattern_title: "Effect-free episteme morphing"
section_id: "A.6.2:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.2/A.6.2__003_problem.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "A.6.2 — Effect-free episteme morphing"
  - "A.6.2:2 — Problem"
line_start: 12918
line_end: 12935
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

Concretely, without EFEM:

1. **No single place for “effect‑free” discipline.**
   The laws for mathematical relations between exact epistemes are otherwise scattered or implicit; any operation application remains separate.

2. **EntityOfConcern behaviour is unclear.**
   Some arrow families have endpoint epistemes about the same EntityOfConcern; others have endpoints about independently different entities. Without a common *EntityOfConcernChangeMode* discipline, a relation that looks like a harmless representation change can hide a different receiving EntityOfConcern.

3. **No functorial backbone.**
   MVPK, KD‑CAL, and E.18 all rely on episteme arrows that compose and respect identities, but the conditions for identity, composition, purity, conservativity, formal domain, and any arrow-family repeat law are not formulated once and reused. Different parts of the spec repeat subtly different sets of laws.

4. **Slot/Ref confusion.**
   C.2.1 identifies an episteme through exact claim content, one exact EntityOfConcern, and one effective ReferenceScheme. A.6.5 SlotSpecs apply only inside an exact reusable relation declaration. Laws for projection or retargeting that rely on unnamed fields or tuple positions therefore hide which parts of the source and receiving epistemes are being compared and which separately obtaining facts the rule reads.

The result: engineers and tool builders can no longer tell whether a mathematical relation keeps the same EntityOfConcern, identifies a different receiving one, or merely accompanies an operation. When the endpoints concern different entities, they also need a separate claim saying whether the arrow supports one receiving use, with its invariant, visible loss, conditions, support, and polarity.

