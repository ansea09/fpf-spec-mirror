---
chunk_kind: "child"
pattern_id: "C.30.AD"
pattern_title: "Architecture Description Adequacy"
section_id: "C.30.AD:5"
section_title: "Archetypal Grounding (Worked Cases)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD/C.30.AD__007_archetypal-grounding-worked-cases.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "C.30.AD — Architecture Description Adequacy"
  - "C.30.AD:5 — Archetypal Grounding (Worked Cases)"
line_start: 60550
line_end: 60564
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.15.5"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.3"
  - "A.6.3.NAR"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18"
  - "C.19"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD.BA"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.MOVE"
  - "E.11.PUR"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.8"
  - "F.18"
  - "G.5"
keywords:
  - "ArchitectureDescription@Context"
  - "architecture description"
  - "architecture description use card"
  - "architecture structural view"
  - "candidate-description boundary"
  - "correspondence"
  - "source return"
  - "specification-use boundary"
  - "viewpoint"
---

### C.30.AD:5 - Archetypal Grounding (Worked Cases)

| Case | C.30.AD treatment |
| --- | --- |
| "The architecture is documented in this view set." | Treat the set as a package of separately identified architecture-description epistemes only if each has an exact claim graph, one EntityOfConcern, and effective `U.ReferenceScheme`. A member is a `U.View` only with its exact viewpoint episteme and independently obtaining E.17.0 conformance relation. The set is not the architecture, relation occurrence, or selected structure. |
| A transformation-flow graph expression is included in an architecture document. | Use `E.18` for graph, path, and crossing semantics and `C.30.TFS-REL` when the graph is used by architecture. `C.30.AD` records the exact description and its path from the source expression into that use; add a source-return condition only if a stronger use must return to the named source or governing pattern. The graph expression or rendering creates no actual transformation. |
| A model card claims deployment safety. | Use `C.30.AD` only if the card publishes or represents a description episteme about an exact architecture-side object. Safety assurance uses `B.3`; evidence uses `A.10`; release uses `A.21`. |
| A generated code-agent relation graph shows modules and calls. | Treat the graph as a generated representation or source publication. Recover observed, inferred, and unknown relations; use `C.30.ASV` or `C.30.TFS-REL` only when an exact architecture structural view or flow relation is being used. Generation and display establish neither relation occurrence nor view membership. |
| A multi-view description set has functional, deployment, control, and evidence-reuse views. | Identify every description episteme separately, including its EntityOfConcern and scheme. Each cited view also names its exact viewpoint and obtaining conformance relation; an `ArchitectureDescriptionViewUseClaim` records set use without minting membership. Evidence-reuse claims do not stay inside C.30.AD. |
| A plant safety architecture description combines control, deployment, evidence, and operator-view material. | `C.30.AD` records exact description identities, view conformance, description-set use, and correspondence among views. `C.30.LCA` governs the control view; `A.10`, `G.6`, or `B.3` governs evidence or assurance; `A.15` is used only if allocation-responsibility semantics apply. |
| A product-line platform document reuses module-interface, variability, and deployment views across products. | `C.30.AD` records exact description epistemes, architecture claims carried as content, structural views, and source-to-use paths for reused views. A source-return condition is added only when a product-specific use exceeds the declared reuse boundary. `A.6.M` normalizes module-interface claims and routes any proposed direct relation; `C.31.RSA` accounts reusable structure or bespoke residue only after structure refs and accounting frame are declared. |
| A multi-view architecture description says local optimization at one declared holon level creates frustration in another. | `C.30.AD` records description-set use, correspondence, and each view's declared use boundary. `C.30.ILC` governs the residual; `C.29` is used only if the description contains a recoverable level mapping or scale mapping with preserved structure and lost structure. |
| An architecture document compares residual-reducing candidate decompositions or optimization moves. | `C.30.AD` records only the exact description or publication use of that comparison. Residual-reducing frames use `C.32.MLAO`; candidate palettes use `C.32`; comparison and selector-policy use `A.19.CPM` or `A.19.SelectorMechanism`; archives and fronts use `C.18` or `C.19`; selected-set publication uses `G.5`; final local choice uses `C.11`; measurement claims use their governing patterns. |
| A review note, dashboard, or generated report describes gaps in an architecture description rather than the architecture itself. | The exact architecture-description episteme can be the one EntityOfConcern for that second-description use. Govern the second description as its own `U.Episteme` and name any source-to-use, representation, publication, review, or evaluation relation directly. Keep the chain to the first description's exact EntityOfConcern visible without treating either description as architecture, residual, decision, or proof. |

