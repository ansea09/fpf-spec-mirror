---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:9"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__010_conformance-checklist-normative.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:9 — Conformance Checklist (normative)"
line_start: 47022
line_end: 47045
dependencies:
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.1"
  - "C.23"
  - "C.32.P2S"
  - "E.10"
  - "E.18"
  - "G.0"
  - "G.4"
  - "G.5"
keywords:
  - "Problem‑CHR"
  - "ScopeSlice(G)"
  - "TaskKind"
  - "TaskSignature"
  - "specialization anchor"
  - "unknown handling"
---

### C.22:9 - Conformance Checklist (normative)

0. **Minimal S2.** S2 contains only fields necessary for Eligibility, Acceptance, and selection; any extra derived traits remain provenance.
1. **TaskSignature present (S2).** Every exported TaskKind has a TaskSignature with all fields declared and **CHR-typed**; `unknown` is an admissible value for each.
2. **CHR admissibility proven.** Any numeric comparison or aggregation **cites CG-Spec** by **Characteristic id** and proves **CSLC admissibility**; **no mean on ordinals; no unit mixing**.
3. **Unknowns propagate.** Unknowns **must** map to {pass|degrade|abstain} in **Acceptance** and **Eligibility**; no implicit coercions; behavior recorded in **SCR**.
4. **Evidence lanes.** **A.10 evidence relations** + **Assurance lanes (TA/VA/LA)** + **freshness windows** recorded; **Γ-fold** default=weakest-link unless proved otherwise.
5. **ReferencePlane guarded.** ReferencePlane noted **per value and per ObjectiveProfile head**; on crossings apply **CL** (and **CL^plane** if planes differ); **Φ(CL)/Φ_plane** are **monotone, bounded, table-backed and documented in the `CG-Spec`**; penalties → **R_eff only** (F/G invariant).
6. **Acceptance thresholds live in CAL.** No acceptance-gate thresholds in CHR or code paths; only in **G.4 AcceptanceClauses**.
7. **Selector admissibility.** Selection uses **admissible (possibly partial) orders**; **weighted sums across mixed scale types are forbidden**; return a **Pareto set** when appropriate.
8. **Crossings visible.** Any cross-stance/cross-Context reuse records **BridgeCard/BridgeDescription + UTS row** with CL notes and (if planes differ) CL^plane + Φ_plane.
9. **UTS twin labels.** All exported cards include **Name Cards** with twin labels; Bridges carry loss notes.
10. **GateCrossing checks.** Exported TaskSignature and any referenced crossings satisfy: (i) stance tagging (if used; informative only), (ii) **CrossingBundle** presence/consistency (**E.18**; **F.9**; **F.17**; **E.17**; **A.21** when gate checks are live), (iii) **LanePurity** (CL→R only; F/G invariant; Φ tables present), and (iv) **Lexical SD** (**E.10**). Failures are **blocking** under the active GateProfile / GateChecks (**A.21**).
11. **QD fields (when QD is in scope).** If `PortfolioMode=Archive` or QD heads are present, **CharacteristicSpaceRef** (d>=2), **ArchiveConfig** (topology, resolution, K, `InsertionPolicyRef`, `DistanceDefRef.edition`), and **EmitterPolicyRef** **SHALL** be present and CHR-typed; characteristics declare **ReferencePlane**.
12. **DominanceRegime default.** `DominanceRegime` **defaults to `ParetoOnly`**; inclusion of illumination in dominance **MUST** be enabled by a **CAL.Acceptance policy**; the policy id **SHALL** be recorded in SCR.
13. **Telemetry.** **PathSliceId**, **decay and refresh policy ids**, and **edition counters** for **CharacteristicSpaceRef**, **DistanceDefRef**, and **EmitterPolicyRef** **SHALL** be recorded; any illumination increase **SHALL** log the **policy-id** that triggered it.
14. **GeneratorIntent (when OEE is in scope).** `GeneratorIntent` **SHALL** cite **`EnvironmentValidityRegion`** and **`TransferRulesRef`** (ids resolvable in G.5/C.23); absence => `Abstain` for OEE generator-family use.
15. **Budgets.** `Budgeting` (evaluation, time, and batch) **SHALL** declare units and E/E-LOG exploration budget id when used.
16. **Archive admissibility.** `DistanceDefRef.edition` and any novelty measures **SHALL** be CSLC-admissible and **editioned**; inadmissible operations => **Abstain**.
17. **Planes.** **ReferencePlane** **SHALL** be declared for all QD heads or characteristics; plane crossings apply **Phi_plane** (penalty to **R** only).
18. **Unknowns.** Unknown QD fields **map** to `{degrade|abstain|sandbox}`; no coercions.

19. **Specialization claims referenced.** Any declared specialization on this TaskSignature **SHALL** name the task family/work target, named work-measure threshold target, adaptation budget, freshness or provenance basis for reuse, and enough attachment detail for the same claim to remain admissible in `C.22.1`, `G.5`, and `G.9` use.

