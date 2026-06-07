---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:2"
section_title: "Problem Frame (DesignRunTag split; crossing-visible)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__003_problem-frame-designruntag-split-crossing-visible.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:2 — Problem Frame (DesignRunTag split; crossing-visible)"
line_start: 43763
line_end: 43770
dependencies:
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.1"
  - "C.23"
  - "E.10"
  - "E.18"
  - "G.0"
  - "G.4"
  - "G.5"
keywords:
  - "Problem‑CHR"
  - "ScopeSlice(G)"
  - "TaskKind"
  - "TaskSignature"
  - "specialization anchor"
  - "unknown handling"
---

### C.22:2 - Problem Frame (DesignRunTag split; crossing-visible)

**Selector-facing problem case**
For selector-facing `C.22` use, a problem case is live when the problem-side representation is stable enough to attach or emit a minimal `TaskSignature` for eligibility, acceptance, and policy-governed selection. Method absence, method contestability, or method-family ambiguity is a common downstream reason for `C.22` use, but it is not the only reason a `ProblemCard@Context` may be needed upstream. `C.22` therefore does not define problemhood by method absence; it defines the downstream typed attachment record used once problem-side readiness is truthful. When the live question is still a symptom, contested framing, stale context, set-derived candidate, opportunity cue, or preselected work item, use `C.22.2` before binding one chosen `TaskSignature`. When selection or synthesis of a method becomes live, strategy or policy is governed by `G.5` and `E/E-LOG`; `C.22` use does not introduce a strategy or policy kernel type.
**Unknown‑first discipline.** Author S2 with `unknown` traits rather than coercions; **SoS‑LOG** branches MUST specify `{admit|degrade|abstain|sandbox}` handling for `unknown` via closed enums registered at UTS.

Un‑typed "problems" collapse into **informal prose**; selectors cannot **filter or abstain** admissibly; acceptance-gate thresholds leak into scoring; cross‑Context reuse is by name, not Bridge. We need a Context‑local descriptor that (i) obeys **MM‑CHR admissibility** (Scale/Unit/Polarity proven before any aggregation), (ii) records **Assurance lanes (TA/VA/LA)** per **A.10** and **ReferencePlane**, (iii) carries **tri‑state unknowns** explicitly, and (iv) records crossing attestations (**BridgeCard + UTS row**) with **Φ(CL)/Φ_plane** policy‑ids.

