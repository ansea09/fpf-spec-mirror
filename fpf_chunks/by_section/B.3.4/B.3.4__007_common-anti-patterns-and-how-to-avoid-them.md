---
chunk_kind: "child"
pattern_id: "B.3.4"
pattern_title: "Evidence Decay & Epistemic Debt"
section_id: "B.3.4:6"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.4/B.3.4__007_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "7ba40a95a967ca5c69afc63aeca381e6adedc8da"
heading_path:
  - "B.3.4 — Evidence Decay & Epistemic Debt"
  - "B.3.4:6 — Common Anti-Patterns and How to Avoid Them"
line_start: 39315
line_end: 39322
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

### B.3.4:6 - **Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It |
| :--- | :--- | :--- |
| **The "Perpetual Evidence" Fallacy** | "We verified this component five years ago, so it's still L2. It's just a simple library, nothing has changed." | **CC-ED.1** forces a `valid_until` date. The context (compiler versions, new vulnerabilities, OS updates) has certainly changed. Setting `valid_until: null` requires explicit justification that the evidence carrier is truly timeless, like a mathematical theorem. |
| **The "Invisible Debt" Trap** | A critical component test suite has been failing silently for months, but the system dashboard is still green. | **CC-ED.3** ensures that the debt from the failing component's expired evidence propagates up to the system level, turning the dashboard amber or red and forcing attention. |
| **The "Risk Acceptance by Silence"** | "We know those tests are stale, but we're too busy to fix them. Let's just ignore the warnings for now." | **CC-ED.5** makes risk acceptance an explicit, auditable action. A manager must formally `Waive` the debt, putting their name on the decision. This transforms passive neglect into active, accountable risk management. |

