---
chunk_kind: "child"
pattern_id: "A.6.9"
pattern_title: "Cross-Context Sameness Disambiguation - Repairing cross-context \"same / equivalent / align\" via explicit Bridges (RPR-XCTX)"
section_id: "A.6.9:section-001"
section_title: "E.24.UK settlement"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.9/A.6.9__002_e-24-uk-settlement.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "A.6.9 — Cross-Context Sameness Disambiguation - Repairing cross-context \"same / equivalent / align\" via explicit Bridges (RPR-XCTX)"
  - "A.6.9:section-001 — E.24.UK settlement"
line_start: 17424
line_end: 17440
dependencies:
  - "A.6.6"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.3.3"
  - "E.10"
  - "E.10.D1"
  - "E.10.U9"
  - "E.17"
  - "E.19"
  - "F.0.1"
  - "F.5"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "CL"
  - "SenseCells"
  - "alignment"
  - "bridge"
  - "cross-context sameness"
  - "direction"
  - "loss notes"
  - "mapping"
  - "substitution licence"
  - "weakest-link"
---

### E.24.UK settlement

A.6.9 does not admit `U.CrossContextSamenessDisambiguation` as a durable U-kind. The pattern governs cross-context sameness disambiguation as a relational precision-restoration pattern. The durable values it uses are Bridge, BridgeKind, direction, congruence level, loss, scope, EntityOfConcern, Description episteme, carrier, and direct C.3/F.9/E.17 values when current; A.6.9-specific bridge-card qualifiers such as `Γ_time` and `facetSpan` are annotation slots, not new kernel relations.

> **Type:** Architectural (A) — A.6.P specialisation (RPR)
> **Status:** Stable
> **Normativity:** Normative
> **Placement:** A.6 cluster; immediately after A.6.8
> **Builds on:** A.6.P (RPR); F.0.1:2.3 (Explicit Bridge Principle); E.10.D1 (Context discipline); E.10.U9 (Alignment/Bridge lexical discipline); F.9 (Bridge discipline + reasoning primitives); F.7/F.8 (Concept‑Set rows & weakest‑link); F.5 (labels); A.7 (Strict Distinction: lanes + stance hygiene); E.19 (normative precision)
> **Coordinates with:** E.17 (Viewpoints / Views / Correspondences, when the prose is really about views/projections); C.3.3 (KindBridge, when the claim is about kind/classification transfer); A.6.6 (Identification/indexing, when the umbrella is really about IDs); Concept‑Set row scope rules; E.10 lexical SD (umbrella tokens); B.3 penalty conversion (if used)

Use this pattern for any document, table row, or boundary statement that asserts cross-context sameness, compatibility, alignment, mapping, or correspondence between SenseCells, or collapses A.7 lanes or `CHR:ReferencePlane`s under umbrella wording such as "same", "equivalent", or "aligned".

This pattern reuses `Bridge`, `BridgeKind`, `dir`, `CL`, `Loss`, and `scope`. A.6.9-specific bridge-card qualifiers such as `Γ_time` and `facetSpan` are annotation slots that make the bridge judgement reviewable; they do not alter the kernel Bridge predicate and do not mint new kernel relations.

When a bridge scope is broader than Naming-only, or when an edit broadens the scope or increases the declared `CL`, provide `witnessRefs` such as a review note, evaluation suite, decision excerpt, or other evidence named by the relying context.

