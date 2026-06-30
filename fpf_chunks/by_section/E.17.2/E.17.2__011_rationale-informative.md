---
chunk_kind: "child"
pattern_id: "E.17.2"
pattern_title: "TEVB - Typical Engineering Viewpoints Bundle"
section_id: "E.17.2:7"
section_title: "Rationale  (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.2/E.17.2__011_rationale-informative.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "E.17.2 — TEVB - Typical Engineering Viewpoints Bundle"
  - "E.17.2:7 — Rationale  (informative)"
line_start: 73085
line_end: 73095
dependencies:
  - "A.1"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.6.2-A.6.4"
  - "A.7"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "F.18"
  - "U.MultiViewDescribing"
  - "U.ViewpointBundleLibrary"
keywords:
---

### E.17.2:7 - Rationale  *(informative)*

#### E.17.2:7.1 - NQD‑grounded choice of the core four

Part G's NQD discipline treats candidate viewpoint families as points in an N, U, C, and D quality space (Use-Value, Constraint-Fit, Novelty, Diversity_P). Applied to a SoTA-harvested candidate set of engineering viewpoints (Functional, Behavioural, Procedural, Structural-Module, Allocation-Responsibility, Information-Data, Assurance-Safety, Mission-Context, Deployment-Operational, Business-Usage), this yields a small Pareto frontier for *engineering holon* viewpoints. On that frontier, the `F-B-S+R` cut implemented by `{VP.Functional, VP.Procedural, VP.AllocationResponsibility, VP.ModuleInterface}` is the minimal set that:
* spans the Function-Behaviour-Structure ontology used in contemporary design theory while adding an explicit allocation and responsibility concern;
* aligns with the “functional”, “process”, “structural”, and “deployment” clusters recurrent in standards and architecture frameworks;
* stays neutral with respect to domain‑specific qualities (`‑ilities`) and business and mission framing, which are captured in separate Q‑Bundles and governance-oriented viewpoint bundles rather than in TEVB itself.

Other candidates (e.g. dedicated information, assurance, or mission viewpoints) remain important but either duplicate concerns already captured by TEVB (when specialised to engineering holons) or are better modelled as orthogonal quality bundles (C.25) or non-engineering viewpoint bundles (business and governance viewpoint bundles). TEVB therefore pins only the core four and leaves the rest to specialised families.

