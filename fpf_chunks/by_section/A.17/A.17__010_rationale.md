---
chunk_kind: "child"
pattern_id: "A.17"
pattern_title: "Canonical “Characteristic” (A.CHR‑NORM)"
section_id: "A.17:9"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.17/A.17__010_rationale.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "A.17 — Canonical “Characteristic” (A.CHR‑NORM)"
  - "A.17:9 — Rationale"
line_start: 29765
line_end: 29778
dependencies:
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.2.3"
  - "A.3.3"
  - "A.7"
  - "B.3"
  - "C.16"
  - "C.2"
  - "D.3"
  - "E.10"
  - "U.Dynamics"
  - "U.PromiseContent.acceptanceSpec"
keywords:
  - "attribute"
  - "axis"
  - "characteristic"
  - "dimension"
  - "measurement"
  - "preference"
  - "property"
  - "quantity calculation"
  - "scale order"
  - "scoring"
---

### A.17:9 - Rationale

The distinction between Scale order and preference follows the different questions they answer. [VIM3 §1.27](https://jcgm.bipm.org/vim/en/1.27.html) orders quantity values by magnitude. Evaluation adds a judgement about which values are desirable for a use. [VIM3 §1.22](https://jcgm.bipm.org/vim/en/1.22.html) supplies the separate notion of a relation between quantities. FPF adopts these measurement distinctions and places use-dependent preference with A.19.ECS and the applicable comparison or scoring Method.

The Canonical Characteristic pattern is a direct response to recurring measurement pitfalls. By insisting on “one precise name per concept”, it upholds **Strict Distinction (A.7)**, ensuring that the framework never treats two different ideas as one. For instance, earlier practice might label both a requirement category and its score as “dimension,” causing confusion; with A.17, the _aspect_ is a Characteristic and its _score_ is separate, so each idea has its place. This clarity is pedagogically vital (**P‑2 Didactic Primacy**): readers and contributors immediately know what a term means and how to interpret any value associated with it.

The solution also draws on fundamentals of measurement theory (Stevens’ levels of measurement) to prevent misuse. By encoding scale types and unit handling into our patterns, we avoid the “pseudo-quantitative” fallacies – no more averaging things like _risk levels_ or adding up _grades_ as if they were true numbers. In effect, A.17 puts a safeguard around **P‑1 Cognitive Elegance and P‑7 Ontological Parsimony**: we use a minimal, universal set of measurement constructs, and we avoid bloating the conceptual space with domain-specific or redundant terms. One canonical set of terms also makes the framework more teachable and **composable across contexts**, since patterns and projects aren’t inventing new synonyms that others must decipher.

Distinguishing entity and relation Characteristics keeps the bearer of a measurement recoverable. A.3.3 can use the declared Characteristics to describe a state; an assurance argument can name the aspect for which it uses a measurement. Quantity calculations use their mathematical relation and applicability conditions; evaluative scores additionally need the preference that the scoring method represents. This lets a reader distinguish a derived physical value from a judgement about that value.

The question determines the required state description. A model may need repeated states, several continuations or a stopping condition. Development can revise that model and open new questions. A state-recognition checklist serves a use that needs such recognition; it does not supply the transition law.

In summary, A.17 is the linchpin that turns a loose collection of measurement practices into a **coherent, principle-driven system**. It rationalizes the language, thereby rationalizing thought: by speaking in one clear voice about measurements, FPF ensures that every number in the system can be trusted to answer “value of what, on what scale, relative to what context.” This rationale is reflected in improved model integrity and cross-domain trust in the meaning of metrics.

