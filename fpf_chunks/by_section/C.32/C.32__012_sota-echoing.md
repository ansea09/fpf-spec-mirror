---
chunk_kind: "child"
pattern_id: "C.32"
pattern_title: "Architecture Candidate Synthesis"
section_id: "C.32:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32/C.32__012_sota-echoing.md"
commit_sha: "5801dc610c657ac7b1efee349b18e80ce6d7df6f"
heading_path:
  - "C.32 — Architecture Candidate Synthesis"
  - "C.32:11 — SoTA-Echoing"
line_start: 61602
line_end: 61621
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.HCS"
  - "C.32.MLAO"
  - "C.32.MWA"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.18"
  - "E.22"
  - "E.23"
  - "G.5"
  - "U.Structure"
keywords:
  - "CandidateArchitecturePalette@Project"
  - "architecture candidate synthesis"
  - "architecture characteristics"
  - "candidate configurations"
  - "retained alternatives"
  - "selected structures"
  - "selected-structure contribution rows"
  - "trade-off front"
---

### C.32:11 - SoTA-Echoing

These rows show how source practice contributes to C.32. The opening of each second-column entry classifies the source use; the opening of each transfer states its disposition. The blocked-overread column gives the use limit, and the source-currentness boundary below gives the reopen rule. Software-system sources are comparison inputs, examples, or lineage only; they do not narrow C.32 to IT architecture.

