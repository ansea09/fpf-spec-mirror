---
chunk_kind: "child"
pattern_id: "A.16.1"
pattern_title: "U.PreArticulationCuePack"
section_id: "A.16.1:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16.1/A.16.1__008_conformance-checklist.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "A.16.1 — U.PreArticulationCuePack"
  - "A.16.1:7 — Conformance Checklist"
line_start: 28797
line_end: 28805
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.2"
  - "A.6.A"
  - "A.7"
  - "B.4.1"
  - "B.5.2.0"
  - "C.16.Q"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
keywords:
  - "candidate route cues"
  - "cue nucleus"
  - "cue pack"
  - "early publication"
  - "pre-articulation"
  - "primary witness"
---

### A.16.1:7 - Conformance Checklist
- `CC-A.16.1-1` A cue pack **SHALL NOT** be presented as a claim, characteristic, method, work occurrence, or route-decision record.
- `CC-A.16.1-2` A cue pack **SHALL** make `cueNucleus` explicit.
- `CC-A.16.1-3` When preservation depends on privileged grounding, `primaryWitnessRef` or `primaryAnchor` **SHALL** be explicit.
- `CC-A.16.1-4` `laneCandidates` and `routeCandidateHints` **MAY** be published early, but `selectedRoute`, `routeRationale`, and route-selection status **SHALL NOT** be smuggled into the cue pack.
- `CC-A.16.1-5` If route-candidate hints are not yet nameable, publication is still admissible only when `preservationRationale` and grounding make the preservation need explicit.
- `CC-A.16.1-6` Language-state, anchoring, and representation-factor details **MAY** be referenced; use `C.2.LS` for the facet profile, `C.2.4` and `C.2.6` for anchoring, `C.2.5` for closure degree, and `C.2.7` for representation factors.
- `CC-A.16.1-7` A cue pack **SHALL NOT** claim that an endpoint test passed or that a stronger use is admitted; use the applicable endpoint pattern to test and publish that later result.

