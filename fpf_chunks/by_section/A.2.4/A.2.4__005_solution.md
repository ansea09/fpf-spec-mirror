---
chunk_kind: "child"
pattern_id: "A.2.4"
pattern_title: "Episteme Evidence-Use and Status-Use Relations"
section_id: "A.2.4:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.4/A.2.4__005_solution.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "A.2.4 — Episteme Evidence-Use and Status-Use Relations"
  - "A.2.4:4 — Solution"
line_start: 3741
line_end: 3874
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

### A.2.4:4 - Solution

Do not create or use `U.EvidenceRole` as a durable role kind. Do not place an episteme in `U.RoleAssignment` merely because it is used as evidence, source, standard, requirement, definition, explanation, publication, status bearer, or assurance input.

Use direct relation patterns instead:

| Current claim | Use |
| --- | --- |
| one episteme is used as evidence for one claim, effect, or bounded reliance use | `A.10`, with the A.2.4 evidence-use SlotKinds below |
| evidence use contributes to assurance, trust, readiness, compliance, safety, release confidence, `F`, `G`, `R`, or `CL` | `B.3`, consuming A.10 evidence-use relations |
| the episteme itself is being identified, versioned, or distinguished from publication faces and publication carriers | `C.2.1` |
| the use is causal, counterfactual, intervention-facing, or simulation-only | `C.28`, with A.10 evidence-provenance graph relation and the A.2.4 evidence-use relation as input |
| the source says "status", "approved", "current", "valid", "stale", "ready", or another status-like value | `F.10`, A.10, B.3, a gate pattern, or a direct status pattern |
| the source is a publication face, view, description, source citation, standard, requirement, explanation, or specification-use case | `E.17`, `E.17.0`, `E.17.2`, `E.17.EFP`, `E.10.D2`, or the direct source-use pattern |
| a system, person, team, organization, or acting holon holds a role and performs or prepares work | `A.2`, `A.2.1`, `A.15`, `A.15.1`, or `A.15.2` |

#### A.2.4:4.1 - Evidence-Use Relation Slots

An evidence-use relation is a relation around an episteme and a claim or effect. It is not a role assignment.

| SlotKind | ValueKind | Identity and currentness discipline |
| --- | --- | --- |
| `EvidenceEpistemeSlot` | `U.Episteme` used as evidence | Identity slot for the evidence-use relation. |
| `EvidenceTargetClaimSlot` | claim or theory statement | Identity slot whenever the relation is claim-bound; a missing value blocks claim-bound evidence use. |
| `EvidenceClaimGroundingHolonSlot` | `U.Holon` grounding the target claim, mirroring C.2.1 `GroundingHolonSlot` | Identity or currentness-required when changing the grounding holon changes the evidence relation or the claim being evidenced. |
| `EvidenceClaimScopeSlot` | claim-scope value governed by `B.3`, `A.10`, `C.28`, or a direct evidence pattern | Identity qualifier when changing scope changes the relation; currentness-required when scope changes admissible use. |
| `EvidencePolaritySlot` | evidential polarity value such as supports, refutes, constrains, or neutral when that value set is current | Identity qualifier when changing polarity changes which evidence-use relation is asserted. |
| `EvidenceRelevanceWindowSlot` | temporal relevance window, theory-version fence, freshness policy, or decay policy | Identity or currentness-required when time, version, or freshness changes the evidence use; consideration slot for formal uses where the theory-version fence already carries the boundary. |
| `EvidenceAssuranceUseSlot` | typing, verification, validation, reliance, gate, release, or another assurance-use value governed by `B.3`, `A.10`, or a direct pattern | Identity qualifier only when changing assurance use changes the relation; currentness-required for reliance-bearing use. |
| `EvidenceWeightModelSlot` | weight, confidence, reliability, likelihood, or scoring model reference | Consideration slot; currentness-required when weighted evidence is claimed. |
| `EvidenceProvenanceConstraintSlot` | provenance constraints over external work, source, publication, method description, proof check, measurement, publication carrier, or evidence-provenance graph relation | Currentness-required when provenance decides admissible use or a rival explanation. |

These SlotKinds are evidence-use relation positions. They are not work-role qualifier slots, not `U.Role` names, and not new U-kinds by themselves.

#### A.2.4:4.2 - Status-Use Relation Slots

A status-use relation is a relation around a bearer, status value, scope, window, source, and use. It is not a status role held by an episteme.

| SlotKind | ValueKind | Use |
| --- | --- | --- |
| `StatusBearerSlot` | episteme, claim, method description, publication, role assignment, work occurrence, clause, gate record, or another governed bearer admitted by the direct pattern | The value whose status is being asserted or read. |
| `StatusTargetSlot` | claim, method, episteme, publication, work result, clause, bearer, or another governed status target | Required when the status is not simply about the bearer itself. |
| `StatusScopeSlot` | bounded-context scope, claim scope, admission scope, requirement scope, or use scope | Currentness-required when scope changes the status assertion. |
| `StatusValueSlot` | status value governed by `F.10` or a direct pattern | Required for a status assertion. |
| `StatusWindowSlot` | temporal validity window, freshness policy, status-currentness relation, or source-currentness relation | Currentness-required for time-sensitive status. |
| `StatusUseSlot` | gate use, assurance use, admission use, source-currentness use, work-plan readiness use, or another direct use | Required when the status is consumed for that use. |
| `StatusProvenanceConstraintSlot` | source order, authority source, publication, proof, verification, register, or provenance constraint | Currentness-required when provenance decides status use. |

