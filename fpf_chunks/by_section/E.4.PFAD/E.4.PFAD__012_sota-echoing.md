---
chunk_kind: "child"
pattern_id: "E.4.PFAD"
pattern_title: "Principle-Framework Architecture Decision"
section_id: "E.4.PFAD:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFAD/E.4.PFAD__012_sota-echoing.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "E.4.PFAD — Principle-Framework Architecture Decision"
  - "E.4.PFAD:11 — SoTA-Echoing"
line_start: 70925
line_end: 70933
dependencies:
  - "A.15.1"
  - "A.22"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.1.5"
  - "C.30.AD"
  - "C.30.STRAT"
  - "C.32.ADR"
  - "C.32.MWA"
  - "C.32.PAD"
  - "C.36"
  - "E.11.DSG"
  - "E.17"
  - "E.19"
  - "E.21"
  - "E.23"
  - "E.23.CDI"
  - "E.24.PUB"
  - "E.4"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.4.PFR"
  - "E.9"
  - "F.18"
  - "F.19"
  - "G.11"
  - "G.2"
keywords:
---

### E.4.PFAD:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and E.4.PFAD mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should an author decide whether a reusable framework family boundary is worth settling rather than recording one current slice or applying a full software product-line method? | Marchezan de Paula et al.'s 2022 systematic review is the best-known-line candidate for this bounded scoping question because it compares product, domain, asset, technical, organizational, and evaluation concerns across 41 approaches. | One-slice authoring, label or pattern-count specificity, and a complete software product-line process are the serious alternatives. | The first defaults hide promised-family coverage and its edition, change, and refresh boundary, plus any maintenance relation actually claimed; the full process adds software assets, features, roles, and mechanisms before the practical boundary is known. **Adapt:** `E.4.PFAD:4.1–4.2` uses a cheap exit, same-grain alternatives, practitioner problems, receiving use, evidence limits, direct subjects, edition/change/refresh boundaries, any obtaining maintenance relation, consequences, and reopen; a material family change routes to `E.4.DPF.DA`. **Reject:** software feature ontology and a mandatory generic scoping process. | Marchezan de Paula et al., [*Software product line scoping: A systematic literature review*](https://doi.org/10.1016/j.jss.2021.111189) (2022), is a systematic synthesis with context and evaluation limits; it does not decide an FPF or DPF boundary, prove reuse value, or supply the E.9 decision. Current `E.4`, `E.9`, and `E.4.DPF.DA` retain those responsibilities. | Reopen if stronger current scoping evidence changes the decision variables or a repeated case shows that the cheap-exit/full-decision split loses a necessary boundary. |
| What evidence prevents a broad framework name or coherent pattern slice from masquerading as a validated domain contribution? | Riehle, Harutyunyan, and Barcomb's 2025 validation line, bounded by Chuprina et al.'s 2024 domain-specific proof of concept, is the best-known current comparison for explicit cases, evidence limits, and actual-use pressure without claiming one universal field grammar. | Pattern count, broad domain labels, and source-layout coherence are the serious defaults. | These defaults make visible specificity substitute for action-changing contribution and warranted retention. **Adapt:** E.4.PFAD compares the same situation at comparable effort, names representative cases and limits, keeps external-result use honest, and separates distinct contribution from package coverage; **reject** a universal grammar and a research programme at the cheap exit. | Riehle, Harutyunyan, and Barcomb, [*Pattern Discovery and Validation Using Scientific Research Methods*](https://doi.org/10.1007/978-3-662-70810-1_6) (2025), supplies the validation branch. Chuprina et al., [*Towards an Approach to Pattern-based Domain-Specific Requirements Engineering*](https://arxiv.org/abs/2404.17338) (2024), supplies bounded proof-of-concept evidence; transfer beyond its evaluated setting remains untested. | Reopen if stronger current pattern-validation or domain-pattern evidence changes the same-situation action test, the evidence limit, or the family-coverage trigger. |

The two comparison rows above are the selected external sources. The `E.9` DRR shape and neighboring FPF boundaries remain direct internal rules.

