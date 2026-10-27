---
chunk_kind: "child"
pattern_id: "C.32.P2S"
pattern_title: "Problem-to-Structure Architecturing Unfolding"
section_id: "C.32.P2S:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.P2S/C.32.P2S__012_sota-echoing.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "C.32.P2S — Problem-to-Structure Architecturing Unfolding"
  - "C.32.P2S:11 — SoTA-Echoing"
line_start: 76486
line_end: 76502
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

| SoTA source to inspect | Why this source is load-bearing here | Adopt, adapt, or reject disposition | Blocked overread |
|---|---|---|---|
| ISO/IEC/IEEE 42010:2022 architecture-description standard (`https://www.iso.org/standard/74393.html`) | Architecture-description practice separates architecture, description, concern, viewpoint, view, model kind, and correspondence. | Adopt the separation of architecture and description; adapt it through the exact description, view, ADR, and publication predicates located in `C.30.AD`, `C.30.ASV`, `C.32.ADR`, `E.17`, and `E.24.PUB`; reject any takeover of FPF holon and selected-structure ontology. | A description, view, diagram, or publication carrier is not the architecture, the project architecture decision, or performed work. |
| Ford, Parsons, Kua, and Sadalage, `Building Evolutionary Architectures`, 2nd ed. (`https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/`) | Practitioner treatment of guided incremental change over declared architecture characteristics with feedback from eval practice. | Adopt guided evolutionary change and feedback; adapt source-practice fitness-function practice into `C.32.ACE` eval programs and `C.16` measurement over `C.32.ACS` rows; reject treating eval success as a decision. | A source-practice fitness-function name, metric, or passing eval result is not the architecture characteristic, decision, or proof of realized structure. |
| Richards and Ford, `Fundamentals of Software Architecture`, 2nd ed. (`https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/`) and Ford et al., `Software Architecture: The Hard Parts` (`https://www.oreilly.com/library/view/software-architecture-the/9781492086888/`) | Practitioner sources for architecture characteristics, trade-offs, risk, coupling, cohesion, and difficult architecture decisions. | Adopt characteristic and trade-off discipline; adapt software-system examples to holons and selected structures; reject software-only module reduction. | A list of qualities, trade-off discussion, or rationale text is not candidate synthesis or decision adequacy by itself. |
| Architecture synthesis and multi-objective quality-attribute optimization, including Di Pompeo and Tucci 2023 (`https://arxiv.org/abs/2301.07516`) and ATRAF 2025 (`https://arxiv.org/abs/2505.00688`) | Research on competing quality attributes, multi-objective trade-offs, and architecture candidate evaluation. | Adopt candidate plurality and trade-off front inspection. Use the FPF patterns that define comparison, selected-set result declaration, local choice, and decision; reject a scalar score or generated winner as sufficient grounds for selection. | A Pareto front, scalar score, optimization run, or generated winner does not select the architecture. |
| DSM, multiple-domain matrix, modularization, and dependency-structure practice; Jiang and Luo 2026 (`https://arxiv.org/abs/2604.28018`), epiplexity structural-information line (`https://arxiv.org/abs/2601.03220`), and `C.31.RSA` structure-accounting rows | Strong engineering-design line for inspecting dependency, coupling, modularity, learnable structural content, and structural loss; the comparison also distinguishes cases in which functional priors and structural modularization objectives can diverge. | Adopt DSM, MDM, and epiplexity as structure-inspection lenses; adapt them through `C.29` lens refs and structural-information slots; reject matrix, cluster, compression, or epiplexity result as architecture adequacy. | A cluster, matrix, graph, compression, or epiplexity result is not architecture adequacy or a decision without recovered selected structures and a route to the next applicable pattern. |
| Conway correspondence, mirroring, DORA loosely coupled teams (`https://dora.dev/capabilities/loosely-coupled-teams/`), and Team Topologies (`https://teamtopologies.com/key-concepts`) | Socio-technical architecture practice examines how typed Work, communication, tool, method, deployment, evidence, selected-structure, or architecture-side sources can enable or block transformed-side architecture content and independent change. | Adopt co-synthesis of the influence-source and transformed sides; adapt through `C.32.CONWAY`; reject organization labels, communication diagrams, architecture relations, claims, or structures as acting Systems or direct transformation participants. | Organization labels, team diagrams, or communication patterns do not settle transformed-side architecture content, acting identity, Work attribution, or transformation participation; they enter only through their exact kinds and direct relations. |
| NASA Systems Engineering Handbook decision and trade-study practice (`https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf`), Michael Nygard's ADR practice (`https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions`), MADR 4.x (`https://adr.github.io/madr/`), and `C.32.ADR` source-anchor rows | Non-software domains often publish architecture choices as trade studies, engineering memos, review records, or certification rationale rather than Markdown ADR files; ADR practice supplies compact status, context, decision, options, consequences, links, and update conditions. | Adopt record-function discipline; adapt carrier form to project domain through the predicates and publication forms defined in `C.32.ADR`, `E.17`, and `E.24.PUB`; reject ADR file form as mandatory or authoritative by itself. | ADR file form is not mandatory and does not create a second decision authority. |
| FPF `C.18`, `C.19`, `E.23`, and `G.11` with NQD, OEE, improvement, telemetry, freshness, and decay practice | Architectures can change during use; retained alternatives, stepping stones, feedback, and decay affect the next synthesis question. | Adopt archive, front, pool, improvement, telemetry, freshness, and decay distinctions; adapt them as exits to the next applicable pattern; reject `G.11` refresh state or archive state as architecture choice. | Archive membership, improvement-loop status, telemetry, or freshness signal does not decide architecture by itself. |

**SoTA-anchor currentness boundary.** Use each source contribution within its stated domain and assumptions. When a source result, receiving use or relied-on condition changes, reconsider the affected construction or inference; retain unrelated results whose grounds still hold.

