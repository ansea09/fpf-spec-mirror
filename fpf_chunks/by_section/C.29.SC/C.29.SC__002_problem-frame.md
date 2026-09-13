---
chunk_kind: "child"
pattern_id: "C.29.SC"
pattern_title: "Derive a Consequence from a Symmetry"
section_id: "C.29.SC:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.SC/C.29.SC__002_problem-frame.md"
commit_sha: "bbfb5347013400e9a895fa4b0f66992e931c0ece"
heading_path:
  - "C.29.SC — Derive a Consequence from a Symmetry"
  - "C.29.SC:1 — Problem frame"
line_start: 64837
line_end: 64850
dependencies:
  - "A.3.3.TR"
  - "C.29.1"
  - "C.29.2"
  - "C.29.AV"
keywords:
---

### C.29.SC:1 - Problem frame

Use this pattern when a transformation appears to preserve the structure relevant to a problem, and you need to turn that observation into a useful restriction, a transferred solution or a reason that a requested answer cannot be selected from the available information.

A symmetric allocation problem can constrain its unique optimum before a full calculation. An anonymous arrangement can make a unique choice impossible under a stated selection rule. A rotationally symmetric physical law can relate motions with different initial states. The useful consequence depends on what the transformation actually preserves and how the required answer transforms.

A *symmetry* here is an invertible transformation preserving the stated structure. The object of the Method is that transformation together with the problem and answer it acts on. State the structure: preserving a shape, an equation, a criterion or a fully specified problem gives different premises.

The first result is a consequence with its reason: another valid solution, a restriction on possible answers, or a conflict between the input symmetry and the required output. This can reduce a search or identify the additional distinction a computation needs.

The reader needs the problem's conditions and enough subject mathematics to apply the transformation and test its effect. The allocation and selection examples need algebra and permutations. The dynamics example additionally needs differentiation and elementary state updates.

If no symmetry-related conclusion is needed, use the direct calculation. If the live problem is a general change of mathematical representation, C.29.1 supplies result transfer without requiring a symmetry.

