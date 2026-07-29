---
chunk_kind: "child"
pattern_id: "C.30.AD"
pattern_title: "Architecture Description Adequacy"
section_id: "C.30.AD:5.1"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD/C.30.AD__008_bias-annotation.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "C.30.AD — Architecture Description Adequacy"
  - "C.30.AD:5.1 — Bias-Annotation"
line_start: 60200
line_end: 60209
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

### C.30.AD:5.1 - Bias-Annotation

| Bias | How C.30.AD prevents it |
| --- | --- |
| Description-as-architecture bias | `ArchitectureDescription@Context` points to one `ArchitectureOf@Context`; the description does not become the architecture, selected structure, or described holon. |
| View-as-structure bias | Every architecture structural view remains bound to `C.30.ASV` or another structure-governing pattern; C.30.AD records membership, correspondence, source return, and use boundary. |
| Publication-as-authority bias | Publication form, dashboard polish, model-card form, or report label does not establish evidence, assurance, gate, decision, work-authorization, or release-authorization claims. |
| Freshness-as-evidence bias | A freshness cue bounds admissible use; it does not make the description evidence-sufficient. |
| Semio-bias in architecture work | C.30 remains centered on architecture as EntityOfConcern; C.30.AD opens only when the architecture description itself is the current EntityOfConcern. |

