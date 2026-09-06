---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:6"
section_title: "Bridge kinds"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__008_bridge-kinds.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:6 — Bridge kinds"
line_start: 95782
line_end: 95804
dependencies:
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.9"
  - "A.6.REL"
  - "B.3"
  - "C.2.1"
  - "C.26.1"
  - "C.26.2"
  - "C.29"
  - "C.3"
  - "E.10.ROLE"
  - "E.17.ID.CR"
  - "E.24.PUB"
  - "F.0.1"
  - "F.10"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9.1"
keywords:
  - "A.10/B.3 reliance"
  - "LocalSenseClaim> projections"
  - "different <ReferenceScheme"
  - "exact F.17 SchemeSenseCell endpoints"
  - "inverse/composition checks"
  - "obtaining Bridge"
  - "optional CL evidence-strength shorthand"
  - "optional card"
  - "quantum/coarsening exit"
  - "relation-semantic profile"
  - "separate C.2.1 bounded-use claim"
---

### F.9:6 - Bridge kinds

A Bridge kind classifies the direct semantic relation tested by a profile. It says what correspondence or difference obtains; it does not settle any proposed use.

#### F.9:6.1 - Same-family relation kinds

1. **Equivalence** - the endpoint senses have the same extension and relevant intension under the stated relation condition. The relation is symmetric and should be rare. A later use still names its direction, rule, and tolerance.
2. **Narrower-than** - the source sense is properly included in the receiving sense. The relation is asymmetric.
3. **Broader-than** - the source sense properly includes the receiving sense. The relation is asymmetric.
4. **Partial-overlap** - the senses have a non-empty intersection, while each has cases excluded by the other. The relation is symmetric.
5. **Disjoint** - the senses have no common admissible case under the stated readings. The relation is symmetric.

For inclusion, a narrower-to-broader proposed use is usually easier to justify than the reverse, but neither direction follows from the relation alone. A broader-to-narrower proposal normally needs refined endpoint cells and a separately tested Bridge plus a separately warranted bounded-use claim.

#### F.9:6.2 - Cross-family relation kinds

These kinds state semantic correspondence across different `senseFamily` readings. They explain a connection; they do not create substitution, evidence authority, policy force, or a receiving occurrence.

6. **Design-spec-to-run-occurrence** - a design sense corresponds to a run-time occurrence sense while remaining different in temporal and realization status.
7. **Measurement-evidence-for** - a measurement sense corresponds to the measured aspect of another sense. The kind is semantic; actual evidential support remains with A.10 or B.3.
8. **Policy-constraint-on** - a policy or deontic sense corresponds to a constrained behavioral sense. Actual obligation, permission, or authority remains with the policy or deontic governor.
9. **Viewpoint-correspondence** - a sense used in one view corresponds to a sense used in another view over an EntityOfConcern. View, description, publication, and source-use claims keep their subject patterns.

