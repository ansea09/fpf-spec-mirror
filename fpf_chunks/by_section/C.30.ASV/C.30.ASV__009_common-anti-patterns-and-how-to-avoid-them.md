---
chunk_kind: "child"
pattern_id: "C.30.ASV"
pattern_title: "Architecture Structural View Adequacy (ASV)"
section_id: "C.30.ASV:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ASV/C.30.ASV__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "C.30.ASV — Architecture Structural View Adequacy (ASV)"
  - "C.30.ASV:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 59109
line_end: 59122
dependencies:
  - "A.1"
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
  - "C.2.1"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.10"
  - "E.10.D2"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "E.24.PUB"
  - "F.18"
  - "G.6"
keywords:
---

### C.30.ASV:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Module diagram as architecture view** | One module-interface diagram is treated as the whole architecture or as a `U.View` by appearance. | Use structure-kind triage; keep module-interface as one structure kind and apply exact E.17.0 conformance only when view membership matters. |
| **Viewpoint as structure kind** | `VP.Functional`, `VP.ModuleInterface`, or another viewpoint is used as if it were the selected structure kind. | Recover `ArchitectureStructureKindRef`; keep its binding to an exact viewpoint episteme separate. |
| **Structure kind as viewpoint** | `FunctionalStructure` or `ControlStructure` is treated as if it were already an admitted viewpoint P. | Keep structure-kind classification separate; when viewpoint reuse is needed, resolve one exact `U.ViewpointRef` from a materialized local catalogue declaration to exact P and test E.17.0 conformance. |
| **Publication-face collapse** | A diagram, model, table, dashboard, generated relation graph, ADR, or C4 view is treated as the view episteme. | Recover description episteme, representation, and E.24.PUB occurrence, form, and carrier separately; use `ArchitectureStructuralView` only if exact conformance obtains and the view changes action. |
| **Single-view decision** | A decision uses one architecture view as if it covered all affected structures. | Name affected structures and view refs, or narrow the decision to the single view's admissible use. |
| **Lost-structure silence** | Extracted, generated, coarsened, or compressed views hide distinctions but still justify action. | Add hidden structure and lost structure and source-return condition, or narrow admissible use. |
| **Proof overread** | The structural view is used as evidence sufficiency, safety proof, causal proof, gate decision, or work record. | Use the applicable evidence, assurance, causal, gate, or work pattern and keep ASV only to view adequacy. |
| **Risk color as security architecture** | A red, yellow, or green risk cell, risk matrix, maturity score, or compliance color stands in for `SecurityTrustBoundaryStructure` or resource-allocation priority. | Recover protected asset or effect, trust boundary, untrusted input, privilege or authority relation, data flow or control flow, abuse or misuse path, and the evidence named by value, assurance, measurement, causal, gate, selection, or allocation claim kind if that claim is being made; do not treat ordinal risk color as security architecture adequacy, resource-allocation priority, or gate passage. |
| **Taxonomy without action** | The text classifies a view but does not say what changes in practice. | Add `admissibleArchitectureMove` or stop at Plain recognition wording. |

