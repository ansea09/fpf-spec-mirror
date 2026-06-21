---
chunk_kind: "child"
pattern_id: "B.5.3"
pattern_title: "Domain-Concept Bridge"
section_id: "B.5.3:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.3/B.5.3__005_solution.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "B.5.3 — Domain-Concept Bridge"
  - "B.5.3:4 — Solution"
line_start: 35829
line_end: 35846
dependencies:
  - "A.13"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.6.5"
  - "A.7"
  - "B.3.3"
  - "C.2.1"
  - "C.3"
  - "E.17"
  - "E.24.UK"
  - "F.1"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "bounded context"
  - "bridge scope"
  - "concept bridge"
  - "domain vocabulary"
  - "local sense"
  - "role assignment boundary"
---

### B.5.3:4 - **Solution**

Use a **Domain-Concept Bridge**. Start with the local word in its `U.BoundedContext`, then recover the FPF value that the project is actually using.

1. Establish the bounded context and local sense: use `F.1` to identify the domain family and authoritative sources, `F.2` to harvest terms with provenance, and `F.3` to cluster the local sense or SenseCell with counter-examples.
2. Ask what the local word is doing in the current claim: naming an entity, admitted U-kind, ontic slot filler, relation, characteristic coordinate, method, mechanism, work plan, performed work, role assignment, episteme, publication-use relation, evidence-use relation, or other governed value.
3. If the claim needs durable kindhood, use admission under `E.24.UK` and `C.3` and supply the ontic and slot relation that make the kind reviewable.
4. If the claim is only local vocabulary, keep it as a LocalSense or SenseCell and bridge it with scope and loss notes.
5. Use role vocabulary for system or holon role assignments in bounded work-facing contexts. Express meaning, status, evidence use, publication use, and domain interpretation through their own FPF values and relations.

The bridge record is therefore not an alias. It is a small typed settlement saying which FPF value the claim uses, what local wording points to it, where the bridge is admissible, and when the stronger source or direct governing pattern must be reopened.

Practical difference from an alias:

* An alias says "`L` is another name for `V`."
* A Domain-Concept Bridge says: in bounded context `K`, local wording `L` is being used for FPF value or relation `V` in the current claim; the bridge carries the constraints, units, role assignments, loss notes, and return conditions that make that use reviewable.
* If a component is called "sensor", the bridge can point to a system, a functional element, a measurement capability, a signal publication, or a role assignment. The claim decides which value is being used; the word "sensor" alone does not.

