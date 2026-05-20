---
chunk_kind: "child"
pattern_id: "C.25"
pattern_title: "Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
section_id: "C.25:17"
section_title: "Migration and Boundary Notes"
source_path: "FPF-Spec.md"
output_path: "by_section/C.25/C.25__018_migration-and-boundary-notes.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "C.25 — Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
  - "C.25:17 — Migration and Boundary Notes"
line_start: 42527
line_end: 42564
dependencies:
  - "A.15"
  - "A.16.0"
  - "A.18"
  - "A.2.6"
  - "A.6.1"
  - "A.6.Q"
  - "B.3"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.2.2a"
  - "C.26.3"
  - "F.9"
  - "F.9.1"
keywords:
  - "admissible quality-family use"
  - "characteristic plus scope"
  - "endpoint classification"
  - "failure mode"
  - "ility"
  - "mechanism/status slots"
  - "proxy metric"
  - "quality bundle"
  - "quality family"
  - "viability envelope"
---

### C.25:17 - Migration and Boundary Notes

#### C.25:17.1 - Migration from bare quality requirements

Legacy phrases such as *quality requirement*, *security requirement*, or *availability requirement* should not survive as bare heads when the underlying endpoint is actually a characteristic or bundle. The migration rule is:

- choose the endpoint shape first,
- then bind the requirement or commitment to that explicit head.

`A.6.Q` may still be the entry repair, but `C.25` is the resting place once the engineering quality family has been made explicit.

#### C.25:17.2 - Boundary to assurance penalties

Cross-context transport, bridge loss, or plane mismatch do not change whether the endpoint is one characteristic or one bundle. Those effects route to `R` and its penalties. `C.25` therefore should not be used to hide assurance degradation inside the quality-family ontology.

#### C.25:17.3 - Boundary to publication convenience

A report, summary surface, or executive summary may expose only one slice of a Q-Bundle, but the underlying authoring structure remains the bundle. Publication convenience is not a reason to collapse the ontology at the source.

#### C.25:15.5 - Serviceability and supportability

Serviceability, supportability, and adjacent family labels often look simple in prose but become composite as soon as operational use is declared. A lawful bundle for this family may need:

- support-scope slices,
- measured restoration or service intervals,
- mechanism slots for support mechanisms, access discipline, or replacement procedures,
- and evidence from service traces or support records.

The lesson is the same as elsewhere in `C.25`: once the truth of the family claim depends on several typed contributors, the bundle should stay explicit.

#### C.25:17.4 - Boundary to description-side and selector-side evaluation

`C.25` is for engineering quality families whose bearer is a system-side, promise-side, or explicit quality-bearing artifact. It does **not** automatically cover:

- viewpoint-fit or architecture-description adequacy claims, which may belong in viewpoint or evaluative-ascription patterns,
- or selector/objective heads where *quality* means use-value under a search or portfolio frame.

This boundary matters because the same word *quality* appears across those zones. `A.6.Q` may be the common repair entry, but the resting endpoint depends on what is actually being evaluated.
