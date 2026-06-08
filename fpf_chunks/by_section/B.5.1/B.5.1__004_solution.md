---
chunk_kind: "child"
pattern_id: "B.5.1"
pattern_title: "Explore → Shape → Evidence → Operate"
section_id: "B.5.1:3"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.1/B.5.1__004_solution.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "B.5.1 — Explore → Shape → Evidence → Operate"
  - "B.5.1:3 — Solution"
line_start: 33111
line_end: 33134
dependencies:
  - "B.5"
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

FPF defines a four-state development cycle model for any `U.Episteme` or `U.System` under development. That episteme or system transitions from one state to the next as it accumulates rigor and evidence. This state machine is driven by the **Canonical Reasoning Cycle** (Pattern B.5).

**The Four Development States:**

| State | Core Activity | Manager's View: What It Means | Driven by Phase of Reasoning Cycle | Typical `AssuranceLevel` |
| :--- | :--- | :--- | :--- | :--- |
| **1. Exploration** | **Generating possibilities.** The focus is on brainstorming, questioning assumptions, and generating multiple, often competing, hypotheses. | "We are in the 'what if' phase. All ideas are on the table. We are looking for a plausible path forward." | **Abduction** (Pattern B.5.2) | `L0` |
| **2. Shaping** | **Defining a single, coherent form.** The most promising hypothesis from the exploration phase is selected and given a rigorous, internally consistent structure. | "We've chosen our direction. Now we are building the blueprint, defining the architecture, and ensuring all the pieces fit together logically."| **Deduction** | `L0` → `L1` (if formalization counts as TA) |
| **3. Evidence** | **Testing against reality.** The shaped episteme or system is subjected to rigorous empirical or formal tests to validate its claims and measure its performance. | "The blueprint is done. Now we are at the proving ground. Does it actually work? We are running the tests and gathering the data." | **Induction** | `L1` → `L2` |
| **4. Operation** | **Deploying and monitoring in a live environment.** The validated episteme or system is put into production, where it performs its intended function and is monitored for ongoing reliability. | "It's live. The system is in service, delivering value, and we are monitoring its health and performance." | Continuous Induction (Monitoring) | `L2` (maintained) |

> **Didactic Note for Managers: Aligning States with Your Project Plan**
>
> This state machine is not an abstract theory; it maps directly to the familiar phases of any well-run project.
>
> *   **Exploration** is your R&D or initial discovery sprint.
> *   **Shaping** is your design and architecture phase.
> *   **Evidence** is your QA, testing, and V&V phase.
> *   **Operation** is the live deployment and maintenance phase.
>
> By using these four states, you can instantly communicate to your team and stakeholders exactly where the episteme or system is in its state transition, what the current focus is, and what needs to happen to move to the next stage.

