---
chunk_kind: "child"
pattern_id: "C.26"
pattern_title: "Quantum-Like Modeling Lens"
section_id: "C.26:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.26/C.26__012_sota-echoing.md"
commit_sha: "e307edbd91c04c1d85661bd309b9944fac251937"
heading_path:
  - "C.26 — Quantum-Like Modeling Lens"
  - "C.26:11 — SoTA-Echoing"
line_start: 65936
line_end: 65960
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
| Quantum-like is a mathematical or representational modeling lens, not a physical claim about the modeled system. | Basieva, Khrennikov, and Ozawa on quantum-like modeling in biology with open-system and instrument language. | Retain the distinction between a mathematical representation and a separate physical claim; apply the :4 test to the proposed QL use. |
| Linear information-state dynamics can simplify a selected representation; that mathematical form alone supplies no general computational-speed or empirical-stability comparison. | Basieva, Khrennikov and Ozawa, §8.4, discuss linearity, compression and stabilization in their proposed biological information-state account. | Specify the represented dynamics and establish the mathematical property being used. When a computational-cost or empirical-performance advantage is claimed, supply its comparison under the receiving model using :4.5. |
| Quantum probability is useful where inference is contextual, previous judgments change state, or possibilities interfere, but QL is not automatically the only formal route. | Quantum cognition work, quantum-instrument work, and process-theory cautions about classical instrument alternatives. | Test the specified contextual-model question and compare adequate ordinary alternatives where the receiving use requires it. |
| DDD, microservice, active-inference and measurement accounts can already answer the ordinary subject question. | Domain analysis, measurement-as-action and performative-prediction accounts. | Reuse a sufficient account; retain QL only for a further named contextual-model obstruction. |

#### C.26:11.1 - Selected operational source anchors

The following anchors support the pattern's operational modeling moves.

| Claim | Source family | Practical implication |
| --- | --- | --- |
| Mathematical formalisms can be transferred as modeling lenses without claiming the target domain is made of the source-domain stuff. | [Wigner on mathematical usefulness](https://www.organism.earth/library/document/unreasonable-effectiveness-of-mathematics), [Jaynes on probability as logic](https://openlibrary.org/books/OL22584017M/PROBABILITY_THEORY_THE_LOGIC_OF_SCIENCE), and Khrennikov's quantum-like modeling line. | Treat QL as a math-lens transfer: name the useful structure, the ordinary FPF pattern, and the local stop before any claim requiring additional evidence or authority. |
| Quantum-like open-system and instrument formalisms can model state and probe interaction without physical quantum ontology. | [Basieva, Khrennikov, and Ozawa](https://www.sciencedirect.com/science/article/pii/S0303264720301994) and [arXiv](https://arxiv.org/abs/2010.15573), plus [Khrennikov on open systems](https://www.mdpi.com/1099-4300/25/6/886). | Use the source's instrument or open-system construction when it supplies the needed mathematical contribution under :4; retain `QL-NQ`. |
| Question order, contextual judgment, and instrument-like operations are practical cues, but not automatic proof that QL is necessary. | [Quantum instruments for question-order effects](https://www.sciencedirect.com/science/article/pii/S0022249620301152), [Quantum Cognition](https://www.annualreviews.org/content/journals/10.1146/annurev-psych-033020-123501), and [process-theory non-exclusivity](https://arxiv.org/abs/2604.08604). | Use order or frame effects to locate the question, then establish the specific obstruction and consequence; retain adequate classical instrument, Bayesian, causal or measurement accounts. |
| Same-content-looking measurements under different probe or measurement frames should not be silently treated as the same random variable or as jointly distributed. | [Contextuality-by-Default](https://www.sciencedirect.com/science/article/abs/pii/S0022249616300207). | Use C.26 only when the exact frames change variable identity, joint availability, or admissible comparison and a named obstruction survives ordinary measurement and Bridge patterns; otherwise keep those ordinary subject patterns. |
| Viability and active sensing often mix reading and acting, but ordinary control and measurement patterns remain primary. | [Free-energy and quantum-cognition link](https://www.frontiersin.org/articles/10.3389/fnbot.2022.910161/full), [physiological regulation and FEP](https://www.sciencedirect.com/science/article/pii/S0149763423004281), [active inference behavior](https://www.sciencedirect.com/science/article/pii/S0301051123002612), and [smart-building active inference](https://arxiv.org/abs/2503.18161). | Recover the envelope and observation/action account first; retain QL only for a further named contextual-model obstruction. |
| Boundary and DDD-locality questions are already disciplined by ordinary architecture practice. | [Computational boundary of a self](https://philpapers.org/rec/LEVTCB-3), [Markov blankets of life](https://philarchive.org/rec/KIRTMB), [Azure domain analysis](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis), and [DDD 2025 SLR](https://www.sciencedirect.com/science/article/pii/S0164121225002055). | Apply direct boundary, local-sense, work, model-use, interface, and Bridge subject patterns first. If Markov-blanket wording is present, recover its exact claim and subject pattern; retain C.26 only where a named probe, order, comparison, export, or state-reading obstruction remains load-bearing. |
| Low-bit, tokenized, compressed, geometric, or neural representations may be useful shortcuts without being QL activation. | [1-bit LLMs](https://arxiv.org/abs/2402.17764), [implicit continuity in language models](https://arxiv.org/abs/2504.03933), [emergent quantumness in neural networks](https://arxiv.org/abs/2012.05082), and [covariant gradient descent](https://arxiv.org/abs/2504.05279). | Keep the actual geometry, compression and implementation claim under its subject account; QL additionally needs the :4 result. |
| Unknown alternatives and regime movement are search/generation problems, not QL claim authority. | [Open-endedness](https://arxiv.org/abs/2406.04268) and [quality-diversity through AI feedback](https://openreview.net/forum?id=owokKCrGYr). | Use search or regime methods to construct alternatives; a suspect frame alone does not establish a QL contribution. |

