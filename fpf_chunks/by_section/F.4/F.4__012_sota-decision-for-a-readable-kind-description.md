---
chunk_kind: "child"
pattern_id: "F.4"
pattern_title: "SystemRoleKindDescription — Describing an Exact System-Role Kind"
section_id: "F.4:10"
section_title: "SoTA Decision for a Readable Kind Description"
source_path: "FPF-Spec.md"
output_path: "by_section/F.4/F.4__012_sota-decision-for-a-readable-kind-description.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "F.4 — SystemRoleKindDescription — Describing an Exact System-Role Kind"
  - "F.4:10 — SoTA Decision for a Readable Kind Description"
line_start: 94174
line_end: 94189
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.6.RSIR"
  - "A.7"
  - "C.2.1"
  - "C.3"
  - "C.3.2"
  - "E.10.D2"
  - "E.10.ROLE"
  - "E.24"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.18"
  - "F.5"
  - "F.9"
keywords:
  - "classification criterion"
  - "description episteme"
  - "effective scheme"
  - "local kind"
  - "non-inference boundary"
  - "system-role-kind description"
---

### F.4:10 - SoTA Decision for a Readable Kind Description

Source use was checked on 2026-08-20. The bounded question is: **how can one work-facing kind be described for recognition without confusing the kind with its bearer, a classification judgment, assignment, capability, Method, Work, designation, or publication?** The comparison assumes the effort of authoring one project pattern, not adopting a whole upper ontology.

| Current line | Strong contribution | Limit at comparable pattern-authoring effort | FPF decision and receiving locus |
| --- | --- | --- | --- |
| Almeida, Guizzardi, Sales, and Fonseca, [*gUFO: A Gentle Foundational Ontology for Semantic Web Knowledge Graphs*](https://arxiv.org/abs/2603.20948), 2026 preprint | It distinguishes kinds of types, things, qualities, relations, and situations; this helps expose confusion among classification, the thing classified, a dependent feature, and participation. | Importing the full typology first adds a foundational-ontology mapping and can choose a source category before the FPF receiving use, local kind, and direct relations are known. | **Adapt** the warning against collapsing classification, bearer, function-like aspects, and participation in sections 4.2, 5, and 8. **Reject** automatic import of gUFO categories or labels as the F.4 kind or description. |
| Current [BFO 2020 artifacts](https://github.com/BFO-ontology/BFO-2020), maintained for the ISO/IEC 21838-2 line | Separates enduring things from processes and distinguishes dependence, roles, and dispositions. | A whole upper-ontology commitment is expensive for a short recognition description and still does not decide the identity of the local FPF kind, its assignment occurrence, Method, Work, or publication package. | **Adopt** the warnings that dependence is not parthood and that role/disposition/process readings must not be fused. **Reject** BFO classification or standard status as the local kind-identity or description gate. This constrains sections 4.2, 7, and 8. |
| [ISO 704:2022](https://www.iso.org/standard/79077.html) together with W3C OntoLex-Lemon's [lexical entry, sense, and reference model](https://www.w3.org/2016/04/ontolex/) | ISO separates object, concept, definition, and designation; OntoLex separates lexical form and sense from the ontology referent. | Neither line establishes an FPF system-role kind, classifies a candidate, makes an assignment obtain, proves capability or Work, or makes a description edition available. | **Adopt** description/designation/referent separation in sections 4.1 and 4.2. **Reject** a definition, label, lexical sense, or row as a fact about the described work. F.4 adds the direct neighboring exits and publication boundary in sections 4, 7, and checklist 12. |

**Selected non-dominated contribution.** gUFO and BFO offer richer foundational categorization, but at higher mapping effort and without deciding the project-local recognition use. ISO 704 and OntoLex keep description and designation separate at lower effort, but leave assignment, capability, Method, Work, and publication outside their answer. F.4 takes the smallest useful middle path: one C.2.1 episteme about one already recovered C.3 kind, a short ordinary-language recognition distinction, and explicit exits for stronger neighboring claims. At the effort of one pattern description, it preserves the needed ontology while remaining usable by a cold project reader.

SysML is intentionally not a SoTA comparator, lineage source, or ontology authority for this question. Its modeling notation does not supply the kind-identity, classification, assignment, description, or Work rules being compared; search visibility or standard status does not make it a content rival.

Currentness and reopen condition: reopen F.4 when A.2, C.3, A.2.1, A.2.5, A.2.7, A.15, A.6.5, A.6.RSIR, C.2.1, F.9, F.10, F.18, or the accepted episteme-use discipline changes enough that the described-kind or non-inference boundary would be stated differently.

