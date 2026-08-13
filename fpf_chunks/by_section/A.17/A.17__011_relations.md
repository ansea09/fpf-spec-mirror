---
chunk_kind: "child"
pattern_id: "A.17"
pattern_title: "Canonical “Characteristic” (A.CHR‑NORM)"
section_id: "A.17:10"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.17/A.17__011_relations.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "A.17 — Canonical “Characteristic” (A.CHR‑NORM)"
  - "A.17:10 — Relations"
line_start: 28485
line_end: 28494
dependencies:
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.2.3"
  - "A.3.3"
  - "A.7"
  - "B.3"
  - "C.16"
  - "C.2"
  - "D.3"
  - "E.10"
  - "U.Dynamics"
  - "U.PromiseContent.acceptanceSpec"
keywords:
  - "attribute"
  - "axis"
  - "characteristic"
  - "dimension"
  - "measurement"
  - "property"
---

### A.17:10 - Relations

-   **Builds on / Elaborates:** _FPF Core Measurement Schema_ (as outlined in C.16). A.17 lifts the metric template concepts from C.16 into a kernel-level rule. It also reinforces **A.7 Strict Distinction**, by giving each measurement concept a unique name and forbidding overloaded terms.

-   **Constrains:** All other patterns that define or use metrics. For example, **A.3.3 `U.Dynamics`** (system dynamics) must name its state variables as Characteristics with proper scales (it cannot refer to them loosely as “KPIs” without context). Similarly, any **service-level targets / SLO clauses (A.2.3 `U.PromiseContent.acceptanceSpec`)** or **assurance calculations (B.3, D.3 patterns)** that involve measurements are governed by this canonical terminology (no unwarranted synonyms or unit confusion per ISO/IEC 80000, ISO/IEC 25024, QUDT, SOSA/SSN best practices). The pattern’s lexical rules are part of the **LEX-BUNDLE** (E.10) – any FPF-conformant context must adhere to these naming conventions.

-   **Coordinates with:** **A.18 (CSLC-KERNEL)**, which defines the minimal **Characteristic/Scale/Level/Coordinate** Standard in detail. A.17 provides the vocabulary and basic distinctions (what is a Characteristic, and its arity), while A.18 applies this to ensure each measurement template is well-formed. Also coordinates with **C.2 KD-CAL** and the **A.19/C.16 characterization stack**; those patterns use the Characteristic/Scale constructs to build domain-specific metrics (e.g. knowledge quality scores) and rely on A.17’s canon for consistency.

-   **Anticipates:** **E.10 Lexical Discipline** rules – A.17’s enforcement of a single term and controlled aliases is a concrete instance of the lexical uniformity mandated in E.10. It also paves the way for **F.7 Concept-Set Bridges** in Unification patterns, since external ontologies for quantities (ISO 80000, QUDT, etc.) can be mapped cleanly onto FPF Characteristics now that the term is fixed. In short, A.17 is a foundational lexicon pattern that a) ensures internal consistency and b) simplifies alignment with external standards for measurable properties.

