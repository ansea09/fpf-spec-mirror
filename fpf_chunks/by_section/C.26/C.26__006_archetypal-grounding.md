---
chunk_kind: "child"
pattern_id: "C.26"
pattern_title: "Quantum-Like Modeling Lens"
section_id: "C.26:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.26/C.26__006_archetypal-grounding.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "C.26 — Quantum-Like Modeling Lens"
  - "C.26:5 — Archetypal Grounding"
line_start: 61177
line_end: 61215
dependencies:
  - "A.10"
  - "A.15"
  - "A.19"
  - "A.3"
  - "A.6"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.25"
  - "C.26.1"
  - "C.26.1-C.26.3"
  - "C.26.2"
  - "C.26.3"
  - "E.17"
  - "E.17.EFP"
  - "E.24.PUB"
  - "E.8"
  - "E.9"
  - "F.9"
keywords:
  - "QL-NQ"
  - "QL-lite"
  - "incompatible probes"
  - "instrument update"
  - "minimal admissible output"
  - "order effect"
  - "probe frame"
  - "quantum-like"
  - "source-loss coarsening"
  - "state export"
---

### C.26:5 - Archetypal Grounding

Tell: A reliability dashboard says "Ready" after a new readiness metric is published. Before publication, teams treated incidents as local triage. After publication, they change priorities to satisfy the metric, while unmeasured recovery work gets delayed.

Show, System side: the delivery system, teams, dashboard, incident-handling cycle, and release decision form one operational situation. The dashboard is not only a window; it is part of the work ecology because it changes attention, escalation, and behavior.

Show, Episteme side: the ordinary account uses C.16 and A.15 for the metric and changed work, A.10 for evidence use, and B.3 only if the release-assurance question is current. Its useful result is to treat the dashboard as evidence affected by publication and behavior, not as a passive readiness read. No surviving contextual-model obstruction is supplied, so this case returns without QL wording.

Second ordinary-pattern return: a large state-space model is too expensive for triage, so the team uses four typed operational states. Use the direct modeling and state-abstraction method to establish the retained distinctions, loss, bounded use, and reopen trigger. Mere reduction to four states does not activate C.26; a named residual contextual-model obstruction would be a separate premise.

#### C.26:5.1 - Matching local distributions can still block a joint model

In this constructed mathematical example, a modeler wants to export three specified pair-measurement distributions as one probability distribution over binary variables A, B and C. Only the pair measurements AB, BC and AC are available in the stipulated model. The proposed export requires each repeated variable to have one shared meaning and value across its two pair accounts; this is an explicit assumption of the comparison, not an inference from a repeated label.

The following probabilities are stipulated model inputs, not observed frequencies:

| Pair | 00 | 01 | 10 | 11 |
| --- | ---: | ---: | ---: | ---: |
| AB | 1/8 | 3/8 | 3/8 | 1/8 |
| BC | 1/8 | 3/8 | 3/8 | 1/8 |
| AC | 1/8 | 3/8 | 3/8 | 1/8 |

Each row sums to one. Each variable has probability 1/2 of either value in both accounts where it appears. Every local outcome is possible, so checking only allowed assignments leaves all eight binary triples available. These local checks do not establish a joint probability law.

Use C.29 for the declared mathematical correspondence and C.29.1 for the proposed transfer: projecting the joint distribution onto each pair must recover that row. The missing comparison is whether any such joint distribution exists. This is the probabilistic global-section question in [Abramsky and Brandenburger, §§2.4–3 and 4.3](https://arxiv.org/pdf/1102.0264). A measurement or cross-context meaning claim would separately need its C.16 or F.9 basis.

**Derive the obstruction.** For one binary triple, let D count unequal pairs. If all three values agree, D = 0; otherwise one differs from the other two and D = 2. Every probability distribution on triples therefore has E[D] ≤ 2. The supplied pair accounts instead require

    E[D] = P(A != B) + P(B != C) + P(A != C)
         = 3/4 + 3/4 + 3/4 = 9/4.

Thus no nonnegative joint probability distribution reproduces all three rows under the stated identification. This is a probabilistic no-global-section result; it does not say that no individual triple is locally possible.

**Use the result.** Keep the pair accounts separate and reject the proposed joint export. A statistic needing that joint law remains unsupported. Changing the pair laws, the shared-variable assumption or the requested statistic reopens the comparison; adding a joint table without that change cannot repair it. The construction establishes no observed probe effect, physical quantum realization or empirical adequacy.

**Compare an unobstructed case.** Give each of the six nonconstant triples probability 1/6 and give 000 and 111 probability zero. Every pair then has probabilities (1/6, 1/3, 1/3, 1/6). These revised local laws have the displayed joint model. Pairwise availability alone therefore does not activate C.26.

The first useful result here is the exact obstruction to the live joint-export proposal. Ordinary probability theory or C.29.1 can supply the same argument; use an already adequate argument directly without an extra QL note. The C.26 contribution is this named contextual-model comparison, not a claim that QL is the only or faster way to compute it.

