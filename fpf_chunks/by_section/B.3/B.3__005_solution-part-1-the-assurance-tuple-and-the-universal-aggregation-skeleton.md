---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust & Assurance Calculus (F–G–R with Congruence)"
section_id: "B.3:4"
section_title: "Solution — Part 1: The assurance tuple and the universal aggregation skeleton"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__005_solution-part-1-the-assurance-tuple-and-the-universal-aggregation-skeleton.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "B.3 — Trust & Assurance Calculus (F–G–R with Congruence)"
  - "B.3:4 — Solution — Part 1: The assurance tuple and the universal aggregation skeleton"
line_start: 31617
line_end: 31900
dependencies:
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.20"
  - "A.21"
  - "A.6"
  - "A.7"
  - "B.1"
  - "B.1.1"
  - "B.1.2"
  - "B.1.3"
  - "B.1.4"
  - "B.3"
  - "B.3.5"
  - "B.3.x"
  - "B.4"
  - "C.13"
  - "C.16"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "C.26.3"
  - "C.28"
  - "D.4"
  - "E.14"
  - "E.17.EFP"
  - "F.9"
keywords:
  - "F-G-R"
  - "assurance"
  - "authority-looking labels"
  - "claim-support posture"
  - "congruence"
  - "dashboard tiles"
  - "evidence"
  - "formality"
  - "probe/distributed/export/causal assurance"
  - "reliability"
  - "scope"
  - "trust"
---

### B.3:4 - Solution — **Part 1: The assurance tuple and the universal aggregation skeleton**

B.3 defines **what** the assurance components are, **how** they live on nodes and edges of the dependency graph, and the **shape** of the aggregation that any Γ‑flavour must honor when producing an *assurance result*.

#### B.3:4.1 - The F–G–R assurance components (typed; `F/R` CHR, `G` USM)

We standardize **two node characteristics**, **one node scope object**, and **one edge characteristic**:

1. **Formality (F)** — *how constrained the reasoning is by explicit, proof‑grade structure.*

   * **Scale kind:** **ordinal** (its scale values do not admit arithmetic).
   * **Canonical scale values (example):**
        `F0 Informal prose` - `F1 Structured narrative` - `F2 Formalizable schema` - `F3 Proof‑grade formalism`.
   * **Monotone direction:** higher is better (never lowers assurance when all else fixed).

2. **ClaimScope (G)** — *the declared set of `U.ContextSlice` where the result applies.*

   * **Type:** **set‑valued USM scope object** (A.2.6), **not** a CHR characteristic.
   * **Well‑typed operations:** **membership** and **set algebra** (`∈`, `⊆`, `∩`, `⋃`, `SpanUnion`, plus declared Bridge translation / widen / narrow / refit).
   * **Scalar proxy (report‑only):** if a profile needs a number for reporting, it MAY publish an explicitly declared **`CoverageMetric(G)`**; such a proxy **MUST NOT** replace `G` in norms, gates, bridge semantics, or CL-bearing relation decisions.
3. **Reliability (R)** — *how likely the claim/behavior holds under stated conditions.*

   * **Scale kind:** **ratio** in `[0,1]` (or a conservative ordinal proxy when numeric modeling is unavailable).
   * **Monotone direction:** higher is better.

2. **Congruence Level (CL)** — *edge property: how well two parts fit* (semantic alignment, calibration, interface Standard).

   * **Scale kind:** **ordinal** with a **monotone penalty function** `Φ(CL)` where `Φ` decreases as CL increases.
   * **Canonical scale values (example):**
     `CL0 tentative guess` - `CL1 plausible mapping` - `CL2 validated mapping` - `CL3 verified equivalence`.
   * **Interpretation:** low CL reduces the credibility of the *integration itself* (not the parts), and therefore **penalizes** the aggregate **R**.

> **EntityOfConcern/Description strict distinction (A.7).**
>
> * Assurance components live as **value/scope claim components**: **F/R** as characteristics, **G** as a scope object, while Γ‑flavours fold **structure/order/time**.
> * Do not smuggle assurance components into structural edges; keep **F/R/CL** explicit as CHR metadata and **G** explicit as a USM scope object.

