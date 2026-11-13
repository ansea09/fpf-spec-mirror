---
chunk_kind: "child"
pattern_id: "C.35"
pattern_title: "Assess Generated or Discovered Results for Architecture Use"
section_id: "C.35:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.35/C.35__006_archetypal-grounding.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "C.35 — Assess Generated or Discovered Results for Architecture Use"
  - "C.35:5 — Archetypal Grounding"
line_start: 85111
line_end: 85144
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
  - "candidate input"
  - "discovered result"
  - "generated result"
  - "modal architecture proposal"
  - "structural discovery"
  - "structural synthesis"
---

### C.35:5 - Archetypal Grounding

C.35 is the pattern for admitting or rejecting a generated or discovered result before another architecture claim relies on it. The result may come from search, clustering, query, learning, transformation, simulation, or discovery. C.35 does not search, select, decide, or realize architecture. It asks what the result is, which organization it concerns, whether the claim about that organization is established, refuted or unestablished, or instead presents a proposal, what use it supports, and which conditions or limitations affect further reliance.

**Generated claim and diagram not yet architecture.** An LLM returns proposal claim `MedicalDeviceProposal-7` and diagram `MedicalDeviceDiagram-7`. The ordinary C.35 result is:

```text
Result: MedicalDeviceProposal-7.
Organization: a proposed device organization; its constituents and relations do not yet obtain.
Next-use condition: C.32 may use it after the missing safety constraint and bearer question are explicit.
Limit and return: do not read the proposal or diagram as A.22 structure or decision; return to the claim when either gap changes.
```

This is enough for the immediate candidate-use boundary. Add the generative-proposal branch only if the receiver relies on its constraints, omissions, or validation needs.

Treat `MedicalDeviceDiagram-7` as a separate representation when graphical correspondence matters, using C.30.AD or C.30.ASV for its architecture description or view and C.29 when a mathematical-representation choice, transfer, or reliance question remains. A source or preservation account requires a declared baseline.

**DSM and MDM clustering.** A DSM modularization returns a clustering result based on co-change and interface hints. This is the discovery branch: C.35 identifies the claim-bearing cluster result and its extraction basis and records which dependencies are observed, which modular interpretation is inferred, what remains unknown, which matrix region was covered or unexplored, the uncertainty, and the validation needed before use. The inferred modular organization remains an unestablished claim about the existing organization until the needed constituents, obtaining relations, applied constraints and use frame are supported. A proposed reorganization remains a distinct modal claim.

Retain the matrix's mapping to the represented dependencies and the validity conditions of its operations; use C.29 when choosing, transferring, or relying on that representation remains unresolved. A comparison with an earlier modularization may add a declared baseline and preservation account, but clustering alone does not require one.


**NAS result.** A multi-objective NAS run returns a modal architecture claim about a proposed neural organization together with a graph representation and Pareto result. This is the generative-proposal branch: C.35 keeps those identities separate and records the search constraints, proposed organization content, known deployment and evidence omissions, bearer boundary, and validation and eval needs.

The graph represents the proposal; C.29 applies when a separate mathematical-representation choice, transfer, or reliance question remains. The graph does not prove that the proposed relation occurrences obtain. C.35 does not invent a preserved-dataflow claim unless the run explicitly transforms or compares against a declared baseline.

`C.32` may consume the proposal as candidate input; `C.32.ACE` handles evaluation results.

**Graph grammar or model transformation.** A graph-grammar Method is applied in dated generation Work and returns a claim-bearing result plus a graph representation for a product-line model. This is the transformation branch: C.35 names the Method, Work when performed-work reliance is current, source and result objects, rules, preserved interfaces, lost manufacturing constraints, and transformation trace.

If the resulting organization is only proposed, it remains modal content in an architecture claim and the graph remains a representation of that proposal, with C.29 used for an unresolved mathematical-representation choice, transfer, or reliance question. Source or result A.22 structures are cited only when their four discriminators independently resolve.

If the use additionally asserts an actual formal or world-side change, it cites the A.3.4 occurrence and the separately governed Work-to-change or A.15.PROD claim; otherwise `model transformation` remains the Method or operation-family label and no `U.Transformation` is inferred. C.34 may check preservation; C.32 may admit the proposal without actualizing it.

