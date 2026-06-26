---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "Static and Regression Conformance Harness for Unification"
section_id: "F.15:9"
section_title: "Static conformance rules for cross-context material"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__011_static-conformance-rules-for-cross-context-material.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "F.15 — Static and Regression Conformance Harness for Unification"
  - "F.15:9 — Static conformance rules for cross-context material"
line_start: 84832
line_end: 84879
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "B.3"
  - "E.10.D1"
  - "E.10.D2"
  - "E.17"
  - "F.1"
  - "F.1-F.14"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
  - "U.BoundedContext"
  - "U.Role"
keywords:
  - "SenseCell testing"
  - "acceptance tests"
  - "regression tests"
  - "static checks"
  - "validation"
---

### F.15:9 - Static conformance rules for cross-context material

Cross-context rules connect local material without collapsing locality.

**SCR-F15-S7 (Single-cell RoleDescription).**
`RoleDescription tau -> refersTo(tau, one SenseCell) and describes(tau, one local U.Role).`
A RoleDescription is not a status template, evidence template, source template, publication template, or role assignment.

**SCR-F15-S8 (Name discipline).**
`RoleDescription tau or NameCard n -> name obeys F.5, F.8, F.14, and F.18 as applicable.`
Naming follows kind recovery before durable naming.

**SCR-F15-S9 (Row spans contexts).**
`Row rho lists cells cell_i -> at least two distinct contexts occur.`
A row of one context is not cross-context unification.

**SCR-F15-S10 (Row purity).**
`Row rho -> each listed item is one SenseCell.`
No cell is a pre-merged bundle, hidden bridge, or global meaning.

**SCR-F15-S11 (Reuse before minting).**
`Proposed row rho2 overlaps intended use of row rho -> reuse rho or record the F.8 mint decision.`
New rows need a visible difference, not merely a new label.

**SCR-F15-S12 (Bridge explicitness).**
`C1 != C2 and relation asserted between cells -> BridgeCard states cells, kind, direction, CL, loss, witness, and admitted use.`
A cross-context relation appears as a Bridge Card before it is consumed by rows, names, assurance, or downstream claims.

**SCR-F15-S13 (Bridge locality).**
`BridgeCard beta -> beta relates cells from different contexts.`
Within one context, use clustering or local relation discipline rather than a bridge.

**SCR-F15-S14 (Status window honesty).**
`Status family Sigma varies by time, scale, phase, confidence, or use -> F.10 names value or window; no new status family by adjective alone.`
Temporal and scale variation does not create status ontology by suffix.

**SCR-F15-S15 (Role-relation preservation).**
`role bundle or incompatibility expression is live -> A.2.7 states it; no fused RoleDescription is minted by convenience.`
Role-relation expressions are not role assignments and do not prove performed work.

**SCR-F15-S16 (Direct-pattern boundary for non-unification claims).**
`Slice contains assignment, work, evidence, source, publication, assurance, gate, decision, method, capability, or policy claim -> cite the direct governing pattern.`
F.15 checks whether the slice is safe to compose; it does not decide those claims.

**SCR-F15-S17 (Public or cross-context naming admission).**
`Name is public, cross-context, or term-sheet-facing -> F.17 and F.18 admit it after kind recovery.`
Public reuse is not created by repeated local labels.

