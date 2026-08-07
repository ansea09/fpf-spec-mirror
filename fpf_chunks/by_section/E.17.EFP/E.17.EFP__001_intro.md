---
chunk_kind: "child"
pattern_id: "E.17.EFP"
pattern_title: "ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
section_id: "E.17.EFP:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.EFP/E.17.EFP__001_intro.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "E.17.EFP — ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
  - "E.17.EFP:intro — Intro"
line_start: 80928
line_end: 80992
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.B"
  - "A.7"
  - "B.3"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.ID.CR"
  - "F.18"
  - "F.9"
  - "U.MultiViewDescribing"
keywords:
---

## E.17.EFP - ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**One-line summary.** `ExplanationFaithfulnessProfile` classifies the bounded explanation use of a publication form or representation of one exact claim-bearing episteme. It does not decide which episteme the text expresses and cannot turn changed claims into another form of the source.

**Explanation-facing text in plain terms.** One published text on an existing MVPK face. If it expresses the source edition's exact ClaimGraph, it is a publication form or representation of that source edition. If its claim content differs, it can be a form only of a separately identified target episteme, not of the source edition.

**Ontic first screen.** Before assigning an explanation class, compare the claims expressed by the text with the exact source ClaimGraph.

1. If the text expresses that same ClaimGraph, identify the applicable E.24.PUB publication form or A.6.3.RT representation of the source edition. EFP then qualifies only the explanation use of that form or representation.
2. If omission, reconstruction, pedagogy, or another change produces a different ClaimGraph, identify the exact target `U.Episteme` under C.2.1 and the obtaining source-to-target relation under `A.6.3.CR`, `A.6.3.CSC`, or another exact pattern. EFP may then qualify the explanation use of a publication form of that target; its class label creates neither the target nor the relation.
3. A new causal or counterfactual proposition is a claim of a separate hypothesis episteme under `B.5.2`, or it stays outside EFP. It is not a passive rendering of the source merely because reliance on it is blocked.

**Explanation-use relation in plain terms.** State which exact episteme the published text expresses, how that episteme relates to the named source when it is a different target, which explanation-use class applies, and what downstream claim or effect still stays outside the profile. Name the exact E.24.PUB publication occurrence, pins, traces, or provenance only when they are material to the present use.

**Use this when.** Use EFP when a real source-pinned, reconstructive, didactic, or speculative ambiguity changes how a published explanation form may be reviewed or used—especially for generated, retrieval-facing, model-facing, derivative, or interactive explanation. Authorship alone does not trigger the profile.

**Start here when.** First decide whether the text expresses the same source ClaimGraph or a different target ClaimGraph. Only after the exact claim-bearing episteme and any required source-to-target relation are known, choose the explanation-use class.

**What goes wrong if missed.** A publication form, a rewritten episteme, and a new hypothesis are all called a rendering of one source. Helpful wording then hides a changed claim-bearing object or an unsupported source relation.

**What this buys.** One honest identity branch followed by one bounded explanation-use class: the reader can tell which episteme is being published, how a changed target was obtained, and which stronger use remains blocked.

**Not this pattern when.** For an ordinary human-authored note, if a source locator plus one natural-language bounded/blocked-use sentence already preserves meaning and prevents the credible overread, use that simpler publication note and stop. Also do not use EFP to establish rewrite, representation change, coarsening, comparison, retargeting, hypothesis production, evidence, work, assurance, or gate claims; apply their exact patterns first.

**First output.** One compact explanation-use note naming the exact source or related target episteme, explanation class, source reference, bounded explanation-reader use, blocked downstream use, and reopen or boundary condition. The note names a source-to-target relation only when the text expresses a different target ClaimGraph. MVPK face, pins, provenance, and other source fields are inherited by reference unless ambiguity or a load-bearing use makes them relevant.

**Ordinary-output claim inventory.** After `ExplanationFaithfulnessProfile`, the author has claimed only that a publication form or representation of this already identified episteme has this explanation class and bounded use. EFP has not constituted an episteme, made a source-to-target relation obtain, or established model truth, evidence, assurance, safe reliance, gate passage, work occurrence, release reliance, or source replacement.

**Working explanation move.** Perform the ontic first screen, identify the exact episteme expressed by the text and any already obtaining source-to-target relation, then classify the publication form's explanation use and state its bounded reader use. If the identity or relation cannot be established, do not repair that gap with an explanation class; return to C.2.1 and the exact rewrite, coarsening, representation, hypothesis, comparison, evidence, work, assurance, or gate pattern.
**Lower-burden ordinary branch.** First try a source locator plus one sentence naming the allowed reader help and blocked stronger use. If that resolves an ordinary human-authored case, do not instantiate EFP. When class ambiguity still changes the next action, use the compact EFP result and no fuller field block.

**Load-bearing use.** Open the fuller explanation review only when the rendering will guide work or reliance, be externally relied on, be disputed, cross context, affect person or team status, or be cited as evidence, approval, engineering justification, gate, or release reliance.

**Stop condition.** Stop before EFP when the simpler source-linked boundary sentence performs the task. After EFP is triggered, stop when the class, bounded/blocked use, and reopen condition settle the next action; add no field or check that does not change it.

**Bounded explanation-use examples.**