> **Assurance shoulders (Working‑Model split).**
> **Mapping** raises **TA** (typing, fit/CL). **Logical** and **Constructive** contribute to **VA** (intended relation semantics; Γₘ extensional identity for structure). **Empirical Validation** contributes to **LA** (evidence in a bounded context). These assurance inputs attach **downward** from the Working‑Model assertion layer (E.14).

#### B.3:4.2 - Assurance as a typed claim

B.3 speaks about **assurance of a specific typed claim** `C` over a holon `H` under context `K` and scope `S ∈ {design, run}`:

```
Assurance(H, C | K, S) = ⟨F_eff, G_eff, R_eff, Notes⟩
```

* `C` examples: *meets load L*, *argument Q holds*, *model M predicts within δ*.
* `K` binds assumptions (environment, usage, priors).
* `Notes` include the **SCR** (all sources, B.1.3), **OrderSpec/TimeWindow** where applicable (B.1.4), cutsets, and evidence citations (A.10).

This tuple gives readers an at‑a‑glance view (didactic primacy) while preserving the pieces needed for audit and improvement.

**Validation modes (declaration, normative).**
Each published Working‑Model assertion **SHALL** declare **`validationMode ∈ {postulate, inferential, axiomatic}`** (E.14).
— *postulate* → pragmatic working claim; **Empirical Validation** is **required** for audit.
— *inferential* → reasoned consequence; **Logical** assurance carries the reasoning requirement.
— *axiomatic* → constructive identity; **structural** edges MUST provide a Γₘ narrative and a **`tv:groundedBy`** pointer (C.13, B.3.5).

**Design vs run (no chimeras).** Assurance tuples for **design‑time** and **run‑time** SHALL be reported **separately** and **not composed into a single score**; see the *Scope drift* hazard in §2 and the obligations in B.3.3.

#### B.3:4.2a - Authority-looking labels and dashboard tiles

A badge, label, score, dashboard tile, credential display, provenance mark, compliance-looking mark, model card, datasheet, data card, assurance document, attestation label, assurance-looking note, or generated confidence phrase does not enter assurance calculus or improve `F`, `G`, `R`, `CL`, readiness, safety, compliance, trust, release confidence, or assurance by display alone.

**Adversarial misuse guard.** Do not let dashboards with favorable labels, compliance-looking badges, old model cards, provenance labels, assurance-looking documents, or generated confidence phrases supply missing evidence, limitations, scope, decay, or argument for an assurance claim.

Valid B.3 dispositions for such an item are:

| Disposition | Use when | Output |
| --- | --- | --- |
| No assurance use | The item is only a cue, source pointer, evidence question, currentness question, gate decision, role assertion, status assertion, commitment, boundary wording, or work occurrence. | Return to `A.15`, `A.10`, `A.6`, `A.21`, `A.20`, `A.2.1`, `A.2.8`, `A.2.9`, or `A.15.1`; no tuple is needed. |
| Compact bounded assurance claim statement | The claim is local, non-release, non-compliance, non-safety, not reused as assurance input, and does not affect people/team status. | Record the claim, assurance use carried by the assurance tuple or relying context, evidence pointer, limit, and stop/reopen condition in the current work record. |
| Full assurance tuple | The item is being used to raise readiness, compliance, safety, release confidence, trust, `F`, `G`, `R`, or `CL`. | One typed `Assurance(H, C \| K, S)` claim per named assurance claim `C`, with argument/evidence/limitations/decay. |
| Rejected or narrowed assurance claim | Evidence, scope, argument, currentness, or limitations do not carry the attempted assurance claim. | State the assurance claim, work claim, or reliance claim that the current assurance tuple does not carry, then name the next legitimate formalization, evidence repair, scope narrowing, or claim narrowing move. |

Build a `B.3` assurance claim only when the next work move or reliance move depends on a typed assurance claim. The typed assurance claim must name:

