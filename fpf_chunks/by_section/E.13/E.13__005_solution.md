---
chunk_kind: "child"
pattern_id: "E.13"
pattern_title: "Pragmatic Utility & Value Alignment"
section_id: "E.13:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.13/E.13__005_solution.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "E.13 — Pragmatic Utility & Value Alignment"
  - "E.13:4 — Solution"
line_start: 54636
line_end: 54666
dependencies:
  - "E.12"
  - "E.2"
keywords:
  - "Goodhart's Law"
  - "MVE"
  - "Proxy-Audit Loop"
  - "pragmatic"
  - "utility"
  - "value"
---

### E.13:4 - **Solution**

FPF elevates **Pragmatic Utility (Pillar P-7)** to a normative architectural principle, operationalized through two mandatory conceptual mechanisms.

#### E.13:4.1 - The Principle of Pragmatic Utility (Expanded Definition)

Any holon or episteme created within FPF is an instrument for achieving a specific, pragmatic `U.Objective`. The value of that holon or episteme is determined solely by its **utility** in achieving that objective, not by its epistemic scores in isolation.

#### E.13:4.2 - Mechanism 1: The Proxy-Audit Loop

To formally manage the risk of Goodhart's Law, FPF introduces a conceptual feedback loop to periodically review the alignment between proxy characteristics and their intended goals.

*   **New Normative Relation:** A new relation, `isProxyFor: U.Characteristic → U.Objective`, is introduced. This relation **MUST** be used to explicitly declare when a measurable characteristic is serving as a proxy for an often qualitative `U.Objective`.
*   **Conceptual Audit Process:** Any characteristic marked with the `isProxyFor` relation is subject to a **periodic conceptual audit**.
*   **Review Roles:** This audit is conceptually performed by the individual(s) in the **`Strategist`** role. They are tasked with answering the question: *"Is optimizing for this proxy still reliably driving progress toward the actual `U.Objective` it represents, or have we observed a divergence?"*
*   **Output Concept:** If a divergence is identified, a high-priority `U.Method` for revising or replacing the proxy **MUST** be proposed.

> **Didactic Note for Managers: Are You Climbing the Right Mountain?**
>
> The Proxy-Audit Loop is your compass. Your team's dashboards might show all green—metrics are improving, targets are being hit. But the audit loop forces a crucial question: "Are these the *right* metrics?"
>
> Imagine you are trying to improve "customer satisfaction" (`U.Objective`). You choose "average call handle time" as a proxy metric. Your team successfully drives this number down. But the Proxy-Audit reveals that customer satisfaction is actually *decreasing* because agents are rushing and providing poor service to meet the time target. The loop forces you to recognize this divergence and find a better proxy (e.g., "first-call resolution rate"). It ensures your team is not just climbing fast, but climbing the right mountain.

#### E.13:4.3 - Mechanism 2: The Minimally Viable Example (MVE) Mandate

To enforce a pragmatic, value-first approach from the very beginning of a project, any new `U.System` or major system component **MUST** begin its development cycle with the creation of a **Minimally Viable Example (MVE)**.

*   **Definition:** An MVE is a simple, end-to-end, working instance of the holon that demonstrates the achievement of at least one core, user-facing objective, however trivial. It is the FPF equivalent of a "Hello, World" for a complex system.
*   **Assurance Requirement:** The MVE **MUST** achieve a minimum of **`AssuranceLevel:L1 (Substantiated)`**. This means the MVE cannot be a mere mock-up or a purely conceptual sketch; it must be supported by at least one piece of tangible evidence (e.g., a passing test case, a formal assertion), as defined in Pattern B.3.3.
*   **Stege transition Precedence:** The development of the full-scale holon cannot proceed to `AssuranceLevel:L2` until the MVE has been created and has met its L1 requirement.