| Source to inspect | Source-use class and why it matters here | Transfer into C.32 | Where this contribution appears in C.32 | Blocked overread |
|---|---|---|---|---|
| Architecture synthesis and quality-attribute optimization: Di Pompeo and Tucci 2023 (`https://arxiv.org/abs/2301.07516`), ATRAF 2025 (`https://arxiv.org/abs/2505.00688`), and current FPF `C.32.HCS`, `C.32.ACS`, `C.32.ACE`, `C.25`, `C.31`, `C.16` | **Current comparison input plus current FPF authority:** quality attributes and architecture characteristics compete, and multi-objective treatment gives the architect a trade-off view instead of one scalar winner. | **Adapt:** make candidate configurations name ACS criteria rows and Q-Bundle slots before comparison, and use ACE evaluation results as feedback for the next synthesis question only through the pattern for that question. | `CandidateArchitecturePalette@Project` includes `architectureCharacteristicCriteriaSetRef?`, `architectureCharacteristicCriteriaRowRefs`, `qBundleRefs?`, `affectedCriteriaRowRefs?`, `architectureCharacteristicEvalResultRefs?`, `constraintFit`, and `tradeoffFrontOrArchiveRef?`; Problem separates functional demand from architecture characteristics. | A user function, metric, benchmark, scalarized score, evaluation result, or apparent improvement is not architecture synthesis, comparison, project architecture decision, or improvement-cycle closure. |
| DSM, multiple-domain matrix, and current DSM modularization research, including Jiang and Luo 2026 (`https://arxiv.org/abs/2604.28018`) | **Current research comparison with established DSM lineage:** modularization is useful, while LLM-based DSM work also exposes divergence between functional priors and structural objectives. | **Adapt:** use DSM or clustering as one candidate-generation and inspection source; recover selected structures, structural objective, and engineering semantics before treating the result as architecture-synthesis material. | Solution adds `selectedStructureContributionRows`; candidate work coordinates functional, constructive, placement, control, work, information, and evidence structures rather than accepting a cluster as architecture. | A cohesive cluster, graph partition, or generated modularization is not architecture adequacy by itself. |
| Current FPF architecture kernel: `A.22`, `C.30`, `C.30.ASV`, `C.30.ILC`, `C.31`, `C.31.ASAP`; architecture source section 15.3 | **Current internal authority:** obtaining architecture relations connect an exact described holon to selected structures for a named architecture question and use. | **Adopt:** use SoTA and domain sources only after recovering described holon, synthesis question and use, current architecture relations, selected-structure contribution rows, architecture criteria rows, selected structure changes, gain, loss, and pattern for the next question. | `CandidateArchitecturePalette@Project` requires `selectedStructureContributionRows`, architecture-characteristic criteria rows, selected structure changes, `constraintFit`, preserved and lost structure, source-return condition, and `nextUse`; worked cases cover heterogeneous holon kinds. | Diagrams, source expressions, software-system templates, and platform proposals remain source cues until the described holon, selected structures, architecture criteria, gain, loss, and pattern for the next question are recovered. |
| ISO 42010:2022 architecture-description standard (`https://www.iso.org/standard/74393.html`) | **Current normative comparison:** it distinguishes architecture, description, view, viewpoint, concern, correspondence, and model kind, while leaving architecture itself outside the standard's subject. | **Adopt narrowly:** treat architecture-description artifacts as source cues or description material until a candidate selected-structure change is recovered. | C.32 fields distinguish source cues, source-side referents, selected structures, and architecture characteristics. For description or view repair, use `C.30.AD` or `C.30.ASV`; for publication, use `E.17` for a source-backed face and source return and `E.24.PUB` for the publication occurrence and audience availability. | An architecture-description artifact or publication face is not a candidate architecture by itself. |
| Ford, Parsons, Kua, and Sadalage, `Building Evolutionary Architectures`, 2nd ed.; overview at `https://evolutionaryarchitecture.com/` and O'Reilly page `https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/` | **Current practitioner comparison:** guided incremental change makes affected architecture characteristics and feedback visible. | **Adapt:** add reversible first steps where useful, affected criteria rows, ACE evaluation results, source-return triggers, a next synthesis question, and no source-term takeover. | Solution and SoTA rows state that source-side fitness-function practice is represented through exact `C.32.ACE` evaluation-program assertions over ACS rows; candidate rows can name `affectedCriteriaRowRefs?`, `architectureCharacteristicEvalResultRefs?`, next synthesis question, and source-return condition; measurement claims use the exact C.16 predicate. | Evaluation results need an exact comparison, local-choice, or other preference-use assertion before they affect preference or start the next synthesis iteration. |
| Shaw and Petre, `Design Spaces and How Software Designers Use Them` (`https://arxiv.org/abs/2407.18502`); Cortellessa, Diaz-Pace, Di Pompeo, Tucci, `Towards Assessing Spread in Sets of Software Architecture Designs` (`https://arxiv.org/abs/2402.19171`) | **Current research comparison:** design-space work distinguishes structural alternatives from objective-space scores. | **Adapt:** preserve a candidate palette when one scalar winner would hide structurally different alternatives; distinguish objective-space signals from selected-structure differences. | Retain candidate plurality until `G.5`, `C.11`, or a `C.32.PAD` project architecture decision relation is current; each candidate must name selected structure, architecture-change kind, gain, loss, and hidden or preserved structure. | A Pareto front, score, spread indicator, or generated set does not select the architecture and does not replace architecture-space inspection. |
| MOSA and open-system engineering from `C.31.RSA` (`https://www.cto.mil/sea/mosa/`; `https://www.cto.mil/wp-content/uploads/2025/03/MOSA-Implementation-Guidebook-27Feb2025-Cleared.pdf`); product-line variability and product-platform practice from `C.31.RSA` and `C.31.ASAP` (`https://www.sei.cmu.edu/library/variability-in-software-product-lines/`; `https://arxiv.org/abs/2605.21353`; `https://link.springer.com/article/10.1007/s00163-023-00427-1`; `https://arxiv.org/abs/2510.11089`); information-hiding lineage carried by `C.31.RSA` | **Current standards and practice comparison plus information-hiding lineage:** the sources expose interface conformance, substitution, variability, extension, exception, assembly, and hidden-change pressures. | **Adapt as candidate prompts:** change the interface grammar, substitution policy, variation slot, evidence scope, exception boundary, or bearer only when the current architecture question needs it. | C.32 adds `interfaceGrammarChange`, `declaredScopeOrHolonLevelChange`, and `boundedException` as architecture-change kinds; the product-family worked case prepares interface-grammar change, evidence-scope split, and bounded exception as candidate alternatives. | Before a candidate is preferred, use `C.31.RSA` for reusable-structure accounting, scale preference to `C.31.ASAP`, interface grammar to `A.6.M`, comparison to `C.16` or `A.19`, and selected-set or local-decision use to `G.5` or `C.11`. |
| TRIZ ideality, Ideal Final Result, technical-system evolution regularities, and current FPF `C.19.1` BLP | **Historical heuristic lineage plus current FPF discipline:** older ideality language suggests useful candidate moves; BLP supplies the current scale-amenability rule. | **Use as lineage and adapt only as a candidate prompt:** transfer a function to an existing bearer, remove support bearers, use available resources, or try a more general bearer; judge the resulting candidate under current FPF rules. | C.32 adds `architectureIdealityPressureRef?`, `scaleAmenabilityPolicyRef?`, and `functionBearerConsolidation`; repair cues require function-bearing, affected architecture characteristics, losses, scale window, and BLP scale window or waiver when scale advantage is claimed. | An ideal-final-result slogan, fewer modules, or one universal module is not architecture adequacy, scale adequacy, or project architecture decision. |
| NAS survey line: Elsken, Metzen, and Hutter 2019 (`https://www.jmlr.org/papers/v20/18-598.html`); multi-objective differentiable NAS 2025 (`https://arxiv.org/abs/2402.18213`); hardware-aware NAS 2024 (`https://arxiv.org/abs/2404.12403`); Sutton's Bitter Lesson (`https://www.incompleteideas.net/IncIdeas/BitterLesson.html`) and scaling-law practice | **Current ML research and practice comparison:** functional graph search works under performance, resource, hardware, and transfer constraints. | **Adapt:** treat functional architecture as one selected structure and require bearer feasibility across module, deployment, resource, control, information, and evidence structures before comparison. | C.32 adds `functionBearerFeasibilityRef?`, `functionBearerFeasibilityRepair`, and didactic slices where a functional graph or method step fails because no bearer can carry it under current constraints. | A neural cell graph, function graph, benchmark winner, or scale curve is not holonic architecture adequacy unless selected structures and bearers are recovered. |
| Conway's law, mirroring, DORA loosely coupled teams (`https://dora.dev/capabilities/loosely-coupled-teams/`), and Team Topologies key concepts (`https://teamtopologies.com/key-concepts`) | **Current practitioner comparison with historical lineage:** these sources expose co-evolution and coordination pressure between organizational and technical structures without supplying a universal causal law. | **Adapt:** treat team, Work, responsibility, Method, toolchain, deployment, communication, evidence, and selected structures through their exact kinds; assert a direct influence relation only when its predicate is satisfied. Use inverse Conway only to generate a candidate change to selected influence-source structures. | C.32 adds `architectureInfluenceCorrespondenceRef?` and `architectureInfluenceCorrespondenceSynthesis`; use `C.32.CONWAY` for the synthesis-local frame or an exact pair row. Keep both architecture sides or modal claims, changed referent, any local system-role kind, classification or assignment, Work, module-interface, evidence, and mathematical-lens claims distinct. | Influence-source change, transformed-side change, joint change, and bounded mismatch remain candidate alternatives or comparison inputs. Architecture influence alone establishes no acting System, Work, or actual transformation. |
| MAAD 2025 (`https://arxiv.org/abs/2507.21382`) and LLM-assisted ADD 2025 (`https://arxiv.org/abs/2506.22688`) | **Current research comparison:** generated alternatives are practical, while the studies retain knowledge, trade-off, evaluation, and human-oversight limits. | **Adapt:** use AI outputs to widen candidate space, then recover source-side referent, selected structure, architecture-change kind, gain, loss, source-return condition, and pattern for the next question before palette admission. | C.32 Problem and Solution treat generated outputs as source cues; `sourceCueRefs?` and `sourceSideReferent?` prevent generated text from carrying an architecture-adequacy authority relation. | A generated blueprint, evaluation report, benchmark, or agent consensus is not an authority relation for architecture adequacy, evidence sufficiency, assurance, gate passage, or decision. |

**Source-currentness boundary.** Use each source row only for the C.32 candidate-generation move that the row transfers. If a named standard, guide, book edition, survey, or research line changes that move, recheck the row before using it again. If a receiving FPF pattern named in the row changes how it handles the source family, recheck the row before using it again. If the project needs comparison, selection, selected-set result declaration, actual publication, local choice, decision, evidence, or assurance, leave C.32 and open the pattern for the next question. Rows named as lineage, such as TRIZ ideality, information hiding, or mature DSM lineage, stay lineage until a current source relation is recovered.

