---
chunk_kind: "child"
pattern_id: "F.11"
pattern_title: "Method Quartet Harmonisation"
section_id: "F.11:2"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/F.11/F.11__003_problem-frame.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "F.11 — Method Quartet Harmonisation"
  - "F.11:2 — Problem frame"
line_start: 72851
line_end: 72859
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.3"
  - "A.3.1"
  - "A.3.2"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.10"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.9"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Work"
keywords:
  - "Actuation"
  - "Method"
  - "MethodDescription"
  - "Role–Method–Work alignment"
  - "Work"
---

### F.11:2 - Problem frame

When Method, MethodDescription, Work, and Actuation **collapse into one another**, models drift:

1. **DesignRunTag blur.** A BPMN *process* (design graph) is cited as if it had *happened*.
2. **Recipe/approval fallacy.** An *approved* SOP (MethodDescription) is treated as proof that the service met its SLO.
3. **Execution ≟ control.** PLC *task execution* logs are conflated with *control outputs* (actuation), hiding stability issues.
4. **Cross‑context homonymy.** *Activity, task, execution, process, command* change sense across Contexts; inferences quietly break.

