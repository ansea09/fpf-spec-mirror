---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Specify Order-Sensitive or Temporal Aggregation (Γ_ctx, Γ_time)"
section_id: "B.1.4:4"
section_title: "Admissible Checks"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__007_admissible-checks.md"
commit_sha: "d8dd955fddb923b5b946d2c5865d0665cff5a67e"
heading_path:
  - "B.1.4 — Specify Order-Sensitive or Temporal Aggregation (Γ_ctx, Γ_time)"
  - "B.1.4:4 — Admissible Checks"
line_start: 42055
line_end: 42086
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

For contextual order aggregation:

- the ordered relation refs are named by value;
- the `OrderSpec` is declared as total order, partial order, or another named relation;
- independence, branch, or join conditions are named when parallel factors are used;
- the claim identifies its included inputs, combining rule, result or result specification, ClaimScope when needed, and admissible use; any holon-boundary crossing it uses has its exact relation basis;
- method, method-description, work, transformation, and resource claims use the patterns that define or test them.

For temporal aggregation:

- each input interval and its bearer or occurrence are identified; a proper-phase claim additionally preserves the one carrier's identity under its direct rule;
- the temporal reference, any required conversion and the selected time window are established;
- the selected combining rule and coverage/overlap policy hold; handle allowed overlaps and gaps as that rule requires, or narrow the use;
- a changed identity is represented as a distinct input when appropriate, rather than hidden as another phase of the same carrier;
- work-resource claims use `B.1.6`; positive temporal-aspect claims use `C.27.TA`, while a separate temporal-claim adequacy question uses `C.27`. Currentness uses `G.11`, and `A.10` recovers provenance and bounded reliance when needed.

**B.1 invariant carry-through.** Apply an algebraic law only when the recovered relation and selected operator justify it. A unique computed contextual result requires the operation, permitted order and actual join or independence conditions to determine that result. If admissible orders give different outcomes, retain the supported alternatives or establish the additional ordering or selection needed by the use. An order structure can itself be a sufficient aggregate without asserting a unique execution outcome. Temporal aggregation follows its selected rule, temporal reference, coverage and overlap policy; one-carrier continuity is additionally required by the proper-phase profile. A repeated designation creates no additional occurrence or relation by itself; retain distinct occurrences and ordered positions when the claim distinguishes them. State any singleton or idempotence law for the actual operator. Weakest-link and monotonicity claims name the characteristic and model being bounded or improved; an aggregation record alone establishes no performance, safety or assurance result.

#### B.1.4:4.1 - Compact Obligation Rows

| Obligation | What must be named | Why it matters |
| --- | --- | --- |
| Independence and joins | For branches used in the aggregate, name their relation refs, any join refs and the actual condition under which they may be combined. | Prevents an ordered aggregate from silently treating dependent branches as independent evidence or work. |
| Order specification | Total order, partial order, precedence relation, or another named relation over the selected positions. | Keeps order-sensitive claims from being read as unordered collection claims. |
| Decisive dependency relation | For a weakest-link claim, name the relation that makes one position, delay or missing step decisive for the aggregate use. | Keeps that claim dependent on its actual model and relation. |
| Bearer identity and phase continuity | Identify each temporal input's bearer. For the proper-phase profile, state which carrier remains the same and under which identity rule. | Keeps separate occurrences distinguishable and prevents a phase account from hiding identity change. |
| Temporal coverage | Temporal reference, time window, exact intervals or phase refs, combining rule and coverage/overlap policy. | Distinguishes covered time from elapsed span and exposes how gaps and overlaps affect the result. |
| Chronological discipline | State whether the claim uses chronological, logical, publication or performed-work order, and the correspondence needed when more than one is used. | Keeps a document sequence, argument sequence and work occurrence sequence from substituting for one another. |
| Monotone characteristic | For a monotonicity claim, name the exact characteristic, comparison and model under which adding inputs preserves or improves the result. | Blocks generic monotonicity claims over an unspecified aggregate. |

