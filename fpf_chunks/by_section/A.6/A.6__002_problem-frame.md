---
chunk_kind: "child"
pattern_id: "A.6"
pattern_title: "Signature Stack & Boundary Discipline"
section_id: "A.6:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6/A.6__002_problem-frame.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "A.6 — Signature Stack & Boundary Discipline"
  - "A.6:1 — Problem frame"
line_start: 9399
line_end: 9420
dependencies:
  - "A.10"
  - "A.15"
  - "A.2.3"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.6"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.B"
  - "A.6.C"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.26"
  - "C.28"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.19"
  - "E.8"
  - "F.18"
  - "F.9"
  - "U.Mechanism"
  - "U.Signature"
  - "U.View"
keywords:
  - "Confuses deontics with mathematical admissibility"
  - "Rewrite as declarative predicate"
  - "Work versus non-Work effect"
  - "acceptance"
  - "actual occurrence"
  - "and evidence"
  - "atomic L/A/D/E claims"
  - "delivery"
  - "in invariants"
  - "publication face"
  - "reference predicate IDs from CC when needed"
  - "separate result"
  - "signature and mechanism declarations"
  - "six-way authority-word branch"
  - "undermines auditability"
  - "“MUST” appears inside Definition: blocks"
---

### A.6:1 - Problem frame

Boundaries are where architecture lives: at the edge of a theory, an API, a protocol, a hardware connector, an organisational interface, or a published model. FPF already has the core building blocks to describe such edges:

* `U.Signature` as a *public, law‑governed declaration* (with Vocabulary, Laws, Applicability).
* `U.Mechanism` as a specialization that introduces operational “entry gates” (AdmissibilityConditions) and additional operational blocks (Transport, Audit, etc.).
* Multi-view describing through E.17.0 `MultiViewDescribing`, plus separate E.17 publication discipline for selected epistemes, face uses, forms, and carriers.
* Strict separation of **EntityOfConcern vs Description episteme vs publication carrier** so we do not accidentally attribute agency or work to an episteme, or treat a file as the entity, claim, work, evidence, or decision.

Yet boundary descriptions in practice fail in a predictable way: authors blend several fundamentally different kinds of claims into one undifferentiated contract paragraph. The result is brittle architecture: signatures become entangled with runtime gates, deontic language is mixed into mathematical invariants, and “effects” are asserted without any disciplined carrier and evidence story.

This cluster overview makes one disciplined move:

1. Treat a boundary as a **stack of boundary layers** (Signature → Mechanism → actual occurrences and their separately governed consequences/evidence) plus publication views and faces, and
2. Provide a **boundary discipline matrix** (2×2) that classifies statements by boundary layer, so evolution remains controlled and substitutions are possible.

*Terminology note (informative):* In this pattern:
* **Layer** names a stratum in the boundary stack (Signature → Mechanism → actual occurrences, separately governed consequences/evidence → Publication).
* **View** (`U.View`) is the same C.2.1 episteme individual when E.17.0 conformance to at least one exact viewpoint episteme obtains; it is not a projection operation, publication file, or document.
* **Viewpoint** (`U.Viewpoint`) is the same C.2.1 episteme individual when the fixed E.17.0 viewpoint-convention conditions obtain; its accountability use does not replace those membership conditions.
* **Face** (MVPK sense) is one named publication-use class (`PlainView`, `TechCard`, `InteropCard`, or `AssuranceLane`). A face may select an episteme that independently has `U.View` membership, but the face, publication form, rendering, and carrier are not that view. Do not coin “signature or mechanism ...Surface” terms; use publication face, form, unit, carrier, and rendering terms only when publication use is live.

