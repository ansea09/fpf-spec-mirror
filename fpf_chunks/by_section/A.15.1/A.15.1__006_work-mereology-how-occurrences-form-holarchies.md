---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:5"
section_title: "Work mereology (how occurrences form holarchies)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__006_work-mereology-how-occurrences-form-holarchies.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:5 — Work mereology (how occurrences form holarchies)"
line_start: 24521
line_end: 24595
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
  - "F.6"
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
  - "actual performer U.System"
  - "admitted U.Work kind"
  - "containing system"
  - "covering U.RoleAssignment"
  - "enacted method"
  - "optional direct bindings and resource use"
  - "performedUnderAssignment"
  - "separate result or consequence"
  - "temporal extent"
  - "world-side dated occurrence"
---

### A.15.1:5 - Work mereology (how occurrences form holarchies)

Work identity is occurrence-grounded and 4D. Start from the actual performance history: work-entry and end events, occupied spatiotemporal extent, performer systems and assignments, enacted method, containing system, any direct work-to-referent relations, actual bindings, resource use, and exact work-part or temporal relations. A distinct actual work-entry after an established completion or termination identifies a later occurrence; a proper work part and its parent are distinct individuals; independently grounded concurrent performances are distinct. A record, trace, policy episteme, or later judgment creates none of them. A continuity policy is needed only when a named use must decide how to group that already existing history across an interruption, resumption, mode or method switch, performer replacement, referent or binding change, or composite boundary.

#### A.15.1:5.1 - Parts and wholes of Work (occurrence facts)

* **Temporal-part (`TemporalPartOf_work`).** A proper **time-slice relation** over one selected Work occurrence or work phase. The selected part is grounded by parent work identity plus interval and, when needed, a named aspect such as resource use, telemetry, SLA coverage, or interval-local evidence. A temporal part is useful for monitoring, utilization, lead time, and interval-local evidence. It has no independent method-switch identity by that fact.
* **Episode-part (`EpisodeOf_work`).** A named, event-bounded fragment selected inside one parent Work occurrence because a named use needs that fragment. Entry, resumption, mode switch, switch-to-method, interruption, switch-away, completion, or a declared pause may supply the candidate boundary. The direct episode predicate also cites an exact `workContinuityPolicyRef` only when the use needs that policy to decide whether the fragment remains under the parent; timestamps or an episode-looking label alone establish no episode relation.

`workContinuityPolicyRef` designates the exact C.2.1 episteme whose claims state the named use, boundary events, tolerated variation, and branch criterion. Interpret those claims under that episteme's effective `U.ReferenceScheme`. Add a `U.ClaimScope`, temporal qualification window, or model-use structure only when changing it changes the segmentation assertion; otherwise omit it. The policy episteme classifies the already existing history for that use. A later or competing policy episteme can support another identity or segmentation assertion. Call it an **edition** only when an exact C.2.1 `EpistemeEditionRelation` obtains between the exact earlier and later epistemes; without that relation it is a non-continuing replacement. Either way, the policy neither becomes a `U.MethodDescription` by policy form nor changes the occurrence, its parts, or their actual facts.

* **Operational-part (`OperationalPartOf_work`).** A **work-part occurrence** that may enact a factor of a recovered `U.Method`, for example, an incision occurrence within an appendectomy occurrence, possibly **overlapping** with others in time. If a method-description reference is used, it identifies, describes, constrains, or evidences that method factor; the referenced `U.MethodDescription` is not enacted. If no `U.Method` factor is recovered, keep the material as the work part, evidence segment, telemetry segment, mechanism material, system-component behavior, or missing-source-relation note that was actually identified; do not infer a method factor from its label.
* **Concurrent work parts (derived use-side reading; no fourth parthood relation).** First state each exact work-part relation to the same parent and then state the independently governed interval `overlaps` fact. If a claim also says that the parts were coordinated, name its declared coordination predicate and actual participants. Shared parentage and overlap do not by themselves establish coordination, and `ConcurrentPartOf_work` is not introduced as a primitive work-part relation.

