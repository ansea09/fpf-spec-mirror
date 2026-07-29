---
chunk_kind: "child"
pattern_id: "B.5.2"
pattern_title: "Abductive Loop"
section_id: "B.5.2:13"
section_title: "Prompt, Candidate, and Hypothesis Package Discipline"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2/B.5.2__014_prompt-candidate-and-hypothesis-package-discipline.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "B.5.2 — Abductive Loop"
  - "B.5.2:13 — Prompt, Candidate, and Hypothesis Package Discipline"
line_start: 40394
line_end: 40434
dependencies:
  - "A.10"
  - "A.16"
  - "A.22.CGUS"
  - "A.6.P"
  - "B.3.3"
  - "B.4.1"
  - "B.5"
  - "B.5.2.0"
keywords:
  - "abduction"
  - "candidate hypotheses"
  - "explanatory prompt"
  - "origin trace"
  - "plausibility filters"
  - "route-to-hypothesis"
---

### B.5.2:13 - Prompt, Candidate, and Hypothesis Package Discipline

The abductive loop stays auditable only if the three main publication forms remain distinct: the **prompt**, the **candidate set**, and the **selected prime hypothesis**. Collapsing them into one paragraph is one of the main reasons later review cannot reconstruct what actually happened.

#### B.5.2:13.1 - Prompt package

A conforming prompt package should make explicit:

- the **prompt species** (`AnomalyStatement`, `ProblemCuePrompt`, `OpportunityCuePrompt`, or `ProbeCuePrompt`),
- the **open question** that makes abduction necessary,
- the **declared scope** under which the question is being posed,
- the **witnesses or provenance cues** that made the prompt worth preserving,
- and the **reason the current model is insufficient**.

If the initiating publication is still primarily evaluative, action-inviting, or lexically overloaded, it should first be repaired by the relevant A.6 family before it is treated as a stable abductive prompt. `B.5.2` assumes typed entry, not raw lexical ambiguity.

#### B.5.2:13.2 - Candidate-set note

A candidate-set note is the minimal record that preserves rival plurality. It need not be heavy, but it should make visible:

- candidate identifiers or short names,
- the differentiating claim each candidate adds,
- the principal plausibility supports and liabilities of each candidate,
- whether the candidate remains live, is deferred, or is rejected,
- and what missing evidence or probe would best discriminate among the remaining rivals.

The important point is not bureaucratic completeness. The important point is to prevent retrospective rewriting in which the surviving candidate is made to look as if it had been the only serious option from the beginning.

#### B.5.2:13.3 - Prime-hypothesis record

A selected prime hypothesis should preserve more than the hypothesis sentence itself. A conforming `L0` hypothesis record should name:

- the **selected candidate**,
- the **prompt** it answers,
- the **filters** under which it outranked rivals,
- the **scope** within which it is being advanced,
- the **next admissible downstream move** (deduction, probe design, targeted evidence acquisition, or explicit reopening criteria),
- and any **known fragilities** already visible at selection time.

This is how `B.5.2` stays connected to the rest of the reasoning cycle. The abductive loop does not merely emit an idea; it emits a conjecture with explicit downstream-use terms.

