---
chunk_kind: "child"
pattern_id: "A.6"
pattern_title: "Signature Stack & Boundary Discipline"
section_id: "A.6:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6/A.6__001_intro.md"
commit_sha: "ef9ded2cb965193aa2484c84f06d65770439cef8"
heading_path:
  - "A.6 — Signature Stack & Boundary Discipline"
  - "A.6:intro — Intro"
line_start: 10134
line_end: 10208
dependencies:
  - "A.10"
  - "A.15"
  - "A.2.8.PER"
  - "A.6"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.5"
  - "A.6.6"
  - "A.6.B"
  - "A.6.C"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.26"
  - "C.28"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.19"
  - "E.8"
  - "F.18"
  - "F.9"
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
  - "reference predicates by ID or canonical location from CC when needed"
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
> **Builds on:** A.6.B for claim classification, A.6.0 and A.6.1 for declaration boundaries, A.7 for subject/description/carrier distinctions, and E.17.0/E.17 for view membership and publication.
> **Purpose (one line):** Keep boundary claims evolvable by classifying each statement under the right layer of the Signature Stack and the right quadrant of the Boundary Norm Square (A.6.B).
>
> **Local terminology:** “Signature Stack”, “Boundary Discipline Matrix”, and “Claim Register” name authoring aids. **L/A/D/E** classify statements; they are not MVPK face designators or pattern IDs.
>
**Canonical companion.** The square itself (quadrant definitions, form constraints, and cross‑quadrant dependency discipline) is specified normatively in **A.6.B — Boundary Norm Square**. This overview only (i) maps quadrants onto the Signature Stack, and (ii) explains how MVPK faces project the canonical L/A/D/E-classified claim set. If anything in this overview conflicts with A.6.B, **A.6.B is authoritative**.

**Use this pattern when.** Use A.6 when a boundary package, API, protocol, contract, compliance statement, SLO/SLA, connector, interface, or publication boundary mixes definitions, admissibility predicates, duties, evidence, and work effects into one account.

**What goes wrong if missed.** Boundary prose starts doing too many jobs at once: invariants are read as permissions, permissions as duties, evidence as gate passage, and publication faces as the governed boundary object.

**What this buys.** The project gets an L/A/D/E-classified claim set with source references and stack placement. Material dependencies name the source claim by ID or canonical location, so work, reliance, evidence, commitment, and gate uses can return to their subject patterns; publication faces cite the same claims.


**First output.** One or more atomic L/A/D/E-classified claims, with stack placement and references for material dependencies.

**Boundary-claim activation discipline.** Use only as much claim-classification structure as the live work claim or reliance claim requires. Split a statement only where one sentence carries more than one claim kind, `relationFunctionClaimRef` or `authoritySourceRef`, or work or reliance consequence, or where evidence, gate, duty, assurance, work occurrence, P2W class, admissible work, or admissible reliance would otherwise remain ambiguous. For a local first-pass repair, ordinary atomic prose suffices; a two-to-four-row scratch table may help. Use a persistent Claim Register when stable claim references are needed for reuse, publication, audit, release, cross-context use, or reliance by `A.15`, `A.10`, `B.3`, `A.21`, `A.20`, `A.2.8`, `A.2.8.PER`, `A.2.9`, or `A.15.1`. Do not atomize ordinary modifiers when one `relationFunctionClaimRef` or `authoritySourceRef` and one work or reliance consequence are already clear.

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

When agreement-like wording leaves an ambiguity that changes interpretation or use, use `A.6.C` to separate promise content, the instituting speech act, governance, Work, consequence, and evidence. For “recommended”, use A.16/A.6.A for a cue, `A6-AW-GATE` for an entry criterion, or A.2.8 only for recommendation-as-duty. Before action or reliance, return to the exact governing claim. Use A.15.4 while appearance hides the required prerequisite; use A.15 when the question is enactment alignment.


