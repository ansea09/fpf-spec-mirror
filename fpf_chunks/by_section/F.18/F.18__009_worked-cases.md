---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local-First Unification Naming Protocol"
section_id: "F.18:7"
section_title: "Worked Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__009_worked-cases.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "F.18 — Local-First Unification Naming Protocol"
  - "F.18:7 — Worked Cases"
line_start: 99484
line_end: 99650
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

#### F.18:7.1 - System-Role Kind, Assignment, Capability, Method, and Work

A shipyard team wants one reusable name for the local system-role kind used in shipbuilding Work. It first separates the values that the source word *shipbuilder* could hide.

Recovered values:

- `ShipbuilderSystemRole`, one local C.3 kind whose admitted-system candidates count when they satisfy the current shipbuilding condition; the member/non-member probes and continuity rule expose the boundary, while the ShipyardProduction source only locates the definition;
- one direct assignment occurrence under A.2.1 whose admitted holder system and assigned `ShipbuilderSystemRole` kind are explicit, while any work area, schedule, interpretation, or reference scheme remains separate unless that direct species needs it for occurrence identity;
- `ShipbuildingCapability` with envelope and measures under the capability pattern;
- `ShipbuildingMethod` or a method family under A.3.1; if a separately identified `ShipbuildingMethodDescription : U.MethodDescription` episteme is current, name it separately under A.3.2 only when its exact `EntityOfConcern` is that Method;
- `HullAssemblyWork` under the Work patterns.

Here `HullAssemblyWork` is a work-family label or a label in a plan or assignment episteme. A designator such as `HullAssemblyWork-42@2026-07-15T09:10–11:35` names performed Work only when each exact actual performer has its A.13 core and A.15.1 independently admits the occurrence from the Method actually used, temporal extent, containing System, affected hull referent, material bindings, resource-use facts, and any current continuity policy. If the naming record also expressly represents which assignment covered that Work, it adds the exact A.2.1 occurrence and F.6 relation through the same A.13 assignment; missing or failed F.6 leaves the Work name intact. A changed hull state, measurement result, evaluation verdict, delivery occurrence, or acceptance verdict remains a separately defined and separately named value.

The local card is:

```text
NameCard:
  NameCardId: NameCard.ShipbuilderSystemRole.ShipyardProduction.2026
  GovernedValueRef: ShipbuilderSystemRole
  GovernedValueKindRef: U.Kind
  SubjectPatternLocator: A.2 with C.3
  ReferenceScheme: Shipyard-Production-Scheme
  ClaimContent: NameCard.ShipbuilderSystemRole.ShipyardProduction.2026.ClaimGraph
  LocalSenseRef: local expression `shipbuilder (system role)`; sense claim: the C.3 kind whose admitted-system candidates satisfy the current shipbuilding condition, member/non-member boundary, and continuity rule; ShipyardProduction provenance locates this settlement but does not identify the kind
  LocalSenseBasisRelationRef: absent; no independent local-sense basis relation is current
  TechLabel: ShipbuilderSystemRole
  PlainLabel: shipbuilder (system role)
  CandidateSet: ShipbuilderSystemRole; ShipbuilderRole; ShipbuilderSystemRoleKind; ShipbuildingCapability; HullAssemblyWorker; CertifiedShipbuilder
  CandidateCoverage: system-role-kind head; ambiguous role head; redundant kind suffix; capability head; holder-or-work head; certification-or-status head
  RejectedCandidates: ShipbuilderRole; ShipbuilderSystemRoleKind; ShipbuildingCapability; HullAssemblyWorker; CertifiedShipbuilder
  SelectionRationale: the selected label designates the already recovered local kind without claiming admission, assignment, capability, performed Work, or certification
  BridgeRefs: absent; this local settlement makes no semantic-correspondence claim
  PublicRowStatus: localOnly
  UnifiedTermRowRef: absent
  LineageEntries: `ShipbuilderRole` is retained only as predecessor wording; source word `shipbuilder` remains ordinary where no stable kind reference is needed
  RefreshCondition: reopen if the local kind identity changes or repeated readers infer a non-human-only system, admission, assignment, agency, capability, or Work from the name
```

The candidates execute the section 4.3 stopping rule: each live head family is represented, and the recovered Method and Work objects are not synonyms for the local kind. If public or cross-context reuse becomes current, apply section 4.4; until it passes, keep this card local.

#### F.18:7.1a - Reviewer in a Journal Context

`ReviewerSystemRole` designates the local kind whose admitted-system candidates count when they supply a substantive review judgment that meets the current JournalReview acceptance conditions. The candidate range, operative condition, member/non-member probes, and continuity rule recover the kind; JournalReview-2026 provenance only locates the definition. A review assignment, responsibility, authority, capability, permission, and performed review Work remain separate claims.

