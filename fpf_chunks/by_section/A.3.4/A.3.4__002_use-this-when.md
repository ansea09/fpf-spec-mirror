---
chunk_kind: "child"
pattern_id: "A.3.4"
pattern_title: "U.Transformation: Actual Bounded Change Under Conditions"
section_id: "A.3.4:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.4/A.3.4__002_use-this-when.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "A.3.4 — U.Transformation: Actual Bounded Change Under Conditions"
  - "A.3.4:0 — Use This When"
line_start: 12863
line_end: 12885
dependencies:
  - "A.1"
  - "A.10"
  - "A.11"
  - "A.14"
  - "A.15.1"
  - "A.15.2"
  - "A.15.PROD"
  - "A.22"
  - "A.3"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "A.6.1"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.7"
  - "B.2"
  - "B.3"
  - "C.13"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "C.32.P2S"
  - "E.18"
  - "E.18.1"
  - "E.24"
  - "E.24.UK"
  - "F.18"
  - "G.11"
keywords:
  - "actual bounded change"
  - "actual subject facts"
  - "changed referent"
  - "continuity and reidentification"
  - "occurrence boundary"
  - "transformation composition"
---

### A.3.4:0 - Use This When

Use this pattern when a project must decide whether an actual change occurred and identify that one change. Ask: what continuing subject changed, where the change begins and ends, which facts differ before, during, and after it, and what rule makes this one occurrence rather than unrelated observations.

**First useful move.** Name the continuing subject and where the change begins and ends. Write the subject facts that hold before, during, and after that boundary, then state the boundary conditions and the continuity or reidentification rule that make this one occurrence. A desired state, method, plan or model alone leaves occurrence unresolved. Use records or observations for the actual facts they support.

Missing information about a neighboring claim leaves that claim unresolved; it neither disproves nor establishes the transformation.

**Practical gain.** Identify one actual change without first deciding whether finer changes are its parts. If no composition or holon claim is needed, continue with the neighboring-object guidance at `4.3`. A positive composition claim requires the additional basis in `4.2.1`; A.1 applies only after the proposed whole and its construction facts are independently supplied.

**Not this pattern when.**

- If the issue is only a semantic way of doing, use `A.3.1`.
- If the issue is a description of that way, use `A.3.2`.
- If the issue is a state-space and transition-law episteme, use `A.3.3`.
- If the issue is a law-governed operation algebra with admissibility predicates, use `A.6.1` and `E.20`.
- If the issue is planned or dated work, use `A.15.2` or `A.15.1`.
- If the issue is the selected compound transformation-flow structure, its locus, path, path slice, crossing, or flow valuation, use `E.18`.
- If the issue is a graph, algebra, category, tuple, morphism, quotient, fold, refinement, factorization, or wiring expression used to describe that structure mathematically, use `E.18.2` and `C.29`.
- If the issue is a positive temporal aspect of an object or claim, use `C.27.TA`.
- If the issue is adequacy or admissible use of a temporal claim, use `C.27`.
- If the issue is holon recognition without a current actual-change identity or constructive transformation-parthood claim, use `A.1`.

