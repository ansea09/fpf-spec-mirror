---
chunk_kind: "child"
pattern_id: "C.22.PFR"
pattern_title: "Problematic-For Relation"
section_id: "C.22.PFR:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.PFR/C.22.PFR__006_archetypal-grounding.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "C.22.PFR — Problematic-For Relation"
  - "C.22.PFR:5 — Archetypal Grounding"
line_start: 52101
line_end: 52130
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19"
  - "A.3.4"
  - "A.6.5"
  - "A.6.REL"
  - "B.3"
  - "C.22"
  - "C.22.2"
  - "E.18.1"
  - "E.23"
  - "G.11"
keywords:
---

### C.22.PFR:5 - Archetypal Grounding

**Executable first use — an assignment that violates a release criterion.** `InspectionReleaseAssignment` is a declared `U.SystemRoleAssignment` species defined under A.2.1. It defines the holder and assigned-kind participant meanings, assignment predicate, applicability, and occurrence identity. Occurrence `InspectionAssignment-17` has admitted System `Robot-7` as holder and local kind `InspectorSystemRole` as assigned-kind value. It obtains without interruption during `[2026-07-13T09:00, 2026-07-13T17:00]`. `MaintenanceRoles-2026`, `Maintenance-Scheme-A`, and the interval description may interpret or describe the assertion; they are not extra world-side participants. A roster row and `InspectionAssignmentAssertion-17` may describe the assignment and interval; neither makes the relation obtain.

A.2.1 identifies `InspectionAssignment-17` through the complete real participant set and the maximal uninterrupted period in which the direct species predicate obtains. Demonstrated non-assignment after the stated 17:00 boundary ends it. If the same participant set again satisfies the predicate on the next day after that actual gap, `InspectionAssignment-18` is a later occurrence; an evidence gap by itself neither ends nor splits the first occurrence. The subject pattern therefore supplies the participant meanings, obtaining rule, temporal extent, recurrence, and same-versus-new-occurrence rule required of `ActualConditionRelationSlot`.

The by-value predicate `NoInspectorSystemRoleBeforeValidation-v2` uses one direct `ConditionToPredicateInputRule`: from `InspectionAssignment-17` it reads the assigned-kind participant as coordinate `assignedSystemRoleKind = InspectorSystemRole` on a nominal system-role-kind scale and the holder participant as the direct link to problem-for entity `Robot-7`. Its adverse region is the declared set of system-role kinds prohibited for that System's autonomous-inspection release before validation, which contains `InspectorSystemRole`. The same kind assigned to another System is the nearest inadmissible input because its holder participant does not link the condition to `Robot-7`; a roster row is inadmissible because it is not the obtaining assignment occurrence.

`Robot7ReleaseCriterionApplicability-4` is the separate applicability occurrence. Its four participants are that predicate, `Robot-7`, `autonomous inspection release before validation` as the exact `U.ClaimScope`, and declared window `[2026-07-13T08:30, 2026-07-15T18:00]`. Because both participant relations obtain and the selected point is adverse, `PFR-InspectionAssignment-17` obtains on `[2026-07-13T09:00, 2026-07-13T17:00]`. The ordinary first-use sentence is:

> Robot-7 is assigned as inspector through `InspectionAssignment-17`, while `InspectorSystemRole` is prohibited for this System's autonomous-inspection release before validation during the declared 13–15 July window. This assignment is an actual Problem for Robot-7's release during its 13 July 09:00–17:00 assignment episode.

**Evaluation and reliance remain separate.** Admitted `SafetyReviewSystem-2 : U.System` performs dated `InspectionReleaseCheckWork-21` under independently obtaining `SafetyReviewAssignment-9 : SafetyReviewWorkAssignment <: U.SystemRoleAssignment`; F.6 uses the assignment's holder projection, and the Work enacts `InspectionReleaseCheckMethod-3`. The operation application returns `true` for the adverse predicate. `InspectionReleaseCheckAssertion-21` states that result; its evidence path and assurance tuple can warrant one release decision, G.11 can qualify the assertion edition, and the release Work can rely or decline. None is a third PFR participant. A `ProblemCard` may later designate `PFR-InspectionAssignment-17`; creating, revising, splitting, or publishing that card changes neither PFR participant nor actuality. If evaluation never occurs, the PFR still obtains. If the assertion is stale, the decision's reliance may become `unknown`, but the world-side relation is not thereby created, ended, or split.

