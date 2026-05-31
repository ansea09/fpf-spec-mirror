---
chunk_kind: "child"
pattern_id: "C.27"
pattern_title: "Temporal Claim Adequacy: State Readings, Temporal Trends, and Intervention-Sensitive Temporal Change"
section_id: "C.27:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.27/C.27__001_intro.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "C.27 — Temporal Claim Adequacy: State Readings, Temporal Trends, and Intervention-Sensitive Temporal Change"
  - "C.27:intro — Intro"
line_start: 47146
line_end: 47184
dependencies:
  - "A.3.3"
  - "B.1.4"
  - "B.1.6"
  - "C.16"
  - "C.18.1"
  - "C.19"
  - "C.22.1"
  - "C.24"
  - "C.25"
  - "C.26"
  - "C.26.3"
  - "C.27"
  - "C.28"
  - "G.9"
  - "U.Rhythm"
keywords:
  - "braking"
  - "coasting"
  - "dynamic benchmark"
  - "effort window"
  - "intervention-sensitive temporal change"
  - "rate reading"
  - "rate-change"
  - "recovery"
  - "resistance/inertia"
  - "rhythm/cadence"
  - "stabilization"
  - "state reading"
  - "temporal claim"
  - "temporal claim adequacy"
  - "temporal trend"
  - "throughput"
---

## C.27 - Temporal Claim Adequacy: State Readings, Temporal Trends, and Intervention-Sensitive Temporal Change


> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Temporal claim adequacy.

**Governed object.** C.27 governs authored temporal claims: descriptions in prose, plans, benchmark lines, dashboards, method notes, promises, or explanations that treat state, rate, rhythm, recovery, braking, coasting, redirection, stabilization, or rate-change as sufficient for some use.

**Described-system, description, and carrier discipline.** The described system, work, practice, method, service, or benchmark is not the C.27 record. A `Dyn2TemporalClaimAdequacyCard` or `Dyn2TemporalClaimProfile` is an authored description of temporal-claim adequacy. A document, table, page, report, or card may carry that description; it is not the temporal claim, not the dynamic system, and not the work trace.

**Use-context and basis discipline.** When this pattern says `supportedUse`, it means the decision, plan, diagnosis, comparison, publication, promise, assurance-facing relation, or other practical use that this exact C.27 record can carry given its claim posture, basis, windows, resistance or cost statement, and reopen condition. `unsupportedUse` means one nearby downstream claim, effect, or use that this exact record does not carry. These fields do not create permission; they state the pragmatic reach of the authored temporal-claim description.

Bare "support" should not do hidden ontology work in C.27. Use `supportedUse` and `unsupportedUse` only for the pragmatic reach of a temporal-claim record; use `evidence basis`, `model basis`, `source basis`, or `assumption` for the reason a reading is credible; use `RouteRef` or a named FPF pattern relation when an existing FPF pattern governs the other question.

**Boundary-crossing claim use.** The object remains an authored temporal claim. What changes is the use context: the claim is used as citable basis outside the immediate local discussion, published, benchmarked, promised, assured, made durable rationale, repeated in a reusable method description, used in a gate/public dashboard/Part G pack, or carried across context or scale. Casual reuse in a neighboring chat is not enough by itself. Boundary-crossing use is what can require a `Dyn2TemporalClaimProfile`.

**Use this pattern when** a claim about speed, rhythm, throughput, recovery, convergence, rollout, adoption, braking, coasting, redirection, or stabilization is used to change action and therefore needs effort, window, resistance, basis, supported-use, unsupported-use, and reopen discipline.

**Do not use this pattern when** the temporal wording is ordinary prose, a state reading or snapshot, a rate reading or trend reading whose measurement construction is enough, a formal `U.Dynamics` model, an actual work trace, a benchmark harness, a service promise, a quality judgement, or a residual quantum-like probe case without an intervention-sensitive temporal claim.

**C.27 in 60 seconds.** Use C.27 only if:

1. temporal wording is used to justify action, comparison, budget, gate, promise, assurance, or an explicit relation to another FPF pattern;
2. the difference between state, rate, and rate-change changes admissible use;
3. the text can name at least target, intervention, window, resistance or cost, basis, supported use, and unsupported use or reopen trigger.

Otherwise stop at ordinary prose, a Dyn0 state reading, a Dyn1 rate reading or trend reading, `C.16.P` when characteristic, scale, score, metric, or proxy wording is hidden, C.16 measurement discipline when the measurement construction is already recoverable, `C.16.Q` or `C.25` when overloaded quality wording or a quality-family endpoint is the live issue, `U.Dynamics` model discipline, or the existing FPF pattern that governs the other question.

For local diagnosis or planning, C.27 usually ends with one `Dyn2TemporalClaimAdequacyCard`. Plain references are enough while the use stays local. A local card should normally fit in 5-9 short lines; if it does not, clarify the claim, narrow it, or cite the existing FPF pattern that governs the other question. `RouteRef`, `C16RouteRef`, `G9ParityPlanRef`, and similar references appear only when the use is FPF-force-bearing beyond the local note.

**Quick refusals.** "Backlog is 120" is Dyn0; no C.27 record. "Backlog fell 20/week" is Dyn1, with C.16 if the measure is FPF-force-bearing; no C.27 record unless a rate-change use appears. "This section accelerates orientation" is ordinary prose unless the `PublicationUnit` carries that acceleration claim as method-effectiveness evidence.

**Dyn2 is not maturity.** Dyn2 classifies the use made of an authored temporal claim, not the system, team, method, or service being described. Higher `DynOrder` is not better; it only says what the authored temporal claim treats as sufficient for supported use.

**Local refresh boundary.** A local card carries only a reopen, downgrade, or pattern-reference condition. G.11, B.3.4, and assurance refresh discipline become relevant only when the temporal claim is public, Part G-facing, assurance-facing, or otherwise durable beyond local planning/diagnosis.

