---
chunk_kind: "child"
pattern_id: "A.3.1"
pattern_title: "U.Method: Reusable Way of Doing with Explicit Applicability"
section_id: "A.3.1:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.1/A.3.1__008_conformance-checklist.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "A.3.1 — U.Method: Reusable Way of Doing with Explicit Applicability"
  - "A.3.1:7 — Conformance Checklist"
line_start: 8364
line_end: 8391
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.15.1"
  - "A.15.2"
  - "A.22"
  - "A.3"
  - "A.3.2"
  - "A.6.1"
  - "A.6.5"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.1.5"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.3.1"
  - "C.3.2"
  - "E.18"
  - "E.18.1"
  - "E.20"
  - "F.9"
  - "G.5"
keywords:
---

### A.3.1:7 - Conformance Checklist

**CC-A3.1-1 (Method identity).** `U.Method` is one reusable way of doing under a stated concern, participant meanings, applicability, preconditions, intended result or preserved condition, and bounds. If the sentence also makes a claim about an actual participant, A.3.4 transformation, description, plan, dated Work occurrence, evidence relation, system-role assignment, capability, mechanism declaration, formal declaration, publication face, or pattern relation, write that claim under its direct pattern and state only the relation to the Method that actually obtains.

**CC-A3.1-2 (Semantic locality).** State the applicability, participant meanings, conditions, intended result, and bounds that distinguish the method. Add an effective reference scheme and local senses only when different meanings would change the identification. Add a claim scope, context slice, selected structure, or model-use relation only when its predicate obtains and changing that object would change the identification or the stated later decision.

**CC-A3.1-3 (Method-description membership and use).** When work, assurance, gate, or audit reliance depends on a method description, name the exact episteme and verify that it meets A.3.2 membership for this Method. If several epistemes are treated as descriptions of the same Method, their `EntityOfConcern` references must resolve to the same A.3.1 identity; compare their claim sets separately for the proposed use.

**CC-A3.1-4 (Assignment-free Method).** A Method may state local system-role-kind admission conditions or capability-fit conditions. These are Method-side admissibility conditions, not deontic obligations by default. The Method does not bind named people, teams, organizations, or calendar allocations.

**CC-A3.1-5 (Runtime-free method).** A dated run is a Work individual under `U.Work`, not a method field. Recover each exact actual performer and its obtaining system-role assignment through A.13; A.15.1 independently grounds the Work, enacted Method, extent, containing System, and every participation or resource relation used by the claim. Add F.6 attribution through that same assignment only when the receiving use expressly represents precise assignment-bound attribution. Telemetry, logs, measurements, evaluations, production, delivery, acceptance, and result records remain separate claims.

**CC-A3.1-6 (Plan-free method).** Work preparation, schedule, go or no-go date, work authorization, and planned work relation belong to `U.WorkPlan`, gate, authority, or commitment patterns.

**CC-A3.1-7 (Mechanism and formal-substrate separation).** A formal substrate, mathematical lens, mechanism declaration, realizer, or control model can constrain or help explain a method only through a relation with stated participants. Use `E.10.ARCH:3.1` to classify that neighboring claim. It does not identify the method until the reusable action, applicability, intended result, and boundary are stated.

**CC-A3.1-8 (Programming-paradigm neutrality).** Imperative, functional, logical, constraint, object-centric event, effect-handler, and hybrid forms remain descriptions or representations until the reusable way and its boundary are stated.

**CC-A3.1-9 (Graph and representation guard).** A graph path, path slice, query, predicate, table, dashboard, publication face, or pattern relation is not a method or work sequence by layout. Use `C.2.P.DR` when representation wording is overread as imperative action.

**CC-A3.1-10 (Method parts, structures, and Work parts).** Call a candidate a submethod only when its reusable action, preconditions, intended result or preserved condition, boundary, and relation to the whole method are stated. Otherwise keep the step, graph node, description fragment, Work part, episode, component behavior, or telemetry slice under its own pattern. A selected method-side `U.Structure` must have all four A.22 discriminators; layout and list membership establish none of them. Mathematical or graphical notation remains a description or C.29 representation.

**CC-A3.1-11 (Practice wording recovery).** For a source word such as *practice*, ask what the sentence lets the reader do: reuse a way, inspect a description, schedule or report Work, allocate a holder, classify a discipline or tradition, cite evidence, or merely quote a label. Choose the corresponding subject pattern only when that action is stated; otherwise retain an unresolved source cue.

**CC-A3.1-12 (Parameter and variant discipline).** Parameters may be method semantics or content of a `U.MethodDescription`. A `U.WorkPlan` may name planned values only against the declaration that gives those values their meaning. An actual value or participant requires an obtaining direct subject relation or A.6.1 application binding. Effects, bounds, participant meanings, applicability, and any semantic basis used by the comparison determine variant identity.

**CC-A3.1-13 (Evidence and assurance boundary).** A method or method description does not by itself prove that work happened, that a result is warranted for the claimed use, that a gate is passed, or that action is authorized. Those claims use the relevant evidence, assurance, gate, temporal, authority, work-plan, or work patterns.

