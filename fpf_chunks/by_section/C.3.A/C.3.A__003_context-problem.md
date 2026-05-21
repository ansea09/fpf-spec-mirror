---
chunk_kind: "child"
pattern_id: "C.3.A"
pattern_title: "Typed Guard Macros for Kinds + USM (Annex)"
section_id: "C.3.A:2"
section_title: "Context & Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.A/C.3.A__003_context-problem.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "C.3.A — Typed Guard Macros for Kinds + USM (Annex)"
  - "C.3.A:2 — Context & Problem"
line_start: 37533
line_end: 37548
dependencies:
  - "A.2.6"
  - "C.3.x"
keywords:
  - "ESG"
  - "Kind-CAL"
  - "Method-Work"
  - "Typed guard"
  - "USM"
  - "regulatory profile"
---

### C.3.A:2 - Context & Problem

Projects often:

* treat **“more abstract wording”** as wider **G**,
* glue claims with incompatible **describedEntity** (kinds),
* move typed content across Contexts without **declared bridges**,
* or bake **AT** (abstraction vibe) into decision logic.

**C.3.A** fixes this by supplying guard macros that:
— **separate** typed compatibility (kinds) from **Scope** coverage (USM),
— require **both** bridges where needed,
— push congruence penalties to **R** only, and
— forbid **AT** in guards.


