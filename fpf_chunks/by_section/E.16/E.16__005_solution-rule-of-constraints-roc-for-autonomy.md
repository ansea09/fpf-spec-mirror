---
chunk_kind: "child"
pattern_id: "E.16"
pattern_title: "RoC‑Autonomy Budget & Enforcement"
section_id: "E.16:4"
section_title: "Solution — Rule‑of‑Constraints (RoC) for Autonomy"
source_path: "FPF-Spec.md"
output_path: "by_section/E.16/E.16__005_solution-rule-of-constraints-roc-for-autonomy.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "E.16 — RoC‑Autonomy Budget & Enforcement"
  - "E.16:4 — Solution — Rule‑of‑Constraints (RoC) for Autonomy"
line_start: 90712
line_end: 90838
dependencies:
  - "A.10"
  - "A.13"
  - "A.15"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.21"
  - "B.3"
  - "C.16"
  - "C.24"
  - "C.9"
  - "E.10"
  - "E.18"
  - "E.8"
  - "F.15"
  - "F.17"
  - "F.4"
  - "F.6"
  - "F.8"
  - "G.10"
  - "G.4"
  - "G.5"
  - "G.8"
  - "G.9"
keywords:
  - "autonomy budget"
  - "autonomy ledger"
  - "guarded enactment"
  - "override speech act"
  - "scout/probe/commit checkpoint"
---

### E.16:4 - Solution — **Rule‑of‑Constraints (RoC) for Autonomy**

This RoC **applies whenever** wording about a local system-role kind, Method, or Service claims that a System may perform Work involving unsupervised decision or actuation.

**E.16-S1 (Autonomy Budget - mandatory).**
Any autonomy claim **MUST** publish a named, versioned **AutonomyBudgetDecl**. A prospective declaration fixes what is being claimed and how later Work will be bounded; it does not pretend that a performer, assignment, Work item, or authority occurrence already exists. An action-bound declaration supplies the proposed-action and actual allocation references for A.21 permission to start. An enactment-bound declaration additionally refers to already admitted actual Work.

```
AutonomyBudgetDecl {
  id, version
  bindingState: prospective | action-bound | enactment-bound
  autonomyClaimRef: U.EpistemeRef
  budgetConsumerSystemRoleKindRef: U.KindRef        // exact local kind required for the Work
  workingSituation: plain statement of the intended Work and its admission condition
  applicablePolicyRef: PolicyIdRef
  scope: ClaimScope
  qualificationWindow: Γ_time
  budget: {                                          // all typed via MM-CHR (C.16)
    action_tokens?     : Unitful quota / rate
    decision_tokens?   : Unitful quota / rate
    risk_bands?        : CHR vector with acceptance bands
    resource_caps?     : set of unitful caps (Γ_work categories)
    time_window?       : Γ_time accounting window & cadence
  }
  AdmissibilityConditionsId: PolicyIdRef             // Aut-Guard policy naming gates & penalties
  overrideProtocolRef: U.EpistemeRef                  // SpeechActs for pause/resume/narrow/escalate
  overrideAuthority: {
    authorizedOverrideSystemRoleKindRef: U.KindRef
    authorityPolicyRef: PolicyIdRef
    authorityRelationOccurrenceRef?: U.EntityRef      // independently obtaining direct relation
    separationOfDutiesRelationRef: U.RelationRef      // exact A.2.7 incompatibility relation
  }
  actionBinding?: {
    workEntryClaimRef: U.EpistemeRef                  // prospective A.21 decision subject
    boundedProposedActionRef: governed action or WorkPlan/action locator
    proposedActionIdentityRuleRef: exact local rule, including rescheduling/continuation
    intendedWindow: bounded intended execution/allocation window
    budgetConsumerHolderSystemRef: U.EntityRef constrained to U.System
    budgetConsumerSystemRoleAssignmentRef: U.RelationRef constrained to U.SystemRoleAssignment
    overrideAuthorityHolderSystemRef: U.EntityRef constrained to U.System
    overrideAuthoritySystemRoleAssignmentRef: U.RelationRef constrained to U.SystemRoleAssignment
  }
  enactmentBinding?: {
    budgetConsumerHolderSystemRef: U.EntityRef constrained to U.System
    budgetConsumerSystemRoleAssignmentRef: U.RelationRef constrained to U.SystemRoleAssignment
    budgetedWorkRef: U.EntityRef constrained to U.Work
    overrideAuthorityHolderSystemRef: U.EntityRef constrained to U.System
    overrideAuthoritySystemRoleAssignmentRef: U.RelationRef constrained to U.SystemRoleAssignment
  }
  telemetrySpecRef?: U.EpistemeRef                     // what to emit into AutonomyLedger
  editionPins: { systemRoleKindRefs, MethodDescRef?, CHR refs, policy refs, ... }
}
```

