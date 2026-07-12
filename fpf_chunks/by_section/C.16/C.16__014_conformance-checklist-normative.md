---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:10"
section_title: "Conformance Checklist (Normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__014_conformance-checklist-normative.md"
commit_sha: "44dd88188a07646ef23aca32627a3f670525853f"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:10 — Conformance Checklist (Normative)"
line_start: 44571
line_end: 44584
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "B.3"
  - "C.26"
  - "C.26.1"
keywords:
  - "CSLC"
  - "U.DHCMethod(Ref)"
  - "U.EvidenceStub"
  - "U.Measure"
  - "U.Unit"
  - "direct comparability"
  - "measurement"
  - "measurement template"
  - "polarity"
  - "probe-changing-state"
  - "scoring method disclosure"
  - "shared-frame check"
---

### C.16:10 - Conformance Checklist (Normative)

> *Thought‑level acceptance conditions for authors and assessors; they constrain meaning, not tooling.*

**CC-MCHR-1 - CSLC binding.** Each `U.DHCMethodRef` binds **exactly one** `U.Characteristic` and **exactly one** scale; each `U.Measure` carries a value valid for that scale (cf. A.18).
**CC‑MCHR‑2 - Polarity declared.** Every **ordered** scale in a template declares **polarity**; any **Score** via 𝒢 is monotone w.r.t. that polarity.
**CC‑MCHR‑3 - Unit coherence.** Claims that compare or combine values are **grounded in unit coherence** (or declared conversions for interval or ratio).
**CC‑MCHR‑4 - Comparability honesty.** Ordered comparisons are asserted **only** when **R‑CMP‑1** holds (same‑template direct comparability) or when a **named and cited** transformation basis is provided per **R‑CMP‑2**; otherwise authors use qualitative/set‑level language.
**CC‑MCHR‑5 - Evidence sufficiency.** Where evidence is required by the template, the measure’s grounds are **conceptually sufficient** to retrace the claim; composition respects **Σ‑1…Σ‑4**.
**CC‑MCHR‑6 - Role-state-relation alignment.** If a measure gates a **state** in `RoleStateRelation@BoundedContext`, the checklist criteria **respect scale semantics** and the **EntityOfConcern vs Description-episteme** split. No lifecycle phrasing; use state assertions and checklist-governed state changes.
**CC‑MCHR‑7 - Dynamics awareness.** Where discussions involve change, the **CharacteristicSpace** is **named** (characteristics, units, topology) and separated from the **transition law**.
**CC‑MCHR‑8 - Lexical guard‑rails.** Tech identifiers and headings use **Characteristic, Scale, Level, Value, Score, Unit, and ScoringMethod**; aliases (axis, dimension, points, or stars) appear **only** in explanatory Plain register with a first‑mention mapping to the Tech canon.
**CC‑MCHR‑9 - Causal-use metric boundary.** A measurement, metric disparity, score, dashboard reading, or benchmark value that reaches `CausalUseActivation` SHALL keep measurement construction, scale admissibility, comparability, and evidence-stub repair in `C.16`, and SHALL carry causal-use question, causal-ladder rung, causal estimand, support basis, support verdict, admissible causal use, and inadmissible causal use in `C.28`.

