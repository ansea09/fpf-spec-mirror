---
chunk_kind: "child"
pattern_id: "C.30.P"
pattern_title: "Architecture and Structure Precision Restoration"
section_id: "C.30.P:5"
section_title: "Direct governing-pattern assignments"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.P/C.30.P__007_direct-governing-pattern-assignments.md"
commit_sha: "1f413fcd23f4ea26956a45d67dde57bb233f6ad9"
heading_path:
  - "C.30.P — Architecture and Structure Precision Restoration"
  - "C.30.P:5 — Direct governing-pattern assignments"
line_start: 60161
line_end: 60193
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18"
  - "C.19"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.17"
  - "E.8"
  - "G.5"
keywords:
---

### C.30.P:5 - Direct governing-pattern assignments

| Recovered use, claim kind, or admissible-use boundary | Governing pattern |
| --- | --- |
| selected structure, structural description, structure source-return | `A.22` |
| `ArchitectureOf@Context`, selected architecture-relevant structure, thin conditional `ArchitectureDescription@Context` bridge use, architecture question card | `C.30` |
| full `ArchitectureDescription@Context` mechanism, architecture-description multi-view set, architecture-description specification-use boundary | `C.30.AD` |
| architecture structural view, structure-kind view, hidden or lost structure | `C.30.ASV` |
| transformation-flow graph expression, flow relation, architecture-to-transformation-flow relation | `C.30.TFS-REL` when an architecture-to-transformation-flow relation claim is being made; otherwise `E.18` or the governing pattern for the claim being made |
| architecture-synthesis wording | Recover the concrete claim kind, then use the architecture-synthesis routing note below. |
| control structure view, LCA sketch or control sketch | `C.30.LCA` when an architecture control-structure view claim is being made |
| cross-scope conflict or frustration triage | `C.30.ILC` when that question is being asked |
| source, publication, carrier, view, face, `PublicationUnit`, dashboard, ADR, documentation, source-return | `C.2.P`, `E.17`, `E.17.0`, or the publication or source-use pattern governing the claim |
| relation construction, basedness, source, base-dependence, evidence and relation-claim discrimination, endpoint compression, comparison | `A.6.P` or the A.6 specialization selected by the recovered claim |
| function, functional, functionality, effect, module, interface, or signature claim | `A.6.F`, `A.6.M`, A.6 signature and slot pattern, or the retained module, interface, or signature specialization selected by the claim |
| stratification or source labels such as `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, or `gate` | `C.30.STRAT`; after recovery, use `A.22`, `C.30`, `C.30.ASV`, `C.30.LCA`, `C.30.TFS-REL`, `A.6.M`, `A.6.F`, `E.18`, `C.16.P`, `C.29`, or the pattern governing the recovered claim |
| mathematical lens, mapping, model, similarity, preserved-structure and lost-structure as mathematical-lens use | `C.29` |
| characteristic, scale, metric, score, indicator, threshold, architecture score, quality coordinate | `C.16.P`, then `C.16`, `A.19`, `C.25`, `E.21`, or the pattern governing the claim |
| quality-term or evaluative characterization | `C.16.Q`, `C.25`, `E.21`, or the characterization pattern governing the claim |
| evidence, proof, validation, witness | `A.10` or the evidence pattern governing the claim |
| assurance, engineering justification, safety case | `B.3` or the assurance pattern governing the claim |
| gate, admissibility, release, approval | `A.20`, `A.21`, release or admissibility pattern, or the gate pattern governing the claim |
| work, method, implementation, operation, change execution | `A.15`, `A.15.4`, `U.Method`, `U.MethodDescription`, or the work or method pattern governing the claim |
| decision, choice, trade-off result | `C.11` or the decision pattern governing the claim |
| causal-use or intervention claim | `C.28` |

Architecture-synthesis routing note:

- Use `C.32`, `C.32.MLAO`, `C.32.CONWAY`, or `C.32.FAIL` when the recovered claim is a candidate palette, residual-reducing multilevel frame, transformer and transformed correspondence frame, or architecture-synthesis repair cue.
- Use `A.19.CPM`, `A.19.SelectorMechanism`, `C.11`, or `G.5` when the recovered claim is comparison-policy use, selector-policy use, local choice, or selected-set publication.
- Use `C.18` or `C.19` when the recovered claim is archive, front, or pool policy.
- For transformation-flow, function, module, transformer, mathematical-lens, relation-signature, affordance, architecture role, or move-like wording, recover that claim kind first and use its governing pattern by value.

