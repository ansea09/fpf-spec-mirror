---
chunk_kind: "child"
pattern_id: "E.4"
pattern_title: "FPF Ecosystem Family Architecture"
section_id: "E.4:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4/E.4__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "1f413fcd23f4ea26956a45d67dde57bb233f6ad9"
heading_path:
  - "E.4 — FPF Ecosystem Family Architecture"
  - "E.4:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 68587
line_end: 68597
dependencies:
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.1"
  - "E.11"
  - "E.11.PUR"
  - "E.17"
  - "E.19"
  - "E.2"
  - "E.2.DA"
  - "E.21"
  - "E.23"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.4.FPF"
  - "E.4.PFAD"
  - "E.4.PFR"
  - "E.5.3"
  - "F.18"
  - "G.11"
  - "G.2"
  - "G.5"
keywords:
---

### E.4:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Core absorption | A domain or local framework is placed into the FPF Core because it is useful. | Create a separate framework edition with dependency records under `E.4.PFR`. |
| File tree or package map as architecture | A folder layout, package descriptor, or manifest is read as the ecosystem architecture. | Use the file or manifest only as a carrier; recover the family-and-structure map, relation records, dependency records, source packs, quality records, publication/access carriers, and refresh routes. |
| Publication-only architecture | A table of contents or all-in-one carrier is used as the architecture description. | Add a family-and-structure map and source-return note, then publish through `E.11` or `E.17`. |
| Ontology or talk guide as framework | A framework names domain entities, terms, or conversation moves but does not identify recurring domain problems, known failure modes, SoTA solution moves, and worked repairs. | Keep the ontology, glossary, or communication guide as support material; create or repair the framework around problem situations, solution moves, cases, and quality routes. |
| Relation flattening | Every cross-reference is treated as the same relation. | Use `E.4.PFR` to state relation function and direct owner. |
| Source-carrier authority | A summary, graph, or generated candidate set is treated as authoritative. | Admit the carrier through `C.35` or record preservation through `C.33` and `C.34` before use. |

