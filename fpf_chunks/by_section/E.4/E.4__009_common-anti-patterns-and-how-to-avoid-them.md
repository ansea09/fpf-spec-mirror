---
chunk_kind: "child"
pattern_id: "E.4"
pattern_title: "FPF Ecosystem Family Architecture"
section_id: "E.4:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4/E.4__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "E.4 — FPF Ecosystem Family Architecture"
  - "E.4:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 67636
line_end: 67652
dependencies:
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.1"
  - "E.11"
  - "E.11.DSG"
  - "E.11.PFP"
  - "E.11.PUR"
  - "E.17"
  - "E.19"
  - "E.2"
  - "E.2.DA"
  - "E.21"
  - "E.23"
  - "E.24.PUB"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.4.FPF"
  - "E.4.PFAD"
  - "E.4.PFR"
  - "E.5.3"
  - "E.9"
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
| File tree or package manifest as architecture | A folder layout, package descriptor, or manifest is read as the ecosystem architecture. | Use the file or manifest only as a carrier; recover the ecosystem-architecture record, relation records, dependency records, source packs, quality records, exact presentation carriers, access routes, and refresh routes. |
| Publication-only architecture | A table of contents or all-in-one carrier is used as the architecture description. | Add an ecosystem-architecture record and source-return note, then constitute the exact practical-entry and publication assertions under the predicates defined in `E.11` and `E.17`. |
| Ontology or talk guide as framework | A framework names domain entities, terms, or conversation moves but does not identify recurring domain problems, known failure modes, SoTA solution moves, and worked repairs. | Keep the ontology, glossary, or communication guide as support material; create or repair the framework around problem situations, solution moves, cases, and quality routes. |
| Relation flattening | Every cross-reference is treated as the same relation. | Use `E.4.PFR` to state relation function and subject pattern. |
| Outside the pattern set means another product | A Preface, coverage account, or refresh note is given a separate product identity although it shares the framework edition's users, access, maintainer, and cadence. | Keep it as a named support publication unit unless an independent use and maintenance boundary is useful. |
| Product label used as an object kind | A guide, service, programme, registry, System, or episteme is asserted to be the same kind because each is managed as a product. | Keep *product* as Plain management wording. Name each direct subject and the relation used for identity, current state, provision, or maintenance; return an unresolved-kind question when needed. |
| Shared carrier or shared use means one product | A cross-framework registry or service is absorbed into one DPF, or a combined carrier merges a framework and catalogue. | Decide each managed boundary from direct subjects, use, and maintenance; keep exact constituent pointers and let the outer carrier remain neutral. |
| Service or publication scheme used as universal architecture | A full service-management system, bibliographic entity model, or content-management process is imposed on every framework unit, programme, guide, or tool. | Reuse only the distinction that answers the current boundary question; keep service, publication, content, and programme claims under their own subject patterns. |
| DPF list presented as a Suite | A title or co-list replaces product-series constitution, the Suite-constitution decision, the direct belongs-to occurrences, identity rules, and maintenance conditions. | Keep a proposal until `E.4:4.2` passes; then identify the Suite collection and the product series that belong to it. |
| Suite belonging inflated | Two product series belong to the same Suite, so the text infers order, dependency, compatibility, maintenance, publication, or co-use. | Keep the Suite claim at product-series grain and apply the direct predicate for every stronger claim. |
| Source-carrier authority | A summary, graph, or generated candidate set is treated as authoritative. | Admit the carrier through `C.35` or record preservation through `C.33` and `C.34` before use. |

