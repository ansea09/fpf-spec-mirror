---
chunk_kind: "child"
pattern_id: "A.22"
pattern_title: "Structure and Structural Views (STRUCT-CAL)"
section_id: "A.22:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22/A.22__012_sota-echoing.md"
commit_sha: "646b0b9b164f7c13258633a33b92d2d0a569da28"
heading_path:
  - "A.22 — Structure and Structural Views (STRUCT-CAL)"
  - "A.22:11 — SoTA-Echoing"
line_start: 29527
line_end: 29537
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.6.2"
  - "A.6.3"
  - "A.6.F"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.2.1"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "E.24"
  - "E.24.PUB"
  - "F.18"
  - "G.5"
  - "G.6"
keywords:
  - "architecture-description boundary"
  - "preserved and lost structure"
  - "selected structure"
  - "source return"
  - "structural description"
  - "structural view"
  - "structure"
---

### A.22:11 - SoTA-Echoing

| Practice or source line | FPF adoption | Action consequence | Boundary |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010:2022 architecture-description practice | Adopt the separation of source-side entity-of-interest, concern, viewpoint, view, and correspondence as pressure for DescriptionContext separation, mapped here to `EntityOfConcern` and `DescriptionContext` terms. | A.22 structural descriptions and views reuse `DescriptionContext`, viewpoint, view, and correspondence machinery rather than inventing a local display ontology. | ISO 42010 does not make every structure an architecture and does not add evidence, assurance, gate, or decision authority. |
| OMG SysML v2 view practice | Adapt views-as-queries and model-view discipline as a source for treating views as selected renderings over model content. | A structural view states selected, hidden, or lost structure when the selection changes action. | A view is not the structure and not a proof of the described holon. |
| C.29 mathematical-lens discipline | Adopt preserved structure, lost structure, lens-use admissibility, and stop-condition discipline when a mathematical lens is used for a structure claim. | Cite C.29 output through C.29 lens-use result, preserved structure, lost structure, stop condition, and source-return discipline. | Lens output is not structure, evidence, assurance, causal-use relation, or decision. |
| arXiv:2603.00601 code-space architecture relation-graph work and related code-probing practice | Adapt partial-observability, typed-relation, uncertainty, and source-return pressure for extracted structural views. | Use extracted structural-view records with validation boundaries and an observation value selected from `observed`, `inferred`, or `unknown` where needed, plus source-return conditions. | Do not mint `U.CodeSpace` and do not treat probe output, probe JSON, or benchmark output as structure adequacy, assurance, release evidence, or assurance evidence. |
| Coarsening, compression, and RG-adjacent traditions | Adopt the need to say what structure is preserved and what is lost. | Use `StructuralCoarseningDescription@Context` and `SourceReturnCondition` before relying on a coarsened structure for action. | RG, epiplexity, structural information, and equivalence reasoning are governed by C.29, C.16, or another governing pattern named for the claim being made. |
| GonzoML neural-network architecture discussions as practitioner-language intake | Adapt block replacement, dataflow change, memory placement, cache placement, path-selection, pruning, distillation, and architecture-search wording as general architecture-operation recognition material. | When such wording is used, keep block, cache, expert, router, gate, and similar words as `C.30.STRAT` source labels until changed structure kind, source relation, base-dependence relation, evidence path, lens output, preserved structure, lost structure, and FPF pattern applications are recovered. | Neural-network labels, benchmark results, ablations, or pruning masks do not become structure ontology, architecture decisions, evidence sufficiency, gate passage, assurance, or architecture adequacy by themselves. |

