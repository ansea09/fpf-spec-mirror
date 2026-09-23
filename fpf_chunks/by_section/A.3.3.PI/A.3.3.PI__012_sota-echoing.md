---
chunk_kind: "child"
pattern_id: "A.3.3.PI"
pattern_title: "Retain the Information Needed for Prediction"
section_id: "A.3.3.PI:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3.PI/A.3.3.PI__012_sota-echoing.md"
commit_sha: "21296c8aaf3611b63ee6a2bb11e439e828ffb9a3"
heading_path:
  - "A.3.3.PI — Retain the Information Needed for Prediction"
  - "A.3.3.PI:11 — SoTA-Echoing"
line_start: 10312
line_end: 10327
dependencies:
  - "A.3.3"
  - "A.3.3.CC"
  - "A.3.3.TR"
  - "B.5.FM"
  - "B.5.MPC.R"
  - "C.11.DUA"
  - "C.16"
  - "C.29.1"
keywords:
---

### A.3.3.PI:11 - SoTA-Echoing

The working question is to obtain a useful future result from the available observations and change law. **Selected approach:** retain the distinctions needed by that result, together with their update or uncertainty. **Serious alternative:** reconstruct and carry the full model state. Full-state recovery supports a broader range of subsequent questions and is convenient when those values are already available. It can require extra measurement, estimation or storage when only an aggregate is observed.

Compare the alternatives for the same law, observations, inputs, horizon and decision, including the preparation needed to use each. In :5.1, a one-total upper bound already settles the 0.6 kg limit; reconstructing composition would require information that cannot improve that decision. For a unique forecast, two available totals support a rolling recurrence. In :5.2, a distribution over hidden states supports the history-dependent forecast without identifying the actual hidden state. That filter costs more than retaining the current readout alone, whose merged histories lose the decision-changing probability. These are chosen information and computation trade-offs, derived in the cases rather than measured as a general efficiency gain.

**Reduction and memory.** Lin and Lu's [Data-driven model reduction, Wiener projections, and the Koopman-Mori-Zwanzig formalism, §§2.1-2.3](https://arxiv.org/html/1908.07725v5) separates forecasting from long-time statistics and exposes memory after projection. **Adapt:** :4.1-:4.3 fix the output and horizon, compare merged states, and choose retained state, history or uncertainty. The projection identity needs a closure construction to become an economical predictor; the elementary mixture and its bounds in :5.1 are authored.

**Filtering a hidden state.** Poole and Mackworth's [Artificial Intelligence: Foundations of Computational Agents, third edition, §§9.6.2-9.6.3](https://artint.info/3e/html/ArtInt3e.Ch9.S6.html) derives filtering under Markov transition and observation assumptions. **Adopt:** :4.4 and :5.2 propagate state weights, incorporate the observation likelihood and normalize. [Section 9.1.1](https://artint.info/3e/html/ArtInt3e.Ch9.S1.html) distinguishes probability masses and densities; :4.4 keeps that distinction for discrete and continuous readouts. The resulting distribution summarizes the history for the supplied model. Learning the model or approximating a larger state space requires further Methods.

**Finite-chain forecasts and averages.** [Cambridge's Markov Chains notes, §§9-10](https://www.statslab.cam.ac.uk/~rrw1/markov/M.pdf) distinguish distribution convergence and ergodic averages. **Adopt:** :4.5 and :5.2 preserve their different questions. The three-state matrix, histories and threshold comparison are authored. Stationary initial weights are used only where stated; the positive finite chain supports the illustrated long-run average.

**Prediction at the intended horizon.** De Jong, Breschi, Schoukens and Lazar's [Koopman Data-Driven Predictive Control with Robust Stability and Recursive Feasibility Guarantees](https://arxiv.org/html/2405.01292v1) constructs multi-step predictors from past inputs and outputs and addresses errors from iterated approximate one-step dynamics. **Adapt:** :4.4-:4.5 compare the predictor at its intended horizon and input policy. The paper's controller guarantees require its specialized construction; the present Method adopts the comparison question, not those guarantees for every predictor.

The common procedure is a conceptual synthesis. Reopen its comparative choice when another description or estimator answers the same question under the same available observations, reader preparation and acceptable error at lower cost, or when a changed law, input policy or consequential prediction failure exposes a distinction it lost. Delay reconstruction, observability, filtering, system identification and model reduction then supply concrete alternative constructions.

