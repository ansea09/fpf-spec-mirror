---
chunk_kind: "child"
pattern_id: "C.35"
pattern_title: "Structural Synthesis and Discovery Adequacy"
section_id: "C.35:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.35/C.35__006_archetypal-grounding.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "C.35 — Structural Synthesis and Discovery Adequacy"
  - "C.35:5 — Archetypal Grounding"
line_start: 65372
line_end: 65393
dependencies:
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.1"
  - "A.22"
  - "A.3.4"
  - "A.6.M"
  - "A.6.RCD"
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
  - "C.36"
  - "E.18"
  - "F.6"
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

### C.35:5 - Archetypal Grounding

Tell: C.35 is the pattern for admitting or rejecting an exact generated or discovered result before another architecture claim relies on it. The result may come from search, clustering, query, learning, transformation, simulation, or discovery. C.35 does not search, select, decide, or realize architecture. It asks what the exact result is, whether the organization it concerns already obtains or is only proposed, what the intended use still requires, and what overread or return keeps it from acquiring false authority.

Show - generated claim and diagram not yet architecture. An LLM returns proposal claim `MedicalDeviceProposal-7` and diagram `MedicalDeviceDiagram-7`. The ordinary C.35 result is:

```text
Result: MedicalDeviceProposal-7.
Organization: a proposed device organization; its constituents and relations do not yet obtain.
Next-use condition: C.32 may use it after the missing safety constraint and bearer question are explicit.
Limit and return: do not read the proposal or diagram as A.22 structure or decision; return to the claim when either gap changes.
```

This is enough for the immediate candidate-use boundary. Add the generative-proposal branch only if the receiver relies on its constraints, omissions, or validation needs. Treat `MedicalDeviceDiagram-7` as a separate C.29 representation only when graphical correspondence matters; no source or preservation account is invented without a declared baseline.

Show - DSM and MDM clustering. A DSM modularization returns a clustering result based on co-change and interface hints. This is the discovery branch: C.35 identifies the exact claim-bearing cluster result and its extraction basis and records which dependencies are observed, which modular interpretation is inferred, what remains unknown, which matrix region was covered or unexplored, the uncertainty, and the validation needed before use. The inferred modular organization stays in its exact architecture claim; it is not an A.22 structure until the constituents, obtaining relations, applied constraints, and named use frame resolve. When matrix operations matter, C.29 separately identifies the representation and represented dependency object. A comparison with an earlier modularization may add an exact declared baseline and preservation account, but clustering alone does not require one.


Show - NAS result. A multi-objective NAS run returns a modal architecture claim about a proposed neural organization together with a graph representation and Pareto result. This is the generative-proposal branch: C.35 keeps those identities separate and records the search constraints, proposed organization content, known deployment and evidence omissions, bearer boundary, and validation and eval needs. The graph is a C.29 representation, not proof that the proposed relation occurrences obtain. C.35 does not invent a preserved-dataflow claim unless the run explicitly transforms or compares against a declared baseline. `C.32` may consume the proposal as candidate input; `C.32.ACE` handles evaluation results.

Show - graph grammar or model transformation. A graph-grammar Method is applied in dated generation Work and returns a claim-bearing result plus a graph representation for a product-line model. This is the transformation branch: C.35 names the Method, exact Work when performed-work reliance is current, exact source and result objects, rules, preserved interfaces, lost manufacturing constraints, and transformation trace. If the resulting organization is only proposed, it remains modal content in an exact architecture claim and the graph remains its C.29 representation. Source or result A.22 structures are cited only when their four discriminators independently resolve. If the use additionally asserts an actual formal or world-side change, it cites the exact A.3.4 occurrence and the separately governed Work-to-change or A.15.PROD claim; otherwise `model transformation` remains the Method or operation-family label and no `U.Transformation` is inferred. C.34 may check preservation; C.32 may admit the proposal without actualizing it.

