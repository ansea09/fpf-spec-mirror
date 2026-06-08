---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti‑Explosion Control (Roles & Statuses)"
section_id: "F.14:2"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__003_problem-frame.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "F.14 — Anti‑Explosion Control (Roles & Statuses)"
  - "F.14:2 — Problem frame"
line_start: 73788
line_end: 73799
dependencies:
  - "F.1"
  - "F.10"
  - "F.11"
  - "F.12"
  - "F.13"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.7"
  - "F.8"
keywords:
  - "bundles"
  - "guard-rails"
  - "reuse"
  - "separation-of-duties"
  - "vocabulary growth"
---

### F.14:2 - Problem frame

Left unchecked, Role and Status vocabularies tend to **diverge**:

1. **Synonym stacks.** *Reviewer*, *Approver*, *Validator*, *Verifier* minted separately despite overlapping responsibilities.
2. **Modifier creep.** *Night‑Operator*, *Shift‑Operator*, *Remote‑Operator* proliferate where one Role plus a window would suffice.
3. **SoD leakage.** New names invented to **evade** an intended separation (*Requestor‑Approver* as one Role).
4. **Status paintjobs.** *Compliant*, *At‑Risk*, *Grace*, *Waived*, *Temporarily‑Breached*—labels multiply where a **single Status × window** model would be clearer.
5. **Context blending.** A control‑Context *Actuator* gets treated as an Enactment *Execution* Role; a deontic *Duty* becomes a runtime *Status*.

Explosion harms didactics and increases alignment cost (F.9).