| Bounded explanation use | Source-finding check with no downstream claim or effect | Blocked explanation use |
| --- | --- | --- |
| A `SourcePinnedExplanation` or `SourceLinkedExplanationReconstruction` helps navigation, bounded restatement, or source inspection with pins and trace visible. | A didactic explanation helps onboarding or source-finding, while any operative claim returns to the exact source or target episteme and its obtaining source-to-target relation; an `A.10` evidence path opens only when the receiving use actually needs evidence. | A fluent explanation is used as assurance, evidence, approval, gate passage, release permission, or work-occurrence evidence. |

**Neighboring patterns and project records.** `E.17.ID.CR` supplies the bounded-comparison discipline for a comparative review unit; `A.6.3.CR` and `A.6.3.RT` define same-entity rewrite and representation change; `A.6.3.CSC` defines the narrower-use result, blocked downstream use, and source-bearing reopen needed after deliberate coarsening; `A.6.4` and `OntologicalReframing` address a changed EntityOfConcern; `A.15` and `A.15.4` define downstream work or reliance; `B.3` supplies assurance and engineering-justification tests; and `A.20` or `A.21` define gate-bearing claims and effects. For permission-looking or policy-bearing prose, use `A.2.8.PER` for strong grants, exercises, weak non-prohibition/non-violation findings, and permission conflicts; use `A.2.8` for obligation, recommendation-as-duty, and prohibition commitments; and use `A.2.9` for the communicative Work that institutes or revokes an effect.

**Common wrong escalations and boundary transfers.** Do not use this profile to hide new claims, bridge-comparison load, action-selection pressure, or gate-bearing guidance inside helpful prose. If the rendering is really a bounded comparison, apply `E.17.ID.CR`; if it is only same-entity rewriting or representation shift, apply `A.6.3.CR` or `A.6.3.RT`; if a deliberately coarsened rendering's narrower bounded claim or effect, blocked downstream use, and source-bearing reopen are the actual problem, apply `A.6.3.CSC`; if it is already making world, work or reliance, assurance, or gate-bearing claims, leave `E.17.EFP` for the more exact downstream FPF pattern or project-side record.

**Generated-explanation repaired case.** For a generated text, first compare its expressed claims with the exact source ClaimGraph. Unchanged claims permit a form or representation of the source edition; changed claims require an exact target episteme and obtaining A.6.3 or other source-to-target relation before EFP classification. Missing identity or relation yields only an unclassified text and a prospective repair request. After identity is settled, use beyond reader help additionally requires an `A.10` path for each operative claim and, for any assurance, gate, work, permission, approval, or release claim, its applicable pattern and exact project record when one is required; missing evidence keeps the classified form at reader help or source-finding.

**Common wrong first interpretation.** A fluent, confident, source-linked, or reliable-looking explanation is treated as evidence. First honest entry: identify the exact episteme expressed by the text and any required source-to-target relation, then classify its publication form for reader help or source-finding; only an operative claim with an A.10 evidence path or another source relation that carries, supports, or exposes the source basis for the operative claim can carry downstream reliance.

Negative result: if a generated explanation says "reliable" but no operative claim maps to a source relation, the E.17.EFP result is source-finding only or reader help only. If an attempted downstream reliance is still raised, the receiving `A.10`, `B.3`, `A.21`, or other relation named by value can return evidence-needed or no-bounded-current-use for that attempted reliance. It is not weak evidence by style, confidence, fluency, or citation-like wording.

**Generated-retelling survival.** A generated text that expresses the same source ClaimGraph may preserve an inspectable reader-help use, source-finding cue, and quoted source pins as a form or representation of that source edition. If it compresses, omits, strengthens, or otherwise changes claim content, identify a different target episteme and the obtaining A.6.3 or other source-to-target relation before classifying its publication form. It does not preserve source identity, evidence, assurance, gate passage, decision status, permission, or work authority by fluency or links.

**Derivative text and adaptation source-link rule.** A fork, adaptation, abridged guide, translation, generated explanation, tutorial, or access-format conversion first undergoes the same ClaimGraph test. Same claims permit a form or representation of the source edition; changed claims require an exact target episteme and an obtaining `A.6.3.CR`, `A.6.3.CSC`, or other direct relation. EFP then qualifies explanation use only if needed. If the result will guide work or reliance, `A.10` maps each operative claim to its exact source basis; a missing map permits only reader help, a source-gap note, or prospective evidence work.

**Published-form and episteme identity over revision and regeneration.** A revised or regenerated text is not reidentified by source face, prompt, template, carrier, or title. Compare its expressed ClaimGraph first: unchanged claims may identify another form or representation of the same episteme edition; changed claims identify another target episteme under C.2.1 and require the exact source-to-target relation. When use beyond ordinary reader help depends on how the text was produced, identify the exact generation or production relation and the source references it actually used; neither relation changes episteme identity by itself. EFP records only the bounded explanation use of the resulting published form.

**Pattern basis.** E.17 supplies face discipline; E.17.0 supplies viewpoint/view conformance only when `U.View` membership is material.
**Builds on.** `E.17.0 U.MultiViewDescribing`; `E.17` MVPK; `A.7`; `E.10.D2`; `A.6.B`; `F.9`; `F.18`.
**Coordinates with.** `ConservativeRetextualization`; `RepresentationSchemeTransition`; `E.17.ID.CR ComparativeReviewUnit`; `A.6.4`; `A.10`; `A.15`; `A.15.4`; `B.3`; `A.20`; `A.21`; `A.2.8`; `A.2.8.PER`; `A.2.9`.

