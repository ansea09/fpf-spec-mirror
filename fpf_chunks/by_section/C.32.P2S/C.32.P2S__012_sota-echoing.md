---
chunk_kind: "child"
pattern_id: "C.32.P2S"
pattern_title: "Problem-to-Structure Architecturing Unfolding"
section_id: "C.32.P2S:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.P2S/C.32.P2S__012_sota-echoing.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "C.32.P2S — Problem-to-Structure Architecturing Unfolding"
  - "C.32.P2S:11 — SoTA-Echoing"
line_start: 61961
line_end: 61977
dependencies:
  - "A.1"
  - "A.1.SCR"
  - "A.1.STM"
  - "A.15.6"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.4"
  - "B.2"
  - "C.22.2"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.HCS"
  - "C.32.MLAO"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.17"
  - "E.18"
  - "E.18.3"
  - "E.24.PUB"
keywords:
---

### C.32.P2S:11 - SoTA-Echoing

These rows document transfers from source practice into C.32.P2S. Software-system sources are used as source families and examples only; they do not narrow P2S to IT architecture.

| SoTA source to inspect | Why this source is load-bearing here | Adopt, adapt, or reject disposition | Transfer into C.32.P2S | Blocked overread |
|---|---|---|---|---|
| ISO/IEC/IEEE 42010:2022 architecture-description standard (`https://www.iso.org/standard/74393.html`) | Current architecture-description practice separates architecture, description, concern, viewpoint, view, model kind, and correspondence. | Adopt the separation of architecture and description; adapt it through the exact description, view, ADR, and publication predicates located in `C.30.AD`, `C.30.ASV`, `C.32.ADR`, `E.17`, and `E.24.PUB`; reject any takeover of FPF holon and selected-structure ontology. | P2S step 8 and `CC-C32P2S-2` keep descriptions, views, and ADR-like records as captured structural content or publication forms with exact neighboring subject assertions. | A description, view, diagram, or publication carrier is not the architecture, the project architecture decision, or performed work. |
| Ford, Parsons, Kua, and Sadalage, `Building Evolutionary Architectures`, 2nd ed. (`https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/`) | Best current practitioner line for guided incremental change over declared architecture characteristics with feedback from eval practice. | Adopt guided evolutionary change and feedback; adapt source-practice fitness-function practice into `C.32.ACE` eval programs and `C.16` measurement over `C.32.ACS` rows; reject treating eval success as a decision. | P2S step 11, the eval-shaped practice row, and `CC-C32P2S-8` require architecture characteristics, eval exits, feedback, stronger-structure inspection return, and next-action triggers selected for the current question rather than one-time design settlement. | A source-practice fitness-function name, metric, or passing eval result is not the architecture characteristic, decision, or proof of realized structure. |
| Richards and Ford, `Fundamentals of Software Architecture`, 2nd ed. (`https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/`) and Ford et al., `Software Architecture: The Hard Parts` (`https://www.oreilly.com/library/view/software-architecture-the/9781492086888/`) | Current practitioner sources for architecture characteristics, trade-offs, risk, coupling, cohesion, and difficult architecture decisions. | Adopt characteristic and trade-off discipline; adapt software-system examples to holons and selected structures; reject software-only module reduction. | P2S steps 2, 7, and 11 plus `CC-C32P2S-3` separate functional demand from architecture characteristics, require accepted-loss visibility, and feed realized functional implications back without confusing kinds. | A list of qualities, trade-off discussion, or rationale text is not candidate synthesis or decision adequacy by itself. |
| Architecture synthesis and multi-objective quality-attribute optimization, including Di Pompeo and Tucci 2023 (`https://arxiv.org/abs/2301.07516`) and ATRAF 2025 (`https://arxiv.org/abs/2505.00688`) | Current research line for competing quality attributes, multi-objective trade-offs, and architecture candidate evaluation. | Adopt candidate plurality and trade-off front inspection. Use the FPF patterns that define comparison, selected-set result declaration, local choice, and decision; reject a scalar score or generated winner as sufficient grounds for selection. | P2S steps 5 and 6, the single-winner pressure-cue row, and `CC-C32P2S-5` keep candidate plurality and require explicit comparison, selection, selected-set result declaration, local choice, and decision predicates after C.32 candidate synthesis; publication remains a separate sequence. | A Pareto front, scalar score, optimization run, or generated winner does not select the architecture. |
| DSM, multiple-domain matrix, modularization, and dependency-structure practice; inherited C.32 source-anchor row for Jiang and Luo 2026 (`https://arxiv.org/abs/2604.28018`), epiplexity structural-information line (`https://arxiv.org/abs/2601.03220`), and `C.31.RSA` structure-accounting rows | Strong engineering-design line for inspecting dependency, coupling, modularity, learnable structural content, and structural loss; the inherited C.32 row also warns that functional priors and structural modularization objectives can diverge. | Adopt DSM, MDM, and epiplexity as structure-inspection lenses; adapt them through `C.29` lens refs and structural-information slots; reject matrix, cluster, compression, or epiplexity result as architecture adequacy. | P2S steps 3 and 5 and `CC-C32P2S-4` let the card cite DSM, MDM, graph, epiplexity, coarse-graining, equivalence, or morphism claims while recording preserved and lost structure. | A cluster, matrix, graph, compression, or epiplexity result is not architecture adequacy or a decision without recovered selected structures and a route to the next applicable pattern. |
| Conway correspondence, mirroring, DORA loosely coupled teams (`https://dora.dev/capabilities/loosely-coupled-teams/`), and Team Topologies (`https://teamtopologies.com/key-concepts`) | Current socio-technical architecture practice shows that typed Work, communication, tool, method, deployment, evidence, selected-structure, or architecture-side sources can enable or block transformed-side architecture content and independent change. | Adopt co-synthesis of the influence-source and transformed sides; adapt through `C.32.CONWAY`; reject organization labels, communication diagrams, architecture relations, claims, or structures as acting Systems or direct transformation participants. | The P2S architecture-influence branch, Show C, and `CC-C32P2S-9` require exact C.30 architecture sides or modal claims, an independently typed influence source and direct relation, the changed referent, and any actual A.3.4 transformation as separate objects. | Organization labels, team diagrams, or communication patterns do not settle transformed-side architecture content, acting identity, Work attribution, or transformation participation; they enter only through their exact kinds and direct relations. |
| NASA Systems Engineering Handbook decision and trade-study practice (`https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf`), Michael Nygard's ADR practice (`https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions`), MADR 4.x (`https://adr.github.io/madr/`), and `C.32.ADR` source-anchor rows | Non-software domains often publish architecture choices as trade studies, engineering memos, review records, or certification rationale rather than Markdown ADR files; ADR practice supplies compact status, context, decision, options, consequences, links, and update conditions. | Adopt record-function discipline; adapt carrier form to project domain through the predicates and publication forms defined in `C.32.ADR`, `E.17`, and `E.24.PUB`; reject ADR file form as mandatory or authoritative by itself. | P2S step 8 and the Relations boundary treat decision records by section function and reader use: project architecture decisions require an exact `C.32.PAD` assertion, while record projection uses the `C.32.ADR` description. | ADR file form is not mandatory and does not create a second decision authority. |
| FPF `C.18`, `C.19`, `E.23`, and `G.11` with NQD, OEE, improvement, telemetry, freshness, and decay practice | Modern architecturing happens under evolution; retained alternatives, stepping stones, feedback, and decay affect the next synthesis question. | Adopt archive, front, pool, improvement, telemetry, freshness, and decay distinctions; adapt them as exits to the next applicable pattern; reject `G.11` refresh state or archive state as architecture choice. | P2S steps 6 and 11 record archive, front, and pool refs, improvement-loop refs, telemetry, actual-structure observations, decay, stronger-structure inspection return, and return or repair refs selected for the next question without merging the meanings defined by their patterns. | Archive membership, improvement-loop status, telemetry, or freshness signal does not decide architecture by itself. |

**SoTA-anchor currentness boundary.** Use each SoTA source-anchor row only for the P2S card field, P2S method or architecturing-transformation-flow step, boundary, or repair named in the row. Recheck the row when the source-practice anchor, applicable FPF pattern, described holon, structure kinds, architecture characteristics, architecture-influence relation, eval mode, or project use changes.

