---
chunk_kind: "child"
pattern_id: "B.5.2.1"
pattern_title: "Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)"
section_id: "B.5.2.1:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2.1/B.5.2.1__001_intro.md"
commit_sha: "c3b34de07a6bd2df85c7081a4c367fd09978079c"
heading_path:
  - "B.5.2.1 — Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)"
  - "B.5.2.1:intro — Intro"
line_start: 49849
line_end: 49858
dependencies:
  - "A.17"
  - "A.18"
  - "B.4"
  - "B.5"
  - "B.5.2"
  - "C.11"
  - "C.17"
  - "C.18"
  - "C.19"
  - "G.5"
keywords:
---

## B.5.2.1 - Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)

**Normativity:** Normative binding to **B.5.2 Abductive Loop**. The local **NQD-Generate** Method in §4, or an equivalent declared generator, constructs the candidates. **C.18** supplies generation, archive and front records; **C.19** supplies the applicable exploration/exploitation policy.

> **Status:** Stable

**Method and records.** Use A.17/A.18 for Characteristics and A.3.1/A.3.2 for the Method and its description. Distinguish its input and seed conditions, conditions for any actual generation Work, and the generated candidate’s later admission to comparison. C.18 records the identified generator and its results; filling that record performs no generation.

**Terminology discipline.** Use **NQD** consistently (Novelty–Quality–Diversity). Treat **S**/**I** as *secondary* metrics unless explicitly promoted by policy (see §3, §5).

