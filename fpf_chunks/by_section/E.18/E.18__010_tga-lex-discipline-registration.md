---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transduction Graph Architecture (E.TGA)"
section_id: "E.18:9"
section_title: "TGA LEX discipline (registration)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__010_tga-lex-discipline-registration.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "E.18 — Transduction Graph Architecture (E.TGA)"
  - "E.18:9 — TGA LEX discipline (registration)"
line_start: 59942
line_end: 59945
dependencies:
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.7"
  - "E.10"
  - "E.17"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "CSLC normalize-then-compare"
  - "CV⇒GF (ConstraintValidity → GateFit)"
  - "DesignRunTag"
  - "MVPK faces"
  - "OperationalGate(profile)"
  - "PathSlice/Sentinel refresh"
  - "Set-return selection"
  - "SquareLaw"
  - "UNM declaration locus"
  - "edge=U.Transfer (single-edge kind)"
  - "nodes=morphisms"
  - "transduction graph"
---

### E.18:9 - TGA LEX discipline (registration)
Register Tech tokens (ASCII) used by this architecture with twin‑labels: `U.TransductionGraph`, `U.TransductionFlow`, `StructuralReinterpretation`, `OperationalGate`, `GateProfile`, `GateCheckRef`, **`GateCheckKind`**, `DecisionLog`, `USM.CompareGuard`, `USM.LaunchGuard`, `KindBridge`, `SubflowRef`, `FlowEmbed`, `SentinelId`, `PathSliceId`, `SliceRefresh`, `FinalizeLaunchValues`, `VALATA`. Add an ASCII alias **`CLKind`** ↔ Plain `CL^k` (cf. `CLPlane` ↔ `CL^plane`). Reference MVPK E.17 naming for faces.
**CtxState Extension Registry.** Register any extra CtxState slot beyond ⟨L,P,E⃗,D⟩ with: slot id, informal intent, partial‑order law (with neutral/absorbing), SquareLaw compatibility note, and the owning Gate profile(s) that may change it. Absence of registration ⇒ **non‑conformant**.

