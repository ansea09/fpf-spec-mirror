---
chunk_kind: "child"
pattern_id: "A.6.P.WMR"
pattern_title: "Exact Relation Recovery for Method and Work Claims"
section_id: "A.6.P.WMR:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.P.WMR/A.6.P.WMR__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "A.6.P.WMR — Exact Relation Recovery for Method and Work Claims"
  - "A.6.P.WMR:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 15897
line_end: 15909
dependencies:
  - "A.15.1"
  - "A.15.1-A.15.3"
  - "A.15.2"
  - "A.15.3"
  - "A.15.PROD"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "A.6.P"
  - "A.6.RCD"
  - "C.2.P"
  - "E.10"
  - "E.10.ARCH"
  - "E.18.1"
  - "F.18"
keywords:
---

### A.6.P.WMR:8 - Common Anti-Patterns and How to Avoid Them

**Informative misuse examples.** The Repair column describes the outcome of applying the checklist; it creates no additional imperative or world-side fact.
| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Boundary word as kind | `Input`, `Output`, `Result`, or `Handoff` is used as the entity kind. | The repaired claim restores the entity's admitted kind, related object, direct relation, orthogonal claim dimensions, and governor. |
| Plan as actuality | A planned filling, work-package row, or intended deliverable is treated as an actual participant or result. | Intended relation content stays under the plan; actuality opens only from direct obtaining facts. |
| Binding as production | An operation result binding is treated as proof that work produced or constituted the bound entity. | The repaired claim states only the binding; `A.15.PROD` opens separately when exact production facts make that question current. |
| Result record as result relation | A report, log, or evaluation-result episteme is treated as the changed entity, work, or direct subject relation. | The repaired claim identifies the episteme and its claim content, then keeps any work, change, measurement, or evaluation relation separate. |
| Local id used as ontology | A project id or assertion id is cited where the `RelationKind`, obtaining predicate, relation-specification edition, or direct owner is needed. | The repaired claim names the token and resolving owner and separates any obtaining occurrence, assertion episteme, and local id; without a settlement it returns the exact missing-governor result. |
| Missing governor hidden by hypernym | A broad word makes an unresolved relation look complete. | The repaired result records exact participants, obtaining question, missing governor, affected use, and future owner. |
| Composition by proximity | Shared work, time, flow, or referent is treated as transformation composition. | The repaired result keeps independently identified transformations and returns the exact composition blocker. |

