---
chunk_kind: "child"
pattern_id: "F.13"
pattern_title: "Lexical Continuity & Deprecation"
section_id: "F.13:9"
section_title: "Micro‑examples (illustrative)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.13/F.13__010_micro-examples-illustrative.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "F.13 — Lexical Continuity & Deprecation"
  - "F.13:9 — Micro‑examples (illustrative)"
line_start: 73535
line_end: 73572
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

### F.13:9 - Micro‑examples (illustrative)

#### F.13:9.1 - Pure rename inside a Context (ITIL → clearer plain label)

*Context:* **ITIL 4 (services)**.
Old: **“SLO” (plain: *service target*)** → New: **“service‑level objective” (plain unchanged)**.
**Relation:** `renames("SLO" → "service‑level objective")`.
**Why:** F.5 morphology & expansion; SenseCell unchanged (same clause semantics).
**Effect:** Old guidance remains readable; new writing spells out the term.

#### F.13:9.2 - Alias for a common legacy synonym (Sys‑CAL)

*Context:* **state‑space control (design)**.
Preferred: **“actuation”**. Legacy: **“control output”**.
**Relation:** `aliases("control output" ↔ "actuation")`.
**Why:** Same SenseCell; legacy term appears in older textbooks.
**Effect:** Readers resolve to the SenseCell; new texts use “actuation”.

#### F.13:9.3 - Split of a muddled local sense (Enactment)

*Context:* **BPMN 2.0**.
Legacy label **“process”** was used to mean both **“collaboration”** and **“executable process”** in a team’s prose.
**Relation:** `splits("process" ⇒ {"collaboration","executable‑process"})`.
**Effect:** The single Concept‑Set row becomes two; old label is deprecated with a disambiguation note.

#### F.13:9.4 - Merge after clustering raised confidence (Kind-CAL row)

Two Concept‑Set rows **{“DBaaS”, “Database‑Service”}** converge after F.3 within the same context profile and F.9 raised CL.
**Relation:** `merges({"DBaaS","Database‑Service"} ⇒ "Database‑Service")`.
**Effect:** “DBaaS” becomes a legacy alias with an epoch note.

#### F.13:9.5 - Not a rename: Cross‑context temptation (forbidden)

*Contexts:* **BPMN (design graph)** vs **PROV‑O (run activity)**.
Temptation: “Let’s rename *process* to *activity*.”
**Diagnosis:** Cross‑context; **different SenseCells**.
**Action:** **No continuity relation.** Keep labels; if needed, declare a **Bridge** (F.9) explaining design→run mapping with CL/Loss.

