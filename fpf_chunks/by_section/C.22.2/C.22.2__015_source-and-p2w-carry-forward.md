---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard"
section_id: "C.22.2:14"
section_title: "Source and P2W Carry-Forward"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__015_source-and-p2w-carry-forward.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "C.22.2 — ProblemCard"
  - "C.22.2:14 — Source and P2W Carry-Forward"
line_start: 52907
line_end: 52930
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.5"
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
  - "C.2.1"
  - "C.2.P"
  - "C.22"
  - "C.22.1"
  - "C.22.PFR"
  - "C.24"
  - "C.25"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.32.P2S"
  - "E.10"
  - "E.10.MOVE"
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
---

### C.22.2:14 - Source and P2W Carry-Forward

Apply the following source details as constraints on `C.22.2` use and its P2W-facing input.

| Source detail | Current FPF recovery | `C.22.2` carry-forward relation |
|---|---|---|
| Source examples: person, team, organization, System, community, episteme, and exact Work | Recognition material for the EntityOfConcern or exact A.15.6 Work when it changes problem-card use; not a new FPF kind taxonomy | A domain or practice locus may qualify the effective ReferenceScheme, ClaimScope, horizon, indicators, cost of error, the exact system-role kind or assignment, participation, viewpoint, or comparison, but it neither constitutes the card nor identifies an actual Problem. |
| Engineering language for reproducibility and management language for coordination, rights, resources, and responsibility | Verification and reproducibility, coordination, right, resource, system-role classification or assignment, participation, and responsibility claims are different FPF relations | `C.22.2` may retain bare *role* only as an E.10.ROLE cue; any exact kind, assignment, participation, budget, right, or responsibility field or relation reference follows its direct pattern. Claims outside the problem-side record stay there. |
| Problem factory, solution factory, and factory-of-factories | Source exposition for three related work families, not FPF process kinds | `C.22.2` covers only the problem-side output. Solution and P2W relations use `G.5`, `A.15`, `E.18`, `A.10`, `G.6`, `B.3`, `A.21`, `E.16`, and `G.11`; organizational-development or platform-capability questions are outside this pattern. |
| Characterization protocol: ReferenceScheme, ClaimScope or slice, compared set, exact system-role-kind, assignment, participation, or viewpoint qualification, scale, polarity, measurement Method, freshness, repeatability, budget, missing data, and comparison rules | `C.16`, `A.19`, `C.25`, `G.9`, and the exact qualification pattern | `ProblemCard` cites characterization, qualification, and comparability relations when current; available measurement or a visible label alone is not an accepted use relation. |
| Indicator uses: mandatory constraints, optimization objectives for the current cycle, and risk signals | Characteristic and Q-bundle use under selected comparison or acceptance | `C.22.2` preserves whether an indicator is used as a mandatory constraint, optimization objective, or monitored risk signal when that distinction affects acceptance; the use is not a system-role kind or assignment. |
| Problem portfolio as a period-bounded selected set with budget, assignment or participation cue, review cadence, and not-selected disposition | `G.5`, `C.19`, `G.9`, `G.11`, `A.6.P:7a`, `C.16.Q`, and E.10.ROLE when bare *role* is the source cue | `ProblemCard` preserves the source set or reference, selection or retention criterion, budget or window, review cadence, and not-selected or stepping-stone disposition. If an actual System, local system-role kind, assignment, participation, or responsibility relation matters, cite that independently obtaining direct claim rather than the portfolio wording. |
| Goldilocks as zone-of-growth selection calibrated to current capability, effective ReferenceScheme, and ClaimScope | Problem-side entry to current NQD, OEE, and set-return family | `C.22.2` does not turn Goldilocks into one global difficulty scale or scalar readiness score. |
| Stepping stones as option value: new actions, tools, data, interfaces, environments, or experiment modes that may expand downstream search | Retained archive, front, or pool member, or selected-set reason | `C.22.2` may record stepping-stone value only with a governing set-return, archive, or pool pattern and a retention or tie-break criterion. |
| P2W chain: signatures and principles help select formalism, ontology, characterization, and method-family material | `A.6.0`, `A.6.1`, `C.16`, `A.19`, `C.29`, `G.5`, and `E.18` | `C.22.2` supplies problem-side cues and relation references; it does not select the formalism, ontology, mechanism, or method family by itself. |
| P2W chain: condition measurement and comparison help select a concrete method | `C.16`, `A.19`, `C.25`, `G.9`, `G.5`, and `A.15` | State the comparison-and-acceptance cue or acceptance-criterion reference and parity and characterization relations needed by downstream method selection. |
| P2W chain: work planning makes planned work inspectable | `A.15.2` and `A.15.3` | `C.22.2` may supply problem-side input for `TaskSignature` preparation and assignment under C.22; the identifiable plan is one exact `U.WorkPlan`, and any planned-filling row remains declaration-local content addressed through that plan. |
| P2W chain: performed work produces work-result records | `A.15`, `A.10`, `G.6`, and `B.3` | `C.22.2` does not treat performed work or result records as problem-card fields beyond problem-side cues or named relation references. |
| P2W chain: result measurement can trigger refresh or return to earlier source material | `C.16`, `G.11`, `A.10`, `G.6`, `B.3`, `C.18`, and `C.19` | `C.22.2` states freshness or expiry and unknown-handling dispositions that let downstream result measurement refresh, retire, or re-open the problem-side record. |
| Runbook, rollback plan, canary, SafeStop, error budget, and override protocol | Work, gate, autonomy, evidence, and control records | These source forms are not `C.22.2` subobjects; apply `A.15`, `A.21`, `E.16`, `A.10`, `G.6`, or `B.3` when the corresponding claim is current. |
| Trust debt after reliance-window expiry | Freshness and decay indicator and bounded-risk continuation question | Treat trust debt as an indicator or problem-formulation follow-up reason, not as punishment, proof failure, or gate passage by itself. |

`C.22.2` remains the problem-side output. P2W carries its problem-side cues and, when current, exact receiving-use and Work references into method-family selection, work planning, performed-work interpretation, and result measurement.

