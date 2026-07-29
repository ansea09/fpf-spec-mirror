---
chunk_kind: "child"
pattern_id: "C.35"
pattern_title: "Structural Synthesis and Discovery Adequacy"
section_id: "C.35:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.35/C.35__011_rationale.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "C.35 — Structural Synthesis and Discovery Adequacy"
  - "C.35:10 — Rationale"
line_start: 66923
line_end: 66930
dependencies:
  - "A.22"
  - "A.6.M"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.ADR"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "E.18"
  - "G.5"
keywords:
  - "DSM"
  - "LLM"
  - "NAS"
  - "candidate admission"
  - "described structure"
  - "generated carrier"
  - "produced carrier"
  - "source return"
  - "structural discovery"
  - "structural synthesis"
---

### C.35:10 - Rationale

Architecture synthesis increasingly receives outputs from search, model transformation, LLM proposal, code-agent mapping, DSM modularization, NAS, simulation, benchmark, and source discovery. Refusing those outputs would waste useful structure. Accepting them as architecture would create false authority. C.35 occupies the middle position: admission of a produced carrier for a declared architecture use.

The separation of produced carrier, described structure, selected candidate structure, bearer boundary, eval return, and decision authority is the core ontology of the pattern. Without that separation, C.35 would duplicate C.32, PAD, ADR, ACE, C.16, C.18, C.19, G.5, evidence, assurance, gate, release, method, or work governing patterns.

The source families explain the chain. MBSE query practice and generated views show why produced descriptions can reveal and omit structure. Graph grammars and model transformations show why transformation trace and preserved structure matter. DSM and MDM work shows semantic-alignment risk between structural optimization and functional priors. Multi-objective NAS shows why Pareto fronts and generated architecture graphs need search-space, criteria, and bearer recovery. Sapunov, ToCS, and GonzoML show why agent maps and neural architecture labels need observation, uncertainty, and source-label recovery before candidate admission.

