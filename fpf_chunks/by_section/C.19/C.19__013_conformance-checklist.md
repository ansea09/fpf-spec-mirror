---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore-Exploit Live-Pool Governor"
section_id: "C.19:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__013_conformance-checklist.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "C.19 — Explore-Exploit Live-Pool Governor"
  - "C.19:7 — Conformance Checklist"
line_start: 47245
line_end: 47262
dependencies:
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.24"
  - "C.28"
  - "C.32"
  - "C.32.P2S"
  - "C.35"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "DecisionSubject clarification"
  - "EmitterPolicy"
  - "InsertionPolicy"
  - "dominance default routing"
  - "explore-exploit"
  - "keep frontier"
  - "lens id"
  - "live candidate pool"
  - "narrow to subset"
  - "pool-policy result"
  - "reroute"
  - "sunset line"
  - "widen"
---

### C.19:7 - Conformance Checklist
- **C19-1** Each C.18 generation or archive-use record **SHALL** cite `U.EmitterPolicyRef` (policy id + params) **and the active `InsertionPolicyRef` and `dedup_threshold` when not inherited**.
- **C19-2** The characteristic set and indicators used for dominance **MUST** be declared; eligibility conditions applied first. *(References to C.18 generator operators are descriptive only; LOG exports no Γ.)*
- **C19-3** If a lens is used, its id MUST be recorded; do not label scalarized top-1 as "frontier".
- **C19-4** Promotion of `Surprise` or `Illumination` into dominance MUST be explicit in policy.
- **C19-5** USM and role-state-relation gates apply: policy actions SHALL operate within the Context's scope and enactable `RoleStateRelation@BoundedContext` states.
- **C19-6** Each selection lens **MUST** implement and document the pipeline: `Eligibility (ConstraintFit=pass) → Dominance (declared set) → Tie-breakers (declared)`. Any **promotion** of `Surprise` or `Illumination` into the dominance set **MUST** be named by lens or policy id and recorded in provenance.
- **C19-7 (LEX-AUTH trigger).** Any change to `EmitterPolicy` defaults that affects domain-family quotas or samplers (HET-FIRST), or any change to `DescriptorMap` family coordinates, `DistanceDef`, or the `δ_family` threshold MUST be authored via **E.15 LEX-AUTH**. Any resulting **LAT** lives in the relevant LAT and evidence authority; the DRR need only carry the content decision itself plus any decisive evidence or validation consequence by value when that consequence materially shaped the choice (see **CC-DRR.6**). Record policy and card ids in SCR.

- **C19-8**  When the Heterogeneity-first lens is used, provenance MUST include: (i) the family-quota vector (including the default triad quota k), (ii) the subFamilyDef id (from F1-Card) if sub-family quotas apply, (iii) the sampler class, seed, and policy id.
- **C19-9** When `C.19` returns one pool-policy result, that result **MUST** identify the still-live pool or family scope, the governing lens or policy id, and the current treatment (`widen`, `keep frontier`, `narrow to subset`, or `sunset line`).
- **C19-10** If the question under repair is still local option choice, already one enactment-facing plan, or already one selector-facing publication result, `C.19` **MUST** name the governing pattern rather than restate `C.11`, `C.24`, or `G.5`.
- **C19-11** If autotelic or capability-discovery evidence is used, the record **MUST** name the `GoalSpaceExpansionPolicyRef` when one governs widening and the `LearningProgressSignal`, `CompetenceModelRef`, or `GoalSpaceExpansionCue` that supports the pool treatment, and it **MUST** keep those signals outside default dominance unless an explicit promotion policy is recorded.
- **C19-12** If an exploration and exploitation policy collects data for a causal claim, changes intervention budget, learns a causal policy, evaluates a policy from behavior data or logging data, or treats counterfactual replay as support, `PoolPolicyResult.causalUseSpec?` **MUST** carry `targetCausalityLadderRung`, `causalUseClaimKind: CausalUseClaimKind`, causal evidence support basis when known, supported use and unsupported use, and relevant `C.28` support refs.
- **C19-13** If a pool-policy result concerns loop, agent-harness, workflow, or DPF-seed candidates, the result names the still-live pool, governing lens, current treatment, and change trigger, and names `E.23`, `G.5`, the `A.15` family, or `G.11` as the next owner when improvement, publication, work, or refresh becomes current.