These names do not create a generic status ontic. They are repair vocabulary for status-use relations in the current role and relation-slot settlement. Durable status families remain governed by `F.10` or a direct status pattern.

#### A.2.4:4.3 - Minimal Evidence-Use Statement

For ordinary use, write only the fields needed for the current reliance question:

```text
Episteme evidence-use statement:
  EvidenceEpisteme:
  BoundedContext:
  EvidenceTargetClaim:
  EvidenceClaimGroundingHolon:
  EvidenceClaimScope:
  EvidencePolarity:
  EvidenceRelevanceWindow:
  EvidenceAssuranceUse:
  EvidenceWeightModel:
  EvidenceProvenanceConstraint:
  DirectGoverningPattern:
  UnsupportedOverread:
```

`UnsupportedOverread` names the stronger claim not carried by this relation, such as approval, permission, gate passage, performed work, assurance, causal identification, release confidence, or global truth.

#### A.2.4:4.4 - Minimal Status-Use Statement

For status-like cases, write the smallest relation that keeps status from becoming role assignment, gate passage, or assurance by display alone:

```text
Episteme status-use statement:
  StatusBearer:
  StatusTarget:
  StatusScope:
  StatusValue:
  StatusWindow:
  StatusUse:
  StatusProvenanceConstraint:
  DirectGoverningPattern:
  UnsupportedOverread:
```

If the status is used for a gate, release, work-plan readiness, assurance, or admission decision, apply the direct governing pattern for that use. A.2.4 only keeps the status-use relation typed and prevents role-holder grammar from returning where an episteme-use relation is needed.

#### A.2.4:4.5 - Formal, Empirical, and Causal Evidence Uses

Source labels such as `AxiomaticProofRole`, `ObservationEvidenceRole`, `MeasurementEvidenceRole`, `ModelFitEvidenceRole`, `ReplicationEvidenceRole`, `CalibrationEvidenceRole`, and `BenchmarkEvidenceRole` become evidence-use classifications or local evidence-use labels, not `U.Role` values.

Formal line:

* the evidence episteme is a proof, derivation, counterexample, theory note, proof-check result, or formal publication;
* `EvidenceTargetClaimSlot` names the theorem or theory statement;
* `EvidenceClaimScopeSlot` names the theory domain or declared scope;
* `EvidenceRelevanceWindowSlot` usually names a theory-version fence rather than an empirical expiry date;
* `EvidenceProvenanceConstraintSlot` names proof checks, source publications, theory version, and dependency conditions when current.

Empirical line:

* the evidence episteme is a dataset, observation record, measurement report, replication report, calibration result, benchmark result, model-fit report, or similar episteme;
* `EvidenceClaimScopeSlot`, `EvidenceRelevanceWindowSlot`, `EvidenceWeightModelSlot`, and `EvidenceProvenanceConstraintSlot` usually decide whether the use is admissible;
* the producing work remains `U.Work` under `A.15.1`, performed by a system or acting holon under `U.RoleAssignment` where that trace is current.

Causal-use line:

* the causal-use question belongs to `C.28`;
* A.2.4 keeps the evidence-use relation typed so the episteme is not relabelled by vocabulary alone;
* exact `C.28` values such as `observationalAssociationSupportBasis`, `interventionalActionSupportBasis`, `realizedCounterfactualSampleSupportBasis`, `identifiedCounterfactualEstimateSupportBasis`, and `simulationOnlyCounterfactualOutputBasis` remain `C.28` values, not role names.

#### A.2.4:4.6 - Work, Source, and Publication Boundary

The producing work and the later evidence use are different relations.

* A lab run, proof-checking session, calibration run, benchmark run, review, model evaluation, or data extraction can be `U.Work`.
* The report, proof file, dataset, benchmark table, or publication produced by that work can be a `U.Episteme`.
* A later project can use that episteme as evidence through an evidence-use relation.
* A publication face, view, source citation, credential view, dashboard display, or generated explanation can cue evidence or status use, but it does not become the evidence-use relation by itself.

When the source-currentness, publication-use, view, explanation, or specification-use question is current, use `E.17`, `E.17.0`, `E.17.2`, `E.17.EFP`, `E.10.D2`, `A.10`, or the direct source-use pattern before relying on the evidence-use or status-use relation.

#### A.2.4:4.7 - Shortcut Cost and Reopen Condition

The baseline is the direct governing pattern: full `A.10` for evidence-provenance graph relations, full `B.3` for assurance, full `C.28` for causal use, full `F.10` for status families, full `E.17` or `E.10.D2` for publication-use and description-use cases, and full `A.15.1` when the producing work is current.

A.2.4 is the weaker first-use representation. It saves effort by writing only the relation positions needed to stop role-like source wording from collapsing evidence, status, work, assurance, source, and publication claims. The loss budget is narrow: A.2.4 may name the evidence-use or status-use relation, preserve the named direct governing pattern, and state unsupported overread. It may not decide assurance value, gate passage, causal identification, source-currentness order, publication interpretation, or performed-work truth.

Open the direct governing pattern when the attempted use depends on assurance, safety, release, compliance, causal effect, gate decision, permission, performed work, source freshness, publication use, status currentness, or a contested provenance relation.

