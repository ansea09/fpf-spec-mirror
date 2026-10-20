---
chunk_kind: "child"
pattern_id: "C.42"
pattern_title: "Reduce Avoidable Work While Preserving the Needed Result"
section_id: "C.42:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.42/C.42__012_sota-echoing.md"
commit_sha: "22984da9ba607842cd2bb4ec8e5201d4f225b69f"
heading_path:
  - "C.42 — Reduce Avoidable Work While Preserving the Needed Result"
  - "C.42:11 — SoTA-Echoing"
line_start: 89583
line_end: 89594
dependencies:
  - "A.11.OP"
  - "A.3.1.MI"
  - "C.11.CRC"
  - "C.11.DUA"
  - "C.28.CM"
  - "C.39"
keywords:
---

### C.42:11 - SoTA-Echoing

**Practice question and selected line.** How can a practitioner reduce avoidable work while preserving the actual result and conditions over the relevant horizon? The selected answer is the conditional synthesis in section 4: purpose and use, diagnosis, intervention construction, complete comparison, introduction and later reconsideration. It is a method proposal grounded in the comparisons below, not an empirical claim of universal superiority.

**Toil reduction is a serious mature alternative.** Google's 2018 SRE treatment already compares elimination, simplification and automation, including maintenance and indirect costs. It is not an automation-first foil. **Adapt** its whole-burden and cause-removal reasoning in 4.3–4.6 to the broader receiving-use question. Use the domain practice directly when it already supplies that answer. For the broader question, sections 4.1 and 4.3 also compare changes when knowledge or capability is the needed result and purposeful repetitions contribute to it. The trade-off is extra diagnosis where those distinctions matter; this synthesis offers no established gain from repeating them when they are already settled. [Eliminating Toil](https://sre.google/workbook/eliminating-toil/).

**A competent improvement cycle can already suffice.** IHI's PDSA guidance connects prediction, a bounded test, observation, learning and adaptation; its implementation guidance distinguishes testing from changes in ordinary provision. **Adopt** that separation in 4.6–4.7. **Adapt** the earlier construction in 4.1–4.5 when the live uncertainty is which demand to remove or which complete alternative to test. PDSA can handle combined changes and unintended effects; the pattern does not claim those as missing inventions. If an existing improvement practice already carries the needed construction and comparison, use it without another pass. Reopen the selected synthesis if an equally usable simpler treatment preserves these distinctions at lower burden. [Testing Changes](https://www.ihi.org/library/model-for-improvement/testing-changes), [Implementing Changes](https://www.ihi.org/library/model-for-improvement/implementing-changes).

**Subtraction deserves consideration, not automatic preference.** Adams and colleagues' experiments support including subtractive possibilities explicitly when people generate changes; they do not show that removal generally outperforms addition. Later work reports task and population variation and further bounded replication. **Adapt** the candidate search in 4.4 to include ending or removing work; **reject** subtraction as the selection rule. An added preventive check can win, as 5.1 shows. Reopen the search cue if evidence for the actual reader and task makes it ineffective or unnecessarily burdensome. [Adams et al., 2021](https://doi.org/10.1038/s41586-021-03380-y), [Juvrud et al., 2024](https://doi.org/10.1038/s41598-024-51549-y), [Fillon et al., 2025](https://doi.org/10.1002/jocb.1535).

The worked cases establish inspectable consequences of their stipulated premises. They do not validate expected savings, a universal human or AI bias, or the comparative effectiveness of the whole method. A stronger practical claim needs evidence from its actual conditions.

