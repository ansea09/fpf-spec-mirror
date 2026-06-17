---
chunk_kind: "child"
pattern_id: "C.2.3"
pattern_title: "Unified Formality Characteristic F"
section_id: "C.2.3:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.3/C.2.3__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "C.2.3 — Unified Formality Characteristic F"
  - "C.2.3:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 36854
line_end: 36863
dependencies:
  - "A.16"
  - "A.18"
  - "A.19"
  - "B.3"
  - "C.2"
  - "C.2.2"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "F.9"
keywords:
  - "F-scale"
  - "F0-F9"
  - "Formality"
  - "language-state separation"
  - "proof"
  - "rigor"
  - "specification"
---

### C.2.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What it looks like | How FPF prevents it |
|---|---|---|
| **Status leakage** | An episteme is called highly formal because it is approved or published. | `CC-F-13` keeps status and formality separate. |
| **Tool-worship** | A notation, prover, or execution harness is named, so the episteme is rated high-F without checking the content. | `CC-F-11` and `CC-F-12` require observable semantic grounds. |
| **Appendix inflation** | A small high-formality appendix is used to advertise the whole episteme as high-F. | `CC-F-6` keeps the whole episteme capped by the least-formal essential support. |
| **Proxy ladder** | A local context invents "bronze / silver / gold" or "ready / mature / final" and uses it instead of `F`. | `CC-F-4` rejects rival ladders. |
| **Characteristic capture** | Articulation, closure, scope, or evidence is spoken of as if it were part of `F`. | `CC-F-8`, `CC-F-10`, and `CC-F-15` keep the characteristics orthogonal. |

