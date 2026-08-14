---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore-Exploit Live-Pool Governor"
section_id: "C.19:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__013_conformance-checklist.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "C.19 — Explore-Exploit Live-Pool Governor"
  - "C.19:7 — Conformance Checklist"
line_start: 49934
line_end: 49953
dependencies:
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.22.PFR"
  - "C.24"
  - "C.28"
  - "C.32"
  - "C.32.P2S"
  - "C.35"
  - "E.17"
  - "E.23"
  - "E.24.PUB"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "already-live candidate pool"
  - "change trigger"
  - "explore-exploit"
  - "governing lens"
  - "keep frontier"
  - "narrow to subset"
  - "pool-policy result"
  - "sunset line"
  - "widen"
---

### C.19:7 - Conformance Checklist
- **C19-1** When a C.18 generation or archive record relies on a named C.19 `EmitterPolicy`, it **SHALL** cite that profile in `emitterPolicyRef?`. If the active insertion policy is not inherited, record it in `insertionPolicyRef?`. If the deduplication threshold is not inherited, record scalar `dedupThreshold?` together with its `deduplicationBasisRef?` and `deduplicationUnit?`; never encode that scalar as a reference. A record with no such policy dependence need not fabricate these fields.
- **C19-2** The characteristic set and indicators used for dominance **MUST** be declared and eligibility conditions applied first. If use-value participates in current `Q`, the record cites the C.16.Q `QS.UseValue` objective head in that Q; otherwise it states that the criterion remains outside Q. *(References to C.18 generator operators are descriptive only; LOG exports no Γ.)*
- **C19-3** If a lens is used, its id MUST be recorded; do not label scalarized top-1 as "frontier".
- **C19-4** Promotion of `Surprise` or `Illumination` into dominance MUST be explicit in policy.
- **C19-5** A pool-policy record creates no `SystemRoleAssignmentStateRelation`, system-role assignment, permission, plan, budget, or Work occurrence. When implementation follows, cite the independently obtaining context and scope, exact system-role-kind classification, assignment or assignment-state condition, and direct planning or Work pattern; C.19 establishes none of them.
- **C19-6** Each pool-treatment lens **MUST** document the pipeline `Eligibility (ConstraintFit=pass) → Dominance (declared set) → Tie-breakers (declared)`. Any promotion of `Surprise` or `Illumination` into the dominance set **MUST** be named by lens or policy id and recorded in provenance.
- **C19-7 (LEX-AUTH trigger).** When a context adopts or changes an `EmitterPolicy` profile that includes domain-family quotas or a sampler, or changes `DescriptorMap` family coordinates, `DistanceDef`, or a `δ_family` threshold, author that context-local change via **E.15 LEX-AUTH**. C.19 establishes no default heterogeneity quota or sampler. Any resulting **LAT** lives in the relevant LAT and evidence authority; the DRR need only carry the content decision itself plus any decisive evidence or validation consequence by value when that consequence materially shaped the choice (see **CC-DRR.6**). Record policy and card ids in SCR.

- **C19-8** When a heterogeneity-first profile is used, provenance **MUST** name each admitted heterogeneity constraint and its governing policy id. If a family or subfamily quota applies, record the exact quota vector and family-definition id; if sampling applies, record the sampler class, seed when relevant, and sampler-policy id. Do not fabricate a default triad, quota, or sampler.
- **C19-9** A `PoolPolicyResult` **MUST** identify `livePool`, `governingLens`, `changeTrigger`, and exactly one `currentTreatment` token from `widen | keep_frontier | narrow_to_subset | sunset_line`; `lens` and space-separated treatment spellings are not alternate record fields or values.
- **C19-10** If the question under repair is local option choice, an enactment-facing plan, selector-facing result declaration, or publication availability, `C.19` **MUST** name the applicable pattern rather than restate it: `C.11`, `C.24`, `G.5`, `E.17`, or `E.24.PUB`.
- **C19-11** If autotelic or capability-discovery evidence is used, the record **MUST** name `goalSpaceExpansionPolicyRef` when one governs widening and the `learningProgressSignal`, `competenceModelRef`, or `goalSpaceExpansionCue` that supports the pool treatment, and it **MUST** keep those signals outside default dominance unless an explicit promotion policy is recorded.
- **C19-12** If an exploration and exploitation policy collects data for a causal claim, changes intervention budget, learns a causal policy, evaluates a policy from behavior data or logging data, or treats counterfactual replay as support, `PoolPolicyResult.causalUseSpec?` **MUST** carry `targetCausalityLadderRung`, `causalUseClaimKind: CausalUseClaimKind`, causal evidence support basis when known, supported use and unsupported use, and relevant `C.28` support refs.
- **C19-13** If a pool-policy record concerns still-live loop-engineering candidates—for example, loops, agent harnesses, workflows, or DPF seeds—it names the pool, governing lens, current treatment, and change trigger. A need for candidate generation, archive update, or front recomputation requires `C.18` with desired policy values and a reason only. Improvement requires `E.23`; selector-result declaration requires `G.5`; audience publication requires `E.17` and `E.24.PUB`; choice requires `C.11`; work requires the A.15 family; and refresh requires `G.11`.
- **C19-14** A pool-policy record, its evidence, and its treatment constitute neither an actual Problem nor `ProblematicForRelation`, improvement result, work result, project Work or parthood, `ChoiceResult`, public selected set, work permission, nor refreshed edition.
- **C19-15** If graduation, scaling, or widening relies on assurance, `assuranceResultRef?` **MUST** cite the exact B.3 assurance result, and `changeTrigger` **MUST** name the satisfied condition and the bounded scope that result supports. A C.19 policy threshold or label does not create that assurance result.



