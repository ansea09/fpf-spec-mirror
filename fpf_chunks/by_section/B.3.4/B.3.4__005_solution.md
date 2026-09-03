---
chunk_kind: "child"
pattern_id: "B.3.4"
pattern_title: "Evidence Decay & Epistemic Debt"
section_id: "B.3.4:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.4/B.3.4__005_solution.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "B.3.4 — Evidence Decay & Epistemic Debt"
  - "B.3.4:4 — Solution"
line_start: 39971
line_end: 40027
dependencies:
  - "A.10"
  - "B.3"
  - "B.3.3"
  - "B.4"
keywords:
  - "decay"
  - "epistemic debt"
  - "evidence aging"
  - "freshness"
  - "stale data"
---

### B.3.4:4 - **Solution**

FPF introduces a formal freshness model and a governance loop that make evidence aging a first-class, manageable property of the assurance calculus.

#### B.3.4:4.1 - The Principle of Perishable Evidence

The core of the solution is a new normative principle: **Evidence is perishable**. The relevance of any piece of evidence is a function of time and context. An `AssuranceLevel` is therefore not a permanent achievement but a state that must be actively maintained.

#### B.3.4:4.2 - Mechanism 1: The Freshness Standard (`valid_until`)**

Every evidence carrier anchored in the Assurance Layer **MUST** carry a `valid_until` attribute.

*   **`valid_until: ISO-8601-date | null`**
*   This attribute acts as a "best before" date, explicitly stating the time horizon over which its creators consider it to be fully relevant without review.
*   A value of `null` signifies that the evidence is considered **perpetual**. This is reserved for evidence carriers such as mathematical axioms or fundamental physical laws whose validity is not expected to decay on engineering timescales.

#### B.3.4:4.3 - Mechanism 2: The Epistemic Debt Metric (ED)

When the current time `t` surpasses an evidence carrier's `valid_until` date, that evidence carrier begins to accrue **Epistemic Debt (ED)**.

*   **Definition:** Epistemic Debt is a quantitative measure of an evidence carrier's "staleness." It is a function of its age past its expiry date.
*   **Purpose:** ED is not a penalty but a **signal**. It makes the invisible risk of relying on old evidence visible and measurable.

#### B.3.4:4.4 - Mechanism 3: The Governance Loop (`Refresh / Deprecate / Waive`)

Epistemic Debt is managed through a project-level **epistemic_debt_budget**. When the total accrued debt exceeds this budget, an alert is triggered, and the team **MUST** take one of three actions:

| Action | What It Means | Manager's View: The Practical Consequence |
| :--- | :--- | :--- |
| **Refresh** | Produce new, up-to-date evidence and set a new `valid_until` date. | **"We invest the resources to re-validate."** This is the engineering fix: run the tests again, update the model, re-certify the component. |
| **Deprecate**| Acknowledge that the evidence is no longer valid and formally downgrade the `AssuranceLevel` of the dependent assurance target (typically to `L0` or `L1`). | **"We accept the risk by lowering the component's official status."** The component is no longer considered fully assured and may be flagged for restricted use until it is refreshed. |
| **Waive** | A designated authority (e.g., a senior systems engineer or a safety officer) formally accepts the risk of using the stale evidence for a limited time. | **"I am signing off on this risk, for now."** This is a temporary, auditable override. It keeps the project moving but makes the risk acceptance explicit and assigns responsibility. |

> **Didactic Note for Managers: Managing Your "Trust Budget"**
>
> Think of Epistemic Debt exactly like financial or technical debt. It’s not inherently evil, but it must be managed. The FPF dashboard now includes a "Trust Health" meter.
>
> *   **Green:** Your evidence is fresh. Your assurance case is solid.
> *   **Amber:** Epistemic Debt is accumulating. It's time to plan for re-validation work in the next sprint.
> *   **Red:** Your debt has exceeded its budget. Your CI/CD pipeline might be issuing warnings, and you are now carrying un-budgeted risk. You must immediately decide: **Pay it down (Refresh), write it off (Deprecate), or take out a short-term, high-visibility loan (Waive).**
>
> This loop transforms the vague problem of "keeping things up to date" into a concrete, resource-managed, and auditable engineering process.

#### B.3.4:4.5 - Mechanism 4: The Epistemic Debt (ED) Calculation & Aggregation**

To make ED a useful leading indicator, it must be computed and aggregated consistently.

*   **Calculation:** For a single evidence carrier `i`, its debt at time `t` is a function of its age past expiry:
    `ED_t(i) = k * max(0, t - valid_until_i)`
    *   The coefficient `k` is a configurable linear decay factor (default: `1.0 per day`), allowing projects to tune the "interest rate" on their debt.

*   **Aggregation:** The total ED for an assurance target `A` is the sum of the debt from all its direct and transitive Evidence Graph Ref:
    `ED_t(A) = Σ_i ED_t(evidence_i)`
    *   This rule ensures that debt propagates up the holarchy. If a foundational component's validation expires, the entire system that depends on it inherits that debt.

*   **Impact on Assurance Level:** When an assurance target's total `ED_t(A)` exceeds a defined threshold (typically `> 0` unless waived), its computed `AssuranceLevel` is **provisionally downgraded by one level**. For example, an `L2` assurance target with expired evidence is treated as `L1` for governance and risk purposes until the debt is resolved. This makes the consequence of inaction immediate and visible on project dashboards.

