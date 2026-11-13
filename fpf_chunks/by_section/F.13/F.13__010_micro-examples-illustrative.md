---
chunk_kind: "child"
pattern_id: "F.13"
pattern_title: "Lexical Continuity & Deprecation"
section_id: "F.13:9"
section_title: "Micro‑examples (illustrative)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.13/F.13__010_micro-examples-illustrative.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "F.13 — Lexical Continuity & Deprecation"
  - "F.13:9 — Micro‑examples (illustrative)"
line_start: 130660
line_end: 130694
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

### F.13:9 - Micro‑examples (illustrative)

#### F.13:9.1 - Pure rename inside a local service vocabulary

*Constructed case:* Under the fixed `ServiceVocabulary-1` reference scheme, the local-sense claim is “a service indicator threshold together with its assessment window”. The old expression is **“SLO”**, the proposed expression is **“service-level objective”**, and both serve the same use of reading a service objective. No change to the objective or assessment rule is proposed.
**Relation:** `renames("SLO" → "service-level objective")`.
**Why:** The scheme, sense and use are unchanged; expansion improves recognition.
**Effect:** Retain the two exact cells `<ServiceVocabulary-1, "SLO", claim>` and `<ServiceVocabulary-1, "service-level objective", claim>` in the naming lineage. Old text retains its earlier expression and meaning; new writing uses the expansion. No Bridge is needed for these identical semantic projections.

#### F.13:9.2 - Alias for a common legacy synonym (Sys‑CAL)

*Illustrative premise:* A local state-space control vocabulary has independently established the same scheme, sense and use for **“control output”** and **“actuation”**. This premise requires source-local recovery in a real application; the words alone are insufficient.
**Relation:** `aliases("control output" ↔ "actuation")`.
**Effect:** Keep the distinct expression-bearing cells and one historical read-path. New text uses the locally selected preferred expression **“actuation”**.

#### F.13:9.3 - Split of a muddled local sense (Enactment)

*Context:* **BPMN 2.0**.
Legacy label **“process”** was used to mean both **“collaboration”** and **“executable process”** in a team’s prose.
**Relation:** `splits("process" ⇒ {"collaboration","executable‑process"})`.
**Effect:** The single Concept‑Set row becomes two; old label is deprecated with a disambiguation note.

#### F.13:9.4 - Merge duplicate comparison rows

Suppose the two Concept-Set rows labelled **“DBaaS”** and **“Database-Service”** display the same named comparison or use, exact entries, independently established relations, losses, basis and receiving-use conclusion. They are duplicate displays; combining them asserts no new sameness among their entries.
**Relation:** `merges({"DBaaS","Database‑Service"} ⇒ "Database‑Service")`.
**Effect:** “DBaaS” becomes a legacy alias with an epoch note.

#### F.13:9.5 - Not a rename: Cross‑context temptation (forbidden)

*Contexts:* **BPMN (design graph)** vs **PROV‑O (run activity)**.
Temptation: “Let’s rename *process* to *activity*.”
**Diagnosis:** A design graph and a run occurrence have different local meanings. A rename requires the same meaning and use.
**Action:** Keep the labels and their exact meanings. If a semantic correspondence matters, test the relation under F.9. If a proposed use relies on it, assess that use and its current grounds separately. A design-to-run or production relation belongs under the rule for that relation.

