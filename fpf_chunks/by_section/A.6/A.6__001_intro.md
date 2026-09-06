---
chunk_kind: "child"
pattern_id: "A.6"
pattern_title: "Signature Stack & Boundary Discipline"
section_id: "A.6:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6/A.6__001_intro.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "A.6 — Signature Stack & Boundary Discipline"
  - "A.6:intro — Intro"
line_start: 10149
line_end: 10236
dependencies:
  - "A.10"
  - "A.15"
  - "A.2.3"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.6"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.B"
  - "A.6.C"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.26"
  - "C.28"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.19"
  - "E.8"
  - "F.18"
  - "F.9"
  - "U.Mechanism"
  - "U.Signature"
  - "U.View"
keywords:
  - "Confuses deontics with mathematical admissibility"
  - "Rewrite as declarative predicate"
  - "Work versus non-Work effect"
  - "acceptance"
  - "actual occurrence"
  - "and evidence"
  - "atomic L/A/D/E claims"
  - "delivery"
  - "in invariants"
  - "publication face"
  - "reference predicate IDs from CC when needed"
  - "separate result"
  - "signature and mechanism declarations"
  - "six-way authority-word branch"
  - "undermines auditability"
  - "“MUST” appears inside Definition: blocks"
---

## A.6 - Signature Stack & Boundary Discipline

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Mixed (normative only where explicitly marked; claim-classification semantics live normatively in A.6.B)
> **Placement:** Part A → A.6.\* (cluster overview; coordinates A.6.0 / A.6.1 / A.6.3 / A.6.B / A.6.5 / A.6.6 / A.6.7)
> **Builds on:** E.8 (authoring template), A.6.B (Boundary Norm Square — quadrant semantics & link discipline), A.6.0 (U.Signature), A.6.1 (U.Mechanism), A.6.3 (optional source-to-receiving episteme construction), E.17.0 (viewpoint conformance and `U.View` membership), E.17 (MVPK — declared face kinds, face designators, and “no new semantics” publication), A.7 (EntityOfConcern and Description-episteme boundary; specification use and publication-carrier distinction), A.6.C, A.2.3, A.2.8, A.2.8.PER, and A.2.9 for promise-content, commitment, permission, speech-act, and dated-Work and separate result, delivery, acceptance, and evidence unpacking, F.18 only when recovered boundary terms need durable naming, E.10.D2 (EntityOfConcern and Description-episteme boundary; specification use and refinement discipline), E.10 publication face, form, unit, and carrier discipline
> **Purpose (one line):** Keep boundary claims evolvable by classifying each statement under the right layer of the Signature Stack and the right quadrant of the Boundary Norm Square (A.6.B).
>
> **Mint/reuse (terminology):** Mints “Signature Stack”, “Boundary Discipline Matrix”, and “Claim Register” as local authoring aids; reuses E.17.0 meanings of `U.View` and `U.Viewpoint`, with A.6.3 only for optional viewing construction, and uses publication face, publication form, or interop publication form terms for publication-use questions. The labels **L/A/D/E** used below are *claim-classification labels for statements*, not MVPK face designators and not pattern IDs.
>
**Canonical companion.** The square itself (quadrant definitions, form constraints, and cross‑quadrant dependency discipline) is specified normatively in **A.6.B — Boundary Norm Square**. This overview only (i) maps quadrants onto the Signature Stack, and (ii) explains how MVPK faces project the canonical L/A/D/E-classified claim set. If anything in this overview conflicts with A.6.B, **A.6.B is authoritative**.

**Use this pattern when.** Use A.6 when a boundary package, API, protocol, contract, compliance statement, SLO/SLA, connector, interface, or publication boundary mixes definitions, admissibility predicates, duties, evidence, and work effects into one account.

**What goes wrong if missed.** Boundary prose starts doing too many jobs at once: invariants are read as permissions, permissions as duties, evidence as gate passage, and publication faces as the governed boundary object.

**What this buys.** The project gets an L/A/D/E-classified claim set with stable claim IDs, source references, stack placement, and publication-face citations, so work, reliance, evidence, commitment, and gate uses can return to their subject patterns.

**Start here when.** The dominant question is an API, protocol, contract, compliance, SLO or SLA, connector, interface, or publication boundary package whose statements are mixing runtime behaviour, governance, and evidence into one undifferentiated boundary account.

**First output.** One Claim Register or equivalent L/A/D/E-classified atomic claim set with stable `L-*`, `A-*`, `D-*`, and `E-*` identifiers, stack placement, and face citations by ID rather than paraphrase.

**Boundary-claim activation discipline.** Use only as much claim-classification structure as the live work claim or reliance claim requires. Split a statement only where one sentence carries more than one claim kind, `relationFunctionClaimRef` or `authoritySourceRef`, or work or reliance consequence, or where evidence, gate, duty, assurance, work occurrence, P2W class, admissible work, or admissible reliance would otherwise remain ambiguous. For a local first-pass repair, an equivalent L/A/D/E-classified claim set may be a two-to-four-row scratch table. Use a persistent Claim Register when the claim set is reused, published, audited, release-bearing, cross-context, or relied on by `A.15`, `A.10`, `B.3`, `A.21`, `A.20`, `A.2.8`, `A.2.8.PER`, `A.2.9`, or `A.15.1`. Do not atomize ordinary modifiers when one `relationFunctionClaimRef` or `authoritySourceRef` and one work or reliance consequence are already clear.

