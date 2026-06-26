---
chunk_kind: "child"
pattern_id: "C.20"
pattern_title: "Composition of U.Discipline (Discipline‑CAL)"
section_id: "C.20:section-001"
section_title: "E.24.UK settlement"
source_path: "FPF-Spec.md"
output_path: "by_section/C.20/C.20__002_e-24-uk-settlement.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "C.20 — Composition of U.Discipline (Discipline‑CAL)"
  - "C.20:section-001 — E.24.UK settlement"
line_start: 45925
line_end: 45944
dependencies:
  - "A.19"
  - "C.2"
  - "C.21"
  - "C.22"
  - "C.23"
  - "E.10"
  - "F.17-F.18"
  - "F.9"
  - "G.0"
  - "G.2"
  - "G.5"
  - "U.BoundedContext"
keywords:
  - "U.AppliedDiscipline"
  - "U.Transdiscipline"
  - "discipline"
  - "episteme corpus"
  - "institutions"
  - "standards"
  - "Γ_disc"
---

### E.24.UK settlement

`U.Discipline` is the root durable holon kind used for field-level practice-and-knowledge wholes. Its EntityOfConcern lets FPF users talk about a discipline as one reusable object without collapsing it into a domain label, bounded context, organization, publication set, or tradition name.

The identity of a `U.Discipline` is held by a composition relation over five required positions:

- **Episteme canon:** theories, models, reference works, definitions, proof traditions, benchmark descriptions, and other epistemes treated as canonical in the discipline;
- **standards and practices:** accepted methods, norms, standard procedures, measurement conventions, and admissible comparison rules;
- **organizational carriers:** journals, committees, curricula, professional bodies, labs, or institutional arrangements that carry and refresh the discipline without being identical to it;
- **bridge set:** F.9/F.17 bridge and term rows that state how the discipline is reused across bounded contexts and source traditions;
- **comparison governance:** characteristic, scale, evidence, and CG-Spec references that make comparisons inside or across disciplines admissible.

This makes `U.Discipline` a `U.Holon`: it is a whole with epistemic, organizational, practice, bridge, and comparison-governance parts. It is not a `U.System` by default; some organizational carriers are systems, but the discipline holon includes epistemes and practices as well. It is not merely a `U.Episteme`; the canon is only one position in the discipline composition.

Boundary: a **domain** names a subject area or catalog stitch; a **bounded context** names a local meaning frame; a **discipline** names the composed field-level holon that carries canon, practices, carriers, bridges, and comparison governance. Similar words across domains do not make one discipline; bridge and loss notes are required.

`U.AppliedDiscipline` and `U.Transdiscipline` are C.3-governed subkind values under `U.Discipline`, not separate root ontics. `U.Tradition` and `U.Lineage` are not root U-kinds in C.20 because they name variant, edition, school, or provenance structures inside or across disciplines; write them as ordinary auxiliary values or C.3 local kinds unless a direct governing pattern supplies their own identity relation, admissible use, and E.24.UK settlement.

**Builds on.** **C.2 KD-CAL** (F-G-R and the CL-to-R penalty rule), **A.19/G.0 CG-Spec** (comparability), **F.9 Bridges** (cross-context alignment), **E.10 LEX** (registers & twin labels). **Coordinates with.** **C.21** (Discipline-CHR, field health), **C.23** (Method-SoS-LOG), **F.17-F.18** (UTS).

