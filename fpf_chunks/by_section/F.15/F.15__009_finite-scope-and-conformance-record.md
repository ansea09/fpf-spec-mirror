---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "Static and Regression Conformance Harness for Unification"
section_id: "F.15:7"
section_title: "Finite scope and conformance record"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__009_finite-scope-and-conformance-record.md"
commit_sha: "5801dc610c657ac7b1efee349b18e80ce6d7df6f"
heading_path:
  - "F.15 — Static and Regression Conformance Harness for Unification"
  - "F.15:7 — Finite scope and conformance record"
line_start: 94364
line_end: 94409
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.6"
  - "A.2.7"
  - "A.22"
  - "A.6.1"
  - "A.6.5"
  - "B.3"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.24.PUB"
  - "F.1-F.14"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.6"
  - "F.8"
  - "F.9"
  - "G.11"
keywords:
  - "SenseCell testing"
  - "acceptance tests"
  - "regression tests"
  - "static checks"
  - "validation"
---

### F.15:7 - Finite scope and conformance record

Declare the finite scope before applying a rule:

```text
FiniteHarnessScope:
  ScopeDesignator:
  ReceivingUse:
  EffectiveReferenceSchemeValues[]:
  ExactCurrentObjectOrOccurrenceRefs[]:
  ExactDescriptionOrRecordRefs[]:
  ExactVersionRefs[]:
  PriorLaterPairs[]?:
  SelectedStructureRefs[]?:
  SelectedStructureDescriptionRefs[]?:
  TriggeredRuleRefs[]:
  ExcludedClaimsAndNearestNonUses[]:
```

`SelectedStructureRefs` is empty unless an independently selected A.1.1/A.22 structure changes interpretation for the receiving use. A Structure description never replaces the Structure, its obtaining membership relations, or another scope member.

Use an optional record only to package already identified neighbors:

```text
UnificationConformanceRecord:
  EntityOfConcern: exact checked slice/version selected by FiniteHarnessScope
  EffectiveReferenceScheme: scheme interpreting this record's ClaimGraph
  ClaimGraph: exact claims designated by the fields below
  FiniteHarnessScopeRef:
  CheckApplicationRefs[]?:
  AssessmentWorkRefs[]?:
  ResultClaimRefs[]:
  WitnessRefs[]?:
  EvidenceProvenancePathRefs[]?:
  BridgeOccurrenceRefs[]?:
  BridgeDescriptionOrCardRefs[]?:
  PublicationOccurrenceRefs[]?:
  PublicationFormRefs[]?:
  PresentationCarrierRefs[]?:
  CurrentnessRelationRefs[]?:
  NonAdmittedUses[]:
  ReopenTrigger:
```

The checked scope, rule declaration, ordinary checking action or admitted dated assessment Work, exact application, result claim, witness, A.10 evidence-provenance path, conformance-record episteme, E.24.PUB occurrence, publication form, carrier, and G.11 currentness relation remain distinct. A result ref is included only after its C.2.1 claim exists. The optional record may cite an already admitted Work ref; it does not restate the Work's performer, Method, assignment, time, or containing System. Publication and currentness refs are neighbouring claims, not record identity shortcuts.

