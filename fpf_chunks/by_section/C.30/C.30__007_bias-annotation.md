---
chunk_kind: "child"
pattern_id: "C.30"
pattern_title: "Grounded Architecture and Selected-Structure Adequacy"
section_id: "C.30:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30/C.30__007_bias-annotation.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "C.30 — Grounded Architecture and Selected-Structure Adequacy"
  - "C.30:6 — Bias-Annotation"
line_start: 57162
line_end: 57175
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.3"
  - "A.6.F"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "E.24.PUB"
  - "F.18"
  - "G.5"
  - "G.6"
keywords:
  - "ArchitectureOf@Context"
  - "architecture claim"
  - "architecture question card"
  - "architecture-description boundary"
  - "artifact-as-architecture guard"
  - "candidate architecture use"
  - "grounded architecture"
  - "selected structure"
---

### C.30:6 - Bias-Annotation

Lenses tested: **Arch**, **Onto**, **Epist**, **Prag**, **Did**, **Gov**. Scope: FPF architecture-description use over holons.

| Bias risk | Mitigation |
| --- | --- |
| Module-diagram bias | Keep module structure and interface relation as one structure family among several; use `C.30.ASV` and the module-and-interface repair pattern when a module or interface claim is being made. |
| Tool-model bias | Treat notation, tool model, generated relation graph, diagram, and dashboard as description, specification-use, or publication forms unless an exact direct relation gives the source material a more specific use. |
| Check-only bias | The first output is an architecture question card plus action palette, not a checklist that only detects mistakes. |
| Assurance or gate bias | Architecture descriptions do not certify safety, evidence sufficiency, release, or gate passage; use the applicable pattern for each such claim. |
| Didactic-thinning risk | Semantic repair preserves why the distinction matters: the pattern begins with the practitioner situation, payoff, stop condition, and first architecture move. |

This checklist verifies the preceding guidance after the practitioner has chosen the selected architecture candidate use; it is not a required project control form and not a substitute for the card, note, view, relation, or repair use above.

