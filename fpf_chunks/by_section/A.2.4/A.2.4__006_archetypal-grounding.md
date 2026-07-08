---
chunk_kind: "child"
pattern_id: "A.2.4"
pattern_title: "Episteme Evidence-Use and Status-Use Relations"
section_id: "A.2.4:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.4/A.2.4__006_archetypal-grounding.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "A.2.4 — Episteme Evidence-Use and Status-Use Relations"
  - "A.2.4:5 — Archetypal Grounding"
line_start: 3668
line_end: 3716
dependencies:
  - "A.10"
  - "A.2"
  - "A.2.1"
  - "A.2.4"
  - "A.6.5"
  - "B.3"
  - "C.2.1"
  - "C.28"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.2"
  - "E.17.EFP"
  - "F.10"
  - "G.6"
  - "U.Role"
  - "U.RoleAssignment"
keywords:
  - "claim"
  - "episteme"
  - "evidence-use"
  - "provenance"
  - "source-use"
  - "status-use"
---

### A.2.4:5 - Archetypal Grounding

#### A.2.4:5.1 - Proof Used as Evidence

`Lemma-12.proof` is an episteme used as evidence for `Theorem-12` in `GraphTheory_v3.1`.

The evidence-use relation names:

* `EvidenceEpistemeSlot = Lemma-12.proof`;
* `EvidenceTargetClaimSlot = Theorem-12`;
* `EvidenceClaimScopeSlot = finite DAGs inside GraphTheory_v3.1`;
* `EvidencePolaritySlot = supports` or an entailment-specific polarity when the local value set declares one;
* `EvidenceRelevanceWindowSlot = theory-version fence GraphTheory_v3.1`;
* `EvidenceAssuranceUseSlot = verification use`;
* `EvidenceProvenanceConstraintSlot = proof publication, proof-check result, dependency list, and theory version`.

No episteme holds `AxiomaticProofRole`. The proof episteme is used in a claim-bound evidence-use relation.

#### A.2.4:5.2 - Calibration Dataset Used as Evidence

`Trial-R3.csv` is an episteme used as evidence for `Sensor S accuracy +/-0.3 C in [0,70] C under lab conditions L`.

The evidence-use relation names the claim scope, polarity, relevance window, weight model, producing work runs, method description, measurement traceability, and freshness policy. If a later assurance claim is made, `B.3` consumes this relation. If the calibration run itself is being discussed, use `A.15.1` for the work occurrence.

#### A.2.4:5.3 - Dashboard Status Cell

A release dashboard shows `Ready`.

That visible cell can be:

* a status cue;
* a status assertion if the source, status value, scope, window, and provenance constraints are recoverable;
* evidence for a gate or release claim only when `A.10` and the gate pattern recover the source relation;
* no evidence-use relation if it is stale, copied, unauthenticated, or disconnected from the decision source.

It is not a status role held by the dashboard episteme.

#### A.2.4:5.4 - Standard Used as Requirement or Evidence

An ISO/IEC/IEEE standard clause can be an episteme used as a requirement source, definition source, status source, or evidence source depending on the current claim.

Do not write "the standard has a normative role" as live FPF ontology. Recover the relation governed by the current claim: standard-use, requirement-use, definition-use, source-use, evidence-use, status-use, or assurance-use.

#### A.2.4:5.5 - Simulation-Only Counterfactual Output

A simulation output mentions a counterfactual. That output may be an episteme used in an evidence-use relation. The causal-use class still belongs to `C.28`.

If the current `C.28` value is `simulationOnlyCounterfactualOutputBasis`, the evidence-use relation cannot be relabelled as `realizedCounterfactualSampleSupportBasis` or `interventionalActionSupportBasis` by evidence wording, validation wording, or role wording alone.

