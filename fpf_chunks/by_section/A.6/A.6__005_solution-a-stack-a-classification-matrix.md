---
chunk_kind: "child"
pattern_id: "A.6"
pattern_title: "Signature Stack & Boundary Discipline"
section_id: "A.6:4"
section_title: "Solution — A stack + a classification matrix"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6/A.6__005_solution-a-stack-a-classification-matrix.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "A.6 — Signature Stack & Boundary Discipline"
  - "A.6:4 — Solution — A stack + a classification matrix"
line_start: 9344
line_end: 9581
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

### A.6:4 - Solution — A stack + a classification matrix

#### A.6:4.1 - Why “stack”: what is stacked, and what “higher and lower” means

This pattern uses **stack** in the same pragmatic sense as other FPF stacks (e.g., the holonic import stack and other layered disciplines): an ordered set of layers where **higher layers are more stable commitments**, and **lower layers are more volatile realizations and evidence**. “Higher” and “lower” are not metaphysical claims; they are **engineering guidance for evolvability**:

* **Higher in the stack** = closer to *public, reusable boundary intent*.
* **Lower in the stack** = closer to *execution, implementation, and evidence* (what is actually done and observed).

This is consistent with existing “stack discipline” uses in FPF (e.g., import layering over holonic strata).

The **Signature Stack** (as used in this cluster) is the ordered family of **canonical claim layers** for a boundary package. Each layer is a stable canonical placement for one quadrant of statements (L/A/D/E), with a canonical boundary publication form or section that carries those statements:

1. **Signature layer (L: laws or definitions).** `U.Signature` provides the stable declarative boundary: Vocabulary + Laws + Applicability, without runtime gate predicates.

2. **Mechanism layer (A: admissibility gates).** `U.Mechanism` specializes the signature and adds **AdmissibilityConditions** (the entry gate) plus operational blocks (e.g., Transport, Audit and observability). These blocks specify runtime gates and observability *interfaces*; they are still **descriptions**. The evidence itself exists only as carriers produced in work.

   *Audit vs AssuranceLane (avoid duplication):* the Mechanism’s **Audit and observability** block defines the required semantics of an observability and evidence interface (carrier classes and required fields, correlation keys, exposure interface). **Retention, access, and enforcement are D‑claims** (role-assignment or acting-system duties) that reference the same carrier classes by ID. An MVPK **AssuranceLane** is a projection for auditors that explains how to adjudicate the evidence interface. This is a special case of CC‑A.6.6: the `AssuranceLane` face references the Mechanism section and the relevant claim IDs rather than restating semantics.

3. **Deontic layer (D: duties, commitments, and grants).** Put here an accountable duty, recommendation-as-duty, prohibition, commitment, or `A6-AW-NORM-GRANT` claim. Cite the exact A.2.8 or A.2.8.PER object selected by that row; other `A6-AW-*` claims keep their own placement. Reference related `L-*`, `A-*`, or `E-*` IDs rather than duplicating them.

4. **Observable-effects and evidence layer (E: Work-Effects & Evidence).** `E-*` is the boundary's observable-effect/evidence claim family. Each claim names the exact actual occurrence or evaluated finding under its direct owner and, when reliance is current, the observation conditions and A.10 evidence path. `U.Work` is named only when role-method-work grounding obtains; a natural, spontaneous, or formal transformation may instead use A.3/A.3.4. Canonical placement is an Evidence-and-carriers section, typically rendered in `AssuranceLane`.

5. **Actual occurrences and realizations (outside the description stack).** Substitutable realizations are exercised through dated Work when A.15.1's performer, assignment, method, time, and containing-system facts obtain. A Work occurrence may participate in change, production, speech-act effect, evaluation, or evidence production, but each of those remains a separately governed relation or claim. A.3/A.3.4 also admits natural, spontaneous, and formal transformations without a performer, assignment, method, or Work occurrence.

6. **Publication faces.** MVPK selects exact epistemes and publication forms for audience-specific face uses. A selected episteme has `U.View` membership only when E.17.0 conformance to the exact viewpoint episteme obtains; any A.6.3 source-to-receiving construction remains separate. The face class, publication occurrence, form, rendering, and carrier are not the `U.View`.