**Typical neighboring subject patterns and authority-reference repairs.** `A.6.B` for the quadrant semantics, `A.6.C` for contract unpacking, `A.6.P`, `C.16.Q`, or `A.6.A` for lexical repair, and `E.17` faces for audience-specific publication of the same decomposed claim set.

**Common neighboring-pattern mistakes.** If the real object is still cue preservation or an early unresolved cue, use `A.16` or `A.16.1`; if a qualified relation, quality term, or action invitation is itself being repaired, apply `A.6.P`, `C.16.Q`, or `A.6.A`; if duties, commitments, promise content, work effects, and evidence are being mixed into one contract sentence, split them through `A.6.B` and `A.6.C` rather than minting one more undifferentiated contract paragraph.

**Causal/deontic split.** In “deploy because it would reduce harm”, `C.28` decides what the causal evidence supports; A.6.B separately classifies the boundary claims. If any atomic claim is permission-looking, choose one `A6-AW-*` row below. A causal-use record supplies none of those boundary claims.

**Authority-word branch (subordinate boundary-claim stress case).** When “approved”, “allowed”, “authorized”, “permitted”, or similar wording matters to action or reliance, choose one row by the claim being made—not by the visible word. These `A6-AW-*` labels are local claim-routing IDs, not new kinds.

| Branch ID | Ask this plain question | Placement and subject pattern | Stop / near-miss |
| --- | --- | --- | --- |
| `A6-AW-NORM-GRANT` | Does an exact policy prescribe an action, does one actual bearer have that duty, or may a named beneficiary perform one under stated conditions? | **D**: `A.2.8` for a generic prescription or, when separately instituted, one `U.Commitment`; `A.2.8.PER` for one `GrantedPermissionRelation@Context`, including beneficiary, action, scope/window, and policy-valid A.2.9 instituting act. | A policy sentence may state a generic prescription but by itself establishes neither an individual commitment nor a grant. |
| `A6-AW-GATE` | Does the sentence state a mechanism entry predicate, or claim one actual A.21 decision for a bounded action? | **A** for the A.6.1 entry predicate; **E** for an exact A.21 `GateDecisionResult` with its bounded action, profile application, complete required `GateCheckApplicationResult` set, decision value, consequence, scope/window, and recheck condition. | Split predicate and result into separate atomic claims. A checked grant or finding is an input; neither it nor a displayed carrier proves passage. |
| `A6-AW-EXERCISE` | Did this dated Work match the beneficiary and action of a current grant? | **E**: A.15.1 for the Work and `A.2.8.PER PermissionExerciseRelation@Context` for exercise. | A grant, plan, or green gate does not show that Work occurred or exercised it. |
| `A6-AW-WEAK` | Did a current, sufficiently complete frame find no prohibition before action or no violation in actual Work? | **E**: the exact A.2.8.PER `NonProhibitionFinding@Context` or `NonViolationFinding@Context`. | A stale or incomplete frame returns `unresolved`, not permission. |
| `A6-AW-CONFLICT` | Do a current grant and norm cover the same case, and has a rule or authorized decision selected the outcome? | **E**: `A.2.8.PER PermissionNormConflictFinding@Context` and its applicable rule or current resolution result. | A system-role kind, assignment, office, permit, or gate label alone leaves the conflict `unresolved`. |
| `A6-AW-SOURCE` | Does the sentence only say that a permit, badge, registry entry, message, or carrier exists, displays, or supports a claim? | **E** for the A.10 evidence claim; **L** only for a definition; keep the exact publication or carrier pattern. | A visible source is not a grant, gate, exercise, weak finding, or conflict resolution. |

**Concrete API/credential case.** A dashboard badge saying “API-7 approved for production” starts at `A6-AW-SOURCE`. It reaches `A6-AW-NORM-GRANT` only if a named policy-valid act instituted a current grant for a beneficiary and deployment action; the admission endpoint is separately `A6-AW-GATE`. Do not claim `A6-AW-EXERCISE` until a dated deployment Work occurrence matches that grant.

When the wording is agreement-like, use `A.6.C` to separate promise content, the instituting speech act, governance, Work, consequence, and evidence. For “recommended”, use A.16/A.6.A for a cue, `A6-AW-GATE` for an entry criterion, or A.2.8 only for recommendation-as-duty. Before any branch guides action or reliance, use A.15 to return to its exact governing claim.

**Positive repaired result.** The reader can identify the L/A/D/E job, select at most one `A6-AW-*` row for each permission-looking atomic claim, and reach the named subject pattern before acting or relying.

