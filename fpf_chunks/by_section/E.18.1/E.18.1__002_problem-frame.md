---
chunk_kind: "child"
pattern_id: "E.18.1"
pattern_title: "P2W Problem-to-Work Carry-Through"
section_id: "E.18.1:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.1/E.18.1__002_problem-frame.md"
commit_sha: "7ba40a95a967ca5c69afc63aeca381e6adedc8da"
heading_path:
  - "E.18.1 — P2W Problem-to-Work Carry-Through"
  - "E.18.1:1 — Problem frame"
line_start: 83584
line_end: 83620
dependencies:
  - "A.15"
  - "A.15.PROD"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.0"
  - "A.6.1"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.2"
  - "C.29"
  - "E.11.PUA"
  - "E.11.PUR"
  - "E.18"
  - "E.18.3"
  - "F.17"
  - "F.18"
  - "F.8"
  - "F.9"
  - "G.11"
  - "G.2"
  - "G.5"
  - "G.9"
  - "U.Mechanism"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Signature"
keywords:
---

### E.18.1:1 - Problem frame

Use this pattern when an accepted `ProblemCard@Context` is ready enough to guide work, but the next FPF use is unsettled. Ask which accepted distinction should shape the next question, which relation and participants that question asserts, and what result or stop is needed before the next action.

The accepted `ProblemCard@Context` is the primary `EntityOfConcern` of any materialized P2W note. Start from one accepted claim and one decision or use that needs it. Then state the relation being asserted, name its participants, and apply the pattern that governs that relation. A separately identified `U.Viewpoint` episteme or `BoundedModelUseStructure` participates only when the claim designates that object and its organization changes how the receiving claim is interpreted; neither becomes an identity field of the ProblemCard or note. Method selection, planning, dated work, actual change, result interpretation, and return remain separate continuations under their direct patterns. P2W introduces no relation kind or occurrence and is neither dated work nor a `U.Transformation`. A governing-pattern reference, selected continuation, recommendation, imperative sentence or intended realization does not admit any episteme as `U.MethodDescription`; A.3.2 requires one already identified C.2.1 episteme, one independently admitted `U.Method` as its exact EntityOfConcern, and at least one substantive way-of-doing claim.

Keep three objects separate. The **accepted ProblemCard** is the `EntityOfConcern` of a materialized P2W note. The note is identified under `C.2.1` by its ClaimGraph, that exact card, and its effective `U.ReferenceScheme`; its ClaimGraph names the receiving use and designates a separately identified viewpoint or model-use structure only when the claim uses that object and its organization changes how the receiving claim is interpreted. The **subject EntityOfConcern** of each direct pattern is the system, episteme, method, role, work occurrence, relation, or other project entity addressed by that pattern. The **compact note, diagram, plan, trace, and publication** are epistemes or publication-side values that describe, constrain, or make those direct claims inspectable. Later method enactment or dated work can change or preserve a subject EntityOfConcern; improving a P2W note or completing its fields does not establish that subject change, work occurrence, evidence, acceptance, or result.

**Primary reader and question.** The reader already has an accepted `ProblemCard@Context` and must decide one next claim. Ask in ordinary words: **what relation am I asserting, between which participants, and what result would change the next action?** Then apply the pattern that governs that relation. Source wording or a supporting episteme may help formulate the question but does not supply the downstream result.

**So-what adoption test.** Use P2W only when keeping the accepted distinction changes which relation you assert, what result you write, or whether you continue, split, stop, or return. If the relation and result are already settled and P2W would add only another note, skip P2W and apply the direct pattern.

E.11.PUA governs a smaller use and may begin without `ProblemCard@Context`: apply one selected pattern to one current practical question, obtain the first directly typed result, and state its receiving use. E.18.1 begins only when the wider work-facing continuation depends on preserving accepted problem-side material. PUA may support one pattern inspection inside a P2W flow, but it does not replace the accepted-problem carry-through.


#### E.18.1:1.1 - Use this when

- an accepted `ProblemCard@Context` names a working problem and the team needs a disciplined next FPF use toward method, planning, performed work, or result interpretation;
- an invariant, `U.Signature(profile=FormalSubstrate)`, `PrincipleFrame`, mechanism-position, method-position, `A.15.2 U.WorkPlan` or plan-item, performed-work, result-record, or source-currentness cue is present, but the FPF kind or relation to use next is still unsettled;
- a transformation-flow structure, mathematical path relation in a graph-shaped description, flow diagram, principle scheme, scenario, functional description, or source publication helps the team think, while the next FPF use still lacks an FPF kind or relation named by value;
- a result artifact, telemetry line, acceptance record, quality-evaluation record, done-state update, feedback pin, or integration claim needs to be unpacked before it can guide the next FPF use.

#### E.18.1:1.2 - What goes wrong if missed

The team jumps from a convincing problem-side formulation into downstream language without naming the FPF relation being used. The work then looks responsive to the accepted problem, but the next record is unclear, the result phrase becomes too broad, and measurement or source-currentness changes have no honest return relation.

#### E.18.1:1.3 - What this buys

The practitioner gets one concrete next move: keep the accepted claim in view, state the question and participants, apply the pattern that answers it, and use the result it returns. Split several relation claims before applying their patterns. If the relation or needed facts are missing, keep the cue and stop. If a relied-on result changes, reopen only the continuation that used it. Add the compact note only when another person or later action must replay that path. The accepted problem-side distinction remains useful without becoming hidden permission to start work.

#### E.18.1:1.4 - Not this pattern when

- there is no accepted problem-side record; use `C.22.2` or the problem-side pattern named by value first;
- the FPF kind under repair, relation, and record to write are already settled; use that pattern directly and do not add a P2W layer;
- the requested output is a local project procedure, schedule, or work-management method; use the relevant work, planning, method, gate, or operational-management pattern;
- the requested record or claim is an evidence case, assurance case, gate record, decision record, architecture description, publication-use claim, or wording-use repair; use the recovered relation and its governing pattern directly.

