---
chunk_kind: "child"
pattern_id: "B.2.4"
pattern_title: "Meta-Functional Transition (MFT)"
section_id: "B.2.4:7"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.4/B.2.4__008_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "B.2.4 — Meta-Functional Transition (MFT)"
  - "B.2.4:7 — Common Anti-Patterns and How to Avoid Them"
line_start: 30300
line_end: 30307
dependencies:
  - "A.3.1"
  - "B.2"
  - "B.2.1"
keywords:
  - "adaptive workflow"
  - "capability emergence"
  - "functional emergence"
  - "new process"
---

### B.2.4:7 - **Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It (Conceptually) |
| :--- | :--- | :--- |
| **The "Process on Paper" Fallacy** | A team creates a beautiful, complex workflow diagram (`MethodDescription`) but continues to operate in the old, siloed way. The new capability exists only in documentation. | An MFT is a transition in **operational reality** (`U.Method` enactment), not just in `design-time` artifacts (`MethodDescription`). **CC-B2.4.1** requires evidence for the B-O-S-C triggers, which are based on observed behavior, not just documented intent. |
| **The "Micromanaging Supervisor"** | A new "meta-process" is introduced, but it's just a manager manually coordinating the old, separate steps. There is no new, emergent logic or automation. | **CC-B2.4.3** requires the supervisory function to be modeled as an explicit mechanism with `controls` relations. If the "supervisor" is just a person doing the same old coordination, no new, persistent `U.Method` has emerged. |
| **The "Capability by Fiat"** | A leader declares that a new, integrated capability now exists, but the underlying methods, tools, and objectives of the team have not actually changed. The "synergy" is aspirational. | An MFT is an observable, bottom-up phenomenon. The B-O-S-C triggers provide a falsifiable checklist. If there is no new boundary, no new objective, and no new supervisory loop, no MFT has occurred, regardless of declarations. |

