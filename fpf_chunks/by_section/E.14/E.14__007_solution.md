---
chunk_kind: "child"
pattern_id: "E.14"
pattern_title: "Human-Centric Working-Model: Readable Claims and Recoverable Assurance"
section_id: "E.14:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.14/E.14__007_solution.md"
commit_sha: "423f9d3fef92bafec7b092b910e8ce056a0f607d"
heading_path:
  - "E.14 — Human-Centric Working-Model: Readable Claims and Recoverable Assurance"
  - "E.14:4 — Solution"
line_start: 112783
line_end: 112861
dependencies:
  - "B.3.5"
  - "C.13"
  - "C.2.3"
  - "E.10"
  - "E.7"
  - "E.8"
keywords:
---

### E.14:4 - Solution

#### E.14:4.1 - Human-Centric principles

##### E.14:4.1.1 - Recognition text and assurance text
Keep the target assertion, its EntityOfConcern and its scope recoverable in both recognition and assurance. A supporting premise may concern a part, another kind of subject or another model. Show which relation lets the reader use that premise for the original assertion and under which conditions it holds.

If the pattern distinguishes an EntityOfConcern, the interpretive or operational move applied to that object, and the wider review or work process around it, the text should distinguish them explicitly instead of changing nouns as though the object, move and work were interchangeable.

Begin the Working-Model text in the subject domain. If a pattern is meant to help with a review, design, cultural, research, or operational problem, the recognition text should open from that problem-owning moment before internal taxonomy or package architecture.

If a broader umbrella and a narrower working branch are both live, say plainly what each names, what object is being discussed, what move the reader makes, and what wider work remains outside.

**Recognition text** and **assurance text** name two reading-order text blocks inside one pattern.

For human-facing canonical patterns, Working-Model-first discipline should appear in a two-part reading order.
The **recognition text** is the working text that a cold practitioner, manager, or researcher should be able to understand first: what situation this pattern is for, what it buys, what it is not for, and what ordinary mistake it helps prevent.
The **assurance text** is the heavier text that carries declaration, object discipline, modeling lens, law, return conditions, and other assurance work.

The assurance text may justify, tighten, or audit the working text, but it must not silently replace or strengthen the recognition-text claim.

Keep the target assertion, its subject and its scope visible through both blocks. Supporting premises may concern other subjects. For Pump-37, calibration of the instrument and the measurement Work can support the vibration reading at 09:00. That reading answers a request for the vibration value at 09:00. To report that a fresh measurement was taken, or that this station performed it, establish the corresponding performance. A service decision also needs the applicable criterion and operating conditions. A conclusion about a fleet needs grounds covering the relevant pumps.
Where episteme-publication-heavy or transform-heavy patterns need a compact ontological account, the assurance text should expose three things explicitly:
- the ontic target or EntityOfConcern;
- the modeling substrate or mathematical lens when one is load-bearing;
- the publication face or working text by which the claim is presented.

Present the Working-Model text first. Readers can consult the assurance text underneath when they need to inspect a claim's grounds. That text remains available for audit.

When empirical evaluation is current, put the ordinary subject claim first. Keep a proposed evaluation distinct from completed performance; use `U.WorkPlan` when the receiving question requires coordination of future Work, and retain the actual Method and any relied-on MethodDescription edition.

When a claim asserts or relies on a dated evaluation Work, recover its required performer basis under A.13 and independently admit the Work under A.15.1.

Add F.6 when precise assignment-bound attribution is consumed, keeping the assignment and any local system-role-kind classification independently grounded.

An ordinary result may omit identifiers it does not consume while keeping all facts needed for its use recoverable.
> **E.14-P.1 – Working-Model first, assurance when current.**
> State the direct claim in one **Working-Model** for human-facing discussion. The reader can stop when that claim and its ordinary explanation answer the commissioned question. Supply additional grounds when the reader needs them to understand, choose or act. Add the formal assurance called for by the publication or current requirement.
>
> When assurance is current, declare only the posture and forms of support required by the applicable pattern: **Mapping** to align a term with the chosen model value it names; **Logical** to state label meaning, scope, constraints, and limits; **Constructive** to make independently grounded construction facts inspectable; or **Empirical Validation** to support a bounded reliance on a domain result.
>
> Under `B.3.5`, covered claims declare `validationMode`.
>
> For each selected shoulder, name only the objects, scope, and qualification window the current use consumes. None creates the model value, subject relation, Work occurrence, or result it supports.

> **E.14‑P.2 – Downward‑only dependency.**
> Keep assurance apparatus subordinate to the readable Working-Model claim: its notation and record structure do not define the public vocabulary.
>
> This presentation rule does not prevent correction. If a proof, trace, or empirical result exposes a false or overbroad claim, revise the Working-Model claim and any affected wording under the direct governing pattern; do not silently leave the recognition text asserting the defeated claim.
>
> **E.14‑P.3 – Small working text, big proof.**
> The Working-Model exposes a **small set** of names chosen through E.10's Plain and Tech registers for the intended reader, and a compact family of relations used in everyday reasoning; the assurance text makes their meanings, basis, limits, and support inspectable below.

> **E.14‑P.4 – Human registers first.**
> Terms in the Working‑Model are chosen for **human legibility** (register‑badged, synonym‑aware). Synonym capture and language variance belong to Mapping; **only the chosen canonical label appears in the Working-Model text**.

> **E.14-P.5 – Required assurance postures are explicit.**
> A Working-Model relation covered by an elected `B.3.5` profile **declares** `validationMode ∈ {axiomatic, inferential, postulate}`. Another named current assurance requirement may require its own declared posture. A direct relation outside such a profile needs no E.14 assurance field.
> _axiomatic_ means that the author relies on the linked construction account required by the elected branch; _inferential_ means that the author relies on a followable reasoned chain.
>
> Under `B.3.5`, a permitted _postulate_ is a scoped pragmatic claim linked to an admissible evidence object, with empirical challenge cues.
>
> Follow another elected profile's own requirements. Empirical Validation may accompany any permitted posture when observation supplies the needed support; a posture declaration does not itself establish performed evaluation.

> **E.14‑P.6 – Parsimony in the working text.**
> No new Working‑Model relation types are introduced if the existing Logical label-meaning rules plus Constructive grounding suffice to capture the intended meaning.

> **E.14‑P.7 – A postulate is not completed evaluation.**
> Under an elected `B.3.5` postulate branch, authors **SHALL** state the claim and scope, link the admissible evidence object, and give the profile's empirical challenge cues.
>
> That requirement does not by itself assert a new evaluation Work. When reliance consumes an actual evaluation or measurement result, keep its necessary subject, scope, result and source grounds recoverable.
>
> Identify dated Work, performers, Method, bindings, result episteme and qualification window where the claim or applicable profile depends on them.
>
> Use A.10 when the source-to-use relationship must be made explicit or replayable, retaining already sufficient direct support; use F.6 for consumed assignment-bound attribution and B.3 for a current assurance claim. Each remains governed by its own conditions.

> **E.14‑P.8 – Explain what the working model lets the reader decide.**
> When a pattern claims a Working‑Model benefit, it **SHALL** state the problem and give the grounds the reader needs to recognize it, use the model’s distinctions and know when the decision also needs assurance. A direct account, a comparison or a worked case can supply those grounds under E.7. Preserve the part of the explanation on which the reader’s judgement depends.

