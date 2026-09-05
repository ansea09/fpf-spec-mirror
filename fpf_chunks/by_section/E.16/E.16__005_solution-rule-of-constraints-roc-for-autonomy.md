---
chunk_kind: "child"
pattern_id: "E.16"
pattern_title: "RoC‑Autonomy Budget & Enforcement"
section_id: "E.16:4"
section_title: "Solution — Rule‑of‑Constraints (RoC) for Autonomy"
source_path: "FPF-Spec.md"
output_path: "by_section/E.16/E.16__005_solution-rule-of-constraints-roc-for-autonomy.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "E.16 — RoC‑Autonomy Budget & Enforcement"
  - "E.16:4 — Solution — Rule‑of‑Constraints (RoC) for Autonomy"
line_start: 81229
line_end: 81347
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
Any autonomy claim **MUST** publish a named, versioned **AutonomyBudgetDecl**. A prospective declaration fixes what is being claimed and how later Work will be bounded; it does not pretend that a performer, assignment, Work item, or authority occurrence already exists. An enactment-bound declaration supplies those actual references before the Green-Gate admits Work.

```
AutonomyBudgetDecl {
  id, version
  bindingState: prospective | enactment-bound
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

In `prospective` state, `enactmentBinding` and `authorityRelationOccurrenceRef` may be absent. Before actual Work is admitted, publish or select an `enactment-bound` edition with every field in `enactmentBinding` and a current authority-relation occurrence. If the override authority rotates, refresh that binding before relying on it. Do not create an assignment or authority occurrence merely to fill the declaration.

The holder Systems, local kinds, any separate System-classification judgments, assignment occurrences, Work, budget declaration, later override Work, authority relation, and separation-of-duties relation are different objects. A kind reference neither classifies a System nor creates an assignment; an assignment alone grants no authority.

**E.16‑S1.A (Scout / probe / commit partition for bounded specialization).**
When an autonomy-bearing method uses bounded specialization scouting, the budget declaration **MUST** keep scout budget, probe budget, and commit checkpoint as distinct control surfaces rather than collapsing them into one undifferentiated burn envelope. A successful probe does not by itself authorize a committed route, wider burn, or scope widening. Leaving probe state requires one explicit checkpoint decision through the declared guard or override path, with budget burn and residual budget recorded in the `AutonomyLedger`. `E.16` governs this budget partition plus guard and ledger enforcement; it does not replace the dyadic move of `A.15` or the `CheckpointReturn` plan semantics of `C.24`.
**E.16-S2 (Guarded enactment - Green-Gate).**
A **Method step** that requires autonomy **MUST** list the exact required local system-role kind and `requiresAutonomyBudget: AutonomyBudgetDecl.id`. A **Work** instance is admissible only when the declaration is `enactment-bound` and the gate has resolved the actual values rather than inferred them from labels:

* `budgetConsumerHolderSystemRef` identifies the performer System, and `budgetConsumerSystemRoleAssignmentRef` resolves to the exact obtaining A.2.1 assignment whose holder and assigned kind match the declaration;
* `budgetedWorkRef` is the Work now being admitted and matches the declared working situation, ClaimScope, and qualification window;
* the assignment is in an enactable A.2.5 state; any separate classification judgment required by the gate is checked separately;
* the named override-authority System and assignment are current, and the independent authority relation covers the override Work allowed by the protocol;
* the budget ledger shows tokens and limits remaining for this declaration in the accounting window; and
* every guard in `AdmissibilityConditionsId` passes.

Failing any gate blocks enactment. Missing actual bindings remain missing; they are not repaired by turning a prospective declaration into fictional Work or assignment data.

**E.16-S3 (Autonomy Ledger).**
Every admitted Work item **MUST** have an **AutonomyLedgerEntry**:

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

The ledger is evidence about the Work. The Work, its performer System, its A.2.1 assignment, and the `performedUnderAssignment` attribution remain separately recoverable. Fold the resulting entries under **Γ_work** and **Γ_time** for reporting.

**E.16-S4 (Overrides - SpeechActs, authority, and separation of duties).**
Every budget **MUST** reference an `overrideProtocolRef` that defines the available SpeechActs:

* **PauseAutonomy(budgetId)** - stop autonomy-gated steps immediately;
* **ResumeAutonomy(budgetId)** - resume after the required checks;
* **NarrowAutonomy(budgetId, Δscope)** - apply stricter limits;
* **Escalate(budgetId)** - hand over through the declared override-authority path.

The declaration names the exact A.2.7 incompatibility relation between the consumer and override-authority local kinds. At each override, the checking System separately resolves the two exact A.2.1 assignment occurrences, their holder Systems, the target Work, and their overlap window, then applies that relation's declared predicate. The override fails when the actual pair satisfies the predicate's prohibited joint-allocation case. Different labels or merely different assignment IDs do not prove separation of duties.

The same check independently confirms that the declared direct authority relation currently authorizes the override Work. Neither the local kind, assignment, policy name, nor incompatibility relation supplies that authority by itself. Every override SpeechAct is Work and receives an `overrideWork` ledger entry, including zero or negative budget deltas as the policy specifies.

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
* edition pins for the referenced local system-role kind, Method, CHR, and policies; and, when enactment-bound, the actual binding references needed by the receiving use.
* *(optional, if a scale preference is declared)* `ScaleLensPolicyRef` and `ScaleLensOptIn ∈ {OptedIn, Neutral, OptedOut}`.

**E.16‑S7 (Scale & selection — optional lens).**
When autonomy interacts with open‑ended search (C.18 and C.19), **budget consumption** and **guard violations** are **selection lenses** in Part G (G.5/G.9). Applying a **Scale‑Lens / Bitter‑Lesson** preference is **OPTIONAL**. Authors **MAY** declare a **ScaleLensPolicy** for the autonomy claim; when declared, it **MUST** state:
* **Trigger criteria** — evidence that expected utility‑of‑scale is monotonic/non‑saturating on held‑out tasks, and a threshold at which scaling beats structured heuristics.
* **Budget fit** — compute/latency/cost targets **within** the declared `AutonomyBudgetDecl` (Γ_time, resource_caps).
* **Safety invariants** — guards and SoD remain **non‑weakened** under scaling; no policy may bypass E.16 gates.
* **Fallback** — a degrade‑gracefully plan if scaling fails to clear the trigger criteria within budget.
If no **ScaleLensPolicy** is declared, selection remains **neutral** with respect to Bitter‑Lesson; RoC does **not** authorize ignoring scale‑safety guards under any policy.

