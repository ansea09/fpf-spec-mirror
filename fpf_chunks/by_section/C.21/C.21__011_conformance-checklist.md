---
chunk_kind: "child"
pattern_id: "C.21"
pattern_title: "Field Health & Structure (Discipline-CHR)"
section_id: "C.21:9"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.21/C.21__011_conformance-checklist.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "C.21 — Field Health & Structure (Discipline-CHR)"
  - "C.21:9 — Conformance Checklist"
line_start: 50880
line_end: 50903
dependencies:
  - "A.17"
  - "A.18"
  - "A.2.6"
  - "B.3"
  - "C.16"
  - "C.2"
  - "C.20"
  - "E.10"
  - "F.9"
  - "G.0"
  - "G.10"
  - "G.11"
  - "G.12"
  - "G.2"
  - "G.5"
  - "G.9"
  - "U.Discipline"
keywords:
  - "alignment"
  - "discipline"
  - "disruption"
  - "field health"
  - "reproducibility"
  - "standardisation"
---

### C.21:9 - Conformance Checklist

This checklist verifies a DHC reading after the practitioner has selected the live discipline-health question. It is not an audit form and not a dashboard specification.

| Check | Passing reading | Boundary preserved |
| --- | --- | --- |
| **CC-C.21-1 CHR typing.** | Every DHC slot declares Characteristic, Scale/Unit, and Polarity, with CSLC admissibility visible before aggregation. | Prevents health labels from becoming untyped opinion. |
| **CC-C.21-2 Freshness.** | Published values carry a `Γ_time` selector and freshness window; stale rows produce `{degrade|abstain}` in G.4 Acceptance. | Prevents stale cumulative history from masquerading as current health. |
| **CC-C.21-3 Plane.** | `ReferencePlane` is declared; cross-plane reuse publishes `CL^plane` policy id alongside CL, with penalties applied to `R_eff`. | Keeps world, concept, and episteme readings distinct. |
| **CC-C.21-4 Design/run tag.** | Each DHC row declares `DesignRunTag ∈ {design, run}` and does not mix design- and run-characteristics in one value or aggregate. | Prevents design claims and run observations from collapsing. |
| **CC-C.21-5 Lane tags.** | Each value tags TA/VA/LA lanes of contributing evidence. | Keeps typing, validation, and live-assurance lanes visible. |
| **CC-C.21-6 Ordinal discipline.** | `StandardisationLevel` remains ordinal: comparisons only, no means or z-scores. | Blocks pseudo-quantification. |
| **CC-C.21-7 Scope.** | All computations declare `TargetSlice`; USM membership is decidable for the declared use. | Prevents free-floating field-health claims. |
| **CC-C.21-8 Bridges.** | Cross-context comparisons or publications cite Bridge id and CL; penalties apply to `R_eff`, never to F/G. | Keeps local meaning loss visible. |
| **CC-C.21-9 UTS.** | DHC rows are publishable as UTS Name Cards with Tech/Plain twin labels. | Keeps names recoverable across contexts. |
| **CC-C.21-10 Registry.** | DHC methods are table-backed; method changes bump `DHCMethodSpecRef.edition` and trigger RSCR. | Prevents silent method drift. |
| **CC-C.21-11 Unknowns.** | Unknown inputs propagate tri-state `{pass|degrade|abstain}` to Acceptance; `unknown -> 0` coercion is excluded. | Preserves honest uncertainty. |
| **CC-C.21-12 Lexical firewall.** | Core narrative follows E.5.1 and does not use tool/vendor tokens as discipline-health kinds. | Prevents vendor or tool labels from becoming characteristics. |
| **CC-C.21-13 CG-Spec citation.** | Numeric comparison or aggregation in DHC cites CG-Spec: characteristics, `ScaleComplianceProfile`, `Γ-fold`, and MinimalEvidence. | Keeps operations scale-admissible. |
| **CC-C.21-14 Phi policies.** | `Phi(CL)` and `Phi_plane` are monotone, table-backed, and published by policy id. | Prevents hidden penalty functions. |
| **CC-C.21-15 Ref discipline.** | Edition pinning appears as `...Ref.edition` on the relevant reference field; bare `...Edition` fields are repaired. | Keeps edition subject explicit. |
| **CC-C.21-16 Role kit, informative.** | Standard roles from F.4 may be used: `DisciplineStewardRole`, `DHCMethodAuthorRole`, `DHCSeriesPublisherRole`; values still declare design/run stance and `ReferencePlane`. | Roles do not become evidence or authority. |
| **CC-C.21-17 Engineering-grade and semio-substitution extensions.** | When `EngineeringClaimJustificationRecoverability` or `SemioSubstitutionPressure` is active, the DHC row names the neighboring pattern governing the claiming FPF pattern that carries live engineering claim kind or admissible-use boundary or semio-substitution repair, plus admissible use, non-admissible overread, and stop or reopen condition. | The extension note is not evidence, assurance, gate passage, mathematical-lens use, release permission, work authority, or project certification. |

