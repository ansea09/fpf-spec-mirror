---
chunk_kind: "child"
pattern_id: "A.2.4"
pattern_title: "U.EvidenceRole"
section_id: "A.2.4:9"
section_title: "Worked examples"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.4/A.2.4__010_worked-examples.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "A.2.4 — U.EvidenceRole"
  - "A.2.4:9 — Worked examples"
line_start: 3190
line_end: 3229
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

### A.2.4:9 - Worked examples

#### A.2.4:9.1 - Formal line — *Proof as evidence for a theorem*

**Role definition (in `GraphTheory`)**
`AxiomaticProofRole`
- `claimRef = Theorem-12` (“Every finite acyclic graph admits a topological ordering”),
- `claimScope = all finite DAG`,
- `polarity = supports` (entails),
- `epistemicMode = formal`, `assuranceUse = VA`,
- fenced to `TheoryVersion = 3.1` (open-ended relevance as long as that version stands).

**Role assignment(s)**
`Lemma-12.proof#AxiomaticProofRole:GraphTheory`

**Provenance sketch**
`verifiedBy → Carrier#Proof_p1` (machine-checked), `usedCarrier → Carrier#Def_graph`.

**Effect on assurance (informative)**
High **F** (machine-checked proof), **G** = “finite DAG”, **R** from proof-obligation integrity; potential CL penalty if an ontology bridge is used.

##### A.2.4:9.2 - Empirical line — *Sensor calibration as evidence for an accuracy claim*

**Role definition (in `Cardio_2026`)**
`ModelFitEvidenceRole`
- `claimRef = “Sensor S achieves ±0.3 °C accuracy in [0,70] °C under lab conditions L”`,
- `claimScope = temperature [0,70] °C; humidity 30–50%; environment L`,
- `polarity = supports`,
- `epistemicMode = postulative`, `assuranceUse = LA`,
- `weightModelRef = KD:SupportMeasure`, `decayPolicy = annual recalibration`.

**Role assignment(s)**
`Trial-R3.csv#ModelFitEvidenceRole:Cardio_2026`

**Provenance sketch**
`validatedBy → Carrier#Dataset_calib_v5`, `protocolRef → MethodDescription#ThermoCalibration`, `fromWorkSet → {cal_run_0502, cal_run_0503}`.

**Effect on assurance (informative)**
**F** from formalised procedure, **G** = measured envelope, **R** from replication and CL on unit mapping; **R** decays after the policy window unless refreshed.