| Field | Required content |
| --- | --- |
| Claim and assurance use carried by the tuple | The claim named by value `C` and the assurance use the tuple carries: readiness, release, audit, compliance, safety, model credibility, or another named assurance use. |
| Holon, context, and scope | `H`, `K`, and `S` plus audience or relying context when the label is human-facing. |
| Evaluation condition | What was evaluated, under which method, policy, test, review, measurement, or assurance case. |
| Evidence relation and carriers | The `A.10` evidence path, carrier refs, source-maintenance role assignments, windows, verifier rule, relying-party rule, and proof results or status results that evidence the assurance tuple. |
| Argument and assurance rationale | The argument pattern, assurance case, or reason why the evidence carriers evidence claim `C` under `K` and `S`, including assumptions, defeaters, and open challenges. |
| Limitations and rival explanations | Scope limits, claims or uses not carried by the assurance tuple, stale display, spoofing, copied text, generated text, proxy-for-value substitution, provenance-only source relation, context shift, and known failure conditions. |
| Decay and reopen condition | Valid-until, revocation, policy version, gate version, model version drift, monitoring change, incident signal, evidence refresh, and contest or redress path. |

**Assurance evidence minimization.** A typed assurance result should cite the minimum `A.10` evidence path needed for the named assurance claim and relying context. Use redacted, hashed, scoped, or role-mediated evidence refs when raw carriers would expose personal data, secrets, privileged logs, tenant identifiers, security-sensitive traces, incident details, or unnecessary identities; do not build a full assurance dossier when pointers preserve enough recoverability.

Role prompts for assurance use:

| Role in the situation | Prompt |
| --- | --- |
| Assurance reviewer | Which named `Assurance(H, C \| K, S)` claim is actually being made or revised? |
| Auditor or reviewer | Which evidence path, argument, limitation, decay condition, reopen condition, and relying context must be recoverable? |
| Manager or release reader | Which desired decision or action is outside B.3 and must instead use `A.15`, `A.21`, `A.10`, or another exact source? |
| Model or data reader | Which documented admissible-use statement or external intended-use field, evaluation condition, version, window, limitation, drift, and incident condition bound the model or data documentation? |
| Evidence source-maintenance role assignment | What evidence carrier or scoped pointer must be exposed without turning documentation presence into an assurance claim? |

Display guidance for assurance labels: a readiness, safety, compliance, trust, release-confidence, or assurance display should show the named assurance claim, assurance use carried by the assurance tuple or relying context, evaluation condition, evidence-path ref, scope, window, limitation, decay condition, reopen condition, and assurance, work, or reliance claims not carried by the assurance tuple. A label that only points to documentation should remain a source pointer, not an assurance result.

Incident-learning fields for assurance overread: visible label, documentation record, or carrier, attempted assurance claim, missing tuple or evidence-path field, assurance claim, work claim, or reliance claim not carried by the assurance tuple, limitation or decay condition that defeated the claim, next legitimate formalization, evidence repair, scope narrowing, or claim narrowing move, and upstream repair item for documentation, evidence refs, assurance label wording, monitoring, or reopen trigger.

Contestability and redress path: when the B.3 material-reliance threshold is live, the B.3 result should name the claim being contested, evidence path, limitation or decay condition, reviewer or decision forum, safe interim disposition, and what evidence or scope change would reopen the assurance claim.

If those fields are missing, the encountered publication face, carrier, rendering, or cue remains an orientation label, source pointer, evidence pointer, documentation record, carrier, or unsubstantiated confidence cue. Return to `A.15` when the question is whether that lane may guide work or reliance, to `A.10` when the question is evidence, currentness, or provenance, and to `A.6` when the question is mixed policy, API, or schema wording.

**Positive repaired path.** When an assurance use is live and the required assurance fields are present, return the smallest typed assurance result that can guide work: the named claim, context, scope, evaluation condition, evidence path, argument, limitations, decay condition, and reopen condition. That result may improve or justify assurance only for the stated claim and scope; other action, gate, evidence, work-occurrence, or compliance uses still need their own exact sources.

Constructive assurance moves:

- narrow `G` to the actually evidenced or admissible scope;
- raise `F` by formalizing argument/method structure;
- raise `R` by adding validation, replication, more probative, repeated, current, or more relevant evidence;
- improve `CL` by repairing mappings, units, interfaces, or integration edges;
- separate design assurance from run assurance;
- add limitations, assumptions, defeaters, monitoring, drift, and reopen triggers;
- reject or downgrade the assurance use when those moves are not available.

Negative controls:

