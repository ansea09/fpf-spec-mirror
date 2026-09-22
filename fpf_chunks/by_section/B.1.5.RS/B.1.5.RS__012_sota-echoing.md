---
chunk_kind: "child"
pattern_id: "B.1.5.RS"
pattern_title: "Replace a Constituent Method in Its Encompassing Uses"
section_id: "B.1.5.RS:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5.RS/B.1.5.RS__012_sota-echoing.md"
commit_sha: "acc387fc7a206495eabe07f1953849217f291715"
heading_path:
  - "B.1.5.RS — Replace a Constituent Method in Its Encompassing Uses"
  - "B.1.5.RS:11 — SoTA-Echoing"
line_start: 39620
line_end: 39629
dependencies:
  - "A.3.1"
  - "B.1.5"
  - "B.1.5.EW"
  - "B.1.5.RS"
  - "C.11.DUA"
  - "C.29"
keywords:
---

### B.1.5.RS:11 - SoTA-Echoing

[Mazo, Compton, Cohen and Ames](https://arxiv.org/html/2409.14902v1) formulate compositional contracts for layered control systems. Their contribution supports checking what adjacent functions assume and supply, including their different signal and timing models. This pattern uses that conditional-composition idea beyond the paper's system class; its formal guarantees are not generalized.

The stable-sort case illustrates contextual preservation by an elementary algorithmic counterexample. The bounded-estimate case applies ordinary interval reasoning. These are constructed cases of the common Method, not evidence that every constituent requires a formal contract or a numerical error bound.

For the practical question of substituting a constituent, a local performance benchmark is a serious alternative: it can reveal speed, cost and errors on its tested inputs. It does not establish that a replacement preserving totals also preserves arrival order, or that its error bound supports the required threshold decision. Sections 4.2–4.4 therefore select receiving-use conditions first, then derive or test only the preservation those uses need. The worked counterexample or an available bound can settle the stated question at less effort than an additional benchmark; an unresolved performance question can still justify a targeted trial.

Formal compositional contracts offer a stronger alternative where the constituent, interfaces and encompassing system fit their mathematical assumptions. The cited control theory makes those assumptions and guarantees explicit. This Method adapts that conditional comparison into ordinary statements of inputs, interactions, results and permitted losses; it keeps the formal proof when its additional assurance is useful and attainable. It does not treat every professional practice as a control-system instance. Reopen the selected comparison when an unmodeled interaction, shared realization, changed receiver or unsupported adaptation defeats the preservation claim. If one constituent cannot satisfy the relevant uses together, retain different variants or change the encompassing arrangement instead of declaring one universally better Method.

