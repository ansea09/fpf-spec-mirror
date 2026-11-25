---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Specify Order-Sensitive or Temporal Aggregation (Γ_ctx, Γ_time)"
section_id: "B.1.4:4"
section_title: "Admissible Checks"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__007_admissible-checks.md"
commit_sha: "423f9d3fef92bafec7b092b910e8ce056a0f607d"
heading_path:
  - "B.1.4 — Specify Order-Sensitive or Temporal Aggregation (Γ_ctx, Γ_time)"
  - "B.1.4:4 — Admissible Checks"
line_start: 43845
line_end: 43882
dependencies:
  - "A.1.1"
  - "A.14"
  - "A.15.1"
  - "A.15.2"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "B.1"
  - "B.1.6"
  - "B.2"
  - "B.2.P"
  - "C.13"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "E.18"
  - "E.18.2"
keywords:
---

### B.1.4:4 - Admissible Checks

For a contextual order rule, specify how a user will select the positions and their relations. For a claim about a particular aggregate, apply that rule to the corresponding values:

- the ordering relations are specified and, for a particular aggregate, the relations used are identified by value;
- the `OrderSpec` is declared as total order, partial order, or another named relation;
- independence, branch, or join conditions are named when parallel factors are used;
- the claim identifies its included inputs, combining rule, result or result specification, ClaimScope when needed, and admissible use; any holon-boundary crossing it uses has its relation basis;
- method, method-description, work, transformation, and resource claims use the patterns that define or test them.

For a temporal rule, establish how its user can determine the bearers, intervals and relevant window. To assess an actual aggregate, apply the rule to the available evidence:

- the rule states which intervals and bearers or occurrences qualify, or a particular application identifies them; a proper-phase claim additionally preserves one carrier's identity under its rule;
- a reference and any conversion make the times comparable, and the rule for selecting the window or its actual bounds are available as the claim requires;
- the selected combining rule and coverage/overlap policy hold; handle allowed overlaps and gaps as that rule requires, or narrow the use;
- a changed identity is represented as a distinct input when appropriate, rather than hidden as another phase of the same carrier;
- work-resource claims use `B.1.6`; positive temporal-aspect claims use `C.27.TA`, while a separate temporal-claim adequacy question uses `C.27`. Currentness uses `G.11`, and `A.10` recovers provenance and bounded reliance when needed.

**B.1 invariant carry-through.** Apply an algebraic law only when the recovered relation and selected operator justify it. A unique computed contextual result requires the operation, permitted order and join or independence conditions to determine that result. Before promising an execution or its result, establish that the applicable constraints admit an execution. When admissible orders give different values, check the requested conclusion across them. A bound on all returned values can establish a condition on those values. For a promise to deliver the result by a deadline, also establish timely completion under the choices the promise covers, using a feasible decision rule if those choices are entrusted to the performer. To refute a guarantee with an adverse order, establish that the order can occur. For an exact value, retain the supported alternatives or establish the additional ordering or selection that determines it. An order structure can be a sufficient aggregate without asserting a unique execution outcome.

Temporal aggregation follows its selected rule, temporal reference, coverage and overlap policy; one-carrier continuity is additionally required by the proper-phase profile.

A repeated designation creates no additional occurrence or relation by itself; retain distinct occurrences and ordered positions when the claim distinguishes them. State any singleton or idempotence law for the operator.

Weakest-link and monotonicity claims name the characteristic and model being bounded or improved; an aggregation record alone establishes no performance, safety or assurance result.

#### B.1.4:4.1 - Aggregation obligations

| Obligation | What must be named | Why it matters |
| --- | --- | --- |
| Independence and joins | Specify how to establish the relations and joins that allow branches to be combined. For an actual aggregate, identify those used. | Prevents an ordered aggregate from treating dependent branches as independent evidence or work. |
| Order specification | Total order, partial order, precedence relation, or another named relation over the selected positions. | Keeps order-sensitive claims from being read as unordered collection claims. |
| Decisive dependency relation | For a weakest-link claim, name the relation that makes one position, delay or missing step decisive for the aggregate use. | Keeps that claim dependent on its model and relation. |
| Bearer identity and phase continuity | State how the rule identifies a temporal input's bearer. For an actual aggregate identify the bearers included. For the proper-phase profile, state which carrier remains the same and under which identity rule. | Keeps separate occurrences distinguishable and prevents a phase account from hiding identity change. |
| Temporal coverage | State how to choose a common reference and window, identify intervals or phases, and combine them for coverage and overlap. Use the values for the period concerned when reporting its coverage. | Distinguishes covered time from elapsed span and exposes how gaps and overlaps affect the result. |
| Chronological discipline | State whether the claim uses chronological, logical, publication or performed-work order, and the correspondence needed when more than one is used. | Keeps a document sequence, argument sequence and work occurrence sequence from substituting for one another. |
| Monotone characteristic | For a monotonicity claim, name the characteristic, comparison and model under which adding inputs preserves or improves the result. | Blocks generic monotonicity claims over an unspecified aggregate. |

