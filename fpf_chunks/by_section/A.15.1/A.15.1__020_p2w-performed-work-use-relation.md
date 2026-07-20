---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:15a"
section_title: "P2W Performed-Work Use Relation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__020_p2w-performed-work-use-relation.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:15a — P2W Performed-Work Use Relation"
line_start: 24133
line_end: 24138
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.6"
  - "A.2.8.PER"
  - "A.3.1"
  - "A.3.2"
  - "B.1"
  - "B.1.6"
  - "B.3"
  - "C.2.1"
  - "C.27.TA"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "U.Capability"
  - "U.Method"
  - "U.MethodDescription"
  - "U.ReferenceScheme"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.System"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "EpisodeOf_work"
  - "TemporalPartOf_work"
  - "actuals"
  - "concurrent work part"
  - "operational work part"
  - "performed enactment"
  - "trace"
  - "work occurrence"
---

### A.15.1:15a - P2W Performed-Work Use Relation

When `E.18.1` reaches performed work, identify the dated `U.Work`: performer assignment, enacted method, concrete bindings, used resources, temporal extent, affected referent, and containing system. Carry actual change, production, evaluation-result, evidence, delivery, acceptance, transfer, or receiving-use claims as separately governed continuation objects.

A `U.Work` occurrence may be designated by an episteme that also cites a `U.WorkPlan`, exact planned-filling claim, or prior `WorkEntryReadiness@Context` as a baseline. That episteme may state launch values, performed values, substitutions, variance, and telemetry, but each plan, comparison, transfer, evidence, assurance, gate, readiness, production, evaluation, delivery, or acceptance claim retains its direct governor.

