---
chunk_kind: "child"
pattern_id: "E.14"
pattern_title: "Human‑Centric Working‑Model"
section_id: "E.14:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.14/E.14__007_solution.md"
commit_sha: "5801dc610c657ac7b1efee349b18e80ce6d7df6f"
heading_path:
  - "E.14 — Human‑Centric Working‑Model"
  - "E.14:4 — Solution"
line_start: 77419
line_end: 77470
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

Working-Model-first drafting therefore also means subject-domain-first drafting. If a pattern is meant to help with a real review, design, cultural, research, or operational problem, the recognition text should open from that problem-owning moment before internal taxonomy or package architecture. If a broader umbrella and a narrower working branch are both live, say plainly what each names, what object is being discussed, what move the reader makes, and what wider work remains outside.

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

When empirical evaluation is current, keep the same reading order. Put the ordinary subject claim first. Keep an intended evaluation in its `U.WorkPlan`, name the selected `U.Method`, and cite a `U.MethodDescription` only when the plan, execution claim, or interpretation relies on that edition. If evaluation actually occurs, point to its complete A.15.1/F.6 basis. In the assurance account, name every performer, the assignment link checked with F.6, and the Method the Work enacted; use A.2.1 for the assignment itself and test any local system-role-kind classification separately. The first sentence may omit identifiers or basis details it does not use, provided the facts remain recoverable. Only the performer System acts. A working model, pattern, plan, criterion, Method, MethodDescription, assignment, record, result, evidence path, provenance value, or assurance claim does not become Work, and its availability does not make Work occur.
> **E.14-P.1 – Working-Model first, assurance when current.**
> Operate one **Working-Model** for all human-facing discussion and state the direct claim first. If neither the publication nor a named current requirement calls for assurance, the author may stop there. When assurance is current, declare only the posture and shoulder or shoulders required by the applicable pattern: **Mapping** to align a term with the chosen model value it names; **Logical** to state label meaning, scope, constraints, and limits; **Constructive** to make independently grounded construction facts inspectable; or **Empirical Validation** to support a bounded reliance on a domain result. Under `B.3.5`, covered claims declare `validationMode`. For each selected shoulder, name only the objects, scope, and qualification window the current use consumes. None creates the model value, subject relation, Work occurrence, or result it supports.

> **E.14‑P.2 – Downward‑only dependency.**
> Information **may** flow from the Working‑Model down into any Assurance layer; **no Assurance layer may impose vocabulary or shape back upward** into the Working‑Model.
>
> **E.14‑P.3 – Small working text, big proof.**
> The Working-Model exposes a **minimal set** of names in the L-1 and L-2 registers and a compact family of relations used in everyday reasoning; the assurance text makes their meanings, basis, limits, and support inspectable below.

> **E.14‑P.4 – Human registers first.**
> Terms in the Working‑Model are deliberately curated for **human legibility** (register‑badged, synonym‑aware). Synonym capture and language variance belong to Mapping; **only the chosen canonical label appears in the Working-Model text**.

> **E.14-P.5 – Required assurance postures are explicit.**
> A Working-Model relation covered by an elected `B.3.5` profile **declares** `validationMode ∈ {axiomatic, inferential, postulate}`. Another named current assurance requirement may require its own declared posture. A direct relation outside such a profile needs no E.14 assurance field.
> _axiomatic_ means that the author relies on one linked Constructive account for this assertion; _inferential_ means that the author relies on a reasoned chain; _postulate_ means that the assertion remains a pragmatic working claim within a stated scope. For a postulate, the author should add brief empirical cues that show where the claim tends to hold or what would challenge it. The posture alone establishes no evaluation Work and no result. Empirical Validation may accompany any posture when observation is the right support. Mapping, Logical, Constructive, and Empirical assurance remain separate from the claim's direct ontology and from the currentness of every record involved.

> **E.14‑P.6 – Parsimony in the working text.**
> No new Working‑Model relation types are introduced if the existing Logical label-meaning rules plus Constructive grounding suffice to capture the intended meaning.

> **E.14‑P.7 – A postulate is not completed evaluation.**
> When *postulate* is chosen, authors **SHALL** state the claim and its scope and **SHOULD** give brief empirical cues — where it tends to hold or what would challenge it — to ease later validation. This posture by itself requires no dated Work, result, complete A.15.1/F.6 basis, provenance path, or assurance claim. If evaluation or measurement actually occurred and the current assurance use relies on its result, authors **SHALL** name the scope and qualification window that use consumes, the domain result and result episteme, and the A.10 evidence-provenance relation; they keep the complete A.15.1/F.6 basis recoverable under §5.5. If an assurance claim is made or B.3's material-reliance threshold is met, the current B.3 assurance claim remains separate and required for that assurance-bearing use. Another named current assurance requirement supplies its own obligations.

> **E.14‑P.8 – Working-model-first is not explanation-thin.**
> Human-facing parsimony does **not** license under-explained pattern prose. When a pattern claims a Working‑Model benefit, it **SHALL** still provide enough problem framing, rationale, and worked slices that readers can tell what the model clarifies, what remains on the assurance shoulders, and when a heavier review path is required.

