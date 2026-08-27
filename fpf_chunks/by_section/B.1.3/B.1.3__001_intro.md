---
chunk_kind: "child"
pattern_id: "B.1.3"
pattern_title: "Γ_epist - Knowledge‑Specific Aggregation"
section_id: "B.1.3:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.3/B.1.3__001_intro.md"
commit_sha: "3f6714ae3235e0d771dce32835be7696f626d2ee"
heading_path:
  - "B.1.3 — Γ_epist - Knowledge‑Specific Aggregation"
  - "B.1.3:intro — Intro"
line_start: 36057
line_end: 36072
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.15.PROD"
  - "A.6.1"
  - "B.1"
  - "B.1.1"
  - "B.1.4"
  - "B.1.6"
  - "B.2"
  - "B.3"
  - "C.2"
  - "C.2.1"
  - "E.17"
  - "E.24.PUB"
  - "F.6"
  - "F.9"
  - "U.Work"
keywords:
  - "KD-CAL"
  - "epistemic"
  - "knowledge aggregation"
  - "provenance"
  - "trust"
---

## B.1.3 - Γ_epist - Knowledge‑Specific Aggregation

**At a glance.** Use B.1.3 to compose exact `U.Episteme` inputs into one knowledge aggregate while preserving provenance, conceptual fit, context, and conservative assurance bounds.

**Use this when.** Use this pattern when a named synthesis or compilation use depends on how claims, models, datasets, or arguments are combined, and the aggregation must keep source, mapping, conflict, order, and temporal qualifications inspectable.

**Not this pattern when.** Use C.2.1 for episteme identity and edition continuity, A.14 for a proper temporal restriction of one unchanged episteme, A.15.1 for Work parts or occurrences, B.1.4 for a bounded aggregation of already recovered order or temporal relations, and B.3 for the assurance claim that consumes the aggregate.

**What changes in practice.** Identify every input episteme and mapping before folding; preserve provenance and conflicts; and return identity, edition, temporal restriction, Work, publication, and assurance questions to their subject patterns.

> **► decided‑by: A.14 Advanced Mereology**
**A.14/C.2.1 compliance —** Use **ConstituentOf** for semantic parts and **PortionOf** only for quantitative splits of texts/data with declared μ. Use `PhaseOf` only for a proper interval of one unchanged C.2.1 episteme. When a MethodDescription or document episteme's claim content, EntityOfConcern, or effective ReferenceScheme changes, identify another episteme and assert `EpistemeEditionRelation` only when its historical-continuation predicate obtains. Work segmentation uses A.15.1; no **ComponentOf** is used here.

> **Plain‑English headline.**
> **Γ\_epist** composes **epistemic holons** (claims, models, datasets, arguments) into a **single episteme** while preserving **provenance**, applying **conservative trust bounds** (B.3 F/G/R), and penalizing **poor conceptual fit** via **congruence levels (CL)**. It is **not** a physical sum; it is a **semantic and evidential fold**.

