---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism - Law-governed application to a SubjectKind over a RangedValueKind"
section_id: "A.6.1:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__013_relations.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "A.6.1 — U.Mechanism - Law-governed application to a SubjectKind over a RangedValueKind"
  - "A.6.1:12 — Relations"
line_start: 10813
line_end: 10840
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.19"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.6.0"
  - "B.3"
  - "C.16"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.D1"
  - "E.18"
  - "E.20"
  - "F.18"
  - "U.BoundedContext"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Signature"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "AdmissibilityConditions"
  - "Bridge‑only"
  - "LawSet"
  - "Mechanism"
  - "OperationAlgebra"
  - "Transport"
---

### A.6.1:12 - Relations

* **Builds on:** `A.6.0 U.Signature`; `A.1.1 U.BoundedContext`; SlotSpec and argument-discipline patterns; Bridge and ReferencePlane patterns.
* **Coordinates with:** `A.3.1 U.Method`; `A.3.2 U.MethodDescription`; `A.15.2 U.WorkPlan`; `A.15.1 U.Work`; `A.19`; `C.16`; `C.29`; `A.10`; `B.3`; `A.20`; `A.21`; `E.18`; `E.20`.
* **Separates from:** direct method choice, implementation recipe, telemetry publication, evidence record, gate decision, result certification, and realization work.
* **Uses for precision restoration:** `E.10`, `E.10.ARCH`, and `F.18`; use `E.10.ARCH:3.1` when source labels such as `algorithm`, `program`, `workflow`, `process`, `procedure`, `recipe`, `solver`, or `control strategy` hide the current relation position.

#### A.6.1:12.1 - P2W mechanism-use relation

When `E.18.1` reaches a mechanism cue, A.6.1 carries the mechanism meaning: operation algebra, LawSet, AdmissibilityConditions, realization relation when declared, transport, and mechanism descriptions. P2W may name the cue and governing pattern, but it does not define these mechanism relations locally.

If the issue under repair is new mechanism introduction, mechanism stabilization, or method-related mechanism use, use `E.20` when mechanism-governing-definition assignment is current. A P2W citation of a mechanism does not select a method, execute work, pass a gate, prove evidence, or certify a result.

#### A.6.1:12.2 - Lowering, repair, and refresh conditions

A `U.Mechanism` remains usable while its MechanismDeclaration, imported signatures, SlotSpecs, LawSet, AdmissibilityConditions, Applicability, Transport, GammaTimePolicy, PlaneRegime, and Audit relations remain recoverable and monotone with respect to A.6.0.

Repair the mechanism, or define a new mechanism when monotone repair is impossible, if any of these conditions holds:

* an inherited SlotKind is renamed, widened, or given a new required argument;
* a realization relaxes a law, bypasses an admissibility predicate, or depends on hidden structure inside an imported signature;
* a cross-context or cross-plane reuse claim lacks BridgeId, ReferencePlane, loss policy, or Reliability penalty relation;
* a numeric comparison or aggregation is no longer compliant with the governing characteristic-space, measurement, scale, or comparison patterns;
* a GammaTimePolicy, applicability window, or implicit latest assumption changes an admissibility result;
* a current SoTA change in effect systems, protocol types, typed semantic translation, policy-as-code, calibrated uncertainty, or context normalization changes the operation algebra, guard discipline, morphism relation, or transport boundary.

Do not repair the mechanism merely because one work occurrence, telemetry publication, evidence record, gate decision, method choice, or realization version changed. Repair the object governed by that neighboring relation unless the change alters the MechanismDeclaration, its imported signature relation, or the monotone relation between a realization and the MechanismDeclaration.

