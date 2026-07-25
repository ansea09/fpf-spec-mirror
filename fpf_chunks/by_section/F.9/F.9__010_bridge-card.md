---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:8"
section_title: "Bridge Card"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__010_bridge-card.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:8 — Bridge Card"
line_start: 89543
line_end: 89567
dependencies:
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.9"
  - "B.3"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "C.29"
  - "E.10.D1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
keywords:
  - "Bridge-supported use"
  - "CL"
  - "bridge"
  - "bridge reading"
  - "cross-context alignment"
  - "direction"
  - "loss notes"
  - "state export"
  - "weakest-link scope"
---

### F.9:8 - Bridge Card

Use this compact record when a Bridge claim matters:

```text
BridgeCard:
  CellA:
  CellB:
  senseFamilyA:
  senseFamilyB:
  BridgeKind:
  Direction:
  CL:
  LossNotes:
  CounterExampleOrInvariantEvidence:
  AdmittedUse:
  NonAdmittedUse:
  DirectGoverningPatternIfNotF9:
  RevisionTrigger:
```

`AdmittedUse` states the strongest use the Bridge permits. `NonAdmittedUse` names the tempting overclaim, such as role assignment, work attribution, structural inference, source authority, or evidence use. `DirectGoverningPatternIfNotF9` points to the pattern that must govern that overclaim before it may become a claim.

`BridgeId` and policy or edition identifiers cited by a Bridge Card are registry references, not semantic symbols exported by signatures. Do not demand them through `SignatureManifest.provides`; validate that referenced registry entries exist and are edition-pinned when required.

