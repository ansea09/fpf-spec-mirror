---
chunk_kind: "child"
pattern_id: "A.17"
pattern_title: "Canonical “Characteristic” (A.CHR-NORM): Name What Is Measured"
section_id: "A.17:9"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.17/A.17__010_rationale.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "A.17 — Canonical “Characteristic” (A.CHR-NORM): Name What Is Measured"
  - "A.17:9 — Rationale"
line_start: 34366
line_end: 34377
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
  - "F.7"
  - "F.9"
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

A.7 keeps the measured aspect distinct from its description and result. For example, a requirement category, a measured Characteristic and an evaluative Score may all have been called a dimension; identifying their different functions lets the reader select the corresponding rule.

The historical distinction among nominal, ordinal, interval and ratio Scales identifies which transformations preserve the represented meaning. FPF uses those distinctions to constrain calculations. A domain model or ScoringMethod may justify an additional operation; a shared numerical encoding alone cannot.

Distinguishing entity and relation Characteristics keeps the bearer of a measurement recoverable. A.3.3 can use the declared Characteristics to describe a state; an assurance argument can name the aspect for which it uses a measurement. Quantity calculations use their mathematical relation and applicability conditions; evaluative scores additionally need the preference that the scoring method represents. This lets a reader distinguish a derived physical value from a judgement about that value.

The question determines the required state description. A model may need repeated states, several continuations or a stopping condition. Development can revise that model and open new questions. A state-recognition checklist serves a use that needs such recognition; it does not supply the transition law.

