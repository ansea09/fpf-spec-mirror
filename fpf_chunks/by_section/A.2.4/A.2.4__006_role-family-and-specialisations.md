---
chunk_kind: "child"
pattern_id: "A.2.4"
pattern_title: "U.EvidenceRole"
section_id: "A.2.4:5"
section_title: "Role family and specialisations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.4/A.2.4__006_role-family-and-specialisations.md"
commit_sha: "e3fedf42dc7cb5d12905913b5a0b0e951ed7d254"
heading_path:
  - "A.2.4 — U.EvidenceRole"
  - "A.2.4:5 — Role family and specialisations"
line_start: 3027
line_end: 3070
dependencies:
  - "A.10"
  - "A.2"
  - "B.3"
keywords:
  - "claim"
  - "episteme"
  - "evidence"
  - "justification"
  - "support"
---

### A.2.4:5 - Role family and specialisations
#### A.2.4:5.3 - Causal evidence-role specialisations

For causal-use support, `U.EvidenceRole` may receive these context-local specialisations as evidence-role terms:

```text
InterventionEvidenceRole
RealizedCounterfactualSampleEvidenceRole
IdentifiedCounterfactualEstimateEvidenceRole
SimulationOnlyCounterfactualOutputRole
```

These are evidence-role specialisations, not new evidence-source authorities. `identifiedCounterfactualEstimateSupportBasis` and `realizedCounterfactualSampleSupportBasis` are both counterfactual support bases but are not the same support basis. `SimulationOnlyCounterfactualOutputRole` may support `simulationOnlyCounterfactualOutputBasis` and bounded model-supported use under `C.28`; it never becomes `interventionalActionSupportBasis` or `realizedCounterfactualSampleSupportBasis` by vocabulary, validation, or role relabeling alone.

What changes in practice: an episteme holding `SimulationOnlyCounterfactualOutputRole` cannot be relabelled as `RealizedCounterfactualSampleEvidenceRole` just because the simulation mentions a counterfactual; the role assignment must preserve whether the support basis is observation, intervention, realized counterfactual sample, identified counterfactual estimate, or simulation-only output.

The corresponding `CausalEvidenceSupportBasis` values are governed by `C.28`: `observationalAssociationSupportBasis`, `interventionalActionSupportBasis`, `realizedCounterfactualSampleSupportBasis`, `identifiedCounterfactualEstimateSupportBasis`, and `simulationOnlyCounterfactualOutputBasis`. `A.2.4` only classifies evidence roles held by epistemes; it does not mint a second causal support-basis value set.

What this does not authorize: `A.2.4` does not decide the causal-use question, estimand, identification, or counterfactual sampling realizability; it preserves the evidence-role assignment and the authority-reference boundary so `C.28` and `B.3` can judge the causal-use claim without vocabulary laundering.

`U.EvidenceRole` is a **role kind** refined by **specialisation** (no mereology of roles). The recommended, substrate‑neutral specialisations are:

**5.1 Axiomatic line (deductive inside a fixed theory)**

* **`AxiomaticProofRole`** — a proof that **entails** a target statement in a declared `U.TheoryVersion`.
* **`CounterexampleRole`** — a witness that **refutes** a universally quantified claim in the theory.
* **`DerivationRole`** — a lemma or intermediary derivation establishing a dependency in the proof spine.
* **`EquiconsistencyEvidenceRole`** — a metaproof establishing equiconsistency or relative strength, often used to **constrain** theory choice.

**Semantics.** In a fixed theory version, these roles are **boolean** and **non‑decaying**. If the axiom base or definitions change, the binding must be re‑issued for the new version; there is no silent carry‑over.

**5.2 Experimental line (empirical, inductive, and model‑selection)**

* **`ObservationEvidenceRole`** — raw or processed observations under a declared method.
* **`MeasurementEvidenceRole`** — calibrated measurements with an error model and traceability.
* **`ModelFitEvidenceRole`** — comparative fit or likelihood of data to competing models; supports one **over** another within the declared scope.
* **`ReplicationEvidenceRole`** — independent replication status (full, partial, failed).
* **`CalibrationEvidenceRole`** — evidence about the measurement chain (instrument validity), typically **constraining** claims.
* **`BenchmarkEvidenceRole`** — standardised tasks or suites producing comparable scores.

**Semantics.** Experimental roles require a **claim-scope** and a **relevance timespan**. Their contribution to confidence is **graded** and may **decay**; the same episteme may carry multiple bindings for different claims or scopes (distinct role assignments).

> **Specialisation, not stacking.** Do not build chains like “transformer‑agent‑observer role.” A system enacts behavioural roles (e.g., `TransformerRole`) to **perform work**; an episteme enacts `U.EvidenceRole` to **classify** its evidential function. Keep enactment lines separate.

