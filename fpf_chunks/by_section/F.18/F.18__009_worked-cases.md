---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local-First Unification Naming Protocol"
section_id: "F.18:7"
section_title: "Worked Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__009_worked-cases.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "F.18 — Local-First Unification Naming Protocol"
  - "F.18:7 — Worked Cases"
line_start: 78019
line_end: 78127
dependencies:
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "A.6.RSIR"
  - "C.2.P"
  - "E.10"
  - "F.0.1"
  - "F.1"
  - "F.1-F.17"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.8"
  - "F.9"
  - "G.10"
  - "G.2"
  - "G.6"
keywords:
---

### F.18:7 - Worked Cases

#### F.18:7.1 - Role, Holder, Capability, Method, And Work

A shipyard team wants one public name for "shipbuilder".

Recovered values:

- `ShipbuilderRole` in `ShipyardProductionContext`;
- holder assignment for a named worker or team under `A.2.1`;
- `ShipbuildingCapability` with envelope and measures under capability patterns;
- `ShipbuildingMethod` or method family under `A.3.1` and `A.3.2`;
- `HullAssemblyWork` under work patterns.

F.18 settlement:

```text
NameCard:
  GovernedValueRef: ShipbuilderRole@ShipyardProductionContext
  GoverningPatternRef: A.2
  TechLabel: ShipbuilderRole
  PlainLabel: shipbuilder role
  RejectedCandidates: ShipbuilderCapability; HullAssemblyWorker; CertifiedShipbuilder
  SelectionRationale: selected label names the role value without claiming capability, holder assignment, or performed work
```

The rejected candidates are not "worse synonyms." They name different governed values.

#### F.18:7.2 - Engineer-Roboticist and Musician

A lab says: "Vasya is an engineer, does robot engineering, is therefore an engineer-roboticist. These are musical robots, and Vasya is also a musician, performs music, and teaches robots music."

Recovered values:

- Vasya as holder in `MusicalRobotLab_2026`;
- engineering role value or local engineering-role expression;
- robotics as domain, practice, method-family, or work-field qualification of the engineering role expression;
- `MusicianRole` as an independent role value when music performance matters separately;
- robot-engineering method or work, music-performance work, and robot-music-teaching method or work under method and work patterns;
- optional role-algebra, graph, matrix, embedding, or neural representation only if the project actually uses such a lens to describe the role relation structure.

F.18 settlement:

```text
NameCard:
  GovernedValueRef: robotics-qualified engineering role expression in MusicalRobotLab_2026
  GoverningPatternRef: A.2.7 plus A.2 and F.4 when a durable role value is declared
  TechLabel: RoboticsEngineerRole only if durable Tech disambiguation is needed
  PlainLabel: engineer-roboticist or robotics engineer
  RejectedCandidates: engineer and roboticist; engineer-roboticist-musician; RobotEngineeringMethod
  SelectionRationale: selected ordinary label keeps robotics as a qualification of engineering, leaves musician as a separate role assignment, and does not turn method names or work names into role names
```

If the current sentence is for ordinary project communication, "Vasya is our engineer-roboticist and musician" is admissible. If the current record is a method record, name `RobotEngineeringMethod` or the relevant method family under `A.3.1`/`A.3.2`. If the current record is performed work, name the work occurrence under `A.15.1`. Do not make one compressed label carry all of these values.

#### F.18:7.2a - Method Relation Structure and Method Algebra Name

A lab says: "Use the robot-engineering method algebra: choose scouting, then calibration, then training; fall back to teleoperation if training fails."

Recovered values:

- one or more robot-engineering methods or method families under `A.3.1`;
- a method-family registry or selector outcome under `G.5` when the family registry or selector result is current;
- `MethodRelationStructure@MusicalRobotLab_2026` when the current claim is serial composition, guarded fallback, or family selection among methods;
- a method description when the source notation describes that structure;
- a `C.29` mathematical-lens use when "algebra" is the selected representation for checking composition, fallback, or preserved/lost structure;
- work plan or dated work only when a concrete plan or occurrence is current.

F.18 settlement: `RobotEngineeringMethod` names a method or method family only when that is the governed value. `RobotEngineeringMethodRelationStructure` may be a Tech-register name for the selected method relation structure when durable naming is needed. `RobotEngineeringMethodAlgebra` names the lens only when the algebraic representation itself is the governed value. Do not use a role label such as `RoboticsEngineerRole` to name the method relation structure, and do not use "method algebra" to hide a work plan or performed work.

#### F.18:7.3 - Evidence-Like Source Phrase

A review table contains the phrase "model card evidence role".

Recovered values:

- a model-card episteme;
- an evidence-use relation to a target claim;
- possible source-currentness and assurance-use relations;
- no work-facing role unless an acting system is assigned one.

F.18 settlement: no durable role name is minted. If a public term is needed, name the relation, for example `ModelCardEvidenceUse`, with `A.10` as governing pattern and `F.17` publication only when the term row is current.

#### F.18:7.4 - Interface-Like Source Phrase

A software team says "the payment interface owns customer identity".

Recovered candidates:

- module interface under `A.6.M`;
- API description or protocol under `A.6.C`;
- signature or SlotSpecs under `A.6.0` and `A.6.5`;
- publication or description interface under `E.17`;
- responsible role assignment under `A.2.1`.

F.18 settlement: do not mint `PaymentInterfaceRole`. First recover which governed value the phrase names. Then name that value through its governing pattern.

#### F.18:7.5 - Cross-Context Name

Two teams use `component`, `module`, and `unit` for nearby meanings.

Recovered values:

- structural component under architecture and part-whole patterns;
- deployable module under module-interface patterns;
- management unit under organizational patterns.

F.18 settlement: choose a Tech label only for the governed value in its bounded context. Use `F.9` bridges for cross-context comparison. Use `F.17` only if a public term row is needed.

