---
chunk_kind: "child"
pattern_id: "B.2.2"
pattern_title: "Meta-System Transition - System Specialization of MHT"
section_id: "B.2.2:5"
section_title: "Archetypal Grounding (Worked Cases)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.2/B.2.2__007_archetypal-grounding-worked-cases.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "B.2.2 — Meta-System Transition - System Specialization of MHT"
  - "B.2.2:5 — Archetypal Grounding (Worked Cases)"
line_start: 32965
line_end: 32994
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.19"
  - "A.2.1"
  - "A.2.2"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "B.1.2"
  - "B.2"
  - "B.2.5"
  - "B.3"
  - "B.3.5"
  - "C.13"
  - "C.16"
  - "C.30"
  - "C.30.ASV"
  - "C.30.TFS-REL"
keywords:
---

### B.2.2:5 - Archetypal Grounding (Worked Cases)

#### B.2.2:5.1 - Search-And-Rescue Swarm

Before MHT, the project has individual drones with local navigation and maintenance records. After MHT, the current object may be one search-and-rescue swarm if the result whole has its own mission objective, coordination relation, external command relation, capability envelope, and swarm-level risks.

```text
SystemMHTSlice@Rescue:
  existingWholeRef: drone fleet as managed aggregate
  mhtResultSystemRef: search-and-rescue swarm
  resultDelimitationRelationRef: command-and-operating-area delimitation
  supervisionOrCoordinationRelationRef: formation and coverage coordination
  capabilityEnvelopeRef: area-search coverage under wind and battery conditions
  evidenceOrAssuranceRefs: swarm-level test evidence, not only drone certificates
```

The old drone evidence remains relevant, but it is not enough for the swarm-level assurance claim.

#### B.2.2:5.2 - Cloud Platform

Independent services become a platform only if the current claim concerns a result system: a shared control plane, system-level SLO, deployment and rollback coordination, platform-level evidence, and external commitments.

If the only change is a better dashboard or one more service, use architecture-description, publication, measurement, or component owners. Use B.2.2 only when `mhtResultSystemRef` is the operating platform itself.

#### B.2.2:5.3 - Production Cell

A machine, robot, fixture, workpiece carrier, and inspection station can become a production cell when the cell has its own delimitation, objective, coordination, transformation structure, work occurrence evidence, and capability envelope.

The fixture being manufactured is not part of the machine merely because the machine changes it. The production cell claim needs a result system; the manufacturing relation remains transformation and work.

