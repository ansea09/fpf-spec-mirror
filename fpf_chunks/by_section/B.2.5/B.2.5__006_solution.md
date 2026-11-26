---
chunk_kind: "child"
pattern_id: "B.2.5"
pattern_title: "Supervisor-Subholon Feedback Relation"
section_id: "B.2.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.5/B.2.5__006_solution.md"
commit_sha: "9d38fbfe4ce5b72d8fe05e839cbca0025a5b31cf"
heading_path:
  - "B.2.5 — Supervisor-Subholon Feedback Relation"
  - "B.2.5:4 — Solution"
line_start: 46670
line_end: 46750
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

For a claim about actual supervision, identify who or what was observed and who or what received the coupled influence. A controller may use a joint condition to act on a whole. A local observation may instead govern an action on one part. For a claim that holds separately for several holons, state it for the required members and interval. One account applying throughout that scope can support all the pairs. State the result in a C.2.1 episteme using A.6.RCD's compound-claim branch. A further use may call for a separately reidentifiable occurrence under :4.1.

For a nonempty set H and each h in H, recover three propositions under their domain definitions:

1. **Observation:** which state of h is observed or reported to the controller, through which obtaining observation, report, publication or source relation.
2. **Return:** which influence from the controller reaches h, under the applicable command, constraint, objective, mode or Work predicate.
3. **Coupling:** which rule applies to this observation and return, and which facts establish that this return depends on that observation under the rule.

The compound claim is true exactly when all three propositions hold for every member of H under common applicability: the named use, participants, scope and temporal qualification. This is logical conjunction of those propositions, not a combination of probability scores or assurance results.

Recover each definition and its applicable edition when the claim relies on it. A local use needs no separately published conjunction rule.

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

Observation and influence references keep their kinds; a report episteme, a signal occurrence and a source-use relation are not interchangeable occupants of one relation position.

Evidence supports the assertion under A.10; its adequacy and the obtaining of the base facts remain separate questions. A local system-role kind and assignment are added only when they independently obtain and affect this use.

#### B.2.5:4.1 - Establish and qualify the conjunction

Trace the observation into the choice made under the applicable rule and the resulting influence to its recipient. An observation can enter the choice even when another reading in the same range would yield the same action. A matching schedule and a copy of the observation show no such use by themselves. A record that identifies the actual input, executed rule and delivered result can settle the question directly. For one-way reporting, retain the established observation.

A confirmed failure of a condition required by the claim, such as a return to a named supervised holon, rules out that claim for the stated interval. When the remaining decision depends on an unspecified coupling rule, identify the missing rule. If the rule is applicable and a required fact is undecided, identify the information that would settle it. Check the rule’s requirement for a nonempty supervised set before an affirmative assertion.

Keep the base occurrences and their extent and continuity rules. A communication break can make an interval-qualified feedback assertion fail without ending a supervisor assignment. Reconnection requires current observation, return and coupling facts.

Apply a changed policy to the affected interval; adding a holon extends the asserted set only after its pair is supported. A common rule and evidence covering every required member may supply those grounds together. To establish feedback on a particular part, show how the observation represents a relevant state of that part and how the coupled return reached it. For a question about receipt alone, confirmed delivery to every member can establish that one member received the message even when its state was never observed.

Reopen the dedicated relation-kind alternative only when a receiving use needs to identify a feedback occurrence independently across changes. That alternative must supply its obtaining, extent and continuity rules, including interruptions, under A.6.RCD and A.6.REL. A useful compound description can stop here.

#### B.2.5:4.2 - Part-Whole Boundary

A supervised holon may be part of a larger holon, but supervision and parthood are different relations. The supervising entity must be independently admitted as `U.System`; it may supervise under a system-role assignment without being a physical part of the supervised holon. A method, policy, or review practice can structure the supervision work; it does not supervise by itself.

Use `A.1` for holon recognition, `A.14` for the mereological claim, and `B.1` or `C.13` for the applicable construction account. Use B.2.5 for the compound supervisor-subholon feedback claim.

#### B.2.5:4.3 - Acting-System Boundary

The supervising participant is an admitted acting system. When local classification matters, A.2 supplies the supervisor system-role kind and A.2.1 supplies the obtaining assignment. Distinguish that system from an episteme it uses, such as a policy or report.

For acting-side externalization, use `A.12`. For transformation, use `A.3.4`. For Work, use `A.15.1`. For system-role kind and assignment, use `A.2` and `A.2.1`.

#### B.2.5:4.4 - Control-Structure View Boundary

When feedback is drawn as planner, controller, observer, plant and supervisor structure, B.2.5 states the compound claim and `C.30.LCA` governs the control-structure view. The view can cite both the assertion and the independently obtaining base relations. Its arrows alone establish neither their obtaining nor the coupling.

To design the feedback, start with the decisions the responsible system must be able to take. Which changes of state would require different action, and by when can that system observe the difference and act? Several arrangements of the parts can give the same whole-level indication. For each indication available before the decision, choose a permitted response that serves every admissible arrangement still consistent with it. If no such response exists, seek a timely observation that separates cases sufficiently for that choice, or revise the proposed policy. The aggregate can suffice when the same response serves the entire group. Specify the participants, observation, return and coupling for the required uses. This conditional result can complete a design commission. An assertion about an actual interval still uses :4.1.

#### B.2.5:4.5 - Neighboring Claim Boundary

B.2.5 does not certify stability, safety, assurance, evidence sufficiency, causal validity, gate passage, rate adequacy, or mathematical adequacy.

Use:

- `A.3.3` for reusable dynamics or state-evolution claims;
- `C.27` for temporal and rate adequacy;
- `C.28` for causal-use claims;
- `A.10` and `G.6` for evidence and provenance;
- `B.3` for assurance;
- `A.20` for its internal-constraint test in a transformation-flow structure and `A.21` for gate decisions;
- `C.29` for a remaining mathematical representation, correspondence, transfer or reliance question.

