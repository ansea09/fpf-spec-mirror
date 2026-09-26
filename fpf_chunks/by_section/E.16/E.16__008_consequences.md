---
chunk_kind: "child"
pattern_id: "E.16"
pattern_title: "RoC‑Autonomy Budget & Enforcement"
section_id: "E.16:7"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/E.16/E.16__008_consequences.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "E.16 — RoC‑Autonomy Budget & Enforcement"
  - "E.16:7 — Consequences"
line_start: 90878
line_end: 90906
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

### E.16:7 - Consequences

* **Testability.** Budget use is checkable against declared tokens/envelopes; Work-anchored ledger entries support audit; **PauseAutonomy** stops autonomy-gated steps.
* **Comparability.** UTS surfaces autonomy metadata for fair selection & parity.
* **Safety.** Guards are hard gates; depletion halts further autonomy‑gated Work.

#### E.16:7.1 - SoTA-Echoing — bind a budget decision to the proposed action

**Practice question.** Is an existing release policy and error-budget ledger enough to permit an autonomous promotion or override? The selected line reuses those controls while checking the proposed action, current allocation and authority, available budget and applicable guards before performance. It then records the actual Work and consumption. A serious lighter alternative gates releases solely by the existing service-level error-budget policy and records their effects afterward. That is sufficient when the release policy already supplies every action/authority condition needed by the use.

The [Google SRE Workbook's Example Error Budget Policy, 2018](https://sre.google/workbook/error-budget-policy/) is the concrete comparator: its four-week budget can freeze changes, explicitly excepts P0/security fixes and supplies an escalation route. **Adopt** policy-bound depletion and explicit exception handling in S2, S4 and S5. **Adapt** the budget to the exact autonomous action and current authority in S1–S2, rather than inferring those facts from the remaining service budget. The cited example is a bounded release policy, not a general autonomy standard or proof of the completeness of a particular gate.

Show-B gives the decisive case: a release can be within its error budget while the required allocation overlap remains unknown. Budget-only permission would miss that unresolved premise; the explicit ReleaseEntryProfile-E1 blocks until it is established. A changed window reopens the affected permission, while S3 records consumption only after actual performance. Show-A adds a real pause/resume authority and depletion stop. The same existing policy, ledger and allocation records can supply these inputs; a second accounting system adds no value when their meanings and exact references are already present. The extra work is resolving a current action/allocation question, not copying the budget into another form.

**Reject** treating a declared pause interface as proof that a learning agent has no incentive to resist interruption. [Orseau and Armstrong's Safely Interruptible Agents, revised October 2016](https://intelligence.org/files/Interruptibility.pdf) supplies the distinct learning-theoretic question and results under stated agent and learning assumptions. It does not establish E.16's runtime enforcement or override authority. S4 requires an effective override path; any stronger incentive or learning claim needs its own applicable analysis. Scout/probe/commit partitioning in S1.A is a local budget-control rule, with no claim here that unnamed agentic-search research proves its effectiveness.

At comparable operational effort, the selected line wins only when an action-sensitive premise could change permission: it uses the same budget evidence and adds that check before harm can follow the proposed action. For a policy already covering it, reuse the existing decision and accounting basis while respecting their currentness. Reopen when the action rule, authority/allocation policy, budget window or override mechanism changes, or when evidence shows a bypass or a cheaper control retaining the same required distinctions. No error-budget policy, interface declaration or interruption theorem alone establishes general autonomous-system safety.

#### E.16:7.2 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Why it fails | Repair |
| --- | --- | --- | --- |
| **Autonomy-by-label** | “Autonomous” is claimed but there is no `AutonomyBudgetDecl` or ledger | Autonomy becomes opaque; cannot be audited or compared | Require **E.16‑S1/S3**; reject publication without `AutonomyBudgetDeclRef` + version |
| **Soft gates** | Budget/guards only warn; enactment proceeds anyway | Violates Safety and SoD; makes budgets non-enforceable | Make Green‑Gate **blocking** on Core surface (**E.16‑S2**) |
| **Self-override** | The actual consumer and override assignments are missing, or their holder, actual-Work or proposed-action identity under the selected species, and window facts match the prohibited joint-allocation case in the declared A.2.7 predicate. | A label pair or two different assignment IDs does not establish separation of duties. | Resolve both exact A.2.1 assignments, apply the declared incompatibility predicate, reject a prohibited pair, and check the independent authority relation (**E.16-S4**). |
| **Budget bypass via “scale”** | Scaling preference relaxes guards or ignores caps | Undermines declared limits; breaks comparability | In ScaleLensPolicy, **guards/SoD must remain non‑weakened** (**E.16‑S7**) |
| **Untyped quotas** | Tokens/caps are recorded without units, or units are mixed | Ledger becomes non-comparable; audits become meaningless | Type budgets and deltas via **MM‑CHR (C.16)**; keep unitful rates/quotas |
| **Ledger-as-logging** | Logs exist but are not Work‑anchored (no workRef/budgetId/version or recoverable edition pins) | Evidence is non-portable; cannot support parity/refresh | Require `AutonomyLedgerEntry` attached to `U.Work` with workRef, budgetId, version, and the referenced declaration's edition pins |

