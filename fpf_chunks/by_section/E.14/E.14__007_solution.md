---
chunk_kind: "child"
pattern_id: "E.14"
pattern_title: "Human‑Centric Working‑Model"
section_id: "E.14:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.14/E.14__007_solution.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "E.14 — Human‑Centric Working‑Model"
  - "E.14:4 — Solution"
line_start: 76197
line_end: 76246
dependencies:
  - "B.3.5"
  - "C.13"
  - "C.2.3"
  - "E.10"
  - "E.7"
  - "E.8"
keywords:
  - "assurance layers"
  - "grounding"
  - "human-centric"
  - "publication surface"
  - "working model"
---

### E.14:4 - Solution

#### E.14:4.1 - Human-Centric principles

##### E.14:4.1.1 - Recognition text and assurance text
Human-facing patterns also need EntityOfConcern stability across the two reading-order text blocks. The working reader should not meet one object in the recognition text and a different ontological kind in the assurance text. If the pattern distinguishes an EntityOfConcern, the interpretive or operational move applied to that object, and the wider review or work process around it, those distinctions should be made explicit rather than hidden behind stylistic noun-swapping.

Working-Model-first drafting therefore also means subject-domain-first drafting. If a pattern is meant to help with a real review, design, cultural, research, or operational problem, the recognition text should open from that problem-owning moment before internal taxonomy or package architecture. If a broader umbrella head and a narrower operative branch are both live, the pattern should state that stack plainly enough that a cold reader can tell what the umbrella names, what branch is current, what object is governed, what move is being carried, and what wider work remains outside.

Under `F.18` local-first naming, the canonical pair here is **recognition text** and **assurance text**.
The earlier provisional `...shell` wording is retired.
These names refer to two reading-order text blocks inside one pattern, not to new publication-face kinds or authority kinds.

For human-facing canonical patterns, Working-Model-first discipline should appear in a two-part reading order.
The **recognition text** is the working text that a cold practitioner, manager, or researcher should be able to understand first: what situation this pattern is for, what it buys, what it is not for, and what ordinary mistake it helps prevent.
The **assurance text** is the heavier text that carries declaration, object discipline, modeling lens, law, return conditions, and other assurance work.

The assurance text may justify, tighten, or audit the working text, but it must not silently replace or strengthen the recognition-text claim.
Where episteme-publication-heavy or transform-heavy patterns need a compact ontological account, the assurance text should expose three things explicitly:
- the ontic target or EntityOfConcern;
- the modeling substrate or mathematical lens when one is load-bearing;
- the publication face or working text by which the claim is presented.

This is a reading-order rule rather than a demand that every reader consume the assurance text first.
The point is to keep the human-facing Working-Model text primary while preserving a recoverable, auditable assurance text beneath it.
> **E.14‑P.1 – Working‑Model first, stance explicit.**  **
> Operate one **Working-Model** for all human-facing discussion. For **each** assertion, the author **SHALL declare** an assurance posture (`validationMode`) and choose the **appropriate assurance shoulder(s)**: **Mapping** (term-to-kind alignment through Lang-CHR or D-Projection), **Logical** (label-meaning rules, scope, and constraints), **Constructive** (a C.2.1 construction-trace episteme about independently grounded facts), and **Empirical Validation** (an evidence-use relation for the claim, with scope, timespan, provenance, and declared `U.BoundedContext`). None of these shoulders creates the governed value, relation occurrence, or identity it supports.

> **E.14‑P.2 – Downward‑only dependency.**
> Information **may** flow from the Working‑Model down into any Assurance layer; **no Assurance layer may impose vocabulary or shape back upward** into the Working‑Model.
>
> **E.14‑P.3 – Small working text, big proof.**
> The Working-Model exposes a **minimal set** of names (L-1/L-2 registers) and a compact family of relations used in everyday reasoning; the assurance text makes their meanings, direct basis, limits, and support inspectable below.

> **E.14‑P.4 – Human registers first.**
> Terms in the Working‑Model are deliberately curated for **human legibility** (register‑badged, synonym‑aware). Synonym capture and language variance belong to Mapping; **only the chosen canonical label appears in the Working-Model text**.

> **E.14‑P.5 – Justification modes are explicit.**
> Each Working‑Model relation **declares** `validationMode ∈ {axiomatic, inferential, postulate}`.
> _axiomatic_ means that the author relies on one linked Constructive account for this assertion; _inferential_ means that the author relies on a reasoned chain; _postulate_ means that the assertion remains a pragmatic claim requiring Empirical Validation. `validationMode` is an assurance posture, not a world-side relation kind, identity test, or timelessness guarantee. Empirical Validation may also accompany inferential or axiomatic assertions. Mapping, Logical, Constructive, and Empirical assurance remain separate from the claim's direct ontology and from the currentness of every record involved.

> **E.14‑P.6 – Parsimony in the working text.**
> No new Working‑Model relation types are introduced if the existing Logical label-meaning rules plus Constructive grounding suffice to capture the intended meaning.

> **E.14‑P.7 – Evidence is first-class claim grounding.**
> When *postulate* is chosen, authors **SHALL** attach an **evidence pointer** (Empirical Validation) appropriate to the claim and context, governed as an evidence-use relation within a declared `U.BoundedContext`.

> **E.14‑P.8 – Working-model-first is not explanation-thin.**
> Human-facing parsimony does **not** license under-explained pattern prose. When a pattern claims a Working‑Model benefit, it **SHALL** still provide enough problem framing, rationale, and worked slices that readers can tell what the model clarifies, what remains on the assurance shoulders, and when a heavier review path is required.

