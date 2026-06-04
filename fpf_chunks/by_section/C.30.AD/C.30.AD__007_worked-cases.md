---
chunk_kind: "child"
pattern_id: "C.30.AD"
pattern_title: "Architecture Description Adequacy"
section_id: "C.30.AD:5"
section_title: "Worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD/C.30.AD__007_worked-cases.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "C.30.AD — Architecture Description Adequacy"
  - "C.30.AD:5 — Worked cases"
line_start: 52088
line_end: 52103
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.3"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TGA-FLOW-REL"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.8"
  - "F.18"
keywords:
  - "ArchitectureDescription@Context"
  - "architecture description"
  - "architecture description use card"
  - "architecture structural view"
  - "correspondence"
  - "source return"
  - "specification-use boundary"
  - "viewpoint"
---

### C.30.AD:5 - Worked cases

| Case | C.30.AD treatment |
| --- | --- |
| "The architecture is documented in this view set." | The view set is an architecture description or publication set only if it names one `ArchitectureOf@Context`, selected structures, viewpoints, view refs, and admissible use. It is not the architecture itself. |
| A TGA graph is included in an architecture document. | Use `E.18` for graph, path, and crossing semantics and `C.30.TGA-FLOW-REL` when the graph is used by architecture. `C.30.AD` records only the architecture-description use and source-return boundary. |
| A model card claims deployment safety. | Use `C.30.AD` only if the card describes an architecture claim or structure view. Safety assurance uses `B.3`; evidence uses `A.10`; release uses `A.21`. |
| A generated code-agent relation graph shows modules and calls. | Treat the graph as a generated view or source publication. Recover observed, inferred, and unknown relations; use `C.30.ASV` or `C.30.TGA-FLOW-REL` only when an architecture structural view or flow relation is live. |
| A multi-view description set has functional, deployment, control, and evidence-reuse views. | Each view has an `ArchitectureDescriptionViewMembership@Context` line and a referenced `C.30.ASV` view record. Evidence-reuse claims do not stay inside C.30.AD. |
| A plant safety architecture description combines control, deployment, evidence, and operator-view material. | `C.30.AD` records the architecture-description chain and correspondence among views. `C.30.LCA` governs the control view; `A.10`, `G.6`, or `B.3` governs evidence or assurance; `A.15` is used only if role-enactor semantics are live. |
| A product-line platform document reuses module-interface, variability, and deployment views across products. | `C.30.AD` records which architecture claim and structural views the document uses, plus source-return conditions for product variation. `A.6.M` repairs module-interface relations; `C.31.RSA` accounts reusable structure or bespoke residue only after structure refs and accounting basis are declared. |
| A multi-view architecture description says local optimization at one declared holon level creates frustration in another. | `C.30.AD` records the description membership, correspondence, and source-return boundary. `C.30.ILC` governs the residual; `C.29` is used only if the description contains a recoverable level mapping or scale mapping with preserved structure and lost structure. |
| An architecture document compares residual-reducing candidate decompositions or optimization moves. | `C.30.AD` records only the description or publication use of that comparison. Candidate sets and selected-set publication use `G.5` or an admitted architecture synthesis receiving pattern; final local choice uses `C.11`; measurement or comparison claims use their exact patterns. |
| A review note, dashboard, or generated report describes gaps in an architecture description rather than the architecture itself. | The architecture description can be the current `EntityOfConcern`; the second description is handled as a Description, view, source relation, publication face, review record, or evaluation record over that EoC. `C.30.AD` keeps the chain to the underlying `ArchitectureOf@Context` visible without treating the second description as the architecture, the residual, the decision, or the proof. |