**Actuality and recurrence.** Selecting another staffing Method and writing a Work order do not end the PFR. Only actual cessation of the A.2.1 assignment predicate at the stated 17:00 boundary ends it. When the same direct species predicate resumes on the next day as `InspectionAssignment-18` while the applicability occurrence still obtains, A.2.1 identifies that later system-role-assignment occurrence and its later adverse inception grounds `PFR-InspectionAssignment-18`. An evidence gap alone establishes neither continuous assignment nor withdrawal and reassignment.

**Blocked stress fixture — installed component.** `Fuse-R17 : U.System` and `Panel-7 : U.System` may be named in a parts claim, but current A.14 supplies no installed-part relation kind, installed-part participant meanings, obtaining predicate, temporal extent, recurrence, or same-versus-new-occurrence rule. Under A.6.REL:5.2, `ComponentOf-FuseR17-Panel7` is therefore not minted as an individuated installed-part occurrence here. A parts list, inspection note, removal report, or reinstallation wording cannot fill `ActualConditionRelationSlot`; the fuse case remains non-conforming until an accepted direct installed-part pattern supplies the complete settlement.

**Blocked stress fixture — battery voltage.** Current A.18 and C.16 can govern the voltage characteristic, scale, measurement work, result, uncertainty, and assertion. They do not supply a direct voltage-state relation with participant meanings, obtaining, temporal extent, recurrence, and occurrence identity. Therefore `TerminalVoltageState-12` is not minted here, and the low-voltage case remains non-conforming until an A.6.RCD decision selects or assigns that direct governor. `MeterReport-88`, an alarm, or a maintenance card may support a claim but cannot fill `ActualConditionRelationSlot` or backdate PFR.

**Blocked stress fixture — proof gap.** Current proof and assurance patterns define or constrain proof epistemes, obligations, evidence, and relying decisions, but no inspected direct pattern supplies both (a) an individuable unresolved-consequence relation with its obtaining and episode law and (b) the exact proof-use or acceptance object and applicability relation needed by the case. Keep the condition gate and problem-for/applicability gate separate. `UnresolvedConsequence-17`, `ProofUseEntity`, and an omnibus proof-gap object are not admitted by this wording; the case remains non-conforming until both direct governors close.

**Blocked stress fixture — clinical condition.** A diagnosis, assessment, measurement report, and patient label are epistemes or context-dependent cues, not the clinical-condition occurrence or patient identity. No clinical-condition pattern selected in this package supplies the needed participants, obtaining, recurrence, identity, and temporal extent. Until one does, keep the case non-conforming. If *patient* also names a work-facing classification or assignment, recover the holder System, local system-role kind, assignment occurrence, and declared `U.SystemRoleAssignment` species separately; none supplies the missing clinical-condition relation.

**Blocked stress fixture — missed transfer.** First distinguish transfer Work, a world-side transfer or delivery relation, a commitment or acceptance relation, and a package or record episteme. E.18's structural `U.Transfer` cannot be reused merely by the phrase *hand-off failure*. No inspected direct pattern supplies the exact missed-transfer condition relation, and the phrase *receiving work* does not decide whether the problem-for entity is intended `U.WorkPlan`, dated `U.Work`, or another governed entity. The case therefore remains non-conforming until separate direct governors settle both questions.

**Blocked stress fixture — one hot surface, two uses.** No inspected direct pattern supplies an individuated hot-surface condition relation; a temperature reading cannot substitute for it. If such a governor later exists, hold its one occurrence fixed and use two distinct applicability occurrences when an exact receiving `U.Work` and an exact `U.System` have different problem-for fillers, scopes, declared windows, or applicability continuity. Adverse truth would then yield two PFR occurrences sharing only the condition reference. Until the condition gate closes, this remains a multiplicity test, not an asserted example.

**Repair branch replay.** Keep four outcomes distinct: a repair method is selected; repair work is planned; dated repair work occurs without a demonstrated condition change; or dated repair work is connected through its direct change/result governors to actual cessation or non-adversity of the condition. Only the fourth outcome can end PFR while applicability continues. A work record, result claim, acceptance verdict, or method label is insufficient.

