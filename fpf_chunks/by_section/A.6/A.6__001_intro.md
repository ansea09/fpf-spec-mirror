---
chunk_kind: "child"
pattern_id: "A.6"
pattern_title: "Signature Stack & Boundary Discipline"
section_id: "A.6:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6/A.6__001_intro.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "A.6 — Signature Stack & Boundary Discipline"
  - "A.6:intro — Intro"
line_start: 6805
line_end: 6877
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.20"
  - "A.21"
  - "A.6"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.B"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.26"
  - "C.26.1"
  - "C.28"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.EFP"
  - "E.19"
  - "E.8"
  - "F.18"
  - "F.9"
  - "U.EpistemicViewing"
  - "U.Mechanism"
  - "U.MultiViewDescribing"
  - "U.Signature"
  - "U.View"
  - "U.Viewpoint"
  - "U.Work"
keywords:
  - "A.6.B L/A/D/E claims"
  - "Confuses deontics with mathematical admissibility"
  - "Rewrite as declarative predicate"
  - "authority-wording split"
  - "boundary"
  - "boundary claim-classification fields"
  - "in invariants"
  - "probe/order/frame/export/state-reading claims"
  - "promise/commitment/API/policy wording"
  - "reference predicate IDs from CC when needed"
  - "register-backed status boundary"
  - "signature stack"
  - "undermines auditability"
  - "“MUST” appears inside Definition: blocks"
---

## A.6 - Signature Stack & Boundary Discipline

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Mixed (normative only where explicitly marked; claim-classification semantics live normatively in A.6.B)
> **Placement:** Part A → A.6.\* (cluster overview; coordinates A.6.0 / A.6.1 / A.6.3 / A.6.B / A.6.5 / A.6.6 / A.6.7)
> **Builds on:** E.8 (authoring template), A.6.B (Boundary Norm Square — quadrant semantics & link discipline), A.6.0 (U.Signature), A.6.1 (U.Mechanism), A.6.3 (U.EpistemicViewing — views as episteme-lane projections under viewpoints), E.17.0 (U.MultiViewDescribing), E.17 (MVPK — fixed face kinds & “no new semantics” publication), A.7 (Object≠Description≠Carrier), F.18 (promise/utterance/commitment), E.10.D2 (I/D/S vs Surface), E.10/L‑SURF (Surface token discipline)
> **Purpose (one line):** Keep boundary claims evolvable by classifying each statement under the right layer of the Signature Stack and the right quadrant of the Boundary Norm Square (A.6.B).
>
> **Mint/reuse (terminology):** Mints “Signature Stack”, “Boundary Discipline Matrix”, and “Claim Register” as local authoring aids; reuses existing FPF meanings of `U.View`/`U.Viewpoint` (E.17.0/A.6.3) and reserves “Surface” for PublicationSurface or InteropSurface (L‑SURF). The labels **L/A/D/E** used below are *claim-classification labels for statements*, not MVPK face kinds and not pattern IDs.
>
**Canonical companion.** The square itself (quadrant definitions, form constraints, and cross‑quadrant dependency discipline) is specified normatively in **A.6.B — Boundary Norm Square**. This overview only (i) maps quadrants onto the Signature Stack, and (ii) explains how MVPK faces project the canonical L/A/D/E-classified claim set. If anything in this overview conflicts with A.6.B, **A.6.B is authoritative**.

**Start here when.** The dominant question is an API, protocol, contract, compliance, SLO/SLA, connector, interface, or publication boundary package whose statements are mixing runtime behaviour, governance, and evidence into one undifferentiated boundary account.

**First output.** One Claim Register or equivalent L/A/D/E-classified atomic claim set with stable `L-*`, `A-*`, `D-*`, and `E-*` identifiers, stack placement, and face citations by ID rather than paraphrase.

**Boundary-claim load posture.** Use only as much claim-classification structure as the live work claim or reliance claim requires. Split a statement only where one sentence carries more than one claim kind, `governingPatternRef` or `authoritySourceRef`, or work or reliance consequence, or where evidence, gate, duty, assurance, work occurrence, P2W class, admissible work, or admissible reliance would otherwise remain ambiguous. For a local first-pass repair, an equivalent L/A/D/E-classified claim set may be a two-to-four-row scratch table. Use a persistent Claim Register when the claim set is reused, published, audited, release-bearing, cross-context, or relied on by `A.15`, `A.10`, `B.3`, `A.21`, `A.20`, `A.2.8`, `A.2.9`, or `A.15.1`. Do not atomize ordinary modifiers when one `governingPatternRef` or `authoritySourceRef` and one work or reliance consequence are already clear.


