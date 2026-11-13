---
chunk_kind: "child"
pattern_id: "G.Core"
pattern_title: "Discipline SoTA Kit Invariants, Defaults and Refresh Triggers (Part G)"
section_id: "G.Core:8"
section_title: "Common anti-patterns and how to avoid them"
source_path: "FPF-Spec.md"
output_path: "by_section/G.Core/G.Core__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "G.Core — Discipline SoTA Kit Invariants, Defaults and Refresh Triggers (Part G)"
  - "G.Core:8 — Common anti-patterns and how to avoid them"
line_start: 134821
line_end: 134843
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

### G.Core:8 - Common anti-patterns and how to avoid them

* **Anti-pattern:** Restating CN‑Spec/CG‑Spec rules inside a `G.x` “for convenience”.
  **Avoid:** cite the applicable specification (`A.19.CN`, `G.0` or both) through `CC‑GCORE‑CN‑CG‑1`.

* **Anti-pattern:** Adding a fourth guard status (“unknown”, “maybe”, “probe-only”) as a separate decision value.
  **Avoid:** keep guard domain tri‑state; express “probe-only” as policy/branching and record via pins/audit.

* **Anti-pattern:** Treating mandatory invariants as “defaults” to centralize them.
  **Avoid:** Cite mandatory invariants through their `CC‑GCORE‑*` items and governing definitions. Reserve the Default Governing Definition Index for defaults, including constants and conditional default rules.

* **Anti-pattern:** Turning partial orders into scalar ranks silently.
  **Avoid:** keep the set returned under the partial order. A total ranking may guide a decision when the applicable comparator or policy explicitly admits it. A scalar summary used only for reporting leaves the selected set unchanged.

* **Anti-pattern:** Competing defaults scattered across multiple patterns.
  **Avoid:** Default Governing Definition Index; delegate duplicate statements to the one governing definition.

* **Anti-pattern:** Local trigger tokens without canonical mapping.
  **Avoid:** provide/cite a `TriggerAliasMap` with namespace‑qualified aliases.

* **Anti-pattern:** Breaking public CC ids during dedup.
  **Avoid:** convert to delegation items; preserve IDs.