| Visible item | Admissible source or assurance use | Non-admissible use without a full tuple |
| --- | --- | --- |
| Source-backed release dashboard tile | If the tile is a current view of `A.21` `GateDecision` or `DecisionLogRef` plus an `A.10` evidence path, it may carry gate-passage reliance outside B.3 for the named release and environment. B.3 is live only when the tile is also asked to raise readiness, safety, compliance, trust, or release-confidence assurance. | Release approval by display, compliance proof, rollback success, work occurrence, or assurance increase without a typed assurance claim. |
| Credential, compliance, or provenance label | Bounded source, holder, status, history, or documentation source relation when evidenced. | Safety, truth, permission, gate passage, readiness, or assurance claim by label presence. |
| Model card, datasheet, data card, assurance document, or assurance-looking note | Scoped documentation for a named claim, documented admissible-use statement or external intended-use field, evaluated condition, limitation, version, and window. | Higher `R`, broader `G`, higher `F`, better `CL`, readiness, compliance, safety, or release confidence by document presence. |
| Generated confidence phrase | Source-finding or explanation relation when grounded. | Assurance increase, authority, approval, or evidence by wording alone. |

Model cards, datasheets, data cards, assurance documents, and assurance-looking notes are external documentation records or source carriers unless they are mapped into existing `FPF` claims and publication faces. They do not add MVPK face kinds and do not bypass `B.3` when the use under repair is an assurance claim.

**Lint trigger.** A model card, datasheet, or data card cited as readiness, safety, compliance, release confidence, or assurance proof requires documented intended-use match, evaluation condition, limitations, an `A.10` evidence path, and one typed `Assurance(H, C \| K, S)` claim for the named assurance claim. Without those, return `no assurance use` or a rejected/downgraded assurance claim.

Positive repaired example: a model card plus documented admissible-use statement or external intended-use field, evaluation condition, version, window, limitations, an `A.10` evidence path, and a typed `Assurance(H, C \| K, S)` claim may carry assurance for that named model claim in that evaluated context. The same documentation still does not carry another deployment context, gate passage, release work occurrence, or compliance proof unless those sources are separately present.

#### B.3:4.2b - Minimum reliance safety assurance record

Use this B.3 section when the B.3 material-reliance threshold is live: reliance on a visible source may materially change behavior, safety, release, compliance, public or protocol behavior, access, resource allocation, people/team status, operational action, or controlled-object regulation. The first B.3 move is to decide whether assurance is live; if it is, write the minimum reliance safety assurance record for the named reliance use. Mere attention shift, learning, orientation, source-finding, or carrier wording correction is not enough.

`RelianceSafetyCase` is the local Tech label for this B.3 assurance-record role. The plain phrase is **minimum reliance safety assurance record**. The label is not a new FPF pattern, Core kind, safety authority, gate, policy source, approval, certificate, compliance method, or general safety-case ontology.

Assurance-record role: the trigger and non-trigger table is a B.3 recognition aid, the minimum assurance-record table is a minimum local record aid, and the worked reliance-threshold slices are regression/review slices. They are not a universal project checklist, sign-off sequence, untyped status vocabulary, or replacement for `Assurance(H, C | K, S)`; use them only when the named material reliance trigger is live. This local section returns the attempted reliance to the B.3 assurance relation; it does not create an extra SEMIO authority or cross-pattern relation vocabulary.

Affordability card: orientation or source-finding stays outside B.3; bounded local reliance stays with the local evidence, explanation, CV, gate, or pattern-quality relation unless assurance is live; threshold reliance opens the minimum reliance safety assurance record only when the B.3 material-reliance threshold is live. Plain wording remains ordinary unless it changes admissible use, source relation, evidence, gate, assurance, work, decision, or neighboring-pattern exit.

Common wrong first reading: a safety-looking note, safety case, compliance-looking label, or dashboard warning is a certificate, approval, or gate. First honest entry: state one typed B.3 assurance claim with A.10 evidence path, assumptions, limitations, defeaters, residual uncertainty, monitoring or stop condition, contest/redress, admissible use, and unadmissible use.

First admissible B.3 move: name the reliance use, the assurance claim, the affected context or audience, the trigger that makes B.3 live, the A.10 evidence path, the argument, limitations, defeaters, contest/redress path, stop or monitoring condition, admissible use, and unadmissible use. If those pieces are absent, return the source to `A.10`, `E.17.EFP`, `A.20`, `A.21`, `E.19`, or the local relation rather than inventing assurance by label.

Trigger and non-trigger cases:

| Encountered source use | B.3 disposition | Minimum action |
| --- | --- | --- |
| Ordinary source-backed report, citation, model card, datasheet, data card, or documentation record with no assurance use and no B.3 material-reliance threshold | No B.3 assurance use. | Stay in `A.10` with claim, carrier, evidence path, window, admissible use, unadmissible use, and reopen trigger. |
| Generated explanation, generated summary, or didactic reconstruction used only for source-finding or learning | No B.3 assurance use. | Stay in `E.17.EFP` unless operative claims are relied on through `A.10` evidence paths or another source relation that evidences the operative claim. |
| Local conformance label, `CV.Status`, benchmark result, or score near a release conversation but not used to raise assurance | No B.3 assurance use. | Keep `CV.Status` in `A.20`, gate-decision publication in `A.21`, pattern-quality result in `E.19`, measurement or marker relation in `C.16`/`A.10`, and no assurance tuple unless an assurance claim is live. |
| Confidence, calibration, prediction interval, or abstention reason tied to one reversible local act | Compact bounded assurance claim only when the act depends on assurance; otherwise no B.3 use. | State act, context, window, calibration basis, stop condition, admissible use, and unsupported attempted use; open `C.27` or `G.11` when time, expiry, refresh, or monitoring changes the move. |
| Safety-looking note, compliance-looking label, public warning, dashboard state, generated operational explanation, or status display is intended or reasonably foreseeable to make the B.3 material-reliance threshold live: reliance materially changes behavior, safety, release, compliance, public or protocol behavior, access, resource allocation, people/team status, operational action, or controlled-object regulation. | Minimum reliance safety assurance record is required. | Build the B.3 assurance record with A.10 evidence path and any live `A.20`, `A.21`, `E.19`, `C.27`, `G.11`, `B.2.5`, or representation/retargeting dependency. |

Minimum assurance record:

| Field | Required content |
| --- | --- |
| Reliance use and assurance claim | The behavior, safety, release, compliance, public or protocol behavior, access, resource allocation, people/team status, operational action, or controlled-object regulation that would materially change, and the assurance claim being made about that change. |
| Context, audience, and affected role | The bounded context, environment, user group, team, public audience, relying role, affected role, tenant, release line, service, or work target. |
| Source carrier and evidence kind | The visible source, publication face, record, cue, marker, conformance label, dashboard, explanation rendering, score, warning, or status display, plus the evidence kind being used. |
| A.10 evidence path | Claim, carrier, producer or method trace, currentness/window, source-maintenance role assignment, evidence relation, rival explanation, admissible use, unadmissible use, and reopen trigger. |
| Argument and assurance basis | Why this evidence path makes the assurance claim admissible under the context; include assumptions, limitations, defeaters, residual uncertainty, and unacceptable-harm or risk-tolerance condition where live. |
| Dependencies | Any live `A.20` CV status, `A.21` gate decision, `E.19` pattern-quality result, `C.27` temporal claim, `G.11` refresh/decay relation, `B.2.5` control relation, or representation/retargeting relation. |
| Monitoring, rollback, or stop condition | What observation, incident, drift, contest, expiry, changed profile, changed source, or failed check stops, narrows, reopens, or withdraws the reliance. |
| Contest and redress | The disputed claim or disposition, affected use or harm, accountable review role, admissible challenge evidence, possible disposition change, outcome record, and reopen trigger. |
| Public and private evidence boundary | Public summary, reviewer-only evidence, affected-party contestable minimum, and any scoped, redacted, hashed, or role-mediated evidence ref needed to preserve recoverability without overexposure. |

Positive repaired path: when the trigger is live and the assurance record is sufficient, return the smallest typed assurance result that can guide the reliance: named assurance claim, reliance use, context, evidence path, argument, limitations, dependencies, monitoring or stop condition, contest/redress path, admissible use, and unadmissible use. When the record is insufficient, narrow the reliance, degrade the assurance use, abstain, require evidence, reopen the source, or block the attempted assurance use; do not convert a polished source into safety acceptance.

A safety case is accepted only as a bounded assurance argument for the named reliance use. It remains contestable by defeaters, changed evidence, changed context, monitoring failure, residual-uncertainty breach, or admissible affected-party challenge. Stop when the named reliance use, unadmissible use, limitations, defeaters, contest/redress path, monitoring or rollback condition, and reopen condition are sufficient for this threshold trigger; do not expand the record into a general safety dossier.