**Credential-currentness boundary.** A displayed credential supports only its issuer, holder, verifier, status, and currentness claims through A.10. Treat it as `A6-AW-SOURCE`; move to another row only when that row's direct object and ground are independently present.

**Register-backed status boundary.** A pass, dashboard cell, API response, or certificate view may be only a publication of a register entry. Start at `A6-AW-SOURCE`; if the governing entry has institutional force, select the one row whose object it actually creates or changes and cite that row's subject pattern. Otherwise keep only source-finding or currentness support under A.10.

**Conflicting-source boundary.** When classified boundary wording, a display, copied summary, current source, gate decision, credential status, register entry, status-source display, recency signal, or provenance label disagree, do not resolve by wording emphasis, visual salience, color, or apparent freshness. Name the source order, decision source, freshness policy, and supersession rule; until those are resolved, keep only cue use, source-finding, or bounded reversible probes available.

**Adversarial wording guard.** When authority wording is intentionally ambiguous, split the sentence, select one `A6-AW-*` row per permission-looking claim, and keep every other work, evidence, gate, or assurance use with its own source.

**Lint trigger.** In boundary, API, schema, or policy text, authority-looking wording triggers the `A6-AW-*` table. A conforming repair names the selected row and source before the claim guides work or reliance.

**Boundary and source repair assignment.** If the split exposes a missing claim or source, give that exact claim ID or selected `A6-AW-*` branch to the identified boundary or source maintainer. Keep only cue use, source-finding, or a bounded reversible probe until the source is exposed or repaired.

Practitioner prompts for boundary wording use:

| Part in the situation | Prompt |
| --- | --- |
| Boundary author | Which words need L/A/D/E claim IDs before they can guide work or reliance? |
| Policy, API, or schema maintainer | Which `L-*`, `A-*`, `D-*`, and `E-*` claims must be separated, and which source carries each one? |
| Acting user | Is the wording only a cue or source-finding handle, or is there a support relation named by value for the required source-backed claim or effect? |
| Claim or source maintainer | Which source is missing for the selected `A6-AW-*` branch or other L/A/D/E claim, and what must be repaired there? |
| Auditor or reviewer | Which L/A/D/E claim IDs are cited by each publication face, and where would paraphrase drift change the allowed use? |

**Recurring boundary ambiguity repair.** If the same wording repeatedly needs the same split, repair the boundary package: replace the misleading label, expose the L/A/D/E claim IDs, and cite the source for the selected `A6-AW-*` branch. Repetition is a source defect, not a normal per-use burden.

Display guidance for boundary wording: a publication face, API page, or credential display should expose the relevant L/A/D/E claim IDs and the source for the selected `A6-AW-*` branch. If it cannot, keep the wording at `A6-AW-SOURCE` or repair the boundary package.

Incident-learning fields for boundary wording overread: displayed phrase, intended next work occurrence or reliance use, required source-backed claim or effect, missing or ambiguous L/A/D/E claim ID, exact `L-*`, `A-*`, `D-*`, or `E-*` source needed, plausible overread, safe disposition used now, and upstream repair item for labels, L/A/D/E claim IDs, source refs, currentness refs, supersession refs, or publication-face wording.

**Conventions:** The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **MAY**, and **SHALL** are to be interpreted as in RFC 2119/8174. Lower-case `must`, `may`, and `should` in explanatory prose is descriptive, not normative.

**Statement identifiers (recommended):** Adopt the quadrant‑prefixed ID scheme from **A.6.B:0** for classifiable statements:
`L-*` (law or definition), `A-*` (admissibility gate), `D-*` (deontic or commitment), `E-*` (effect or evidence).
Other sections and faces **SHOULD** refer to these IDs instead of restating the same constraint in new words.
IDs are intended to be “lintable” identifiers (and are especially useful when D‑duties enforce A‑gates or E‑claims). Consider pairing IDs with a lightweight Claim Register (A.6.B:7) to reduce paraphrase drift across faces.
**Non-collision note (informative):** The `A-*` prefix here is “Admissibility”, not Part‑A numbering and not MVPK’s `AssuranceLane` face kind. If this is a readability hazard in your program, prefer an explicit `G-*` (“Gate”) local convention while keeping the quadrant name “Admissibility”.

**Admissibility-predicate distinction (informative):** An `A-*` claim is a mechanism admissibility predicate or entry condition inside the L/A/D/E-classified boundary claim set. It is not an A.21 `GateDecisionResult`, `GateCheckApplicationResult`, optional `GateCheckRef`, optional `DecisionLog`, or proof that a gate passed. An `A-*` claim may name conditions consumed by a later A.21 profile application; actual passage is a separate `E-*` claim about the exact `GateDecisionResult`. An A.20 `ConstraintValidity` witness remains separate from the predicate, each check application, and the gate result.

**Claim Register (informative, recommended).** Use the Claim Register mini‑record in **A.6.B:7**. In this cluster the register is additionally used to record stack placement (Signature, Mechanism, Norms, and Evidence) and the MVPK faces that cite each claim (`viewRef`/`viewpointRef`), so “no paraphrase drift” can be audited mechanically.

