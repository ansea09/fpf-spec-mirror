---
chunk_kind: "child"
pattern_id: "B.5.1"
pattern_title: "Explore → Shape → Evidence → Operate"
section_id: "B.5.1:3"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.1/B.5.1__004_solution.md"
commit_sha: "a87d0ef4f3712507edd6e5a59f4de5bf7a55905a"
heading_path:
  - "B.5.1 — Explore → Shape → Evidence → Operate"
  - "B.5.1:3 — Solution"
line_start: 41022
line_end: 41042
dependencies:
  - "B.3.3"
  - "B.4"
  - "B.5"
  - "B.5.2"
keywords:
  - "Evidence"
  - "Explore"
  - "Operate"
  - "Shape"
  - "development state cycle"
  - "open-ended progression"
  - "state machine"
---

### B.5.1:3 - **Solution**

Use the four development states to name the current focus for the episteme or system under development. For an intended transition, identify the design, evidence and operational conditions that actually need to hold. The Canonical Reasoning Cycle (B.5) can supply the relevant reasoning contributions; the state names do not prescribe an assurance ladder.

**The Four Development States:**

| State | Core Activity | Manager's View: What It Means | Reasoning Contribution | What the state leaves to the receiving claim and use |
| :--- | :--- | :--- | :--- | :--- |
| **1. Exploration** | **Generating possibilities.** Frame the problem and compare candidate explanations or designs. | "We are looking for a plausible direction and keeping the serious alternatives visible." | **Abduction** (B.5.2) | A qualified conjecture may be sufficient for the present question; its origin does not assign `L0`. |
| **2. Shaping** | **Defining a coherent form.** Develop the selected direction and derive its relevant consequences. | "We are making the design and its implications clear enough for the next intended use." | **Deduction** | Logical support concerns the consequence under its premises. A coherent design alone does not establish actual performance. |
| **3. Evidence** | **Evaluating the relevant claims.** Use applicable empirical or formal results and obtain missing evidence when it is required and feasible. | "We are deciding whether the needed claims are supported in the intended conditions." | **Empirical evaluation and applicable formal reasoning** | Relevant existing support can be sufficient. A passed test does not automatically confer a higher assurance level. |
| **4. Operation** | **Using in a live environment.** Begin or continue the intended operation and monitor what its actual conditions require. | "The system or episteme is in use, with the required operational conditions in place." | **Reasoning about operating observations and needed changes** | Readiness and continuing use depend on the actual qualification, protective and authority conditions, not maintained `L2`. |

B.3.3 governs any assurance conclusion about the particular claim and receiving use. Retain an applicable domain profile, proof obligation or validation requirement where that use requires it. Existing results count only when they cover the present conditions; a missing required result can block the intended transition. A proposal to improve an excessive requirement does not waive a currently binding condition.

> **Didactic Note for Managers: Aligning States with Your Project Plan**
>
> Exploration can describe discovery, Shaping design, Evidence evaluation, and Operation live use and maintenance. Name the subject and the intended transition so that the team can tell what remains to be done. Completing a useful answer during Exploration does not mean that the developed system has entered Operation, nor that the answer must wait for every later project state.

**Worked case.** A service team completes B.5.2's latency-spike inquiry with a qualified backup-interaction conjecture and live rivals. The possible causal probe is unavailable, so the explanatory result remains limited. An existing operational qualification separately supports a permitted diversion to a spare instance for this traffic and interval. The team can use that basis for the diversion without declaring the explanation validated or advancing a new design through Evidence. If the team instead proposes a new deployment whose required load test is missing, that deployment remains blocked; the useful conjecture does not supply the missing qualification.

