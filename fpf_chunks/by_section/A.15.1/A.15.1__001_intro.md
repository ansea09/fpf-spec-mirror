---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__001_intro.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:intro — Intro"
line_start: 19992
line_end: 20018
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3.1"
  - "A.3.2"
  - "B.1"
  - "B.1.6"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.System"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "actuals"
  - "event"
  - "execution"
  - "log"
  - "occurrence"
  - "run"
---

## A.15.1 - U.Work

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Use `U.Work` when the question under repair is what actually happened: a dated, resource-consuming occurrence enacted by a holder under `U.RoleAssignment`, inside a `U.BoundedContext`, with method, time window, parameters, resources, affected referent, result, and evidence kept inspectable.

**Use this when.** Use this pattern when a plan, method description, schedule, log, telemetry stream, dashboard, approval-looking cue, or result statement is being treated as if it were actual performed work. `U.Work` is the run-time occurrence; the surrounding records may identify, constrain, evidence, schedule, or judge it, but they do not become the occurrence by being published.

**First output.** One work-occurrence record naming `performedBy -> U.RoleAssignment`, `enactsMethod -> U.Method`, `methodDescriptionRef` when the source episteme is live, `executedWithin`, time window, concrete parameter bindings, affected referent, resource ledger, pre-state and post-state anchors or a declared delta predicate, outcome, and the governing `U.BoundedContext`.

**Working action path.**
1. Name the candidate occurrence and the work move that depends on it.
2. Recover the `U.RoleAssignment`, enacted `U.Method`, method-description source, time window, system or subsystem accountable for the occurrence, affected referent, parameters, resources, and outcome.
3. Decide whether the item is actual `U.Work`, only a plan (`A.15.2`), only a method or method description (`A.15`), only evidence for work (`A.10`), or a work-relevant source-restoration case (`A.15.4`).
4. For composite, repeated, interrupted, or overlapping occurrences, declare the work-part relation and aggregation policy before using totals or identity claims.
5. If the required anchors cannot be recovered, lower the claim to a source-gap note, work-evidence note, plan note, or source-restoration request; do not backdate work.

**Ordinary use.** For a simple run, one compact work card with performer, method, time window, affected referent, resources, and outcome is enough.

**Reliance-bearing use.** Use the full record when the work occurrence carries cost, quality, audit, evidence, compliance, gate, release, result measurement, cross-context reuse, or aggregation claims.

**Stop condition.** Stop once the occurrence is either recoverable as `U.Work` at the needed granularity or lowered to a neighboring record that no longer claims performed work.

**Not this pattern when.** Not this pattern when the live object is only a method description, only a plan or schedule (`A.15.2`), only a slot-filling plan item (`A.15.3`), only a visible source cue that must be restored before reliance (`A.15.4`), only evidence or assurance (`A.10` or `B.3`), or only publication-use or representation behavior (`E.17`, `A.7`, or the relevant representation pattern).

