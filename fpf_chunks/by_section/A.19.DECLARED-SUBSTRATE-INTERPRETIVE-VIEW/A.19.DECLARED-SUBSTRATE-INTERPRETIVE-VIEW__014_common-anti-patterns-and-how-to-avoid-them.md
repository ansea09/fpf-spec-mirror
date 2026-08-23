---
chunk_kind: "child"
pattern_id: "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
pattern_title: "Declared-Substrate Interpretive View"
section_id: "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW/A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW__014_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW — Declared-Substrate Interpretive View"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 29810
line_end: 29820
dependencies:
  - "A.0"
  - "A.19"
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE"
  - "A.6.3"
  - "A.6.P"
  - "C.19"
  - "C.24"
  - "E.17"
  - "E.17.0"
  - "G.10"
  - "G.2"
  - "G.5"
keywords:
  - "DeclaredSubstrateAtlasView"
  - "DeclaredSubstrateInterpretiveView"
  - "TraditionAtlasView"
  - "TypedSetViews"
  - "atlas-form interpretation"
  - "declared-substrate interpretive view"
  - "interpretive qualifiers"
  - "interpretive-only reading"
  - "thin interpretation"
---

### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| Writing as if `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW` were a fresh autonomous theory of views | It duplicates existing `A.6.3` and `E.17.0` law and collapses `U.Viewpoint`, `U.View`, and publication-face discipline. | State the docking to existing view law explicitly. |
| Letting atlas language become the default meaning of every interpretive case | The fullest visible interpretive form silently becomes the family head. | Keep ordinary thinner interpretive views admissible and say when atlas form is actually needed. |
| Treating qualifier refs as the view's semantic center | Metrics, transitions, or distortion notes then replace the base substrate. | Keep the base substrate and inspection question explicit, and keep qualifier refs optional. |
| Letting a derived tradition view replace its base palette | The reader loses palette-first recoverability and mistakes one local interpretation for the default ontology. | Keep `DerivedViewKind` and `BasePaletteRef` visible together. |
| Turning the interpretive view into publication or pool policy | The reader can no longer tell whether the text is helping interpret the line or deciding what survives and gets published. | Keep `G.5`, `G.10`, `C.19`, and `C.24` outside this pattern. |
| Forcing atlas form into every first reading | Simple cases become over-typed and harder to use. | Start with the thinner interpretive-view form and widen only when the current need genuinely requires it. |

