---
chunk_kind: "child"
pattern_id: "A.14"
pattern_title: "Advanced Mereology: Components, Portions, Aspects & Phases"
section_id: "A.14:5"
section_title: "Formal cores (normative semantics)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.14/A.14__006_formal-cores-normative-semantics.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "A.14 — Advanced Mereology: Components, Portions, Aspects & Phases"
  - "A.14:5 — Formal cores (normative semantics)"
line_start: 23102
line_end: 23159
dependencies:
  - "A.1"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.7"
  - "B.1"
  - "B.1.1"
  - "B.2"
  - "B.3.5"
  - "C.13"
keywords:
  - "ComponentOf"
  - "PhaseOf"
  - "PortionOf"
  - "composition"
  - "mereology"
  - "part-of"
---

### A.14:5 - Formal cores (normative semantics)

#### A.14:5.1 - PortionOf — metrical part of a measurable whole

**Intent.** Capture “some of the same stuff/extent”, governed by a measure that adds up.

**Applicability.** Any `U.Holon` that carries an **extensive** measure μ on the chosen scope
(examples: mass, volume, length‑of‑text, byte size, wall‑time budget).

**Primitive.** `PortionOf(x, y)` means: *x is the same kind of stuff/content as y, but less*.

**Axioms (A14‑POR‑\*)**

* **POR‑1 (Partial order).** PortionOf is reflexive, antisymmetric, transitive on its domain.
* **POR‑2 (Metrical dominance).** If `x ProperPortionOf y` then `0 < μ(x) < μ(y)` for the agreed μ.
* **POR‑3 (Additivity on disjoint portions).** If `PortionOf(x,y)`, `PortionOf(z,y)`, and `x ⟂ z` (the two portions do not overlap), and their join is admitted under the same measure and boundary rule, then `μ(x ⊔ z) = μ(x)+μ(z)` and `PortionOf(x ⊔ z,y)`. `ProperPortionOf` additionally requires the joined measure to remain strictly below `μ(y)`; a join equal to the whole is `PortionOf` but not `ProperPortionOf`.
* **POR‑4 (Kind integrity).** x and y must share the same **measure kind** and **unit** (or a declared conversion).
* **POR‑5 (Boundary compatibility).** For physical wholes, the whole’s boundary encloses the union of its portions; cross‑boundary “leaks” are interactions, not portions.

**Didactic tests.**
✔ “5 kg from a 20 kg billet” — PortionOf.
✔ Two disjoint 5 kg cuts from the same 20 kg billet have a 10 kg join under the same mass unit and boundary rule; that join is still a ProperPortionOf the billet.
✔ “Pages 1–10 of the report” — PortionOf (μ = page or token count).
✘ “The pump module of the plant” — **ComponentOf**, not PortionOf.
✘ “The Methods section of the paper” — **ConstituentOf**, not PortionOf.

#### A.14:5.2 - PhaseOf — temporal part of the same carrier

**Intent.** Capture “the same holon during a sub‑interval”, preserving identity through change.

**Applicability.** Any `U.Holon` that persists across time with a recognised **carrier identity**.

**Primitive.** `PhaseOf(x, y)` means: *x is y restricted to a proper time interval*.

**Axioms (A14‑PHA‑\*)**

* **PHA‑1 (Strict temporal parthood).** `PhaseOf` is irreflexive, asymmetric, and transitive on proper temporal restrictions of one unchanged carrier. In particular, `PhaseOf(y,y)` is false: a whole-lifetime or self-reference is not a proper temporal part.
* **PHA‑2 (Proper interval and same carrier).** `PhaseOf(x,y)` requires the interval of x to be a proper sub-interval of y's interval and the carrier-identity rule to hold throughout both. It does not require x to be a maximal cell of a partition.
* **PHA‑3 (Nesting and overlap are allowed).** Temporal restrictions of the same carrier may nest or overlap. A week may be part of a year-long phase, and a diagnostic window may overlap a calibration window. Those facts are not contradictions and do not by themselves select an aspect or partition.
* **PHA‑4 (Selected partition is an additional claim).** When a use needs exhaustive non-overlapping cells, declare one carrier, one interval to be covered, one analysis aspect or partition rule, and the selected family of `PhaseOf` values. Only cells of that same explicitly selected partition must be pairwise non-overlapping and jointly cover the declared interval. Another aspect or rule may select a different, overlapping family.
* **PHA‑5 (Identity through change).** Properties may vary between phases, but the carrier’s identity criteria hold continuously (e.g., same serial number, same legal identity, same theorem statement).
* **PHA‑6 (Escalation to MHT).** If identity criteria break (e.g., metamorphosis with new objectives), **declare a Meta‑Holon Transition (B.2)** rather than a PhaseOf.

**Didactic tests.**
✔ “PumpUnit\#3 **before** calibration” — PhaseOf(Pump\#3\_pre, Pump\#3).
✔ If `PhaseOf(Pump#3@week-32, Pump#3@2026)` and `PhaseOf(Pump#3@2026, Pump#3)`, transitivity also gives `PhaseOf(Pump#3@week-32, Pump#3)`. A high-vibration diagnostic window may overlap a calibration window for the same pump; neither is thereby a cell of one selected partition.
✔ “Specification episteme E during τ₂”, with the C.2.1 identity triple unchanged and a proper interval current — PhaseOf(E@τ₂, E). ✘ “Spec v2” — if a C.2.1 discriminator changed, identify another episteme and test `EpistemeEditionRelation(E_v1,E_v2)` separately; the label proves neither identity nor continuity.
✘ “Shift 1 of the same batch run” — use A.15.1 `TemporalPartOf_work`, `EpisodeOf_work`, `OperationalPartOf_work`, or another exact Work-part or occurrence relation whose predicate obtains.
✘ “Prototype vs. production unit” — likely **different carriers**; use ComponentOf/ConstituentOf or MHT per criteria.

#### A.14:5.3 - CT2R‑LOG & Compose‑CAL handshake *(normative link)*

* A direct **structural relation claim** is usable without this assurance handshake. When the publication elects B.3.5 or a named current requirement demands it, the published claim **SHALL** link through `tv:groundedBy` to one current C.2.1 construction-trace episteme in the `Γ_m.sum | Γ_m.set | Γ_m.slice` form (see **B.3.5** and **C.13**) and carry the profile's declared `validationMode`. The exact relation predicate, current facts, and occurrence-identity rule determine whether the occurrence obtains and how it is identified; the candidate's direct identity or reidentification rule determines continuity. The trace only reports that basis.
* **PhaseOf** is **temporal parthood**; it **SHALL NOT** be grounded through `Γ_m`. Its assurance follows the same-carrier and proper-interval criteria, the separately declared selected-partition rule when one is claimed, and `Γ_time` ordering (B.1.4).
* **MemberOf** remains **non-mereological** (CC-MEM-2). A `set` trace is truthful only after one exact collection, its identity rule, and the exact direct membership occurrences are grounded; no **ComponentOf** inference follows.

Two quick identity tests apply before relying on a trace. The same listed constituents can form a different whole when their direct assembly relations or rule differ. Conversely, a permitted constituent replacement can preserve the same whole. An equal input list, a repeated trace, or `validationMode=axiomatic` decides neither case.

