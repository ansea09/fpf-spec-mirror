---
chunk_kind: "child"
pattern_id: "C.30.AD"
pattern_title: "Architecture Description Adequacy"
section_id: "C.30.AD:5"
section_title: "Archetypal Grounding (Worked Cases)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD/C.30.AD__007_archetypal-grounding-worked-cases.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "C.30.AD — Architecture Description Adequacy"
  - "C.30.AD:5 — Archetypal Grounding (Worked Cases)"
line_start: 59402
line_end: 59417
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
  - "E.10.D2"
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
| A transformation-flow graph expression is included in an architecture document. | Use `E.18` for graph, path, and crossing semantics and `C.30.TFS-REL` when the graph is used by architecture. `C.30.AD` records the exact description and its path from the source expression into that use; add a source-return condition only if a stronger use must return to the named source or exact defining or constraining ClaimGraph. The graph expression or rendering creates no actual transformation. |
| A model card claims deployment safety. | Use `C.30.AD` only if the card publishes or represents a description episteme about an exact architecture-side object. Safety assurance uses `B.3`; evidence uses `A.10`; release uses `A.21`. |
| A generated code-agent relation graph shows modules and calls. | Treat the graph as a generated representation or source publication. Recover observed, inferred, and unknown relations; use `C.30.ASV` or `C.30.TFS-REL` only when an exact architecture structural view or flow relation is being used. Generation and display establish neither relation occurrence nor view membership. |
| A multi-view description set has functional, deployment, control, and evidence-reuse views. | Identify every description episteme separately, including its EntityOfConcern and scheme. Each cited view also names its exact viewpoint and obtaining conformance relation; an `ArchitectureDescriptionViewUseClaim` records set use without minting membership. Evidence-reuse claims do not stay inside C.30.AD. |
| A plant safety architecture description combines control, deployment, evidence, and operator-view material. | `C.30.AD` records exact description identities, view conformance, description-set use, and correspondence among views. Use `C.30.LCA` for the control view and `A.10`, `G.6`, or `B.3` for evidence or assurance. If a system-role assignment, F.6 Work attribution, authority, allocation, or responsibility is claimed, cite its separate direct relation; otherwise record the exact missing governor. |
| A product-line platform document reuses module-interface, variability, and deployment views across products. | `C.30.AD` records exact description epistemes, architecture claims carried as content, structural views, and source-to-use paths for reused views. A source-return condition is added only when a product-specific use exceeds the declared reuse boundary. `A.6.M` normalizes module-interface claims and routes any proposed direct relation; `C.31.RSA` accounts reusable structure or bespoke residue only after structure refs and accounting frame are declared. |
| A multi-view architecture description says local optimization at one declared holon level creates frustration in another. | `C.30.AD` records set use, correspondence, and each view use boundary. Use `C.30.ILC` for the residual; use `C.29` only when the description contains a recoverable level or scale mapping with preserved and lost structure. |
| An operations model groups individual queues and interactions into three broad bands. | Name the operating subject, the fine and coarse description structures, the grouping map, the distinctions preserved and lost, and the use of the three-band view. This establishes a coarser description, not three subject levels. Use `C.30.STRAT`, `C.29`, `A.22`, or `C.30` only if their separate subject or model claims are needed and supported. |
| An architecture document compares residual-reducing candidate decompositions or optimization moves. | Record with `C.30.AD` only the exact description or publication use of that comparison. Use `C.32.MLAO` for residual-reducing frames, `C.32` for candidate palettes, `A.19.CPM` or `A.19.SelectorMechanism` for comparison and selector-policy use, `C.18` or `C.19` for archives, fronts, and current-pool treatment, `G.5` for selected-set result declaration, and `C.11` for final local choice. For a measurement claim, use the pattern that defines or tests the measured characteristic and result. |
| A review note, dashboard, or generated report describes gaps in an architecture description rather than the architecture itself. | Treat the second description as its own `U.Episteme` and name its source, representation, publication, review, or evaluation relation directly. Keep the path to the first description and its EntityOfConcern visible without treating either description as architecture, residual, decision, or proof. |

