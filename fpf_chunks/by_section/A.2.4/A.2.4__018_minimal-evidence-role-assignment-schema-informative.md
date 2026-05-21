---
chunk_kind: "child"
pattern_id: "A.2.4"
pattern_title: "U.EvidenceRole"
section_id: "A.2.4:17"
section_title: "Minimal evidence-role assignment schema (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.4/A.2.4__018_minimal-evidence-role-assignment-schema-informative.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "A.2.4 — U.EvidenceRole"
  - "A.2.4:17 — Minimal evidence-role assignment schema (informative)"
line_start: 3359
line_end: 3372
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

### A.2.4:17 - Minimal evidence-role assignment schema (informative)

```yaml
EvidenceRoleAssigning:
  id: ERB-…
  context: <BoundedContextId>
  holder: <EpistemeId>                # paper/proof/dataset/report
  role: <EvidenceRoleId>              # defined within the context, with normative properties
  timespan?: {from: ISO-8601, to: ISO-8601|null} # optional assignment window
  provenance:
    formal?: { theoryRef: <TheoryId>, proofArtifactRef: <CarrierId>, checkedBy?: <ProofCheckId> }
    empirical?: { protocolRef: <MethodDescriptionId>, fromWorkSet: [<WorkId>… ], dataCarrierRef?: <CarrierId> }
```

