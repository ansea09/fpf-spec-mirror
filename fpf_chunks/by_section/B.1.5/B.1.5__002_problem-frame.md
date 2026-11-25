---
chunk_kind: "child"
pattern_id: "B.1.5"
pattern_title: "Gamma_method - Order-Sensitive Method Composition and Work Enactment"
section_id: "B.1.5:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5/B.1.5__002_problem-frame.md"
commit_sha: "423f9d3fef92bafec7b092b910e8ce056a0f607d"
heading_path:
  - "B.1.5 — Gamma_method - Order-Sensitive Method Composition and Work Enactment"
  - "B.1.5:1 — Problem Frame"
line_start: 43965
line_end: 44010
dependencies:
  - "A.1"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.1"
  - "A.3.2"
  - "A.6.0"
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
  - "E.10"
  - "E.24"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.6"
  - "G.5"
  - "U.Signature"
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

Use this pattern when you need to decide whether identified Methods constitute one reusable Method, or to find which larger Methods, if any, include a known operation. Their contributions may depend on order, guards, joins, shared constraints or satisfying distinct requirements of the whole. If the recipient must devise the arrangement, begin with B.1.5.CM and use the qualification below on the resulting proposal.

Typical moments:

- a procedure, algorithm, or protocol has named steps or branches;
- changing the order of two candidate submethods changes the result or the admissible conditions of use;
- a diagram or code file looks like a method, but it may be only a method description, a work plan, a dated work trace, a selector registry, or a mathematical lens;
- a larger method must expose some interactions at its boundary while hiding internal steps;
- assurance needs to know which joins, adapters, cutsets, or exposed interfaces make the composite method reliable enough to enact.
- a source presents Methods as a first–then list even though representative Work may also require several of them to contribute at the same time.

**Primary EntityOfConcern.** When qualifying a proposed composition, take one candidate `U.Method` identified under A.3.1. Whether its part Methods and whole-forming facts qualify it as composite is a further claim. A C.2.1 episteme can carry that claim in its ClaimGraph with the candidate Method as its EntityOfConcern under the effective ReferenceScheme. An inquiry that starts with a known operation takes its search range from the question. Within that range it can identify several encompassing Methods or establish that none includes the operation.

**First useful move.** Establish whether the recipient wants to test a proposed composition, construct a way to obtain a whole result, or find which larger Methods include an operation already known. For construction use B.1.5.CM. For the upward inquiry start at §4.1 with the known operation and the uses whose rules matter. A step, plan item, dated action, diagram position or registry entry can lead to relevant evidence. Determine what it denotes before using it as a Method or a part of one.

**What goes wrong if missed.** A flowchart becomes the method, a plan item becomes a submethod, an event log becomes proof that a method was enacted, an order edge becomes a part, or a registry of alternatives is treated as one composed method. Then work starts from a description or label whose method identity, joins, interfaces, and failure conditions were never recovered.

**What this buys.** A practitioner can qualify a proposed composite Method or establish which of the larger Methods under consideration actually include an operation. A description, plan, identified structure or selector result can remain useful when the composition claim lacks grounds. Use `A.15.4` when the claim depends on appearances.

**Not this pattern when.**

- If the claim concerns one semantic way of doing and its composition is outside the question, use `A.3.1`.
- If the claim is a claim-bearing episteme that describes a method or relations among methods, use `A.3.2` and `C.2.1`.
- If the claim is intended work, use `A.15.2`.
- If the claim is a dated occurrence, use `A.15.1`.
- If the claim is structural component parthood, use `A.14`; use `C.13` for a needed construction account and `B.3.5` only when its additional assurance profile is elected.
- If the claim is only a method-family registry, selector, fallback relation, or useful organization of already identified methods without one whole-method construction, use `G.5` or select a `U.Structure` under `A.22`.

#### B.1.5:1.1 - Composition Question And Object Boundaries

`U.Method` is a non-agentive method holon kind. A method can have submethods and can participate as a submethod in a larger method. This does not mean every step-looking node, document section, file module, graph edge, work-plan item, or work occurrence is a method part.

For a proposed composition, ask:

```text
Given independently recovered U.Method parts,
which methodPartOf occurrences, whole-forming claims, and constraints qualify one already identified candidate as composite,
and what whole-level commitments let a practitioner identify, reidentify, and enact that method?
```

The whole method is not the diagram, code, schedule, event log, card, or work history that may describe, plan, record, or evidence it. Work enacts the method; the method does not perform work. An A.22-selected `U.Structure` may organize several methods and obtaining relations for one use without constructing another method.

`Gamma_method` names this method-composition discipline. Use the patterns above for related objects and B.1.6 for resource accounting.

