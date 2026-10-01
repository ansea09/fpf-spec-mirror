---
chunk_kind: "child"
pattern_id: "C.28.CM"
pattern_title: "Construct and Challenge a Causal Model"
section_id: "C.28.CM:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28.CM/C.28.CM__012_sota-echoing.md"
commit_sha: "e9b4ea53bed91a5364342d302708e8ec40db3175"
heading_path:
  - "C.28.CM — Construct and Challenge a Causal Model"
  - "C.28.CM:11 — SoTA-Echoing"
line_start: 64567
line_end: 64578
dependencies:
  - "A.15.9"
  - "B.5.2"
  - "B.5.FM"
  - "C.11.DUA"
  - "C.16"
  - "C.27"
  - "C.28"
  - "C.28.MR"
  - "C.29"
keywords:
---

### C.28.CM:11 - SoTA-Echoing

The comparison concerns usable construction and criticism for a bounded causal question. It does not rank causal-discovery algorithms or claim a universally best empirical workflow.

| Practice question and selected move | Alternative, trade-off and concrete use | Source role, limits and reopening |
| --- | --- | --- |
| How can a working account become explicit causal assumptions? **Adapt** extraction, translation and critical integration of subject claims. | Directly drawing the preferred story is cheaper but can hide missing or conflicting premises. :4.2–4.3 recover meanings and alternatives; a full evidence synthesis is reserved for questions that need it. | [Ferguson et al., 2020, Table 1 and Discussion](https://pdfs.semanticscholar.org/cb52/45fd90f7942f734911ebd1492c3d3e5a4e24.pdf) supplies a developed construction comparator. Its integration heuristics do not establish causal truth. Reopen when this extraction loses a subject mechanism or a simpler adequate construction is available. |
| Which conditioning changes the causal question or opens a misleading path? **Adopt** whole-graph path inspection; **reject** deciding from a variable's name or one three-node picture. | Classifying a few familiar motifs is quicker but can miss another open path or conditioning through selection. :4.4 works the entire small graph and :5.3 preserves assignment and selection. | [Geiger, Verma and Pearl, 1990](https://ftp.cs.ucla.edu/pub/stat_ser/r116.pdf) gives the formal separation basis; [Cinelli, Forney and Pearl, 2022](https://ftp.cs.ucla.edu/pub/stat_ser/r493-reprint.pdf) supplies the current practice comparison for controls. These are conditional graphical results, not tests of omitted subject premises. Change the rule when the graph class or estimand changes. |
| What if the graph itself is uncertain? **Adapt** comparison of the causal query over admissible structures. | Selecting one convenient graph simplifies calculation but can suppress a result-changing rival. :4.5 retains the remaining family and states its shared or differing consequences. | [Padh et al., 2025, §§2 and 6](https://arxiv.org/html/2502.17030v2) supplies a computational line with explicit structural uncertainty; its procedure assumes no hidden confounding and has optimization limitations. [Peters et al., 2014](https://jmlr.org/papers/volume15/peters14a/peters14a.pdf) shows how additional model assumptions can identify structure. Neither licenses assumption-free discovery. Reopen when a qualified result excludes a live rival or reveals another. |
| How should feedback affect construction? **Adopt** temporal distinction where it answers the query; otherwise request a suitable cyclic model. | Forcing an equilibrium loop into a DAG can delete the operative mechanism. :4.4 and :5.2 retain the horizon and the controller dependency. | [Bongers et al., 2021](https://staff.fnwi.uva.nl/j.m.mooij/articles/21-AOS2064.pdf) supplies existence and interpretation conditions for cyclic structural models. Its theory makes a cyclic alternative available under conditions, not automatically solvable. Reopen when the chosen temporal resolution or equilibrium premise changes. |
| Is specialized construction needed at all? **Retain** direct use of sufficient general modeling or a supplied mechanism model. | B.5.FM can construct the thermal limiting argument without a causal-model family; C.28.MR can transform supplied equations directly. This pattern adds work only when the causal account or a material alternative is missing. | These internal alternatives determine :1 and :4.7. In :5.2 the additional work distinguishes supply, display and feedback before choosing a transformation. The examples establish conditional reasoning, not superior field performance. Prefer the simpler route when it supplies that distinction already. |

