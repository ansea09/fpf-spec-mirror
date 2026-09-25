---
chunk_kind: "child"
pattern_id: "E.17.EFP"
pattern_title: "ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
section_id: "E.17.EFP:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.EFP/E.17.EFP__001_intro.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "E.17.EFP — ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
  - "E.17.EFP:intro — Intro"
line_start: 92804
line_end: 92869
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
  - "C.2.8"
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

**Explanation-facing text in plain terms.** One published text on an existing MVPK face. It may express only the part of an exact source edition needed for a declared explanation use. Identify that edition by its ClaimGraph, exact EntityOfConcern and effective ReferenceScheme; then test whether the form expresses enough for that use. Omitting other source content neither claims whole-source coverage nor by itself constitutes another episteme. A changed assertion, concern or effective scheme needs its own identity decision.

**Ontic first screen.** Before assigning an explanation class, identify the source and the intended reader use.

1. Recover the exact source edition's ClaimGraph, EntityOfConcern and effective ReferenceScheme under C.2.1. Equal displayed words alone do not establish this identity.
2. Test whether the text expresses enough of that edition for the declared use under E.24.PUB §4.2. Preserve every qualification that changes the answer for that use, keep the source return, and disclose use-relevant omissions. A partial expression may qualify; a missing required condition leaves source sufficiency unresolved or fails it, even when each displayed sentence is individually true. Omission alone does not create a target episteme. Apply A.6.3.RT as well when a representation-change claim is current.
3. If the text asserts changed content or concerns another entity or effective scheme, identify the exact target under C.2.1 and the source-to-target relation actually claimed under A.6.3.CR, A.6.3.CSC, A.6.4 or another applicable pattern. Establish that relation independently before EFP classifies the target form; the class creates neither participant nor relation.
4. A new causal or counterfactual proposition belongs to a separate hypothesis episteme under B.5.2, or stays outside EFP. Blocking reliance on it does not make it a rendering of the source.

**Explanation-use relation in plain terms.** State which exact episteme the published text expresses, how that episteme relates to the named source when it is a different target, which explanation-use class applies, and what downstream claim or effect still stays outside the profile. Name the exact E.24.PUB publication occurrence, pins, traces, or provenance only when they are material to the present use.

**Use this when.** Use EFP when a real source-pinned, reconstructive, didactic, or speculative ambiguity changes how a published explanation form may be reviewed or used—especially for generated, retrieval-facing, model-facing, derivative, or interactive explanation. Authorship alone does not trigger the profile.

**Start here when.** Identify the source edition through claim content, concern and effective scheme. Then test whether the text preserves enough for the declared explanation use, or asserts a separately identified target. Choose the explanation-use class only after source sufficiency and any required target relation are established.

**What goes wrong if missed.** A publication form, a rewritten episteme, and a new hypothesis are all called a rendering of one source. Helpful wording then hides a changed claim-bearing object or an unsupported source relation.

**What this buys.** One honest identity branch followed by one bounded explanation-use class: the reader can tell which episteme is being published, how a changed target was obtained, and which stronger use remains blocked.

**Not this pattern when.** For an ordinary human-authored note, if a source locator plus one natural-language bounded/blocked-use sentence already preserves meaning and prevents the credible overread, use that simpler publication note and stop. Also do not use EFP to establish rewrite, representation change, coarsening, comparison, retargeting, hypothesis production, evidence, work, assurance, or gate claims; apply their exact patterns first.

**First output.** One compact explanation-use note naming the exact source or related target episteme, explanation class, source reference, bounded explanation-reader use, blocked downstream use, and reopen or boundary condition. The note names a source-to-target relation when the text expresses a separately identified target, including a changed concern or effective scheme. MVPK face, pins, provenance, and other source fields are inherited by reference unless ambiguity or a load-bearing use makes them relevant.

**Ordinary-output claim inventory.** After `ExplanationFaithfulnessProfile`, the author has claimed only that a publication form or representation of this already identified episteme has this explanation class and bounded use. EFP has not constituted an episteme, made a source-to-target relation obtain, or established model truth, evidence, assurance, safe reliance, gate passage, work occurrence, release reliance, or source replacement.

**Working explanation move.** Perform the ontic first screen, identify the exact episteme expressed by the text and any already obtaining source-to-target relation, then classify the publication form's explanation use and state its bounded reader use. If identity, sufficiency for the declared use or a required relation cannot be established, do not repair that gap with an explanation class; return to C.2.1 and the exact rewrite, coarsening, representation, hypothesis, comparison, evidence, work, assurance, or gate pattern.
**Lower-burden ordinary branch.** First try a source locator plus one sentence naming the allowed reader help and blocked stronger use. If that resolves an ordinary human-authored case, do not instantiate EFP. When class ambiguity still changes the next action, use the compact EFP result and no fuller field block.

**Load-bearing use.** Open the fuller explanation review only when the rendering will guide work or reliance, be externally relied on, be disputed, cross context, affect person or team status, or be cited as evidence, approval, engineering justification, gate, or release reliance.

**Stop condition.** Stop before EFP when the simpler source-linked boundary sentence performs the task. After EFP is triggered, stop when the class, bounded/blocked use, and reopen condition settle the next action; add no field or check that does not change it.

**Bounded explanation-use examples.**

| Bounded explanation use | Source-finding check with no downstream claim or effect | Blocked explanation use |
| --- | --- | --- |
| A `SourcePinnedExplanation` or `SourceLinkedExplanationReconstruction` helps navigation, bounded restatement, or source inspection with pins and trace visible. | A didactic explanation helps onboarding or source-finding, while any operative claim returns to the exact source or target episteme and its obtaining source-to-target relation; an `A.10` evidence path opens only when the receiving use actually needs evidence. | A fluent explanation is used as assurance, evidence, approval, gate passage, release permission, or work-occurrence evidence. |

