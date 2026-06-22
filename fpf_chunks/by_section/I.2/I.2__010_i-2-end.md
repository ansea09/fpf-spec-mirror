---
chunk_kind: "child"
pattern_id: "I.2"
pattern_title: "Expanded Entry Disambiguation Cases"
section_id: "I.2:End"
section_title: "I.2:End"
source_path: "FPF-Spec.md"
output_path: "by_section/I.2/I.2__010_i-2-end.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "I.2 — Expanded Entry Disambiguation Cases"
  - "I.2:End — I.2:End"
line_start: 89149
line_end: 89191
dependencies:
keywords:
---

### I.2:End

# **Part J – Indexes & Navigation Aids**

| §   | ID & Title               |  Concise reminder                                        |
| --- | ------------------------ | ------------------------------------------------------- |
| J.1 | Concept‑to‑Pattern Index |  Quick jump from idea (“boundary”) to pattern (§, id).   |
| J.2 | Pattern‑to‑Example Index |  Table listing every archetypal grounding vignette.      |
| J.3 | Principle‑Trace Index    |  Maps each Pillar / C‑rule / P‑rule to concrete clauses. |

# **Part K - Lexical Debt**

## Mandatory replacement map for measurement terms


> **Rule:** In all **normative** content (specifications, data schemas, etc.), the deprecated terms **“axis”** and **“dimension”** (and their plural or compound forms) **MUST NOT** be used to denote a measurable aspect. Use **Characteristic** in the Tech register instead. Other colloquial terms should be mapped to canonical terms as listed below. In **Plain** narrative, deprecated aliases may appear _only on first use_ and only if paired with their canonical equivalent for clarity.

| Deprecated term (context) | **Replace with** (Tech register) | Plain register allowance | Canonical Reference |
| --- | --- | --- | --- |
| axis (of measurement); dimension (of a system or quality) | **(disallowed in Core prose)** → use **Characteristic** | No parenthetical allowance in Core; use **Characteristic**, **Measure**, or **Coordinate** only | A.17 (CHR-NORM) |
| point (on an axis); data point | **Coordinate** (on a Scale) | “point” _(in explanations only, e.g. “a point on the scale”)_ | A.18 (CSLC-KERNEL) |
| metric value; raw score | **Coordinate** (or **Value**) | “value” _(acceptable in plain usage when context is clear, but formally it’s a Coordinate tied to a Characteristic)_ | A.18, C.16 |
| score (composite or normalized) | **Score** (produced via a **ScoringMethod**) | “score” _(if needed in narrative, ensure it’s explained as a result of a defined ScoringMethod)_ | A.17/A.18 (ScoringMethod/Score) |
| unit dimension; unit axis | **Unit** (of a Scale) | “unit” _(plain usage okay)_ | A.18 (Scale/Unit) |
| metric (as a noun) | **Avoid in Tech and as primitive** → use **`U.DHCMethodRef` / `U.Measure` / Score** | “metric” _(Plain only on first use, with pointer to canonical terms)_ | C.16 § 5.1 (L5), A.18 |

## Temporal claim lexical debt from C.27

Retire untyped velocity, acceleration, cadence, agility, rhythm, inertia, and dynamics language when it is used outside a named C.27, C.16, or A.3.3 reading. Repair each occurrence to one of: ordinary prose, Dyn0 state reading or snapshot, Dyn1 measured rate or trend, Dyn2 intervention-sensitive temporal claim, C.16 measurement construction, or A.3.3 reusable transition law or model.

Russian/English Plain-Tech twins for authoring:

| Russian Plain | Safe Tech reading |
| --- | --- |
| скорость | rate, throughput, or tempo reading |
| ускорение | rate-change or intervention-sensitive temporal claim |
| усилие | planned effort, work, resource, or input basis, or intervention basis |
| инерция | resistance/inertia proxy, not a physical mass analogue by default |
| ритм | bearer/anchor/window/proxy relation |
| динамика второй производной | Dyn2 claim reading, not second-derivative ontology |

## Migration debt from A.2.6 (Scope, ClaimScope, WorkScope)

