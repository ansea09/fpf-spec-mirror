---
chunk_kind: "child"
pattern_id: "A.7.CP"
pattern_title: "Constructive-Premise Compact and Reasoning-Basis Use"
section_id: "A.7.CP:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7.CP/A.7.CP__007_archetypal-grounding.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "A.7.CP — Constructive-Premise Compact and Reasoning-Basis Use"
  - "A.7.CP:5 — Archetypal Grounding"
line_start: 22315
line_end: 22324
dependencies:
  - "A.7"
  - "A.7.1"
  - "A.7.2"
keywords:
  - "ClaimUsedAsReasoningBasisRelation@Context"
  - "adopted premise or conditional assumption"
  - "constructive-premise claim"
  - "dated reasoning Work"
  - "exact receiving claim or result"
  - "selective reopen"
---

### A.7.CP:5 - Archetypal Grounding

**Relation-occurrence repair.** Ontology-analysis work splits one support relation into two occurrences after removal and reinstallation and returns `SupportOccurrenceRepairDecision-17`. That result relies on `A7CP-01` and `A7CP-10`, so two reasoning-basis occurrences name the same work and receiving result but different basis claims. The other ten claims stay latent.

**Role/chart reconciliation.** Reconciliation work returns `AssignmentConstitutionDecision-42`, which distinguishes assignment constitution from a chart that evidences the assignment. Four result-specific relation occurrences connect that decision to `A7CP-01`, `A7CP-03`, `A7CP-05`, and `A7CP-06`. Source-use and evidence relations stay under their subject patterns.

**Same-work selective reopen.** `SupportRepairWork-19` returns both `WarrantyClaimRepair-19` and `IncidentAttributionRepair-19`. Each has its own relation occurrence to `A7CP-10`. The warranty result uses that claim as an adopted premise; the incident result uses it as a conditional assumption while a removal timestamp is disputed. Evidence that settles that timestamp changes the posture only on the incident-result edge, so `IncidentAttributionRepair-19` reopens while the unchanged warranty-result edge leaves `WarrantyClaimRepair-19` closed.

**No compact use.** Missing telemetry blocks a state claim while the relevant state and evidence distinctions are already clear. Work returns to measurement/evidence. No compact claim is load-bearing, so no reasoning-basis occurrence is created.