**Neighboring patterns and project records.** `E.17.ID.CR` supplies the bounded-comparison discipline for a comparative review unit; `A.6.3.CR` and `A.6.3.RT` define same-entity rewrite and representation change; `A.6.3.CSC` defines the narrower-use result, blocked downstream use, and source-bearing reopen needed after deliberate coarsening; `A.6.4` and `OntologicalReframing` address a changed EntityOfConcern; `A.15` governs System-Role–Method–Work alignment; `A.15.1` independently admits dated Work; `A.15.4` repairs an appearance-based work or reliance use only while its prerequisite remains unclear; `B.3` supplies assurance and engineering-justification tests; `A.20` tests a named internal constraint for a stated case under that pattern's subject and applicability conditions; and `A.21` governs a named gate decision under its applicable profile. For permission-looking or policy-bearing prose, use `A.2.8.PER` for strong grants, exercises, weak non-prohibition/non-violation findings, and permission conflicts; use `A.2.8` for obligation, recommendation-as-duty, and prohibition commitments; and use `A.2.9` for the communicative Work that institutes or revokes an effect.

**Common wrong escalations and boundary transfers.** Do not use this profile to hide new claims, bridge-comparison load, action-selection pressure, or gate-bearing guidance inside helpful prose. If the rendering is really a bounded comparison, apply `E.17.ID.CR`; if it is only same-entity rewriting or representation shift, apply `A.6.3.CR` or `A.6.3.RT`; if a deliberately coarsened rendering's narrower bounded claim or effect, blocked downstream use, and source-bearing reopen are the actual problem, apply `A.6.3.CSC`; if it is already making world, work or reliance, assurance, or gate-bearing claims, leave `E.17.EFP` for the more exact downstream FPF pattern or project-side record.

**Generated-explanation repaired case.** Identify the exact source by its claims, concern and effective scheme, then test the generated text for the declared use. A sufficient partial expression may remain a form of that source; missing use-relevant content requires source return or repair, not automatic target creation. Changed assertions require an exact target and an independently obtaining source-to-target relation. An identity, sufficiency or relation gap leaves classification for that use open. After identity and bounded sufficiency are settled, use beyond reader help additionally requires an `A.10` path for each operative claim and, for any assurance, gate, work, permission, approval, or release claim, its applicable pattern and exact project record when one is required; missing evidence keeps the classified form at reader help or source-finding.

**Common wrong first interpretation.** A fluent, confident, source-linked, or reliable-looking explanation is treated as evidence. First honest entry: identify the exact episteme expressed by the text and any required source-to-target relation, then classify its publication form for reader help or source-finding; only an operative claim with an A.10 evidence path or another source relation that carries, supports, or exposes the source basis for the operative claim can carry downstream reliance.

Negative result: if a generated explanation says "reliable" but no operative claim maps to a source relation, the E.17.EFP result is source-finding only or reader help only. If an attempted downstream reliance is still raised, the receiving `A.10`, `B.3`, `A.21`, or other relation named by value can return evidence-needed or no-bounded-current-use for that attempted reliance. It is not weak evidence by style, confidence, fluency, or citation-like wording.

**Generated-retelling survival.** Compression or omission may preserve a source edition's inspectable reader-help use, source-finding cue and quoted pins when the partial form remains sufficient under the ontic first screen. State the limited use and material omissions. If the text strengthens or otherwise changes an assertion, or changes the concern or effective scheme, identify the target and establish its claimed source-to-target relation before classifying the target form. Fluency and links establish neither identity nor sufficiency, evidence, assurance, permission, gate passage or work authority.

**Derivative text and adaptation source-link rule.** A fork, adaptation, abridged guide, translation, generated explanation, tutorial or access-format conversion first undergoes the same identity-and-bounded-sufficiency test. A sufficient partial expression may remain a source form. Insufficient expression returns the exact missing source content or condition; a changed claim-bearing target requires its own identity and an obtaining direct relation. EFP then qualifies explanation use only if needed. If the result will guide work or reliance, `A.10` maps each operative claim to its exact source basis; a missing map permits only reader help, a source-gap note, or prospective evidence work.

**Published-form and episteme identity over revision and regeneration.** Reidentify the source or target through ClaimGraph, exact EntityOfConcern and effective ReferenceScheme, then retest expression sufficiency for the declared use. A different selection of source content may remain another sufficient form of the same edition; equal words about another concern or under another effective scheme do not establish the same episteme. A changed target requires its direct source-to-target relation. Face, prompt, template, carrier or title alone settles none of these questions. When use beyond ordinary reader help depends on how the text was produced, identify the exact generation or production relation and the source references it actually used; neither relation changes episteme identity by itself. EFP records only the bounded explanation use of the resulting published form.

**Pattern basis.** E.17 supplies face discipline; E.17.0 supplies viewpoint/view conformance only when `U.View` membership is material.
**Builds on.** `E.17.0 U.MultiViewDescribing`; `E.17` MVPK; `A.7`; `E.10.D2`; `A.6.B`; `F.9`; `F.18`.
**Coordinates with.** `ConservativeRetextualization`; `RepresentationSchemeTransition`; `E.17.ID.CR ComparativeReviewUnit`; `A.6.4`; `A.10`; `A.15`; `A.15.4`; `B.3`; `A.20`; `A.21`; `A.2.8`; `A.2.8.PER`; `A.2.9`.

