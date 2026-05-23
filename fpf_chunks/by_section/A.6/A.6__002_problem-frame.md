---
chunk_kind: "child"
pattern_id: "A.6"
pattern_title: "Signature Stack & Boundary Discipline"
section_id: "A.6:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6/A.6__002_problem-frame.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.6 — Signature Stack & Boundary Discipline"
  - "A.6:1 — Problem frame"
line_start: 6879
line_end: 6900
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.20"
  - "A.21"
  - "A.6"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.B"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.26"
  - "C.26.1"
  - "C.28"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.EFP"
  - "E.19"
  - "E.8"
  - "F.18"
  - "F.9"
  - "U.EpistemicViewing"
  - "U.Mechanism"
  - "U.MultiViewDescribing"
  - "U.Signature"
  - "U.View"
  - "U.Viewpoint"
  - "U.Work"
keywords:
  - "A.6.B L/A/D/E claims"
  - "Confuses deontics with mathematical admissibility"
  - "Rewrite as declarative predicate"
  - "authority-wording split"
  - "boundary"
  - "boundary claim-classification fields"
  - "in invariants"
  - "probe/order/frame/export/state-reading claims"
  - "promise/commitment/API/policy wording"
  - "reference predicate IDs from CC when needed"
  - "register-backed status boundary"
  - "signature stack"
  - "undermines auditability"
  - "“MUST” appears inside Definition: blocks"
---

### A.6:1 - Problem frame

Boundaries are where architecture lives: at the edge of a theory, an API, a protocol, a hardware connector, an organisational interface, or a published model. FPF already has the core building blocks to describe such edges:

* `U.Signature` as a *public, law‑governed declaration* (with Vocabulary, Laws, Applicability).
* `U.Mechanism` as a specialization that introduces operational “entry gates” (AdmissibilityConditions) and additional operational blocks (Transport, Audit, etc.).
* Multi‑view publication discipline via `U.MultiViewDescribing` (views + viewpoints).
* Strict separation of **Object vs Description vs Carrier** so we do not accidentally attribute agency or work to an episteme (or treat a file as “the thing”).

Yet boundary descriptions in practice fail in a predictable way: authors blend several fundamentally different kinds of claims into one “contract soup”. The result is brittle architecture: signatures become entangled with runtime gates, deontic language is mixed into mathematical invariants, and “effects” are asserted without any disciplined carrier/evidence story.

This cluster overview makes one disciplined move:

1. Treat a boundary as a **stack of boundary layers** (Signature → Mechanism → Work/Evidence carriers) plus publication views and faces, and
2. Provide a **boundary discipline matrix** (2×2) that routes statements to the correct layer, so evolution remains controlled and substitutions are possible.

*Terminology note (informative):* In this pattern:
* **Layer** names a stratum in the boundary stack (Signature → Mechanism → Work/Evidence carriers → Publication).
* **View** (`U.View`) is an episteme-lane projection, not a file/document.
* **Viewpoint** (`U.Viewpoint`) is an intensional accountability spec that constrains views.
* **Face** (MVPK sense) is a named publication view kind (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`) whose rendering lives on a `PublicationSurface` (carrier). Do not coin “signature/mechanism …Surface” terms; “Surface” is reserved for publication surfaces (L‑SURF).

