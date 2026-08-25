---
chunk_kind: "child"
pattern_id: "C.30.AD.BA"
pattern_title: "Built-Asset Architecture Description and Reference Designation"
section_id: "C.30.AD.BA:4"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD.BA/C.30.AD.BA__007_conformance-checklist.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "C.30.AD.BA — Built-Asset Architecture Description and Reference Designation"
  - "C.30.AD.BA:4 — Conformance Checklist"
line_start: 57925
line_end: 57939
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.5"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "A.6.M"
  - "A.6.P"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.TFS-REL"
  - "E.17"
  - "E.17.0"
  - "E.24.PUB"
  - "F.18"
  - "G.11"
keywords:
---

### C.30.AD.BA:4 - Conformance Checklist

| ID | Check | Repair when absent |
| --- | --- | --- |
| `BA-1` | The exact built asset is recoverable, and every used architecture description has one exact ClaimGraph, one EntityOfConcern—built asset, obtaining `ArchitectureRelation`, or selected structure—and effective `U.ReferenceScheme`. | Recover the asset under `A.1`, subject relations and architecture relation under `C.30`, selected structure under `A.22`, and description identity under C.2.1; do not derive the subject from an optional architecture-claim field. |
| `BA-2` | Every asserted architecture structural view is the same exact description episteme whose selected-structure EntityOfConcern, structure kind, exact viewpoint, and independently obtaining E.17.0 conformance relation are named. | Apply `A.22`, `E.17.0`, and `C.30.ASV`; do not use the file, bundle, dashboard, representation, publication, or current use as the structure or view constructor. |
| `BA-3` | Every relied-on designation names its scheme, designated entity, selected aspect structure, qualification window, and exact designation/reference relation when one is claimed; design/realization correspondence remains a separate claim or relation. | Recover the direct designation/reference owner and occurrence, or keep a bounded designation-use claim; never use repeated spelling as entity identity or parthood proof. |
| `BA-4` | Exchange checking and architecture evaluation have different evaluated objects and governors; source episteme, representation, publication occurrence, form, carrier, actual subject relations, selected structures, and descriptions remain distinct. | Keep description conformance with the exchange use; return relation truth, architecture adequacy, evidence, and assurance to their direct patterns. |
| `BA-5` | Reused or live descriptions name source-to-use, source-return when stronger use needs it, description freshness, and publication-currentness objects appropriate to the exact claim. | Apply `G.11`; do not turn freshness, synchronization, recent publication, or live data into grounding, truth, evidence sufficiency, or architecture adequacy. |
| `BA-6` | Digital and physical objects retain direct kinds, identities, coupling relations, Work, and transformations; actual change is cited only with the full A.3.4 basis. Project-local use additionally names both exact composite Work and the obtaining project-use relation. | Recover model, systems, epistemes, the exact composite `U.Work`, interfaces, coupling, actual changed referent and facts, and `builtAssetDescriptionProjectUseRelationRef` as the separately governed obtaining relation by which this description use concerns that Work before making identity, parthood, transformation, or project-locality claims. |
| `BA-7` | Every used cost, schedule, operation, maintenance, sustainability, or energy view names exact description identity and, when asserted as a structural view, selected structure, viewpoint, and conformance; its characteristic, Work, temporal, causal-use, evidence, assurance, and currentness claims keep exact direct owners. | Use `C.16` for the measurement result, `A.15` for Work, `C.27.TA` or `C.27` for the exact temporal use, `C.28` only when the view, telemetry, simulation, maintenance action, or claimed change is used causally, `A.10` or `B.3` for reliance or assurance, and `G.11` for currentness; do not let the auxiliary view itself establish a causal effect, sustainability, acceptance, evidence, assurance, or architecture adequacy. |
| `BA-8` | Every ISO 19650-based use names the exact part and edition, exact source-to-use path, used information or model edition, source-status reference date, validity window, refresh or source-return condition, and admissible and non-admissible use. | Pin the exact published edition used; reopen this source-use locus when ISO status, the cited edition, information edition, or intended use changes. Do not silently substitute a draft or successor edition or import standard terminology as FPF ontology or authority. |
| `BA-9` | Every declared use that crosses design-side and run-side material fills one `BuiltAssetDesignRunSeparationUse` with exact side-specific descriptions, Work when current, source and currentness refs, classification basis, admissible cross-lifecycle use, and blocked merge; correspondence, coupling, and transformation refs appear only when their direct predicates obtain. | Fill the local carrier from already governed refs, or narrow or block the cross-lifecycle use. Do not restore a generic tag, infer identity or parthood from co-display, or treat telemetry, Work, correspondence, coupling, or a proposed effect as actual A.3.4 change. |
| `BA-10` | A green twin, dashboard, exchange result, or release screen remains a cue unless an actual `A.21` gate-decision relation is current; gate decision, release action, work-entry readiness, permission or grant act, performed Work, and a subject-release predicate remain distinct claims. | Recover `OperationalGate(profile)`, declared `GateCheckRef`s, `GateDecision`, and `DecisionLogRef` only for the actual gate relation. Route a release action or other performed Work to its exact `A.15.1` occurrence, readiness to `A.15.5`, a permission result or exercise to `A.2.8.PER`, an instituting or revoking grant act to `A.2.9`, and a subject-release claim to its named predicate and participants or `A.6.RCD missing-governor`; none is entailed by freshness, evidence, assurance, the display, or `GateDecision=pass`. |

