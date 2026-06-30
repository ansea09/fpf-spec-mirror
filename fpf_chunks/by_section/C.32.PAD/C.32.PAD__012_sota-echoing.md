---
chunk_kind: "child"
pattern_id: "C.32.PAD"
pattern_title: "Project Architecture Decision After Candidate Synthesis"
section_id: "C.32.PAD:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.PAD/C.32.PAD__012_sota-echoing.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "C.32.PAD — Project Architecture Decision After Candidate Synthesis"
  - "C.32.PAD:11 — SoTA-Echoing"
line_start: 61257
line_end: 61273
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.21"
  - "B.2"
  - "B.2.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "E.11.PUR"
  - "E.17"
  - "E.24.PUB"
  - "E.8"
  - "G.5"
keywords:
  - "ArchitectureDecisionRelation@Project"
  - "accepted loss"
  - "affected selected structure"
  - "architect-developer split"
  - "architecture-characteristic trade-off"
  - "method-use instruction"
  - "project architecture decision"
  - "reopen condition"
  - "selected architecture option"
---

### C.32.PAD:11 - SoTA-Echoing

These rows document transfers from source practice into C.32.PAD. Keep a source citation only when it changes a decision-relation field, boundary, or reopen condition.

| Source to inspect | Why this source is load-bearing here | Transfer into PAD | Concrete PAD mutation | Blocked overread |
|---|---|---|---|---|
| ISO/IEC/IEEE 42010:2022 official standard (`https://www.iso.org/standard/74393.html`; IEEE page `https://standards.ieee.org/ieee/42010/6846/`) | Current official source for architecture-description requirements; it explicitly scopes itself to AD structure and expression, not architecting methods or the architecture itself. | Keep architecture descriptions as description objects and use PAD for the decision relation that may cite them. | PAD has `architectureDescriptionRefs`, selected-structure effects, and source-return conditions rather than treating a view, viewpoint, file, or model as the decision. | ISO 42010 architecture-description structure does not replace C.32 synthesis, A.15 method work, or PAD decision relation. |
| Michael Nygard, `Documenting Architecture Decisions` (`https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions`) | Practitioner source for small, statused records that preserve context, decision, and consequences across time. | Use context, decision, status, consequences, and supersession as publication-relevant decision-description fields. | PAD requires status, consequences, and supersession or reopen conditions before ADR projection. | ADR records are not the project decision relation and do not by themselves ground selected structures. |
| MADR 4.x (`https://adr.github.io/madr/`) | Current ADR practice with options, outcome, status, links, and confirmation pressure. | Require candidate basis, outcome, decision status, links to related decisions, and confirmation or eval exits. | PAD separates candidate basis, selected option, consequence rows, method-use instruction, and reopen conditions. | MADR's broad "any decision" use is not imported as FPF architecture-decision ontology. |
| Ford, Parsons, Kua, and Sadalage, `Building Evolutionary Architectures`, 2nd ed. (`https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/`) | Current practitioner source for guided incremental architecture change and source-side fitness-function wording. | Treat eval support as `C.32.ACE` inputs and reopen conditions, not as the decision itself. | PAD requires eval refs, guardrails, and reopen conditions when evolutionary feedback guides the decision. | Fitness-function terminology is not imported as an FPF object name. |
| Ford, Richards, Sadalage, and Dehghani, `Software Architecture: The Hard Parts` (`https://www.oreilly.com/library/view/software-architecture-the/9781492086888/`) | Current practitioner source for trade-offs, least-worst choices, and architecture characteristics under uncertainty. | Make accepted losses and protected counter-characteristics mandatory decision content. | PAD records architecture-characteristic trade-offs, rejected options, accepted losses, and consequences. | A trade-off discussion does not replace candidate synthesis, comparison, evidence, or governance. |
| NASA Systems Engineering Handbook, decision analysis and trade-study practice (`https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf`) | Non-software engineering source for alternatives, selection criteria, assumptions, limitations, recommendation, impacts, and final decision documentation. | Generalize PAD beyond software ADR practice by requiring candidate basis, selection criteria or comparison refs, assumptions or accepted losses, impacts, and decision-maker commitment. | PAD carries `candidateBasisRefs`, `comparisonOrSelectionRefs?`, trade-offs, consequence rows, status, and reopen conditions for engineering decisions such as fixtures, vehicles, built assets, or methods. | NASA trade-study process is not imported as FPF architecture ontology and does not by itself decide the architecture. |
| Conway and Team Topologies source line, mediated through `C.32.CONWAY` | Architecture of the transformer holon and transformed holon can constrain each other. | Use correspondence as decision content when work organization, method, toolchain, or team structure must fit target architecture. | PAD may cite `transformerTransformedCorrespondenceRef` and reopen on mismatch. | Team structure is not automatically the target holon's architecture; correspondence must be recovered through C.32.CONWAY. |
| Current FPF `A.15`, `E.8`, `E.11.PUR`, `C.30.AD`, `C.32`, `C.32.ACS`, `C.32.ACE`, `C.32.ADR`, and `C.32.ADA` | Existing FPF ontology for method descriptions, pattern use, architecture descriptions, candidate synthesis, evals, publication projection, and adequacy evaluation. | Keep PAD narrow: decision relation after candidate synthesis. | Relation and conformance rows send neighboring claims to their governing patterns. | PAD does not duplicate FPF method, publication, evidence, assurance, or pattern-form doctrine. |

**Source-currentness boundary.** Recheck a source row when an ADR template, architecture-description standard, evolutionary-architecture practice, FPF pattern, or project governance practice changes the decision field, method-work boundary, or reopen condition that PAD uses.

