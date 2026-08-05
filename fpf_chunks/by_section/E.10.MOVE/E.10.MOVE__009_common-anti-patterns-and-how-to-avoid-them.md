---
chunk_kind: "child"
pattern_id: "E.10.MOVE"
pattern_title: "Move and Readiness Wording Precision Restoration"
section_id: "E.10.MOVE:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.MOVE/E.10.MOVE__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "E.10.MOVE — Move and Readiness Wording Precision Restoration"
  - "E.10.MOVE:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 75541
line_end: 75550
dependencies:
  - "A.1.STM"
  - "A.10"
  - "A.15"
  - "A.15.5"
  - "A.21"
  - "A.22.CGUS"
  - "A.3.4.P"
  - "C.24"
  - "C.30"
  - "E.10"
  - "E.10.ARCH"
  - "E.11.PUR"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.23"
  - "E.24"
  - "F.17"
  - "F.18"
  - "G.11"
keywords:
---

### E.10.MOVE:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Better use |
| --- | --- | --- |
| Synonym replacement | "Move" becomes "action" or "use" without recovered kind. | Recover governed text span, claim being made, object under wording repair, relation, and governing pattern first. |
| Imported MOVE kind | TameFlow source wording becomes FPF ontology. | Recover intended work, readiness, gate, preparation work, or performed work. |
| Readiness as gate passage | A ready label becomes `GateDecision=pass`. | Use A.21 only when gate fields are present. |
| Path as work-authorization route | Evidence path or source-reference path becomes a way to authorize work by resemblance. | Recover evidence relation, source relation, graph path, gate relation, work authorization, or deontic permission separately. |
| Local expression generalized | A bounded local phrase is generalized to unrelated project work. | Keep `mantra move` bound to one `DemonstratedPatternUseRow@Context`; restore every other phrase through its own governed value and direct pattern. |

