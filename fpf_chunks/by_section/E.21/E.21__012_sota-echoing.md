---
chunk_kind: "child"
pattern_id: "E.21"
pattern_title: "FPF Pattern-Quality Evaluation CharacteristicSpace"
section_id: "E.21:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.21/E.21__012_sota-echoing.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "E.21 — FPF Pattern-Quality Evaluation CharacteristicSpace"
  - "E.21:11 — SoTA-Echoing"
line_start: 66425
line_end: 66442
dependencies:
  - "A.17-A.19"
  - "A.19.ECS"
  - "A.6.P"
  - "C.16"
  - "C.2.P"
  - "C.25"
  - "E.10"
  - "E.11"
  - "E.19"
  - "E.2.DA"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9.DA"
  - "F.18"
  - "J.4"
keywords:
  - "and admissibility predicates are not written as duties"
  - "definitions"
  - "invariants"
  - "state agent obligations only"
  - "typing rules"
---

### E.21:11 - SoTA-Echoing

`E.21:11` is a SoTA-binding table, not a bibliography. A row is live only when it changes at least one `E.21` field, eligibility condition, coordinate, worked slice, relation, conformance item, non-use boundary, or stop/reopen condition, and it uses `SoTA` in the E.8 sense: current best-known problem-solving practice for the governed problem.

If a `SoTA Synthesis Pack@CG-Frame` exists for pattern-quality evaluation, this section cites its claim IDs and does not fork an untracked SoTA narrative. If no pack exists, this section is a provisional seed and must still state `adopt | adapt | reject`, the concrete `E.21` effect, and the boundary of non-overread.

A source that only supplies lineage, popularity, or familiar terminology is not a SoTA row. It may remain as rationale material, but it does not satisfy `SoTABindingMinimum`.

