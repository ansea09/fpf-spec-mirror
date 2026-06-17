---
chunk_kind: "child"
pattern_id: "D.5"
pattern_title: "Bias-Audit & Ethical Assurance"
section_id: "D.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/D.5/D.5__005_solution.md"
commit_sha: "646b0b9b164f7c13258633a33b92d2d0a569da28"
heading_path:
  - "D.5 — Bias-Audit & Ethical Assurance"
  - "D.5:4 — Solution"
line_start: 56899
line_end: 56993
dependencies:
  - "B.3"
  - "B.3.3"
  - "C.28"
  - "E.5.4"
keywords:
  - "AI ethics"
  - "assurance"
  - "audit"
  - "bias"
  - "ethics"
  - "fairness"
  - "responsible AI"
  - "review cycle"
  - "taxonomy"
---

### D.5:4 - **Solution**

FPF introduces the **Bias-Audit Cycle (BA-Cycle)**, a lightweight, iterative review loop designed to integrate ethical reflection directly into the engineering development cycle. It is not a one-time gate but a continuous loop of inquiry.

#### D.5:4.1 - The Bias-Audit Cycle: Four Phases

The cycle consists of four distinct phases, aligned with the project's natural rhythm.

| Phase | Trigger | Core Activity | Output |
| :--- | :--- | :--- | :--- |
| **BA-0: Kick-off** | Project start or major new feature. | **Framing the ethical scope.** The team identifies potential areas of bias and creates an initial, living document called the **Bias Register**. | A skeleton Bias Register with initial questions. |
| **BA-1: Rapid Scan**| End of each sprint or design session. | **Continuous lightweight check.** A rotating member of the core team (the *Engineer-Scrutineer*) quickly scans recent changes against a checklist, flagging potential issues in the Bias Register. | Updated Bias Register with new items flagged for discussion. |
| **BA-2: Panel Review**| Before a major integration or release decision (e.g., before moving to the `Evidence` state). | **Deep, multi-perspective critique.** A small panel, including individuals in roles like **Ethicist**, **Domain Sociologist**, and **UX Design Critic**, reviews the flagged items and proposes concrete mitigations. | A structured, auditable record called the **Bias-Audit Report**, documenting findings and required actions. |
| **BA-3: Closure** | At the release freeze. | **Ensuring accountability.** The facilitator confirms that all "blocking" issues from the Bias-Audit Report have either been resolved or have a documented, accepted risk. | The final Bias-Audit Report is marked as *resolved* or *risk-accepted* for that release. |

#### D.5:4.2 - The Bias Taxonomy: A Shared Language for Critique

To structure the audit, FPF provides a minimal, extensible taxonomy of common bias categories.

| Code | Bias Category | Manager's View: The Simple Question to Ask |
| :--- | :--- | :--- |
| **REP** | **Representation Bias** | "Whose voice, data, or perspective is missing from this model?" |
| **ALG** | **Algorithmic Bias** | "Could our automated rule or formula unintentionally amplify unfairness for minority or edge cases?" |
| **VIS** | **Visual Framing Bias** | "Does this diagram, color choice, or dashboard visualization steer the user towards a preferred conclusion?" |
| **MET** | **Metric Proxy Bias** | "Are we chasing a metric that is easy to measure, at the expense of the real, harder-to-measure objective?" (Connects to ADR-015) |
| **LNG** | **Lexical Bias** | "Do our naming choices (e.g., 'master/slave', 'blacklist/whitelist') encode unintended value judgments or historical baggage?" |

> **Didactic Note for Managers: This is Risk Management, Not a Philosophy Seminar**
>
> The Bias-Audit Cycle is FPF's "immune system." It's designed to find and neutralize hidden assumptions before they become costly product failures or public relations disasters. Think of it like a security audit, but for the ethical and social integrity of your system.
>
> *   **It's not about being "perfect"; it's about being "aware."** The goal is not to eliminate all bias (an impossible task) but to make your team's biases explicit, documented, and consciously managed.
> *   **It's cost-effective.** The lightweight "Rapid Scan" catches most issues early, during a sprint. The more intensive "Panel Review" is reserved for key moments, ensuring that expert time is used efficiently.
> *   **It creates a defensible record.** The Bias-Audit Reports provide a clear, auditable trail showing that your team has taken a systematic and responsible approach to identifying and mitigating potential harms. In an era of increasing scrutiny on AI and autonomous systems, this record is not just good practice—it's a critical business asset.

