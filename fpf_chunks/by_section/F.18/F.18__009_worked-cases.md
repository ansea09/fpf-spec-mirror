---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local-First Unification Naming Protocol"
section_id: "F.18:7"
section_title: "Worked Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__009_worked-cases.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "F.18 — Local-First Unification Naming Protocol"
  - "F.18:7 — Worked Cases"
line_start: 95688
line_end: 95827
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.6.RSIR"
  - "B.3"
  - "C.2.1"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.PUB"
  - "F.0.1"
  - "F.1"
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

A shipyard team wants one reusable name for the role used in shipbuilding work. It first separates the values that the source word "shipbuilder" could hide.

Recovered values:

- `ShipbuilderRole`, interpreted through the role-taxonomy episteme `ShipyardProductionRoles-2026` under `Shipyard-Production-Scheme`;
- one holder-assignment occurrence under `A.2.1`, with its holder system, role value, taxonomy episteme, and scheme as participants and its known assignment interval stated separately;
- `ShipbuildingCapability` with envelope and measures under capability patterns;
- `ShipbuildingMethod` or method family under `A.3.1`; if a separately identified `ShipbuildingMethodDescription : U.MethodDescription` episteme is current, name it separately under `A.3.2` only when its exact `EntityOfConcern` is that Method;
- `HullAssemblyWork` under work patterns.

Here `HullAssemblyWork` is a work-family label or a label in a plan or assignment episteme. A designator such as `HullAssemblyWork-42@2026-07-15T09:10/11:35` names performed work only when the current record recovers its obtaining performer assignment, enacted method, temporal extent, containing system, affected hull referent, material bindings and resource-use facts, plus an applicable continuity policy when disambiguation is current. A changed hull state, measurement result, evaluation verdict, delivery occurrence, or acceptance verdict remains a separately governed and separately named value.

F.18 settlement: no separately recoverable F.17 coordinate is current for this local-only case, so the card states one direct `LocalSenseRef` using the expression `shipbuilder role`; the other candidates remain comparison alternatives, not extra sense coordinates.

```text
NameCard:
  NameCardId: NameCard.ShipbuilderRole.ShipyardProduction.2026
  GovernedValueRef: ShipbuilderRole
  GovernedValueKindRef: U.Role
  GoverningPatternRef: A.2
  ReferenceScheme: Shipyard-Production-Scheme
  ClaimContent: NameCard.ShipbuilderRole.ShipyardProduction.2026.ClaimGraph — complete C.2.1 U.ClaimGraph constituted by all identity-bearing naming-settlement claims designated below
  LocalSenseRef: local expression `shipbuilder role`; sense claim: the ShipbuilderRole value interpreted under Shipyard-Production-Scheme
  LocalSenseBasisRelationRef: absent; no independently admitted local-sense basis relation is current for this case
  TechLabel: ShipbuilderRole
  PlainLabel: shipbuilder role
  CandidateSet: ShipbuilderRole; ShipbuildingCapability; HullAssemblyWorker; CertifiedShipbuilder
  CandidateCoverage: role head; capability head; holder-or-work head; certification-or-status head; no plausible live head family remains untested
  RejectedCandidates: ShipbuildingCapability; HullAssemblyWorker; CertifiedShipbuilder
  SelectionRationale: selected label names the role value without claiming capability, holder assignment, performed work, or certification
  BridgeRefs: absent; this local settlement makes no semantic-correspondence claim
  PublicRowStatus: localOnly; change to pending only if public or cross-context reuse opens and section 4.4 does not yet pass
  UnifiedTermRowRef: absent
  LineageEntries: initial durable settlement; source word "shipbuilder" split from capability, holder-or-worker, performed-work, and certification readings
  RefreshCondition: reopen if A.2 changes the role value, the taxonomy episteme or scheme edition changes its local sense, or repeated readers infer capability, assignment, work, or certification
```

The four candidates execute the section 4.3 stopping rule: each live head family is represented, and the already recovered method and work objects are not plausible alternative labels for this role value. The rejected candidates are not "worse synonyms." They name different governed values or add conditions not carried by this role value. If public, Core-facing, durable-across-context, or cross-context reuse becomes current, apply the section 4.4 gate. Until it passes, keep this card local and do not imply a row or publication occurrence.

#### F.18:7.2 - Engineer-Roboticist and Musician

A lab says: "Vasya is an engineer, does robot engineering, is therefore an engineer-roboticist. These are musical robots, and Vasya is also a musician, performs music, and teaches robots music."

Recovered values:

- Vasya as the admitted holder system; `MusicalRobotLab_2026` is the lab and work locus in its direct relations, not a participant added to `U.RoleAssignment`;
- `MusicalRobotLabRoles-2026` as the role-taxonomy episteme and `MusicalRobotLab-Scheme` as its effective reference scheme;
- an engineering role value or local engineering-role expression;
- robotics as a domain, practice, method-family, or work-field qualification of that engineering role expression;
- `MusicianRole` as an independent role value when music performance matters separately;
- robot-engineering method or work, music-performance work, and robot-music-teaching method or work under method and work patterns;
- an optional role-algebra, graph, matrix, embedding, or neural representation only if the project actually uses such a lens to describe the selected role relation structure.

