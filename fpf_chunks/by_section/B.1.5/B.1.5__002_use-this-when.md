---
chunk_kind: "child"
pattern_id: "B.1.5"
pattern_title: "Gamma_method - Order-Sensitive Method Composition and Work Enactment"
section_id: "B.1.5:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5/B.1.5__002_use-this-when.md"
commit_sha: "44dd88188a07646ef23aca32627a3f670525853f"
heading_path:
  - "B.1.5 — Gamma_method - Order-Sensitive Method Composition and Work Enactment"
  - "B.1.5:0 — Use This When"
line_start: 33152
line_end: 33180
dependencies:
  - "A.1"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.3.1"
  - "A.3.2"
  - "A.6.0"
  - "A.6.1"
  - "B.1"
  - "B.1.4"
  - "B.1.6"
  - "B.2"
  - "B.3"
  - "B.3.5"
  - "C.13"
  - "C.29"
  - "E.10"
  - "E.20"
  - "G.5"
  - "U.Method"
  - "U.MethodDescription"
keywords:
  - "MIC"
  - "assurance hooks"
  - "capability continuity"
  - "method composition"
  - "method relation structure"
  - "method/work granularity"
  - "order-sensitive method"
  - "submethod"
  - "typed join"
  - "work enactment"
---

### B.1.5:0 - Use This When

Use this pattern when a project must decide whether several recovered methods compose into one larger `U.Method`, and when order, guarded choice, parallel branches, typed joins, adapters, or method-interface exposure changes the identity of that whole method.

Typical moments:

- a procedure, workflow, algorithm, pipeline, proof route, clinical protocol, manufacturing recipe, inference pipeline, or operational playbook has named steps or branches;
- changing the order of two candidate submethods changes the result or the admissible conditions of use;
- a diagram or code file looks like a method, but it may be only a method description, a work plan, a dated work trace, a selector registry, or a mathematical lens;
- a larger method must expose some interactions at its boundary while hiding internal steps;
- assurance needs to know which joins, adapters, cutsets, or exposed interfaces make the composite method reliable enough to enact.

**Primary EntityOfConcern.** The EntityOfConcern is an order-sensitive method-composition claim: a claim that recovered `U.Method` values form one composite `U.Method` under a bounded context.

**First useful move.** For each apparent step or branch, recover the governed object before composing anything: `U.Method`, `U.MethodDescription`, `U.WorkPlan`, dated `U.Work`, `MethodRelationStructure@BoundedContext`, method-family registry or selector outcome, mathematical lens, mechanism, formal substrate, or quoted wording that does not yet carry a method claim.

**What goes wrong if missed.** A flowchart becomes the method, a plan item becomes a submethod, an event log becomes proof that a method was enacted, an order edge becomes a part, or a registry of alternatives is treated as one composed method. Then work starts from a description or label whose method identity, joins, interfaces, and failure conditions were never recovered.

**What this buys.** The project can admit a composite `U.Method` only when method parts, whole-forming relations, whole identity, interface exposure, assurance hooks, and enactment boundary are explicit. If that threshold is not met, the project still has a useful lower object: a selected method relation structure, description, plan, work record, lens, or `A.15.4` appearance-based reliance repair request.

**Not this pattern when.**

- If the current claim is one semantic way of doing with no order-sensitive composition question, use `A.3.1`.
- If the current claim is a representation that describes a method or method relation structure, use `A.3.2`.
- If the current claim is intended work, use `A.15.2`.
- If the current claim is a dated occurrence, use `A.15.1`.
- If the current claim is structural component parthood, use `A.14`, `C.13`, and `B.3.5`.
- If the current claim is only a method-family registry, selector, fallback relation, or alternative set without one whole-method assembly, use `G.5` or `MethodRelationStructure@BoundedContext`.

