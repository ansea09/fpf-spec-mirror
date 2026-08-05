---
chunk_kind: "child"
pattern_id: "B.1.5"
pattern_title: "Gamma_method - Order-Sensitive Method Composition and Work Enactment"
section_id: "B.1.5:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5/B.1.5__002_problem-frame.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "B.1.5 — Gamma_method - Order-Sensitive Method Composition and Work Enactment"
  - "B.1.5:1 — Problem Frame"
line_start: 36393
line_end: 36437
dependencies:
  - "A.1"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.6.0"
  - "A.6.1"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.1"
  - "B.1.4"
  - "B.1.5"
  - "B.1.6"
  - "B.2"
  - "B.3"
  - "C.13"
  - "C.2.1"
  - "C.29"
  - "E.10"
  - "E.20"
  - "E.24"
  - "E.24.PUB"
  - "E.24.UK"
  - "G.5"
  - "U.MethodDescription"
  - "U.PresentationCarrier"
  - "U.Signature"
  - "U.Structure"
  - "U.Work"
keywords:
  - "A.6.RCD claim disposition"
  - "assurance hooks"
  - "capability continuity"
  - "composite-Method boundary account"
  - "method composition"
  - "method relation structure"
  - "method/work granularity"
  - "methodPartOf"
  - "order-sensitive method"
  - "submethod"
  - "typed join"
  - "work enactment"
---

### B.1.5:1 - Problem Frame

Use this pattern when a project must decide whether several recovered methods compose into one larger `U.Method`, and when order, guarded choice, parallel branches, typed joins, adapters, or method-interface exposure changes the identity of that whole method.

Typical moments:

- a procedure, workflow, algorithm, pipeline, proof route, clinical protocol, manufacturing recipe, inference pipeline, or operational playbook has named steps or branches;
- changing the order of two candidate submethods changes the result or the admissible conditions of use;
- a diagram or code file looks like a method, but it may be only a method description, a work plan, a dated work trace, a selector registry, or a mathematical lens;
- a larger method must expose some interactions at its boundary while hiding internal steps;
- assurance needs to know which joins, adapters, cutsets, or exposed interfaces make the composite method reliable enough to enact.

**Primary EntityOfConcern.** The EntityOfConcern is one exact candidate or composite `U.Method`, already identified under A.3.1. The proposition that exact part Methods and whole-forming facts qualify it as composite is separately governed claim content. A separately identified C.2.1 episteme may carry that proposition in its ClaimGraph; the episteme then has the exact candidate Method as its EntityOfConcern under its effective ReferenceScheme. The proposition does not become the episteme.

**First useful move.** For each apparent step or branch, recover the governed object before composing anything: `U.Method`, `U.MethodDescription`, `U.WorkPlan`, dated `U.Work`, an A.22-selected `U.Structure`, method-family registry or selector outcome, mathematical lens, mechanism, formal substrate, or quoted wording that does not yet carry a method claim.

**What goes wrong if missed.** A flowchart becomes the method, a plan item becomes a submethod, an event log becomes proof that a method was enacted, an order edge becomes a part, or a registry of alternatives is treated as one composed method. Then work starts from a description or label whose method identity, joins, interfaces, and failure conditions were never recovered.

**What this buys.** The project can test whether an already identified candidate `U.Method` is composite and can state the needed part, order, join, interface, and identity facts without turning every useful sentence into a relation kind. If that qualification fails, the project still has a useful lower object: an A.22-selected `U.Structure`, description, plan, work occurrence, lens, selector result, or `A.15.4` appearance-based reliance repair request.

**Not this pattern when.**

- If the current claim is one semantic way of doing with no order-sensitive composition question, use `A.3.1`.
- If the current claim is a claim-bearing episteme that describes a method or relations among methods, use `A.3.2` and `C.2.1`.
- If the current claim is intended work, use `A.15.2`.
- If the current claim is a dated occurrence, use `A.15.1`.
- If the current claim is structural component parthood, use `A.14`, `C.13`, and `B.3.5`.
- If the current claim is only a method-family registry, selector, fallback relation, or useful organization of already identified methods without one whole-method construction, use `G.5` or select a `U.Structure` under `A.22`.

#### B.1.5:1.1 - Composition Question And Object Boundaries

`U.Method` is a non-agentive method holon kind. A method can have submethods and can participate as a submethod in a larger method. This does not mean every step-looking node, document section, file module, graph edge, work-plan item, or work occurrence is a method part.

Order-sensitive method composition is a narrow constructive question:

```text
Given independently recovered U.Method parts,
which methodPartOf occurrences, exact whole-forming claims, and constraints qualify one already identified candidate as composite,
and what whole-level commitments let a practitioner identify, reidentify, and enact that method?
```

The whole method is not the diagram, code, schedule, event log, card, or work history that may describe, plan, record, or evidence it. Work enacts the method; the method does not perform work. An A.22-selected `U.Structure` may organize several methods and obtaining relations for one use without constructing another method.

`Gamma_method` is the name for this method-composition discipline. It is not a new root U-kind, not a workflow notation, not a generic container, not a resource-accounting operator, and not a substitute for `U.Work`.