#### D.5:4.3 - Normative Artifacts

The Bias-Audit Cycle produces two key records that serve as the auditable record of ethical deliberation.

*   **The Bias Register:**
    *   **Nature:** A living, evolving **episteme** that serves as a repository of questions, concerns, and potential biases identified throughout a holon's evolution.
    *   **Content:** It is a structured collection of inquiries, organized by the Bias Taxonomy (REP, ALG, etc.). It is continuously updated during the Rapid Scans (BA-1) and represents the "running log" of ethical and bias-related considerations for the project.

*   **The Bias-Audit Report:**
    *   **Nature:** A formal, versioned **episteme** that documents the findings of the Panel Review (BA-2).
    *   **Content:** It contains a structured record of findings. Each finding is a `U.Episteme` with attributes for:
        *   `biasCode`: The category from the Bias Taxonomy.
        *   `severity`: An ordinal level (`high`, `medium`, `low`).
        *   `description`: A narrative explaining the issue.
        *   `mitigation`: A proposed `U.Method` or `U.ConstraintRule` to address the issue.
        *   `status`: A state (`blocking`, `resolved`, `risk-accepted`).
    *   **Conceptual Example:**
        *   `finding-01`: An episteme with `biasCode: REP`, `severity: high`, and a `description` stating that the training data for a recognition holon lacks representation from certain demographics. The `mitigation` would be a `U.Method` for acquiring a balanced dataset, and the `status` would be `blocking` until this method is executed and its outcome validated.

#### D.5:4.4 - Causal fairness use audit

When a fairness claim is causal rather than metric-only, `D.5` records the ethical-audit question and cites `C.28` for causal-use support:

```text
CausalFairnessUseAuditCard {
  causalUseQuestionRef: U.CausalUseQuestion
  protectedVariableRef
  decisionVariableRef
  outcomeVariableRef
  fairnessCausalityLadderRung: CausalityLadderRung
  fairnessEstimandRef: U.CausalEstimand
  permittedPathSet?
  prohibitedPathSet?
  pathSpecificFairnessEstimandRef?
  pathSpecificExcessLossRef?
  comparatorOrCounterfactualRef
  causalEvidenceSupportBasis: CausalEvidenceSupportBasis
  causalIdentificationProfileRef?
  counterfactualSamplingRealizabilityProfileRef?
  causalUseEvidenceDesignRef?
  causalUseSupportRecordRef?
  causalUseSupportVerdict: CausalUseSupportVerdict
  fairnessCausalEthicalConstraintRef?
  supportedFairnessUse
  unsupportedFairnessUse
}
```

Metric-only fallback: if only a metric disparity is claimed and no causal fairness use is made, record it as metric/evaluation use, not `C.28`-heavy causal fairness.

Local causal-fairness repair does not by itself trigger the full Bias-Audit Cycle, a panel review, or release-cycle duties. It may only downgrade causal wording, add the missing `C.28` support reference, or mark unsupported causal fairness use.

The full `D.5` duties activate under `D.5` project or release conditions: the holon, model, metric, decision system, policy, or authored claim may materially affect people or groups; the fairness/ethical claim is release-bearing; or the local causal-fairness repair becomes an input to audit, assurance, deployment, publication, or risk acceptance.

Fairness escalation rule: interventional-action proxy may support bounded interventional fairness use but cannot be published as counterfactual fairness.

What changes in practice: a fairness audit must say whether the claim is associative, interventional, or counterfactual, and a counterfactual fairness claim must carry the causal-use question, comparator/counterfactual, permitted paths, prohibited paths, causal evidence support basis, causal identification or counterfactual sampling realizability, causal-use support verdict, and supported fairness use and unsupported fairness use.

What this does not authorize: `D.5` does not replace `C.28` for causal-use question, causality-ladder rung, estimand, identification, realizability, or `CausalUseSupportVerdict`; it keeps ethical audit and fairness assurance, while `B.3` keeps assurance claim support and non-admissible-use consequences.

