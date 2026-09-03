---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:9"
section_title: "E.18 LEX Discipline (registration)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__012_e-18-lex-discipline-registration.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:9 — E.18 LEX Discipline (registration)"
line_start: 86035
line_end: 86038
dependencies:
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.6.RCD"
  - "A.7"
  - "C.29"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.17"
  - "E.18.1"
  - "E.18.2"
  - "E.18.NET"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.18:9 - E.18 LEX Discipline (registration)
Register Tech tokens (ASCII) used by this pattern with twin labels: `TransformationFlowStructure`, `TransformationFlowValuation`, `StructuralReinterpretation`, `OperationalGate`, `GateCrossing`, `CrossingRef`, `CrossingBundle`, `GateProfile`, `GateCheckRef`, **`GateCheckKind`**, `DecisionLog`, `USM.CompareGuard`, `USM.LaunchGuard`, `FlowPositionRef`, `SubflowRef`, `FlowEmbed`, `SentinelId`, `PathSliceId`, `SliceRefresh`, `FinalizeLaunchValues`, `VALATA`. `Bridge`, `BridgeCard`, and `CL` retain their F.9/C.2.1 meanings and are not E.18 crossing tokens. Reference MVPK E.17 naming for faces.
**CtxState Extension Registry.** Register any extra CtxState slot beyond ⟨L,P,E⃗,D⟩ with: slot id, informal intent, partial‑order rule (with neutral or absorbing), SquareLaw compatibility note, and the Gate profile or profiles allowed to change it. Absence of registration ⇒ **non‑conformant**.

