---
chunk_kind: "child"
pattern_id: "E.21"
pattern_title: "FPF Pattern Quality Characteristic Space"
section_id: "E.21:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.21/E.21__012_sota-echoing.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "E.21 — FPF Pattern Quality Characteristic Space"
  - "E.21:11 — SoTA-Echoing"
line_start: 65037
line_end: 65055
dependencies:
  - "A.17-A.19"
  - "A.6.P"
  - "A.6.Q"
  - "C.16"
  - "C.2.P"
  - "C.25"
  - "E.11"
  - "E.17.AUD"
  - "E.19"
  - "E.8"
  - "F.18"
  - "J.4"
keywords:
  - "Goodhart/proxy substitution"
  - "Pareto/front comparison"
  - "PatternQualityCharacteristicSpace"
  - "PatternQualityQBundle"
  - "activation-normalized coordinates"
  - "and admissibility predicates are not written as duties"
  - "bounded non-use"
  - "coordinate evidence"
  - "definitions"
  - "eligibility filters"
  - "first move"
  - "invariants"
  - "pattern quality"
  - "state agent obligations only"
  - "stop condition"
  - "typing rules"
---

### E.21:11 - SoTA-Echoing

`E.21:11` is a SoTA-binding table, not a bibliography. A row is live only when it changes at least one `E.21` field, eligibility condition, coordinate, worked slice, relation, conformance item, non-use boundary, or stop/reopen condition.

If a `SoTA Synthesis Pack@CG-Frame` exists for pattern-quality evaluation, this section cites its claim IDs and does not fork an untracked SoTA narrative. If no pack exists, this section is a provisional seed and must still state `adopt | adapt | reject`, the concrete `E.21` effect, and the boundary of non-overread.

A source that only supports lineage, popularity, or familiar terminology is not a SoTA row. It may remain as rationale support, but it does not satisfy `SoTABindingMinimum`.

| Claim | Source stance | Adopted/adapted content | Concrete E.21 effect | Boundary of non-overread |
|---|---|---|---|---|
| Pattern-quality evidence must show applicability and generality without making ordinary reading heavy. | Riehle et al. (2021) are adopted for explicit pattern validation methods; Zarras (2023) is adopted for applicability/generality evidence; Iba (2021) is retained only as writing-style support. | Pattern claims need explicit discovery or validation support rather than informal consensus, and examples must show how use is done in practice without turning every description into a tiring dossier. | `CaseCountercaseAndTransferCoverage`, `CoordinateEvidenceRefs`, and the first-pass slice require at least one usable application slice and, where broad scope is claimed, heterogeneous or known-use support. | This does not require controlled studies, long empirical packages, or known-use sections for every small FPF edit; ordinary first-pass remains lightweight. |
| Living pattern-quality reads need currentness windows and section-level reopen triggers, not whole-pattern churn. | Akl et al. (2017) living guidelines are adopted and adapted; Page et al. (2021) PRISMA 2020 is used only for transparent reporting of review/update basis. | The currentness unit is the live claim, coordinate, source stance, relation, or worked case, not automatically the whole pattern. | `QualificationWindow`, `refreshNeeded`, `SoTAStalenessSignals`, `CoordinateEvidenceRefs`, `ClaimSupportTraceabilityCurrentnessAndReplayability`, and `EvolutionFrontAndRefreshDiscipline` state what makes the read current and what can reopen it. | This does not import systematic-review or clinical-guideline workflow as mandatory apparatus for ordinary FPF pattern drafts. |
| Multi-characteristic improvement should preserve non-dominated alternatives and useful diversity instead of forcing one winner. | MAP-Elites and the 2016 QD survey are retained as lineage; CMA-ME/CMA-MAE, differentiable QD, and QDax-class accelerated QD practice are adopted only for the set-valued/front/archive idea. | Quality-diversity practice keeps diverse high-performing alternatives rather than collapsing to one scalar winner. | `PatternQualityFront`, `PatternImprovementArchive`, and `TieBreakerSet` keep viable candidate edits visible under a declared scope, while ordinary use remains first-pass and non-algorithmic. | No QD algorithm, grid, emitter policy, hardware stack, or library workflow becomes mandatory for pattern review. |
| Coordinate improvement can destroy the value the coordinates were meant to protect. | Manheim and Garrabrant (2018) are adopted for distinguishing Goodhart/proxy-overoptimization failure modes; internal `E.12` and `E.13` remain the FPF receiving support. | Overoptimization by a metric or proxy can become ineffective or harmful, and mixed Goodhart mechanisms need exact naming rather than broad "metric failure" prose. | `ProxyForValueSubstitutionResistance` becomes a load-bearing coordinate; before stop, the read asks what got worse in first-use cost, repair-impact predictability, neighbour ripple, bounded non-use, practical payoff, entry/projection integrity, or corpus ecology. | This does not make `E.21` an adoption forecast, economics model, or project-value estimator. |
| Pattern-quality evaluation must not become safety, security, compliance, or release certification. | AI evaluation-limit literature, UK AI Safety Institute evaluation guidance, and related governance work are adopted only for the non-overread boundary: evaluations can support claims but do not prove absence of risk or certify the project world. | Evaluations are useful, but evaluation alone is not sufficient for effective governance, real-world safety, or absence-of-risk claims. | `NeighborAuthorityAndBoundedUseFit`, `ClaimSupportTraceabilityCurrentnessAndReplayability`, `supportBoundaryEvidence`, and `PatternQualityStatus` keep project-side evidence, assurance, gate, release, work, safety, security, and compliance claims under exact receiving patterns. | This rejects compliance-by-checklist, audit theatre, and "review passed therefore safe/compliant" readings. It does not import AI-safety governance machinery into ordinary pattern-quality reading. |
| Pattern-quality stop decisions must keep perspective, resource cost, feasibility, acceptability, and equity or differential impact visible when they change admissible use. | GRADE Evidence-to-Decision practice is adapted for explicit decision perspective and resource/feasibility/acceptability/equity-impact criteria. | Resource use, cost, feasibility, acceptability, equity, and differential impact can legitimately change a recommendation or admissible use. | `WorkingReaderScope`, `UseAffordabilityAndApparatusProportionality`, `RepairLocalityAndChangeImpactPredictability`, and `StopCondition` treat cost and differential reader/practice impact as quality evidence when they change ordinary use. | This does not import clinical guideline panels, medical evidence grading, population-health policy machinery, or project-side impact assessment into FPF pattern review. |
| Retrieval-facing pattern quality needs component-level evidence, not one search-success score. | RAGAS and ARES are adopted only for the multi-dimensional retrieval-facing evaluation stance: context relevance, support/faithfulness, answer relevance, and component evidence. | Retrieval/RAG evidence distinguishes whether the right context is found, whether the answer is faithful to support, and whether the answer is relevant. | `retrievalHitQuality`, `coldReaderMisentryRate`, `ExternalEntryAndProjectionIntegrity`, `PatternLanguageEcologyFit`, and `CoordinateEvidenceRefs` may use tiny retrieval fixtures only when retrieval-facing entry, projection, or observed misretrieval is live. | This does not require universal RAG benchmarks or LLM evaluation harnesses for ordinary pattern drafts. |
| Measurement and bundle discipline should be internal to FPF rather than imported as a rival framework. | Current FPF `C.16`, `A.17`, `A.18`, `A.19`, `C.25`, `E.8`, `E.19`, and `F.18` are adopted internally. | Existing FPF already has Characteristic/Scale, Q-Bundle, review, and naming machinery. | `E.21` composes those patterns and adds the missing pattern-quality receiving locus. | `E.21` does not replace the neighbouring patterns it cites. |

