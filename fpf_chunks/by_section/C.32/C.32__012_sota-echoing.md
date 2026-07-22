---
chunk_kind: "child"
pattern_id: "C.32"
pattern_title: "Architecture Candidate Synthesis"
section_id: "C.32:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32/C.32__012_sota-echoing.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "C.32 — Architecture Candidate Synthesis"
  - "C.32:11 — SoTA-Echoing"
line_start: 62932
line_end: 62951
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
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.18"
  - "E.22"
  - "E.23"
  - "G.5"
keywords:
  - "CandidateArchitecturePalette@Project"
  - "architecture candidate synthesis"
  - "architecture characteristics"
  - "candidate configurations"
  - "retained alternatives"
  - "selected structures"
  - "synthesis structure map"
  - "trade-off front"
---

### C.32:11 - SoTA-Echoing

These rows document transfers from source practice into C.32. Each row states which C.32 field, repair row, boundary, or worked case the draft sets or revises from the source, and where a reader can inspect that source line. Software-system sources are used as lineage and domain examples only; they do not narrow C.32 to IT architecture.

| Source to inspect | Why this source is load-bearing here | Transfer into C.32 | Concrete C.32 mutation | Blocked overread |
|---|---|---|---|---|
| Architecture synthesis and quality-attribute optimization: Di Pompeo and Tucci 2023 (`https://arxiv.org/abs/2301.07516`), ATRAF 2025 (`https://arxiv.org/abs/2505.00688`), and current FPF `C.32.HCS`, `C.32.ACS`, `C.32.ACE`, `C.25`, `C.31`, `C.16` | Current architecture optimization line: quality attributes and architecture characteristics compete, and multi-objective treatment gives the architect a trade-off view instead of one scalar winner. | Make candidate configurations name ACS criteria rows and Q-Bundle slots before comparison, and use ACE eval results as feedback for the next synthesis question only through the receiving pattern. | `CandidateArchitecturePalette@Project` now includes `architectureCharacteristicCriteriaSetRef?`, `architectureCharacteristicCriteriaRowRefs`, `qBundleRefs?`, `affectedCriteriaRowRefs?`, `architectureCharacteristicEvalResultRefs?`, `constraintFit`, and `tradeoffFrontOrArchiveRef?`; Problem separates functional demand from architecture characteristics. | A user function, metric, benchmark, scalarized score, eval result, or apparent improvement is not architecture synthesis, comparison, project architecture decision, or improvement-cycle closure. |
| DSM, multiple-domain matrix, and current DSM modularization research, including Jiang and Luo 2026 (`https://arxiv.org/abs/2604.28018`) | DSM modularization remains a strong engineering-design line. Current LLM-based DSM work also shows a concrete semantic-alignment risk: functional priors and structural modularization objectives can diverge. | Use DSM or clustering as one candidate-generation and inspection source; recover selected structures, structural objective, and engineering semantics before treating the result as architecture-synthesis material. | Solution adds `synthesisStructureMap`; candidate work coordinates functional, constructive, placement, control, work, information, and evidence structures rather than accepting a cluster as architecture. | A cohesive cluster, graph partition, or generated modularization is not architecture adequacy by itself. |
| Current FPF architecture kernel: `A.22`, `C.30`, `C.30.ASV`, `C.30.ILC`, `C.31`, `C.31.ASAP`; architecture source section 15.3 | This is the current local architecture law for holonic architecture: selected structures of a described holon in a bounded context remain primary. | Use SoTA and domain sources only after recovering described holon, synthesis structure map, architecture criteria rows, selected structure changes, gain, loss, and receiving pattern. | `CandidateArchitecturePalette@Project` now requires `synthesisStructureMap`, architecture-characteristic criteria rows, selected structure changes, `constraintFit`, preserved and lost structure, source-return condition, and `nextUse`; worked cases cover heterogeneous holon kinds. | Diagrams, source expressions, software-system templates, and platform proposals remain source cues until the described holon, selected structures, architecture criteria, gain, loss, and receiving pattern are recovered. |
| ISO 42010:2022 architecture-description standard (`https://www.iso.org/standard/74393.html`) | Current architecture-description standard. It is load-bearing because C.32 must not confuse architecture, description, view, viewpoint, concern, correspondence, or model kind. ISO also states that architecture itself is outside the AD standard's subject. | Treat architecture-description artifacts as source cues or architecture-description material until a candidate selected-structure change is recovered. | C.32 fields distinguish source cues, source-side referents, selected structures, and architecture characteristics; the Relations section names `C.30.AD` or `C.30.ASV` for description or view repair, and `E.17` or `E.24.PUB` for publication-face use, when current. | An architecture-description artifact or publication face is not a candidate architecture by itself. |
| Ford, Parsons, Kua, and Sadalage, `Building Evolutionary Architectures`, 2nd ed.; overview at `https://evolutionaryarchitecture.com/` and O'Reilly page `https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/` | Best current practitioner line for architecture as guided incremental change over declared architecture characteristics, affected selected structures, and feedback from source-side fitness functions. | Add evolutionary candidate discipline: reversible first step where useful, affected criteria row, ACE eval result, source-return trigger, next synthesis question, and no source-term takeover. | Solution and SoTA rows now say source-side fitness-function practice is restored through `C.32.ACE` as eval programs over ACS rows; candidate rows can name `affectedCriteriaRowRefs?`, `architectureCharacteristicEvalResultRefs?`, next synthesis question, and source-return condition; measurement claims belong to C.16. | Eval results need a receiving comparison, local choice, or governance pattern before they affect preference or start the next synthesis iteration. |
| Shaw and Petre, `Design Spaces and How Software Designers Use Them` (`https://arxiv.org/abs/2407.18502`); Cortellessa, Diaz-Pace, Di Pompeo, Tucci, `Towards Assessing Spread in Sets of Software Architecture Designs` (`https://arxiv.org/abs/2402.19171`) | Current research line for design alternatives and architecture-space diversity. It repairs the common error of judging only objective-space scores while losing architectural differences. | Preserve a candidate palette when one scalar winner would hide structurally different alternatives; distinguish objective-space signals from selected-structure differences. | C.32 keeps candidate plurality until `G.5`, `C.11`, or a `C.32.PAD` project architecture decision relation is current; each candidate must name selected structure, architecture-change kind, gain, loss, and hidden or preserved structure. | A Pareto front, score, spread indicator, or generated set does not select the architecture and does not replace architecture-space inspection. |
| MOSA and open-system engineering from `C.31.RSA` (`https://www.cto.mil/sea/mosa/`; `https://www.cto.mil/wp-content/uploads/2025/03/MOSA-Implementation-Guidebook-27Feb2025-Cleared.pdf`); product-line variability and product-platform practice from `C.31.RSA` and `C.31.ASAP` (`https://www.sei.cmu.edu/library/variability-in-software-product-lines/`; `https://arxiv.org/abs/2605.21353`; `https://link.springer.com/article/10.1007/s00163-023-00427-1`; `https://arxiv.org/abs/2510.11089`); information-hiding lineage carried by `C.31.RSA` | Current source families for modular interface conformance, substitution policy, variability slots, extension rules, exception curves, and assembly or realization constraints. Information hiding is lineage for hidden-change and implicit-dependency repair. | Use them as candidate-generation prompts: change the interface grammar, change substitution policy, move a variation slot, split evidence scope, admit a bounded exception, or consolidate a bearer. | C.32 adds `interfaceGrammarChange`, `declaredScopeOrHolonLevelChange`, and `boundedException` as architecture-change kinds; the product-family worked case prepares interface-grammar change, evidence-scope split, and bounded exception as candidate alternatives. | Before a candidate is preferred, send reusable-structure accounting to `C.31.RSA`, scale preference to `C.31.ASAP`, interface grammar to `A.6.M`, comparison to `C.16` or `A.19`, and selected-set or local-decision use to `G.5` or `C.11`. |
| TRIZ ideality, Ideal Final Result, technical-system evolution regularities, and current FPF `C.19.1` BLP | Older heuristic lineage for increasing useful function while reducing cost, harm, and unnecessary parts; BLP supplies current FPF discipline for preferring more general scale-amenable bearers when safety and admissibility are comparable. | Use idealization only to generate candidates: transfer function to an existing bearer, remove support bearers, use available resources, or try a more general bearer as a candidate. | C.32 adds `architectureIdealityPressureRef?`, `scaleAmenabilityPolicyRef?`, and `functionBearerConsolidation`; repair cues require function-bearing, affected architecture characteristics, losses, scale window, and BLP scale window or waiver when scale advantage is claimed. | An ideal-final-result slogan, fewer modules, or one universal module is not architecture adequacy, scale adequacy, or project architecture decision. |
| NAS survey line: Elsken, Metzen, and Hutter 2019 (`https://www.jmlr.org/papers/v20/18-598.html`); multi-objective differentiable NAS 2025 (`https://arxiv.org/abs/2402.18213`); hardware-aware NAS 2024 (`https://arxiv.org/abs/2404.12403`); Sutton's Bitter Lesson (`https://www.incompleteideas.net/IncIdeas/BitterLesson.html`) and scaling-law practice | Current ML architecture line for functional graph search under multi-objective performance, resource, hardware, and transfer constraints. It is load-bearing as a transferable synthesis technique, not as an IT ontology. | Treat functional architecture as one selected structure and require bearer feasibility across module, deployment, resource, control, information, and evidence structures before comparison. | C.32 adds `functionBearerFeasibilityRef?`, `functionBearerFeasibilityRepair`, and didactic slices where a functional graph or method step fails because no bearer can carry it under current constraints. | A neural cell graph, function graph, benchmark winner, or scale curve is not holonic architecture adequacy unless selected structures and bearers are recovered. |
| Conway's law, mirroring, DORA loosely coupled teams (`https://dora.dev/capabilities/loosely-coupled-teams/`), and Team Topologies key concepts (`https://teamtopologies.com/key-concepts`) | Current socio-technical architecture practice for co-synthesizing the changing holon and the changed holon under independent change, test, deployment, evidence, and coordination constraints. | Treat team, work, responsibility, method, toolchain, deployment, and communication structures as transformer-side selected structures when they constrain transformed-holon architecture. Use inverse Conway only as a candidate architecture change that changes selected transformer structures. | C.32 adds `transformerTransformedCorrespondenceSynthesis`, names `C.32.CONWAY` as the correspondence-frame governing pattern, and keeps role, work, module-interface, evidence, and mathematical-lens claims with their governing patterns. | Keep transformer-side change, transformed-side change, joint change, and bounded mismatch as candidate alternatives or comparison inputs; explicit comparison, module-interface, evidence, decision, and G.5 publication claims exit to their own patterns. |
| MAAD 2025 (`https://arxiv.org/abs/2507.21382`) and LLM-assisted ADD 2025 (`https://arxiv.org/abs/2506.22688`) | Current AI-assisted architecture design research. It is load-bearing because generated alternatives are now practical, but the research itself stresses knowledge intensity, trade-offs, evaluation, and human oversight. | Use AI outputs to widen candidate space, then recover source-side referent, selected structure, architecture-change kind, gain, loss, source-return condition, and receiving pattern before palette admission. | C.32 problem and Solution now treat generated outputs as source cues; `sourceCueRefs?` and `sourceSideReferent?` prevent generated text from carrying an architecture-adequacy authority relation. | A generated blueprint, evaluation report, benchmark, or agent consensus is not an authority relation for architecture adequacy, evidence sufficiency, assurance, gate passage, or decision. |

**Source-currentness boundary.** Use each source row only for the C.32 candidate-generation move that the row transfers. If a named standard, guide, book edition, survey, or research line changes that move, recheck the row before using it again. If a receiving FPF pattern named in the row changes how it handles the source family, recheck the row before using it again. If the project needs comparison, selection, publication of a selected set, local choice, decision, evidence, or assurance, leave C.32 and open the receiving pattern. Rows named as lineage, such as TRIZ ideality, information hiding, or mature DSM lineage, stay lineage until a current source relation is recovered.

