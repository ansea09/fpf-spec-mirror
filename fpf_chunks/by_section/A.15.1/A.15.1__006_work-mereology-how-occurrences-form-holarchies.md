---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:5"
section_title: "Work mereology (how occurrences form holarchies)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__006_work-mereology-how-occurrences-form-holarchies.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:5 — Work mereology (how occurrences form holarchies)"
line_start: 24364
line_end: 24436
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.6"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "B.1.4"
  - "B.1.6"
  - "B.3"
  - "C.2.1"
  - "C.27.TA"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "U.Capability"
  - "U.Method"
  - "U.MethodDescription"
  - "U.ReferenceScheme"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.System"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "U.Work admitted kind"
  - "actual binding"
  - "affected referent"
  - "enactsMethod"
  - "episode"
  - "no automatic transformation"
  - "occurrence assertion and record separation"
  - "overlap"
  - "performed resource-use fact"
  - "performedBy"
  - "retry"
  - "work continuity"
  - "work part"
  - "world-side dated occurrence"
---

### A.15.1:5 - Work mereology (how occurrences form holarchies)

Work identity is occurrence-grounded and 4D, but temporal extent alone is not sufficient. Resolve one occurrence under its exact `workContinuityPolicyRef` using performer assignment, actual enacted method, extent, affected referent, containing system, actual bindings, resource-use facts, and the tolerances current to that policy. MethodDescription, plan, log, publication, or trace identity does not replace this rule.

#### A.15.1:5.1 - Parts and wholes of Work (occurrence facts)

* **Temporal-part (`TemporalPartOf_work`).** A proper **time-slice relation** over one selected Work occurrence or work phase. The selected part is grounded by parent work identity plus interval and, when needed, a named aspect such as resource use, telemetry, SLA coverage, or interval-local evidence. A temporal part is useful for monitoring, utilization, lead time, and interval-local evidence. It has no independent method-switch identity by that fact.
* **Episode-part (`EpisodeOf_work`).** A **policy-governed, event-bounded, maximally continuous enactment fragment** of one parent Work occurrence. It starts at a work-entry, resumption, mode-switch, or switch-to-method event and ends at interruption, switch-away, completion, or a policy-declared pause. It is not an arbitrary time slice. It remains under the parent work identity only when exact `workContinuityPolicyRef` says that the interrupted or resumed activity is still the same Work occurrence; `WorkEpisode` is not introduced as a second kind or relation name.
`workContinuityPolicyRef` designates the exact C.2.1 episteme whose claims state the episode boundaries, tolerated variation, and work-continuity rule used for this occurrence. Interpret those claims under that episteme's effective `U.ReferenceScheme`; name any current `U.ClaimScope`, temporal qualification window, or model-use structure separately. The policy episteme governs the identity judgment without becoming a MethodDescription, context container, or work part.

* **Operational-part (`OperationalPartOf_work`).** A **work-part occurrence** that may enact a factor of a recovered `U.Method`, for example, an incision occurrence within an appendectomy occurrence, possibly **overlapping** with others in time. If a method-description reference is current, it identifies, describes, constrains, or evidences that method factor; the referenced `U.MethodDescription` is not enacted. If no `U.Method` factor is recovered, govern the material as a work part, evidence segment, telemetry segment, mechanism material, system-component behavior, or missing-source-relation note under the direct pattern.
* **Concurrent work parts (derived use-side reading; no fourth parthood relation).** First state each exact work-part relation to the same parent and then state the independently governed interval `overlaps` fact. When coordination is current, state its exact direct relation separately. Shared parentage and overlap do not by themselves establish coordination, and `ConcurrentPartOf_work` is not introduced as a primitive work-part relation.

**Naming threshold.** Do not mint a durable public U-kind, durable named work object, or separate work occurrence for every interval, telemetry segment, pause, or episode-looking wording. Use a derivative part relation unless the downstream use needs a named work part with its own resources, evidence, KPI, acceptance, repair, aggregation, cross-context reliance, or source-relation return use. Otherwise lower to a temporal relation, evidence slice, telemetry segment, method-description constituent, missing-source-relation note, or the neighboring object that is actually current.

**Didactic rule:** **Method composition is not proof of Work decomposition, and Work decomposition is not proof of method composition.** A temporal work part may enact the same whole method during a slice. An episode may continue one method or mode, span several operational parts, repeat the same method fragment, or be split by evidence policy without changing method identity. An operational part may correspond to a method factor only when that factor is recovered as `U.Method`.

**Quick choice test.**

- Ask **"which interval or aspect of the parent work do I need?"** If that is enough, use `TemporalPartOf_work`.
- Ask **"which continuous attempt under the episode policy do I need?"** If entry, resumption, mode-switch, interruption, switch-away, completion, or policy pause is the boundary, use `EpisodeOf_work`.
- Ask **"which performed sub-occurrence has its own performer assignment, temporal extent, enacted method, affected referent, bindings, resource use, or aggregation role?"** If that is current, use `OperationalPartOf_work` or another declared work-part relation. A neighboring evaluation or effect claim does not establish work parthood by itself.
- Ask **"which way-of-doing part is being composed?"** If the answer needs preconditions, effects, interface, and whole-method relation, recover a `U.Method` submethod under `A.3.1` and `B.1.5`; do not make the work part itself carry the method identity.

#### A.15.1:5.2 - Key relations among Work

