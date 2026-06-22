---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:7"
section_title: "CL scale and admitted-use thresholds"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__009_cl-scale-and-admitted-use-thresholds.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:7 — CL scale and admitted-use thresholds"
line_start: 78470
line_end: 78487
dependencies:
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.9"
  - "B.3"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "C.29"
  - "E.10.D1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
keywords:
  - "Bridge-supported use"
  - "CL"
  - "bridge"
  - "bridge reading"
  - "cross-context alignment"
  - "direction"
  - "loss notes"
  - "state export"
  - "weakest-link scope"
---

### F.9:7 - CL scale and admitted-use thresholds

| CL | Name | Intuition | Typical loss | Admitted use |
| --- | --- | --- | --- | --- |
| 0 | Opposed | Intentionally contrastive or disjoint | incompatibility | contrastive explanation only |
| 1 | Comparable | Shared label can orient readers, but senses differ materially | material sense divergence | Naming-only |
| 2 | Translatable | Bounded loss with examples and counter-examples | stated losses | Naming-only; role-description naming or other same-family name reuse; no direct assignment or work attribution |
| 3 | Near-identity | Invariants match; no material counter-example | profile-level only | Type-structure rows and other invariant-preserving same-family uses |

Thresholds:

* A Naming-only row requires `CL >= 1`.
* A Role-description naming row requires `CL >= 2`, the same Role `senseFamily`, and stated local-role losses. It still does not create a `U.RoleAssignment`.
* A Type-structure row requires `CL = 3` and matched invariants such as acyclicity, anti-symmetry, unit transform, cardinality, or signature-preserving relation shape.
* Interpretation Bridges remain Explanation-only regardless of `CL`.

B.3 may convert `CL` into an assurance penalty when a cross-context claim uses a Bridge.

