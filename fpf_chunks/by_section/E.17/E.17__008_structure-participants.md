---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:7"
section_title: "Structure & participants"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__008_structure-participants.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:7 — Structure & participants"
line_start: 57055
line_end: 57071
dependencies:
  - "A.6.2"
  - "A.6.3"
  - "A.6.9"
  - "A.7"
  - "E.10"
  - "E.10.D2"
  - "E.10.SEMIO"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.17.AUD"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.8"
  - "F.9"
  - "F.9.1"
  - "U.EffectFreeEpistemicMorphing"
  - "U.EpistemicViewing"
  - "U.MultiViewDescribing"
keywords:
---

### E.17:7 - Structure & participants
```
                 Σ_viewpoints
                      │
            ┌─────────┴─────────┐
            │                   │
        Emit_s(-)           Emit_t(-)      … (family)
            │                   │
U :  X ──f──▶ Y ──g──▶ Z    X ──f──▶ Y ──g──▶ Z
        U.ViewMorph        U.ViewMorph
            │                   │
        Emit_s(f),…         Emit_t(f),…
```
* **Author** chooses `Σ_viewpoints` (declared concerns + conformance rules).
* **MVPK** emits `U.ViewFamily(f)` for each arrow `f`.
* **Declared publication checks** verify that pins, anchors, and IDs are present and that MVPK invariants are respected. Use `OperationalGate(profile)` GateChecks only when a live project gate profile actually governs the next project move.

