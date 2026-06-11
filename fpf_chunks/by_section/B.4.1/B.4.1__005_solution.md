---
chunk_kind: "child"
pattern_id: "B.4.1"
pattern_title: "Observe -> Notice -> Stabilize -> Route"
section_id: "B.4.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.4.1/B.4.1__005_solution.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "B.4.1 — Observe -> Notice -> Stabilize -> Route"
  - "B.4.1:4 — Solution"
line_start: 32797
line_end: 32860
dependencies:
  - "A.15"
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.6.A"
  - "A.6.P"
  - "B.4"
  - "B.5.2"
  - "B.5.2.0"
  - "C.16.Q"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "C.22.1"
  - "F.9.1"
keywords:
  - "pre-abductive seam"
  - "route plurality"
  - "route selection"
  - "routed cue set"
  - "task-family specialization route"
---

### B.4.1:4 - Solution
Insert a pre-abductive route-bearing seam inside the language-state cluster, between observation/cue preservation and endpoint governing-pattern entries:

`Observe -> Notice -> Stabilize -> Route`

The seam yields a `RoutedCueSet`, normally downstream of `U.PreArticulationCuePack`.

#### B.4.1:4.1 - `RoutedCueSet` shape
A conforming routed cue set may publish:

- `sourceCuePackRef`
- `candidateRouteSet`
- `routeDecision?`
- `selectedRoute?`
- `routeRationale?`
- `routeAuthorityState?`
- `multiRoutePolicy?`
- `publicationFaceRefs?`
- `articulationThresholdStatus?`
- `closureStatus?`
- `scope?`
- `GammaTime?`

`RoutedCueSet` is not itself the late endpoint. `articulationThresholdStatus` and `closureStatus` report guard state only; their governance remains with `C.2.4` and `C.2.5`, and route discrimination may additionally cite `C.2.6` or `C.2.7` when anchoring or representation-factor differences are load-bearing.

`candidateRouteSet` and `routeDecision` are the load-bearing core here. `selectedRoute`, `routeRationale`, and `routeAuthorityState` belong here when route selection is explicit. They do **not** belong in `U.PreArticulationCuePack`.

`publicationFaceRefs` names MVPK faces only when face typing matters for publication or review. Faces are renderings of the routed cue set or of later typed projection publications; they are not the route-bearing form itself.

A multi-route `RoutedCueSet` is still one governed member. A lineage fork appears only after distinct successor publications are issued.

#### B.4.1:4.2 - Starter route family and conditional extension species
The candidate route set may contain, among others:

- starter canonical routes:
  - `EvaluativeRoute`
  - `ActionInvitationRoute`
  - `ProblemAbductionRoute`
  - `MethodWorkRoute`
  - `RequirementCommitmentRoute`
- conditional extension routes for bounded specialization or corridor discovery:
  - `TaskFamilySpecializationRoute`
  - `AdaptationProbeRoute`
  - `NonHumanUtilityRoute`
  - `SubstrateDiversificationRoute`

##### B.4.1:4.2.1 - Specialization-sensitive extension route family
These four routes are not part of the starter canonical core. Use them only when the cue already carries explicit bounded-specialization pressure, corridor-entry pressure, or substrate-fit doubt that governing patterns must be able to recover by value.

Use `TaskFamilySpecializationRoute` when the cue points toward acquiring one narrower higher-fit specialist lane for one declared task family under budget, where that lane may later resolve into one specialist method, portfolio, or competence bundle. Use `AdaptationProbeRoute` when the honest next question is whether threshold-reaching specialization is actually attainable under the current budget. Use `NonHumanUtilityRoute` when the cue suggests a promising utility target outside the current human-default solution corridor but still tied to one declared task family or utility target. Use `SubstrateDiversificationRoute` when the cue says the current method substrate may be too narrow and a broader or different substrate should be tested before commitment.

Contexts may refine the route family locally, but they shall keep the distinction between early route publication and endpoint governance.

#### B.4.1:4.3 - Projection discipline
Here `projection` names route-bounded partialization, not a rival governing pattern and not a face kind. The resulting publication must be a **typed publication form** rendered, when needed, on an existing MVPK face.

A routed cue set may therefore lead to:

- `U.AbductivePrompt` under `B.5.2.0`,
- a later typed endpoint-entry publication under `A.6.P`, `A.6.A`, or `C.16.Q`,
- or another explicitly typed upstream projection publication.

If no typed downstream publication form can yet be named honestly, stay in `RoutedCueSet` rather than hiding a pseudo-form behind face language.

