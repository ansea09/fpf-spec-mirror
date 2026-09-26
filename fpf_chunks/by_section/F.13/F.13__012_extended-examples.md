---
chunk_kind: "child"
pattern_id: "F.13"
pattern_title: "Lexical Continuity & Deprecation"
section_id: "F.13:11"
section_title: "Extended examples"
source_path: "FPF-Spec.md"
output_path: "by_section/F.13/F.13__012_extended-examples.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "F.13 — Lexical Continuity & Deprecation"
  - "F.13:11 — Extended examples"
line_start: 106895
line_end: 106934
dependencies:
  - "F.1"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "deprecation"
  - "historical reading"
  - "lexical continuity"
  - "local aliases"
  - "renaming labels"
  - "retirement"
  - "splitting and merging labels"
---

### F.13:11 - Extended examples

#### F.13:11.1 - KD‑CAL × Services — *metric target* labels over time

* **Contexts:** *ITIL 4 (services, design)*; *SOSA/SSN (sensing, run)*.
* **Before:** An illustrative local service-objective description used **“SLO”** (plain “target”), and older texts also used **“service target”** for the same locally recovered meaning.
* **Move:** `renames("SLO" → "service‑level objective")` (Context: ITIL). Keep `aliases("service target" ↔ "service‑level objective")`.
* **Why:** The example assumes the same scheme, local-sense claim and use. Retain each expression's exact cell and the later naming settlement; SOSA/SSN labels are unchanged.
* **Pay‑off:** Runtime **Observations** (SOSA) are later compared to **service‑level objective** clauses (ITIL) without Cross‑context aliasing.

#### F.13:11.2 - Sys‑CAL × LCA‑CAL — separating *execution* vs *actuation*

* **Contexts:** *IEC 61131‑3 (run)*; *state‑space control texts (design)*.
* **Temptation:** Rename **“task execution”** to **“actuation”** “to sound control‑ish”.
* **Diagnosis:** Different Contexts; different SenseCells (program run vs control output).
* **Move:** **No rename.** Keep the labels. Establish any actual Work-to-signal production or output relation under its direct pattern, following F.11. Add F.9 only when a separate semantic correspondence between exact local senses is needed; then keep the bounded-use claim and reliance separate.
* **Pay‑off:** Plant narratives stop calling programs “actuators”; runtime vs control semantics stay crisp.

#### F.13:11.3 - Kind-CAL × method/work stack — false merge avoided

* **Contexts:** *OWL 2 (types, design)*; *SPEM 2.0 (methods, design)*.
* **Issue:** A row labeled **“Class”** tried to absorb **“WorkProductKind”** by a `renames`.
* **Diagnosis:** Not same sense; different calculi (type vs artefact category).
* **Move:** **Split the row**: `splits("class" ⇒ {"type‑class","work‑product‑category"})`.
* **Pay-off:** Later descriptions can cite the exact local meaning they use. Any SystemRoleKindDescription still describes its independently recovered system-role kind under F.4; a source-cell pointer does not establish that kind.

#### F.13:11.4 - Enactment × KD‑CAL — replacing a misleading metaphor

* **Context:** *BPMN 2.0 (design)*.
* **Legacy:** Team jargon **“heartbeat”** used for a **timer event**. Newcomers confuse it with **sensor heartbeats** (KD‑CAL).
* **Move:** `renames("heartbeat" → "timer event")` for the team’s unchanged BPMN timer-event meaning. Keep a local historical read-path; the sensor-liveness use remains a different local meaning.
* **Pay‑off:** Two different ecosystems stop colliding on the same catchy word.

#### F.13:11.5 - Concept‑Set row refactor after duplicate comparison is established

* **Rows:** `{“DBaaS”, “Database‑Service”}` representing service notions across several Contexts.
* **Comparison basis:** Both rows display the same named comparison or use, exact source-local entries, independently established relations, losses, basis and receiving-use conclusion. Only the duplicate display is combined; no source meanings or Bridge occurrences are merged.
* **Move:** `merges({"DBaaS","Database‑Service"} ⇒ "Database‑Service")` at **row level**. Both legacy labels become row‑local aliases with epoch notes.
* **Pay‑off:** One clearer row label; old articles still understandable.

