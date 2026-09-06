---
chunk_kind: "child"
pattern_id: "C.30.AD.BA"
pattern_title: "Built-Asset Architecture Description and Reference Designation"
section_id: "C.30.AD.BA:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD.BA/C.30.AD.BA__001_intro.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "C.30.AD.BA — Built-Asset Architecture Description and Reference Designation"
  - "C.30.AD.BA:intro — Intro"
line_start: 59775
line_end: 59792
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

## C.30.AD.BA - Built-Asset Architecture Description and Reference Designation

> **Type:** Architecture-description subpattern under `C.30.AD`
> **Status:** Stable
> **Normativity:** Normative for built-asset architecture-description, reference-designation, model-exchange, and digital-twin use

**Builds on.** `C.30`, `C.30.AD`, `C.30.ASV`, `A.1`, `A.22`, `C.2.1`, `E.17.0`, `E.17`, `E.24.PUB`, and `A.7`.

**Coordinates with.** `A.6.P`, `A.6.RCD`, `A.6.REL`, `A.6.F`, `A.6.M`, `C.30.TFS-REL`, `C.30.LCA`, `C.29`, `C.16`, `C.27`, `C.27.TA`, `C.28`, `A.3.4`, `A.10`, `G.11`, `A.15`, `A.15.1`, `A.15.5`, `A.21`, `A.2.8.PER`, `A.2.9`, `B.3`, and `F.18`.

**Use this when.** Use this pattern when a BIM or IFC publication, asset-information description, reference designation, cost, schedule, operation, maintenance, sustainability, or energy view, or digital-twin description is being used to say something about the architecture of one exact built asset.

**What goes wrong if missed.** A rich model is treated as the asset or its architecture; a file or multi-view bundle is allowed to select structure or grant `U.View` membership; or a designation and a live data feed are asked to carry identity, occurrence, truth, and currentness claims that their direct relations do not establish.

**What this buys.** An engineer can use current built-asset information systems while keeping the physical asset, actual subject relations, exact selected structures, any obtaining `ArchitectureRelation`, bounded architecture claims, each description episteme, exact viewpoint conformance, each representation and publication object, each designation or reference relation, and each currentness claim inspectably connected but distinct.

**Not this pattern when.** Use `C.30` when the current object is the direct architecture relation or bounded architecture claim, `C.30.AD` when no built-asset specialization is needed, and `C.30.ASV` when one structural view is under repair. Use the direct designation/reference, evidence, currentness, Work, decision, transformation, or causal-use pattern when that relation rather than built-asset architecture-description use is current. When auxiliary-view, telemetry, simulation, maintenance, or digital-twin material is used to claim that an intervention caused an effect, handle that causal use under `C.28`; `C.27` remains the owner of temporal-claim adequacy. When a twin, dashboard, exchange result, or release screen looks like gate passage, recover whether a named gate decision is current. Use `A.21` when that gate must decide a bounded action or when its `GateDecisionResult` is being relied on; the display remains a cue until the required result is established. Return any separate evidence, work-entry readiness, assurance, Work, or other claim to its own governor. Do not collapse release into gate passage: route a release action or other performed Work to the exact `A.15.1` `U.Work` occurrence, work-entry readiness to `A.15.5`, a permission result or exercise to `A.2.8.PER`, an instituting or revoking grant act to `A.2.9`, and a claim that a subject was released to its named subject predicate and participants; if that predicate cannot be recovered, return `A.6.RCD missing-governor`. An authorization-looking label does not choose among these claims.