Accountable review is insufficient by title alone. It counts here only when it can change the disposition, records the outcome, and leaves the admissible use, unadmissible use, and reopen condition inspectable.

Misuse guard: an incoming or attempted-reliance `RelianceDisposition=safety-case-required` must name the trigger that makes B.3 live. A source producer, dashboard-state publisher or maintainer, model producer, documentation producer, or status-label issuer cannot self-clear a threshold-bearing reliance by attaching the label. Where the B.3 material-reliance threshold is live, the assurance record must expose an accountable review role and a contest path capable of changing the disposition.

Affected-party contestable minimum: public/private evidence separation is valid only if the affected party can see enough of the claim, source class, disposition, affected use, accountable role, and allowed challenge evidence to challenge the result. Reviewer-only evidence may stay protected, but protected evidence cannot make redress non-contestable while the assurance use still claims contest or assurance relation. A blocked, abstained, degraded, or evidence-needed assurance use is not final if admissible challenge evidence, missing affected-party evidence, changed source, changed context, monitoring failure, or redress can materially change the disposition.

Worked reliance-threshold slices:

| Slice | B.3 move | Boundary |
| --- | --- | --- |
| A public-service or access-status display changes who receives access, support, or review. | Use the minimum reliance safety assurance record for the named status-changing reliance, with contest/redress and unadmissible use. | The display is not approval, safety, fairness, compliance, or resource authority by itself. |
| An SRE dashboard changes incident behavior or resource allocation. | Use B.3 only when the dashboard is asked to raise assurance or safety-bearing reliance; keep ordinary evidence/currentness in A.10. | Use B.2.5 only for a live control relation and A.21 only for a live gate decision. |
| A public warning or synthetic-content label changes perceived meaning but there is no evidence that it changed the target behavior, release risk, safety claim, or control relation. | Keep the label as A.10 evidence or source-finding/orientation cue; require audience/action effect evidence before B.3 reliance. | Do not infer safety, compliance, behavior change, or control effect from label presence alone. |
| A manufacturing conformance label appears near release. | Keep local CV or conformance evidence in `A.20`, `A.21`, `C.16`, or `A.10`; open B.3 only when assurance, safety, compliance, or release-confidence reliance is live. | Conformance presence is not safety acceptance or release permission. |
| A software supply-chain attestation is cited as runtime safety. | Use `A.10` for origin/build/process claims and B.3 only for the named assurance claim with argument, limitations, defeaters, and stop condition. | Build provenance is not runtime safety or operational permission. |
| A people or team status badge changes permissions, resources, or review priority. | Require a assurance record that names affected role, relying role, evidence path, contest path, and disposition change condition. | The badge issuer cannot self-clear the people/team-status-changing reliance by issuing the badge. |
| A standards-document clause is reused as approval. | Use `A.10` for evidence of the clause; open the exact approval, commitment, gate, or assurance relation only when live. | A cited clause is not project approval, gate passage, or assurance by quotation. |

Do not read the assurance record as a graded scale, standalone status, universal assurance checklist, release certificate, or new safety-case state family. B.3 consumes the assurance record only as typed assurance input for the named claim and reliance use.

#### B.3:4.3 - Where the numbers live (and do not)

* **On nodes:** each input holon contributes its local `F, G, R` according to its nature (system vs. episteme).
* **On edges:** each integration step has a `CL` (congruence of the connection).
* **Not inside Γ:** Γ consumes `D` and returns a composed holon; B.3 governs how `F, G, R, CL` **propagate** to the **Assurance** tuple for that composed holon. This keeps Γ algebra and assurance calculus **separable** and reviewable.
* **Not a state space:** `⟨F,G,R⟩` is an **assurance tuple**, not a `U.CharacteristicSpace`; do **not** draw “trajectories” in `⟨F,G,R⟩`. For episteme evolution, use **ESG** states and the **assurance‑trace** hooks (see below).

#### B.3:4.4 - Universal aggregation skeleton (domain‑neutral)

Any Γ‑flavour that claims an **Assurance** result **must** adopt the following **conservative skeleton**:

1. **Formality:**

   ```
   F_eff = min_i F_i
   ```

   *Rationale:* the least formal piece caps the formality of the whole (WLNK on F).
   *Monotone:* raising any `F_i` cannot reduce `F_eff`.

