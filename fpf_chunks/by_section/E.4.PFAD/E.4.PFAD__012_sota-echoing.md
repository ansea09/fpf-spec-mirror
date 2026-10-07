---
chunk_kind: "child"
pattern_id: "E.4.PFAD"
pattern_title: "Principle-Framework Architecture Decision"
section_id: "E.4.PFAD:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFAD/E.4.PFAD__012_sota-echoing.md"
commit_sha: "0c6ade275e9360f0c5ab9715d8f05c0dbaa13cf8"
heading_path:
  - "E.4.PFAD — Principle-Framework Architecture Decision"
  - "E.4.PFAD:11 — SoTA-Echoing"
line_start: 82999
line_end: 83012
dependencies:
  - "A.15.1"
  - "A.22"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.1.5"
  - "C.11.CRC"
  - "C.11.DUA"
  - "C.19.2"
  - "C.2.8"
  - "C.30.AD"
  - "C.30.STRAT"
  - "C.31"
  - "C.32.ADR"
  - "C.32.MWA"
  - "C.32.PAD"
  - "C.36"
  - "E.11"
  - "E.11.DSG"
  - "E.11.PFP"
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
  - "E.8"
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
| How much explanation and teaching should different readers receive? | Preparation-sensitive support, with sufficient method content and optional fuller acquisition routes. | One fully expanded route for everyone, or one compressed instruction presumed sufficient for everyone. | **Adapt:** :4.1.1 compares task-specific preparation and the cost of acquisition and repeated use; E.8 assigns the method/companion boundary. | Tetzlaff et al., [expertise-reversal meta-analysis](https://doi.org/10.1016/j.learninstruc.2025.102142) (2025), supports different effects by prior knowledge across heterogeneous learning settings. It gives no universal text length or model ranking. | Reopen the selected support when actual users' recovery, learning or recurring burden contradicts its assumed benefit. |
| When does human–AI cooperation supply the intended gain? | Compare relevant solo and combined arrangements, and distinguish aided task performance from acquired human capability. | Assume that adding AI improves the best available performance, or count a correct AI answer as human learning. | **Adapt:** :4.1.1 exposes allocation, handover, checking and learning costs and preserves the intended result. | Vaccaro et al., [meta-analysis](https://www.nature.com/articles/s41562-024-02024-1) (2024), finds heterogeneous combination effects in experiments from 2020–2023, not a universal AI frontier. Bastani et al., [mathematics learning experiment](https://doi.org/10.1073/pnas.2422633122) (2025), distinguishes assisted work from subsequent independent performance in its studied teaching setting. Neither validates FPF teaching or current model capabilities. | Reopen when the task, participants, AI system or division of work materially changes. |
| What makes useful content attainable for a bounded reader? | Observer-relative recovery of structure under actual resources and access, followed by a separate relevance and use question. | Count available text, compression or model intelligence as delivered utility. | **Adapt:** :4.1.1 connects discovery and C.2.8 recovery to an attainable benefit; it does not equate epiplexity with economic value. | Finzi et al., [epiplexity](https://arxiv.org/html/2601.03220v2) (2026 preprint), supplies the bounded-observer structural-information line and explicitly distinguishes task relevance. Human readability and utility are not validated bit estimates. | Reopen if recovery under the selected budget fails or stronger measurement changes the inference. |
| When is shared content worth the dependency it creates? | Compare consumer and producer costs, compatibility and independent change alongside reuse. | Maximize reuse, or assume duplication always restores modularity. | **Adapt:** :4.1.1 varies one use's premise and compares a common supplier, bounded interface and independent variants. | Badampudi, Usman and Chen, [Ericsson industrial case](https://arxiv.org/html/2309.15175v1) (2023), reports benefits and costs including understanding, compatibility, coordination and upgrades. Transfer from software implementation reuse to framework content is a stated architectural analogy, not an established effect size. | Reopen if an actual change reaches unrelated uses or the cost of separate variants defeats the expected independence. |
| How much research or protection is justified before inclusion? | Treat prospective benefit as a testable hypothesis and spend decision effort where its result could change the choice. | Exhaustive prevention of conceivable mistakes or inclusion from novelty alone. | **Adapt:** :4.1.1 uses C.11.DUA/C.11.CRC and bounded inquiry rather than a universal admission survey. | Camuffo et al., [four entrepreneurial trials](https://doi.org/10.1002/smj.3580) (2024), supports disciplined hypothesis testing and termination with bounded transfer to framework investment. De Sabbata et al., [LLM metareasoning](https://arxiv.org/html/2410.05563v2) (2024), supplies a computation-allocation comparator, not evidence that shorter instructions always improve reasoning. | Reopen when a material cost, expected frequency or failure consequence changes the decision. |

The external comparisons above supply bounded grounds for the selected construction. The whole-cost method is their methodological synthesis with C.11.DUA/C.11.CRC, not a claim that any source established one optimal library size or audience-independent publication form.

