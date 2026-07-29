---
chunk_kind: "child"
pattern_id: "F.11"
pattern_title: "Method Quartet Harmonisation"
section_id: "F.11:10"
section_title: "Anti‑patterns & remedies"
source_path: "FPF-Spec.md"
output_path: "by_section/F.11/F.11__011_anti-patterns-remedies.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "F.11 — Method Quartet Harmonisation"
  - "F.11:10 — Anti‑patterns & remedies"
line_start: 92018
line_end: 92034
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

### F.11:10 - Anti‑patterns & remedies

| #       | Anti‑pattern                   | Symptom in prose/models                                               | Why it harms thinking                                                       | Remedy (conceptual move)                                                                                                                                                                                             |
| ------- | ------------------------------ | --------------------------------------------------------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A1**  | **Design→Run Substitution**    | “The process **achieved** X” while pointing to a design diagram.      | Treats a **MethodDescription** as if it were **Work**; collapses stances.           | Apply the **stance split**: restate as “The **diagram describes** how X **should** be achieved.” To claim it **happened**, reference a **Work** SenseCell in a run‑time Context and, if needed, add a **Window** (F.10). |
| **A2**  | **Approval = Evidence**        | “Approved SOP ⇒ requirement satisfied.”                               | A **StatusCell** about a **MethodDescription** does not entail a run‑time outcome. | Keep **Approved** on Spec; place **Satisfied/Violated** on clauses **about Work** within a **Window**; require Observation/Evidence (KD‑CAL) for the run side.                                                       |
| **A3**  | **Execution = Actuation**      | PLC log of setpoints recorded as the whole execution history.         | Loses non‑signal aspects (delays, conditions, context); removes reasoning support.  | Model **Actuation** as **within** **Work**. Keep both SenseCells: *Task execution* (Work) and *Command/Setpoint* (Actuation).                                                                                        |
| **A4**  | **BPMN‑as‑Run**                | BPMN *Process* treated as “the thing that ran.”                       | BPMN’s meaning is context‑local and design‑time.                               | Use a **Bridge** (F.7/F.9) from *BPMN\:Process (design)* → *PROV\:Activity (run)* with kind **Interpretation**, CL/Loss declared.                                                                                    |
| **A5**  | **Spec Drift Retroactivity**   | Update to a recipe is assumed to modify past executions.              | Violates temporal honesty; breaks auditability.                             | Past **Work** remains as‑was. New **MethodDescription** versions describe future **Work** only; record variant relations if a run deviated.                                                                                 |
| **A6**  | **Homonym Collapse**           | *Task*, *activity*, *process* used interchangeably across Contexts.      | Imports meaning implicitly; masks losses.                                   | Prefix with **Context** and use **SenseCells**: e.g., *task (IEC)*, *activity (PROV)*, *process (BPMN)*. Any relation uses **Bridges** with CL/Loss.                                                                    |
| **A7**  | **Signal‑Only Compliance**     | SLO judged solely from actuator traces.                               | Ignores measured outcomes; risks false positives.                           | Tie **SLO** clauses to **Observations** (KD‑CAL) **about Work outcomes**; treat Actuation as an input, not proof.                                                                                                    |
| **A8**  | **Recipe-as-Role**             | “The Spec assigns responsibility” (mixes MethodDescription with Role constructs — `U.RoleDescription`/`U.RoleAssignment`).  | Conflates the `U.MethodDescription` episteme with behavioural masks.         | Use **F.4 Role Description**; let **MethodDescription** only **describe** a Method.                                                                            |
| **A9**  | **One‑Context Scope**        | A single Context (e.g., BPMN) used as if it covered control/measurement. | Scope mirage; silent cross‑domain generalisation.                           | Re‑cut Contexts (F.1) to include control and sensing. Re‑express statements with the quartet across those Contexts.                                                                                                        |
| **A10** | **Lossless Bridge Assumption** | Claiming “equivalent” across Contexts without Loss.                      | Hides mismatches; unsafe transfer of inferences.                            | In **F.7/F.9** declare Bridge **kind**, **CL**, and explicit **Loss** notes.                                                                                                                                         |
| **A11** | **Recipe-as-Kind**             | Treating a MethodDescription vocabulary as a method-kind taxonomy.                  | Category error; confuses description wording with method kindhood.                                           | If a stable hierarchy of **kinds** of Methods is needed, use admission under E.24.UK and C.3 with an ontic and bridge record; keep MethodDescription as *description* only.                                                                                   |
| **A12** | **Actuation Outside Work**     | Commands modeled without enclosing Work.                              | Severs signal from enactment context; breaks traceability.                  | Embed **Actuation** **within** **Work** intervals; relate to the enacting Role and Method or MethodDescription references.                                                                                                     |

