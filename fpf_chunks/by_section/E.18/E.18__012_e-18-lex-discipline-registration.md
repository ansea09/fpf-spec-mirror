---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:9"
section_title: "E.18 LEX Discipline (registration)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__012_e-18-lex-discipline-registration.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:9 — E.18 LEX Discipline (registration)"
line_start: 74763
line_end: 74766
dependencies:
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.7"
  - "C.29"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.17"
  - "E.18.1"
  - "E.18.2"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "P2W support"
  - "composition"
  - "crossings"
  - "flow valuation"
  - "guards"
  - "selected transformations"
  - "transformation flow structure"
---

### E.18:9 - E.18 LEX Discipline (registration)
Register Tech tokens (ASCII) used by this pattern with twin-labels: `TransformationFlowStructure`, `TransformationFlowValuation`, `StructuralReinterpretation`, `OperationalGate`, `GateProfile`, `GateCheckRef`, **`GateCheckKind`**, `DecisionLog`, `USM.CompareGuard`, `USM.LaunchGuard`, `KindBridge`, `SubflowRef`, `FlowEmbed`, `SentinelId`, `PathSliceId`, `SliceRefresh`, `FinalizeLaunchValues`, `VALATA`. Register ASCII spelling **`CLKind`** for Plain display `CL^k` (cf. `CLPlane` for `CL^plane`). Reference MVPK E.17 naming for faces.
**CtxState Extension Registry.** Register any extra CtxState slot beyond ⟨L,P,E⃗,D⟩ with: slot id, informal intent, partial‑order law (with neutral or absorbing), SquareLaw compatibility note, and the Gate profile or profiles allowed to change it. Absence of registration ⇒ **non‑conformant**.

