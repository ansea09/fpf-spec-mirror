---
chunk_kind: "child"
pattern_id: "G.3"
pattern_title: "CHR Authoring for a CG‑Frame: Characteristics, Scales, Levels, Coordinates"
section_id: "G.3:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/G.3/G.3__002_problem-frame.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "G.3 — CHR Authoring for a CG‑Frame: Characteristics, Scales, Levels, Coordinates"
  - "G.3:1 — Problem frame"
line_start: 100677
line_end: 100686
dependencies:
  - "A.10"
  - "A.15.3"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CHR"
  - "B.3"
  - "B.3.4"
  - "C.16"
  - "C.18"
  - "C.19"
  - "E.10"
  - "E.5.1"
  - "E.5.3"
  - "F.0.1"
  - "F.1"
  - "F.17"
  - "F.18"
  - "F.9"
  - "G.0"
  - "G.1"
  - "G.10"
  - "G.11"
  - "G.2"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.Core"
keywords:
  - "CHR Pack@CG-Frame"
  - "CHR authoring"
  - "CSLC lawfulness"
  - "RSCRTriggerKindId"
  - "ReferencePlane"
  - "characteristics"
  - "coordinates"
  - "edition pins"
  - "levels"
  - "scales"
  - "typed measurement"
  - "Φ/CL policy pins"
---

### G.3:1 - Problem frame

A team is defining or evolving a `CG‑Frame` (via `G.1`) and has plural, competing SoTA traditions and constructs (via `G.2`). The team needs a *admissibility-ready CHR publication* that makes downstream work possible without hidden semantic drift:

* **CAL authoring (`G.4`)** needs typed, admissible operands and guard/legality surfaces to build admissibility and acceptance rules (thresholds and policy cut‑offs remain governed by CAL).
* **Selector/dispatch (`G.5`)** needs CHR‑typed quantities and explicit provenance pins so selection can remain set-returning and auditable under admissible orders.
* **Reuse beyond the defining source or use** must name the exact characteristic and scale editions, bearer, scope and validity window, reference plane, evidence, and intended downstream use. Cite an `F.9` relation only when it actually obtains between the named `F.17` cells; any claim that relies on the relation for this use remains a separate `F.18` use and reliance claim.

The resulting publication is a **CHR Pack** that is **CG‑Frame‑scoped**, **notation‑independent**, and **UTS‑published**, with explicit edition/policy pins sufficient for reproducibility and RSCR.

