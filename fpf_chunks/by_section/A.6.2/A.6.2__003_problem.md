---
chunk_kind: "child"
pattern_id: "A.6.2"
pattern_title: "U.EffectFreeEpistemicMorphing — Effect‑free morphisms of epistemes"
section_id: "A.6.2:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.2/A.6.2__003_problem.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "A.6.2 — U.EffectFreeEpistemicMorphing — Effect‑free morphisms of epistemes"
  - "A.6.2:2 — Problem"
line_start: 12956
line_end: 12973
dependencies:
  - "A.1"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "C.2.1"
  - "C.3"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "U.EpistemicRetargeting"
  - "U.EpistemicViewing"
  - "U.Mechanism"
  - "U.Signature"
keywords:
---

### A.6.2:2 - Problem

Concretely, without EFEM:

1. **No single place for “effect‑free” discipline.**
   The distinction between episteme-only change and Work in the world is already important: C.2.1 separates the three episteme identity values and neighboring direct relations from Work, publication forms, renderings, and carriers. The laws for episteme-only operations are otherwise scattered or implicit.

2. **EntityOfConcern behaviour is unclear.**
   Many transforms **intend** to keep “what this episteme is about” fixed (viewing), others **intend** to change it under an invariant (retargeting). Without a common *EntityOfConcernChangeMode* discipline we get silent breaks in “entityOfConcern”: an operation that looks like a harmless format change may in fact surreptitiously change the entity of concern.

3. **No functorial backbone.**
   MVPK, KD‑CAL, and E.18 all implicitly assume that episteme transforms **compose** and respect identities, but the conditions for this (purity, conservativity, idempotence, scope) are not formulated once and reused. Different parts of the spec repeat subtly different sets of laws.

4. **Slot/Ref confusion.**
   C.2.1 identifies an episteme through exact claim content, one exact EntityOfConcern, and one effective ReferenceScheme. A.6.5 SlotSpecs apply only inside an exact reusable relation declaration. Laws for “projection” or “retargeting” that instead rely on unnamed fields or tuple positions therefore hide what the morphism actually reads or changes.

The result: engineers and tool builders can no longer tell **when they are allowed to transform epistemes without changing what is being claimed about the world**, nor what needs to be witnessed by Bridges and CL‑penalties when entityOfConcern does change.