**Credential-currentness boundary.** Use A.10 to determine which claims a displayed credential's source and evidence support for the bounded use. Recover issuer, holder, verifier, status and currentness where they matter. Treat the display as `A6-AW-SOURCE`; move to another row only when that row's direct object and ground are independently present.

**Register-backed status boundary.** A pass, dashboard cell, API response, or certificate view may be only a publication of a register entry. Start at `A6-AW-SOURCE`; if the governing entry has institutional force, select the one row whose object it actually creates or changes and cite that row's subject pattern. Otherwise keep only source-finding or currentness support under A.10.

**Conflicting-source boundary.** When a classified boundary claim disagrees with its governing source or a display, resolve the source order, decision source, freshness policy and supersession rule. Until then, keep cue use or source-finding available; allow a bounded reversible probe only on its own adequate basis, without relying on the unsupported claim.



**Boundary and source repair assignment.** If the split exposes a missing claim or source, give the claim ID or canonical location, or the selected `A6-AW-*` branch to the identified boundary or source maintainer. Keep cue use or source-finding available. A bounded reversible probe needs its own adequate basis; the missing source still blocks the unsupported Work or reliance use.


**Recurring boundary ambiguity repair.** If the same wording repeatedly needs the same split, repair the boundary package: replace the misleading label, identify the L/A/D/E claims by ID or canonical location, and cite the source for the selected `A6-AW-*` branch. Repetition is a source defect, not a normal per-use burden.

Display guidance for boundary wording: a publication face, API page, or credential display should identify the relevant L/A/D/E claims by ID or canonical location and the source for the selected `A6-AW-*` branch. If it cannot, keep the wording at `A6-AW-SOURCE` or repair the boundary package.

For an incident-learning use, record the displayed phrase, intended Work or reliance use, unsupported claim or effect, missing or ambiguous L/A/D/E claim ID or canonical location, required source, plausible overread, safe disposition and upstream repair. Retain source, currentness and supersession references only where they change that case.

**Conventions:** The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **MAY**, and **SHALL** are to be interpreted as in RFC 2119/8174. Lower-case `must`, `may`, and `should` in explanatory prose is descriptive, not normative.

**Statement identifiers (recommended):** Adopt the quadrant‑prefixed ID scheme from **A.6.B:0** for classifiable statements:
`L-*` (law or definition), `A-*` (admissibility gate), `D-*` (deontic or commitment), `E-*` (effect or evidence).
Other sections and faces **SHOULD** cite the canonical claim ID or location. Face prose may explain or faithfully paraphrase the claim without creating another specification.
IDs are intended to be “lintable” identifiers (and are especially useful when D‑duties enforce A‑gates or E‑claims). Consider pairing IDs with a lightweight Claim Register (A.6.B:7) to reduce paraphrase drift across faces.
**Non-collision note (informative):** The `A-*` prefix here is “Admissibility”, not Part‑A numbering and not MVPK’s `AssuranceLane` face designator. If this is a readability hazard in your program, prefer an explicit `G-*` (“Gate”) local convention while keeping the quadrant name “Admissibility”.

**Admissibility-predicate distinction (informative):** An `A-*` claim is a mechanism admissibility predicate or entry condition inside the L/A/D/E-classified boundary claim set. It is not an A.21 `GateDecisionResult`, `GateCheckApplicationResult`, optional `GateCheckRef`, optional `DecisionLog`, or proof that a gate passed. An `A-*` claim may name conditions consumed by a later A.21 profile application; actual passage is a separate `E-*` claim about the exact `GateDecisionResult`. An A.20 `ConstraintValidity` witness remains separate from the predicate, each check application, and the gate result.

**Claim Register (informative, recommended).** When a Claim Register is useful, use the mini-record in **A.6.B:7**. It can record stack placement (Signature, Mechanism, Norms, and Evidence) and the face designators that cite each claim. Add `viewRef`/`viewpointRef` only when the corresponding episteme identities matter. Mechanical checks can test ID resolution and exact text copying; inspect meaning for paraphrase drift.

