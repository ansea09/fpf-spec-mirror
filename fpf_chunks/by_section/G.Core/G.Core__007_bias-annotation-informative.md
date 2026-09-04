---
chunk_kind: "child"
pattern_id: "G.Core"
pattern_title: "Part G Core Invariants"
section_id: "G.Core:6"
section_title: "Bias-annotation (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.Core/G.Core__007_bias-annotation-informative.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "G.Core — Part G Core Invariants"
  - "G.Core:6 — Bias-annotation (informative)"
line_start: 101059
line_end: 101075
dependencies:
  - "A.15.3"
  - "A.19"
  - "A.19.CHR"
  - "A.6.7"
  - "E.10"
  - "E.19"
  - "E.8"
  - "G.0"
  - "G.13"
  - "G.Core"
keywords:
  - "Default Governing Definition Index"
  - "ID continuity"
  - "Part‑G invariants"
  - "RSCR trigger kinds"
  - "core linkage"
  - "delegation-first core"
---

### G.Core:6 - Bias-annotation (informative)

* **Centralization bias:** One governing hub can become too thick. Mitigation: delegation-first citation; keep only true Part‑G invariants and typed indices here.
* **Over-typing bias:** A trigger catalogue can become overly granular. Mitigation: granularity discipline + scope notes; only add new kinds when planning/selection needs it.
* **Refactor rigidity bias:** Preserving IDs can feel cumbersome. Mitigation: delegation items preserve IDs while enabling deduplication.
* **Default absolutism bias:** Defaults may require conditional rules. Mitigation: Default Governing Definition Index allows conditional default rules with explicit applicability conditions.
* **Single-writer bias:** prefers single‑writer *authoring* for catalogs and explicit governing-definition tables.
  *Mitigation:* delegation-first citation; keep catalogs minimal; avoid “second specs”.
* **Architectural bias:** centralizes invariants to prevent accidental coupling across `G.x`.
  *Mitigation:* keep core thin; force `Extensions` to remain pattern‑scoped.
* **Ontological/epistemic bias:** enforces strict distinction between governing spec refs, kits, mechanisms, and orchestration.
  *Mitigation:* allow didactic scope notes while keeping normative surface id‑based.
* **Pragmatic bias:** adds authoring overhead (linkage sections, alias maps).
  *Mitigation:* one small mandatory bridge CC item per pattern (`CC‑Gx‑CoreRef`) and short linkage slices only.
* **Didactic bias:** risks “glossy hub prose” that hides missing CC coverage.
  *Mitigation:* enforce CC/Solution coherence (E.19) and keep invariants checkable via `CC‑GCORE‑…`.

