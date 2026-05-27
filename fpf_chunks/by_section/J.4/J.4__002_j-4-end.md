---
chunk_kind: "child"
pattern_id: "J.4"
pattern_title: "First Practical Entry Neighborhood Index"
section_id: "J.4:End"
section_title: "J.4:End"
source_path: "FPF-Spec.md"
output_path: "by_section/J.4/J.4__002_j-4-end.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "J.4 — First Practical Entry Neighborhood Index"
  - "J.4:End — J.4:End"
line_start: 79111
line_end: 79144
dependencies:
keywords:
---

### J.4:End
# **Part K  – Lexical debt**

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