**Typical neighboring governing patterns and authority-reference repairs.** `A.6.B` for the quadrant semantics, `A.6.C` for contract unpacking, `A.6.P`, `A.6.Q`, or `A.6.A` for lexical repair, and `E.17` faces for audience-specific publication of the same decomposed claim set.

**Common neighboring-pattern mistakes.** If the real object is still cue preservation or an early candidate-route cue, use `A.16` or `A.16.1`; if a qualified relation, quality term, or action invitation is itself being repaired, apply `A.6.P`, `A.6.Q`, or `A.6.A`; if agent duties are being mixed into one contract sentence, split them through `A.6.B` rather than minting one more contract-soup paragraph.

**Causal/deontic split.** A mixed boundary sentence such as "deploy because it would reduce harm" is not settled by one hidden pattern. `C.28` carries the causal-use question, `CausalityLadderRung`, estimand, support basis, support verdict, and supported causal use and unsupported causal use. `A.6.B` classifies deontic duties, boundary admissibility gates, and work-effects as atomic `L/A/D/E` claims. `A.6.C` unpacks contract, promise, commitment, utterance, and boundary-publication language when the sentence is agreement-like or release-facing. A causal support record does not by itself create a duty, commitment, promise, release gate, or boundary admissibility predicate.

**Authority wording split (subordinate boundary-claim stress case).** When a boundary, policy, API, schema, connector, or compliance statement uses "approved", "allowed", "authorized", "guaranteed", "certified", "recommended", or equivalent wording, do not decide by the word. The object under repair is still the L/A/D/E-classified boundary claim set: split the statement into `A.6.B` `L-*` definition or invariant claims, `A-*` admissibility or gate claims, `D-*` commitment claims, and `E-*` evidence or work-effect claims before treating it as action guidance. When "guaranteed", "promise", "contract", "SLA", "SLO", or certified-under-agreement wording is agreement-like, service-facing, promise-bearing, or release-facing, unpack promise content, utterance package, deontic commitment, and work or evidence substrate through `A.6.C`, `A.2.3`, `A.2.8`, and `A.2.9` before using the L/A/D/E-classified claims. When "recommended" wording is cue preservation, advice, or action invitation, apply `A.16`, `A.16.1`, or `A.6.A` according to the live kind; when it is an admissibility criterion, use the `A-*` claim and any live `A.21` gate decision; when it is evidence-supported advice, use the `E-*` claim plus `A.10`; only recommendation-as-duty uses a `D-*` claim and `A.2.8`. If the encountered item is a dashboard or status display rather than boundary prose, do not turn color, label, or visible status into an `A-*` admissibility claim; return through `A.15`, `A.10`, and, when a gate decision is live, `A.21`. If the split result will guide work, release, permission, role or status reliance, evidence reliance, or assurance, return through `A.15` to the governing FPF pattern and exact project-side FPF kind and reference that carry the live claim or effect.

**Positive repaired path.** A repaired boundary statement is not merely "less vague"; it is an L/A/D/E-classified claim set that tells the user which statement is definitional, which is an admissibility predicate, which is a deontic commitment, which is an evidence or work-effect claim, and which FPF pattern or exact project-side FPF kind and reference must be cited before the work claim or reliance claim is used.

**Credential-currentness boundary.** A displayed credential can support only issuer, holder, verifier, status, and currentness claims after an `A.10` evidence path verifies it for the relying context. Boundary permission, admissibility, authorization, deontic commitment, role or status effect, or gate passage still needs the exact `A.6.B`, `A.2.8`, `A.2.9`, `A.2.1`, or `A.21` source.

**Register-backed status boundary.** A pass, badge, dashboard cell, API response, certificate view, or other status-looking item may be only a publication of a governing register entry or status-source entry. If that register entry is the source that creates or changes permission, role or status, duty, or gate state in the bounded context, cite that exact register entry or status-source entry and split the created claims through `A.6.B`, `A.2.1`, `A.2.8`, `A.2.9`, or `A.21`. If the item is only an extract, cache, screenshot, certificate view, or convenience display, keep it as source-finding or currentness support under `A.10` until the exact source is recoverable.

**Conflicting-source boundary.** When routed boundary wording, a display, copied summary, current source, gate decision, credential status, register entry, status-source display, recency signal, or provenance label disagree, do not resolve by wording emphasis, visual salience, color, or apparent freshness. Name the source order, decision source, freshness policy, and supersession rule; until those are resolved, keep only cue use, source-finding, or bounded reversible probes available.

**Adversarial wording guard.** Do not let intentionally ambiguous "allowed", "approved", "authorized", "certified", "recommended", or "guaranteed" wording collapse `L-*`, `A-*`, `D-*`, and `E-*` claims. Split the boundary statement first, then cite the exact supporting source for the live work use, reliance use, evidence use, gate use, commitment use, or assurance use.