2. **ClaimScope:**

   ```
   G_eff = SpanUnion({G_i}) constrained by evidence relation
   ```

   * “SpanUnion” is a **set/coverage union** in the domain’s space.
   * **Constraint:** any region in the union **not covered** by reliable parts is **dropped** (WLNK).
   * *Monotone:* adding evidence-covered span cannot reduce `G_eff`.

3. **Reliability (penalized by integration):**

   ```
   R_raw = min_i R_i                       // Weakest-link cap
   R_eff = max(0, R_raw − Φ(CL_min))       // Congruence penalty
   ```

   * `CL_min` is the **lowest** Congruence Level (`CL`) value on any edge in the proof spine / critical integration region for the claim `C`.
   * `Φ` is **monotone decreasing** and **bounded** (never makes negative values).
   * *Monotone:* increasing any `R_i` or any `CL` cannot lower `R_eff`.

4. **SCR and Notes:**
   * The aggregate SHALL produce a SCR listing all contributing nodes and edges, with their F, G, R, CL, scopes, and evidence links (A.10).
   * The SCR SHALL additionally display the **EntityOfConcernRef** (`entityOfConcernRef and groundingHolonRef`) and the **ReferencePlane** for the claim, and present a **separable TA/VA/LA table** of evidence contributions with **valid_until/decay** marks and the **Epistemic‑Debt** per § B.3.4.
   * If order/time mattered for the claim, attach the OrderSpec or TimeWindow identifiers (B.1.4).

This skeleton is **mandatory**. Domain‑specific patterns may add **refinements** (e.g., separate epistemic “replicability” vs. “calibration”) as long as they **do not violate** WLNK or MONO and preserve scale kinds.

#### B.3:4.5 - System vs. Episteme — same shape, different readings

* **For systems (Γ\_sys):**

  * `F` reads as **engineering discipline** (from ad‑hoc method to verified specification).
  * `G` reads as **operational envelope coverage**.
  * `R` reads as **assured reliability** under `K` (requirements, environment, test campaigns).
  * `CL` often arises at **interfaces** (Boundary‑Inheritance Standard; B.1.2): poorly controlled interfaces reduce `R_eff`.

* **For epistemes (Γ\_epist):**

  * `F` reads as **logical/semantic formality** (from prose to proof).
  * `G` reads as **domain span** (concepts, populations, conditions).
  * `R` reads as **evidential relation quality** (replication quality, measurement integrity).
  * `CL` measures **semantic alignment** of merged constructs (terminology mapping, ontology bridges, calibration).

> **Agentness is separate (A.13).**
> Agency metrics (Agency‑CHR) **do not enter the skeleton by default**. They may act as a **contextual overlay** (e.g., to argue why a supervisory policy can maintain `R` across disturbances), but **never** to bypass **WLNK** or the **CL penalty**. Grade shifts should be modeled as **MHT** events when they create new capabilities.

#### B.3:4.6 - Scale discipline (CHR guard‑rails)

To prevent silent misuse:

* **Ordinal scales (F, CL):** never average or subtract; only `min`/`max`, thresholds, and monotone comparisons are valid operations.
* **Coverage scales (G):** use union/intersection in a declared domain space; do not “average” sets. If a numeric proxy is used (e.g., coverage ratio), it **must** be derived from a set operation, not vice versa.
* **Ratio scales (R):** may be combined with `min`, `max`, or **explicitly justified** conservative functions; do not add R’s from different contexts without normalization of `K` (assumptions).

#### B.3:4.7 - What improves the tuple (action-pattern overview)

B.3 remains neutral about *how* improvement happens, but for didactic clarity:

* **Raise F:** formalize narratives (specifications, machine‑checked models).
* **Raise G:** enlarge evidence-covered span (new test regimes, new populations) with adequate evidence.
* **Raise R:** replicate, calibrate, tighten measurement error, reduce bias.
* **Raise CL:** reconcile vocabularies, align units, formalize mappings, verify interface Standards.

Each of these corresponds to recognizable **Transformer roles** and KD‑CAL moves (design‑time); their **run‑time** counterparts are covered by Γ\_time (phase evidence) and Γ\_work (cost of obtaining assurance).

