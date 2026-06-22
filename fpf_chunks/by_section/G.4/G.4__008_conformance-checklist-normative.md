---
chunk_kind: "child"
pattern_id: "G.4"
pattern_title: "CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
section_id: "G.4:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.4/G.4__008_conformance-checklist-normative.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "G.4 — CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
  - "G.4:7 — Conformance Checklist (normative)"
line_start: 84899
line_end: 84918
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
  - "admissibility gates"
  - "edition pins"
  - "evidence profiles"
  - "operators"
  - "tri-state admissibility"
  - "Γ-fold hooks"
  - "Φ/Ψ/Φ_plane policy pins"
---

### G.4:7 - Conformance Checklist (normative)

| ConformanceId     | Statement                                                                                                                                                                                                                                                                                                      |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CC‑G4‑CoreRef** | Conformance with `G.4` requires satisfying the effective `G.Core` obligations referenced by the `GCoreLinkageManifest` in **G.4:4.1** (profiles, pin sets, consumed defaults, and trigger kinds).                                                                                                              |
| **CC‑G4‑01**      | `CAL Pack@CG-Frame` is published as a notation-independent object with stable UTS ids (Name Cards with twin labels) for `CAL.Charter`, `TaskMap`, all operator, acceptance, flow, and evidence carriers, Worked-Examples, and public-id continuity notes, including deprecations and lexical-continuity notes. Tooling/vendor details remain non-normative. |
| **CC‑G4‑02**      | `CAL.Charter@Context` pins `CG-FrameContext`, `entityOfConcern` (incl. `ReferencePlane`), and the relevant governing spec references by edition pins (`CNSpecRef.edition`, `CGSpecRef.edition`).                                                                                                                     |
| **CC‑G4‑03**      | Every `CAL.Operator` has an explicit CHR‑typed signature and explicit preconditions; any legality guard macros referenced are cited by id (no “implicit legality”).                                                                                                                                             |
| **CC‑G4‑04**      | Every `CAL.Acceptance` binds to CHR ids (`CharacteristicRefs`) and declares unknown handling and failure behavior via pins/refs; thresholds and cutoffs appear only here (not inside CHR artifacts and not inside operator prose). If the clause depends on cross-context, cross-plane, or cross-edition imports, it cites `GateCrossingId[]/CrossingBundleId[]`. |
| **CC‑G4‑05**      | If an acceptance clause, operator, or flow induces numeric comparison/aggregation, it cites the relevant `CG‑Spec.characteristic` ids and links to legality proof refs (CSLC) in the ProofLedger; otherwise it must be authored so that downstream can degrade/abstain rather than perform illegal operations. |
| **CC‑G4‑06**      | Every `CAL.Flow` declares its result kind and the set of gating acceptance clauses; any thinning/selection‑aid policies (e.g., ε‑front selection) are explicitly policy‑bound and do not silently replace the underlying result kind.                                                                      |
| **CC‑G4‑07**      | Every `CAL.EvidenceProfile` declares: provenance anchors (A.10), evidence lanes (`F/G/R`), freshness/decay pins (incl. freshness window + decay/Γ_time selector refs), and any penalty routing policy pins (`Φ(CL)`, `Ψ(CL^k)`, `Φ_plane`) needed for run‑time `SCR` surfacing. It either pins an explicit `ΓFoldRef.edition` override or (if absent) cites `DefaultId.GammaFoldForR_eff` (via `G.Core.DefaultGoverningDefinitionIndex`). Penalty policies affect `R_eff` only and do not define dominance. Any referenced penalty policy family is justified in the ProofLedger (monotone + bounded).  |
| **CC‑G4‑08**      | `CAL.ProofLedger` exists and is UTS‑citable; it links each operator/flow/clause to required proof/justification refs and records explicit degradation conditions when assumptions fail. If an explicit `ΓFoldRef` is pinned, it includes monotonicity + boundedness/boundary behavior proof refs for that fold. |
| **CC‑G4‑09**      | CAL publication includes RSCR tests and Worked‑Examples sufficient to detect illegality (incl. unit laundering / ordinal arithmetic), to exercise authored acceptance/flow behavior, and to validate the authored freshness envelope when it is part of admissibility; missing tests/examples are treated as an auditable gap, not as “assumed OK”. |
| **CC‑G4‑10**      | `TaskMap@Context` (`TaskMap`) is present and provides `G.5` with acceptance clause ids (`AcceptanceClauseId[]`; selector gates), operator/flow ids, and evidence profile ids required for explainability and audit; selector implementations must not embed thresholds or duplicate acceptance semantics.    |
| **CC‑G4‑11**      | Any method/discipline specifics are placed under `G.4:4.5 Extensions` as `GPatternExtension` blocks (stable `PatternScopeId`, explicit governing definition, pins, and RSCR triggers); no extension introduces competing defaults or replaces `G.Core` invariants. |
| **CC‑G4‑12**      | `CAL Pack@CG-Frame` includes public-id continuity records for public ids: deprecations, edition bumps, and lexical-continuity notes. It exposes refresh payload pins, including editions, policies, UTS ids, and, when present, `PathId` and `PathSliceId`, sufficient for `G.11` to plan RSCR without inferring semantics from prose. |
| **CC‑G4‑13**      | When `G.4:Ext.NQD` is present, `CAL.NQD[]` is present and is wired only via the declared governing pattern (`C.18`): at minimum it pins `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and `InsertionPolicyRef`, and it treats archive/illumination summaries as report‑only unless explicitly promoted by a CAL acceptance clause/policy. |
| **CC‑G4‑14** | CAL does not mint new universal types to encode “strategy/policy”. Strategy is expressed as authored flows + acceptance clauses + policy/task pins (and downstream registry/composition in `G.5`); any specialization is introduced only via `GPatternExtension` wiring blocks or cited governing patterns.  |