| Claim | Source stance | Adopted/adapted content | Concrete E.21 effect | Boundary of non-overread |
|---|---|---|---|---|
| Pattern-quality evidence must show applicability and generality without making ordinary reading heavy. | Current pattern-validation anchors for this narrow problem: Riehle et al. (2021) for explicit pattern validation methods and Zarras (2023) for applicability/generality evidence; Iba (2021) is lineage/writing-style support only. | Pattern claims need explicit discovery or validation support rather than informal consensus, and examples must show how use is done in practice without turning every description into a tiring dossier. | `CaseCountercaseAndTransferCoverage`, `CoordinateEvidenceRefs`, and the first-pass slice require at least one usable application slice and, where broad scope is claimed, heterogeneous or known-use support. | This does not require controlled studies, long empirical packages, or known-use sections for every small FPF edit; ordinary first-pass remains lightweight. |
| Living pattern-quality reads need currentness windows and section-level reopen triggers, not whole-pattern churn. | Living-guideline currentness is adopted by analogy from Akl et al. (2017); PRISMA 2020, Page et al. (2021), is current-standard/reference-only for transparent reporting of review/update basis, not pattern-quality SoTA by itself. | The currentness unit is the live claim, coordinate, source stance, relation, or worked case, not automatically the whole pattern. | `QualificationWindow`, `refreshNeeded`, `SoTAStalenessSignals`, `CoordinateEvidenceRefs`, `ClaimSupportTraceabilityCurrentnessAndReplayability`, and `EvolutionFrontAndRefreshDiscipline` state what makes the read current and what can reopen it. | This does not import systematic-review or clinical-guideline workflow as mandatory apparatus for ordinary FPF pattern drafts. |
| Multi-characteristic improvement should preserve non-dominated alternatives and useful diversity instead of forcing one winner. | Current QD overview: `A survey on Quality-Diversity optimization: Approaches, applications, and challenges`, Swarm and Evolutionary Computation 100:102240 (2026), for QD currentness; retained lineage: MAP-Elites and the 2016 QD survey; CMA-ME/CMA-MAE, differentiable QD, and QDax-class accelerated QD practice are adopted only for the set-valued/front/archive idea. | Quality-diversity practice keeps diverse high-performing alternatives rather than collapsing to one scalar winner. | `PatternQualityFront`, `PatternImprovementArchive`, and `TieBreakerSet` keep viable candidate edits visible under a declared scope, while ordinary use remains first-pass and non-algorithmic. | No QD algorithm, grid, emitter policy, hardware stack, or library workflow becomes mandatory for pattern review. |
| Coordinate improvement can destroy the value the coordinates were meant to protect. | Current proxy-risk anchors include `Goodhart's Law in Reinforcement Learning` (ICLR 2024) and current catastrophic-Goodhart reward-misspecification work (NeurIPS 2024); retained lineage: Manheim and Garrabrant (2018) for the Goodhart taxonomy. | Overoptimization by a metric or proxy can become ineffective or harmful, and mixed Goodhart mechanisms need exact naming rather than broad "metric failure" prose. | `ProxyForValueSubstitutionResistance` becomes a load-bearing coordinate; before stop, the read asks what got worse in first-use cost, repair-impact predictability, neighbour ripple, bounded non-use, practical payoff, entry/projection integrity, or corpus ecology. | This does not make `E.21` an adoption forecast, economics model, or project-value estimator. |
| Pattern-quality evaluation must not become safety, security, compliance, or release certification. | Current-standard/reference-only governance-boundary material: UK AI Safety Institute, `AI Safety Institute approach to evaluations` (GOV.UK, current institutional guidance page), and `What AI evaluations for preventing catastrophic risks can and cannot do` (`arXiv:2412.08653`). These are adopted only for the non-overread boundary, not as FPF pattern-quality value sources. | Evaluations are useful, but evaluation alone is not sufficient for effective governance, real-world safety, or absence-of-risk claims. | `NeighborAuthorityAndBoundedUseFit`, `ClaimSupportTraceabilityCurrentnessAndReplayability`, `supportBoundaryEvidence`, and `PatternQualityStatus` keep project-side evidence, assurance, gate, release, work, safety, security, and compliance claims under exact receiving patterns. | This rejects compliance-by-checklist, audit theatre, and "review passed therefore safe/compliant" readings. It does not import AI-safety governance machinery into ordinary pattern-quality reading. |
| Pattern-quality stop decisions must keep perspective, resource cost, feasibility, acceptability, and equity or differential impact visible when they change admissible use. | Current-standard/reference-only decision-support material: GRADE Evidence-to-Decision practice is adapted for explicit decision perspective and resource/feasibility/acceptability/equity-impact criteria. | Resource use, cost, feasibility, acceptability, equity, and differential impact can legitimately change a recommendation or admissible use. | `WorkingReaderScope`, `UseAffordabilityAndApparatusProportionality`, `RepairLocalityAndChangeImpactPredictability`, and `StopCondition` treat cost and differential reader/practice impact as quality evidence when they change ordinary use. | This does not import clinical guideline panels, medical evidence grading, population-health policy machinery, or project-side impact assessment into FPF pattern review. |
| Retrieval-facing pattern quality needs component-level evidence, not one search-success score. | Retrieval-evaluation reference anchors for the narrow retrieval-facing entry problem: RAGAS, `Automated Evaluation of Retrieval Augmented Generation` (EACL 2024), and ARES, `An Automated Evaluation Framework for Retrieval-Augmented Generation Systems` (NAACL 2024), adopted only for the multi-dimensional retrieval-facing evaluation stance: context relevance, faithfulness to cited context, answer relevance, and component evidence. | Retrieval/RAG evidence distinguishes whether the right context is found, whether the answer is faithful to cited context, and whether the answer is relevant. | `retrievalHitQuality`, `coldReaderMisentryRate`, `ExternalEntryAndProjectionIntegrity`, `PatternLanguageEcologyFit`, and `CoordinateEvidenceRefs` may use tiny retrieval fixtures only when retrieval-facing entry, projection, or observed misretrieval is live. | This does not require universal RAG benchmarks or LLM evaluation harnesses for ordinary pattern drafts. |
| Measurement and bundle discipline should be internal to FPF rather than imported as a rival framework. | Inherited-current FPF neighbours: current FPF `C.16`, `A.17`, `A.18`, `A.19`, `C.25`, `E.8`, `E.19`, and `F.18`. | Existing FPF already has Characteristic/Scale, Q-Bundle, review, and naming machinery. | `E.21` composes those patterns and adds the missing pattern-quality receiving locus. | `E.21` does not replace the neighbouring patterns it cites. |