**Lint trigger.** In boundary, API, schema, or policy text, `approved`, `authorized`, `allowed`, `guaranteed`, `certified`, or `recommended` should trigger the A.6 split: identify the `L-*`, `A-*`, `D-*`, and `E-*` claims, then cite the exact source before work use, reliance use, evidence use, gate use, commitment use, or assurance use.


**Boundary and source repair assignment.** If splitting boundary wording exposes a missing or broken `L-*`, `A-*`, `D-*`, or `E-*` source, assign repair to the accountable boundary-maintenance or source-maintenance role assignment: boundary author, policy or schema maintainer, gate source, commitment source, evidence-carrier source, or publication face maintainer. Keep only cue use, source-finding, or bounded reversible use available until that source is exposed or repaired.

Role prompts for boundary wording use:

| Role in the situation | Prompt |
| --- | --- |
| Boundary author | Which words need L/A/D/E claim IDs before they can guide work or reliance? |
| Policy/API/schema maintainer | Which `L-*`, `A-*`, `D-*`, and `E-*` claims must be separated, and which source carries each one? |
| Acting user | Is the wording only a cue or source-finding handle, or is there exact routed support for the required source-backed claim or effect? |
| Gate, commitment, or evidence source | Which gate decision, commitment, speech act, evidence path, or work-effect source must be exposed or repaired? |
| Auditor/reviewer | Which L/A/D/E claim IDs are cited by each publication face, and where would paraphrase drift change the allowed use? |

**Recurring boundary ambiguity repair.** If the same boundary, API, schema, or interface wording repeatedly needs the same split or source recovery, repair the boundary package rather than making each user reinterpret it: replace misleading labels, expose L/A/D/E claim IDs, cite the gate source, commitment source, evidence source, or work-effect source, add currentness or supersession refs, or remove the phrase that invites unsupported work claims or reliance claims. Repetition is a signal that the boundary source or publication face needs repair, not a normal per-use task.

Display guidance for boundary wording: a publication face, API doc, schema page, connector card, or compliance statement that uses approval-, authorization-, permission-, recommendation-, certification-, or guarantee-like wording should expose the `L-*`, `A-*`, `D-*`, and `E-*` claim IDs, the source for each live work claim or reliance claim, freshness and supersession refs where currentness matters, and unsupported work claims, reliance claims, or effects. If it cannot expose those, keep the wording as source-finding or repair the boundary package.

Incident-learning fields for boundary wording overread: displayed phrase, intended next work move or reliance move, required source-backed claim or effect, missing or ambiguous L/A/D/E claim ID, exact `L-*`, `A-*`, `D-*`, or `E-*` source needed, plausible overread, safe disposition used now, and upstream repair item for labels, L/A/D/E claim IDs, source refs, currentness refs, supersession refs, or publication-face wording.


**Conventions:** The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **MAY**, and **SHALL** are to be interpreted as in RFC 2119/8174. Lower‑case “must/may/should” in explanatory prose is descriptive, not normative.

**Statement identifiers (recommended):** Adopt the quadrant‑prefixed ID scheme from **A.6.B:0** for routable statements:
`L-*` (law/definition), `A-*` (admissibility gate), `D-*` (deontic/commitment), `E-*` (effect/evidence).
Other sections and faces **SHOULD** refer to these IDs instead of restating the same constraint in new words.
IDs are intended to be “lintable” anchors (and are especially useful when D‑duties enforce A‑gates or E‑claims). Consider pairing IDs with a lightweight Claim Register (A.6.B:7) to reduce paraphrase drift across faces.
**Non-collision note (informative):** The `A-*` prefix here is “Admissibility”, not Part‑A numbering and not MVPK’s `AssuranceLane` face kind. If this is a readability hazard in your program, prefer an explicit `G-*` (“Gate”) local convention while keeping the quadrant name “Admissibility”.

**Admissibility-predicate distinction (informative):** An `A-*` claim is a mechanism admissibility predicate or entry condition inside the L/A/D/E-classified boundary claim set. It is not an `A.21` `GateDecision`, `DecisionLogRef`, or proof that a gate passed. An `A-*` claim may name a condition that a later `A.21` gate evaluates; actual gate passage needs the `A.21` source. An `A.20` `ConstraintValidity` witness remains separate from both the predicate and the gate decision.

**Claim Register (informative, recommended).** Use the Claim Register mini‑record in **A.6.B:7**. In this cluster the register is additionally used to record stack placement (Signature/Mechanism/Norms/Evidence) and the MVPK faces that cite each claim (`viewRef`/`viewpointRef`), so “no paraphrase drift” can be audited mechanically.