```text
NameCard:
  NameCardId: NameCard.ReviewerSystemRole.JournalReview.2026
  GovernedValueRef: ReviewerSystemRole
  GovernedValueKindRef: U.Kind
  SubjectPatternLocator: A.2 with C.3
  ReferenceScheme: FPFCoreReferenceScheme
  ClaimContent: NameCard.ReviewerSystemRole.JournalReview.2026.ClaimGraph
  LocalSenseRef: local expression `reviewer (system role)`; sense claim: the C.3 kind whose admitted-system candidates satisfy the current substantive-review condition, member/non-member boundary, and continuity rule; JournalReview-2026 provenance locates this settlement but does not identify the kind
  TechLabel: ReviewerSystemRole
  PlainLabel: reviewer (system role)
  CandidateSet: ReviewerSystemRole; ReviewerRole; ReviewerSystemRoleKind; ReviewerSystemWorkRole; reviewer
  RejectedCandidates: ReviewerRole; ReviewerSystemRoleKind; ReviewerSystemWorkRole
  SelectionRationale: `SystemRole` exposes the system-classification reading; `Kind` is already stated by `U.Kind`, while `Work` would add a false occurrence claim
  BridgeRefs: absent
  PublicRowStatus: localOnly
  UnifiedTermRowRef: absent
  LineageEntries: `ReviewerRole` is predecessor wording only; ordinary `reviewer` remains available when no stable technical reference is needed
  RefreshCondition: reopen on a changed local kind or repeated non-human-only, admission, assignment, agency, capability, participation, or Work overread
```

No F.17 row is created without a named public or cross-local reader use.

#### F.18:7.2 - Engineer-Roboticist and Musician

A lab says: “Vasya is an engineer, does robot engineering, is therefore an engineer-roboticist. These are musical robots, and Vasya is also a musician, performs music, and teaches robots music.”

Recovered values:

- Vasya as an admitted system; `MusicalRobotLab_2026` is the lab and Work locus in its direct relations, not a generic assignment participant;
- `RoboticsEngineerSystemRole`, one local system-role kind whose admitted-system candidates count when they satisfy the current robotics-engineering condition, boundary probes, and continuity rule; MusicalRobotLab provenance locates the definition but does not identify the kind;
- robotics as the qualification that distinguishes this local engineering kind, with any non-monotonic restriction retained as a separate A.2.7 relation;
- `MusicianSystemRole` as another exact local kind when its own music-performance condition and boundary matter separately;
- any current engineering or musician assignments as occurrences of their declared A.2.1 species;
- robot-engineering Method or Work, music-performance Work, and robot-music-teaching Method or Work under their direct patterns;
- an optional algebraic, graph, matrix, embedding, or neural representation only if the project actually uses that lens to describe the selected system-role-kind relation structure.

If the exact robotics-qualified local kind has been admitted, its local naming settlement is:

```text
NameCard:
  NameCardId: NameCard.RoboticsEngineerSystemRole.MusicalRobotLab.2026
  GovernedValueRef: RoboticsEngineerSystemRole
  GovernedValueKindRef: U.Kind
  SubjectPatternLocator: A.2 with C.3 and A.2.7 for the separately current qualification relation
  ReferenceScheme: MusicalRobotLab-Scheme
  ClaimContent: NameCard.RoboticsEngineerSystemRole.MusicalRobotLab.2026.ClaimGraph
  LocalSenseRef: local expression `engineer-roboticist`; sense claim: the C.3 kind whose admitted-system candidates satisfy the current robotics-engineering condition, member/non-member boundary, and continuity rule; MusicalRobotLab provenance locates this settlement but does not identify the kind
  LocalSenseBasisRelationRef: absent; no separate source-bearing basis relation is current for this use
  TechLabel: RoboticsEngineerSystemRole
  PlainLabel: engineer-roboticist
  CandidateSet: RoboticsEngineerSystemRole; RoboticsEngineerRole; engineer-roboticist; robotics engineer; engineer and roboticist; RobotEngineeringMethod; engineer-roboticist-musician
  CandidateCoverage: system-role-kind head; ambiguous role head; two ordinary expressions; method neighbour; compressed multi-kind neighbour
  RejectedCandidates: RoboticsEngineerRole; engineer and roboticist; engineer-roboticist-musician; RobotEngineeringMethod
  SelectionRationale: the Tech label exposes one local system-role kind; the Plain label preserves recognizable lab speech; musician classification or assignment, Method, and Work remain separate
  BridgeRefs: absent; the card makes no semantic-correspondence claim
  PublicRowStatus: localOnly
  UnifiedTermRowRef: absent
  LineageEntries: `RoboticsEngineerRole` is predecessor wording only; ordinary `robotics engineer` remains available in local prose when no stable technical reference is needed
  RefreshCondition: reopen if the local kind or A.2.7 qualification changes, or readers merge musician classification or assignment, Method, or Work into this name
```