If a durable qualified role value has been admitted, no separately recoverable F.17 coordinate is current for this local-only case, so the card states one direct `LocalSenseRef` using `engineer-roboticist`; `robotics engineer` remains a NameCard lineage alias and does not identify a second sense coordinate. Its naming settlement can be:

```text
NameCard:
  NameCardId: NameCard.RoboticsEngineerRole.MusicalRobotLab.2026
  GovernedValueRef: RoboticsEngineerRole
  GovernedValueKindRef: U.Role
  GoverningPatternRef: A.2
  ReferenceScheme: MusicalRobotLab-Scheme
  ClaimContent: NameCard.RoboticsEngineerRole.MusicalRobotLab.2026.ClaimGraph — complete C.2.1 U.ClaimGraph constituted by all identity-bearing naming-settlement claims designated below
  LocalSenseRef: local expression `engineer-roboticist`; sense claim: the admitted engineering role qualified by the robotics work field under MusicalRobotLab-Scheme
  LocalSenseBasisRelationRef: absent; no separate source-bearing basis relation is current for this use
  TechLabel: RoboticsEngineerRole
  PlainLabel: engineer-roboticist
  CandidateSet: RoboticsEngineerRole; engineer-roboticist; robotics engineer; engineer and roboticist; RobotEngineeringMethod; engineer-roboticist-musician
  CandidateCoverage: Tech role head; two ordinary role-expression forms; method neighbour; compressed multi-role neighbour; no plausible live head family remains untested
  RejectedCandidates: engineer and roboticist; engineer-roboticist-musician; RobotEngineeringMethod
  SelectionRationale: Tech `RoboticsEngineerRole` and Plain `engineer-roboticist` are selected for this source-preserving lab use; robotics remains a qualification of engineering, musician remains a separate role assignment, and method or work names do not become role names
  BridgeRefs: absent; the card makes no semantic-correspondence claim
  PublicRowStatus: localOnly; change to pending only if public or cross-context reuse opens and section 4.4 does not yet pass
  UnifiedTermRowRef: absent
  LineageEntries: initial durable qualified-role settlement; `robotics engineer` retained as a Plain alias for the same value, scheme, sense, and declared use, not as a second selected PlainLabel; earlier local wording retained when no durable role value is admitted
  RefreshCondition: reopen if A.2 changes the role value, A.2.7 changes the qualification relation, the taxonomy episteme or scheme changes, or readers merge musician assignment, method, or work into this role name
```

The robotics qualification relation remains separately governed by `A.2.7`; the card does not absorb it into role identity. If no durable qualified role value is admitted, keep `engineer-roboticist` as local ordinary wording rather than filling the card. In ordinary project communication, "Vasya is our engineer-roboticist and musician" is admissible when the two assignments remain recoverable. If the current object is a method, name `RobotEngineeringMethod` or the relevant method family under `A.3.1`. If a separately identified `RobotEngineeringMethodDescription : U.MethodDescription` episteme is current, name it separately under `A.3.2` only when its exact `EntityOfConcern` is that Method. If the current object is performed work, name the work occurrence under `A.15.1`. If public reuse becomes current, apply section 4.4; do not infer a current F.17 row from this local card.

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

F.18 settlement: no durable role name is minted. If a public term is needed, first name the exact evidence-use relation, for example `ModelCardEvidenceUse`, with `A.10` as governing pattern. Then apply the section 4.4 gate; until it passes, retain the durable relation name and NameCard locally and mark the public row pending.

#### F.18:7.4 - Interface-Like Source Phrase

A software team says "the payment interface owns customer identity".

Recovered candidates:

- module interface under `A.6.M`;
- API description or protocol under `A.6.C`;
- signature or SlotSpecs under `A.6.0` and `A.6.5`;
- claim-bearing interface description under `C.2.1`;
- multi-view publication face or form under `E.17`;
- publication availability, form expression, or carrier bearing under `E.24.PUB`;
- responsible role assignment under `A.2.1`.

F.18 settlement: do not mint `PaymentInterfaceRole`. First recover which governed value the phrase names. Then name that value through its governing pattern.

#### F.18:7.5 - Cross-Context Name

Two teams use `component`, `module`, and `unit` for nearby meanings.

Recovered values:

- structural component under architecture and part-whole patterns;
- deployable module under module-interface patterns;
- management unit under organizational patterns.

F.18 settlement: first keep the three recovered values and their local labels separate. If only local speech is needed, stop there; do not name a claim merely because one team wants to explain the difference. If a public term use is proposed between different `<ReferenceScheme, LocalSenseClaim>` projections, identify the exact source and receiving F.17 cells and test the F.9 Bridge predicate between them. The same scheme with different `LocalSenseClaim` values qualifies; a different scheme only opens the question and never establishes the relation. When the Bridge obtains, state in ordinary C.2.1 wording whether it is suitable for this naming use, naming the direction, label-correspondence rule, tolerated loss, and polarity, and establish the current A.10 or B.3 reliance required by section 1. The Bridge does not choose the Tech label, the claim does not identify the governed value, and neither authorizes or performs publication. Only after those objects are current does section 4.4 send the naming settlement to F.17. If the F.17 gate fails, keep the name and card local and mark the row pending; if no correspondence use is current, stop with the local settlement and create no Bridge or use claim regardless of scheme count.