*Observability compatibility note (informative):* When specifying evidence carriers and correlation rules, it is often convenient to describe evidence-carrier classes in terms familiar from contemporary observability practice (post‑2015): traces and spans, logs and log records, and metrics time-series, with explicit correlation identifiers. Treat these as example *carrier schemas and join keys*, not as mandatory technology choices. (Concrete schema/exchange mapping remains outside Part E; keep Part E conceptual.)

##### A.6:4.1.1 - AssuranceLane skeleton (informative)

An MVPK **AssuranceLane** is a view that teaches a specific audience how to adjudicate `E-*` claims against carriers produced in work. It references (not restate) the Mechanism’s Audit and observability semantics.

Minimal content (suggested):
- **Scope:** boundaryRef, version, viewRef, viewpointRef.
- **Carrier inventory:** carrier-class and carrier-schema refs (A.7 Carrier) + where to obtain them.
- **E‑claim map:** a table keyed by `E-*` ID with: measurement conditions, carrierRef(s), join and correlation keys, and a reference to the canonical `E-*` text that defines pass or fail criteria.
- **Operational policies:** references to relevant `D-*` duties (retention, access control, exposure), without redefining them.
- **Limitations:** sampling, redaction, missing signals, expected false negatives and false positives.

**No new semantics reminder.** An `AssuranceLane` may explain adjudication informatively, but every new normative sentence first enters the canonical claim set. A changed permission-looking claim cites its selected `A6-AW-*` row and direct owner rather than being introduced inside the face.

Example (conceptual, no tools):

```
AssuranceLane:
  viewRef: <ViewId>
  viewpointRef: <ViewpointId>
  boundaryRef: <BoundaryId>
  version: <SemVer or revision>
  evidence:
    - E: E-OBS-1
      carrierRefs: [Carrier.AuthorizationRecord, Carrier.AuditLogEntry]
      measurement:
        conditions: "on every rejection due to A-AC-1"
        vantage: "Operator and auditor pipeline"
        correlation: ["traceId", "requestId"]
      adjudication:
        check: "query audit stream for code=NotAdmissible and join to traceId"
        criteriaRef: "E-OBS-1 (pass or fail criteria live canonically in the E-claim)"
      references: [A-AC-1, D-RET-1, Mechanism.AuditObservability]
```

Default placements (quadrant → stack layer / section):

* **L →** Signature.Laws (and, where appropriate, mechanism‑local semantic laws; never runtime gates)
* **A →** Mechanism.AdmissibilityConditions
* **D →** accountable duties, recommendations-as-duty, prohibitions, commitments, and `A6-AW-NORM-GRANT` claims at their exact A.2.8 or A.2.8.PER owner
* **E →** actual occurrences, evaluated findings, and evidence claims, including `A6-AW-EXERCISE`, `A6-AW-WEAK`, `A6-AW-CONFLICT`, and `A6-AW-SOURCE` when those claims are current

**Integration stitches (informative; this cluster is a classification hub, not a standalone philosophy):**
* **A.6.1 ↔ A‑quadrant:** `U.Mechanism.AdmissibilityConditions` is the canonical claim layer for `A-*` gate and admissibility claims.
* **A.10 / B.3 ↔ E‑quadrant:** `E-*` claims should cite evidence carriers and provenance (A.10); without an explicit evidence-carrier reference they are treated as `AssuranceLevel:L0 (Unsubstantiated)` in the Trust & Assurance calculus (B.3).
* **A.2.3 and F.12 ↔ D/E separation:** a `U.PromiseContent` promise is not evidence; promise acceptance is linked to work evidence via F.12, and role obligations to maintain admissibility are expressed as `D-*` duties referencing `A-*` and `E-*` by ID when needed.

 A stack is useful because the intended direction of change is clear:

* Lower layers (realizations, audit formats, transport mechanisms) are expected to change more frequently and can often evolve without forcing higher‑layer changes, provided higher‑layer commitments remain satisfied.
* Changes to higher layers are boundary-claim evolution and typically require explicit compatibility reasoning (and therefore explicit versioning and communication).

#### A.6:4.2 - Boundary Discipline Matrix: classify by A.6.B (the Boundary Norm Square)

**Normative source.** The canonical 2×2 square (the two A.6.B distinctions, quadrant semantics, form constraints, and cross‑quadrant reference rules) is defined in **A.6.B**. This section provides a short operational summary and worked rewrites only.

