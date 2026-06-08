---
chunk_kind: "child"
pattern_id: "F.13"
pattern_title: "Lexical Continuity & Deprecation"
section_id: "F.13:11"
section_title: "Extended examples"
source_path: "FPF-Spec.md"
output_path: "by_section/F.13/F.13__012_extended-examples.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "F.13 — Lexical Continuity & Deprecation"
  - "F.13:11 — Extended examples"
line_start: 73591
line_end: 73630
dependencies:
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "deprecation"
  - "evolution"
  - "merging terms"
  - "renaming"
  - "splitting terms"
---

### F.13:11 - Extended examples

#### F.13:11.1 - KD‑CAL × Services — *metric target* labels over time

* **Contexts:** *ITIL 4 (services, design)*; *SOSA/SSN (sensing, run)*.
* **Before:** Role Description used **“SLO”** (plain “target”) and readers often saw **“service target”**.
* **Move:** `renames("SLO" → "service‑level objective")` (Context: ITIL). Keep `aliases("service target" ↔ "service‑level objective")`.
* **Why:** Same local sense; clearer morphology for F.5; SOSA/SSN labels untouched.
* **Pay‑off:** Runtime **Observations** (SOSA) are later compared to **service‑level objective** clauses (ITIL) without Cross‑context aliasing.

#### F.13:11.2 - Sys‑CAL × LCA‑CAL — separating *execution* vs *actuation*

* **Contexts:** *IEC 61131‑3 (run)*; *state‑space control texts (design)*.
* **Temptation:** Rename **“task execution”** to **“actuation”** “to sound control‑ish”.
* **Diagnosis:** Different Contexts; different SenseCells (program run vs control output).
* **Move:** **No rename.** Keep labels; later add **Bridge** “`execution (IEC)` *produces* signals that realise `actuation (control)`” with CL stating partial coverage.
* **Pay‑off:** Plant narratives stop calling programs “actuators”; runtime vs control semantics stay crisp.

#### F.13:11.3 - Kind-CAL × Method‑CAL — false merge avoided

* **Contexts:** *OWL 2 (types, design)*; *SPEM 2.0 (methods, design)*.
* **Issue:** A row labeled **“Class”** tried to absorb **“WorkProductKind”** by a `renames`.
* **Diagnosis:** Not same sense; different calculi (type vs artefact category).
* **Move:** **Split the row**: `splits("class" ⇒ {"type‑class","work‑product‑category"})`.
* **Pay‑off:** Downstream Role Descriptions can point to the correct **SenseCell** without redefining ontological commitments.

#### F.13:11.4 - Enactment × KD‑CAL — retiring a misleading metaphor

* **Context:** *BPMN 2.0 (design)*.
* **Legacy:** Team jargon **“heartbeat”** used for a **timer event**. Newcomers confuse it with **sensor heartbeats** (KD‑CAL).
* **Move:** `retires("heartbeat")` in BPMN Context with note “use **timer event**; ‘heartbeat’ refers to sensor liveness in KD‑CAL”.
* **Pay‑off:** Two different ecosystems stop colliding on the same catchy word.

#### F.13:11.5 - Concept‑Set row refactor after rising CL

* **Rows:** `{“DBaaS”, “Database‑Service”}` representing service notions across several Contexts.
* **F.3 + F.9 outcome:** High CL; evidence of same Cross‑context alignment.
* **Move:** `merges({"DBaaS","Database‑Service"} ⇒ "Database‑Service")` at **row level**. Both legacy labels become row‑local aliases with epoch notes.
* **Pay‑off:** One clearer row label; old articles still understandable.

