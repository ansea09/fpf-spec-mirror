---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:9"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__010_conformance-checklist-normative.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:9 — Conformance Checklist (normative)"
line_start: 50522
line_end: 50546
dependencies:
  - "A.6.0"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.1"
  - "C.22.2"
  - "C.23"
  - "C.32.P2S"
  - "E.10"
  - "E.18"
  - "G.0"
  - "G.4"
  - "G.5"
keywords:
---

### C.22:9 - Conformance Checklist (normative)

0. **Minimal four-row S2.** `TaskSignature@Context` exposes an A.6.0 `SignatureManifest` plus SubjectBlock, Vocabulary, Laws, and Applicability. The manifest supplies stable identity and dependency metadata, not a fifth semantic row; the four-row declaration contains only content needed for eligibility, acceptance, or selection.
1. **Signature and assignment present.** Every exported selector-facing case names one TaskSignature identity and edition plus one `TaskSignatureAssignmentRelation@Context` whose problem-side episteme, receiving-use description, and bounded Context are recoverable. Current characteristic bindings are CHR-typed; a live unknown preserves `unknown`, while a non-current optional vocabulary item remains absent.
1a. **Publication does not define identity.** Two E.17 publications or serialized records that resolve to the same SignatureId, edition, and four-row semantic content describe the same TaskSignature. Carrier, layout, or serialization change alone does not create a new signature edition or assignment relation.
2. **CHR admissibility proven.** Any numeric comparison or aggregation **cites CG-Spec** by **Characteristic id** and proves **CSLC admissibility**; **no mean on ordinals; no unit mixing**.
3. **Unknowns remain typed.** A live unknown remains `unknown`, cites the direct downstream policy, and is not coerced. The acceptance, eligibility, or selector pattern records its own governed result.
4. **Evidence lanes.** **A.10 evidence relations**, **Assurance lanes TA, VA, and LA**, and **freshness windows** are recorded; **Gamma-fold** defaults to weakest-link unless the governing CAL establishes an alternative.
5. **ReferencePlane guarded.** ReferencePlane is noted **per value and per ObjectiveProfile head**; crossings apply **CL** and **CL^plane** when planes differ. **Φ(CL) and Φ_plane** are **monotone, bounded, table-backed, and documented in the `CG-Spec`**; penalties affect **R_eff only**, preserving F and G invariants.
6. **Acceptance thresholds live in CAL.** No acceptance-gate thresholds in CHR or code paths; only in **G.4 AcceptanceClauses**.
7. **Selector-use support.** The TaskSignature exposes the scales, units, polarities, and admitted order relations needed by `G.5`; it carries no mixed-scale scalarization or local selector verdict. `G.5` governs any Pareto-set result when its admissible relation remains partial.
8. **Crossings visible.** Any cross-stance or cross-Context reuse records **BridgeCard or BridgeDescription plus UTS row** with CL notes and, when planes differ, CL^plane plus Φ_plane.
9. **UTS twin labels.** All exported cards include **Name Cards** with twin labels; Bridges carry loss notes.
10. **GateCrossing checks.** Exported TaskSignature and referenced crossings satisfy: (i) stance tagging when used, as informative only; (ii) **CrossingBundle** presence and consistency under **E.18**, **F.9**, **F.17**, **E.17**, and **A.21** when gate checks are live; (iii) **LanePurity**, with CL affecting R only, F and G invariants preserved, and Φ tables present; and (iv) **Lexical SD** under **E.10**. Failures return a blocking gate result under the active GateProfile and GateChecks governed by A.21.
11. **QD fields (when QD is in scope).** A `TaskSignature` with `PortfolioMode=Archive` or QD heads is complete only when it carries CHR-typed **CharacteristicSpaceRef** (d>=2), **ArchiveConfig** (topology, resolution, K, `InsertionPolicyRef`, `DistanceDefRef.edition`), and **EmitterPolicyRef** fields; every characteristic declares its **ReferencePlane**.
12. **DominanceRegime default.** `DominanceRegime` defaults to `ParetoOnly`. Illumination enters dominance only through a cited **CAL.Acceptance policy** enabling that relation; the SCR records the policy id.
13. **Telemetry.** The telemetry record carries **PathSliceId** when an E.18 path slice is current, the applicable **decay and refresh policy ids**, and edition counters for **CharacteristicSpaceRef**, **DistanceDefRef**, and **EmitterPolicyRef**. An illumination increase is traceable to the policy id that admitted it.
14. **GeneratorIntent (when OEE is in scope).** A TaskSignature supports the claimed OEE generator-family use only when `GeneratorIntent` cites **`EnvironmentValidityRegion`** and **`TransferRulesRef`** with ids resolvable in G.5 and C.23. Any downstream abstention is their result, not a C.22 output.
15. **Budgets.** When `Budgeting` is live, its evaluation, time, and batch values carry declared units and the applicable E/E-LOG exploration-budget id.
16. **Archive-comparison support.** A TaskSignature supports the claimed archive comparison only when `DistanceDefRef.edition` and the applied novelty measures are CSLC-admissible and editioned. The archive or selector pattern governs any downstream abstention or returned-set result.
17. **Planes.** QD heads and characteristics carry a declared **ReferencePlane**; a plane crossing applies **Phi_plane** as a penalty to **R** only.
18. **Unknown QD values.** A live unknown QD field remains `unknown`, cites the policy governing its downstream use, and is not coerced or mapped by C.22 itself.

19. **Specialization claims referenced.** A declared specialization on this TaskSignature is complete when it names the task family and work target, work-measure threshold target, adaptation budget, freshness or provenance basis for reuse, and the exact TaskSignature edition and assignment relation needed for the same claim to remain admissible in `C.22.1`, `G.5`, and `G.9` use.