A “four‑part list” is insufficient, because real sentences reuse the same visible words (“must”, “guarantees”, “valid”) across different logical roles. A **2×2 matrix** is better fit because it arises from crossing **two independent distinctions**:

* **Modality family:** truth-conditional versus governance content. For permission-looking wording, the selected `A6-AW-*` row states which side applies; A.2.8.PER membership alone does not.
* **Adjudication substrate:** in‑description vs in‑work (whether satisfaction is decided from the description alone or requires observing executed work and carriers).

Operational summary (quadrant → canonical claim layer in the stack):
* **L** (Laws & Definitions) → `Signature.Laws` (truth‑conditional semantics, in‑description)
* **A** (Admissibility & Gates) → `Mechanism.AdmissibilityConditions` (runtime entry predicates; a predicate may consume an exact grant or finding selected by `A.6.B:8.4.1`, but it neither creates nor resolves that object)
* **D** (Deontics) → accountable A.2.8 claims and `A6-AW-NORM-GRANT`
* **E** (Work-Effects & Evidence) → actual-occurrence, evaluated-finding, and evidence claims, including the applicable E-side `A6-AW-*` row

Atomicity rule:

If a sentence mixes roles (e.g., “MUST” + a gate predicate + an effect claim), it is **not classifiable** as a single statement. Per **A.6.B**, split it into **atomic** claims so each one has exactly one quadrant (and, ideally, an identifier you can reference).

Micro‑template: **Atomize → Classify → Place → Bind to EntityOfConcern, Description, or carrier → Register**

1. **Split** the sentence into atomic claims (one logical role each).
2. **Assign** each claim to exactly one quadrant (L/A/D/E) using the matrix.
3. **Place** each claim into its correct section or publication form (stack layer + section).
4. **Anchor A.7:** name what each claim is about. For permission-looking wording, bind the direct object and participants required by the selected `A6-AW-*` row; the owner family never supplies the quadrant.
5. **Register:** add the atomic claim to the Claim Register (if used) and ensure every downstream face references the claim by ID rather than paraphrasing.

Action outputs after classification:

- implement or repair an admissibility predicate when the claim being made is `A-*`;
- repair the accountable subject or direct object named by a D claim; for permission-looking wording, perform only the action required by the selected `A6-AW-*` row;
- recover the exact actual occurrence, evaluated finding, or evidence path named by an E claim; use the selected E-side `A6-AW-*` row when permission wording is current;
- publish or update an MVPK face that cites L/A/D/E claim IDs rather than paraphrasing them;
- reopen the exact direct owner when the classified statement is used beyond boundary wording; the selected `A6-AW-*` row names the permission-side owner;
- downgrade the visible wording to cue use or source-finding only when the exact source is missing;
- keep the work claim or reliance claim local, reversible, or blocked only for the unsupported work claim or reliance claim while the source is repaired.

> **Informative example.** Example rewrite (mixed → atomic):

*Before (mixed, not classifiable yet):* “Clients **MUST** include header `X`; otherwise the request is invalid and the system logs `NotAdmissible`.”

*After (classifiable + lintable):*
* `A-AC-1` (Quadrant A, Mechanism.AdmissibilityConditions): `admissible(req) iff hasHeader(req, "X")`.
* `D-CL-1` (Quadrant D, Norms-and-commitments): “Client implementers **MUST** satisfy `A-AC-1`.”
* `E-OBS-1` (Quadrant E, Evidence-and-carriers): “When a request is rejected due to `A-AC-1`, an `AuditLogEntry{code="NotAdmissible"}` carrier is produced and can be observed in the audit stream.”