An unscheduled `prospective` budget may omit actionBinding, enactmentBinding, nonexistent assignments and authority occurrences. Permission to start a scheduled action uses `action-bound` with its exact proposed action, work-entry claim, real holders/assignments and current independent authority. Use A.2.7's separately declared prospective incompatibility species for that allocation check. `enactment-bound` adds actual Work only after A.15.1 admission, retaining the applicable action/permission match. A request, schedule or pass result creates no Work. If authority rotates or a permission-relevant action/window changes, recheck before relying on the permission.

The holder Systems, local kinds, any separate System-classification judgments, assignment occurrences, Work, budget declaration, later override Work, authority relation, and separation-of-duties relation are different objects. A kind reference neither classifies a System nor creates an assignment; an assignment alone grants no authority.

**E.16‑S1.A (Scout / probe / commit partition for bounded specialization).**
When an autonomy-bearing method uses bounded specialization scouting, the budget declaration **MUST** keep scout budget, probe budget, and commit checkpoint as distinct control surfaces rather than collapsing them into one undifferentiated burn envelope. A successful probe does not by itself authorize a committed route, wider burn, or scope widening. Leaving probe state requires one explicit checkpoint decision through the declared guard or override path, with budget burn and residual budget recorded in the `AutonomyLedger`. `E.16` governs this budget partition plus guard and ledger enforcement; it does not replace the dyadic move of `A.15` or the `CheckpointReturn` plan semantics of `C.24`.
**E.16-S2 (Guarded enactment - Green-Gate).**
A Method step requiring autonomy **MUST** name the exact required local kind and `requiresAutonomyBudget: AutonomyBudgetDecl.id`. Green-Gate decides permission for the A.21 prospective work-entry claim and bounded action. It resolves:

* the action's artifact/subject, operation, target and intended window under its exact identity/continuation rule;
* the real prospective performer System and obtaining A.2.1 assignment whose holder/kind match the declaration, with the required A.2.5 state and any separate classification judgment;
* the actual authorizer/override-authority System and assignment, the applicable prospective incompatibility result, and the independent authority covering this action;
* applicable ClaimScope, qualification/accounting windows, remaining budget and every required guard.

A known prohibited allocation blocks the action before performance. Keep every required check present with its source outcome, including missing information, `unknown` or `notRun`, then apply the exact A.21 profile mapping. A required missing or unrun result may map only to `degrade` or `block` under an explicit rule; an unknown result retains its uncertainty and the policy-qualified consequence. Any accepted uncertainty must name its subject, tolerance, permitted bounded action, consequence and recheck/expiry condition. Reserve `abstain` for a gate that actually makes no decision and states the remaining decision route. Aggregate only after these mappings are known; a pass permits only the bounded action under the checked conditions. Resubmitting the same action changes no action identity. Rescheduling reopens window-sensitive permission even when the action-continuation rule preserves a continuing action. Work is admitted separately from actual performance history under A.15.1.

**E.16-S3 (Autonomy Ledger).**
Every actual Work item admitted under this budget **MUST** have an **AutonomyLedgerEntry**:

```
AutonomyLedgerEntry {
  entryKind: budgetedWork | overrideWork
  workRef: U.EntityRef constrained to U.Work
  performerSystemRef: U.EntityRef constrained to U.System
  performedUnderSystemRoleAssignmentRef: U.RelationRef constrained to U.SystemRoleAssignment
  budgetId, version, time
  deltas: { action_tokensΔ?, decision_tokensΔ?, riskΔ?, resourceΔ? }
  guardVerdicts: { name -> pass|fail }
  overrideAuthorityRelationOccurrenceRef?             // required for overrideWork
  separationOfDutiesCheckResultRef?                    // required for overrideWork
  pathIds: { PathId, PathSliceId }                     // for G-suite parity/refresh
}
```

