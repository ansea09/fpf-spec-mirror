---
chunk_kind: "child"
pattern_id: "E.24.UK"
pattern_title: "U-kind Admission and Ontic Settlement"
section_id: "E.24.UK:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.UK/E.24.UK__009_conformance-checklist.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "E.24.UK — U-kind Admission and Ontic Settlement"
  - "E.24.UK:7 — Conformance Checklist"
line_start: 83382
line_end: 83403
dependencies:
  - "A.11"
  - "A.3.2"
  - "A.6.0"
  - "A.6.3"
  - "A.6.5"
  - "A.6.REL"
  - "A.8"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "E.10"
  - "E.17.0"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "F.18"
  - "U.MethodDescription"
  - "U.View"
  - "U.Viewpoint"
keywords:
---

### E.24.UK:7 - Conformance Checklist

| Check | Closure condition |
| --- | --- |
| `CC-E24UK-1` | The candidate's governed object is recovered before the `U.*` spelling is judged. |
| `CC-E24UK-2` | C.3 `U.Kind` and `U.SubkindOf` are not used as synonyms for all U-kind governance. |
| `CC-E24UK-3` | A root U-kind has a primary E.24-compatible settlement and an identity, grounding, recognition, or membership rule rather than a taxonomic label alone. |
| `CC-E24UK-3a` | Root `U.Relation` classifies only individuable obtaining relation occurrences; `A.6.REL` supplies the common discipline and each direct relation pattern supplies its participant meanings, obtaining condition, and occurrence-identity rule. |
| `CC-E24UK-3b` | The claim-bearing decision episteme records exactly one typed `AdmissionDisposition` value — `root`, `same-individual-dependent`, `identity-dependent`, `reuse`, `local-kind`, or `reject` — and only the detail fields conditional on that value; it creates no project-side relation occurrence, and naming begins only after disposition. |
| `CC-E24UK-4` | A dependent durable U-kind states its root U-kind and either a same-individual membership rule that preserves root identity or an identity-dependence relation with every additional discriminator. |
| `CC-E24UK-4a` | `U.MethodDescription` preserves C.2.1 identity and uses the exact stable A.3.2 membership condition: one admitted `U.Method` is the exact EntityOfConcern and at least one substantive claim concerns that method as a way of doing; mention-only content, use adequacy, C.29 representation, publication occurrence, publication form, `U.PresentationCarrier`, approval, and work do not establish membership. `U.Viewpoint` and `U.View` likewise preserve C.2.1 identity and use the exact stable E.17.0 membership predicates; structure selection, bundle membership, DescriptionContext selection, direct authoring, A.6.3 construction, form, carrier, publication, query execution, evaluation, and work do not substitute for those predicates. |
| `CC-E24UK-4b` | `U.EpistemePublication` is rejected; Plain `published episteme` is relation-defined wording in a claim that states obtaining participation and identifies or permits recovery of the exact `EpistemePublicationRelation` occurrence. The Plain wording is neither a reference nor a designator and does not resolve. |
| `CC-E24UK-4c` | Every public example in section 4.2 records exactly one of the six dispositions. `reuse` points to an already admitted kind, `local-kind` points to one C.3.2 declaration, and neither is rewritten as a root or dependent admission. |
| `CC-E24UK-4d` | Under the effective reference scheme, `ViewpointId i` designates exact viewpoint episteme P and resolving `U.ViewpointRef r` that uses i yields P; i, r, and P remain distinct, neither designation nor resolution grants membership, E.17.0 owns membership, and `DescriptionContext` remains a separate one-viewpoint use qualification. |
| `CC-E24UK-5` | Structural locations retain `U.*` only with settlement evidence or direct reference to an already admitted U-kind. |
| `CC-E24UK-6` | A world-side relation participant retains its independently governed kind, while the direct relation pattern states its participant meaning. |
| `CC-E24UK-6a` | A reusable declaration component remains one A.6.5 SlotSpec; its SlotKind does not become a U-kind. |
| `CC-E24UK-6b` | A participant designation or other assertion or description field remains inside the receiving `U.Episteme`. |
| `CC-E24UK-6c` | A selected structure, reusable form, or representation element remains under `A.22`, `E.24.PUB`, or `C.29` respectively. |
| `CC-E24UK-7` | F.8, F.5, F.18, and F.17 are used only after the governed object and admission decision are stable. |
| `CC-E24UK-8` | E.24 remains the head ontic pattern; E.24.UK governs detailed U-kind admission without duplicating that procedure back into E.24. |

