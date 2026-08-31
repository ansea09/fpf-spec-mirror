---
chunk_kind: "child"
pattern_id: "C.26"
pattern_title: "Quantum-Like Modeling Lens"
section_id: "C.26:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.26/C.26__012_sota-echoing.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "C.26 — Quantum-Like Modeling Lens"
  - "C.26:11 — SoTA-Echoing"
line_start: 54410
line_end: 54434
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

### C.26:11 - SoTA-Echoing

| Pattern claim | Practice source | Pattern implication |
| --- | --- | --- |
| Mathematical objects can be transferred as modeling lenses without claiming the target domain is made of the source-domain stuff. | Wigner on mathematical usefulness, Jaynes on probability as logic of science, and Khrennikov on quantum formalism outside physics. | Treat QL as a math-lens transfer card: explain the useful structure first, then state the inherited boundary. |
| Quantum-like is a mathematical or representational modeling lens, not a physical claim about the modeled system. | Basieva, Khrennikov, and Ozawa on quantum-like modeling in biology with open-system and instrument language. | Keep `QL-NQ` as non-entailment, not as the main claim; use detached mathematical modeling where state, probe, or export cue is real. |
| Linear quantum-like representation can make selected information-state processing more tractable if the representation and loss profile are declared. | Basieva-Khrennikov-Ozawa linearity / speed-up / stability arguments and finite-dimensional matrix-calculus discussions. | Support the state-representation coarsening card discipline; block blanket "quantum-like is faster" claims unless baseline cost, shortcut, loss, and reopen trigger are named. |
| Quantum probability is useful where inference is contextual, previous judgments change state, or possibilities interfere, but QL is not automatically the only formal route. | Quantum cognition work, quantum-instrument work, and process-theory cautions about classical instrument alternatives. | Use QL-lite as useful abstract modeling, not as proof of non-classical necessity. |
| DDD, microservice, active-inference, and measurement practice already supply ordinary FPF patterns. | DDD and microservice domain analysis, active-inference measurement-as-action work, performative prediction, metric-induced behavior. | Keep ordinary FPF patterns first; add QL only for the remaining state, probe, export, frame, or coarsening cue. |

#### C.26:11.1 - Selected operational source anchors

This section is intentionally short. It carries operational anchors for using the pattern, not an expanded bibliography.

| Claim | Source family | Practical implication |
| --- | --- | --- |
| Mathematical formalisms can be transferred as modeling lenses without claiming the target domain is made of the source-domain stuff. | [Wigner on mathematical usefulness](https://www.organism.earth/library/document/unreasonable-effectiveness-of-mathematics), [Jaynes on probability as logic](https://openlibrary.org/books/OL22584017M/PROBABILITY_THEORY_THE_LOGIC_OF_SCIENCE), and Khrennikov's quantum-like modeling line. | Treat QL as a math-lens transfer: name the useful structure, the ordinary FPF pattern, and the local stop before any claim requiring additional evidence or authority. |
| Quantum-like open-system and instrument formalisms can model state and probe interaction without physical quantum ontology. | [Basieva, Khrennikov, and Ozawa](https://www.sciencedirect.com/science/article/pii/S0303264720301994) and [arXiv](https://arxiv.org/abs/2010.15573), plus [Khrennikov on open systems](https://www.mdpi.com/1099-4300/25/6/886). | Keep `QL-NQ` central and use QL only where probe, instrument, open-information-system update rule, probe frame, export admissibility, or state export cue changes the admissible reading. |
| Question order, contextual judgment, and instrument-like operations are practical cues, but not automatic proof that QL is necessary. | [Quantum instruments for question-order effects](https://www.sciencedirect.com/science/article/pii/S0022249620301152), [Quantum Cognition](https://www.annualreviews.org/content/journals/10.1146/annurev-psych-033020-123501), and [process-theory non-exclusivity](https://arxiv.org/abs/2604.08604). | Use QL-lite when order/frame/probe effects change the result; keep classical instrument, Bayesian, causal, and ordinary measurement rivals live. |
| Same-content-looking measurements under different probe or measurement frames should not be silently treated as the same random variable or as jointly distributed. | [Contextuality-by-Default](https://www.sciencedirect.com/science/article/abs/pii/S0022249616300207). | Use C.26 only when the exact frames change variable identity, joint availability, or admissible comparison and a named obstruction survives ordinary measurement and Bridge patterns; otherwise keep those ordinary subject patterns. |
| Viability and active sensing often mix reading and acting, but ordinary control and measurement patterns remain primary. | [Free-energy and quantum-cognition link](https://www.frontiersin.org/articles/10.3389/fnbot.2022.910161/full), [physiological regulation and FEP](https://www.sciencedirect.com/science/article/pii/S0149763423004281), [active inference behavior](https://www.sciencedirect.com/science/article/pii/S0301051123002612), and [smart-building active inference](https://arxiv.org/abs/2503.18161). | For viability cases, name sensors, probes, actuators, and envelope variables first; retain QL only for remaining probe, frame, export, or coarsening cue. |
| Boundary and DDD-locality questions are already disciplined by ordinary architecture practice. | [Computational boundary of a self](https://philpapers.org/rec/LEVTCB-3), [Markov blankets of life](https://philarchive.org/rec/KIRTMB), [Azure domain analysis](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis), and [DDD 2025 SLR](https://www.sciencedirect.com/science/article/pii/S0164121225002055). | Apply direct boundary, local-sense, work, model-use, interface, and Bridge subject patterns first. If Markov-blanket wording is present, recover its exact claim and subject pattern; retain C.26 only where a named probe, order, comparison, export, or state-reading obstruction remains load-bearing. |
| Low-bit, tokenized, compressed, geometric, or neural representations may be useful shortcuts without being QL activation. | [1-bit LLMs](https://arxiv.org/abs/2402.17764), [implicit continuity in language models](https://arxiv.org/abs/2504.03933), [emergent quantumness in neural networks](https://arxiv.org/abs/2012.05082), and [covariant gradient descent](https://arxiv.org/abs/2504.05279). | Keep implementation substrate, geometry, compression, and representation shortcuts in ordinary FPF patterns unless a declared QL cue changes the admissible use. |
| Unknown alternatives and regime movement are search/generation problems, not QL claim authority. | [Open-endedness](https://arxiv.org/abs/2406.04268) and [quality-diversity through AI feedback](https://openreview.net/forum?id=owokKCrGYr). | Use QL only to mark a suspect frame; apply search or regime patterns to generation of alternatives. |

