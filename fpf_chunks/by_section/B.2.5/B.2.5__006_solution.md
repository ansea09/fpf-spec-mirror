---
chunk_kind: "child"
pattern_id: "B.2.5"
pattern_title: "Supervisor-Subholon Feedback Relation"
section_id: "B.2.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.5/B.2.5__006_solution.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "B.2.5 — Supervisor-Subholon Feedback Relation"
  - "B.2.5:4 — Solution"
line_start: 41680
line_end: 41750
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15.1"
  - "A.2.1"
  - "A.20"
  - "A.21"
  - "A.3.3"
  - "A.3.4"
  - "A.6.M"
  - "A.6.RCD"
  - "B.1"
  - "B.2"
  - "B.2.P"
  - "B.3"
  - "C.13"
  - "C.2.1"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30.LCA"
  - "E.10"
  - "F.19"
  - "G.6"
keywords:
---

### B.2.5:4 - Solution

State the feedback claim in one C.2.1 episteme about the named controller and supervised holons. A sufficient ordinary reading is: “For every drone in this set during the stated interval, controller C receives the stated observations and returns commands coupled to those observations under rule R.” Use A.6.RCD's compound-claim branch; the description does not require a new relation kind or one independently reidentifiable feedback occurrence.

For a nonempty set H and each h in H, recover three propositions under their direct domain definitions:

1. **Observation:** which state of h is observed or reported to the controller, through which obtaining observation, report, publication or source relation.
2. **Return:** which influence from the controller reaches h, under the applicable command, constraint, objective, mode or Work predicate.
3. **Coupling:** which rule applies to this observation and return, and which facts establish that this return depends on that observation under the rule.

The compound claim is true exactly when all three propositions hold for every member of H under common applicability: the same named use, participants, scope and temporal qualification. This is ordinary logical conjunction of those propositions, not a combination of probability scores or assurance results. Recover each direct definition and its applicable edition when the claim relies on it. A local use needs no separately published conjunction rule.

An optional note can retain the needed details:

```text
SupervisorSubholonFeedbackClaim@Context:  // claim-bearing episteme, not U.Relation
  supervisingActingSystemRef: U.EntityRef resolving to one admitted U.System
  supervisedHolonRefs: FinSet(U.HolonRef)  // nonempty
  useAndTemporalQualification:
  pairClaims:  // one for every supervised holon
    supervisedHolonRef:
    observationClaimAndBaseRelationRefs:
    returnedInfluenceClaimAndBaseRelationRefs:
    applicableCouplingRuleAndEdition:
    couplingFacts:
  supervisorSystemRoleKindRef?:
  supervisorSystemRoleAssignmentRef?:
  evidenceRefs?:
  strongerClaimPatternRefs?:
```

Observation and influence references keep their own kinds; a report episteme, a signal occurrence and a source-use relation are not interchangeable occupants of one relation position. Evidence supports the assertion under A.10; its adequacy and the obtaining of the base facts remain separate questions. A local system-role kind and assignment are added only when they independently obtain and affect this use.

#### B.2.5:4.1 - Establish and qualify the conjunction

Co-present telemetry and commands are insufficient. For each pair, apply the coupling rule to the actual observation and return. An unrelated broadcast fails that condition; one-way reporting fails the two-sided predicate. If the rule is missing, return the missing governor. If the rule exists but a needed observation or dependency fact is unavailable, return missing information. Neither absence of proof alone nor an empty supervised set supports the affirmative assertion. A negative claim needs the rule's non-obtaining test and facts that satisfy it.

Keep the base occurrences and their own extent and continuity rules. A communication break can make an interval-qualified feedback assertion fail without ending a supervisor assignment. Reconnection requires current observation, return and coupling facts. Apply a changed policy to the affected interval; adding a holon extends the asserted set only after its own pair is supported.

Reopen the dedicated relation-kind alternative only when a receiving use needs to identify a feedback occurrence independently across changes. That alternative must supply its obtaining, extent and continuity rules, including interruptions, under A.6.RCD and A.6.REL. A useful compound description can stop here.

#### B.2.5:4.2 - Part-Whole Boundary

A supervised holon may be part of a larger holon, but supervision and parthood are different relations. A controller, committee, platform-governance group, review board, or tool-mediated group can supervise when the exact acting entity is independently admitted as `U.System`; it may do so under an exact system-role assignment without being a physical part of the supervised holon. A method, policy, or review practice can structure the supervision work; it does not supervise by itself.

Use `A.1` for holon recognition, `A.14` for the exact mereological claim, and `B.1` or `C.13` for the applicable construction account. Use B.2.5 for the compound supervisor-subholon feedback claim.

#### B.2.5:4.3 - Acting-System Boundary

The supervising participant is an admitted acting system. When local classification matters, A.2 supplies the exact supervisor system-role kind and A.2.1 supplies the obtaining assignment; neither label nor assignment acts. Do not create `U.TransformerRef` or treat a publication, theory, dashboard, model, method description, or report as the acting system.

For acting-side externalization, use `A.12`. For transformation, use `A.3.4`. For Work, use `A.15.1`. For system-role kind and assignment, use `A.2` and `A.2.1`.

#### B.2.5:4.4 - Control-Structure View Boundary

When feedback is drawn as planner, controller, observer, plant and supervisor structure, B.2.5 states the compound claim and `C.30.LCA` governs the control-structure view. The view can cite both the assertion and the independently obtaining base relations. Its arrows alone establish neither their obtaining nor the coupling.

#### B.2.5:4.5 - Neighboring Claim Boundary

B.2.5 does not certify stability, safety, assurance, evidence sufficiency, causal validity, gate passage, rate adequacy, or mathematical adequacy.

Use:

- `A.3.3` for reusable dynamics or state-evolution claims;
- `C.27` for temporal and rate adequacy;
- `C.28` for causal-use claims;
- `A.10` and `G.6` for evidence and provenance;
- `B.3` for assurance;
- `A.20` for its internal-constraint test in a transformation-flow structure and `A.21` for gate decisions;
- `C.29` for mathematical-lens use.

