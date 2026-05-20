---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:2"
section_title: "Problem Frame (DesignRunTag split; crossing-visible)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__003_problem-frame-designruntag-split-crossing-visible.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:2 — Problem Frame (DesignRunTag split; crossing-visible)"
line_start: 41344
line_end: 41351
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

**method‑first stance**
In FPF a **Problem** exists when a Holder or external **Transformer** cannot cite a known **Method** (or specialisation thereof) that satisfies the current **TaskSignature** under the declared **ScopeSlice(G)**. Problem‑solving therefore entails **strategizing** (selecting or synthesising a method). The resulting **strategy/policy** is a composition under **G.5/E/E‑LOG** and **is not** a new kernel type.
**Unknown‑first discipline.** Author S2 with `unknown` traits rather than coercions; **SoS‑LOG** branches MUST specify `{admit|degrade|abstain|sandbox}` handling for `unknown` via closed enums registered at UTS.

Un‑typed "problems" collapse into **informal prose**; selectors cannot **filter or abstain** admissibly; acceptance-gate thresholds leak into scoring; cross‑Context reuse is by name, not Bridge. We need a Context‑local descriptor that (i) obeys **MM‑CHR legality** (Scale/Unit/Polarity proven before any aggregation), (ii) records **Assurance lanes (TA/VA/LA)** per **A.10** and **ReferencePlane**, (iii) carries **tri‑state unknowns** explicitly, and (iv) **publishes crossing attestations** (**BridgeCard + UTS row**) with **Φ(CL)/Φ_plane** policy‑ids.

