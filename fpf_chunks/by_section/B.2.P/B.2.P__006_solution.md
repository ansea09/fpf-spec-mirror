---
chunk_kind: "child"
pattern_id: "B.2.P"
pattern_title: "Emergence and MHT Precision Restoration"
section_id: "B.2.P:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.P/B.2.P__006_solution.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "B.2.P — Emergence and MHT Precision Restoration"
  - "B.2.P:4 — Solution"
line_start: 35660
line_end: 35752
dependencies:
  - "A.10"
  - "A.14"
  - "A.2.2"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "B.2"
  - "B.2.2"
  - "B.2.3"
  - "B.2.4"
  - "B.3.5"
  - "C.13"
  - "C.16"
  - "C.2.1"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.TFS-REL"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "E.24"
  - "F.18"
keywords:
---

### B.2.P:4 - Solution

Recover the claim kind and direct owner before any wording replacement.

#### B.2.P:4.1 - Emergence Claim-Kind Recovery

Use this recovery note:

```text
EmergenceClaimKindRecovery@Context:
  sourceExpression:
  projectConcern:
  candidateEntityOfConcernRef:
  sourceUseDisposition:
  recoveredClaimKind:
  recoveredDirectOwnerPattern:
  candidateWholeReidentificationRef?
  candidateResultHolonKindRef?
  characteristicOrCapabilityRef?
  functionOrFunctioningRef?
  architectureOrStructureRef?
  mathematicalLensUseRef?
  evidenceOrMeasurementRef?
  collectionAdmissionRef?
  publicationOrSourceUseRef?
  blockedOverreads:
  replacementWordingOrStop:
```

The recovery note is not a U-kind and not a durable project object by itself. It is a local precision-restoration record.

#### B.2.P:4.2 - Claim-Kind Recovery and Owner Selection Table

| Recovered claim kind | Use this owner | Do not overread as |
| --- | --- | --- |
| Whole reidentification of a holon | `B.2`, then `B.2.2`, `B.2.3`, `B.2.4`, or another admitted result-kind owner when current | generic emergence, metric gain, or title mnemonic |
| System-result MHT | `B.2.2` | all emergence cases or all system aggregation |
| Episteme-result MHT | `B.2.3` plus `C.2.1` and episteme family | episteme agency, publication authority, or EFEM by title |
| Capability or functioning evidence that creates or reveals whole reidentification | `B.2.4` under B.2 | generic capability, generic function, or all functioning |
| Ordinary capability claim | `A.2.2` and `C.16` | MHT |
| Function or functioning claim | `A.6.F`, `A.3.4`, `C.30.TFS-REL`, `C.16`, or direct owner named by value | `U.Emergence` or MHT by wording |
| Whole-level characteristic or threshold | `C.16`, `A.19`, `A.13`, evidence owners | new whole by metric alone |
| Architecture-induced property or residual | `C.30`, `A.22`, `C.30.ASV`, `C.30.TFS-REL`, `C.30.ILC`, and `C.29` when mathematical lens is current | MHT unless B.2 reidentification is recovered |
| Mathematical emergence, scale, coarse-graining, graph, morphism, benchmark, or MSPD expression | `C.29` plus the direct subject owner | ontology by mathematical spelling |
| Metric or benchmark mirage | `C.16`, `A.10`, `C.29`, source-use, and evaluation owners | MHT or system admission |
| Collection or collective wording mixed with emergence, MHT, or synergy | First recover membership, collection-as-whole, acting collective, whole-level characteristic, or MHT | collection admission by B.2.P |
| Publication, model, dashboard, theory-text, or report claim | `C.2.1`, `E.17`, `C.30.AD`, `E.17.*`, source-use, or episteme owners | in-life whole by description alone |

#### B.2.P:4.3 - Whole-Reidentification Recovery

When whole reidentification remains possible after the claim-kind recovery, recover the B.2 slot relation:

```text
B2WholeReidentificationRecovery@Context:
  existingWholeRef:
  boundedContextRef:
  candidateResultHolonKindRef:
  candidateResultRef:
  mhtTriggerProfileRef:
  existingWholeExplanationCheckRef:
  changedContentOwnerRefs:
  evidenceOrSourceRelationRefs:
  mathematicalLensUseRefs?
  blockedOverreads:
```

Then return to B.2. B.2.P does not declare MHT.

#### B.2.P:4.4 - Collection Boundary

Collection words enter B.2.P only when they are entangled with emergence, synergy, MHT, metric mirage, or whole-reidentification wording.

If the claim is plain collection admission:

- use `A.14` for membership and part-whole relation vocabulary;
- use `C.13` for collection-as-whole constructional grounding;
- use `B.3.5` for working-model assurance grounding;
- use `A.1` with `A.15` and A.2 patterns for an acting collective admitted as `U.System`;
- use `C.16` for a whole-level characteristic.

B.2.P may record that these are the direct owners; it does not own them.

#### B.2.P:4.5 - Source Mnemonics and Result Fields

Treat source labels and short forms as recognition cues until their governed object is recovered.

- `MET` may point to an episteme-result MHT, source-title wording, episteme morphing, publication synthesis, or source-only phrase. Recover before use.
- `MFT` may point to capability and functioning whole reidentification, a functional-structure view, function-like wording, method and work collapse, or source-only phrase. Recover before use.
- `promotion` may hide whole reidentification, status change, release, gate, publication, or project process wording. Recover before use.
- `post*` fields should become `mhtResult*Ref` only when B.2 record fields are current.

Do not keep the source label as the pattern owner merely because it is recognizable.

