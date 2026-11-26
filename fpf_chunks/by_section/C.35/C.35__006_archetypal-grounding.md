---
chunk_kind: "child"
pattern_id: "C.35"
pattern_title: "Assess Generated or Discovered Results for Architecture Use"
section_id: "C.35:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.35/C.35__006_archetypal-grounding.md"
commit_sha: "9d38fbfe4ce5b72d8fe05e839cbca0025a5b31cf"
heading_path:
  - "C.35 — Assess Generated or Discovered Results for Architecture Use"
  - "C.35:5 — Archetypal Grounding"
line_start: 85658
line_end: 85691
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

**What a generated proposal establishes.** An LLM returns proposal `MedicalDeviceProposal-7` and diagram `MedicalDeviceDiagram-7`. An architect considering it for the candidate set records the following.

```text
Result: MedicalDeviceProposal-7.
Organization: proposed arrangement of device components. The proposal leaves open which parts of that arrangement are already installed.
Next use: C.32 may examine the proposed arrangement as an alternative now. Its feasibility remains open.
Limit and return: before relying on feasibility, establish the applicable constraints and that components capable of meeting them can be provided under the intended conditions. To establish what is installed, use the device's applicable as-built evidence.
```

This is enough for the immediate candidate-use boundary. Add the generative-proposal branch only if the receiver relies on its constraints, omissions, or validation needs.

Treat `MedicalDeviceDiagram-7` as a separate representation when graphical correspondence matters, using C.30.AD or C.30.ASV for its architecture description or view and C.29 when a mathematical-representation choice, transfer, or reliance question remains. A question about which requirements the designer used can arise in a new design. A claim to preserve the organization of an earlier design requires a baseline.

**DSM and MDM clustering.** A team groups the rows of a dependency matrix using co-change observations and interface data. Check whether the reported groups satisfy the grouping rule on that matrix. If the rule allows several groupings, the saved output identifies the one returned by this run. Reproduction also suffices when the procedure and its inputs determine the same choice, including any tie-breaking or random choices that mattered. To infer that the corresponding components perform one function, the team must relate the observed dependencies to that function and check what the matrix omits. A different decision is to reorganize the components into those groups. That proposal needs a reason the new allocation would serve the design. Use the discovery or proposal branch for the claim actually made.

Retain the matrix's mapping to the represented dependencies and the validity conditions of its operations; use C.29 when choosing, transferring, or relying on that representation remains unresolved. A comparison with an earlier modularization may add a declared baseline and preservation account, but clustering alone does not require one.


**NAS result.** A multi-objective neural architecture search returns a proposed neural organization and its graph. No evaluated alternative matched or improved on the proposal on every criterion and improved on it on at least one. Report that comparison over the evaluated set. To report the same conclusion over the full search space, establish coverage or a bound that excludes a dominating alternative. Keep the search constraints, hardware conditions and validation needed for deployment with the proposal.

The graph represents the proposal; C.29 applies when a separate mathematical-representation choice, transfer, or reliance question remains. The graph does not prove that the proposed relation occurrences obtain. C.35 does not invent a preserved-dataflow claim unless the run explicitly transforms or compares against a declared baseline.

`C.32` may consume the proposal as candidate input; `C.32.ACE` handles evaluation results.

**Graph grammar or model transformation.** A graph-grammar Method is applied in dated generation Work and returns a claim-bearing result plus a graph representation for a product-line model. This is the transformation branch: C.35 names the Method, Work when performed-work reliance is current, source and result objects, rules, preserved interfaces, lost manufacturing constraints, and transformation trace.

If the resulting organization is only proposed, it remains modal content in an architecture claim and the graph remains a representation of that proposal, with C.29 used for an unresolved mathematical-representation choice, transfer, or reliance question. Source or result A.22 structures are cited only when their four discriminators independently resolve.

If the use additionally asserts an actual formal or world-side change, it cites the A.3.4 occurrence and the separately governed Work-to-change or A.15.PROD claim; otherwise `model transformation` remains the Method or operation-family label and no `U.Transformation` is inferred. C.34 may check preservation; C.32 may admit the proposal without actualizing it.