> **Informative example.** Example rewrite (guarantee + SLA + measurement + enforcement):
>
> *Before (mixed contract prose):* “The service **guarantees** 99.9% availability per calendar month and **MUST** keep p95 latency under 200ms; breaches are penalized; operators **SHALL** alert on violations.”
>
> *After (classifiable + adjudicable):*
> * `D-SLA-1` (Quadrant D, Commitments and SLA): “Provider **SHALL** meet `E-SLA-AVAIL-1` and `E-SLA-LAT-1` under the stated exclusions.”
> * `E-SLA-AVAIL-1` (Quadrant E, Evidence-and-carriers): “`availability ≥ 0.999` over calendar month `T`, measured by carrier `UptimeProbeSeries` from viewpoint `VP.ExternalMonitor`.”
> * `E-SLA-LAT-1` (Quadrant E, Evidence-and-carriers): “`latency_p95 ≤ 200ms` under workload `W`, measured by carrier `LatencyMetricSeries` from viewpoint `VP.Client`.”
> * `D-OPS-ALERT-1` (Quadrant D, Ops duty): “Operators **MUST** page on breach of `E-SLA-AVAIL-1` or `E-SLA-LAT-1` within 5 minutes (policy).”
> * `E-ALERT-1` (Quadrant E, Evidence-and-carriers): “Pages are evidenced by carrier `AlertEvent{ruleId,firedAt,target}` and can be joined via `incidentId`.”

See **A.6.B:4–A.6.B:6** for the normative square, quadrant form constraints, and explicit cross‑quadrant link patterns (notably: **D→A**, **E→A**, **D→E**, and **A/E→L**).

##### A.6:4.2.1 - Authority-wording split examples

These examples are informative. They show how to keep mixed authority prose from becoming evidence, assurance, commitment, gate passage, or work by wording alone.

*Before (mixed):* "This API is approved for production use and guarantees safe rollback."

*After (classifiable + source-ready):*
* `L-API-1` (Quadrant L): the API operation and rollback terms are defined in the signature vocabulary.
* `A-API-1` (Quadrant A): a request is admissible only under the named subject, action, object, context, and policy-version predicate.
* `D-API-1` (Quadrant D): the accountable provider or operator commits to maintain or enforce `A-API-1` under the named window and exclusions.
* `E-API-1` (Quadrant E): rollback success is evidenced only by the named work traces, audit records, or metrics; a gate decision carrier can support gate passage, but not rollback execution by itself.

Here “approved” creates no extra claim: `A-API-1` applies `A6-AW-GATE`, while any approval badge remains `A6-AW-SOURCE` unless another row's closing facts are present.

For a filled grant/exercise/evidence case and its near-misses, use `A.6.B:8.4.5.4`. It applies `A6-AW-NORM-GRANT`, `A6-AW-EXERCISE`, and the separate A.10 evidence claim by value; do not reproduce the owner model here.

Then:
- if a user is deciding whether the wording may guide action, enter `A.15`;
- if evidence, currentness, or provenance is live, attach the `A.10` evidence relation;
- if trust, readiness, compliance, or release confidence is being raised, build the `B.3` assurance tuple;
- if an actual gate decision or gate passage is asserted, cite `A.21` `OperationalGate(profile)`, `GateDecision`, and `DecisionLogRef`;
- if a flow witness or constraint witness is asserted, cite `A.20` `ConstraintValidity` status or witness;
- if a permission-looking claim is asserted, use the selected `A6-AW-*` row and its direct owner; an entry predicate or gate decision does not substitute for another row;
- if release, deployment, rollback, or execution Work is asserted, cite the exact A.15.1 dated occurrence; then use only the applicable `A.15.1:4.6` row for an application result, A.15.PROD production branch, delivery/transfer relation, evaluation/acceptance relation, or A.10 evidence path. None is an intrinsic Work field;
- if the phrase is only an action invitation or cue, keep it in `A.6.A`, `A.16`, or `A.16.1` according to the current kind.

Policy engines, credentials, registers, provenance, and attestations can supply policy decisions, source claims, currentness, or evidence. Start a visible permit, badge, or registry value at `A6-AW-SOURCE`; move to another branch only when its named direct object and participants are independently established.

#### A.6:4.3 - View membership needs exact viewpoint conformance

