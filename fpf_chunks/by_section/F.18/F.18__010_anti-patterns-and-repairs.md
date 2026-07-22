---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local-First Unification Naming Protocol"
section_id: "F.18:8"
section_title: "Anti-Patterns And Repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__010_anti-patterns-and-repairs.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "F.18 — Local-First Unification Naming Protocol"
  - "F.18:8 — Anti-Patterns And Repairs"
line_start: 92953
line_end: 92966
dependencies:
  - "A.15.1"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.6.RSIR"
  - "C.2.1"
  - "E.10"
  - "E.10.ARCH"
  - "F.0.1"
  - "F.1"
  - "F.1-F.17"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.8"
  - "F.9"
  - "G.10"
  - "G.2"
  - "G.6"
keywords:
---

### F.18:8 - Anti-Patterns And Repairs

| Anti-pattern | Ontological failure | Repair |
| --- | --- | --- |
| "Same spelling means same value." | Treats string identity or a sense bridge as governed-value identity. | Use `F.9` only to state exact cross-context sense correspondence and admitted use; apply the direct object owner for any identity claim, or keep the values separate. |
| "Evidence role" for a report, source, or standard. | Turns an episteme or source-use relation into a work-facing role. | Recover evidence-use, source-use, status-use, publication-use, or assurance-use relation. |
| "Night operator role" when only schedule differs. | Bakes temporal admission into role identity. | Keep role value; put time window in assignment, status, or work plan. |
| "Certified engineer role" when certification is evidence or admission. | Bakes capability evidence or admission into role name. | Keep `EngineerRole`; record capability evidence, admission, or status relation separately. |
| "Role-derived method" treated as a role-relation result. | Confuses role expression with method identity. | Name method or method family under `A.3.1` and `A.3.2`; cite role requirement separately. |
| "Method algebra" treated as the method or plan. | Confuses mathematical or representation lens with method relation structure, method description, work plan, or performed work. | Recover `MethodRelationStructure@BoundedContext`, method description, `C.29` lens use, work plan, or work occurrence by direct governing pattern before naming. |
| Action nominal, WBS element, or Work Package treated as performed work. | Function/method morphology or intended-work content is mistaken for one dated occurrence; a nearby result is folded into the work name. | Recover the exact `A.15.1` occurrence basis, apply `A.6.P.WMR` if the relation is still hidden, and name neighboring production claims, measurement results, evaluation results, delivery occurrences, and acceptance verdicts separately. |
| Role-looking interface wording for API, port, or boundary. | Uses role morphology to avoid recovering port, signature, boundary, or interface-specific relation. | Use `A.6.RSIR` and the direct governing pattern; name the recovered relation, signature, port, or bounded interface value only when that pattern admits it. |
| "Unscoped glossary." | Publishes words without governed value, by-value reference scheme, local sense, and bridge. | Use `NameCard`; use `F.17` term row when publication is current. |

