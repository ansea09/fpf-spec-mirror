---
chunk_kind: "child"
pattern_id: "A.19.SUPPORT-VIEW"
pattern_title: "Cross-Surface Support View"
section_id: "A.19.SUPPORT-VIEW:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SUPPORT-VIEW/A.19.SUPPORT-VIEW__014_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.19.SUPPORT-VIEW — Cross-Surface Support View"
  - "A.19.SUPPORT-VIEW:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 23941
line_end: 23952
dependencies:
  - "A.0"
  - "A.19"
  - "A.19.SURF-SPACE"
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
  - "CrossSurfaceAtlasView"
  - "CrossSurfaceSupportView"
  - "TraditionAtlasView"
  - "TypedSetViews"
  - "atlas support"
  - "support qualifiers"
  - "support view"
  - "support-only reading"
  - "thin support"
---

### A.19.SUPPORT-VIEW:8 - Common Anti-Patterns and How to Avoid Them


| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| Writing as if `A.19.SUPPORT-VIEW` were a fresh autonomous theory of views | It duplicates existing `A.6.3` and `E.17.0` law and collapses `U.Viewpoint`, `U.View`, and publication-surface discipline. | State the docking to existing view law explicitly. |
| Letting atlas language become the default meaning of every support case | The fullest visible support form silently becomes the family head. | Keep ordinary thinner support views admissible and say when atlas form is actually needed. |
| Treating support pins as the view's semantic center | Metrics, transitions, or distortion notes then replace the base substrate. | Keep the base substrate and support question explicit, and keep support pins optional. |
| Letting a derived tradition view replace its base palette | The reader loses palette-first recoverability and mistakes one local interpretation for the default ontology. | Keep `DerivedViewKind` and `BasePaletteRef` visible together. |
| Turning the support view into publication or pool policy | The reader can no longer tell whether the text is helping interpret the line or deciding what survives and gets published. | Keep `G.5`, `G.10`, `C.19`, and `C.24` outside this pattern. |
| Forcing atlas form into every first reading | Simple cases become over-typed and harder to use. | Start with the thinner support-view form and widen only when the current need genuinely requires it. |