`MultiViewDescribing` makes the candidate episteme and exact viewpoint episteme explicit. The candidate has `U.View` membership only when E.17.0 conformance obtains. A projection or query may participate in an A.6.3 construction, but that construction does not establish membership. MVPK separately fixes a closed set of publication face classes (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`).

A disciplined stack therefore requires:

* Every published face use identifies the exact selected episteme, the exact viewpoint episteme through `U.ViewpointRef`, the publication occurrence, the form, and the carrier. The face class is not any of those objects.
* Calling the selected episteme a `U.View` requires E.17.0 conformance; a face label, viewpoint reference, projection history, or publication does not establish it.
* Per **E.17** (“no new semantics”), a face **MUST NOT** introduce a new semantic commitment or any new object or claim selected through `A6-AW-*`. A face **MAY** add informative explanation, examples, and cross-references. Every normative sentence cites the canonical L/A/D/E claim ID and direct object or moves into the canonical claim set.
* Per **E.17** and **publication-face and publication-form discipline** (face‑kind closure), a publication package that claims MVPK alignment **MUST NOT** mint additional MVPK face kinds (e.g., “EvidenceCard”, “NormsCard”) as if they were first‑class kinds; if you need local headings, keep them as sections within the canonical face kinds.

#### A.6:4.4 - “Contract” unpacking: avoid assigning agency to epistemes

When practitioners say “the API contract”, they usually compress several independently optional objects into one word. Use **A.6.C** to ask the four plain questions—what was promised, what was said or instituted, what governance position obtains, and what actually happened—then use `A.15.1:4.6` to separate the dated Work from any result, production, delivery/transfer, evidence, or acceptance claim.

* **Promise content (promise content; `U.PromiseContent`, A.2.3):** what is promised to be made available to eligible consumers — **a promise, not execution** (`U.Work`).
* **Utterance package (published descriptions + instituting act):** what is said and published and versioned (signature or mechanism descriptions plus MVPK faces), plus the `U.SpeechAct <: U.Work` that published or approved it when provenance matters (A.2.9).
* **Commitment (deontic commitment relation; `U.Commitment`, A.2.8):** what an accountable role assignment, `U.Role`, or admitted acting system is obligated, recommended-as-duty, or prohibited to do (often: to satisfy a promise content).
* **Permission-looking claim:** do not make `Permission` a bundle part or quadrant. Select one `A6-AW-*` row for each atomic claim and cite its direct object.
* **Performed Work (`A.15.1`):** whether one exact dated Work occurrence happened, with its performer system, covering assignment, enacted method, extent, and containing system. This claim supplies no result, delivery, or acceptance by itself.
* **Result or consequence (`A.15.1:4.6` dispatch):** only when current, name the exact A.6.1 application/result binding or subject-specific `WorkResultRelation`, A.15.PROD production branch, A.3.4 change, evaluation result, delivery/transfer relation, or acceptance relation.
* **Evidence (`A.10`):** only when a receiving use relies on one of those claims, name the claim-bound evidence path and carrier. Evidence supports that claim; it creates neither Work nor its result.

In A.6 terms:

* The **signature** is the *utterance substrate* for the boundary; it is not itself a promiser or obligor (A.7).
* Deontic claims use A.2.8 for accountable duties or commitments and `A6-AW-NORM-GRANT` for the current norm/grant branch. Other permission-looking claims keep the placement and object named by their selected row.
* Operational “guarantees” are empty rhetoric unless each atomic claim is classified as **L** (truth-conditional law), **A** (entry predicate), **D** (accountable commitment or current grant), or **E** (actual exercise, evaluated result, work effect, or measured property with evidence).

**Compact optional-object replay.** `SVC-DEPLOY-1` states promise content. Admitted system `ReleaseManager-4` performs `SA-4711 : U.SpeechAct` under `ReleaseManager-4@ReleaseShift`; the exact policy may institute `COM-4711 : U.Commitment` or `PER-4711 : GrantedPermissionRelation@Context`. Later admitted system `Operator-7` performs `DeployRun-4711 : U.Work` under its covering assignment. If the application returns `ReleaseArtifact-4711`, cite the exact A.6.1 result binding or an already governed `WorkResultRelation`; if that artifact is delivered, cite a separately obtaining subject-owned transfer relation; if acceptance is claimed, cite the criterion, evaluation Work/result, and acceptance relation. An A.10 path may support whichever one of those claims is relied on. Omit every absent object: the Work can occur without a result, delivery, acceptance, or evidence-use claim.

This paragraph is a compact reminder; the reusable expansion and the same `A.15.1:4.6` dispatch belong in **A.6.C — Contract Unpacking for Boundaries**.

#### A.6:4.5 - Where statements go (classification examples)

> **Informative.** Classification examples for learning the discipline; they do not add requirements beyond A.6:7.

The table below intentionally uses near‑everyday spec phrases. The same visible words appear in different quadrants depending on what they *do*.

| ID | Example statement (typical wording) | Matrix quadrant | Put it under… | A.7 primary layer |
| --- | --- | ---: | --- | --- |
| `L-1` | “`op f` is **defined iff** `P(x)` holds.” | L | Signature → **Laws** (`Definition:`) | Description |
| `L-2` | “For all requests, `idempotencyKey` is **unique** per subject.” | L | Signature → **Laws** (`Invariant:`) | Description |
| `A-1` | “The mechanism may be applied only if `tokenValid`.” *(rewrite as predicate: `admissible(req) iff tokenValid(req)`)* | A | Mechanism → **AdmissibilityConditions** (entry gate) | Description |
| `A-2` | “A request is admissible only if header `X` is present.” | A | Mechanism → **AdmissibilityConditions** | Description |
| `D-1` | “Client implementers **MUST** satisfy `A-2`.” | D | Norms-and-commitments (role duty; reference gate ID) | Object |
| `D-2` | “Authors **MUST** publish a versioned MVPK face for this boundary.” | D | Conformance Checklist and publication norms (authoring plane) | Object |
| `D-3` | “Operators **SHOULD** rotate keys every 90 days.” | D | Norms (role-assignment obligation; link to role and method claim IDs where applicable) | Object |
| `D-4` | “Implementers **MUST** expose audit‑log carriers via endpoint `/audit`.” | D | Norms-and-commitments (exposure duty) *about carriers* | Carrier |
| `D-5` | “The vendor commits to `99.9%` availability over window `T` (SLA).” | D | Commitments and SLA (identify committing role assignment or admitted acting system, window, exclusions) | Object |
| `E-1` | “`LedgerBalance-L17` changed from 80 to 65 across interval `T` under the stated account-continuity rule.” | E | A.3/A.3.4 actual transformation claim; no Work is inferred from the delta alone | Object |
| `E-1-EVID` | “`AuditRecord-L17` evidences `E-1` for audit use under the stated source, window, and A.10 path.” | E | Evidence relation and carrier for the already named change | Carrier |
| `D-6` | “Operators **MUST** retain audit‑log carriers for 30 days.” | D | Retention policy (deontic) *about carriers* | Carrier |
| `E-2` | “`latency_p95 ≤ 200ms` under workload `W` as measured by carrier `LatencyMetricSeries` from collector `C`.” | E | Evidence claim with measurement conditions | Carrier |

Notes:

* The classification is not just about modal verbs. “Shall” can be D (a duty) or A (a gate behavior). “Guarantees” can be D (a commitment) or E (a measured property). The matrix forces disambiguation.
* If a sentence reads like “X **MUST** … if … then …”, it almost always bundles multiple quadrants. Split into (A) a gate predicate (`A-*`), (D) an enforcement duty on a role assignment, `U.Role`, or admitted acting system (`D-*` referencing the gate ID), and (E) an evidence claim (`E-*`) if observability matters.
* When something needs to be enforceable but is mathematical, prefer predicate blocks rather than deontic language in the L/A blocks, per E.8’s deontics vs admissibility guidance.

#### A.6:4.6 - Classification sanity rules (informative, concept-level)

These are *writing diagnostics*, not tool requirements. They exist to keep the mental model crisp.

- **RFC keyword inside Definition, invariant, or admissibility predicate** → classification error (rephrase as predicate; move obligation to `D-*`).
- **`E-*` with no exact actual occurrence or evaluated predicate, or with a carrier but no evidence relation for the claimed use** → incomplete effect/evidence claim. Ground Work through A.15.1 only when it actually obtains; otherwise use A.3/A.3.4 or the exact interaction/causal owner. A carrier supports the claim but does not create the effect.
- **`D-*` that re-states an `A-*`/`L-*` predicate instead of referencing its ID** → drift risk (prefer “MUST satisfy `A-…`”).
- **A face introduces new L/A/D/E content not present in the canonical claim set** → view-fork (make it informative only, or repair the exact direct object and classify its claim: duty/commitment/grant in D; exercise/evaluated finding/evidence in E; gate in A).
- **“The system or service SHALL …” where no accountable role assignment or admitted acting system is named** → likely misclassified deontic (rewrite as `E-*` behavior + `D-*` duty on implementers and operators).

