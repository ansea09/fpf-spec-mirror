---
chunk_kind: "child"
pattern_id: "G.4"
pattern_title: "CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
section_id: "G.4:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/G.4/G.4__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "3f6714ae3235e0d771dce32835be7696f626d2ee"
heading_path:
  - "G.4 — CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
  - "G.4:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 101319
line_end: 101344
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.18"
  - "A.19"
  - "A.2.1"
  - "A.21"
  - "A.6.1"
  - "B.3"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.23"
  - "E.17"
  - "E.18"
  - "E.8"
  - "F.17"
  - "F.6"
  - "F.9"
  - "G.0"
  - "G.1"
  - "G.10"
  - "G.11"
  - "G.2"
  - "G.3"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.8"
  - "G.9"
  - "G.Core"
keywords:
  - "CAL Pack@CG-Frame"
  - "Context charter"
  - "acceptance clause"
  - "legal flow"
  - "pass \\"
  - "typed operator card"
---

### G.4:8 - Common Anti-Patterns and How to Avoid Them

* **Hidden thresholds.**
  Avoid: embedding cutoffs in CHR prose or in operator descriptions.
  Prefer: `CAL.AcceptanceClause` with explicit ids and pins.

* **Untyped “score(x)”.**
  Avoid: operators with implicit units and untracked legality assumptions.
  Prefer: explicit CHR‑typed operator signatures + cited legality checks.

* **Silent cross‑context reuse.**
  Avoid: importing constructs across Contexts/planes/editions without published crossings.
  Prefer: explicit crossing artifacts and citations; keep CAL pack Context‑local.

* **Acceptance as implementation detail.**
  Avoid: acceptance embedded in tool logic.
  Prefer: publish acceptance as citable CAL artifacts; downstream consumes ids.

* **Exploratory telemetry treated as dominance.**
  Avoid: letting probe/illumination telemetry quietly become a dispatch criterion.
  Prefer: keep it report‑only unless an explicit policy‑bound acceptance clause authorizes promotion.

* **Declaration mistaken for execution.**
  Avoid: treating a CAL card, `TaskMap`, proof-ledger row, worked example, or evidence edge as proof that an operator ran or a verdict obtained.
  Prefer: ground the dated Work through its complete A.15.1/F.6 basis and recover actual direct bindings separately. Compact wording may omit only an unused assignment identifier. Keep the domain-local result and any result episteme separate from both.