**Naming threshold.** Do not mint a durable public U-kind, durable named work object, or separate work occurrence for every interval, telemetry segment, pause, or episode-looking wording. Use a derivative part relation unless the downstream use needs a named work part with its own resources, evidence, KPI, acceptance, repair, aggregation, cross-context reliance, or source-relation return use. Otherwise keep the temporal relation, evidence slice, telemetry segment, method-description constituent, missing-source-relation note, or other concrete neighboring object that the task actually needs.

**Didactic rule:** **Method composition is not proof of Work decomposition, and Work decomposition is not proof of method composition.** A temporal work part may enact the same whole method during a slice. An episode may continue one method or mode, span several operational parts, repeat the same method fragment, or be split by evidence policy without changing method identity. An operational part may correspond to a method factor only when that factor is recovered as `U.Method`.

**Quick choice test.**

- Ask **"which interval or aspect of the parent work do I need?"** If that is enough, use `TemporalPartOf_work`.
- Ask **"does this named use need an event-bounded fragment of the parent?"** If yes, recover the candidate boundary events. Cite `workContinuityPolicyRef` only when interruption, resumption, switch, replacement, or pause leaves the grouping ambiguous for that use; then use `EpisodeOf_work` only when its direct predicate is satisfied.
- Ask **"which performed sub-occurrence has its own actual performer system, covering assignment, temporal extent, enacted method, affected referent, bindings, resource use, or aggregation role?"** If that is current, use `OperationalPartOf_work` or another declared work-part relation. A neighboring evaluation or effect claim does not establish work parthood by itself.
- Ask **"which way-of-doing part is being composed?"** If the answer needs preconditions, effects, interface, and whole-method relation, recover a `U.Method` submethod under `A.3.1` and `B.1.5`; do not make the work part itself carry the method identity.

#### A.15.1:5.2 - Key relations among Work

* **`precedes` or `happensBefore`** — strict partial order on Work windows.
* **`overlaps`** — intervals intersect but neither contains the other.
* **`contains` or `within`** — one Work's window contains another's.
* **Causal-use relation reference** — if one work occurrence is claimed to explain, trigger, or cause another, keep the work-occurrence link separate from the causal-use claim governed by `C.28` or another causal-use pattern named by value.
* **`retryOf`** — a later Work occurrence that starts after the earlier occurrence ended and re-attempts the same named objective or enacted Method under the exact predicate of the retry relation. Similar wording or revised bindings alone do not establish the link.
* **`resumptionOf`** — an event-bounded episode or later Work occurrence that continues after interruption. Cite a continuity policy only when the named use must decide whether the later performance remains under the same parent or is a distinct occurrence linked to the earlier one.

These relations are **occurrence facts**, not method-design assumptions.

#### A.15.1:5.3 - Work-occurrence relations used by Part B roll-ups

`A.15.1` supplies the identity of each independently identified Work occurrence or Work part and makes its exact temporal and performed resource-use relations recoverable. It does not itself return a temporal aggregate or resource ledger.

* **Temporal coverage.** When a receiving use needs utilization, elapsed time, phase coverage, or another roll-up over Work intervals, open `B.1.4`. Its recovered `ContextTemporalAggregation@Context`, coverage and non-overlap conditions, aggregation policy, and optional `Gamma_time` notation govern union, hull, or another admitted temporal aggregate. The work intervals remain A.15.1 facts.
* **Resource aggregation.** When a receiving use needs a total over materials, energy, time, money, tool wear, or another performed resource value, open `B.1.6`. Its recovered `WorkResourceAggregation@Context`, typed resource-accounting basis, evidence refs, overlap or deduplication policy, ledger, aggregation rule, and optional `Gamma_work` notation govern the aggregate. Each contributing performed resource-use relation obtains separately with its exact Work occurrence as a participant; any ledger or assertion about that relation is a separate episteme.

**Manager's tip:** cite the exact `B.1.4` or `B.1.6` aggregation result and policy beside the KPI. A Work-part list, shared parent, or operator spelling supplies neither the aggregate nor its policy.

#### A.15.1:5.4 - Identity and reidentification of Work

Two descriptions, assertions, records, or traces resolve to the same Work occurrence only when they designate the same actual world-side performance history, not merely the same name, policy label, similar policy content, or later date. First compare the direct facts at the selected grain:

