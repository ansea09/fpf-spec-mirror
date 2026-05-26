---
chunk_kind: "child"
pattern_id: "D.5"
pattern_title: "Bias-Audit & Ethical Assurance"
section_id: "D.5:6"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/D.5/D.5__007_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "D.5 — Bias-Audit & Ethical Assurance"
  - "D.5:6 — Common Anti-Patterns and How to Avoid Them"
line_start: 52204
line_end: 52211
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

### D.5:6 - **Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It (Conceptually) |
| :--- | :--- | :--- |
| **The "Ethics Ghetto"** | One person is the "ethics officer," and the rest of the engineering team sees bias as "not my job." | The **Rapid Scan (BA-1)** is a conceptual activity performed by a rotating member of the core team. This distributes the responsibility for ethical reflection across all roles. |
| **The "Checklist Charade"** | The team mechanically answers "yes/no" to bias questions just before a release, without any real reflection, simply to satisfy a process requirement. | The **Panel Review (BA-2)** is a moment of deep, multi-perspective critique that a perfunctory checklist cannot survive. The requirement for a structured **Bias-Audit Report** also forces concrete findings and mitigation methods, not just checkmarks. |
| **The "Bias Whack-a-Mole"** | The team fixes one bias issue, only for another to pop up, because they are only addressing symptoms. | The **Bias Taxonomy** encourages a more systematic approach. By considering categories like Representation (REP) and Metric Proxy (MET), the team is prompted to look for root causes (e.g., flawed data collection methods or poorly chosen objectives) rather than just patching individual algorithmic flaws. |

