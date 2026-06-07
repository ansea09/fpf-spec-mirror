---
chunk_kind: "child"
pattern_id: "G.Core"
pattern_title: "Part G Core Invariants"
section_id: "G.Core:8"
section_title: "Common anti-patterns and how to avoid them"
source_path: "FPF-Spec.md"
output_path: "by_section/G.Core/G.Core__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "G.Core — Part G Core Invariants"
  - "G.Core:8 — Common anti-patterns and how to avoid them"
line_start: 76129
line_end: 76151
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
  **Avoid:** cite `A.19` and `G.0` through `CC‑GCORE‑CN‑CG‑1`.

* **Anti-pattern:** Adding a fourth guard status (“unknown”, “maybe”, “probe-only”) as a separate decision value.
  **Avoid:** keep guard domain tri‑state; express “probe-only” as policy/branching and record via pins/audit.

* **Anti-pattern:** Treating mandatory invariants as “defaults” to centralize them.
  **Avoid:** keep invariants as invariants (CC‑GCORE‑* cited through canonical governing definitions); restrict the Default Governing Definition Index to true defaults (constants or conditional default-rules).

* **Anti-pattern:** Turning partial orders into scalar ranks silently.
  **Avoid:** keep set‑valued semantics unless a total order is explicitly declared by a comparator/policy.

* **Anti-pattern:** Competing defaults scattered across multiple patterns.
  **Avoid:** Default Governing Definition Index; delegate duplicate statements to the one governing definition.

* **Anti-pattern:** Local trigger tokens without canonical mapping.
  **Avoid:** provide/cite a `TriggerAliasMap` with namespace‑qualified aliases.

* **Anti-pattern:** Breaking public CC ids during dedup.
  **Avoid:** convert to delegation items; preserve IDs.