Existing budget and performance records may supply this declaration and ledger when they retain the required meanings, identities and references; no duplicate accounting store is required. The ledger is evidence about actual Work. When prior permission is relied on, cite its exact result and the policy-supported match from this performance to the previously bounded action; a shared request label is insufficient. The Work, its performer System, its A.2.1 assignment, and the `performedUnderAssignment` attribution remain separately recoverable. For reporting, use **Γ_work** (B.1.6) for the recorded resource values under the applicable accounting and overlap policy, and **Γ_time** (B.1.4) for the recovered temporal relations among the Work occurrences.

**E.16-S4 (Overrides - SpeechActs, authority, and separation of duties).**
Every budget **MUST** reference an `overrideProtocolRef` that defines the available SpeechActs:

* **PauseAutonomy(budgetId)** - stop autonomy-gated steps immediately;
* **ResumeAutonomy(budgetId)** - resume after the required checks;
* **NarrowAutonomy(budgetId, Δscope)** - apply stricter limits;
* **Escalate(budgetId)** - hand over through the declared override-authority path.

The declaration names the exact A.2.7 incompatibility species and its predicate. Before a proposed pause, resume, narrowing or escalation, identify that bounded override action, its real holder/assignment and independent authority. The target navigation Work may already exist; the proposed override is not yet override Work. Apply the actual-Work species when its condition concerns the existing target Work, or the separately declared prospective species when the policy concerns allocation to the proposed override action. Resolve both actual assignments, holders, relevant subject identity, windows and applicability; reject a known prohibited joint allocation. Different labels or assignment IDs alone do not establish separation.

Check authority for the proposed override independently. Once the override is actually performed and admitted under A.15.1, record its `overrideWork` ledger entry and policy-specified zero, negative or other budget delta. Match that performance to prior permission by the policy's exact action rule. The proposal and its pass result remain distinct from that performed SpeechAct Work.

**E.16-S5 (Depletion behavior).**
When a budget depletes - no tokens remain, an envelope is exceeded, or a cap is breached:

* block further autonomy-gated steps in the same accounting window;
* emit a **DepletionNotice** SpeechAct and either **Escalate** or **Park** as the policy says; and
* reopen the gate only after an admitted System performs **ResumeAutonomy** under its exact override-authority assignment, the A.2.7 predicate check over both actual assignments passes, the independent authority relation is current, and the ordinary guards pass.

**E.16‑S6 (Publication in UTS).**
A UTS row that carries an autonomy claim about Work described through a local system-role kind, **Method**, **Service**, or **Selector** **MUST** include:

* `AutonomyBudgetDeclRef` (id and version) and `bindingState`;
* `Aut-Guard policy-id (PolicyIdRef)`;
* `OverrideProtocolRef`;
* declared **Scope (G)** and **Γ_time** window;
* edition pins for the referenced local system-role kind, Method, CHR, and policies; and, when action-bound, its proposed-action and real allocation refs; when enactment-bound, the additional actual Work refs needed by the receiving use.
* *(optional, if a scale preference is declared)* `ScaleLensPolicyRef` and `ScaleLensOptIn ∈ {OptedIn, Neutral, OptedOut}`.

**E.16‑S7 (Scale & selection — optional lens).**
When autonomy interacts with open‑ended search (C.18 and C.19), **budget consumption** and **guard violations** are **selection lenses** in Part G (G.5/G.9). Applying a **Scale‑Lens / Bitter‑Lesson** preference is **OPTIONAL**. Authors **MAY** declare a **ScaleLensPolicy** for the autonomy claim; when declared, it **MUST** state:
* **Trigger criteria** — evidence that expected utility‑of‑scale is monotonic/non‑saturating on held‑out tasks, and a threshold at which scaling beats structured heuristics.
* **Budget fit** — compute/latency/cost targets **within** the declared `AutonomyBudgetDecl` (Γ_time, resource_caps).
* **Safety invariants** — guards and SoD remain **non‑weakened** under scaling; no policy may bypass E.16 gates.
* **Fallback** — a degrade‑gracefully plan if scaling fails to clear the trigger criteria within budget.
If no **ScaleLensPolicy** is declared, selection remains **neutral** with respect to Bitter‑Lesson; RoC does **not** authorize ignoring scale‑safety guards under any policy.

