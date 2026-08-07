---
chunk_kind: "child"
pattern_id: "G.0"
pattern_title: "Frame Standard and Comparability Governance — CG‑Spec"
section_id: "G.0:5"
section_title: "Archetypal Grounding — Tell–Show–Show; System / Episteme"
source_path: "FPF-Spec.md"
output_path: "by_section/G.0/G.0__006_archetypal-grounding-tell-show-show-system-episteme.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "G.0 — Frame Standard and Comparability Governance — CG‑Spec"
  - "G.0:5 — Archetypal Grounding — Tell–Show–Show; System / Episteme"
line_start: 98246
line_end: 98274
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "B.3"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.23"
  - "E.10"
  - "E.5"
  - "E.5.2"
  - "F.9"
  - "G.1"
  - "G.2"
  - "G.3"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.Core"
keywords:
  - "CG-Frame"
  - "CG-Spec"
  - "CL-routing"
  - "ComparatorSet"
  - "MinimalEvidence"
  - "RSCRTriggerKindId"
  - "ReferencePlane"
  - "ScaleComplianceProfile (SCP)"
  - "admissibility gate"
  - "edition pins"
  - "Γ-fold"
  - "Φ(CL)"
  - "Φ_plane"
---

### G.0:5 - Archetypal Grounding — Tell–Show–Show; System / Episteme

#### G.0:5.1 - Archetype 1: System comparability under mixed evidence and unit constraints

**Tell.** Two labs compare energy efficiency results of a physical system where measurements use different rigs and units, and some evidence is missing.

**Show (failure without CG‑Spec).** The team averages an ordinal safety rating, mixes units (“kWh” vs “MJ”), and silently treats missing lanes as zeros. Cross-lab reuse happens without explicit bridge and loss notes, so selection becomes a black box.

**Show (repair with CG‑Spec).** A conformant `CG‑Spec`:

* pins the lawful comparator(s) (e.g., unit-aligned ratio comparisons only; ordinal comparisons are order-only),
* declares `MinimalEvidence` lanes/carriers and freshness windows per characteristic,
* declares explicit failure behavior wiring (tri-state semantics delegated to `G.Core`),
* exposes crossing pins (bridge ids + CL/policy ids) when reuse across rigs is attempted,
* publishes the pinned editions so parity/refresh can detect drift.

#### G.0:5.2 - Archetype 2: Epistemic comparability for selected-set publication across traditions

**Tell.** A team selects an R&D set using multiple evaluation traditions: safety assurance, cost models, and readiness heuristics.

**Show (failure without CG‑Spec).** The team collapses partial orders into a single score, hides the threshold policy in code, and cannot explain why cross-tradition penalties changed between runs.

**Show (repair with CG‑Spec).** A conformant `CG‑Spec`:

* defines a comparator bundle (e.g., Pareto dominance + explicit lexicographic tiebreaks where lawful),
* pins `CNSpecRef.edition` and the editioned segments (`ComparatorSetRef.edition`, `SCPRef.edition`, `MinimalEvidenceRef.edition`),
* makes `AcceptanceStubs` explicit as templates while locating thresholds in CAL (G.4),
* ensures RSCR triggers are emitted when comparator or policy pins change.

