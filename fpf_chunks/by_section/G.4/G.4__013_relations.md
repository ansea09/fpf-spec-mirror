---
chunk_kind: "child"
pattern_id: "G.4"
pattern_title: "CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
section_id: "G.4:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/G.4/G.4__013_relations.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "G.4 — CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
  - "G.4:12 — Relations"
line_start: 70041
line_end: 70053
dependencies:
  - "A.10"
  - "A.18"
  - "A.19"
  - "A.21"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.23"
  - "E.17"
  - "E.18"
  - "E.8"
  - "F.17"
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
  - "CAL authoring"
  - "RSCRTriggerKindId"
  - "acceptance clauses"
  - "edition pins"
  - "evidence profiles"
  - "legality gates"
  - "operators"
  - "tri-state admissibility"
  - "Γ-fold hooks"
  - "Φ/Ψ/Φ_plane policy pins"
---

### G.4:12 - Relations

**Builds on:** `G.Core` (and the pattern template discipline in `E.8`).

**Uses:** `G.1` (CG‑FrameContext), `G.2` (SoTA Synthesis Pack), `G.3` (CHR Pack), `G.0` (CG‑Spec legality gate), `A.19` (CN‑Spec), `A.18` (CSLC), `A.10` (provenance anchors), `B.3` (trust/freshness/decay), `E.18` + `A.21` + `F.9`/`F.17`/`E.17` (GateCrossing harness).

**Uses (via Extensions):** `G.6` (EvidenceGraph/Path citation; when `G.4:Ext.EvidenceGraphWiring` is present), `C.18` (NQD), `C.19` (E/E‑LOG), `C.23` (SoS‑LOG).

**Used by:** `G.5` (selector/dispatcher), `G.8` (SoS‑LOG bundles), `G.9` (parity), `G.10` (shipping), `G.11` (refresh orchestration).
**Publishes to:** UTS (public ids and public-id continuity records), RSCR (tests and trigger emissions), `G.5` (handoff manifest), and, as cited payload, shipped packs governed by `G.10`.

**Constrains:** any run‑time LOG implementation that executes CAL operators/flows must treat CAL artifacts as citable specifications and must not re‑invent acceptance semantics.

