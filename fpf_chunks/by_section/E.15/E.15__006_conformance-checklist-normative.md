---
chunk_kind: "child"
pattern_id: "E.15"
pattern_title: "Lexical Authoring & Evolution Protocol  (LEX‑AUTH)"
section_id: "E.15:5"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.15/E.15__006_conformance-checklist-normative.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "E.15 — Lexical Authoring & Evolution Protocol  (LEX‑AUTH)"
  - "E.15:5 — Conformance Checklist (normative)"
line_start: 79395
line_end: 79423
dependencies:
  - "A.10"
  - "B.3"
  - "B.4"
  - "C.18"
  - "C.19"
  - "E.10"
  - "E.9"
  - "F.15"
keywords:
  - "LAT"
  - "delta-classes"
  - "evolution protocol"
  - "lexical authoring"
---

### E.15:5 - Conformance Checklist (normative)

**CC‑LA‑1 (Exact frame and intended use).**
Every authoring run **MUST** name the exact pattern and edition, receiving question and intended use, `ClaimScope`, Delta-Class, objectives, and acceptance lenses before generating candidates. It names a scheme, source, model-use structure, or subject-specific situation only when that value changes the work.

**CC‑LA‑2 (SoTA as evidence).**
External inputs **MUST** be bound through evidence-use relations around source epistemes with **claim, claim‑scope, polarity, timespan** (formal/empirical lines). No raw links.

**CC‑LA‑3 (Open‑ended generation).**
At least **K≥3** candidate variants **MUST** be generated via **NQD‑CAL** with a declared **E/E policy**; single‑shot edits violate LEX‑AUTH.

**CC‑LA‑4 (Bridges & CL).**
When a candidate actually relies on a relation between distinct F.17 local-sense cells, that relation **MUST** be stated through F.9 with its admitted use and loss notes. CL penalties apply to the R-lane when scoring. Shared wording, a source import, or an edition change alone does not establish a Bridge.

**CC‑LA‑5 (Harness).**
The candidate winner **MUST** pass **LEX‑BUNDLE** lint, **SCR/RSCR** tests, Γ‑consistency, and SoD/RSG gates where applicable.

**CC‑LA‑6 (Assurance deltas).**
The LAT **MUST** publish Δ⟨F,G,R⟩ relative to baseline, explicitly accounting for CL penalties and any narrowed scopes.

**CC‑LA‑7 (DRR).**
A **DRR** entry is mandatory for Δ‑2/Δ‑3 changes; it records options considered, rationale, and impact radius.

**CC‑LA‑8 (Refresh plan).**
Empirical evidence in the LAT **MUST** carry a **decay/refresh** window; a watchpoint **MUST** be scheduled in the Canonical Evolution Loop.

**CC‑LA‑9 (Publication).**
Publish the **pattern + LAT** together; past LATs are immutable. New runs produce new LATs.

