---
chunk_kind: "child"
pattern_id: "E.10.D1"
pattern_title: "Recovering What “Context” Means in Use"
section_id: "E.10.D1:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D1/E.10.D1__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "E.10.D1 — Recovering What “Context” Means in Use"
  - "E.10.D1:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 74998
line_end: 75008
dependencies:
  - "A.1.1"
  - "A.2.6"
  - "C.30"
  - "E.10"
  - "E.10.ARCH"
  - "E.17.0"
  - "F.0.1"
  - "F.17"
  - "F.19"
  - "F.9"
keywords:
  - "architecture"
  - "claim scope"
  - "context wording"
  - "environment"
  - "model use"
  - "positive wording repair"
  - "source-local meaning"
  - "viewpoint"
  - "working situation"
---

### E.10.D1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Universal Context proxy | One entity stands for source scheme, scope, situation, architecture, and model-use boundary. | Select the branch and name the direct value or relation. |
| Context field as participant | A `ContextId` or `...ContextRef` field silently becomes a relation participant or identity discriminator. | Resolve the field to the subject-pattern value; otherwise keep it as a designator and state the blocker. |
| Automatic bounded-context structure | The phrase *bounded context* selects A.1.1 even when one direct relation answers the decision. | Begin with applicability, actual use, or coherence and stop at the first sufficient result. |
| Context map as relation truth | A diagram or table is treated as an obtaining Bridge, `ArchitectureRelation`, or model-use crossing. | Recover the represented objects, correspondence, and direct relation under their subject patterns. Use an `ArchitectureClaim` when architecture remains negative, unresolved, candidate, or expected. |
| Blanket word ban | Every occurrence of *context* or *anchor* is deleted, including precise source terms and established designations. | Preserve the defined source or subject-pattern use; rewrite only wording that hides content needed by the FPF claim. |
| Bare pattern citation | The sentence cites a PatternID but still leaves the boundary unexplained. | State whether the cited pattern defines, constrains, tests, or supplies a method for the recovered content. |

