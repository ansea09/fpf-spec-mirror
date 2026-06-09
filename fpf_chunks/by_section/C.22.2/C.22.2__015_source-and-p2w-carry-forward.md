---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:14"
section_title: "Source and P2W Carry-Forward"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__015_source-and-p2w-carry-forward.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:14 — Source and P2W Carry-Forward"
line_start: 44764
line_end: 44787
dependencies:
  - "A.10"
  - "A.15"
  - "A.19"
  - "A.21"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.Q"
  - "C.18"
  - "C.19"
  - "C.2.P"
  - "C.22"
  - "C.22.1"
  - "C.24"
  - "C.25"
  - "C.27"
  - "C.28"
  - "C.29"
  - "E.10"
  - "E.16"
  - "E.17"
  - "E.17.ID.CR"
  - "E.18"
  - "E.18.1"
  - "E.2"
  - "E.9"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "P2W-ready"
  - "Thin problem card"
  - "first-principles cue"
  - "freshness and unknown disposition"
  - "problem card"
  - "problem signal"
  - "problem-side record"
  - "safe-probe-needed"
  - "setContextRef"
  - "support posture"
  - "validation boundary"
---

### C.22.2:14 - Source and P2W Carry-Forward

The source presentation is not compressed into a generic problem-card summary. The following source details become carry-forward constraints for `C.22.2` use and for the P2W-facing relation from `C.22.2`.

| Source detail | Current FPF recovery | `C.22.2` carry-forward relation |
|---|---|---|
| Source examples: person, team, organization, system, community, episteme, and work project | Source-local recognition examples for the domain or practice locus when that locus helps identify use, and for the EntityOfConcern or project-side FPF kind or reference named by value when it changes the problem-side move; not a new FPF kind taxonomy | `ProblemCard@Context` may state the domain or practice locus when it affects time horizon, indicators, cost of error, role concern, or admissible comparison, but it must also state the context grounding that carries local meaning. The listed examples are not minted here as a new taxonomy of FPF kinds. |
| Engineering language for reproducibility and management language for coordination, rights, resources, and responsibility | Verification and reproducibility, coordination, right, resource, and responsibility claims are different FPF relations | `C.22.2` may name reproducibility, role, budget, right, or responsibility pressure only as a field or relation reference; claims outside the problem-side record stay with their governing patterns. |
| Problem factory, solution factory, and factory-of-factories | Source exposition for three related work families, not FPF process kinds | `C.22.2` covers only the problem-side output. Solution and P2W relations use `G.5`, `A.15`, `E.18`, `A.10`, `G.6`, `B.3`, `A.21`, `E.16`, and `G.11`; organizational-development or platform-capability questions are outside this pattern. |
| Characterization protocol: context or slice, compared set, role or viewpoint characteristics, scale, polarity, measurement method, freshness, repeatability, budget, missing data, and comparison rules | `C.16`, `A.19`, `C.25`, and `G.9` governing patterns | `ProblemCard@Context` must cite characterization and comparability relation when that relation is being made; it must not treat available measurement as admitted indicator. |
| Indicator roles: admission constraints, optimization objectives for the current cycle, and risk signals | Characteristic and Q-bundle use under selected comparison or acceptance | `C.22.2` must preserve whether an indicator is a mandatory constraint, an optimization objective, or a monitored risk signal when that distinction affects acceptance. |
| Problem portfolio as period-bounded selected set with budget, role assignment, review cadence, and not-selected disposition | `G.5`, `C.19`, `G.9`, `G.11`, `A.6.P:7a`, and `C.16.Q` | `ProblemCard@Context` must preserve source set or reference, selection or retention criterion, budget or window, review cadence, and not-selected or stepping-stone disposition when the set-source relation is live. |
| Goldilocks as zone-of-growth selection calibrated to current capability and context | Problem-side entry to current NQD, OEE, and set-return family | `C.22.2` must not turn Goldilocks into one global difficulty scale or scalar readiness score. |
| Stepping stones as option value: new actions, tools, data, interfaces, environments, or experiment modes that may expand downstream search | Retained archive, front, or pool member, or selected-set reason | `C.22.2` may record stepping-stone value only with a governing set-return, archive, or pool pattern and a retention or tie-break criterion. |
| P2W chain: signatures and principles help select formalism, ontology, characterization, and method-family material | `A.6.0`, `A.6.1`, `C.16`, `A.19`, `C.29`, `G.5`, and `E.18` | `C.22.2` supplies problem-side cues and relation references; it does not select the formalism, ontology, mechanism, or method family by itself. |
| P2W chain: condition measurement and comparison help select a concrete method | `C.16`, `A.19`, `C.25`, `G.9`, `G.5`, and `A.15` | State the comparison-and-acceptance cue or acceptance-criterion reference and parity and characterization relations needed by downstream method selection. |
| P2W chain: work planning makes planned work inspectable | `A.15`, `A.15.3`, and `SlotFillingsPlanItem` | `C.22.2` may emit or bind `TaskSignature`, but planned work stays in work-planning patterns. |
| P2W chain: performed work produces work-result records | `A.15`, `A.10`, `G.6`, and `B.3` | `C.22.2` must not treat performed work or result records as problem-card fields beyond problem-side cues or named relation references. |
| P2W chain: result measurement can trigger refresh or return to earlier source material | `C.16`, `G.11`, `A.10`, `G.6`, `B.3`, `C.18`, and `C.19` | `C.22.2` must state freshness or expiry and unknown-handling dispositions that let downstream result measurement refresh, retire, or re-open the problem-side record. |
| Runbook, rollback plan, canary, SafeStop, error budget, and override protocol | Work, gate, autonomy, evidence, and control records | These source forms are not `C.22.2` subobjects; apply `A.15`, `A.21`, `E.16`, `A.10`, `G.6`, or `B.3` when the corresponding claim is live. |
| Trust debt after validity expiry | Freshness and decay indicator and bounded-risk continuation question | Treat trust debt as an indicator or problem-formulation next-move reason, not as punishment, proof failure, or gate passage by itself. |

This carry-forward preserves detail, not broader scope. `C.22.2` remains the problem-side output; P2W uses it with enough source cues and project-side references to select method families, plans, performed work, and result measurement without making the problem card a P2W pattern.