* **`precedes` or `happensBefore`** — strict partial order on Work windows.
* **`overlaps`** — intervals intersect but neither contains the other.
* **`contains` or `within`** — one Work's window contains another's.
* **Causal-use relation reference** — if one work occurrence is claimed to explain, trigger, or cause another, keep the work-occurrence link separate from the causal-use claim governed by `C.28` or another causal-use pattern named by value.
* **`retryOf`** — a new Work occurrence re-attempting the same intended objective or enacted Method after the prior occurrence has ended under the exact work-continuity policy; revised bindings remain separately governed actual facts.
* **`resumptionOf`** — an episode or later occurrence that **continues** after interruption; policy decides whether it is under the same parent Work-occurrence identity or a separate Work occurrence linked to the earlier occurrence.

These relations are **occurrence facts**, not method-design assumptions.

#### A.15.1:5.3 - Work-occurrence relations used by Part B roll-ups

`A.15.1` supplies the identity of each independently identified Work occurrence or Work part and makes its exact temporal and performed resource-use relations recoverable. It does not itself return a temporal aggregate or resource ledger.

* **Temporal coverage.** When a receiving use needs utilization, elapsed time, phase coverage, or another roll-up over Work intervals, open `B.1.4`. Its recovered `ContextTemporalAggregation@Context`, coverage and non-overlap conditions, aggregation policy, and optional `Gamma_time` notation govern union, hull, or another admitted temporal aggregate. The work intervals remain A.15.1 facts.
* **Resource aggregation.** When a receiving use needs a total over materials, energy, time, money, tool wear, or another performed resource value, open `B.1.6`. Its recovered `WorkResourceAggregation@Context`, typed resource-accounting basis, evidence refs, overlap or deduplication policy, ledger, aggregation rule, and optional `Gamma_work` notation govern the aggregate. Each contributing performed resource-use relation obtains separately with its exact Work occurrence as a participant; any ledger or assertion about that relation is a separate episteme.

**Manager's tip:** cite the exact `B.1.4` or `B.1.6` aggregation result and policy beside the KPI. A Work-part list, shared parent, or operator spelling supplies neither the aggregate nor its policy.

#### A.15.1:5.4 - Identity and reidentification of Work

Two descriptions, assertions, records, or traces resolve to the same Work occurrence only when they designate one occurrence under the exact `workContinuityPolicyRef` and its declared tolerances. Check at least:

* compatible spatiotemporal extent at the selected resolution;
* the same exact set of performer `U.RoleAssignment` values current at the selected identity grain;
* the same actual enacted `U.Method`, or a policy-admitted method switch within one occurrence;
* the same containing `U.System` and affected referent at the identity grain;
* compatible actual direct-relation and A.6.1 bindings, with every admitted change named by policy; and
* compatible resource-use and work-part facts where the policy makes them identity-bearing.

An occurrence designator, label, ticket, record, MethodDescription edition, WorkPlan, publication, evidence set, or model-use structure may help resolve the occurrence but does not decide identity. A changed description edition alone does not reidentify work when the enacted method and occurrence facts remain the same. A changed performer assignment, enacted method, extent, affected referent, containing system, actual binding, or continuity outcome identifies another occurrence unless the exact policy admits the variation inside one bounded Work.

#### A.15.1:5.5 - Interruptions, retries, resumptions, and description changes

* **Retry:** identify a new Work occurrence admitted under `U.Work`, with its own extent and actual bindings; link it through `retryOf` only when that relation's policy holds.
* **Episode under the same parent work:** retain event-bounded fragments inside one Work occurrence only when `workContinuityPolicyRef` admits the interruption, resumption, mode switch, or policy pause.
* **Separate occurrence after interruption or actual change:** identify another Work occurrence when the policy treats interruption, retune, rework, retry, changed actual binding, changed affected referent, switch-away, restart, or method switch as crossing the work boundary. Link occurrences only through an exact obtaining `retryOf`, `resumptionOf`, `precedes`, `overlaps`, `contains`, or other declared relation.
* **MethodDescription change:** record the selected description edition separately. A changed description edition neither splits nor preserves Work by itself; apply the continuity policy to the actual enacted method and occurrence facts.
* **Rework:** identify new work after failed earlier work unless the exact policy admits it as an episode or operational part of the same parent occurrence. Keep any causal attribution with the governing causal-use pattern.

Plans, costs, quality statistics, telemetry evidence, and method-reliance claims depend on whether the selected interval is a temporal part, event-bounded episode, operational part, or new occurrence. Name the exact policy episteme, effective reference scheme, and any current scope or temporal qualification before relying on that distinction.

#### A.15.1:5.6 - Work mereology does not compose effects or transformations

A parent Work can have exact work parts without having one composite effect or composite transformation. Any temporal aggregate uses `B.1.4`; any performed-resource aggregate uses `B.1.6`; each names its own aggregation concern, policy, and evidence. Identify every actual transformation independently under A.3.4 and every work-to-change fact under its direct governor.

Work parthood, method parthood, temporal inclusion, a common affected referent, a list of changed characteristics, or adjacent plan items establishes neither transformation parthood nor a composite transformation. If a receiving production or effect claim requires transformation composition and no accepted governor supplies it, retain the exact Work and independently identified transformations and return the missing-governor blocker. A.15.PROD may still recover any independent production-work, entity-inception, or completion claim that does not depend on that missing composition.