* the same actual work-entry or start and compatible occupied spatiotemporal extent;
* the same performance history, with each performer system, covering assignment, enacted method, and containing system, plus every actually obtaining work-to-referent, binding, and resource-use fact used by the identity claim, placed at the interval where it obtains;
* compatible work-part and temporal relations; and
* no fact that already identifies distinct individuals: a proper part versus its parent, independently grounded concurrent performances, or a later work-entry after the first occurrence's established completion or termination.

A corrected or later description of the same actual start, open end, or completed end can refine the assertion without changing the occurrence. A change of performer, assignment, method, referent, binding, resource use, or containing system during an otherwise unended performance history is an actual change to state explicitly; that change alone neither splits nor preserves the Work occurrence.

When a named receiving use must decide whether an interruption, resumption, method or mode switch, performer replacement, retune, rework, referent or binding change, or composite boundary stays inside one parent, cite the exact continuity-policy episteme, its effective reference scheme, applicable scope and window, and the branch criterion it applies to those facts. The selected policy can support one identity or segmentation assertion for that use. A later or competing policy episteme may support another assertion; call it a later edition only when the exact C.2.1 `EpistemeEditionRelation` obtains, and otherwise treat it as a non-continuing replacement. Neither branch retroactively changes what occurred.

#### A.15.1:5.5 - Interruptions, retries, resumptions, and description changes

* **Established end and later entry:** identify a later Work occurrence when the first occurrence has actually completed or terminated and another work-entry occurs. A larger composite Work may contain both only through explicit work-part relations.
* **Retry:** identify the later Work occurrence independently and add `retryOf` only when that relation's own predicate connects it to the ended attempt.
* **Ambiguous interruption or resumption:** preserve the actual boundary events and facts. If a named use must decide same-parent versus separate-occurrence grouping, apply its exact `workContinuityPolicyRef`; without that criterion, return an unresolved segmentation rather than making the policy implicit.
* **Performer, assignment, method, referent, binding, retune, or mode change:** state the actual change where it occurs. Split or retain the parent only when the direct facts already decide the boundary or a policy current to the named identity, episode, retry, resumption, or aggregation use supplies the criterion.
* **Method-description episteme change:** record the newly selected description episteme separately. That selection neither splits nor preserves Work by itself; only an accompanying actual occurrence change enters the boundary judgment. Call the two descriptions editions only when their exact C.2.1 `EpistemeEditionRelation` obtains.
* **Rework:** identify the later performance independently. Relate it as another occurrence, episode, or operational part only after the applicable direct predicate and any genuinely needed boundary policy are satisfied. Keep causal attribution with the governing causal-use pattern.

Plans, costs, quality statistics, telemetry evidence, and method-reliance claims may depend on whether the selected history is a temporal part, event-bounded episode, operational part, or later occurrence. Name a continuity-policy episteme, effective reference scheme, scope, and qualification window only when that distinction is actually current. Otherwise retain the direct occurrence facts and stop; do not add policy apparatus to a simple uninterrupted case.

#### A.15.1:5.6 - Work mereology does not compose effects or transformations

A parent Work can have exact work parts without having one composite effect or composite transformation. Any temporal aggregate uses `B.1.4`; any performed-resource aggregate uses `B.1.6`; each names its own concern, policy, evidence, and result. Identify every actual transformation independently under A.3.4. Connect one to Work only through a named domain predicate and exact participants, or a C.2.1 local compound claim under A.6.RCD disposition 2 with its constructor, governed bases, participants, and case facts recoverable; otherwise return `missing-governor[work-to-change]`.

Work parthood, method parthood, temporal inclusion, a common affected referent, a list of changed characteristics, or adjacent plan items establishes neither transformation parthood nor a composite transformation. If a production or effect claim needs transformation composition, name the declared composition predicate, its participants, and the facts that make it obtain. If none is available, retain the exact Work and independently identified transformations and return `missing-governor[transformation-composition]`. A.15.PROD may still recover any independent production-work, entity-inception, or completion claim that does not depend on that missing composition.