If no durable qualified kind is admitted, keep *engineer-roboticist* as local ordinary wording rather than filling the card. Ordinary project communication may say “Vasya is our engineer-roboticist and musician” when the separate claims about his engineering and musicianship remain recoverable; any assignment is another claim. Name a current Method, MethodDescription, or performed Work through A.3.1, A.3.2, or A.15.1. If public reuse becomes current, apply section 4.4; do not infer an F.17 row from this local card.

#### F.18:7.2a - Method Relation Structure and Method Algebra Name

A lab says: "Use the robot-engineering method algebra: choose scouting, then calibration, then training; fall back to teleoperation if training fails."

Recovered values:

- one or more robot-engineering methods or method families under `A.3.1`;
- a method-family registry or selector outcome under `G.5` when the family registry or selector result is current;
- `MethodRelationStructure` for the named `MusicalRobotLab_2026` use when the current claim concerns serial composition, guarded fallback, or family selection among exact methods;
- a method description when the source notation describes that structure;
- a `C.29` mathematical-lens use when "algebra" is the selected representation for checking composition, fallback, or preserved/lost structure;
- work plan or dated work only when a concrete plan or occurrence is current.

F.18 settlement: `RobotEngineeringMethod` names a Method or method family only when that is the governed value. `RobotEngineeringMethodRelationStructure` may name the selected method relation structure when durable naming is needed. `RobotEngineeringMethodAlgebra` names the lens only when the algebraic representation itself is the governed value. Do not use a system-role-kind label such as `RoboticsEngineerSystemRole` to name the method relation structure, and do not use *method algebra* to hide a WorkPlan or performed Work.

#### F.18:7.3 - Evidence-Like Source Phrase

A review table contains the phrase "model card evidence role".

Recovered values:

- a model-card episteme;
- an evidence-use relation to a target claim;
- possible source-currentness and assurance-use relations;
- no system-role kind, assignment, or acting system merely because the episteme is used as evidence.

F.18 settlement: no system-role-kind or assignment name is minted. If a public term is needed, first name the exact evidence-use relation, for example `ModelCardEvidenceUse`, with A.10 as its direct pattern. Then apply the section 4.4 gate; until it passes, retain the durable relation name and NameCard locally and mark the public row pending.

#### F.18:7.4 - Interface-Like Source Phrase

A software team says "the payment interface owns customer identity".

Recovered candidates:

- module interface under `A.6.M`;
- API description or protocol under `A.6.C`;
- signature or SlotSpecs under `A.6.0` and `A.6.5`;
- claim-bearing interface description under `C.2.1`;
- multi-view publication face or form under `E.17`;
- publication availability, form expression, or carrier bearing under `E.24.PUB`;
- a system-role assignment under A.2.1 only when an occurrence belongs to a declared species, has an admitted System as holder, and has the local kind as assigned-kind value; any responsibility or authority relation remains separate.

F.18 settlement: do not mint `PaymentInterfaceRole`. First recover which governed value the phrase names. Then name that value through its subject pattern.

#### F.18:7.5 - Cross-Context Name

Two teams use `component`, `module`, and `unit` for nearby meanings.

Recovered values:

- structural component under architecture and part-whole patterns;
- deployable module under module-interface patterns;
- management unit under organizational patterns.

F.18 settlement: first keep the three recovered values and their local labels separate. If only local speech is needed, stop there; do not name a claim merely because one team wants to explain the difference. If a public term use is proposed between different `<ReferenceScheme, LocalSenseClaim>` projections, identify the exact source and receiving F.17 cells and test the F.9 Bridge predicate between them. The same scheme with different `LocalSenseClaim` values qualifies; a different scheme only opens the question and never establishes the relation. When the Bridge obtains, state in ordinary C.2.1 wording whether it is suitable for this naming use, naming the direction, label-correspondence rule, tolerated loss, and polarity, and establish the current A.10 or B.3 reliance required by section 1. The Bridge does not choose the Tech label, the claim does not identify the governed value, and neither authorizes or performs publication. Only after those objects are current should the practitioner apply F.17 as specified in section 4.4. If the F.17 gate fails, keep the name and card local and mark the row pending; if no correspondence use is current, stop with the local settlement and create no Bridge or use claim regardless of scheme count.

