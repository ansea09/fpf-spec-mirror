✓ `A.16` keeps `projection` as a move name for route-bounded partialization; `F.9.1` keeps `projection` as a bridge stance label. If one durable reusable replacement name is really needed, handle the naming question with **F.18 `MintNew` or `DocumentLegacy`** rather than flattening both readings into one umbrella rewrite.

**Editorial note.**
This section **inherits** § 7 **MG-DA** (anchored head nouns; Characteristic/CharacteristicSpace for enums; collision checks) and § 8 **LEX.Morph** (suffix/prefix/casing). It deliberately **omits** their details to avoid duplication.  The only legitimate uses of *plane* in the Core are **CHR:ReferencePlane** and the derived operators **CL^plane** and **Φ_plane**; policy flags MUST NOT introduce new “planes”. To distinguish pre‑operational vs operational states *within* **ReferencePlane=world**, use **WorldRegime ∈ {prep|live}** (formerly `PlaneRegime`).

### E.10:9.1 - Guarded-head cross-reference *(normative lexical caution)*
When one surface head already carries several load-bearing local readings, lexical cleanup should prefer a **guarded-head note** over silent flattening. The note may record that the head remains risky, name the cited texts or patterns that govern the local readings, and point readers to the local canonical reading in each cited text.

If cleanup reveals that no admissible existing token can carry the needed meaning, use the local repair pattern for one-off wording. If the change needs one durable reusable name, handle the naming question with **F.18 `MintNew` or `DocumentLegacy`** rather than inventing an ad hoc synonym by feel.

This cross-reference is lexical only. It does **not** create a new repair-side definition site, does **not** establish Cross-context equivalence, and does **not** overrule cited local definitions. It simply keeps overloaded heads from being normalized into one false global reading.

`projection` is the main current example: `A.16` keeps it as a move name for route-bounded partialization, while `F.9.1` keeps it as a bridge stance label. E.10 therefore requires deconfliction notes and explicit naming of the cited text that governs each local reading, not one umbrella rewrite that erases the distinction.

### E.10:10 - Migration playbook — turning messy language into ULR‑clean prose *(informative)*

> A pragmatic **three‑pass** routine. Works with plain text, diagrams, or models; no tools required.

#### E.10:10.1 - Pass 0 — *Pre‑flight (2 minutes per page)*

0.1 **Name the Context card** you’re writing in (title, edition, scope note).
0.2 For every new or renamed token, **declare `LEX.TokenClass`** ∈ {KernelToken, ContextToken, DiscriminatorToken}.
0.3 Run **MG-DA pre‑check** (anchored head noun; no metaphor heads; if enum → declare its **CharacteristicSpace**).
0.4 Run **collision/uniqueness**: full‑text grep + Reserved‑Names registry (see § 7). If collides → rename or DRR deprecate.

#### E.10:10.2 - Pass 1 — *Harvest in the Context*

1.1 **Underline overloaded words** (*process, service, function, workflow, ticket, approval, spec, plan,* …).
1.2 For each, write a **one‑line intent** in Plain register (what FPF kind or relation is meant).
1.3 Mark any cross‑Context reuse candidates.

#### E.10:10.3 - Pass 2 — *Map to Core anchors (mechanical)*

2.1 Replace underlined words via **§ 9 L‑rules** table:
 • recipe → **`U.Method` / `U.MethodDescription`**
 • scheduled run → **`U.Work` / `U.WorkPlan`**
 • promise → **`U.PromiseContent`**
 • ability → **`U.Capability`**
 • actor‑mask → **`…Role / RoleAssignment`**
 • document/evidence carrier → **`Episteme`** with **`EvidenceRole/RequirementRole`**
2.2 Apply **LEX.Morph** (§ 8): suffix gates (`…Role/…Work/MethodDescription/Service`), casing, reserved prefixes.
2.3 Pass **I/D/S layer** check: types/roles on I; recipes/docs on D; actuals on runs.
2.4 Attach **Context tags** on first use; set **twin labels** (Tech/Plain) in the local Glossary.

#### E.10:10.4 - Pass 3 — *Stitch & publish*

3.1 Add **safe rewrites** for any anti‑patterns you found (use § 9.2 quick table).
3.2 If sameness is needed across Contexts, create a **Bridge** (F.9) with explicit `kind/dir/CL/Loss/scope` (apply **A.6.9 (RPR‑XCTX)** when quoted or imported source wording uses umbrella “same/equivalent/align/map/…” language).
3.3 Publish a one‑page **UTS** (F.17) for the Context (columns: Context, Tech label, Plain label, Kernel anchor, Warnings).
3.4 Log a short **DRR** when renames/aliases occur (F.13), linking to grep results that motivated the change.


### E.10:11 - ULR conformance prompts *(normative, concept-only questions)*

> Use these **prompts** during review. They reference § 7 (MG-DA) and § 8 (LEX.Morph) instead of repeating them.

1. **Context prompt.** Does each potentially polysemous noun live inside a **named `U.BoundedContext`**?
2. **Layer prompt.** Is each sentence in the correct **I/D/S layer** (I: type/role; D: description/spec; run: actuals)?
3. **Token prompt.** For new/renamed tokens, is **`LEX.TokenClass`** declared and consistent with where the token appears?
4. **Head-kind prompt.** Does the **head noun** name what kind of thing the phrase is actually about (Role/Method/Service/Work/Context/Characteristic/publication form/reading/process/authority use)? A narrowing qualifier alone does **not** answer this question.
5. **Qualifier-load prompt.** If an adjective, participle, genitive, or comparative modifier is doing semantic work, has that load been restored explicitly rather than left inside the modifier alone?
6. **Comparison-basis prompt.** If the sentence compares, ranks, escalates, or downgrades something, is the comparison basis ontologically homogeneous after head-kind and qualifier restoration?
7. **Morphology prompt.** Do suffix/prefix/casing pass **LEX.Morph** gates (e.g., `…Role`, `MethodDescription`, `Work`)?
8. **Promise vs ability vs performance.** Are **Service** (promise), **Capability** (ability), and **Work** (performance) distinct?
9. **Plan vs execution.** Are **WorkPlan** windows separated from **Work** actuals?
10. **Evidence prompt.** Do documents **hold roles** and **justify**, while **systems act**?
11. **Bridge prompt.** If sameness spans Contexts, is there an explicit **Bridge** with **CL** and loss notes?
12. **Collision prompt.** Did we run full-text + Reserved-Names checks (no other meaning of this token anywhere in FPF)?
13. **Naming-procedure prompt.** If one durable reusable name is needed because no admissible existing token carries the needed meaning beyond one local repair, did we run the full **F.18 `MintNew` or `DocumentLegacy`** procedure rather than picking a label by intuition and filling a partial Name Card afterward?

**Working order for precision repair on load-bearing prose.** Restore the head kind first; a narrowing qualifier such as `comparative`, `safe`, `interactive`, or `reliable` does **not** by itself restore that kind. Then unpack qualifier load, then check whether the comparison or escalation basis is homogeneous. Only after that may a later Plain, didactic, or coarsened rendering admissibly relax the sentence, and even then the more precise upstream reading must remain recoverable.

### E.10:11a - SoTA-Echoing for lexical governance

E.10 lexical governance is not a private FPF style preference. It is a compact authoring discipline for communication, comprehension, term formation, and error prevention. These external practice rows support the discipline only where they change what an author or reviewer does in a live wording repair.

| Practice support | What E.10 adopts | What E.10 rejects |
| --- | --- | --- |
| ISO 704:2022 and ISO 1087:2019 terminology work on concepts, definitions, designations, and term formation. | Use explicit designation and definition discipline when a term is minted, repaired, or made reusable. Keep the head kind, context, and intended use recoverable. | Do not solve FPF wording by dictionary substitution, synonym stuffing, or global alias registry. Do not turn every term into a class hierarchy. |
| Human-readable identifier and label clarity practice in software and HCI work. | Treat names as comprehension and error-prevention aids, not as cosmetic polish. Use clear local names only when they preserve the same FPF kind and relation. | Do not let a nicer label change kind, scope, authority, or downstream use. Do not accept readability as proof that the term is semantically safe. |
| Ontology and controlled-vocabulary practice. | Use exact modeling only when the current problem really needs it, and then make the modeled kind and relation explicit. | Do not make OWL-style term-to-class modeling the default answer to every vague term. E.10 repairs wording first and applies `F.18`, `A.6.P`, or a domain pattern only when that heavier modeling move is live. |

The practical result is simple: lexical governance must improve action guidance and semantic composability, not become language-police work. A SoTA row that does not change a rewrite, a forbidden shortcut, a neighboring-pattern application, or a conformance check remains decorative and does not carry E.10.

### E.10:12 - ULR regression cues *(concept-only “diff” triggers)*

Re-review your prose when any of these happen:

* **Context edition** changes → re-affirm twin labels, Bridges, and acceptance wording.
* **A role/type name grows** (“and/plus/--”) → apply MG-DA: split or bundle (A.2).
* **A “service” statement broadens scope** → check that **acceptance** terms cover the new target; else split the Service.
* **Recipes gain/lose steps** → update **`MethodDescription`**, not `Service` or `Role` names.
* **Evidence verbs creep into actor sentences** → re-apply L-rules (documents do not act).
* **A generic head acquires a load-bearing qualifier** (`comparative`, `safe`, `interactive`, `reliable`, and similar modifiers) → restore the head kind first, then unpack the qualifier load before broader publication.
* **New token minted** → ensure `LEX.TokenClass` declared; run collision checks; add CharacteristicSpace if enum.
* **Suffix drift** (e.g., `…Work` on a plan) → fix via **LEX.Morph**.
* **Cross-Context reuse by label** appears → require a **Bridge** (F.9) or split senses.
* **A guarded head needs a new label** → prefer a guarded-head note first; if no admissible existing token remains for one durable reusable name, handle the naming question with full **F.18 `MintNew` or `DocumentLegacy`**.

### E.10:13 - Teaching deck — the ULR quick card *(reusable in any Context)*

> **Say it cleanly, once (memorise):**
> **Role** = assignment (mask) - **Method** = way‑of‑doing - **MethodDescription** = recipe (document) - **Work** = run (dated)
> **Capability** = can‑do within bounds (envelope + measures) - **Service** = promise (access + acceptance)
> **I/D/S are layers**; **documents don’t act**; **Contexts own meanings**; **Bridges** move meanings.

**Name forms (allowed morphology):**
• **Types/roles:** `<Noun><Role/Type>` (`IncidentCommanderRole`, `NormativeStandardRole`, `WorkItemType`).
• **Statuses:** `<Noun>Status` inside the Context’s role space (`ApprovedStatus`) — status‑only; not enactable.
• **No suitcase nouns:** avoid “and/plus/&” in names; use **bundles** (A.2) or separate roles.
• **Acronyms:** first expansion + register; short‑form registered per **§ 7.7**.


### E.10:14 - Three worked micro‑examples — ULR across domains *(informative)*

#### E.10:14.1 - Healthcare (OR context)

**Messy:** “The surgical **process** is scheduled at 08:00; the SOP approves the incision and the **service** documents recovery.”
**ULR rewrite:**
“**WorkPlan** OR‑Case‑221 starts 08:00 and will execute **MethodDescription** `Incision_v4`.
`SOP_OR_v4` holds **RequirementRole**; a **SpeechAct Work** by `QA_Officer#ApproverRole` authorises the run.
The hospital offers **Service** ‘Post‑op monitoring’ (access = ward protocol; acceptance = vitals envelope).”

#### E.10:14.2 - Manufacturing (assembly line)

**Messy:** “The welding **function** provides air‑tight seams; the **process** costs 3 min.”
**ULR rewrite:**
“`Robot_SN789` has **Capability** ‘execute `Weld_MIG_v3` within envelope E at measures M’.
**Work** instances that **fulfil Service** ‘Provide seam S’ average 3 min; **acceptance** bounds are in `Seal_Acceptance.md`.
The **MethodDescription** is `Weld_MIG_v3`; the **Role** is `WelderRole`.”

#### E.10:14.3 - Cloud/SRE (production Context)

**Messy:** “The storage **service** wrote logs and the deployment **process** failed after 2 min.”
**ULR rewrite:**
“`sCG‑Spec_ci_bot#DeployerRole:CD_v7` performed **Work** ‘Deploy r4711’ (failed at T+120 s).
The platform offers **Service** ‘Object Storage’ (access = `S3_API_Spec_vX`; **acceptance** = durability/availability targets).
`LogWriter` is a **System** bearing `TransformerRole` that wrote the records; *the service did not act*.”


### E.10:15 - Closing notes *(governance & purity)*

* **Notation‑agnostic.** ULR is a **language constitution**, not a scanner or template. Apply it in prose, sketches, or formal models.
* **Where checks live.** Convenience checks belong to Tooling; ULR itself stays notation‑agnostic. Conformance code lives in **SCR‑LEX / RSCR‑LEX** as referenced above.
* **Acts vs tokens.** LEX applies to **tokens**; USM applies to **acts** (mint/rename/use). Conformance:
  `LEX.TokenClass(t)=c  ⇒  USM.Scope(usage) ∈ AllowedScopes(c)` (§ 7.5).
* **Guards honoured.** DevOps Lexical Firewall and Unidirectional Dependency remain intact.
* **Reserved “plane”.** Only **`CHR:ReferencePlane`** uses the bare word *plane*; I/D/S are **layers**; all other category talk is expressed as **Characteristics** in a **CharacteristicSpace**.

> **One‑line memory:** *“ULR keeps words honest so ideas stay composable.”*


### E.10:End
## E.10.SEMIO - Episteme-Publication Semantic Rewrite Discipline

> **Type:** Definitional (D), E.10 cluster specialization
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### E.10.SEMIO:0 - Use this when

Use `E.10.SEMIO` when semio-heavy conformant text relies on loose wording around epistemes, publications, views, publication forms, generic publication faces, governed MVPK faces, bounded publication units, carriers, records, relations, admissible uses, or pattern application.

Use it especially when wording around claim-bearing epistemes, described entities, publication units, publication forms, admissible use, claim support, pattern application, placement wording, movement wording, or slash compounds seems convenient but may be carrying ontology, authority, evidence, or admissibility load.

**Ordinary-language survival.** Ordinary words remain admissible until the sentence gives them FPF-kind, relation, authority, evidence, admissibility, work, gate, decision, bridge, or reliance load. `Source` may stay ordinary when it only means where a quote came from; `view` may stay ordinary when it means what the reader sees and not `U.View`; `route` may stay ordinary navigation prose; `support` may stay ordinary help. Repair by load-bearing sentence function, not by trigger word alone.

**Do not punish clarity.** Prefer the clearest ordinary head that preserves kind, relation, and admissible use. Do not replace a clear plain phrase with a technical phrase unless the technical phrase blocks a live false reading or is needed for accepted stable FPF naming. In an ordinary case, `reader help`, `source-pointer-only`, or `comparison only` may be better than a more technical phrase.



**Not this pattern when.** `E.10.SEMIO` is not the governing pattern for every recovered construct. General lexical discipline stays under `E.10`; stable reusable naming under `F.18`; relation precision under `A.6.P`; A.6.B law-, admissibility-, deontic-, and effect-claim boundary splitting under `A.6.B`; object-description-carrier separation under `A.7`; view and publication discipline under `E.17` and `E.17.0`; project work, evidence, gate, decision, method, action-invitation, assurance, and engineering-justification claims under their exact FPF patterns. When one of those claims is live, this pattern supplies only the semio trigger, recovery, and rewrite profile; the neighboring named pattern supplies its invariant.

**First output.** The ordinary first move is to repair one overloaded phrase, row, field, or sentence so the reader can tell which exact FPF kind, relation, publication construction, or project-side value is live. If that one local repair restores kind, relation, and admissible use without changing work, evidence, gate, release, policy, assurance, adjudication, or bridge use, stop there. Use a compact pattern-local `SemioRewriteRecord` or equivalent local rewrite note only when the phrase carries load that must remain inspectable after the repair.

When a load-bearing recovery note is needed, the final value is one exact FPF kind, relation record, relation phrase, tuple-like record, exact project-side FPF kind and reference when `projectSourceLoad` is live. The selected value is one live value, not the list: `C.11` `ChoiceResult`; `C.11` decision record; `A.6.A` action invitation; `A.15` `U.WorkPlan`; `A.15.1` dated `U.Work` occurrence; `U.Method`; `U.MethodDescription`; `A.20` constraint or adjudication decision record; `A.21` `GateDecision`; `A.21` `DecisionLogRef`; `A.10` evidence path; typed evidence record; `B.3` assurance or engineering-justification record; typed status record whose FPF status pattern is named; carrier relation; front-end relation; or not-triggered alternative. Otherwise it is explicitly left as quote-only wording, reduced-use cue, understandable FPF extension candidate, or blocked current transfer.


### E.10.SEMIO:0.1 - What goes wrong if missed

Semio-heavy text starts to build a parallel ontology. A generic publication face becomes a `U.View`, a file becomes an episteme, a dashboard tile becomes evidence, a pattern name becomes a procedure, a slash list becomes a group kind, or a broad word such as `source` hides whether the text means a pattern, a `DRR`, a publication, a document with named source-basis, evidence-basis, architecture-basis, or review-basis role, an exact project-side FPF kind and reference, or a relation.

The immediate cost is not only ugly terminology. Engineers and FPF authors start making action, evidence, gate, decision, or engineering-justification claims from the wrong object.

### E.10.SEMIO:0.2 - What this buys

`E.10.SEMIO` gives authors and reviewers one small semantic-rewrite action: recover the FPF kind stack first, then write exact wording that preserves the needed distinction without adding another claim. It prevents string-replacement cleanup, keeps FPF-side and project-side episteme and publication work separate, and blocks unclear text from becoming current FPF content by author guesswork.

**Successful repair condition.** Semantic repair is not closed by type-correct wording alone. It is governed by `E.2` Pillars, especially `P-2 Didactic Primacy`, together with `E.12` and the register rule in `E.10:6.2`. It closes only when the repaired text preserves or restores one remaining admissible reader move: a usable action, a recognition reason that tells the working reader why the distinction matters, or a named neighboring-pattern handoff that now carries the live claim. When both Tech and Plain registers are live, the Tech reading must remain recoverable and any Plain or didactic line must map back to that Tech reading. A Plain, more expressive line, or intentional didactic metaphor may stay ordinary when it carries no FPF load; when it carries ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility load, that load must be recoverable through the Tech fields, exact FPF kind, recovered relation, project-side source reference, or disposition named by the repair. If a repair in a load-bearing Problem frame, Problem section, recognition text, example, or worked slice makes the text more exact but less able to show the working situation, why it matters, or what action remains, the repair is incomplete unless a named neighboring FPF pattern now carries that live claim. Overread removal is only half of semantic repair; the other half is surviving admissible action under the Pillars.



**Governed object in plain terms.** The governed object is one semio-heavy wording use inside conformant text: the word or phrase, the sentence function it carries, the FPF kind or relation it must recover, and the admissible remaining use after recovery.

**Primary working reader.** The first reader is an author or reviewer of conformant FPF-style text who must repair wording without losing ontology. The downstream reader is the engineer-manager using the resulting pattern or project text in a working situation.

**Anti-overread payoff question.** A repair is useful only if the pattern text can answer three things in ordinary prose: what false downstream reading is blocked; what useful admissible action remains; and when the reader must apply a neighboring FPF pattern because evidence, gate, decision, work, assurance, bridge, release, or reliance is live. If the repair blocks an overclaim but leaves no useful action, the text is probably becoming ceremony rather than guidance.


### E.10.SEMIO:1 - Problem frame

FPF already has episteme, publication, view, carrier, presentation, relation, naming, and pattern-application concepts. Semioarchitecture work nevertheless created many convenient intermediate words while the architecture was being discovered. Those words were useful in chat, review, and drafts, but they are dangerous when they survive as final pattern or architecture prose.

The recurring situation is simple: a sentence is understandable enough to feel worth keeping, but its head kind is not recovered. If it is repaired by replacing one broad word with another broad word, the ontology gets worse while the text looks cleaner.

#### E.10.SEMIO:1.1 - Purpose Carried From The Glossary And Rules
This pattern gives the current glossary and rewrite rules for terms around epistemes, publications, views, publication forms, generic publication faces, governed MVPK faces, carriers, records, and bounded publication units.

It exists because semio-heavy texts can use locally convenient heads that collapse described entity, publication unit, publication face, carrier, record, source relation, and project-side value.
Those words may be useful recognition handles, but they are not safe FPF heads when they carry ontology, authority, or authority-changing meaning.

The rewrite discipline here is semantic, not lexical:
- do not replace one broad token with one new broad token by string substitution;
- first recover the FPF kind stack, the claim-bearing status, the publication, view, carrier, or relation construction, and any work, action, or authority crossing;
- then choose the smallest exact wording that preserves the load-bearing distinction without creating a second ontology.

This pattern follows the `E.10` style: head noun first, kind and relation discipline second, register, plain use, and tech use third, and only then canonical rewrites.

### E.10.SEMIO:2 - Problem

Without a semantic-rewrite discipline for semio-heavy wording:

1. broad publication words hide whether the claim is about `U.Episteme`, `U.View`, publication form, generic publication face, governed MVPK face, `PublicationUnit`, carrier, document with named source-basis, evidence-basis, architecture-basis, or review-basis role, review target, or exact project-side FPF kind and reference;
2. FPF pattern-application claims and project-side work-occurrence, work-plan, decision, action-invitation, method, record, carrier, or front-end claims get mixed in one sentence;
3. slash lists and heterogeneous rows become false group kinds;
4. unclear source meaning is guessed into FPF rather than blocked or promoted through an accepted FPF extension;
5. authors copy the same loose wording into `DRR`s, patterns, source-basis notes, or project texts.

### E.10.SEMIO:3 - Forces

| Force | Tension |
| --- | --- |
| Exactness vs readability | FPF prose needs exact kinds, but a sentence overloaded with every possible kind becomes unreadable. |
| Preservation vs cleanup | Accepted architecture text must not be paraphrased away, but source-companion status cannot be mistaken for pattern authority. |
| Local repair vs new ontology | Many phrases only need local A.6.P and F.18 recovery; a few reveal a real missing FPF kind or relation. |
| FPF-side vs project-side work | The same word can describe FPF pattern authorship or a user's project publication, record, work, or action. |
| Guidance vs audit | The pattern must tell authors what to do, while check rows only verify that the rewrite was carried out. |

### E.10.SEMIO:4 - Solution

Repair semio-heavy wording by semantic recovery, not by dictionary replacement.

A successful rewrite satisfies these field-validity constraints:

1. the head kind and sentence function are recoverable under `E.10`;
2. a stable reusable name has `F.18` status;
3. a relation, comparison, dependency, support, sameness, grounding, mapping, or endpoint claim has `A.6.P` relation precision, with admissibility and project-side support questions split into their own fields;
4. a claim-bearing episteme, exact episteme species, episteme-lane view, or exact project-side FPF kind and reference has the needed `C.2.1` or neighboring FPF reading;
5. publication, view, face, and carrier distinctions satisfy `E.17.0`, `E.17`, and MVPK;
6. the repaired text satisfies `E.2` Pillars, especially `P-2 Didactic Primacy`, by preserving or restoring one remaining admissible reader move: a usable action, a recognition reason that tells the working reader why the distinction matters, or a named neighboring-pattern handoff that now carries the live claim; when both Tech and Plain registers are live, the Plain or didactic line maps back to the recovered Tech kind, relation, or neighboring-pattern handoff under `E.10:6.2`; ordinary Plain wording and intentional didactic metaphor stay light when they carry no FPF load, but ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility load in a more expressive Plain line must be recoverable through the repaired Tech fields; load-bearing Problem frames, Problem sections, recognition texts, examples, and worked slices must still show the broad working situation and first useful move, or the rewrite is incomplete;
7. the final phrase preserves the distinction without adding another claim;
8. unrecoverable meaning, kind, register mapping, or remaining reader move fails closed.

The detailed solution below carries the glossary and rewrite rules as ordinary pattern subsections. It is not an external container: these subsections are the pattern's detailed semantic-rewrite guidance.



#### E.10.SEMIO:4.0a - SemioRewriteRecord

For load-bearing cases, the recovery product is a compact pattern-local `SemioRewriteRecord` or an equivalent local rewrite note. Ordinary local phrase repair may end as the repaired sentence itself when kind, relation, and admissible use are now clear and no downstream reliance, cross-context reuse, grouped-kind risk, hidden authority claim, project-side overclaim, conflict among publication, describedEntity, and project-side action claims, or contested source meaning remains live. Prefer the plain names `semantic rewrite note`, `compact semantic rewrite row`, or `local rewrite note` when durable inspection does not require the code-like field name. The recovery note is a lightweight pattern-local author or reviewer product, not a new ontology, not a dispatch table, not a durable FPF record kind, and not a mandatory heavyweight project record. It becomes a durable FPF record only if another accepted pattern or accepted `DRR` explicitly admits it as one. It records only the trigger, the recovered FPF kind stack, the requirement from the exact governing FPF pattern, and the final rewrite disposition that must remain inspectable after the repair.


Minimum fields when load-bearing:

Recover by claim force, not word form. For words such as `source`, `support`, `status`, `valid`, `ready`, `approved`, and `used`, first ask what the sentence would let the reader do or rely on: source-finding only, source availability, source use, evidence support, gate passage, decision status, readiness threshold, work permission, assurance, engineering justification, or ordinary orientation. Then fill only the field whose exact FPF kind, relation, or project-side reference is live.

| Field | Meaning | Governing FPF source when live |
| --- | --- | --- |
| `triggerSpan` | The exact word, phrase, field, row, or sentence fragment carrying semio load. | `E.10` and this pattern. |
| `sentenceFunction` | Whether the span is definition, claim, instruction, comparison, publication description, evidence statement, gate statement, work statement, reliance statement, example, quote, or another named function. | `E.8`, `E.10`, and the local pattern being authored. |
| `recoveredHeadKind` | The exact FPF kind or explicit non-transfer disposition recovered from the phrase. | `F.18`, `A.6.P`, `A.7`, and the governing pattern for that kind. |
| `laneStack` | The live side and kind stack: FPF-side pattern text; project-side episteme, publication, and work; the `A.7` object-description-carrier distinction when live; publication form, generic publication face, governed MVPK face, `U.View`, `PublicationUnit`, carrier, front-end, and cue when live; and exact work, evidence, gate, decision, or action-invitation value when live. | `A.7`, `E.17`, current episteme and publication patterns, and exact project-side FPF patterns. |
| `claimBearingEpistemeOrRecord` | Exact claim-bearing `U.Episteme`, exact episteme-lane `U.View` with explicit episteme tether when the governing FPF pattern makes that view live, exact project record kind and reference, or no-claim-bearing-object disposition. Publication form, generic publication face, carrier, `PublicationUnit`, and source cue stay in `publicationStack` or `projectSourceLoad` unless the claim is explicitly about that object. A governed MVPK face is handled through the exact episteme-lane `U.View` reading when that typing is live. | `C.2.1`, `E.17`, and the exact governing pattern for the record if live. |
| `publicationStack` | `U.EpistemePublication`, publication form, generic publication face, governed MVPK face, bounded `PublicationUnit`, carrier, carrier relation, and front-end relation when live. | `C.2.1`, `E.17.0`, `E.17`, MVPK, and `A.7`. |
| `relationLoad` | Empty, or a local note that `A.6.P` relation precision is live for this sentence. It must name the relation problem being handled: relation, comparison, dependency, support, sameness, grounding, mapping, endpoint claim, or cross-context bridge claim. The recovery then names `RelationKind`, `QualifiedRelationRecord`, relation phrase, candidate-set note, or bridge card when live. | `A.6.P`. |
| `admissibleUse` | The exact admissibility target, non-admissible neighboring use, and L-, A-, D-, and E-claim split when the sentence makes a boundary-use claim. | `A.6.B`, `A.6`, and the exact governing pattern for the use. |
| `projectSourceLoad` | The exact project-side FPF kind and reference when the sentence would support work, evidence, gate, constraint, adjudication, decision, commitment, method, action invitation, assurance, or engineering justification. | `A.15`, `A.15.4`, `A.10`, `A.20`, `A.21`, `B.3`, `C.11`, `A.2.8`, `A.2.9`, `A.6.A`, or another exact FPF pattern. |
| `selectedRewrite` | The final exact wording or record-shaped value. | This pattern plus the exact governing FPF pattern named above. |
| `remainingAdmissibleReaderMove` | One short line, Plain-facing when the text serves a working reader, naming what the reader may now do, why the distinction still matters, or which named neighboring FPF pattern now carries the live claim. This field is the local `E.2` `P-2` preservation check for load-bearing semio repair, not an optional commentary line. When both Tech and Plain registers are live, this line must map back to the recovered Tech kind, relation, or neighboring-pattern handoff. It may be more readable or memorable than the Tech line, and may use an intentional didactic metaphor, but any ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility load must remain recoverable through that repaired Tech reading. If no such line can be stated, the rewrite is incomplete or must fall to a non-transfer disposition. | This pattern, `E.2`, `E.8`, `E.10:6.2`, `E.12`, and the named neighboring FPF pattern when a handoff is live. |
| `disposition` | Local recovery outcome: recovered by value, quote-only wording, reduced-use cue, understandable FPF extension candidate, blocked current transfer, rewrite incomplete, or not triggered. This slot is not a recovered FPF kind. | This pattern. |



Use the short form when only one field is live. Use the full record when several fields are live or when the phrase might otherwise create a grouped kind, hidden authority claim, project-side overclaim, conflict among publication, describedEntity, and project-side action claims, contested source-meaning transfer, or procedure-like ordering of pattern applications.

#### E.10.SEMIO:4.1 - General Recovery Check
Use this recovery check whenever the text proposes a new term, repairs a semio-heavy term, or relies on wording around `PublicationUnit`, `describedEntity`, publication, view, face, carrier, source relation, target relation, publication face, described entity, or bounded publication-unit status.

1. **E.10 head-kind and relation recovery.**
   Decide what the head noun names before accepting the phrase: intension, description episteme or specification episteme, `U.Episteme`, `U.View`, publication form, generic publication face, governed MVPK face, carrier or rendering, exact project-side FPF kind and reference, `A.15.1` dated `U.Work` occurrence, `A.6.A` action invitation, `A.2.9` `SpeechActRef`, `A.2.8` `U.Commitment`, `U.Method`, `U.MethodDescription`, or document with named source-basis, evidence-basis, architecture-basis, or review-basis role, or review target.
   Apply Intension, Description, and Specification, Context, Tech and Plain, and carrier humility rules before treating a word as meaning-bearing.
2. **F.18 naming pass when a stable term is being chosen.**
   If the phrase is becoming a reusable head, fill at least the lightweight Name Card facts: Context, Kind, purpose and use-domain, local sense, candidate head families, NQD-front reasoning, sense-seed read-through, and the lexical Q tuple `{SemanticFidelity, CognitiveErgonomics, MorphologicalActionFit, AliasRisk}`.
   Do not pick a label only because it is intuitive.
3. **A.6.P relation-precision pass when a phrase carries relation, comparison, or action load.**
   Restore generic head kind first, then endpoint facets and kinds, then relation kind, slots, qualifiers, scope, time, viewpoint, and hooks for admissibility, evidence, and work.
   If ambiguity remains, write a local Candidate-Set Note rather than debating synonyms.
4. **C.2.1 episteme-slot pass when the object is claim-bearing.**
   Name `describedEntity`, grounding, ClaimGraph, viewpoint and view, reference scheme, representation scheme, and bounded context as far as the claim needs.
   Do not use `PublicationUnit` or a carrier word as a substitute episteme.
5. **E.17.0, E.17, MVPK publication pass when the object is published or reader-facing.**
   Separate the underlying episteme or view, `U.EpistemePublication`, publication form, generic publication face, governed MVPK face, `PublicationUnit`, carrier or rendering, and the exact project-side FPF kind and reference when a project-side claim is live.
   A face, card, screen, or explanation can guide reading or source-finding without becoming evidence, work, gate passage, authority, or release permission. If those claims are live, fill `admissibleUse` and `projectSourceLoad` instead of treating the generic publication face or governed MVPK face as the source value.
6. **Remaining admissible reader move.**
   After the kind, relation, publication, and project-side splits are recovered, state the remaining admissible reader move in one short line: what the working reader can now do, why the distinction still matters, or which named neighboring FPF pattern now carries the live claim.
   If both Tech and Plain registers are live, keep the Tech reading recoverable and make the Plain or didactic line map back to the recovered Tech kind, relation, or named neighboring-pattern handoff under `E.10:6.2`. Do not make this a heavy form for ordinary prose: a Plain line that carries no FPF load may stay ordinary; a Plain line that carries ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility load must be recoverable through the repaired Tech fields.
   If the repaired wording only proves that an overclaim was removed, but leaves no usable action, recognition reason, or neighboring-pattern handoff, do not classify the repair as recovered by value.
7. **Authority-changing rewrite boundary.**


   If the result would rename an accepted FPF pattern, change an accepted FPF term, or mint a reusable FPF kind, this pattern only classifies the phrase as recovered by value or as an understandable FPF extension candidate.
   It does not make the authority change by itself.
   Use the accepted source that already carries the decision by value; do not add a second decision source merely to restate the same content.

Fail closed:
- if the kind stack cannot be recovered, keep the term as plain or informative prose;
- if the relation kind cannot be recovered, keep the statement as a cue or split alternatives;
- if the publication construction cannot be recovered, do not use that publication, generic publication face, governed MVPK face, form, carrier, or rendered unit for work, evidence, gate, or authority claims. Fill `relationLoad` only when a relation claim is live, and fill `admissibleUse` plus `projectSourceLoad` when an admissibility or project-side support claim is live;
- if the recovered wording is type-correct but leaves no remaining admissible reader move, recognition reason, Tech-to-Plain mapping when both registers are live, or neighboring-pattern handoff, or if a Plain or didactic line supplies practical force through unrecovered ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility load, mark the rewrite incomplete or demote the phrase to quote-only wording, reduced-use cue, or blocked current transfer before using it as current pattern, architecture, `DRR`, or project text.



##### E.10.SEMIO:4.1.1 - Slash Discipline

In many standards, a slash can mark near-synonyms or parallel labels.
In FPF-facing semioarchitecture, a slash is a recovery trigger before it is a synonym marker.

Before leaving a slash expression in current prose, classify the expression as one of these cases:
- an accepted token, formal notation, file path, URL, quoted source wording, or product name where the slash is part of the carrier syntax;
- a plain-language synonym pair with no ontology, authority, evidence, or admissibility load;
- a composite-kind candidate that needs `F.18` and `A.6.P` recovery;
- a relation claim that needs a `RelationKind`, a `QualifiedRelationRecord`, or a multi-term relation phrase with typed endpoints, slots, qualifiers, scope, time, and viewpoint;
- a tuple-like record that needs a named record kind and named slot semantics;
- a failed ontology signal where the sentence lists unlike objects because the live FPF kind, relation record, relation phrase, tuple-like record, or not-triggered disposition has not yet been recovered.

If the expression is not one of the first two safe carrier or plain-language cases, do not keep the slash as final wording.
Write the recovered FPF kind, relation record, relation phrase, tuple-like record, or not-triggered disposition by value.

##### E.10.SEMIO:4.1.2 - Unclear Source Meaning and FPF Extension Candidates

Sometimes the problem is not a bad word but one of two different cases:
- the intended claim cannot be determined from the surrounding source, current `FPF` kinds, or current semioarchitecture;
- the claim is understandable, but current `FPF` does not yet contain the kind, pattern, relation record, or method guidance needed to carry it.

Do not merge those cases.
An unclear claim is not current architecture truth merely because deleting it feels risky, and it must not be rewritten by guessing a likely author intention.
An understandable uncovered claim may be retained as a candidate `FPF` extension only when the problem situation, tempting overread, rejected current uses, current `FPF` gap, and the first user action that would improve are stated by value.

Classify the case explicitly:
- **recovered by value:** the text now names the exact `U.Episteme`, `describedEntity`, `U.View`, publication form, generic publication face, governed MVPK face, `PublicationUnit`, carrier relation, relation record, relation phrase, tuple-like record, FPF pattern, document with named source-basis, evidence-basis, architecture-basis, or review-basis role, exact project-side FPF kind and reference when `projectSourceLoad` is live. The selected value is one live value, not the list: `C.11` `ChoiceResult`; `C.11` decision record; `A.6.A` action invitation; `A.15` `U.WorkPlan`; `A.15.1` dated `U.Work` occurrence; `U.Method`; `U.MethodDescription`; `A.20` constraint or adjudication decision record; `A.21` `GateDecision`; `A.21` `DecisionLogRef`; `A.10` evidence path; typed evidence record; `B.3` assurance or engineering-justification record; typed status record whose FPF status pattern is named; carrier relation; front-end relation; or not-triggered alternative;
- **understandable FPF extension candidate:** the thought is clear enough to state as a candidate new or amended FPF kind, pattern, relation record, method guidance, `DRR` obligation, or campaign problem, but it does not carry current authority, evidence, or admissibility load until an accepted architecture decision, accepted `DRR`, or accepted FPF pattern supplies that authority;
- **quote-only source wording:** the phrase may remain only as quoted source wording or provenance, with no current authority, evidence, or admissibility load;
- **reduced-use cue:** the phrase is kept only as a recognition cue or anti-case, not as a claim-bearing architecture decision;
- **blocked current transfer:** the phrase is not admissible for claim-bearing architecture, `DRR`, pattern, or project text until a new source, author clarification, or accepted architecture decision supplies the missing meaning, kind, or relation.
- **rewrite incomplete:** the repaired wording may be kind-correct, but it does not yet state a remaining admissible reader move, recognition reason, Tech-to-Plain mapping when both registers are live, or neighboring-pattern handoff, or a Plain or didactic line carries ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility load that cannot be recovered from the Tech reading; continue repair or demote to a non-transfer disposition before treating the text as landed.



These dispositions are recovery results, not a meta-governance authority over all of `FPF`.
When recovery names a neighboring FPF kind, the neighboring FPF pattern governs that kind, its admissible use, and its conformance checks.
`E.10.SEMIO` may identify that `A.10`, `A.15`, `A.15.4`, `A.20`, `A.21`, `B.3`, `C.11`, `F.9`, `E.17.EFP`, `E.17.ID.CR`, or another neighboring FPF pattern is live.
It does not govern the recovered kind after that identification.
`E.10.SEMIO` only makes the live kind, relation, and use boundary explicit enough that the right governing pattern can be applied.

No other disposition is closed.
In particular, "seems to mean", "probably about", a cleaner paraphrase, or a broad umbrella replacement is not a successful recovery.

#### E.10.SEMIO:4.2 - Core Glossary

##### E.10.SEMIO:4.2.0 - Cross-Side Fields That Must Stay Split

These fields are current semioarchitecture vocabulary for `DRR`, architecture, and pattern-drafting work.
They exist to prevent one sentence from mixing FPF-side admissibility, project-side records, actual work or action, method selection, carrier access, and authority records.
They are local recovery aids, not FPF kinds, not record kinds, and not a universal record ontology.
Each field closes only by naming the exact FPF kind, relation record, relation phrase, exact project-side FPF kind and reference, or explicit non-transfer disposition that is live in the sentence.
The same local-aid rule applies to neighboring field names such as `sourceSupportPosture`, `explanationSourcePosture`, `comparativeRelationPosture`, `representationValiditySupportPosture`, `allowedUse`, `misuseRisk`, and `worldContactPolicy`: they help record a local recovery or reader-use boundary, but they do not become kinds. Posture fields do not instantiate evidence, gate, assurance, work, commitment, speech act, decision, release, authority, representation kind, world-contact kind, or policy kind. Read `allowedUse` as a local reader-fit field under `admissibleUse`, not as permission, evidence support, or authority.

| Term | Current reading | Must not mean |
| --- | --- | --- |
| `FPF` as episteme | The whole `FPF` is a claim-bearing episteme with publications, parts, patterns, pattern sections, `DRR`s, and support documents and documents with named source-basis, evidence-basis, architecture-basis, or review-basis roles. | A file, repository, taxonomy, pattern-language metaphor, or packet-local summary by default. |
| FPF pattern | A named FPF pattern: a reusable episteme species that gives action guidance for a problem situation. It is applied in a live problem situation. | Any recurring arrangement, procedure, method call, route, cluster label, checklist, or document with a named source-basis role. |
| pattern section | Either a part of the pattern episteme or a bounded `PublicationUnit` of that pattern publication, depending on sentence function. State which one matters when the distinction carries a claim. | Independent pattern, file location, generic locus, or record with named authority-reference relation. |
| accepted campaign `DRR` | A campaign decision source that states accepted content decisions for one campaign. | A pattern, current-authority summary, open-ended plan, review log, or replacement for pattern text. |
| `relationLoad` | Empty, or a local note that `A.6.P` relation precision is live for one sentence. It must name the relation problem being handled: relation, comparison, dependency, support, sameness, grounding, mapping, endpoint claim, or cross-context bridge claim. The recovery then names `RelationKind`, `QualifiedRelationRecord`, relation phrase, candidate-set note, or bridge card when live, with typed endpoints, slots, qualifiers, and scope. | Dictionary replacement, one new umbrella kind, a bare `RelationKind` standing in for a relation record, a generic relation slot, support relation by default, or a list left as the final answer. |
| `admissibleUse` | The exact admissibility target and non-admissible neighboring use when the sentence says what use, act, claim, or reliance is admissible. Use A.6.B when the boundary claim needs L-, A-, D-, and E-claim separation. | Generic supported use, permission-by-appearance, or visual cue or readability cue treated as admissibility. |
| `projectSourceLoad` | The exact project-side FPF kind and reference when a publication, display, cue, or explanation is read as support for work, evidence, gate, constraint, adjudication, decision, commitment, method, action invitation, assurance, or engineering justification. The field points to the project-side FPF kind and reference; the neighboring FPF pattern governs that relation and its checks. | One slot accepting records, actions, methods, carriers, evidence, gates, decisions, assurance, and engineering justification interchangeably. |
| `rejectedOverread` | A local field naming the tempting interpretation, evidence, gate, work, permission, approval, commitment, release, safety-proof, engineering-justification, or pattern-entry reading that must not be granted by resemblance alone. It is valid only with the recovered relation record or phrase or current-context unpacking that blocks it. It is not `U.Kind`, not a record kind, not a review-finding kind, and not a moralized defect class. | A general risk slogan, review finding, moralized "bad use", vague misuse label, or reusable FPF kind. |
| `admissibilityTargetKind`, `admissibilityTargetRef` | Older local helper fields. Prefer `admissibleUse`; if these fields appear, they name the exact admissibility target kind and reference inside `admissibleUse`, not an `A.6.P` relation slot. | A generic `supported use`, document capability, "stronger claim", reviewer permission, or untyped target. |

##### E.10.SEMIO:4.2.1 - Episteme, Publication, Carrier Stack

| Term | Current reading | Must not mean |
| --- | --- | --- |
| `U.Episteme` | Claim-bearing episteme or episteme species. Use when the value is a claim-bearing episteme that can be described, viewed, grounded, revised, published, or relied on under FPF. | File, paragraph, screen, carrier, status note, process state, or generic "content". |
| `U.EpistemeSlotGraph` | The recoverable slot graph for a claim-bearing episteme: `DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ViewSlot`, `ReferenceSchemeSlot`, `RepresentationSchemeSlot`, and bounded context where live. | A prose checklist, a file map, or an optional decoration. |
| `describedEntity`, `DescribedEntityRef` | The exact `Entity` reference under `C.2.1` named by a claim-bearing episteme: entity, relation, FPF pattern, FPF publication, project episteme, project publication, exact project-side FPF kind and reference, work or action when that work or action is itself the described entity, or another explicitly typed description target. Use this when the text is really about what the episteme describes. In publication-unit work, `DescribedEntityRef` is used only through a live claim-bearing episteme or episteme-lane `U.View`; it does not float as a free field on the unit. | Generic topic, local table subject, file title, review target, required project-side work, decision, action invitation, authoring work, or anything someone happens to talk about. |
| `primary described entity` | The main described entity kept stable by the claim-bearing episteme, view, or pattern body that a `PublicationUnit` carries or exposes when stability matters. | The whole publication unit, the authoring process, the carrier, or the reader's topic of interest. |
| `GroundingHolon`, grounding relation | The grounding holon or grounding relation that anchors the described entity when a claim depends on grounding, embodiment, witness, or reference-plane discipline. | A convenient source citation or an untyped entity mention. |
| `U.View`, `U.EpistemeView` | Effect-free projection or view over an episteme under `E.17.0`, `E.17` and the episteme morphism patterns. A governed MVPK face can be this kind only under MVPK constraints. | A UI view, reader viewpoint, screen, generic publication face, or new claim-bearing episteme by default. |
| `Viewpoint` | The stance or viewpoint specification for a view or multi-view description. | A reader viewpoint, reviewer opinion, pattern-application order, publication label, or carrier label. |
| publication | A publishable episteme, view, record relation, act or occurrence of publishing, or publication form, depending on sentence function. Always split by kind before use. | Generic document, any public-looking file, or proof that a claim is authorized. |
| `U.EpistemePublication` | Claim-bearing publication of an episteme when the publication itself carries episteme-publication identity. | Publication form, generic publication face, governed MVPK face, copy, file, dashboard tile, or carrier. |
| publication form | The typed form in which an episteme, view, or record is published. | The claim-bearing episteme itself, the face rendered for a reader, or the carrier holding bytes. |
| generic publication face | Reader-facing publication projection or face. It is not `U.View` by default; it becomes a view only when the exact governing FPF pattern makes that relation live. | `U.View` by default, carrier, UI face, front-end display, governed MVPK face, or claim-bearing episteme. |
| governed MVPK face | `E.17` face emitted under MVPK constraints from a source episteme or episteme-lane view, publication viewpoint, scope, pins, and face kind. It may be a `U.EpistemeView` when the MVPK profile makes that typing live. | Generic publication face, carrier, UI face, front-end display, or proof of evidence, work, gate, or authority by presentation. |
| carrier, front-end, rendering | The system, medium, file, display, front-end, or rendering that bears or shows an encoding. | Episteme identity, publication form, `U.View`, proof of evidence, or authority-reference relation. |
| `PublicationUnit` | `E.17.AUD`-cluster head for one bounded unit inside a publication that a person inspects or reads as one unit: a pattern body, section, table, note, card, sheet, screen block, or another bounded publication unit whose boundary is named. A card, sheet, or screen block counts only when its boundary is inside a named publication or generic publication face and the sentence needs that bounded unit as the inspected publication unit. It is part of or bounded by the publication face that renders or locates it, whether that face is generic or governed by MVPK. It may carry or expose a claim-bearing episteme, view, record, cue, or local rendered content when that carried item and relation are named, but it is not identical with the carried item. | Authoring process, reviewer process, file, carrier, front-end, UI behavior, dashboard behavior or export behavior, whole publication architecture, `U.Episteme`, `U.View`, publication form, generic publication face, governed MVPK face, or "anything written". |
| exact project-side FPF kind and reference | Evidence record, gate record, work record, status record, commitment record, role-assignment record, decision record, source `U.Episteme`, source `U.EpistemePublication`, status-register entry, or another project record whose governing FPF kind is named. | Semantic content in general, current process state, or a free-form note. |
| source document | A document used as source basis, evidence basis, architecture basis, or review basis. Name whether it is source basis, evidence basis, architecture basis, or review basis directly. | A governing source by folder proximity, the described entity, or the authority-reference relation unless that relation is explicit. |
| review target | The exact review target sent or inspected in review. | The described entity carried or exposed by that target, the source basis behind it, or a packet-local summary. |

##### E.10.SEMIO:4.2.2 - FPF Text Trigger Lexicon

These trigger words are frequent in conformant FPF and FPF-facing project texts.
Files carrying FPF pattern text are useful search examples, not the boundary of semantic cleanup: the same rule applies wherever the text under repair is claim-bearing FPF or FPF-facing project guidance.
They are not banned words.
They are words that must trigger kind recovery when they carry ontology, authority, evidence, or admissibility load. The table gives alternatives to recover from; it must not be copied as a group kind. The chosen rewrite may be a named kind, a relation record, a multi-term relation phrase with typed endpoints, slots, qualifiers, scope, time, and viewpoint, a tuple-like record, or an explicit not-triggered disposition.

| Trigger words | Recovery choices; write the selected kind, relation record, relation phrase, tuple-like record, or not-triggered disposition before use | Must not mean |
| --- | --- | --- |
| `case`, `scenario`, `example`, `pilot`, `anti-case` | worked case, recognition case, pilot case, negative control, project situation, evidence case, comparison case, or source example | proof, evidence, universal pattern, accepted `DRR`, source basis, or decision by itself |
| `basis` | source basis, decision basis, evidence basis, comparison basis, threshold basis, grounding basis, admissibility basis, or authority basis | generic reason, untyped support, or "whatever the text relies on" |
| `context`, `scope`, `frame` | bounded context, project operational context, review context packet, source context, reference frame, viewpoint frame, or claim scope | world, situation, authority, authority-reference status, or hidden qualifier |
| `state`, `status`, `posture`, `readiness` | characteristic-space position, status record, role assignment or status assertion, protocol state, publication posture, process state, or readiness claim with threshold basis | maturity adjective, authority, gate passage, release permission, or evidence by appearance |
| `claim`, `claim content`, `claim referent` | claim node or claim content in a claim-bearing episteme, claim-bearing publication, admissibility target, or described entity or referent relation | sentence, opinion, text fragment, document with named source-basis, evidence-basis, architecture-basis, or review-basis role, or whole publication unit |
| `evidence`, `witness`, `ground`, `proof` | evidence record or evidence path, witness, grounding relation, source pin, observation, validation result, or assurance argument component | authority, approval, gate, engineering justification, or truth by label |
| `authority`, `permission`, `approval`, `commitment`, `obligation` | role assignment, speech act, commitment record, authority relation, gate record, decision record, or policy claim | visible label, author confidence, reviewer praise, explanation, or provenance mark |
| `profile`, `harness`, `catalog`, `registry`, `index`, `map` | support profile, review harness, entry index, registry record, source map, navigation map, publication form, support publication, or exact named support record | governing FPF pattern, governing source, ontology, method, or release decision unless named by value |
| `entry`, `front door`, `corridor`, `route` | navigation support, recognition entry, navigation-bearing publication, corridor overview, or movement, control, and temporal relation | governing pattern body, mandatory process sequence, release readiness, or proof that the target publication or target record is complete |
| `same`, `parity`, `identity`, `equivalence`, `mirror` | same described entity, semantic equivalence, bridge relation, version identity, carrier mirror relation, or file mirror relation | similarity, substitutability, no-loss transform, source equality, or authority equality by wording resemblance |
| `file`, `path`, `host`, `packet`, `bundle`, `package` | carrier path, file carrying FPF pattern text, review-facing target packet, review-facing context packet, package-form decision, or transport bundle | episteme, publication form, pattern body, review result, `authoritySourceRef` target, governing FPF pattern, or authority-reference relation |
| `quality`, `characteristic`, `metric`, `indicator`, `score` | `U.Characteristic`, quality term, Q-bundle, scale, indicator, observed value, benchmark, or evaluation record | vague praise, scalar truth, success proof, or replacement for the named characteristic space |
| `slot`, `field`, `row`, `label`, `badge`, `mark` | schema slot, relation slot, table row, publication label, provenance mark, status badge, or cue | kind, evidence, authority, gate passage, or proof of currentness |

#### E.10.SEMIO:4.3 - Current Preferred Vocabulary
Use `PublicationUnit` when the intended object is a bounded, human-inspected unit inside a publication.
Do not use it for UI behavior, carrier behavior, front-end behavior, file identity, dashboard behavior, or export behavior; use `A.7`, carrier wording, front-end wording, or the exact neighboring FPF pattern instead.

Use the current cluster names directly: `PublicationUnit Stability Discipline`, `Local Head Restoration`, and `PublicationUnit Primary Described-Entity Discipline`.
When the live object is a bounded unit inside a publication, use `PublicationUnit`; when the live object is authoring or editing work, name that work directly.

Use `primary described entity`, `DescribedEntityRef` when local wording means the described entity named by a claim-bearing episteme or episteme-lane view.

Use ordinary `topic`, `subject`, or `local object` only in non-normative explanatory prose where no episteme slot, publication construction or authority relation is being asserted.

Do not mint any other new reusable FPF name from this pattern alone. `PublicationUnit` is governed by the `E.17.AUD` cluster named **PublicationUnit Stability Discipline**; this pattern recovers bounded-publication-unit wording into that head when the object is live and points to that cluster for governance. Load-bearing uses keep the nearby definition or explicit publication stack.

##### E.10.SEMIO:4.3.1 - F.18 And A.6.P Admission Reading For `PublicationUnit`

This is the F.18 and A.6.P name reading that this pattern reflects from the selected `E.17.AUD` cluster correction.
It records why `PublicationUnit` is the selected bounded publication-unit head for the `E.17.AUD` cluster, while `E.10.SEMIO` remains the semantic-rewrite profile.

```text
F.18 and A.6.P admission reading:
  Context: conformant FPF authoring and review where bounded publication units must not be confused with epistemes, views, publication forms, generic publication faces, governed MVPK faces, carriers, authoring work, or review process.
  Kind: governed-object head for a bounded unit inside one publication.
  Purpose and use-domain: keep one human-inspected publication unit distinct from episteme, view, publication form, generic publication face, governed MVPK face, carrier, authoring work, and review process.
  Selected Tech label: PublicationUnit.
  Plain reading: bounded unit inside a publication that a person inspects as one unit.
  Candidate head families considered:
    - authoring-centered unit labels
    - reading-centered unit labels
    - mixed authoring-and-reading unit labels
    - PublicationReadingUnit
    - PublicationAuthoringUnit
    - PublicationUnit
    - ContentSpan
    - DocumentUnit
  F.18 result:
    - `PublicationUnit` has better SemanticFidelity than authoring-centered unit labels because the unit belongs to the publication lane, not to the authoring process.
    - `PublicationUnit` has better MorphologicalActionFit than mixed authoring-and-reading unit labels because it does not mix author, reader, and unit-boundary roles in one head.
    - `PublicationUnit` has lower AliasRisk than `content span` and `document unit` because `content` and `document` blur episteme, publication form, and carrier.
    - `PublicationUnit` still has nonzero AliasRisk because `publication` itself splits into act or occurrence of publishing, episteme publication, form, generic face, governed MVPK face, unit, and carrier; therefore load-bearing uses keep the nearby definition or explicit publication stack.
  Current status: admitted reusable FPF head for this pattern and its selected campaign scope; use a more specific already accepted head where one governs the text under repair.
```

#### E.10.SEMIO:4.4 - Rewrite Rules

##### E.10.SEMIO:4.4.1 - primary described entity and local topic wording

Do not replace every topic-like or object-like phrase with `describedEntity`.
Classify the sentence first.

| If local wording meant... | Rewrite as... |
| --- | --- |
| the entity described by a claim-bearing episteme | `describedEntity`, `DescribedEntityRef`, `primary described entity` |
| the described-entity stability requirement for one bounded publication unit | primary described entity of the claim-bearing episteme carried in that `PublicationUnit`; otherwise exact non-claim-bearing kind or reference, or plain `topic`, `subject` only when no normative slot is live |
| a review target | `review target`, exact review-facing target packet, FPF pattern, pattern section, or file-carrier set only when the file-carrier reading is live |
| a local table or paragraph topic with no claim-bearing slot | `topic`, `subject`, or direct noun |
| an FPF-side pattern, pattern section, accepted `DRR`, FPF publication, FPF view, document with named source-basis, evidence-basis, architecture-basis, or review-basis role, or support companion being improved | exact FPF pattern, pattern section, accepted `DRR`, FPF publication, FPF view, document with named source-basis, evidence-basis, architecture-basis, or review-basis role, or support companion |
| a project-side episteme, publication, record, carrier, or activity under work | exact project episteme, view, publication, `A.10` evidence path, typed evidence record, `A.20` constraint or adjudication decision record, `A.21` `GateDecision`, `A.21` `DecisionLogRef`, `B.3` assurance or engineering-justification record, typed status record whose FPF status pattern is named, `A.2.8` `U.Commitment`, `C.11` `ChoiceResult`, `C.11` decision record, `A.6.A` action invitation, `A.15.1` dated `U.Work` occurrence, `A.15` `U.WorkPlan`, `U.Method`, `U.MethodDescription`, carrier relation, or front-end relation |

Required check:

```text
described-entity rewrite:
  sentence under repair:
  claim-bearing episteme live? yes or no
  describedEntity, grounding, ClaimGraph, viewpoint slots triggered:
  PublicationUnit reading, if any:
  review-target reading, process-description reading, source-basis-document reading, if any:
  chosen replacement:
  distinction preserved:
```

##### E.10.SEMIO:4.4.2 - publication-unit wording that implies authoring or reading work

When a phrase makes the bounded unit sound like authoring work or reading work, split the sentence by live kind.

| If local wording meant... | Rewrite as... |
| --- | --- |
| bounded human-inspected unit inside a publication | `PublicationUnit` |
| the act of writing or editing | authoring work, editing work, or `U.Work`, `U.WorkPlan`, `U.MethodDescription` where live |
| a pattern body or section | exact pattern body, pattern section, or `PublicationUnit` of that pattern |
| a file or rendered medium | carrier, front-end, rendering, or document with named source-basis, evidence-basis, architecture-basis, or review-basis role |
| a publication form | publication form |
| a generic publication face | generic publication face, or `U.View` only when the governing pattern makes that relation live |
| a governed MVPK face | governed MVPK face, and `U.EpistemeView` only under MVPK constraints |
| a claim-bearing episteme or exact episteme species | `U.Episteme`, `U.EpistemePublication`, episteme-lane `U.View` with explicit episteme tether, or exact episteme species |

Do not make a permanent technical modifier by joining authoring, reading, and unit-boundary roles.
That mix hides whether the sentence is about a publication unit, authoring work, reader inspection, or a carried claim.

##### E.10.SEMIO:4.4.3 - `content`

Do not use `content` as a governing head.
Split it into:
- claim-bearing episteme content;
- publication-unit text;
- publication form;
- generic publication face;
- governed MVPK face;
- carrier data;
- record payload;
- pattern section;
- source-basis excerpt;
- review target.

Plain explanatory prose may use `content` only when the sentence does not carry ontology, authority, or admissibility.

##### E.10.SEMIO:4.4.4 - `publication`

Every load-bearing `publication` sentence must say which publication construction is live:
- act or occurrence of publishing, or publishing work;
- `U.EpistemePublication`;
- publication form;
- generic publication face;
- governed MVPK face;
- `PublicationUnit`;
- carrier or rendering;
- document with named source-basis, evidence-basis, architecture-basis, or review-basis role;
- external-standard publication;
- project record publication.

If the sentence says a publication "supports", "authorizes", "proves", "permits", or "makes admissible" something, split the basis: fill `relationLoad` when a relation claim is live, fill `admissibleUse` when a boundary-use claim is live, and fill `projectSourceLoad` when project-side records, evidence paths, gate decisions, constraint or adjudication decisions, assurance records, work, action invitations, speech acts, commitments, methods, or carriers are live. If either side is not triggered, say so explicitly rather than filling it with generic support.

##### E.10.SEMIO:4.4.5 - `surface`, `view`, `face`

Do not treat these as synonyms.

| Word | First split |
| --- | --- |
| `view` | `U.View`, `U.EpistemeView`, reader viewpoint, UI view, support view, or review view |
| `face` | generic publication face, governed MVPK face, UI face, or public-facing support publication |
| `surface` | If the final term is a `SurfaceKind` value, use only `PublicationSurface` or `InteropSurface`. Otherwise rewrite the occurrence to generic publication face, governed MVPK face, publication carrier, interop carrier, UI or front-end face, support publication, support companion, or carrier relation. |

If the sentence can survive only because these are blurred, the sentence is not ready.

##### E.10.SEMIO:4.4.6 - `source`, `target`

These are relation words, not final kinds.

Split `source` into source `U.Episteme`, source `U.EpistemePublication`, `U.View` over a source `U.Episteme`, document with named source-basis, evidence-basis, architecture-basis, or review-basis role, `A.10` evidence path, authority-reference relation, named FPF pattern cited as source, file carrier, source frame, source context, relation slot on the source side of a named relation, or exact project-side FPF kind and reference.

Split `target` into described entity, target `U.Episteme`, review target, receiving FPF pattern, project target, work target, target publication form, exact project-side FPF kind and reference, target frame, target context, or relation slot on the target side of a named relation.

Do not publish "source and target" if the selected relation needs the actual FPF kind.

##### E.10.SEMIO:4.4.7 - `artifact`, `material`, `output`, `deliverable`

These are high-risk umbrella words.
Before accepting them, test publication-related and record-related readings first:
- `U.Episteme`;
- `U.View`, `U.EpistemeView`;
- publication form;
- generic publication face;
- governed MVPK face;
- `PublicationUnit`;
- carrier, front-end, or rendering;
- exact project-side FPF kind and reference;
- work result, work-occurrence output, or project record named by the governing FPF pattern;
- evidence carrier;
- document with named source-basis, evidence-basis, architecture-basis, or review-basis role;
- review target.

If none fits, record the candidate missing kind in architecture first; do not invent it inside pattern prose.

##### E.10.SEMIO:4.4.8 - `record`

Use `record` only when the governing FPF pattern or project practice names the record kind and relation. The nearby wording must say which FPF kind the record instantiates or records, for example:

- `A.10` evidence path or evidence record for a named claim;
- `A.21` `GateDecision` or `DecisionLogRef`;
- `A.20` constraint or adjudication decision record;
- `C.11` `ChoiceResult` or decision record;
- `A.15` `U.WorkPlan`, `A.15.1` dated `U.Work` occurrence, or other named work record;
- `A.2.8` `U.Commitment` or `A.2.9` `SpeechAct` publication;
- `U.RoleAssignment` or status-register entry under the named governing pattern;
- `E.19` review run record or another named review record whose review target and review relation are explicit;
- process run record in process documents.

Do not let `record` mean "any file that remembers something", "the missing source", or "the thing to create when support is absent". If required support is absent, create a prospective repair request, future decision request, prospective work-plan entry, or explicit source-gap note; it does not backdate support.

##### E.10.SEMIO:4.4.9 - `model`, `diagram`, `screen`, `dashboard`, `table`, `note`, `memo`, `summary`, `explanation`

These are recognition examples, not governing kinds.
Classify each occurrence as one of:
- episteme or episteme publication;
- `U.View`, `U.EpistemeView`;
- publication form;
- generic publication face;
- governed MVPK face;
- `PublicationUnit`;
- carrier, front-end, or rendering;
- exact project-side FPF kind and reference;
- explanation and source-finding relation under `E.17.EFP`;
- evidence, currentness, and provenance relation under `A.10`;
- gate-bearing claim or effect under `A.20` or `A.21`;
- assurance and engineering-justification record under `B.3`;
- work and reliance source-restoration relation under `A.15.4`.

Keep the ordinary example word only after the governing kind is visible nearby.

##### E.10.SEMIO:4.4.10 - `reader`, `reviewer`, `author`, `operator`

Do not use people-position words as hidden kind names.

Use:
- `working reader` or `intended practitioner` for ordinary usability;
- `engineer-manager` when the FPF use case is the engineer-manager applying the pattern in work;
- `reviewer` only for a participant in a named review relation; use review process, review gate, or review target for the process, gate, or object;
- `author` only for authoring or editing work;
- `operator` only for an actual `U.Role`, operator position or process operator in the selected context.

If a text says "reader-facing" or "review-facing", it must also name what is facing that person: generic publication face, governed MVPK face, packet, document with named source-basis, evidence-basis, architecture-basis, or review-basis role, `PublicationUnit`, carrier, or UI or front-end.

##### E.10.SEMIO:4.4.11 - `owner`, `home`, `host`, `locus`

These are not interchangeable.

`owner` may be kept as architecture-discussion shorthand only when the live kind is an explicit responsibility assignment or stewardship assignment. It is not an admissible substitute for `pattern`, `DRR`, `U.Episteme`, `U.EpistemePublication`, publication unit, file carrier, or project record.

Split into:
- governing FPF pattern relation or authority-reference relation;
- named governing source set;
- explicit source-maintenance role assignment;
- file carrying FPF pattern text;
- file carrier;
- publication unit;
- process-control role assignment;
- role assignment;
- evidence record or evidence source;
- receiving FPF pattern or project target;
- support root.

Never use `owner` to avoid deciding whether the sentence is about a governing FPF pattern, authority-reference relation, file carrier, responsibility assignment, or process control.

##### E.10.SEMIO:4.4.12 - `route`, `branch`, `handoff`, `path`, `trajectory`, `move`, `flow`

Recover the movement, control, and temporal relation stack before using these words:
- `A.16` local move;
- `A.16.0` trajectory account;
- `A.19`, `C.2.2a` position in characteristic space or state space;
- `B.2.5` control relation, control-layer relation;
- process handoff;
- selector relation or selection mechanism;
- work transfer;
- `E.18` path publication;
- `A.6.3`, `A.6.4` episteme morphism or retargeting.

If no movement, control, and temporal relation is live, keep the word ordinary and non-authorizing.

##### E.10.SEMIO:4.4.13 - `use`, `supported use`, `action`, `effect`

Split the word before accepting it:
- applying an FPF pattern to a problem situation;
- reading or interpreting a publication, view, record, cue, or carrier;
- relying on a named project episteme, a named source-basis document, or an exact project-side FPF kind and reference for a named claim or effect;
- admissible act, work, or claim under a named FPF pattern, `A.6.P` relation claim, relation phrase, or exact project-side FPF kind and reference;
- non-admissible act, work, or claim requiring one other named value: FPF pattern, `A.6.P` relation claim, relation phrase, exact project-side FPF kind and reference, `C.11` `ChoiceResult`, `C.11` decision record, `A.6.A` action invitation, `A.15` `U.WorkPlan`, `A.15.1` dated `U.Work` occurrence, `U.Method`, `U.MethodDescription`, `A.20` constraint or adjudication decision record, `A.21` `GateDecision`, `A.21` `DecisionLogRef`, `A.10` evidence path, typed evidence record, `B.3` assurance or engineering-justification record, typed status record whose FPF status pattern is named, carrier relation, or front-end relation;
- planned work;
- actual `U.Work`;
- evidence of interpretation or effect;
- gate or admission decision.

Do not let `supported use` become a generic capability of a document.
The load-bearing wording names the exact `admissibleUse` target and non-admissible neighboring use, `relationLoad` when a relation claim is live, and `projectSourceLoad` when an exact project-side FPF kind and reference is live.
If the sentence says "supported", it must name the exact `admissibleUse` target and non-admissible neighboring use, `relationLoad` when a relation claim is live, and `projectSourceLoad` when an exact project-side FPF kind and reference is live. Do not satisfy the rule by naming only a project record, evidence record, gate record, assurance record, engineering-justification record, only an FPF pattern, or one mixed project-side entry when several `A.7` or `A.15` role, method, work-plan, and actual-work kinds are live.

##### E.10.SEMIO:4.4.14 - `sign`, `concept`, `denotat`, and school-semiotic labels

Do not import the school-semiotic triad as architecture ontology.
When a source or review text says `sign`, `signifier`, `signified`, `concept`, `denotat`, `representamen`, `interpretant`, or `sign vehicle`, apply the composite recovery order before the term appears in FPF-facing prose.

Possible recoveries include:
- `U.Episteme` or exact episteme species;
- `describedEntity`, grounding, reference-plane relation;
- `U.View`, `U.EpistemeView`;
- publication form, generic publication face, governed MVPK face, or `PublicationUnit`;
- carrier, front-end, or rendering;
- cue, displayed wording, mark, status display, credential display, provenance mark, signature evidence;
- evidence record, gate record, work-state record, commitment record, role-assignment record, or another exact project-side FPF kind and reference;
- FPF pattern, pattern section, accepted `DRR`, FPF publication, or FPF view when the object is on the FPF side.

Use `concept` only where current `FPF` already has the relevant concept-set, UTS, local-meaning, or Part F machinery live.
Otherwise recover the exact episteme slot, relation, or typed record.

##### E.10.SEMIO:4.4.15 - `pattern`, generic FPF-side object wording, `locus`, `row`, `target`

`Pattern` is not a free synonym for regularity.
If the intended object is an FPF pattern, write `FPF pattern` or name the exact pattern.
If it is not an FPF pattern, do not write `recovered FPF construction` as the final value. Choose one recovered value by sentence function: episteme, view, publication, publication form, generic publication face, governed MVPK face, `PublicationUnit`, carrier relation, front-end relation, exact project-side FPF kind and reference, document with named source-basis, evidence-basis, architecture-basis, or review-basis role, review target, relation record, relation phrase, `C.11` `ChoiceResult`, `C.11` decision record, `A.6.A` action invitation, `A.15` `U.WorkPlan`, `A.15.1` dated `U.Work` occurrence, `U.Method`, `U.MethodDescription`, `A.20` constraint or adjudication decision record, `A.21` `GateDecision`, `A.21` `DecisionLogRef`, `A.10` evidence path, typed evidence record, `B.3` assurance or engineering-justification record, or typed status record whose FPF status pattern is named.

Avoid generic FPF-side object wording, generic named-target wording, `locus`, `row`, and `host` when they hide kind.
Use them only when the kind is literally a table row, document with named source-basis role, file carrying FPF pattern text, or review target and the sentence does not need a narrower FPF kind.
For FPF-facing semantic work, these are candidate recoveries, not a group kind: exact FPF pattern, pattern section, accepted `DRR`, FPF publication, FPF view, typed record, relation record, or relation phrase. Choose one by sentence function.

##### E.10.SEMIO:4.4.16 - Union-field unpacking under A.6.P

Do not write `authority-bearing FPF pattern`, `authority-bearing FPF row`, `exact FPF row`, `selected FPF pattern, record, or relation`, `governing FPF relation`, or `required project record or action` as final fields.

When one of these union-fields appears, make the A.6.P choice explicit:
- if the sentence is making a relation claim, recover the `RelationKind`, endpoints, slots, qualifiers, scope, time, viewpoint, and admissibility target, then express the result as a relation record or relation-stack specification;
- if the sentence is not making one relation claim, unpack the current context into exact FPF-side kind, reference, or relation and one exact project-side FPF kind with its reference, or state that no project-side FPF kind is triggered;
- if the same unpacking recurs across cases with one stable repair load, open a light A.6.P specialization candidate rather than minting a vocabulary-wide replacement field.

This unpacking is mandatory when a publication, display, cue, explanation, dashboard tile, schema, signature, badge, or generated output is being read as evidence, gate passage, work, permission, approval, commitment, release, safety proof, assurance, or engineering justification.

Do not fill one project-side slot with whichever nearby FPF kind is easiest to name. A project publication or record is a description-side item or record-side item; `A.15.1` dated `U.Work` occurrence, `A.6.A` action invitation, `A.2.9` `SpeechActRef`, `A.2.8` `U.Commitment`, and `U.Method` and `U.MethodDescription` belong to different FPF kinds.

##### E.10.SEMIO:4.4.17 - Heterogeneous kind lists

Do not repair a heterogeneous list by giving it one broader umbrella name.
When a sentence lists unlike candidates such as pattern, `DRR`, publication, `U.View`, carrier relation, front-end relation, exact project-side FPF kind and reference, `C.11` `ChoiceResult`, `C.11` decision record, `A.6.A` action invitation, `A.15` `U.WorkPlan`, `A.15.1` dated `U.Work` occurrence, `U.Method`, `U.MethodDescription`, `A.20` constraint or adjudication decision record, `A.21` `GateDecision`, `A.21` `DecisionLogRef`, `A.10` evidence path, typed evidence record, `B.3` assurance or engineering-justification record, or typed status record whose FPF status pattern is named, do not promote the row to a new kind. Classify the list as one of:
- one live kind selected at minimal sufficient generality;
- a relation stack with typed slots;
- a tuple-like record;
- several alternative cases;
- an indicator of failed ontology.

If the list is a relation stack, name the slots.
If it is a tuple-like record, name the tuple object and its slot semantics.
If it is an alternative-case set, split the cases.
If it is failed ontology, return to architecture before pattern or `DRR` prose depends on the list.

##### E.10.SEMIO:4.4.18 - `strong`, `stronger`, `weak`, `weaker`, `support`

Do not use strength metaphors unless a named FPF scale, evidence class, threshold, or characteristic space is live.

Preferred rewrites:
- `stronger claim` -> wider claim scope, higher evidence requirement, gate or admission threshold, claim requiring world-contact evidence or authority relation, authority claim, or named evidence-support class;
- `weaker claim` -> narrower claim scope, lower evidence-support class, bounded admissible act, work, or claim, `source-loss mode` under `A.6.3.CSC` when a source-to-rendering loss is live, coarsened rendering, or explicit abstain or reopen posture;
- `support` -> evidence support, source-basis support, `relationLoad` when a relation claim is live, exact `admissibleUse` when a boundary-use claim is live, `projectSourceLoad` when an exact project-side FPF kind and reference are live, explanation and source-finding relation, or support-only companion function.

If the sentence cannot name the scale, evidence class, threshold, relation, or source-loss mode, it is not ready for architecture or pattern prose. `A.6.3.CSC` governs load-bearing source-loss-mode governance; `E.10.SEMIO` only forces the wording to recover the exact governing pattern and mode.

##### E.10.SEMIO:4.4.19 - Applying patterns versus procedural calls

FPF patterns are applied in problem situations.
They are not called, invoked, routed through, executed as procedure steps, or chained as an imperative program.

Use `apply pattern`, `use the pattern guidance`, `the pattern governs this problem situation`, or `the case falls under this pattern` when the FPF side is live.
Do not use `project action` as a final class. For project-side activity, choose exactly one live kind for the sentence: `U.Method`; `U.MethodDescription`; `U.Mechanism`; `A.15` `U.WorkPlan`; `A.15.1` dated `U.Work` occurrence; work-result record or result-measurement record; `C.11` `ChoiceResult`; `C.11` decision record; `A.6.A` action invitation; `A.20` constraint or adjudication decision record; `A.21` `GateDecision`; `A.21` `DecisionLogRef`; `A.10` evidence path; typed evidence record; `B.3` assurance or engineering-justification record; typed status record whose FPF status pattern is named; carrier relation; front-end relation; or another accepted project-side FPF kind.
Use `route`, `path`, `branch`, `handoff`, `trajectory`, `move`, or `flow` only after the movement, control, and temporal stack has named the live FPF kind.

##### E.10.SEMIO:4.4.20 - FPF-side and project-side episteme and publication contexts

Semioarchitecture often talks about two different described contexts:
- FPF-side episteme and publication context: `FPF` as episteme, FPF patterns, pattern sections, `DRR`s, FPF publications, FPF views, support documents and documents with named source-basis, evidence-basis, architecture-basis, or review-basis roles, and review targets;
- project-side episteme and publication context: the engineer-manager's project epistemes, publications, views, records, carriers, cues, evidence records, `A.20` constraint or adjudication decision records, `A.21` gate decisions, `A.21` decision-log refs, `B.3` assurance or engineering-justification records, commitments, `A.15.1` dated `U.Work` occurrences, `C.11` `ChoiceResult` values, `C.11` decision records, and `A.6.A` action invitations.

Do not blur them with `source`, `artifact`, `object`, `material`, `target`, `pattern`, or broad `semiosis`.
If both contexts are live, split the sentence into `relationLoad` when a relation claim is live, `admissibleUse` when a boundary-use claim is live, and `projectSourceLoad` when an exact project-side FPF kind and reference are live.
If one context is not live, state `not triggered` rather than leaving a placeholder.


##### E.10.SEMIO:4.4.21 - `decision`, `action`, `work`, `method`, `plan`

Do not let `action` cover every project-side event.
Split:
- decision-making and decision records under `C.11` when a decision is live;
- role, method, and work-plan and actual-work alignment under `A.15`;
- work occurrence, work plan, work record, launch value or finalization value, or gate record under the relevant work patterns or gate patterns;
- action invitation under `A.6.A` when the representation invites an action without itself becoming authority;
- `A.15.1` dated `U.Work` occurrence when the live `A.15` object is work; `A.2.9` `SpeechActRef` when the live act is a communicative act; `A.2.8` `U.Commitment` when the act institutes a commitment.

P2W language from TGA is not a generic `source-to-work` slogan.
Use it only when the chain from principles, theories, and signatures through method choice, work planning, work execution, result measurement, and cycle return is actually live.

##### E.10.SEMIO:4.4.22 - Whole-corpus trigger use

When a whole-corpus cleanup is selected, use this pattern's trigger guide over claim-bearing FPF and FPF-facing project text.

Do not do a global string replacement. Classify each unclear term occurrence by the smallest sufficient rewrite mode and preserve accepted FPF names unless a separate accepted naming decision changes them.

##### E.10.SEMIO:4.4.23 - `case`, `scenario`, `example`, `pilot`, `anti-case`

These words are useful for recognition and testing, but they often hide whether the text is talking about a project situation, evidence, a worked slice, a negative control, or a decision basis.

Split before use:
- working problem situation;
- worked case or example;
- pilot case;
- anti-case, negative control;
- evidence case;
- comparison case;
- source example;
- benchmark case;
- candidate corpus example.

A case can illustrate or test a pattern.
It does not by itself become evidence, a pattern, a `DRR`, a source basis, or an authority-reference relation.
If the case is being used to justify a claim-bearing text change, choose and name each live object or relation separately: evidence record or evidence path, decision basis or decision record, authority relation, relation to a governing FPF pattern, or relation to an accepted `DRR`.

##### E.10.SEMIO:4.4.24 - `basis`, `context`, `scope`, `frame`

These are boundary, context, relation, and scope words.
They must not stand as final kinds.

Split:
- source basis;
- decision basis;
- evidence basis;
- comparison basis;
- threshold basis;
- grounding basis;
- admissibility basis;
- review context packet;
- bounded context;
- claim scope;
- viewpoint frame or reference frame.

If a basis changes what may be done, fill `admissibleUse`; fill `relationLoad` only when a relation claim is live, and fill `projectSourceLoad` when an exact project-side FPF kind and reference are live.
If context changes the described entity, apply the `describedEntity`, grounding, and reference-plane checks before any bridge, parity, or identity claim.

##### E.10.SEMIO:4.4.24a - translation and multilingual heads

A translated term is not automatically the same FPF head. A translation may preserve reader access while losing kind precision, admissible use, or source-support posture. A bilingual alias is not a Bridge by itself and does not create equivalence, substitution, UTS admission, or cross-context naming relation.

When translated wording carries load, recover the exact FPF kind, local head, publication construction, source relation, and admissible use before accepting the translation. A translated explanation is a derivative rendering; operative claims need source links and `E.17.EFP` or `A.10` when reliance is live. A translated `PublicationUnit` may preserve form while shifting primary described entity or carried publication move; apply `E.17.AUD` or `E.17.AUD.OOTD` when that shift is live. Local translated heads may use `E.17.AUD.LHR` or `E.10.SEMIO` without full `F.18` unless durable cross-context naming, UTS row, Core-facing term, or reusable FPF head is intended.
##### E.10.SEMIO:4.4.25 - `state`, `status`, `posture`, `readiness`

Do not let state language become a maturity adjective or gate claim.

Classify:
- position in a named `U.CharacteristicSpace`;
- language-state chart position;
- protocol state or process state;
- status record;
- role assignment or status assertion;
- publication posture;
- release or gate readiness claim;
- temporal claim under `C.27`;
- dynamics claim under `A.3.3`.

If the word is used to justify movement, routing, gate entry, release, or work, the text must name the characteristic-space slot, threshold basis, evidence or witness, and publication lane or carrier lane that makes the claim reviewable.

##### E.10.SEMIO:4.4.26 - `claim`, `evidence`, `witness`, `ground`, `proof`

`Claim` is not a synonym for sentence or prose.
`Evidence` is not a synonym for source, proof, approval, or confidence.

For `claim`, recover:
- claim-bearing episteme;
- claim node, claim content;
- described entity or claim referent;
- viewpoint and representation scheme when live;
- admissibility target when the claim is used.

For evidence-like words, recover:
- evidence record or evidence path;
- witness or source pin;
- grounding relation;
- validation result;
- assurance argument component;
- provenance mark only as provenance, not as evidence by itself.

If evidence is being read as engineering justification, gate passage, permission, safety proof, or release confidence, apply the exact neighboring pattern or use the exact project-side FPF kind and reference instead of strengthening the evidence word.

##### E.10.SEMIO:4.4.27 - `authority`, `permission`, `approval`, `commitment`, `obligation`

These are deontic claims or claims carrying an authority-reference relation, not visual or rhetorical properties.

Recover:
- role assignment;
- speech act or issuing act;
- commitment record;
- policy claim;
- authority relation;
- gate record or decision record;
- authority-changing decision;
- delegated permission;
- contestability, revocation, expiry condition.

Labels, badges, signatures, dashboards, certificates, comments, reviewer praise, and generated explanations may cue authority-looking cases.
They do not carry authority unless the authority act, authority record, authority-reference relation, and evidence path are named.

##### E.10.SEMIO:4.4.28 - `profile`, `harness`, `catalog`, `registry`, `index`, `map`

These usually point to a support profile, review harness, registry record, catalog publication, navigation index, map, publication form, support publication, publication-support relation, or relation between one support publication and the publication unit or project record it supports. Choose that exact kind before writing; do not leave `support record` as the recovered head unless the named FPF pattern really defines that record kind.
Treat one as a governing FPF pattern body, accepted campaign `DRR`, named current architecture document, or relation to one of them only when the named FPF pattern, accepted `DRR`, architecture document, relation record, or relation phrase is given by value.

Split:
- support profile;
- review harness;
- source map;
- navigation index;
- registry record;
- catalog publication;
- benchmark harness;
- entry support or discoverability support;
- governing pattern body.

If the named support publication, support profile, review harness, registry record, index, or map mainly helps readers find, compare, test, or review something, keep it support-only until a named FPF pattern or accepted `DRR` records the recurring action-guidance gain by value.

##### E.10.SEMIO:4.4.29 - `entry`, `front door`, `corridor`, `route`

These terms often mix navigation, recognition, movement, and authority.

Split:
- entry publication or navigation support;
- first-use recognition text;
- navigation-bearing publication;
- movement, control, and temporal relation;
- process sequence;
- corridor overview;
- exact FPF pattern named by the live problem; if a cluster or relation between patterns is genuinely live, name the exact cluster phrase or relation phrase and the governing FPF patterns by value.

An entry can make the right pattern easier to find.
It does not prove the pattern is sufficient, complete, or ready for gate use.

##### E.10.SEMIO:4.4.30 - `same`, `parity`, `identity`, `equivalence`, `mirror`

Similarity is not identity.
Before accepting same, parity, or equivalence wording, name which relation is being claimed:
- mirror file in parity with a governing source;
- same described entity;
- same claim content;
- semantic equivalence;
- bridge relation;
- version identity;
- file or carrier equality;
- source-publication identity;
- no-loss transform.

If the relation is about mirror parity, verify against the governing source or state that the check is not performed.
If the relation is semantic, use `A.6.3`, `A.6.4`, `F.9`, or the selected bridge pattern or equivalence pattern rather than relying on matching labels.

##### E.10.SEMIO:4.4.31 - `file`, `path`, `host`, `packet`, `bundle`, `package`

These are carrier, transport, or package-form words.

Split:
- file or carrier;
- mirror file;
- file carrying FPF pattern text;
- document with named source-basis, evidence-basis, architecture-basis, or review-basis role;
- review-facing target packet;
- review-facing context packet;
- release package;
- pattern package, pattern family, or pattern group under an accepted decision;
- governing source section.

A packet or bundle can carry a review target by value.
It is not automatically the authority-reference status, the target pattern, the accepted review result, or the FPF `authoritySourceRef` target.

##### E.10.SEMIO:4.4.32 - `quality`, `characteristic`, `metric`, `indicator`, `score`

Do not let evaluation words float.

Split:
- `U.Characteristic`;
- characteristic space;
- Q-bundle;
- scale;
- indicator;
- observed value;
- benchmark result;
- review finding;
- decision threshold;
- qualitative judgment with no scale.

`metric` is especially risky because FPF often treats it as imprecise shorthand for scale, value, or indicator machinery.
If the text says a quality improved, name what changed: characteristic, scale, observed value, threshold, decision consequence, or admissible act, work, or claim.

##### E.10.SEMIO:4.4.33 - `slot`, `field`, `row`, `label`, `badge`, `mark`, `cue`

These words are not kinds by themselves.

Split:
- episteme slot;
- relation slot;
- schema field;
- table row;
- row in a pattern body;
- publication label;
- provenance mark;
- status badge;
- pre-articulation cue;
- displayed cue;
- evidence marker.

A label, badge, mark, or cue may trigger review.
It does not prove currentness, identity, authority, evidence, gate passage, or release permission unless the exact source relation and evidence path are named.

#### E.10.SEMIO:4.5 - Rewrite Execution Modes
Use the smallest sufficient mode that preserves the distinction. The template is a semantic safety device, not a form to fill for every ordinary wording cleanup.

##### E.10.SEMIO:4.5.1 - Local prose cleanup

Use this mode when the phrase under repair is non-normative local prose and does not carry ontology, authority, review scope, release posture, admissibility, or a reusable name.

Action: rewrite directly or leave it unchanged. No table row is required.

##### E.10.SEMIO:4.5.2 - Compact semantic rewrite row

Use a compact row for ordinary architecture and support-document cleanup where a sufficient FPF kind, relation record, relation phrase, or tuple-like record can be recovered without minting a new FPF head.

```text
Compact semantic rewrite row:
  file path, if live:
  FPF pattern, if live:
  pattern section, if live:
  sentence reference:
  phrase under repair:
  live sentence function:
  selected exact FPF kind or exact project-side FPF kind:
  `relationLoad` triggered? yes or no
  relation problem, if triggered:
  admissibleUse triggered? yes or no
  projectSourceLoad triggered? yes or no
  relation claim? yes or no
  if relation claim:
    RelationKind:
    endpoint, slot, qualifier notes:
    admissibilityTargetKind:
    admissibilityTargetRef:
  if local current-context unpacking:
    FPF-side kind, reference, or relation:
    exact project-side FPF kind, if live:
    exact project-side reference, if live:
    notTriggeredReason:
  replacement:
  remaining admissible reader move:
  distinction disposition: preserved, split, intentionally retired, still missing
```



##### E.10.SEMIO:4.5.3 - Full semantic rewrite check

Use the full check when the wording may change ontology, introduce or retire a reusable head, change a claim-bearing pattern or document with named source-basis, evidence-basis, architecture-basis, or review-basis role, or resolve a contested source-meaning problem.

```text
Semantic rewrite check:
  file path, if live:
  FPF pattern, if live:
  pattern section, if live:
  sentence reference:
  phrase under repair:
  sentence function:
  distinction carried:
  E.10 head kind and Intension, Description, and Specification reading:
  F.18 naming status: no stable term, reuse, MintNew sketch, DocumentLegacy
  F.18 candidate head families, if naming is live:
  F.18 lexical Q result, if naming is live:
    SemanticFidelity:
    CognitiveErgonomics:
    MorphologicalActionFit:
    AliasRisk:
  A.6.P trigger? yes or no
  A.6.P selected relation kind, slots, qualifiers, if live:
  claim-bearing episteme live? yes or no
  FPF kind stack:
  describedEntity, grounding, ClaimGraph, viewpoint slots triggered:
  E.17 and MVPK publication form, generic face, governed MVPK face, view, carrier split:
  PublicationUnit reading, if any:
  FPF-side or project-side sentence:
  `relationLoad` triggered? yes or no
  relation problem, if triggered:
  admissibleUse triggered? yes or no
  projectSourceLoad triggered? yes or no
  relation claim? yes or no
  if relation claim:
    RelationKind:
    QualifiedRelationRecord slots:
    admissibilityTargetKind:
    admissibilityTargetRef:
  if local current-context unpacking:
    FPF-side kind, reference, or relation:
    exact project-side FPF kind, if live:
    exact project-side reference, if live:
    notTriggeredReason:
  rejectedOverread, if live:
  project-side record, work, action, method, carrier crossing:
  heterogeneous-list classification: one live kind, relation stack, tuple-like record, alternative cases, failed ontology, not triggered
  pattern application, project work, decision distinction:
  chosen rewrite:
  remaining admissible reader move:
  distinction disposition: preserved, split, intentionally retired, still missing
  unrecovered wording retained? no, yes, with scope and reason:
  transfer disposition: recovered by value, extension candidate, quote-only, reduced-use cue, blocked transfer, rewrite incomplete, not triggered
```


##### E.10.SEMIO:4.5.4 - Semantic Rewrite Note

Use a semantic rewrite note only when wording carries ontology, authority, evidence, or admissibility load. The note records the original phrase, recovered FPF kind or relation, exact reference when live, project-side FPF kind and reference when live, remaining admissible reader move, and disposition: recovered by value, extension candidate, quote-only, reduced-use cue, blocked transfer, rewrite incomplete, or not triggered.

### E.10.SEMIO:5 - Archetypal Grounding


| Scenario | Show - failure without E.10.SEMIO | Show - repair with E.10.SEMIO |
| --- | --- | --- |
| FPF pattern draft | A draft says a pattern section, host, row, and source all support an action. The reader cannot tell whether this is a pattern, a section as `PublicationUnit`, a `DRR`, a file, or a relation. | The author names the exact FPF pattern, pattern section as part of the episteme or `PublicationUnit`, accepted `DRR`, document with named source-basis, evidence-basis, architecture-basis, or review-basis role, relation record, or relation phrase. The useful next move is then explicit: keep the pattern-application claim, narrow it to source-finding or quote-only use, or apply the exact named governing FPF pattern before action wording is retained. |
| Engineering project publication | A green dashboard tile, certificate badge, or generated explanation is treated as evidence, gate passage, engineering justification, assurance, or permission for work. | The engineer names the generic publication face, governed MVPK face, or carrier, then names the exact project-side FPF kind and reference that makes the work claim admissible: evidence record, `A.20` constraint or adjudication decision record, `A.21` `GateDecision`, `A.21` `DecisionLogRef`, `B.3` assurance or engineering-justification record, `C.11` `ChoiceResult`, `C.11` decision record, `A.6.A` action invitation, `A.15` `U.WorkPlan`, `A.15.1` dated `U.Work` occurrence, `U.Method`, or `U.MethodDescription`. The useful next move is either orientation or source-finding only, or finding or creating the exact evidence, gate, decision, assurance, plan, work, method, or action-invitation value before work or reliance proceeds. The row chooses the live value, not this list. |
| Source-basis text | A source-basis note uses loose wording that says material should be moved without naming whether the target is an FPF pattern, document with a named source-basis role, file carrier, relation record, or project record. | The author recovers whether the target is an FPF pattern, a document with named source-basis, evidence-basis, architecture-basis, or review-basis role, a pattern section, a file carrier, a relation record, or an exact project-side FPF kind and reference whose FPF kind is named. The useful next move is to apply the exact receiving FPF pattern or edit the exact named support document or reference; if the meaning remains unclear, the phrase becomes quote-only or blocked transfer. |


### E.10.SEMIO:6 - Bias-Annotation

| Lens | Risk | Mitigation |
| --- | --- | --- |
| Ontology | Exact-sounding words become a new parallel ontology. | Require recovery to current FPF kinds and relations before reuse. |
| Usability | The rule becomes too heavy for ordinary edits. | Use the smallest sufficient rewrite mode; reserve the full check for load-bearing wording. |
| Preservation | Source-basis text is mistaken for direct pattern authority. | Keep source-basis status separate from the ordinary pattern guidance. |
| Checklist ritual | The rule becomes a form to satisfy rather than a wording action to perform. | Put the action in `Solution`; use row evidence only when wording carries load. |

### E.10.SEMIO:7 - Conformance Checklist

| Item | Check |
| --- | --- |
| CC-E10.SEMIO-1 | Every load-bearing broad head names the recovered FPF kind, relation record, relation phrase, tuple-like record, exact project-side FPF kind and reference when `projectSourceLoad` is live, or explicit non-transfer disposition. The selected project-side entry must be one exact live kind, such as `C.11` `ChoiceResult`, `C.11` decision record, `A.6.A` action invitation, `A.15` `U.WorkPlan`, `A.15.1` dated `U.Work` occurrence, `U.Method`, `U.MethodDescription`, `A.20` constraint or adjudication decision record, `A.21` `GateDecision`, `A.21` `DecisionLogRef`, `A.10` evidence path, typed evidence record, `B.3` assurance or engineering-justification record, typed status record whose FPF status pattern is named, carrier relation, front-end relation, or not-triggered alternative. |
| CC-E10.SEMIO-2 | Slash compounds and heterogeneous lists are not left as final kinds unless they are accepted tokens, carrier syntax, plain synonym pairs with no load, or explicitly recovered tuple-like constructions or relation constructions. |
| CC-E10.SEMIO-3 | FPF pattern-application claims and project-side publication, record, work, method, carrier, and action claims stay separated when both are live. |
| CC-E10.SEMIO-4 | Broad admissibility, support, source, target, publication-face, carrier, placement, movement, procedure-like, topic-like, and pre-FPF semiotic wording requires semantic recovery when it carries ontology, authority, evidence, or admissibility load. |
| CC-E10.SEMIO-5 | Unclear meaning is not rewritten by author guesswork; it is classified as quote-only wording, reduced-use cue, blocked current transfer, or understandable FPF extension candidate. |
| CC-E10.SEMIO-6 | Any newly stable name passes `F.18`; any relation claim passes `A.6.P`; any admissibility claim fills `admissibleUse` and uses `A.6.B` when L-, A-, D-, and E-claim separation is live; any claim-bearing episteme, exact episteme species, episteme-lane view, or exact project-side FPF kind and reference passes `C.2.1` or the named neighboring FPF pattern as needed; any publication, view, or carrier claim passes `E.17.0`, `E.17`, and MVPK as needed. |
| CC-E10.SEMIO-7 | The final text remains action guidance under `E.2` `P-2` and `E.12`: it tells the author what wording action to take, what overread to block, why the distinction still matters to the working reader, and what remaining admissible reader move or neighboring-pattern handoff remains. When both Tech and Plain registers are live, the Plain or didactic line maps back to the recovered Tech reading under `E.10:6.2`. A rewrite fails this check if the repaired wording is typed and relation-correct but no longer tells the working reader why the distinction matters, what admissible move remains, or which neighboring FPF pattern now carries the live claim. If the edited locus is load-bearing early recognition prose such as a Problem frame, Problem section, example, or worked slice, the check must confirm that the broad working situation and first useful move still survive. This check does not require flattening intentional didactic metaphors when they are ordinary recognition aids or when their load remains recoverable from the Tech reading. It does fail if a Plain or didactic line carries ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility load that cannot be recovered from the Tech reading or named handoff. |

| CC-E10.SEMIO-8 | This pattern does not rename existing FPF patterns or mint reusable heads without `F.18` and `A.6.P`. |


#### E.10.SEMIO:7.1 - Current Scan Reading
For conformant text cleanup, high-risk phrases are not automatically wrong. The rows below are candidate recovery prompts, not group kinds. Choose the recovered value by sentence function before reuse:
- topic-like or object-like wording: recover episteme slots or non-claim-bearing project kind;
- publication-unit wording that implies authoring or reading work: distinguish `U.Episteme`, `U.EpistemePublication`, `PublicationUnit`, file, support note, review target;
- `content`: usually one of claim graph, text span, publication unit, carrier bytes, or document with named source-basis, evidence-basis, architecture-basis, or review-basis role;
- primary-object field names: use `primaryDescribedEntity` when claim-bearing or exact non-claim-bearing kind or reference when no episteme slot is live;
- `surface`: keep `PublicationSurface` or `InteropSurface` only when exact `SurfaceKind` discipline is live; otherwise rewrite to generic publication face, governed MVPK face, publication carrier, interop carrier, UI or front-end face, support publication, exact named support record, or carrier relation;
- `artifact`, `material`, `output`, and `content`: do not let them stay as heads in architecture or pattern prose when they carry ontology or authority;
- `source`, `target`: acceptable only when the recovered source kind, target kind, and any live relation slot are also named;
- `reader`, `reviewer`: safe only when the word really names a usability reader, review participant, or review process; otherwise name the generic publication face, governed MVPK face, packet, or `PublicationUnit`;
- pre-FPF semiotic vocabulary: recover FPF episteme kinds, publication kinds, view kinds, carrier kinds, and record kinds before reuse; do not rebuild semioarchitecture on a concept-sign-denotation triad;
- generic FPF-side object wording, `locus`, `row`, `host`, or `target`: choose the exact recovered value: FPF pattern, pattern section, accepted `DRR`, FPF publication, FPF view, document with named source-basis, evidence-basis, architecture-basis, or review-basis role, file carrier, review target, typed record, relation record, or relation phrase;
- `supported use`: replace with the exact `admissibleUse` target and non-admissible neighboring use, `relationLoad` when a relation claim is live, and `projectSourceLoad` when an exact project-side FPF kind and reference is live;
- `strong`, `stronger`, `weak`, `weaker`: replace with scope, evidence class, threshold, gate or admission threshold, `source-loss mode` under `A.6.3.CSC` when a source-to-rendering loss is live, coarsened rendering, or explicit abstain or reopen posture;
- `authority-bearing FPF pattern or row`: split into exact FPF pattern or pattern section, `relationLoad` when a relation claim is live, exact `admissibleUse` when a boundary-use claim is live, and `projectSourceLoad` when an exact project-side FPF kind and reference are live;
- `route`, `call`, `invoke`, or procedure-like pattern wording: replace with pattern application or with exact project-side `U.Work` occurrence, `U.Method`, `C.11` decision value, or `A.6.A` action invitation.

High-risk residue classes:
- pre-FPF semiotic vocabulary must be restored to FPF kinds by context;
- FPF-side umbrellas: generic FPF-side object wording, generic named-target wording, `locus`, `row`, `host`, and `source` must be unpacked into the exact recovered value, such as `FPF pattern`, `pattern section`, `DRR`, `FPF publication`, `U.View`, document with named source-basis, evidence-basis, architecture-basis, or review-basis role, file carrier, relation record, relation phrase, or file-carrier phrase;
- project-side umbrellas: `artifact`, `material`, `output`, `screen`, `dashboard`, `credential`, `badge`, and `explanation` must be unpacked into one exact recovered value, such as publication, generic publication face, governed MVPK face, publication form, carrier relation, front-end relation, exact project-side FPF kind and reference, `A.10` evidence path, typed evidence record, `A.20` constraint or adjudication decision record, `A.21` `GateDecision`, `A.21` `DecisionLogRef`, `B.3` assurance or engineering-justification record, typed status record whose FPF status pattern is named, `C.11` `ChoiceResult`, `C.11` decision record, `A.6.A` action invitation, `A.15` `U.WorkPlan`, `A.15.1` dated `U.Work` occurrence, `U.Method`, `U.MethodDescription`, work-result record, or result-measurement record;
- admissibility phrases: `supported use`, neighboring use not carried by the current pattern, insufficient evidence-support posture, and similar formulas must name the exact `admissibleUse` target and non-admissible neighboring use, `relationLoad` when a relation claim is live, and `projectSourceLoad` when an exact project-side FPF kind and reference is live;
- pattern-control metaphors: `route`, `call`, `invoke`, `exit`, `path`, `branch`, `chooser`, and `workflow` must be checked for declarative pattern application versus real movement, control, and temporal claims.

### E.10.SEMIO:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Avoidance |
| --- | --- | --- |
| Token swap | Replace `surface` with `face` or `host` with `file` without recovering kind and sentence function. | Apply head-kind and relation recovery before rewriting. |
| Group-kind list | Leave a list such as `pattern, record, relation, or action` as if the list names one kind. | Decide whether the sentence needs one kind, a relation record, a tuple-like record, alternative cases, or a blocked ontology. |
| Type-correct but inert rewrite | All overread is removed, all heads are typed, and no practical force remains: the reader can see that local checks passed but cannot tell why the distinction matters, what to do, or where the live claim moved. | Recover the didactic or recognition function in admissible wording, keep any Plain line mapped to the recovered Tech reading when both registers are live, state the remaining admissible reader move, or demote the phrase to reduced-use cue, quote-only wording, blocked transfer, or rewrite incomplete instead of pretending the repair landed. |
| Expressive overread rebound | A repair tries to restore practical force with a memorable Plain or didactic line, but that line carries ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility load not recoverable from the Tech fields, exact FPF kind, recovered relation, project-side source reference, disposition, or named handoff. | Rewrite the line as ordinary recognition aid mapped to the recovered Tech reading under `E.10:6.2`, recover the load through the exact Tech fields, name the neighboring-pattern handoff that carries the live claim, or demote the phrase to reduced-use cue, quote-only wording, blocked transfer, or rewrite incomplete. |
| Pillar-blind precision pass | A broad cleanup proves trigger removal and kind recovery, but never checks whether `E.2` `P-2`, `E.6`, `E.8`, or `E.12` still let the intended reader see the working situation, why it matters, and what first useful move remains. | For load-bearing Problem frames, Problem sections, recognition texts, examples, and worked slices, state the remaining admissible reader move or named neighboring-pattern handoff. Preserve intentional didactic metaphors when they are ordinary recognition aids or when their load maps back to Tech. If the didactic function was harmed, repair the wording in admissible Plain mapped to Tech, or mark the rewrite incomplete instead of accepting type-correct but inert wording. |
| Source-status leakage | Carry a source-companion header into a pattern and let `Authority: none` or `Current use` define the new pattern. | State current pattern status in the pattern header and relations. |
| Pattern as procedure | Say the pattern is called, routed, invoked, or chained as if it were executable code. | Say the FPF pattern is applied in a problem situation; name exact project-side `U.Work` occurrence, `U.Method`, `C.11` decision value, or `A.6.A` action invitation when project activity is live. |
| Strength metaphor | Say a claim is strong or weak without a characteristic, threshold, evidence class, scope, gate, or admissibility relation. | Name the exact comparison basis or replace the metaphor with the recovered admissibility relation. |

### E.10.SEMIO:9 - Consequences

| Benefit | Trade-off and mitigation |
| --- | --- |
| Prevents parallel semio ontology from entering FPF prose. | Adds a small recovery step before apparently simple rewrites; mitigate by using the smallest sufficient mode. |
| Preserves accepted glossary and rules without turning source-basis status lines into accidental pattern authority. | Requires a clear separation between pattern guidance and source-basis status. |
| Makes unclear meaning fail closed. | Some attractive phrases will not be accepted until their kind or relation is actually recovered. |
| Improves DRR and pattern drafting discipline. | Authors must resist convenient lists and umbrellas when one exact kind or relation is needed. |

#### E.10.SEMIO:9.1 - Operating Consequence
For new semio architecture prose:
- start from FPF kinds and relations, not from familiar publication nouns and document nouns;
- use `PublicationUnit` for bounded publication units;
- use `describedEntity` only when the episteme slot is live;
- keep publication form, generic publication face, governed MVPK face, view, carrier, document with named source-basis, evidence-basis, architecture-basis, or review-basis role, review target, and exact project-side FPF kind and reference separate;
- name `relationLoad`, `admissibleUse`, and `projectSourceLoad` separately when more than one is live;
- classify heterogeneous kind lists before writing a sentence that depends on them;
- say that FPF patterns are applied in problem situations, not called or routed as procedures;
- leave accepted FPF names untouched unless a separate accepted naming decision authorizes a rename.

Operationally, each rewrite should:
- separate FPF-side episteme and publication context from project-side episteme and publication context whenever both are present;
- name `relationLoad`, `admissibleUse`, and `projectSourceLoad` separately when a publication, display, cue, or explanation is read as evidence, gate, constraint, adjudication, decision support, work permission, assurance, or engineering justification;
- classify heterogeneous lists before naming them: one live kind, relation stack, tuple-like record, alternative cases, not-triggered alternatives, or failed ontology;
- say that FPF patterns are applied in problem situations, while project records, publications, views, carriers, and actions are worked with in project practice;
- avoid strength metaphors unless the characteristic, scale, threshold, evidence class, or admissibility relation is named.

For cleanup of existing conformant texts:
- do not do a global string replacement;
- classify each unclear term occurrence by the smallest sufficient rewrite mode;
- use the full semantic rewrite check only when ontology, reusable naming, FPF pattern text, or source-bearing project text is live;
- do not rename accepted FPF patterns from this pattern alone.

### E.10.SEMIO:10 - Rationale

FPF already contains the relevant ontology. The recurring defect was not lack of concepts but ad hoc wording that bypassed them: `source`, `target`, `surface`, `object`, `host`, `route`, `supported use`, and similar terms packed several FPF kinds and relations into one convenient phrase.

The correct repair is therefore not a new umbrella. It is a disciplined recovery action: use `E.2`, `E.10`, `F.18`, `A.6.P`, `A.7`, `C.2.1`, `E.17.0`, `E.17`, and MVPK together until the sentence says what object, relation, publication, view, carrier, record, work, action, or pattern application it means.

Because `E.2` governs all normative FPF patterns, semantic precision is not a value apart from `P-2 Didactic Primacy`. A semio repair may be stricter than the original wording, but if it turns load-bearing reader-facing problem text into a kind inventory with no working situation or first useful move, it has not landed the FPF repair. The remedy is not expressive license and not metaphor removal; the remedy is admissible recognition wording whose load remains recoverable through the Tech reading or a named neighboring-pattern handoff.

The detailed rules remain in ordinary pattern sections, so the pattern is usable as FPF guidance rather than as an external glossary container.

### E.10.SEMIO:11 - SoTA-Echoing

`E.10.SEMIO` does not claim to replace semiotics, terminology science, document engineering, or ontology engineering. Its live claim is narrower: semio-heavy conformant text must recover accepted FPF kinds and relations before it is rewritten, so that episteme, publication, view, carrier, naming, relation, and project-side records are not replaced by ad hoc words.

Full external SoTA comparison is therefore not the governing evidence mode for this definitional specialization. A reduced external practice basis is still required because the pattern governs terminology drift and semantic recovery. The reduced basis supports the recovery discipline; it does not create a new ontology and does not outrank the FPF patterns named below.

| Reduced source idea | Adapted FPF invariant | Rejected shortcut | Recovery anchor |
| --- | --- | --- | --- |
| ISO 704:2022 and ISO 1087:2019 terminology work distinguishes the object under discussion, the concept used in a terminology system, the definition, the designation, and term-formation practice. | Recover the FPF kind, relation, and sentence function before accepting a rewritten phrase. Use external terminology work only as support for careful designation and definition practice. | Do not replace FPF episteme and publication ontology with an ISO concept system, a dictionary substitution, or a global class row. | `E.10.SEMIO:4.1`, `E.10.SEMIO:4.4`, and `E.10.SEMIO:10` |
| SHACL-style constraint validation makes local constraints explicit and fail-closed when a data shape does not satisfy them. | Treat the semantic rewrite record as a local fail-closed recovery check when the FPF kind, relation, or admissible use cannot be recovered. | Do not import SHACL ontology, machine-validation authority, or shape vocabulary as FPF pattern ontology. | `E.10.SEMIO:4.0a`, `E.10.SEMIO:4.2`, and `E.10.SEMIO:8` |
| Current word-sense disambiguation and ambiguity-resolution work treats sense recovery as context-sensitive rather than solved by the most common word sense. | When one local head or qualifier carries multiple possible readings, recover the local FPF context and exact neighboring FPF pattern before choosing wording. | Do not import machine-learning benchmarks or treat common usage as proof that the local FPF sense is recovered. | `E.10.SEMIO:4.4.1`, `E.17.AUD.LHR`, and `F.18` |

**External-practice boundary.** External traditions are admitted only through the exact local FPF invariant they sharpen. Object-oriented modeling and OWL-style ontology modeling do not become the default repair for vague FPF wording. Architecture-description standards help keep views, viewpoints, concerns, and descriptions explicit. Explainability and NLP faithfulness work helps prevent explanation laundering. RAG evaluation helps separate retrieval support from answer trust. Quality-diversity and multi-objective search help avoid premature scalarization in candidate selection. None of these traditions becomes FPF ontology, FPF authority, or a universal pattern-quality benchmark.

The internal FPF basis remains primary:

| Claim need | Current FPF support | Alignment with E.10.SEMIO | Adoption status |
| --- | --- | --- | --- |
| Head-kind discipline | `E.10` | Use head-kind recovery before accepting a phrase. | Adopt. |
| Stable naming | `F.18` | Run a name card when a reusable head is being minted. | Adopt. |
| Relation precision | `A.6.P` | Recover relation kind, endpoints, slots, qualifiers, and scope when relation or admissibility load is live. | Adopt. |
| Carrier and object-description humility | `A.7` | Keep object, description, and carrier apart before reading a publication as evidence, work, gate, or authority. | Adopt. |
| Episteme and publication ontology | `C.2.1`, `E.17.0`, `E.17`, MVPK | Separate episteme, publication, view, generic publication face, governed MVPK face, publication unit, carrier, and rendering. | Adopt. |
| Project-side downstream use | `A.6.A`, `A.10`, `A.15`, `A.15.4`, `B.3`, `A.20`, `A.21`, `C.11` | When a publication, display, cue, or explanation is read as evidence, gate, decision, work permission, method, assurance, or engineering justification, name the exact neighboring FPF pattern and the exact project-side FPF kind and reference. | Adopt. |

This reduced SoTA basis changes the Solution in one practical way: a semio rewrite cannot close merely because the replacement wording sounds cleaner. It closes only when the FPF kind, relation, admissible use, and any neighboring pattern application are recoverable by value; otherwise the wording is blocked, quote-only, or becomes a candidate for a separate FPF-kind decision.

Internal support details:

- `E.10` supplies the head-kind, term, morphology, register, and forbidden-umbrella discipline.
- `E.10.D2` gives the "thing vs words vs rules" discipline and the carrier humility rule.
- `F.18` gives the local-first naming protocol: Context, Kind, purpose and use-domain, local sense, candidate head families, NQD-front, semantic read-through, and lexical Q components before one label becomes a reusable head.
- `A.6.P` gives the relation-precision restoration method: restore generic head kind, build candidate sets for endpoint kinds and relation kinds, select kind-explicit slots and qualifiers, then allow guardrailed wording.
- `E.17.0`, `E.17` distinguish views, viewpoints, MVPK faces, publication forms, and publication projections.
- `A.15.4` is a good current pattern example of keeping encountered publication, display, or cue items distinct from the exact project-side FPF kind and reference that makes work or reliance admissible.
- `A.16`, `A.16.0`, `A.19`, `B.2.5`, `C.27`, and `A.3.3` provide the movement, control, temporal stack used when semio prose talks about route, trajectory, movement, cadence, or dynamics.
- `E.19` already treats terminology and sentence-level precision restoration as real review obligations, not editorial polish.
- `A.6.A` carries action-invitation discipline when a publication, representation, or cue invites an action without itself becoming authority, evidence, gate passage, or work completion.
- `C.11` carries decision-making and decision-record discipline when the live question is a decision rather than generic action.
- `A.15` and `A.15.4` split role, method, work-plan, and actual-work alignment from work-relevant source restoration, so semio prose must not let `A.15` become a universal semio governing pattern.
- `E.9` is the campaign `DRR` pattern for campaign-level content decisions; `E.11` is only for entry-discoverability situations and must not organize a semio campaign by default.

### E.10.SEMIO:12 - Relations

* **Builds on:** `E.2` Pillars, especially `P-2 Didactic Primacy`; `E.10`, `A.7`, `F.18`, `A.6.P`, `C.2.1`, `E.17.0`, `E.17`, MVPK, `A.6.Q`, and `A.6.A`.
* **Coordinates with:** `E.6`, `E.7`, `E.8`, `E.9`, `E.12`, `E.19`, `A.10`, `A.15`, `A.15.4`, `B.3`, `A.20`, `A.21`, `A.6.3.CSC`, `A.6.3.CR`, `A.6.3.RT`, `E.17.EFP`, and `E.17.ID.CR`.
* **Does not replace:** `E.10` general lexical rules, `F.18` naming protocol, `A.6.P` relation precision, or local semio patterns. It tells authors when those patterns must be applied to semio-heavy wording.
### E.10.SEMIO:End
## E.10.P - Conceptual Prefixes policy & registry
 **Intent.** Provide a compact, **notation‑neutral** registry and **minting policy** for *conceptual prefixes* — short shorthands that signal **cognitive namespaces** used throughout the Core.

 **Policy (normative).**
1. **Purpose.** A conceptual prefix exists **to aid reasoning**, not to name files, serialisations, or APIs. It labels a **role in thought** (e.g., meta‑type, calculus operator, relation family).
 2. **Anchoring.** Every prefix **MUST** be anchored to a **Core extension patterns**  (CAL/LOG/CHR) or Kernel construct and documented in its *Relations*.
 3. **No tool lock‑in.** A prefix **MUST NOT** imply a particular notation or machine binding (see E.5.1–E.5.2).
 4. **Minting rule.** New prefixes are introduced by a **DRR** (E.9) that demonstrates
    (a) cross‑pattern need,
    (b) non‑overlap with existing prefixes,
    (c) alignment with Pillars **P‑1/P‑5**.
 5. **Scope.** Prefixes are **globally reserved** within the Core; domain patterns  **MAY** mint local shorthands only inside their Contexts and **MUST NOT** collide with this registry.

 **Registered conceptual prefixes (Core).**
* `U.` — **U.Types meta‑namespace** (holons & primitives). *Anchor:* Kernel Part A.
* `Γ_` — **Calculus operator family** (by flavour: `Γ_sys`, `Γ_epist`, …). *Anchor:* Part B umbrella on Γ.
* `ut:` — **Universal relation family** (e.g., `PartOf` sub‑relations). *Anchor:* A.14 (Mereology) — informative alias vocabulary.
* `tv:` — **Trace & Validation vocabulary** (CT2R‑LOG): `tv:AliasOf`, `tv:groundedBy`. *Anchor:* B.3 (Trust & Assurance, LOG‑use).
* `ev:` — **Evidence hooks** (bindings/roles). *Anchor:* A.10 / B.3 (Evidence Graph Referring).
* `mero:` — **Mereology trace types** (internal labels: `SumTrace` / `SetTrace` / `SliceTrace`) used **informatively** in examples. *Anchor:* B.1 (Γ‑aggregation).

**Conformance Checklist (E.10.P).**
* **CC‑LEX‑P.1** New Core text **SHALL NOT** introduce an unregistered conceptual prefix.
* **CC‑LEX‑P.2** Each occurrence of a registered prefix **SHALL** cite its anchor pattern on first use in a section.
* **CC‑LEX‑P.3** Examples that expand a prefix into a concrete URI or syntax **MUST** mark the expansion *informative* and locate it in Tooling/Pedagogy.

**Relations.** Constrains E.5.1 (Lexical Firewall) & E.5.2 (Notational Independence); Depends on E.9 (DRR).

### E.10.P:End

## E.10.D1 - Lexical Discipline for “Context” (D.CTX)

> **One‑sentence summary.** Make the word **Context** unambiguous: in FPF it **only** denotes the formal primitive **`U.BoundedContext`**; remove the term **anchor**; reserve **Problem Frame** for situational narrative; treat **Domain** as an **informative family label**, not a type.

**Status.** Discipline definitional pattern.
**Depends on.** C‑6 *Strict Distinction*; C‑7 *Temporal Duality*; G‑1 *Minimal Generality*; G‑2 *Contextual Specification*.
**Coordinates with.** E.10.U1 *Domain‑Family Landscape Survey*; E.10.U2 *Term Harvesting & Normalisation*; E.10.U7 *Concept‑Set Table*; E.10.U9 *Alignment/Bridge*; `RoleAssigning` patterns (e.g., E.10.U4).
**Aliases (informative).** Context Discipline; No‑Anchor Rule.


### E.10.D1:1 - Intent & Applicability

**Intent.** Eliminate ambiguity around “context” by (a) fixing **one** formal meaning—`U.BoundedContext`; (b) removing “anchor” from the vocabulary; (c) reserving **Problem Frame** for prose about situations; and (d) clarifying **Domain** as an **informative family** (workflow, provenance, services, …) that groups several `U.BoundedContext`s.

**Applicability.** Mandatory across **all FPF patterns** (Role Assignment & Enactment, Sys-CAL, KD-CAL, Kind-CAL, planned LCA-CAL). Apply at the start of any unification effort and whenever documentation introduces or refactors “context”, “domain”, “anchor”.

**Non‑goals.** No governance, workflow, or tool mandates; no storage formats; no team roles.


### E.10.D1:2 - Problem Frame

1. **Polysemy.** “Context” is used for formal scopes, narrative situations, and even runtime modes.
2. **Extra token (“anchor”).** “Anchor” pretends to be “where meaning is attached”, duplicating context semantics.
3. **Domain overreach.** “Domain context” conflates **families** (disciplinary areas) with **formal contexts**.
4. **Plane mixing.** Runtime/design stances and deontic/behavioural notions are smuggled into “context”.


### E.10.D1:3 - Forces

| Force                     | Tension to resolve                                                 |
| ------------------------- | ------------------------------------------------------------------ |
| Universality vs locality  | One calculus vs many local context of meaning (C‑6 vs C‑1).          |
| Brevity vs precision      | Short labels vs unambiguous reference.                             |
| Stability vs evolution    | Fixed terms vs edition turnover and language variants (C‑7).       |
| Parsimony vs expressivity | Few primitives vs enough hooks for Role Assignment & Enactment, Concept Sets, and Bridges. |


### E.10.D1:4 - Solution — **Name one thing “Context” can mean**

**D‑CTX‑1 (Canonical meaning).** In all FPF materials, **Context** denotes the formal primitive **`U.BoundedContext`** only. The short form **Context** is permitted in the *Tech* register strictly as an alias of `U.BoundedContext`.

**D‑CTX‑2 (Remove “anchor”).** The term **anchor** is **prohibited**. When you need “the place where a meaning lives”, use:

* **`SenseCell := (U.BoundedContext, Local‑Sense)`** — the *cell of meaning* inside a specific Context; or
* a **`ConceptSet.Row`** + column reference (see E.10.U7).

**D‑CTX‑3 (Domain is informative).** **Domain** (workflow, provenance, services, access, sensing, …) is **not** a U.Type. It is an **informative family label** grouping several `U.BoundedContext`s. There is no “domain context”.

**D‑CTX‑4 (Narrative is Problem Frame).** Use **Problem Frame** (or **Frame**) for situational narrative in patterns. Do **not** use “context” for narrative sections.

**D‑CTX‑5 (Time is a tag, not a context).** `design` / `run` are **TimeScope tags** (C‑7) on artefacts or sources; they do **not** create separate contexts.

**D‑CTX‑6 (No context inheritance).** `U.BoundedContext`s have **no is‑a** or containment relations. Any cross‑context relationship appears **only** via E.10.U9 *Alignment/Bridge* with explicit loss policies.

**D‑CTX‑7 (Language/edition discipline).** Different languages or editions may be **distinct `U.BoundedContext`s** when meaning or usage can diverge. Where an official source binds multilingual labels to the **same** semantics, record them as **labels** of the **same** Context.

**D‑CTX‑8 (Reference forms).** Use **one of the following** when pointing to meaning:

* **`ContextId:LocalLabel`** (e.g., `BPMN_2_0:process`), or
* **`SenseCell(ContextId, Local‑SenseId)`**, or
* **ConceptSet(RowId).Column(ContextId)** (E.10.U7).


### E.10.D1:5 - Structure — Minimal reference shapes (informative)

> Shapes shown **do not** prescribe formats; they are naming conventions.

* **Context Id.** Stable short handle (e.g., `BPMN_2_0`, `PROV_O_2013`, `ITIL4_2020`, `NIST_RBAC_2004`, `SOSA_SSN_2017`).
* **SenseCell.** `(ContextId, Local‑Sense)` where `Local‑Sense` is the Context‑local preferred label (from E.10.U2).
* **ConceptSet Row.** A table row keyed by a row id; columns are `SenseCell`s per Context (E.10.U7).


### E.10.D1:6 - Core Invariants (normative)

1. **LCTX‑INV‑1 (Uni‑meaning).** The word **Context** in formal text equals **`U.BoundedContext`**.
2. **LCTX‑INV‑2 (No anchor).** The token **anchor** does **not** appear in normative prose; use **SenseCell** or **ConceptSet reference**.
3. **LCTX‑INV‑3 (No domain contexts).** “Domain context” is invalid; use **Domain family** + list of `U.BoundedContext`s.
4. **LCTX‑INV‑4 (Frames, not contexts).** Pattern headers use **Problem Frame** for narrative.
5. **LCTX‑INV‑5 (No hierarchy).** Contexts are flat; relationships are declared **only** via E.10.U9 Bridges.
6. **LCTX‑INV‑6 (Plane hygiene).** Contexts describe **context of meaning** for sources; they are not roles, statuses, executions, or types (C‑6).
7. **LCTX‑INV‑7 (Time tags).** DesignRunTag is a **tag** on carriers, source publications, or source epistemes as applicable; it does not multiply contexts.
8. **LCTX‑INV‑8 (Language/edition).** Multilingual or multi‑edition handling follows D‑CTX‑7.


### E.10.D1:7 - Conformance Checklist (normative)

* **CC‑LCTX‑1.** Grep‑style check: every “Context” in formal sections expands to **`U.BoundedContext`**.
* **CC‑LCTX‑2.** The token **anchor** is absent from normative text; where needed, occurrences are replaced by **SenseCell** or **ConceptSet reference**.
* **CC‑LCTX‑3.** Pattern headers use **Problem Frame**; none use “Context” for narrative.
* **CC‑LCTX‑4.** References to meaning are in one of the **reference forms** (Sec. 5).
* **CC‑LCTX‑5.** No file defines “domain context”; Domain appears only as an **informative family**.
* **CC‑LCTX‑6.** No is‑a edges between contexts; any cross‑context relation is located in **E.10.U9**.
* **CC‑LCTX‑7.** Language/edition handling matches **D‑CTX‑7** (separate Contexts when semantics can diverge).


### E.10.D1:8 - Anti‑patterns & Remedies

| Anti‑pattern                  | Symptom                                                           | Why harmful                          | Remedy (normative)                                                           |
| ----------------------------- | ----------------------------------------------------------------- | ------------------------------------ | ---------------------------------------------------------------------------- |
| **A1 Context-as-situation**   | “Context” used for narrative sections                             | Ambiguity                            | Use **Problem Frame**; reserve Context for `U.BoundedContext` (D‑CTX‑4).     |
| **A2 Anchor-speak**           | “role anchor”, “ontology anchor”                                   | Redundant token; hides locality      | Replace with **SenseCell** or **ConceptSet(Row).Column** (D-CTX-2, D-CTX-8). |
| **A3 Domain context**         | “Workflow domain context”, etc.                                   | Family ≠ formal context              | Use **Domain family** + explicit list of Context ids (D‑CTX‑3).              |
| **A4 Context hierarchy**      | Context A “is‑a” Context B                                        | Leaks meanings; blocks loss policies | Remove hierarchy; use **E.10.U9 Bridge** with loss policy (D‑CTX‑6).         |
| **A5 Time‑as‑context**        | “Runtime context” vs “Design context”                             | Multiplies Contexts incorrectly         | Use **TimeScope tags** (C‑7); keep one Context (D‑CTX‑5).                    |
| **A6 Cross‑lingual blending** | Mixing language labels as one context despite divergent semantics | Hidden drift                         | Split Contexts per **D‑CTX‑7** or document shared semantics if truly bound.  |


### E.10.D1:9 - Worked Examples

#### E.10.D1:9.1 Enactment — process vs activity (two context of meaning).

* Use `BPMN_2_0:process` and `PROV_O_2013:activity` as **SenseCell**s.
* In a Concept‑Set row, code the provisional relation `⋈` (overlap), not an equality.
* Role Descriptions later reference **the specific SenseCell**, not “an anchor”.

#### E.10.D1:9.2 Roles — behavioural mask vs access status.

* `BPMN_2_0:participant` vs `NIST_RBAC_2004:role`.
* Mark `⟂` (incompatible) in the Concept‑Set row to prevent conflation.
* Any cross‑use requires E.10.U9 with explicit loss policy.

#### E.10.D1:9.3 Services & evidence.

* `ITIL4_2020:service` / `ITIL4_2020:service‑level‑objective` with KD‑CAL cells `SOSA_SSN_2017:observation`.
* References in acceptance patterns point to **SenseCell**s; provenance stays within the PROV Context.


### E.10.D1:10 - Reasoning Primitives (conceptual judgements; notation‑agnostic)

> Pure **thinking moves**; no APIs, no storage, no governance.

* **(J1) Context expansion.** `⊢ Context ≡ U.BoundedContext`
  *Reading:* wherever “Context” appears in formal prose, it denotes `U.BoundedContext`.

* **(J2) Anchor ban.** `uses("anchor") ⊢ violation(D‑CTX‑2)`
  *Reading:* usage of “anchor” flags a discipline violation.

* **(J3) Sense reference.** `ref(ContextId, LocalLabel) ⊢ SenseCell(ContextId, Local‑Sense)`
  *Reading:* a well‑formed reference identifies a SenseCell.

* **(J4) Narrative frame.** `header("Context") ⊢ replaceWith("Problem Frame")`
  *Reading:* headings “Context” in patterns must become “Problem Frame”.

* **(J5) Domain family.** `label ∈ {workflow,…} ⊢ DomainFamily(label)`
  *Reading:* Domain labels are families, not contexts.

* **(J6) Time tag.** `stance ∈ {design, run} ⊢ TimeScopeTag(stance)`
  *Reading:* time is a tag, not a new context.


### E.10.D1:11 - Relations (with other patterns)

**Builds on:** C‑6, C‑7, G‑1, G‑2.
**Constrains:**

* **E.10.U1** — lists only `U.BoundedContext`s; no “domain contexts”; context records never encode pattern semantics.
* **E.10.U2** — Seeds and Occurrences are **always** Context‑anchored; references use forms from Sec. 5.
* **E.10.U7** — Columns are **SenseCell**s; row notes never call them “anchors”.
* **E.10.U9** — All cross‑context relations live here; no implicit equivalences elsewhere.
* **`RoleAssigning` patterns (E.10.U4, …)** — Context points to **SenseCell** or **Concept‑Set columns**, never to “anchors”.


### E.10.D1:12 - Migration Notes (conceptual playbook)

1. **Rename headings.** Replace any “Context” section title with **Problem Frame**.
2. **Delete “anchor”.** Replace with **SenseCell** or **Concept‑Set** references.
3. **Split domain vs context.** Where “domain context” appears, rewrite as **Domain family** + explicit list of `U.BoundedContext`s.
4. **Audit references.** Ensure every semantic reference is `ContextId:LocalLabel` or `SenseCell(ContextId, …)` or Concept‑Set column.
5. **Flatten contexts.** Remove any inheritance among contexts; move relations to **E.10.U9**.
6. **Tag time.** Replace “design or runtime context” with **TimeScope tags**.
7. **Language/edition pass.** Split or merge Contexts per **D‑CTX‑7**; document rationale.


### E.10.D1:13 - Acceptance Tests (SCR/RSCR stubs)

**SCR — Static discipline checks**

* **SCR‑DCTX‑S01.** No occurrence of the token **anchor** in normative sections.
* **SCR‑DCTX‑S02.** All formal uses of “Context” resolve to **`U.BoundedContext`**.
* **SCR‑DCTX‑S03.** Pattern headers contain **Problem Frame** instead of “Context”.
* **SCR‑DCTX‑S04.** All semantic references use the forms in Sec. 5.
* **SCR‑DCTX‑S05.** No “domain context” strings; Domain appears only as family metadata.
* **SCR‑DCTX‑S06.** No is‑a or containment relations between contexts outside **E.10.U9**.

**RSCR — Regression discipline checks**

* **RSCR‑DCTX‑E01.** Adding a new family or edition does not introduce “domain context” or context hierarchies.
* **RSCR‑DCTX‑E02.** Refactors of E.10.U1/U.2/U.7/U.9 do not re‑introduce “anchor”.
* **RSCR‑DCTX‑E03.** Multilingual updates follow D‑CTX‑7 (split/merge rationale recorded informatively).

### E.10.D1:End

## E.10.D2 - Intension–Description–Specification Discipline (I/D/S)

*Definitional pattern — normative, notation‑agnostic*

> **One‑sentence summary.** For every intensional FPF-governed entity (e.g., `U.Role`, `U.Method`, `U.System`, `U.Work`, `U.PromiseContent`), clearly distinguish the **thing itself** (*Intension*), its **context‑bound Description** (KU), and its **formal Specification** (KU). Use **–Spec** only when strict, testable invariants and an acceptance harness exist; otherwise use **–Description**. This keeps semantics clean, didactic, and testable across all FPF patterns.

**Status.** Definitional pattern.
**Builds on:** A.7 **Strict Distinction (Clarity Lattice)**; E.10.D1 **D.CTX (Context ≡ U.BoundedContext)**; C.2.1 **U.EpistemeSlotGraph (DescriptionContext, IDS‑13)**; C.2.3 **Unified Formality Characteristic (F)**.
**Coordinates with.** F.4 **Role Description**; F.5 **Naming Discipline**; F.10 **Evaluation**; F.15 **SCR/RSCR Harness**.
**Non‑goals.** No editors, workflows, registries, or storage formats. No tooling commitments.

### E.10.D2:1 - Problem frame

**Intent.** Prevent perennial confusions such as “the role contains the checklist” or “the method is the document.” Establish a universal discipline so that:

* **Intensions** (e.g., `U.Role`, `U.Method`) remain I/D/S layer‑pure and context‑agnostic entities in the kernel.
* **Descriptions** (KUs) capture human‑readable, **Context‑local** semantics (labels, glosses, characterisations, state graphs, checklists).
* **Specifications** (KUs) exist **only** when there are verifiable invariants, an acceptance harness, **and a declared Formality F adequate for checkability (C.2.3; default F ≥ F4)**, making claims testable.

**Applicability.** Whenever an FPF text introduces or uses an intensional `U.Type` (e.g., `U.Role`, `U.Method`, `U.PromiseContent`, `U.System`, `U.Work`, `U.RCS`, `U.RSG`, `U.RoleEnactment`) in any part (A–H).

### E.10.D2:2 - Problem

1. **Plane/layer mixing.** Intensions are routinely conflated with their documents and with runtime facts.
2. **Name drift.** “Spec” gets used for any write‑up; “status” drifts between states of a role and epistemic/deontic statuses over knowledge units.
3. **Didactic friction.** Inconsistent naming raises cognitive load and impedes reuse across FPF patterns.
4. **Unverifiable claims.** Without a clear gate to **–Spec**, normative wording appears without testability.

### E.10.D2:3 - Forces

| Force                        | Tension to resolve                                                                |
| ---------------------------- | --------------------------------------------------------------------------------- |
| **Simplicity vs rigour**     | Easy‑to‑learn naming vs the need for machine‑checkable invariants.                |
| **Universality vs locality** | Kernel intensions must be universal; language and criteria are **Context‑local**. |
| **Stability vs evolution**   | Names should be stable; artefacts must mature via **ΔF** along the **F** ladder cleanly. |

### E.10.D2:4 - Solution — the I/D/S layer + a formal Spec‑gate

#### E.10.D2:4.1 The triad (applies to **any** intensional `U.T`)

**Terminology discipline (normative).** Say **I/D/S layers** when you mean the **stratified order with a Spec‑gate**; say **I/D/S triad** only to note **three‑ness without order or dependency**. **Do not call I/D/S a “plane”.** Reserve **plane** for uses explicitly defined elsewhere (e.g., **`CHR:ReferencePlane`** and status families).
**Layer semantics (clarity).** **I‑layer** = **kernel/intensional type** (non‑epistemic; **not** a episteme) . **D‑layer** and **S‑layer** = **epistemic Knowledge Units** (KUs). The **Spec‑gate** upgrades a Description to a Specification only under declared checkability and harness conditions (unchanged).

For every intensional type `U.T`:

* **Intension — `U.T`.**
  The thing itself (e.g., `U.Role`, `U.Method`, `U.PromiseContent`, `U.System`, `U.Work`, `U.RCS`, `U.RSG`).
  *It does **not** contain documents, checklists, or carriers; it is not a runtime event or a file.*

* **Description episteme — `U.TDescription(@Context)`**
  A **Context‑local** knowledge unit that **characterises** `U.T` with labels (Tech/Plain), glosses, and, when applicable, **Role Characterisation Space (`U.RCS`)**, **Role State Graph (`U.RSG`)**, and **state conformance checklists**.
  *Readable, precise, didactic; may reference evaluation criteria but does not assert testable “shall”s by itself.*

* **Specification episteme — `U.TSpec(@Context)`**
  A **Context‑local** knowledge unit that states **testable invariants** for `U.T` and is **bound to an acceptance harness**.
  *Normative, verifiable, suitable for SCR/RSCR (F.15).*

> **Key phrasing discipline.** Intensions are **characterised by** (not “contain”) RCS/RSG/checklists, which **live in** the Description/Spec.
> **Terminology guard.** To avoid collisions with **ReferencePlane** and other semantic planes, the I/D/S triad is referred to as **I/D/S Layers** (Intension Layer - Description Layer - Specification Layer). The word **plane** is reserved for **semantic planes** (Role, Status, Measurement, Type-structure, Method, or Work, etc.) and for the **ReferencePlane** field used in describedEntity/assurance.

#### E.10.D2:4.2 The Spec‑gate (when “–Spec” is allowed)

Use the **–Spec** suffix **only if all** of the following hold:

1. **Formality F (C.2.3):** the artefact declares **F ≥ F4** (or a context-defined higher threshold) so predicates are checkable.
2. **Verifiability:** invariants are stated as checkable predicates or thresholds.
3. **Harness bound:** there is a linked **acceptance harness** (SCR/RSCR matrices per F.15).
4. **Context anchoring:** all wording is explicitly local to a named `U.BoundedContext` (E.10.D1).

If any condition is missing, the artefact **must be** a `…Description`.

#### E.10.D2:4.3 Where RCS/RSG and evaluations sit

* **`U.RCS` (Role Characterisation Space)** and **`U.RSG` (Role State Graph)** are **intensional** types that structure the space of role characteristics and permissible state transitions.
* Their **human presentation** (characteristics, dimensions, node labels, admissible transitions) lives in the **RoleDescription**, and becomes part of **RoleSpec** only when the transitions and state predicates are made **testable** and harness‑bound.
* **`U.Evaluation`** operates on **evidence** against the conformance checklist (from the Description/Spec) to produce a **state attestation** (“X is in state S @Context within window W”).
* **Epistemic/deontic statuses** (e.g., *Evidence*, *Requirement*, *Standard*) are **roles over Epistemes** (not states of the role). They are governed elsewhere (F‑R family) and must not be conflated with `U.RSG` state names.

#### E.10.D2:4.4 Plain‑language memory hook

> *Thing vs words vs rules.*
> **The thing** (`U.Role`, `U.Method`) is clean and abstract.
> **The words** (labels, glosses, RCS/RSG pictures, checklists) live in the **Description**.
> **The rules** (testable “shall”s with harness) live in the **Specification**.
> If you can’t test it, don’t call it **Spec**.

### E.10.D2:5 - Minimal vocabulary & naming discipline (this pattern only)

**Core trio (per intensional `U.T`).**

* **`U.T` — the Intension.**
  Kernel object (e.g., `U.Role`, `U.Method`, `U.PromiseContent`, `U.System`, `U.Work`, `U.RCS`, `U.RSG`).
  *Never* a document, *never* an event, *never* a file.

* **`U.TDescription(@Context)` — the Description Episteme.**
  Context‑local characterisation of `U.T`: Tech/Plain labels, gloss, notes; for roles, may **characterise** with an `U.RCS` (characteristics/traits), an `U.RSG` (states/transitions), and **state conformance checklists** (per state). *Readable; precise; not yet a set of testable “shall”s.*

* **`U.TSpec(@Context)` — the Specification Episteme.**
  Context‑local, **testable** invariant set for `U.T`, explicitly **bound to an acceptance harness** (SCR/RSCR matrices per F.15). Use **–Spec** only through the Spec‑gate (Sec. 4.2).

**Suffix rules.**

* Use **`…Description`** by default (M‑mode or F‑mode without harness).
* Use **`…Spec`** *only* when **all** Spec‑gate conditions (Sec. 4.2) hold.
* No alternative suffixes (“Profile”, “Definition”, “Guide”) inside the Core; such epistemes live in pedagogy/tooling layers, not in the I/D/S discipline.

**Naming morphology (recap of F.5 as it applies here).**

* Two registers: **Tech** and **Plain** labels on every Description/Spec.
* Roles use **count nouns** (e.g., *Operator*); states use **state nouns** (e.g., *Approved*).
* Statuses over knowledge (e.g., Evidence/Requirement) are **not** role states; they name **roles over Epistemes** (F‑R family), not nodes in `U.RSG`.

**Context anchoring.**
Every Description/Spec is **local to** a `U.BoundedContext` (E.10.D1). Phrases in the episteme must read correctly once prefixed by the Context name (e.g., “(ITIL4) Acceptance criteria …”).

**Carriers.**
`U.Carrier` holds **encodings** of a Description/Spec; the Episteme’s identity is **not** the file. *Never* say “the role contains the checklist in the PDF”; say “the **RoleDescription** characterises the role with checklists; this **carrier** encodes them.”

**Time stance.**
Descriptions/Specs must declare DesignRunTag when inherent (e.g., RoleDescription is design‑time; state attestation via `U.Evaluation` is run‑time).

### E.10.D2:6 - Invariants (normative)

**IDS‑1 (Plane purity).**
An intensional `U.T` **MUST NOT** be conflated with its Description/Spec or with any `U.Carrier` or `U.Work`.

**IDS‑2 (Context locality).**
Every `…Description/…Spec` **MUST** name a `U.BoundedContext`. Wording inside is read **as‑local**; no global meaning is implied.

**IDS-3 (Spec-gate).**
A episteme **MUST NOT** use the **–Spec** suffix unless: *(a)* the artefact declares **`U.Formality = Fk` with k ≥ 4** per **C.2.3**, *(b)* invariants are testable predicates, *(c)* an acceptance harness is linked (F.15), *(d)* Context is explicit.

**IDS‑4 (Characterisation verbs).**
Texts **MUST** say: *“`U.Role` is **characterised by** `U.RCS`/`U.RSG` in the RoleDescription”*.
They **MUST NOT** say: *“the role **contains** the RCS/RSG”*.

**IDS‑5 (RCS/RSG scope).**
`U.RCS`/`U.RSG` are **intensional structures**. Their **presentations** (characteristics, state names, admissible transitions, checklists) live in the **RoleDescription**, and in **RoleSpec** only when transitions and state predicates are fully testable.

**IDS‑6 (Evaluation semantics).**
`U.Evaluation` **MUST** operate over evidence against conformance checklists from the Description/Spec and **MUST** produce a **state attestation** (who/what is in state *S* @Context within window *W*). Evaluation **does not** mutate the intensional object.

**IDS‑7 (Status separation).**
Epistemic/deontic statuses (Evidence/Requirement/Standard) are roles over **knowledge units**; they **MUST NOT** be used as state names in `U.RSG`.

**IDS‑8 (Register discipline).**
Every Description/Spec **SHOULD** include both **Tech** and **Plain** labels. Symbolic aliases are optional and informative.

**IDS‑9 (No stealth bridges).**
Descriptions/Specs **MUST NOT** import meanings from other Contexts by shared labels. Cross‑context relations exist only as **F.9 Bridges**.

**IDS‑10 (Window honesty).**
When an evaluation is time‑bounded, the **window** **MUST** be stated in the attestation.

**IDS‑11 (Ladder clarity).**
A Description may mature into a Spec by satisfying IDS‑3; the opposite move requires a rationale (loss of testability) and must drop the **–Spec** suffix.

**IDS‑12 (Didactic bound).**
A RoleDescription **SHOULD** fit on one screen per state graph plus one screen of notes; sprawling documents belong to pedagogy, not to the core Description.

### E.10.D2:7 - Reasoning primitives (judgement schemas, notation‑free)

> Judgements are **mental moves**—they assert what follows when premises hold. They do **not** imply queries, storage, or workflows.

1. **Description link (with DescriptionContext)**

   ```
   U.T, C, Vp ⊢ isDescriptionOf(TDesc, U.T, C, Vp)
   ```

   *Reading:* `TDesc` is the Context‑local Description of `U.T` in Context `C` under Viewpoint `Vp`. Its `subjectRef` decodes to `DescriptionContext = ⟨DescribedEntityRef(U.T), C, Vp⟩` (IDS‑13, C.2.1 §6.1).

2. **Spec link (Spec‑gate, viewpoint‑local)**

   ```
   isDescriptionOf(TDesc, U.T, C, Vp) ∧ U.Formality(TSpec) ≥ F4
      ∧ testableInvariants(TSpec) ∧ harnessBound(TSpec)
      ∧ sameDescriptionContext(TSpec, TDesc)
      ⊢ isSpecOf(TSpec, U.T, C, Vp)
   ```

   *Reading:* Only when F‑mode, testability, harness, and a matching `DescriptionContext` are present may we judge `TSpec` a Specification of `U.T` in `C` under Viewpoint `Vp`.

3. **Role characterisation**

  ```
   isDescriptionOf(RoleDesc, U.Role, C, Vp)
   ∧ characterises(RoleDesc, U.RCS) ∧ characterises(RoleDesc, U.RSG)
   ⊢ characterisedBy(U.Role, {U.RCS, U.RSG}) @C
  ```

   *Reading:* The role is *characterised by* the RCS/RSG as presented in the Description (which is pinned to `(C, Vp)`), not that it “contains” them.

4. **State conformance predicate**

   ```
   checklistFor(RoleDesc, state S) = χ
   ∧ evidence E within window W
   ⊢ conformsToState(E, χ, W) ⇒ attestation(subject ∈ S @C, W)
   ```

   *Reading:* Evidence satisfies the checklist for state `S`, yielding a state attestation.

5. **Transition admissibility**

   ```
   U.RSG allows (S → S') @C
   ∧ attestation(subject ∈ S @C, W)
   ∧ conformsToState(E', checklistFor(S'), W')
   ⊢ admissibleTransition(subject : S → S' @C)
   ```

   *Reading:* A move from `S` to `S'` is admissible when RSG permits it and `S'` is satisfied.

6. **Status / state separation guard**

   ```
   statusOverKU(KU, σ) ∧ stateInRSG(ρ)
   ⊢ σ ≠ ρ  (distinct planes)
   ```

   *Reading:* A status over a knowledge unit is not a role‑state.

7. **No Cross‑context import**

   ```
   isDescriptionOf(TDescA, U.T, CA, VpA) ∧ isDescriptionOf(TDescB, U.T, CB, VpB) ∧ CA≠CB
   ⊢ ¬equateByLabel(TDescA, TDescB)  (bridges required in F.9)
   ```

   *Reading:* Identical wording across Contexts (and Viewpoints) does not grant equivalence; only Bridges may relate them.

### E.10.D2:8 - Anti‑patterns & remedies

| ID   | Anti‑pattern                | Symptom                                                              | Why it harms thinking                     | Remedy (concept move)                                                                          |
| ---- | --------------------------- | -------------------------------------------------------------------- | ----------------------------------------- | ---------------------------------------------------------------------------------------------- |
| A‑1  | **Spec‑by‑name**            | Every write‑up is titled “Spec”.                                     | Inflates normativity; untestable claims.  | Apply **Spec‑gate** (IDS‑3). If any condition fails, rename to `…Description`.                 |
| A‑2  | **Role contains RSG**       | “The role contains a state graph.”                                   | Plane mixing; mereological confusion.     | Use **characterised by** phrasing (IDS‑4); RSG presentation lives in RoleDescription/RoleSpec. |
| A‑3  | **Status ≡ state**          | *Approved* (status over episteme)  appears as a node in the role graph.     | Cross‑plane conflation; logic errors.     | Keep **statuses** (over Epistemes) separate from **role states** (IDS‑7).                            |
| A‑4  | **Stealth bridge**          | Copying state names across Contexts to imply sameness.                  | Hidden cross‑context import.              | Declare an **F.9 Bridge** or accept divergence (IDS‑9).                                        |
| A‑5  | **Checklist = process**     | Treating conformance checklist as an execution workflow.             | Category error (design vs run).           | Checklists are **criteria** used by `U.Evaluation`; executions live under `U.Work`.            |
| A‑6  | **Carrier identity**        | File path/version treated as “the spec itself.”                      | Identity drift; archival brittleness.     | Identity is the **KU**; `U.Carrier` is only an encoding (Sec. 5).                              |
| A‑7  | **Windowless verdict**      | Attestations omit time window.                                       | Unreproducible results; stale judgements. | Require **window** in attestation (IDS‑10).                                                    |
| A‑8  | **Over‑formal Description** | Description bloats into a standard; unreadable.                      | Violates didactics; blocks adoption.      | Enforce **one‑screen** discipline (IDS‑12); move exegesis to pedagogy.                         |
| A‑9  | **Spec without harness**    | “Shall” statements with no linked acceptance matrices.               | Unverifiable normativity.                 | Bind to **SCR/RSCR harness** (F.15) or downgrade to Description (IDS‑3).                       |
| A‑10 | **Global language leakage** | Description reads as universal definition rather than Context‑local. | Breaks locality; fuels conflicts.         | Prefix mentally with the Context; rewrite locally (IDS‑2).                                        |

### E.10.D2:9 - Worked examples (didactic)

> Each vignette shows **intension ↔ Description/Spec ↔ Evaluation** with **context‑local** wording. No workflows; only thinking moves.

#### E.10.D2:9.1 - Enactment (Role Assignment & Enactment line) — *Change Authority* role (ITIL 4 Context)

**Contexts.** `ITIL4_2020` (services/deontics), `PROV_O_2013` (run‑time traces).
**Intension.** `U.Role :: ChangeAuthority` — a behavioural mask that may be worn by a system (person/team/tool) to **authorise** a change.

**RoleDescription\@ITIL4.**

* **Tech/Plain.** *ChangeAuthority* / “change approver”.
* **RCS (characteristics).** CredentialLevel ∈ {L1,L2}; Scope ∈ {Service, Platform}; SeparationOfDuty ∈ {Clean, Violates}.
* **RSG (states).** `Proposed → Designated → Authorized → Active → Suspended → Revoked`.
* **State checklists (sketch).**

  * *Authorized:* { valid nomination, SoD=Clean, credential ≥ required, mandate window set }.
  * *Active:* *Authorized* ∧ { current shift/roster entry ∧ no conflicting active duty }.

**Evaluations.**
`U.Evaluation@ITIL4` over evidence (roster entries, mandate doc, SoD list, PROV Activities of approvals) yields **attestations**:

* `subject=Team‑X ∈ Authorized@ITIL4 in ⟨2025‑08‑01, 2025‑12‑31⟩`.
* Later, `subject=Team‑X ∈ Active@ITIL4 at 2025‑09‑14T10:05Z`.

**Didactic hooks.**

* The **role** is *characterised by* RCS/RSG in the **RoleDescription**; it **does not contain** them.
* The **attestation** is a statement about state‑in‑window; it does **not** mutate the role.

#### E.10.D2:9.2 - Method (Essence‑language Context) — *Backlog Refinement* method

**Contexts.** `OMG_Essence_Language_2023` (method language), `PROV_O_2013` (runtime).
**Intension.** `U.Method :: BacklogRefinement`.

**MethodDescription\@Essence.**

* **Tech/Plain.** *BacklogRefinement* / “tidy backlog”.
* **Inputs and outputs (informative).** Work items (ideas) → clarified items (ready/not-ready tags).
* **RCS (characteristics).** Cadence ∈ {weekly, continuous}; CollaborationMode ∈ {sync, async}.
* **RSG (states).** `Sketched → Defined → Adopted`.
* **State checklist (Adopted).** { team agreed practice note exists, cadence set, entry/exit criteria published }.

**Spec‑gate outcome.**
No acceptance harness yet → remains **MethodDescription**, **not** MethodSpec.

**Run‑time echo.**
`U.Work` instances (calendar sessions, chat threads) are traced in PROV; **Evaluation** can check whether an *Adopted* practice is being followed in window W without ever reifying the method as a workflow.

#### E.10.D2:9.3 - Service (SLO/SLA) — *Calibration Service* (ITIL 4 + SOSA/SSN Contexts)

**Contexts.** `ITIL4_2020` (service), `SOSA_SSN_2017` (observation), `ISO_80000_1_2022` (units).
**Intension.** `U.PromiseContent :: CalibrationService`.

**ServiceDescription\@ITIL4.**

* **Tech/Plain.** *CalibrationService* / “we calibrate your sensor”.
* **Acceptance facet (informative).** *SLO: error ≤ 0.5% FS under ISO 80000 units*; **formal criteria live in** ServiceSpec only if harness exists.

**Evaluation\@ITIL4+SOSA.**
Observations (SOSA) from test runs compared with thresholds → **ServiceEvaluation** attests *Met/Not‑Met* in a stated window.
No Cross‑context import: ISO units cited **as context‑local** references.

#### E.10.D2:9.4 - Epistemic (KD‑line) — *Evidence status vs role state*

**Contexts.** `PROV_O_2013` (provenance), `FPF_Evidence_Status` (status family).
**Intensions.** `U.KnowledgeUnit :: Report_42`; `U.EvidenceStatus :: SupportsClaim`.

**Separation.**

* `SupportsClaim@C` is a **status over a Episteme** (classifies the report).
* It is **not** a node of any role’s `U.RSG`.
* `U.Evaluation` produces `attestation(Report_42 has EvidenceStatus=SupportsClaim@C, W)`.

**Didactic point.**
State names in *role* graphs do not duplicate **statuses**; planes stay disjoint.

#### E.10.D2:9.5 - Control (Sys‑CAL line) — *Control‑Operator* role (IEC 61131‑3 Context)

**Contexts.** `IEC_61131_3` (control languages), `ISA_95` (integration).
**Intension.** `U.Role :: ControlOperator`.

**RoleDescription\@IEC61131‑3.**

* **RCS.** StationLevel ∈ {Cell, Line}; TaskMode ∈ {Cyclic, Event}; AlarmPrivileges ∈ {Ack, Ack+Shelve}.
* **RSG.** `Onboarded → Authorized → ConsoleActive → Paused → Suspended`.
* **Checklists (ConsoleActive).** { Authorized ∧ current console login ∧ task watchlist loaded }.

**Attestation (run‑time).**
`subject=Operator‑A ∈ ConsoleActive@IEC at 2025‑09‑14T08:00Z` based on log evidence.
No “workflow” required in the Description.

### E.10.D2:10 - Relations (with other patterns)

**Builds on:**

* **E.10.D1 — Lexical Discipline for “Context” (D.CTX).** Provides the *Context* primitive and bans “anchor” talk.
* **A.7 — Strict Distinction (Clarity Lattice).** This pattern concretises SD for intension vs description/spec vs carrier vs work.
* **C.2.3 — Unified Formality Characteristic (F).** Supplies the **F** anchors and **ΔF** moves that gate `…Spec`.

**Constrains:**

* **F.1–F.3 (Contexts → seeds → local senses).** Descriptions **must** cite context‑local senses (SenseCells) rather than global words.
* **F.4–F.5 (role/service naming).** Tech/Plain labels on Descriptions obey F.5 morphology rules.
* **F.8 (Service Acceptance Binding).** Evaluations of services read acceptance **from Description/Spec**, compare against Observations.
* **F.9 (Alignment & Bridge).** No Description/Spec may imply Cross‑context equivalence; Bridges carry all Cross‑context semantics.
* **F.15 (SCR/RSCR Harness).** Any `…Spec` must link to its harness; RSCR re‑checks verdict stability across editions/windows.

**Is used by.**

* **Part C Extention Patterns.** Sys‑CAL, KD‑CAL, Kind-CAL, Method‑CAL cite `…Description/…Spec` epistemes explicitly and consume **state attestations** from `U.Evaluation`.
* **Part B trust calculus.** Uses the presence/absence of harnessed Specs and the windowed nature of attestations in confidence roll‑ups.

### E.10.D2:11 - Migration notes (conceptual refactor playbook)

> Goal: remove conflations and normalise names without changing underlying models.

1. **Rename by default.** Any `XSpec` lacking a bound acceptance harness becomes **`XDescription`**. Keep content intact; change suffix and preface with a “Description, not Spec” note.
2. **Promote selectively.** For epistemes that *are* testable and declare **F ≥ F4**, add harness links (F.15) and re-label as **`XSpec`** via the Spec-gate.
3. **Fix the verbs.** Rewrite “Role contains RSG/RCS” → “Role is **characterised by** RSG/RCS in RoleDescription”.
4. **Detach carriers.** Replace identity‑by‑file with **`U.Carrier` encodes …Description/Spec** wording.
5. **Add Contexts.** Where a Description drifts globally (“the backlog refinement is…”), prefix with the Context and adjust wording to be **local**.
6. **Split planes.** Move any Evidence/Requirement **statuses** out of role state lists; keep them as roles over **knowledge units**.
7. **Window‑ise verdicts.** Ensure every evaluation statement adds an explicit **window** (instant or interval).
8. **Document maturity.** **Declare each Description’s F** (C.2.3) and track **ΔF** promotions/demotions as part of change notes (no governance implied).

### E.10.D2:12 - Acceptance tests (SCR/RSCR — concept‑level)

#### E.10.D2:12.1 Static conformance checks (SCR)

* **SCR-D2-S01 (Suffix discipline).** Every episteme with suffix **–Spec** passes the **Spec-gate** (**F ≥ F4** ∧ testable invariants ∧ harness link ∧ Context named). Otherwise it bears **–Description**.
* **SCR‑D2‑S02 (Characterisation verbs).** Texts never say an intension “contains” RCS/RSG; they say it is **characterised by** them via the Description/Spec.
* **SCR‑D2‑S03 (Plane purity).** No episteme mixes role **states** and knowledge **statuses**; each appears only on its correct plane.
* **SCR‑D2‑S04 (context‑locality).** Every Description/Spec names its `U.BoundedContext`; wording reads correctly when prefixed by the Context.
* **SCR‑D2‑S05 (Two registers).** Tech **and** Plain labels present on all Descriptions/Specs.
* **SCR‑D2‑S06 (Carrier separation).** Identity statements refer to Epistemes; files are referenced only as `U.Carrier` encodings.
* **SCR‑D2‑S07 (Windowed evaluation).** All state attestations cite a window `W` (instant or interval).

#### E.10.D2:12.2 Regression checks (RSCR)

* **RSCR‑D2‑E01 (Spec demotion guard).** If a **–Spec** loses its harness or testability, it is demoted to **–Description**; diffs show no lingering “shall” claims.
* **RSCR‑D2‑E02 (Bridge drift).** If two Contexts begin to share identical labels, verify no Descriptions/Specs imply Cross‑context identity; add or revise **F.9 Bridges** instead.
* **RSCR‑D2‑E03 (Edition churn).** When a Context’s canon updates, previously valid attestations remain historical (windowed); new Specs/Descriptions cite the new edition.
* **RSCR‑D2‑E04 (Verb hygiene).** Automated grep over corpus finds “contains RSG/RCS” phrasing; none remain after refactor.
* **RSCR‑D2‑E05 (Status bleed).** Spot‑audit a random sample of role graphs to ensure no epistemic/deontic statuses appear as role states.

*Didactic takeaway.*
Think in three layers: **Intension** (what the thing *is*), **Description/Spec** (how we *state* its character and, when mature, *test* it), and **Evaluation** (what we can *attest* about it in a **window**). Keep Contexts local, planes separate, and “contains” out of your vocabulary.

### E.10.D2:13 - Author’s pocket guide (carry‑in‑mind rules)

> **Use these as thinking cues, not as paperwork.** Each cue is a one‑breath test you can apply while writing.

1. **Name the Context.** Write “*Role (ITIL4)*”, “*Method (Essence‑language)*”, “*Execution (PROV)*”. Never speak global words.
2. **Pick the described entity and lane.** Am I talking about an **intension** (Role/Method/Service), a **Description/Spec**, an **Evaluation**, or a **Carrier**? Keep one described entity and one lane per sentence.
3. **Prefer –Description.** Use **`…Description`** by default. Switch to **`…Spec`** only after the **Spec‑gate** (testable invariants + harness + F‑mode).
4. **Characterised by…** Say *“Role is **characterised by** RCS/RSG recorded in RoleDescription”*, never *“Role **contains** its states”*.
5. **Window every verdict.** An Evaluation must read “*X ∈ State\@context **in** W*”. No naked, timeless verdicts.
6. **Status ≠ state.** Role **states** live in `U.RSG`; Evidence/Requirement **statuses** classify **knowledge units**. Do not mix.
7. **Bridge later.** If two Contexts “feel the same”, write the itch down and leave it for **F.9 Bridge**.
8. **Two registers.** Every Description/Spec has **Tech** and **Plain** labels; prefer the shortest tech term that matches the invariants.
9. **Carrier humility.** Files and records are **Carriers** of Descriptions/Specs; they don’t *equal* the thing you reason about.
10. **Spec = test.** If you can’t point to a harness that would falsify it, it isn’t a **Spec** yet.

### E.10.D2:14 - Phrasebook & pitfall table (say this, not that)

| Mistaken phrasing (avoid)              | Didactically correct phrasing (use)                                                                                  | Why                                                                                        |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| “The Role **contains** its states.”    | “The **Role** is **characterised by** RCS/RSG **recorded in** the RoleDescription.”                                  | Roles are intensions; state graphs live in their **Descriptions/Specs** (knowledge plane). |
| “MethodSpec (draft).”                  | “**MethodDescription** (Essence‑language Context); not a Spec yet.”                                                     | **–Spec** is reserved for testable artifacts that passed the Spec‑gate.                    |
| “We proved the service meets the SLO.” | “**Evaluation** attests *Service ∈ Met\@ITIL4 in W* based on observations and the **Acceptance harness**.”           | Evaluations produce **windowed attestations**, not timeless facts.                         |
| “Evidence status is a role state.”     | “**Evidence status** classifies a **KnowledgeUnit**; **Role states** live in RSG. Different planes.”                 | Prevents status/state conflation.                                                          |
| “The PDF is the Method.”               | “The PDF is a **Carrier** that **encodes** a **MethodDescription**.”                                                 | Carrier ≠ content.                                                                         |
| “BPMN workflow = PROV activity.”        | “Add a **Bridge (F.9)** if needed; in F.1/F.2/F.3 we treat them as **context‑local** senses.”                           | No Cross‑context identity outside Bridges.                                                    |
| “WorkSpec / WorkPlan (synonyms).”      | “**U.WorkPlan** (preferred). **WorkDescription** is an allowed alias; **WorkSpec** is deprecated.”                   | Aligns with the –Description/–Spec discipline.                                             |
| “RoleSpec is our template.”            | “**RoleDescription** is our template; promote to **RoleSpec** once the harness exists.”                              | Keeps the Spec word meaningful.                                                            |
| “Spec says the same in all Contexts.”     | “Each **Spec/Description** is **context‑local**; Cross‑context reuse requires an **Alignment Bridge** with CL/loss notes.” | Locality guard.                                                                            |

### E.10.D2:15 - Naming & alias policy (normative, notation‑free)

#### E.10.D2:15.1 - Suffix discipline (recap).**

* **Preferred default:** **`…Description`** for Role/Method/Service/Work.
* **Reserved:** **`…Spec`** only if the item passed the **Spec‑gate** (F‑mode, testable invariants, harness id, Context named).
* **Banned:** Using **–Spec** as a synonym for “detailed description”.

#### E.10.D2:15.2 - Canonical/alias map (current edition).**

| Concept (intension) | Preferred episteme name      | Allowed alias (equal scope)   | Deprecated alias | Notes                                                                                 |
| ------------------- | ---------------------- | ----------------------------- | ---------------- | ------------------------------------------------------------------------------------- |
| Role                | **RoleDescription**    | RoleCard *(Pedagogy only)*    | —                | *RoleCard* is informal (teaching layer), not a normative episteme name.                     |
| Role (F‑mode)       | **RoleSpec**           | —                             | —                | Only after Spec‑gate.                                                                 |
| Method              | **MethodDescription**  | —                             | **MethodSpec**   | Global rename complete; legacy references should be updated.                          |
| Method (F‑mode)     | **MethodSpec**         | —                             | —                | Now reserved for harnessed, testable methods.                                         |
| Work (schedule)     | **U.WorkPlan**         | **WorkDescription**           | **WorkSpec**     | *WorkSpec* alias removed; *WorkDescription* remains as didactic alias for *WorkPlan*. |
| Service             | **ServiceDescription** | ServiceCard *(Pedagogy only)* | —                | As above: Card is informal only.                                                      |
| Service (F‑mode)    | **ServiceSpec**        | —                             | —                | Requires acceptance harness id (F.15).                                                |

#### E.10.D2:15.3 - Verb & morphology rules.**

* **Verbs.** Use *characterised by*, *recorded in*, *encoded by*; avoid *contains*, *is stored in*, *is implemented by* when speaking at the conceptual level.
* **Morphology.**

  * Roles name **masks** as **count nouns** (*Operator, ChangeAuthority*).
  * States as **state nouns/participles** (*Authorized, Active*).
  * Status names are **classifiers over knowledge** (*SupportsClaim, NormativeStandard*).
  * Descriptions/Specs use neutral nouns (*RoleDescription, MethodSpec*).

#### E.10.D2:15.4 - Deprecations (effective now).**

* **MethodSpec** (as a general name) → **MethodDescription** unless Spec‑gate is met.
* **WorkSpec** (alias for WorkPlan) → **WorkDescription** (allowed alias), or **U.WorkPlan** (preferred).
* Texts must avoid “contains RSG/RCS” phrasing (see RSCR‑D2‑E04).

### E.10.D2:16 - Quick templates (fill‑in‑mind, not forms)

> Copy these **lines** into your prose as thinking scaffolds. They are not schemas, fields, or checklists to fill; they are didactic prompts.

#### E.10.D2:16.1 - Role (default).

* *Intension.* `U.Role :: <TechName> in <ContextId>`.
* *RoleDescription\@context.* Tech/Plain: **`<TechName> / <PlainName>`**.

* **RCS characteristics.** `<characteristic₁ ∈ {… }>; <characteristic₂ ∈ {… }>`.
* **RSG nodes (→).** `<S₀ → S₁ → …  → Sₙ>`.
* **State checklist (one node).** `<StateX : {criterion₁, …}>`.
* *Evaluation attestation.* `subject=<Holder> ∈ <StateX>@<ContextId> in <Window> (evidence: <cue₁,…>)`.

#### E.10.D2:16.2 - Method (Essence‑language Context).

* *Intension.* `U.Method :: <TechName>`.
* *MethodDescription\@context.* Inputs and outputs (informative), **RCS/RSG** (if you track adoption).
* *Spec upgrade (optional).* “Becomes **MethodSpec** when harness `<id>` exists.”

#### E.10.D2:16.3 - Service (acceptance‑bearing).**

* *ServiceDescription\@context.* Tech/Plain; **Acceptance facet** (informative until harnessed).
* *Evaluation.* `Service ∈ Met/Not‑Met@context in <Window>` based on observations and acceptance criteria.

#### E.10.D2:16.4 - Alignment reminder.

* “No Cross‑context identity is implied; if needed, add **F.9 Bridge**: `<ContextA:TermA> ↔ <ContextB:TermB>` with CL/loss notes.”

### E.10.D2:17 - Didactic distillation (90‑second script)

> **“Three layers; one context; no leakage.”**

1. **Pick the Context.** Every word lives **inside** a `U.BoundedContext`.
2. **Pick the I/D/S layer.** Speak about the **Intension (I)**, or about its **Description/Spec (D/S)**—but never mix layers. If your sentence also asserts describedEntity or evidence, **name the `ReferencePlane`** (`world|concept|episteme`).
3. **Describe, then test.** Start with **Role/Method/ServiceDescription**. Only when you can **falsify** it with a harness do you call it a **Spec**.
4. **State is attested.** Role **states** are attested by **Evaluations** as *“X ∈ State\@context **in** W”*. Evidence/Requirement **statuses** classify **knowledge**, not roles.
5. **Carriers carry.** PDFs and repos are **Carriers** of the Description/Spec; they aren’t the thing itself.
6. **Bridges are explicit.** Cross‑context sameness is never assumed; you declare a **Bridge** with CL/loss.
   Follow these six lines and SD (*Strict Distinction*) stops being an abstraction—you feel it in every sentence you write.

### E.10.D2:End

## E.11 - First-Practical Entry and Pattern-Use Discoverability Discipline

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### E.11:1 - Problem frame

One cold reader often enters `FPF` with one ordinary work phrase rather than one
pattern ID. The reader may see several plausible patterns, one search result,
one `Preface` blurb, one `J.4` row, or one local pattern opening, but still not
know which authoritative pattern to inspect first, which nearby pattern is only
support or a tempting wrong first stop, and where the admissible entry stop belongs.

Pattern-entry discoverability is the discipline that makes that first
recognition honest without turning the pattern language into workflow.

Use this pattern when the reader can name the entry load in ordinary work language
but still cannot tell which pattern to inspect first, which nearby pattern is
only support, and where the first admissible entry stop belongs.

What goes wrong if this pattern is missed:

- `Preface`, `README`, `J.4`, one search result, or one local top is treated as
  if it were the authoritative pattern rather than one projection or support
  role;
- one plausible nearby pattern becomes a hidden required next step because
  entry language turns into workflow language;
- lexical support turns into synonym stuffing instead of governed query cues;
- readers repeat the same wrong first guesses because the corpus never
  publishes one explicit entry-neighborhood discipline.

What this pattern buys:

- the first honest entry load becomes nameable near the point of use;
- candidate patterns, tempting wrong patterns, and admissible entry stops become
  visible without minting a workflow;
- support/projection roles can help the reader recover the right pattern
  without competing with the governing pattern body.

Ordinary not-this-pattern boundary:

- not when the real entry load is first-contact recognition of one single
  encountered description; use `A.6.RSIG`;
- not when the real entry load is already one published route, language-state cue,
  endpoint publication line, or work sequence;
- not when the authoritative pattern is already known and the remaining job is
  only didactic order or lexical repair;
- not when a formal quality claim about discoverability is being made; route
  that quality claim through `C.25` / `A.6.Q` as applicable.

### E.11:2 - Problem

Pattern-entry discoverability loads are spread across `Preface`, `J.4`,
`I.2`, local pattern `Problem frame`s, table-of-content query rows, and
lexical-support patterns. Without one governing pattern for their split, readers
can infer false sequence, wrong pattern, wrong governing pattern body, or shadow
projection authority because the support roles are under-governed.

### E.11:3 - Forces

| Force | Tension |
| --- | --- |
| High recall vs high precision | Coarse orientation helps the reader enter quickly without creating false confidence or false sequence. |
| Local fit vs corpus consistency | Pattern-local cues stay honest while the corpus avoids stale echoes and duplicated load-bearing guidance. |
| Subject-domain wording vs canonical wording | Readers search in real phrases, but canonical names and governed distinctions stay admissible. |
| Quick orientation vs anti-workflow discipline | Entry support helps pattern selection without reading like route execution, handoff, or pipeline. |
| Reader economy vs fanout control | More support roles can help entry, but repeated near-duplicate guidance creates contradiction risk and maintenance cost. |
| Human and AI-assisted retrieval vs authority | Retrieval may return helpful fragments, but fragments must not answer as if they were the applicable governing pattern body. |

### E.11:4 - Solution

#### E.11:4.1 - Governed object, non-goals, and non-minting boundary

`E.11` governs pattern-entry discoverability for `FPF` and
`FPF`-conformant pattern-language support roles: the coordination discipline by which one
reader can bring plausible authoritative patterns into view, compare them,
reject tempting wrong patterns and wrong governing pattern bodies, use admissible
projection/support roles, and reach one admissible entry stop or entry-load
reclassification without reading the pattern language as workflow.

In `E.11`, the live governed case is pattern-entry discoverability. Description
discoverability remains governed by `A.6.RSIG`; `E.11` mentions it only to
preserve the semantic-name settlement and support-role partition.

`E.11` does not govern:

- discoverability trigger-word repair or naming assets that belong to
  `A.6.P / F.18 / E.10`;
- description-recognition signatures in general, which belong to `A.6.RSIG`;
- local first-reading placement and form, which belong to `E.8`;
- `DRR` and campaign content decisions, which belong to `E.9`;
- ordinary pattern authoring and pattern-content changes, which belong to `E.8`
  plus the governing domain pattern unless a live pattern-entry discoverability
  defect is being repaired;
- didactic order, learning order, cognitive-load ramping, tutorial sequence,
  progressive mastery, and teaching examples after the relevant pattern family
  has already been identified;
- workflows, process routes, control-flow graphs, prescribed method sequences,
  work handoffs, or runtime execution stops;
- the governing semantics of referenced patterns;
- formal quality treatment, which belongs to `C.25` / `A.6.Q` when the claim
  becomes evaluative;
- graph ontology in `E.18`.

This pattern does not mint one new `U.Discoverability`, `RelationKind`,
`PatternKind`, `StatusKind`, `SurfaceKind`, graph node, or workflow state.

#### E.11:4.2 - Pattern-entry discoverability claim and FPF strata

Pattern-entry discoverability is one composite quality-facing concern over
whether one reader can:

- bring the right candidate patterns into view, together with any admissible
  support roles needed for comparison;
- recognize applicability or non-applicability;
- avoid common wrong patterns, wrong governing pattern bodies, or projection-only
  fragments answered as if they were authoritative;
- reach one admissible entry stop or entry-load reclassification.

This pattern keeps these semantic heads distinct:

| Head | Working meaning here |
| --- | --- |
| `pattern-entry discoverability` | one composite entry quality over a support/projection stack inside a pattern language |
| `description-recognition signature` | one first-contact cue structure of one encountered description, governed by `A.6.RSIG` |
| `first-reading role` | the local reading job carried by an existing pattern section or projection; not a new surface kind |
| `lexical-query support` | cue-to-pattern/source access through the reader's words, domain phrases, and query cues without alias minting |
| `worked entry reading` | one explanatory reading case, not `U.Work`, not a workflow, and not an execution trace |
| `entry neighborhood` | one case-relative editorial grouping or `J.4` row, not a graph node, route, selector output, or object kind |
| `thin echo` | lower-case projection discipline: a reminder or pointer, not a `U.Type`, publication-face kind, or authority relation |

None of those heads is a synonym for the others. This pattern routes each
effect to its applicable governing pattern body or applicable projection role rather than letting
`discoverability` become one semantic swamp.

Reader-facing entry language speaks primarily in pattern-language terms:
`candidate pattern`, `nearby pattern`, `tempting wrong pattern`, `entry-load
reclassification`, `admissible entry stop`, `thin echo`, and `applicable governing pattern body`.

`owner` and `ownership` are not default reader-facing terms here. Use them only
when the live question is responsibility or stewardship assignment, process-law owner-set
control, or explicit authority-conflict diagnostics; do not use them as substitutes
for candidate pattern, nearby pattern, publication, file carrier, or project record.

#### E.11:4.3 - Pattern-language navigation stance and case-orientation snapshot

An `entry neighborhood` is one case-relative editorial grouping of plausible
candidate patterns, nearby patterns, common misclassifications, entry-load
reclassifications, and admissible entry stops under one first honest entry load.

`candidate patterns` here are case-plausible patterns to inspect under one
named entry load. They are not `OptionSet`s, candidate pools, selected sets, or
selector outputs unless another authoritative pattern explicitly promotes that
structure.

`nearby pattern` means case-near for recognition, disambiguation, or entry-load
reclassification. It does not mean next, required, dependent, broader,
narrower, or pedagogically prior.

Authors can use one lower-case `case-orientation snapshot` as an editorial lens
over the current cues, current entry-load hypothesis, plausible candidate patterns,
tempting wrong pattern, disambiguating fact, admissible entry stop, and current
reading role. It is not one canonical persisted object and does not create a
transition history.

Minimal example:

```text
case_signal = "we need a shortlist, not one winner"
current_entry_load_hypothesis = selected-set publication or candidate-pool policy
plausible_candidate_patterns = C.19; G.5 only when selected-set publication is live
nearby_patterns_or_reclassifications = C.11, C.24, A.19 comparator/selector supports
tempting_wrong_pattern = C.11
disambiguating_fact = output remains a governed set, not one local choice
admissible_entry_stop = inspect C.19 if pool policy is live; inspect G.5 if publication is live; inspect C.11/C.24 only after the entry load narrows

```

#### E.11:4.4 - Entry-orientation labels and entry-load reclassification discipline

The local `FPF` application of this pattern is the coordination discipline for
first-practical entry orientation over the `FPF` pattern language: support-role
partition, entry-bearing vs nearby-pattern discipline, entry-load-reclassification
presentation, thin-echo discipline, entry-lexeme-support hooks, and review
hooks.

Route-shaped wording can blur entry orientation with admissible publication seams,
early language-state route publication, endpoint publication, `A.6.B` L/A/D/E-classified claim
structure, `DRR` claim routing, or actual method sequencing or work sequencing. Repair that
blur by typing the live entry load explicitly rather than by treating every
route-shaped phrase as entry guidance.

Use this placement test whenever one pattern-entry discoverability-bearing
claim or wording repair is being placed:

| If the claim is about... | Route it to... |
| --- | --- |
| first bringing candidate patterns into view through reader words, domain phrases, or query cues | lexical-query support under `F.17, F.18, and E.10`, coordinated by `E.11` only where the pattern-entry load is live |
| one description's first-contact recognition, truthful applicability signal, or defining `U.Episteme` | `A.6.RSIG` |
| choosing among patterns, candidate patterns, nearby patterns, wrong governing pattern bodies, or entry-load reclassifications inside the pattern language | `E.11` |
| the admissible local `Problem frame` first-reading role, reading order, or recognition/assurance relation | `E.8` |
| review trigger, evidence-mode selection, or cross-role parity checks for one pattern-entry discoverability-bearing change | `E.19 / PCP-ENTRY` |
| one compact or worked projection of already-governed pattern-entry discoverability content | `J.4`, `I.2`, `Preface`, the pattern `Problem frame`, or lexical support according to the governing-role map |
| the order in which one already-identified area is learned or taught | `E.6`, `E.7`, `E.12`, `F.16`, and the appropriate tutorial views or walkthroughs |
| cue preservation, route-bearing publication, or endpoint publication | `A.16`, `A.16.1`, `B.4.1`, or the relevant publication pattern |
| one actual work sequence, method, plan, episteme publication, work-result record, or execution stop | the relevant pattern for method description, work planning, or work occurrence rather than `E.11` |
| the meaning of the actual pattern, method, boundary description, or other governed object | the relevant authoritative pattern or governing pattern/source rather than the entry support role |

`E.11` uses only lower-case editorial labels when reviewers need a compact
diagnostic vocabulary:

- entry-orientation labels: `candidate-pattern`, `nearby-pattern`,
  `entry-load-reclassification`, `common-misclassification`;
- projection-support labels: `lexical-support`, `worked-reading-expansion`;
- entry-posture labels: `entry-bearing`, `participant-only`,
  `entry-load-critical`;
- projection-purpose labels: `global-entry orientation role`,
  `catalogue-search support role`, `entry-neighborhood index role`,
  `worked-entry-reading support role`, `Problem-frame recognition role`,
  `entry-lexeme support role`, `review-profile role`, `assurance-support role`.

These labels are optional reviewer/editor vocabulary. They are not exported
kind families and are not required authoring dimensions for ordinary pattern
repairs.

#### E.11:4.5 - Support-role partition, Problem-frame first-reading discipline, and README boundary

The concrete `FPF` application uses distinct support/projection roles:

- `Preface` gives coarse global orientation;
- `Table of Content` `Keywords & Search Queries` gives sparse
  catalogue-search and lexical-query support;
- `J.4` gives compact entry-neighborhood comparison;
- `I.2` gives worked entry readings for high-risk or compact-insufficient
  cases;
- the pattern's own `Problem frame` gives the primary local first-reading role;
- `F.17, F.18, and E.10` carry entry-lexeme support;
- `README` can echo the Core entry architecture and point to `Preface`, `J.4`,
  `I.2`, and selected pattern families.

`README` remains downstream of Core and does not introduce entry neighborhoods,
candidate patterns, or lexical names absent from Core. It changes when public
entry claims change materially, not for every internal local wording repair.

Canonical entry neighborhoods can use compact lexical-query support when the
lexical entry load is real. Query cues are retrieval aids, not aliases, Bridges,
equivalence claims, or semantic twins. A query cue becomes an alias only through
the relevant lexical/naming pattern or `authoritySourceRef` target.

Minimal visible lexical-query shape:

```text
canonical_label
plain_twin_if_governed
visible_query_cues
domain_query_examples
deprecated_cues
false_friends_or_forbidden_synonyms
```

Ordinary lexical-query support stays sparse:

- ordinary `Table of Content` rows: prefer `2-5` high-signal query phrases;
- ordinary `J.4` neighborhoods: keep only the most discriminating domain phrases and
  false friends;
- fuller lexical sets belong under `F.17, F.18, and E.10` only when one real
  naming, alias, bridge, or collision question exists.

#### E.11:4.6 - Fanout, thin-echo discipline, and semantic parity

Each entry/discoverability claim names one most applicable pattern body or governing
projection role. Other mentions remain thin echoes.

| Claim payload | Governing FPF pattern, source-maintenance role assignment, or projection role | Thin echoes allowed in |
| --- | --- | --- |
| trigger-word repair and naming fix | `A.6.P`, `F.18`, and `E.10` | quoted local reminders only when needed for user safety |
| description-recognition-signature claim | `A.6.RSIG` | one bounded publication/view cue under `E.17` when needed |
| compact entry-neighborhood row | `J.4` | `Preface`, README, one pattern's `Problem frame` |
| worked entry reading | `I.2` | one compact `J.4` pointer |
| local problem-frame recognition cue | the pattern `Problem frame` under `E.8` | `J.4` as cross-pattern comparison |
| lexical-query cue | `F.17`, `F.18`, or `E.10`; or a bounded ToC or J.4 support hook | `I.2`, README, and local prose only as sparse cues |

Support-role parity means semantic consistency of first-contact entry load, governing
FPF pattern, source-maintenance role assignment, governing projection role, wrong-pattern boundary, projection-only
status, and no claim with broader authority than the Core pattern body. It does not require
identical wording, identical examples, identical rows, or exhaustive coverage
across all support/projection roles.

#### E.11:4.7 - Change propagation, compact pattern-local-note discipline, and `PCP-ENTRY` hook

Authors do not introduce `Entry-orientation account` as a standalone artifact
family.

For material entry/discoverability changes, the author leaves one compact pattern-local note
inside the `DRR`, `PCP` record, patch note, or equivalent pattern-local note record.
Ordinary wording repairs do not require a separate note when candidate-pattern
force, first honest entry load, applicable governing pattern body or applicable projection role, and
support role remain unchanged.

Allowed pattern-local note shape:

```text
Entry-change note:
changed projection or support role:
changed first-contact entry load:
applicable governing pattern body or projection role:
wrong-pattern or parity risk:
selected check, if any:
```

If the note takes more than a few lines for an ordinary material entry change,
the change is probably too large for a local note or should escalate to a real
`DRR` / `PCP` record.

`PCP-ENTRY` is the narrow additive review profile for material
pattern-entry-discoverability changes. It is risk-triggered rather than
universal and reviews only entry-facing effects.

A pattern does not need a `J.4` row merely because it exists. A `J.4` row is
needed only when the pattern or neighborhood is a likely first practical entry,
a common wrong first guess, or a public/retrieval-facing entry point.

`I.2` worked readings are rare-depth. A compact-index-only posture is a
complete admissible entry result when the `J.4` row plus pattern `Problem frame` are
enough for the entry load.

#### E.11:4.7.1 - Minimum viable entry discipline

For an ordinary `E.11`-triggered entry-discoverability change, the minimum is:

1. the `Problem frame` names the working situation;
2. it names or implies the first candidate pattern or `authoritySourceRef` target;
3. it rejects one tempting wrong reading if that risk is live;
4. it does not imply workflow, handoff, or route order;
5. any support role remains a thin echo.

Everything else is triggered:

- `J.4` row: only if it is a likely first entry or common wrong first guess;
- `I.2` worked reading: only if compact guidance repeatedly fails or risk is
  high;
- ToC lexical cues: only if search/query support is material;
- README/Preface echo: only if public entry changes materially;
- pattern-local note: only for material entry-force changes;
- evidence mode: only for high-risk, disputed, retrieval-facing,
  repeated-failure, or measured-improvement claims.

### E.11:5 - Archetypal grounding

#### E.11:5.1 - System-side worked entry repair: shortlist entry load, not one-off choice

Live reader phrase:

> "We need a shortlist, not one winner."

Why the phrase is easy to mishandle:

- `C.11` looks tempting because a local decision may eventually happen;
- `G.5` looks tempting because publication may happen later;
- `C.24` can be nearby when the missing object is a tool-call plan;
- one reader can mistake the live entry load for a required next step in a hidden
  selection workflow.

Entry repair:

1. first honest entry load = selected-set shaping, candidate-pool policy, or
   selected-set publication, not automatically one-off local choice;
2. plausible candidate patterns = `A.19.CN`, `A.17-A.19`, `C.18`, `C.19`,
   `G.0`, and `G.5` when selected-set publication is already live;
3. nearby / entry-load-reclassification patterns = `C.11` only after the entry load
   narrows to one local decision doctrine, `C.24` only when the next honest
   C.24 object is a `CallPlan` or `CheckpointReturn`, and `A.19.CPM` /
   `A.19.SelectorMechanism` when comparator/selector structure is live;
4. disambiguating fact = the desired output remains a governed set or
   shortlist rather than one local winner;
5. admissible entry stop = inspect `C.19` if pool/candidate policy is live; inspect
   `G.5` if selected-set publication is already live; inspect `C.11` or `C.24`
   only after that narrower entry load is actually live.


#### E.11:5.2 - Episteme-side anti-case: partly-said cue is not yet a claim

Live reader phrase:

> "This phrase matters, but it is not yet a claim."

Plausible but wrong first reading:

- the reader jumps straight to `A.6.P`, `A.6.Q`, `A.6.A`, or `C.25` because
  the phrase sounds conceptually important.

Entry repair:

1. first honest entry load = cue preservation and entry-load typing, not endpoint claim
   publication;
2. plausible candidate patterns = `C.2.LS`, `A.16`, `A.16.1`, `B.4.1`,
   `B.5.2.0`;
3. tempting wrong pattern = any endpoint claim, action, or quality pattern that
   assumes the cue is already stable enough to publish as a claim;
4. admissible entry stop = cue preserved, entry plurality opened, or entry load
   reclassified honestly; if the phrase is already a boundary claim, inspect
   `A.6.B` / `A.6.C` instead.

#### E.11:5.3 - Episteme-side worked entry repair: same-entity rewrite

Live reader phrase:

> "We need to explain the same described entity for another audience."

Entry repair:

1. first honest entry load = same-entity retextualization, representation-scheme
   transition, explanation-facing rendering, or bounded comparative reading;
2. plausible candidate patterns = `A.6.3.CR`, `A.6.3.RT`, `E.17.EFP`,
   `E.17.ID.CR`;
3. tempting wrong pattern = minting one second `U.Episteme` for the same claim or one parallel rule
   lane;
4. disambiguating fact = the governed `U.Episteme` or `PublicationUnit` stays the same; only rendering,
   reading posture, or explanatory framing changes;
5. admissible entry stop = same-entity rewrite opened or explanation-facing
   rendering stabilized with source pins.

#### E.11:5.4 - Quick compact-index-only examples

- **Project alignment.** If the first entry load is responsibility/method/plan vs
  run confusion, `A.15` and neighboring work/role patterns are likely first
  governing pattern bodies; `F.17` is a typical vocabulary stabilizer when vocabulary is
  unstable. This can stay compact-index-only unless repeated readers confuse it
  with the whole FPF method.
- **Generator, SoTA, or portfolio kit.** If the work is to publish a reusable
  search/harvest/portfolio scaffold, inspect `A.0`, `G.0`, `G.1`, `G.2`, and
  `G.5`. This can stay compact-index-only unless portfolio/generator entry is
  repeatedly misclassified as one-off recommendation.

### E.11:6 - Bias-Annotation

This pattern counters:

- workflow bias;
- programmer's-bias graph language;
- front-door centralization bias;
- synonym-soup bias;
- support-projection authority bias;
- `owner`-word bias in reader-facing entry language.

### E.11:7 - Conformance checklist

- **CC-E11-0 Affordability.** Entry guidance is non-conforming when it becomes
  more expensive to author, review, or read than the discoverability risk
  warrants.
- **CC-E11-1 No workflow.** Entry prose does not imply mandatory sequence,
  handoff, route execution, baton transfer, control state, or artifact
  pipeline.
- **CC-E11-2 Pattern authority.** Entry support roles do not redefine the
  governing semantics of the authoritative pattern.
- **CC-E11-3 Governing entry / thin echo.** Each entry/discoverability claim has
  one applicable governing pattern body or applicable projection role; other mentions remain thin
  echoes.
- **CC-E11-4 Pattern-language vocabulary.** Reader-facing entry prose uses
  candidate patterns, nearby patterns, tempting wrong patterns, entry load
  reclassification, and admissible entry stop rather than next-step vocabulary.
- **CC-E11-4a Editorial labels only.** Entry labels in `E.11` are editorial
  projection labels over existing patterns, sections, rows, or publication
  faces. They do not create `PatternKind`, `RelationKind`, `StatusKind`,
  `SurfaceKind`, `Role`, `U.Type`, graph node, or workflow state.
- **CC-E11-5 Problem-frame first-reading role.** Local problem-frame recognition
  remains in the pattern's `Problem frame`; `J.4`, `I.2`, lexical support, and
  `README` do not become competing local recognition pattern bodies.
- **CC-E11-6 Quality boundary.** Formal quality claims about discoverability or
  recognition apply `C.25` or `A.6.Q` as applicable; `E.11` coordinates
  pattern-entry use, not quality authority.
- **CC-E11-7 Semantic parity.** Multi-role changes keep entry load, authority,
  boundary, and projection-only status compatible without requiring identical
  wording or exhaustive coverage.
- **CC-E11-8 Worked reading threshold.** High-risk, often-misclassified,
  repeatedly failed, retrieval-facing, or materially new entry neighborhoods
  have either one worked entry reading or one explicit compact-index-only
  posture.
- **CC-E11-9 Lexical-query support.** Material lexical divergence is handled
  through governed lexical-query support, not synonym stuffing or alias
  equivalence.
- **CC-E11-10 Retrieval-facing claim.** Retrieval fixtures are used only when
  retrieval behavior is explicitly claimed, observed to fail, or
  machine-facing projection support is in scope.

### E.11:8 - Common Anti-Patterns and How to Avoid Them

- **Problem-frame absence.** The pattern body is lawful, but the first-use
  situation is still unclear. Repair by rewriting the `Problem frame` for the
  first-reading role.
- **Top overgrowth.** The opening carries architecture placement, token guards,
  route fields, or law before the working situation is clear. Repair by moving
  heavy material to `Solution`, `Relations`, `Conformance`, or `I.2`.
- **Route smuggling.** Local text says `Start here`, `next governing pattern`, `next actor`, `handoff`, or
  `reroute` as if it were a sequence. Repair by replacing it with candidate
  patterns, nearby patterns, entry-load reclassification, and admissible entry stop.
- **Shadow projection.** `J.4`, `README`, or another projection defines pattern
  semantics. Repair by moving that definition back to the authoritative pattern
  and leaving only one thin echo.
- **Lexical stuffing.** Pattern bodies fill themselves with synonyms for
  findability. Repair by routing lexical support through `F.17, F.18, and E.10`.
- **Entry-block-as-ontology.** A temporary map of neighborhoods is frozen as if
  it were one stable ontology. Repair by keeping neighborhoods case-relative
  and projection-scoped.

### E.11:9 - Consequences

This pattern gives `FPF` one explicit coordination discipline for pattern-entry
discoverability instead of leaving the entry guidance fragmented across `Preface`,
`J.4`, `I.2`, pattern tops, query rows, and lexical support lanes.

It also imposes discipline: entry support becomes thinner, more explicit about
its authoritative patterns and support roles, and less tolerant of
workflow-shaped wording. The cost stays bounded because worked readings,
pattern-local notes, parity scans, retrieval fixtures, and evidence modes are triggered
by risk rather than required for ordinary wording repairs.

### E.11:10 - Rationale

This pattern is needed because the entry problem is no longer only local pattern form
and not only lexical repair. `E.8` governs local first-reading form;
`A.6.RSIG` governs the neutral description-recognition-signature substrate;
`E.19` reviews risk-triggered entry changes. The cross-pattern entry law still
needs its own governing pattern.

### E.11:11 - SoTA-Echoing

This pattern is an `FPF`-local pattern-entry discipline. It adopts current
discoverability, documentation-mode, taxonomy, pattern-validation,
human/AI-facing, and retrieval practices only where they preserve one
entry-load-oriented entry reading over a pattern language. It rejects turning that
reading into one workflow, front door, route graph, synonym store, or
retrieval-tooling ontology.

| Pattern claim carried here | Source-bearing SoTA support (post-2015) | Alignment with `E.11` | Adoption status and worked-slice implication |
| --- | --- | --- | --- |
| Pattern-entry starts from first honest entry load and candidate-pattern recognition, not chapter order or route execution. | Jorge Arango (2018), *Living in Information: Responsible Design for Digital Places*; Raluca Budiu (2020), "Information Scent: How Users Decide Where to Go Next", Nielsen Norman Group. | Information-architecture practice supports orientation through places, labels, context, and reader expectations. `E.11` adopts scent as first-contact cue economy, then adds governing-pattern-body recovery, tempting-wrong-pattern rejection, entry-load reclassification, and admissible entry stop. | **Adopt and add governing-pattern-body discipline.** Adopt cue economy and entry-load-oriented orientation; reject scent, familiar wording, or a retrieved support echo as sufficient governing pattern body. In the shortlist case, the manager distinguishes selected-set publication, candidate-pool policy, and one-off choice before opening the wrong pattern. |
| Pattern-entry support needs role partition: coarse orientation, compact index, worked reading, local first-reading role, and lexical support are different jobs. | ISO/IEC/IEEE 26514:2022; Daniele Procida, *Diataxis* documentation framework (2017-2025). | User-information and documentation-mode practice separates information needs and presentation modes. `E.11` extends this from documentation form to governing-pattern-body recovery and wrong-pattern rejection. | **Adapt.** Adopt mode separation; reject replacing pattern authority with documentation architecture. Practitioners get compact rows in `J.4`, worked readings in `I.2`, and local recognition in the authoritative pattern. |
| Entry lexemes and query cues need controlled governance, but lexical support is not alias minting and not semantic equivalence. | Helen Lippell, ed. (2022), *Taxonomies: Practical Approaches to Developing and Managing Vocabularies for Digital Information*. | Taxonomy practice supports governed terms, validation, and maintenance for search, browse, and interpretation. `E.11` routes query cues, false friends, and plain twins through `F.17, F.18, and E.10`, `J.4`, `I.2`, and ToC rows instead of stuffing synonyms into every pattern body. | **Adapt.** Adopt lexical-query discipline; reject uncontrolled alias growth. In the partly-said anti-case, subject-language cues help find the neighborhood while the cue remains not-yet-claim. |
| Human and AI-assisted readers need clear capability, limitation, and uncertainty cues. | Amershi et al. (2019), "Guidelines for Human-AI Interaction", CHI 2019. | Human-AI guidance validates the need to make capabilities and limits clear enough for calibration. `E.11` adapts this into public and machine-assisted entry: thin echoes say what they can point to and what they cannot define, while `A.6.RSIG` fields such as applies-to, excludes, defining `U.Episteme`, and admissible entry stop calibrate what an encountered description can and cannot settle. | **Adapt and narrow.** Adopt expectation management for mixed human/AI reading; reject an AI-interface pattern. README and `Preface` should say "typical entry-stabilizing result" rather than promise guaranteed outputs, and the `E.19` LLM-retrieved-paragraph case should recover the applicable governing pattern body instead of letting a helpful fragment answer as authority. |
| Pattern-entry claims need accountable case-linked validation and selected evidence, but evidence cost is risk-triggered. | Riehle, Harutyunyan, and Barcomb (2020), *Pattern Discovery and Validation Using Scientific Research Methods*. | Pattern-validation practice supports explicit evidence beyond folklore. `E.11` adapts this into `PCP-ENTRY`, worked-entry readings, wrong-pattern checks, compact pattern-local notes, tiny golden cases, and selected evidence only when entry force, semantic support-role parity, public-entry risk, repeated failure, or retrieval-facing behavior warrants them. | **Adopt / lightweight.** Adopt accountable case-linked validation; reject universal empirical validation or heavy fixture work for ordinary wording or support-role/projection edits. |
| Retrieval-facing entry support must distinguish successful retrieval from correct pattern selection and faithful source use. | Lewis et al. (2020), "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"; Liu, Zhang, and Liang (2023), "Evaluating Verifiability in Generative Search Engines"; Gao et al. (2023), "Enabling Large Language Models to Generate Text with Citations"; Asai et al. (2024), "Self-RAG"; Saad-Falcon et al. (2023), "ARES"; Es et al. (2023), "RAGAS"; Wallat et al. (2024/2025), work on correctness versus faithfulness in `RAG` attributions. | Current retrieval and citation work distinguishes context relevance, retrieved support, citation precision/recall, answer faithfulness, attribution faithfulness, post-rationalized citation-like support, and adaptive retrieval. `E.11` adapts that into governing-pattern-body and thin-echo hygiene and selected retrieval fixtures that distinguish pattern hit, support-role hit, source faithfulness, projection-vs-governing-pattern-body ambiguity, stale-echo absence, and thin-echo anchor presence. | **Adapt, risk-triggered.** Adopt the hit/support/authority/faithfulness split; reject universal RAG benchmarking and reject citation-like support as authority by itself. In the "LLM retrieved a helpful paragraph but not the pattern" case, the repair is to recover the applicable governing pattern body, not to bless the fragment as authority. |

### E.11:12 - Relations

- **Builds on:** `A.6.RSIG`, `E.8`
- **Coordinates with:** `E.19 / PCP-ENTRY`, `J.4`, `I.2`, `F.17`, `F.18`,
  `E.10`, `E.6`, `E.7`, `E.12`, `F.16`, `C.25`, `A.6.Q`
- **Constrains:** reader-facing entry support roles for `FPF` and
  `FPF`-conformant pattern languages

### E.11:End

## E.12 - Didactic Primacy & Cognitive Ergonomics


### E.12:1 - **Problem Frame**

The FPF is designed as an "Operating System for Thought," a tool intended to augment and clarify human (and artificial) reasoning. This mission places a unique demand on its architecture: the framework's internal elegance and formal power are secondary to its primary function of being understandable and usable. A perfectly consistent but incomprehensible system fails in its didactic purpose. As formal mechanisms like `Assurance Levels` and epistemic scores are introduced, there is a significant risk that the pursuit of these metrics becomes an end in itself, overshadowing the ultimate goal of fostering clearer thought.

### E.12:2 - **Problem**

If the framework's design prioritizes theoretical purity or formal completeness over cognitive ergonomics, it becomes vulnerable to two critical failure modes:

1.  **Goodhart's Law:** When a measure (like `AssuranceLevel:L2`) becomes the primary target, it ceases to be a good measure of genuine understanding. Teams may start "gaming the metrics," producing assurance-bearing epistemes or publications that are formally perfect but conceptually shallow or pragmatically useless.
2.  **Cognitive Overload & Rejection:** The framework becomes so dense, jargon-laden, and procedurally complex that its users—the very agents it is meant to serve—either burn out or abandon it in favor of simpler, albeit less rigorous, methods. The "Operating System for Thought" devolves into a bureaucratic machine for certification.

### E.12:3 - **Forces**

| Force | Tension |
| :--- | :--- |
| **Formal Rigor vs. Human Usability** | How to build a system that is both formally sound and cognitively accessible, without sacrificing one for the other. |
| **Intrinsic Complexity vs. Incidental Complexity**| How to distinguish the necessary cognitive load inherent in solving a difficult problem from the unnecessary friction imposed by a poorly designed framework. |
| **Means vs. Ends** | How to ensure that the production of high-quality epistemes or publications (the means) always serves the ultimate goal of enhancing an agent's cognitive capabilities (the end). |

### E.12:4 - **Solution**

FPF elevates **Didactic Primacy (Pillar P-2)** to a normative architectural principle, operationalized through two conceptual mechanisms designed to act as a permanent counterbalance to excessive formalism.

#### E.12:4.1 - The Principle of Didactic Primacy (Expanded Definition)

The primary purpose of the FPF is to enhance the cognitive capabilities (`U.Capability`/`Mastery`) of an Agent (`U.Agent`) in service of its Objectives (`U.Objective`). The creation of assurance-bearing epistemes or publications with high assurance levels and epistemic scores is a *means to that end, not the end itself*. Any architectural decision that increases formal rigor at the cost of clarity or usability must be explicitly justified by a demonstrable gain in the agent's ability to reason effectively.

#### E.12:4.2 - Mechanism 1: The Rationale Mandate

Every key assurance episteme or publication (such as a `U.AssuranceCase` or `Proof`) **MUST** contain a mandatory, human-readable **`rationale`** component.

*   **Nature:** The `rationale` is not a technical description but a narrative explanation.
*   **Content:** It **MUST** answer the question: *"How does achieving this level of formal assurance tangibly help the agent better understand the problem or make a more reliable decision?"*
*   **Purpose:** This mandate forces a moment of reflection, formally linking the act of formalization back to its pragmatic, cognitive purpose. An empty or perfunctory rationale indicates that the assurance work may be an exercise in formalism for its own sake.

> **Didactic Note for Managers: The "So What?" Test**
>
> The Rationale Mandate is FPF's built-in "So What?" test. When your team presents a complex, formally checked episteme or publication (`AssuranceLevel:L2`), the `rationale` is where they answer your fundamental question: "This is impressive, but *so what*? How does this help us ship a better product, make a smarter investment, or avoid a critical risk?" If the answer isn't clear and compelling in the `rationale`, the formal work may have been a waste of resources. It keeps your most brilliant minds focused on creating value, not just elegant proofs.

#### E.12:4.3 - Mechanism 2: The Human-Factor Loop (HF-Loop)**

To provide a continuous, self-correcting mechanism against cognitive overload, FPF introduces a conceptual feedback loop.

*   **Core Concept:** The HF-Loop is a formal method of inquiry designed to distinguish between the *essential complexity* of the problem being solved and the *incidental complexity* introduced by the FPF itself.
*   **Trigger Concept:** A review is triggered when the **subjective cognitive workload** associated with using the framework exceeds a conceptual threshold. This is not about performance metrics, but about the perceived mental effort required to use FPF's concepts and structures.
*   **Review Concept:** When triggered, a formal review is conducted by individuals in roles that specialize in human-centric perspectives, such as the **`Ethicist`** and **`UX Design Critic`**.
*   **Output Concept:** The review produces a set of proposed **conceptual simplifications** or **didactic improvements** to the framework's patterns. These are then submitted as formal change proposals (DRRs).

#### E.12:5 - **Conformance Checklist**

*   **CC-E12.1 (Rationale Mandate):** Every `U.AssuranceCase` or proof publication at `AssuranceLevel:L2` **MUST** contain a non-empty `rationale` component that satisfies the "So What?" test.
*   **CC-E12.2 (HF-Loop Trigger Condition):** Each pattern that defines a significant workflow **SHOULD** specify a conceptual condition for triggering an HF-Loop review, based on the principle of managing cognitive load.
*   **CC-E12.3 (HF-Loop Review Mandate):** If a trigger condition is met, a review involving the designated human-centric roles **MUST** be initiated. Its outcome **MUST** be a documented set of conceptual refinement proposals.
*   **CC-E12.4 (Didactic Primacy in DRRs):** Any DRR proposing a change to a normative pattern **MUST** include a section analyzing its impact on cognitive ergonomics and didactic clarity.

#### E.12:6 - **Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It (Conceptually) |
| :--- | :--- | :--- |
| **The "Ivory Tower" Framework** | The FPF specification becomes a beautiful but impenetrable fortress of abstract logic that no practicing engineer can actually use. | The **HF-Loop** provides a formal channel for user feedback to drive conceptual simplification. The roles of `UX Design Critic` and `Ethicist` are constitutionally empowered to challenge complexity that does not serve a clear purpose. |
| **The "Meaningless Rationale"** | The `rationale` field is filled with boilerplate text like "To increase assurance," without any real connection to the problem. | The "So What?" test is part of the review process for L2 assurance cases or proof publications. A perfunctory `rationale` is grounds for rejecting promotion of the assurance case or proof publication to L2, forcing the author to articulate the *real* value of their formal work. |
| **Glorifying Complexity** | A culture emerges where the most complex and difficult-to-understand models are considered the "best," regardless of their utility. | The core principle of **Cognitive Elegance (P-1)** and the mechanisms in this pattern create a constant pressure towards simplicity and clarity. The framework formally values understanding over mere complexity. |

#### E.12:7 - **Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Guards FPF's Core Mission:** This pattern acts as an "immune system," protecting the framework from devolving into sterile formalism and ensuring it remains a tool for enhancing thought. | **Introduces "Softer" Concepts:** Cognitive load and rationale quality are less quantifiable than formal proofs. *Mitigation:* FPF operationalizes them through a formal method. The HF-Loop is a structured inquiry, not an informal chat. |
| **Empowers Human-Centric Roles:** It gives the `Ethicist` and `UX Design Critic` roles a concrete, constitutional function in the evolution of the framework. | - |
| **Prevents User Burnout and Rejection:** The HF-Loop is an early warning system that detects when the framework is becoming too cumbersome, allowing for course correction before users become frustrated and abandon it. | - |
| **Creates a Self-Simplifying System:** The pattern creates a formal pressure that forces FPF to evolve towards greater clarity and usability, balancing the drive for formal rigor. | - |

#### E.12:8 - **Rationale**

This pattern operationalizes **Didactic Primacy (P-2)**, transforming it from a philosophical statement into an enforceable architectural Standard. The `Rationale Mandate` ensures that every act of formalization is tied to a clear purpose. The `Human-Factor Loop` ensures that the *cost* of using the framework is measured not just in resources, but in the most critical resource of all: the cognitive capacity of its users.

This pattern does not weaken the formal rigor established by other ADRs; it complements it. It guarantees that the powerful machinery of FPF is always directed towards a meaningful, human-relevant goal. It is the constitutional guarantee that FPF will remain, first and foremost, an "Operating System for Thought."

#### E.12:9 - **Relations**

*   **Implements:** Pillar `P-2 Didactic Primacy`.
*   **Complements:** `E.13 Pragmatic Utility & Value Alignment` (which focuses on the relevance of the *problem*, while this pattern focuses on the usability of the *framework*).
*   **Is constrained by:** The overall governance process (DRRs), which is the vehicle for implementing the conceptual simplifications proposed by the HF-Loop.

### E.12:End

## E.13 - Pragmatic Utility & Value Alignment

### E.13:1 - **Problem Frame**

The FPF provides a powerful engine for constructing formally correct and highly reliable holons. This power, however, introduces a subtle but profound risk: a team can create a perfectly verified and validated holon or episteme (`AssuranceLevel:L2`) that solves an irrelevant, misunderstood, or non-existent problem. The framework guarantees that the solution is *correct*, but it does not, by itself, guarantee that the solution is *useful*.

Furthermore, many of the most important system objectives—such as "safety," "usability," or "security"—are not directly measurable. They are assessed via **proxy characteristics** (e.g., "number of reported vulnerabilities" as a proxy for security). This practice is vulnerable to Goodhart's Law: when a proxy becomes the primary target, it often ceases to be a good measure of the original goal, as teams begin to optimize the proxy at the expense of the real objective.

### E.13:2 - **Problem**

Without a formal mechanism to keep the entire assurance apparatus tethered to real-world value, FPF risks enabling two critical failure modes:

1.  **Formalism for Formality's Sake:** Teams become preoccupied with achieving high epistemic scores, producing elegant but useless holons or epistemes. The framework is used to build beautiful solutions to the wrong problems.
2.  **Proxy-Metric Distortion (Goodhart's Law):** Teams successfully optimize for a chosen proxy characteristic, but in doing so, they diverge from—or even actively undermine—the true, often qualitative, `U.Objective` that the proxy was intended to represent. The system becomes technically successful but pragmatically a failure.

### E.13:3 - **Forces**

| Force | Tension |
| :--- | :--- |
| **Measurability vs. Meaning** | How to use quantitative, measurable proxies for progress without losing sight of the qualitative, often un-measurable, goals that truly matter. |
| **Abstraction vs. Application** | How to build and reason with abstract models without them becoming disconnected from any concrete, practical application. |
| **Incremental Progress vs. Global Value** | How to ensure that local optimizations and incremental improvements are genuinely contributing to the overall value proposition of the holon. |

### E.13:4 - **Solution**

FPF elevates **Pragmatic Utility (Pillar P-7)** to a normative architectural principle, operationalized through two mandatory conceptual mechanisms.

#### E.13:4.1 - The Principle of Pragmatic Utility (Expanded Definition)

Any holon or episteme created within FPF is an instrument for achieving a specific, pragmatic `U.Objective`. The value of that holon or episteme is determined solely by its **utility** in achieving that objective, not by its epistemic scores in isolation.

#### E.13:4.2 - Mechanism 1: The Proxy-Audit Loop

To formally manage the risk of Goodhart's Law, FPF introduces a conceptual feedback loop to periodically review the alignment between proxy characteristics and their intended goals.

*   **New Normative Relation:** A new relation, `isProxyFor: U.Characteristic → U.Objective`, is introduced. This relation **MUST** be used to explicitly declare when a measurable characteristic is serving as a proxy for an often qualitative `U.Objective`.
*   **Conceptual Audit Process:** Any characteristic marked with the `isProxyFor` relation is subject to a **periodic conceptual audit**.
*   **Review Roles:** This audit is conceptually performed by the individual(s) in the **`Strategist`** role. They are tasked with answering the question: *"Is optimizing for this proxy still reliably driving progress toward the actual `U.Objective` it represents, or have we observed a divergence?"*
*   **Output Concept:** If a divergence is identified, a high-priority `U.Method` for revising or replacing the proxy **MUST** be proposed.

> **Didactic Note for Managers: Are You Climbing the Right Mountain?**
>
> The Proxy-Audit Loop is your compass. Your team's dashboards might show all green—metrics are improving, targets are being hit. But the audit loop forces a crucial question: "Are these the *right* metrics?"
>
> Imagine you are trying to improve "customer satisfaction" (`U.Objective`). You choose "average call handle time" as a proxy metric. Your team successfully drives this number down. But the Proxy-Audit reveals that customer satisfaction is actually *decreasing* because agents are rushing and providing poor service to meet the time target. The loop forces you to recognize this divergence and find a better proxy (e.g., "first-call resolution rate"). It ensures your team is not just climbing fast, but climbing the right mountain.

#### E.13:4.3 - Mechanism 2: The Minimally Viable Example (MVE) Mandate

To enforce a pragmatic, value-first approach from the very beginning of a project, any new `U.System` or major system component **MUST** begin its development cycle with the creation of a **Minimally Viable Example (MVE)**.

*   **Definition:** An MVE is a simple, end-to-end, working instance of the holon that demonstrates the achievement of at least one core, user-facing objective, however trivial. It is the FPF equivalent of a "Hello, World" for a complex system.
*   **Assurance Requirement:** The MVE **MUST** achieve a minimum of **`AssuranceLevel:L1 (Substantiated)`**. This means the MVE cannot be a mere mock-up or a purely conceptual sketch; it must be supported by at least one piece of tangible evidence (e.g., a passing test case, a formal assertion), as defined in Pattern B.3.3.
*   **Stege transition Precedence:** The development of the full-scale holon cannot proceed to `AssuranceLevel:L2` until the MVE has been created and has met its L1 requirement.

### E.13:5 - **Conformance Checklist**

*   **CC-E13.1 (Proxy Declaration Mandate):** Any `U.Characteristic` used as a primary driver for an objective **MUST** be explicitly linked to that `U.Objective` via the `isProxyFor` relation.
*   **CC-E13.2 (Proxy-Audit Mandate):** A formal Proxy-Audit review **MUST** be conducted at regular conceptual intervals (e.g., before each major release). The outcome of this review **MUST** be a documented episteme.
*   **CC-E13.3 (MVE Mandate):** The development of any new `U.System` **MUST** be preceded by the creation of an MVE that satisfies the `AssuranceLevel:L1` requirement.
*   **CC-E13.4 (MVE Traceability):** The full-scale `U.System` **MUST** maintain a formal traceability link (`isEvolutionOf`) to its originating MVE.

### E.13:6 - **Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It (Conceptually) |
| :--- | :--- | :--- |
| **The "Perfectly Engineered Irrelevance"** | The team delivers a technically brilliant system that is formally verified and validated, but no one wants to use it because it doesn't solve a real problem. | **CC-E13.3** forces the team to build a working, end-to-end slice of value (the MVE) *first*. This grounds the entire project in a demonstrated solution to a real user need from day one. |
| **The "Metric Myopia"** | The team becomes obsessed with improving a specific KPI, ignoring clear indicators that this is not improving—and may even be harming—the overall user experience or business goal. | **CC-E13.2** mandates the Proxy-Audit Loop. This forces a periodic, strategic step-back, where the `Strategist` role is constitutionally required to ask, "Are we still measuring what matters?" |
| **The "Big Design Up Front" Trap** | The team spends months creating a vast, abstract, and highly detailed model of a system before ever building a single working component. | The **MVE Mandate** prevents this. It forces an iterative, pragmatic "build-to-learn" approach, ensuring that models are always grounded in a working reality. |

### E.13:7 - **Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Defense Against Goodhart's Law:** The Proxy-Audit Loop is a concrete, operational defense against the common failure mode of optimizing for the wrong thing. It forces regular, strategic reflection on the meaning of metrics. | **Introduces Strategic Overhead:** The Proxy-Audit Loop and the creation of an MVE require dedicated time for strategic thinking and early implementation. *Mitigation:* This is not an expense but a strategic investment. This upfront effort is designed to prevent the far greater cost of developing the wrong system over months or years. |
| **Ensures Value-Driven Development:** The MVE Mandate guarantees that all major development efforts are grounded in a demonstrated, working solution to a real problem, however small. This prevents teams from investing significant resources in abstract models that have no proven path to practical application. | - |
| **Prevents "Analysis Paralysis":** By requiring an early, working example, this principle encourages an iterative, pragmatic development style. It forces teams to build and learn, rather than over-specifying in a vacuum. | - |
| **Positions FPF as an Engineering Discipline:** This pattern firmly anchors FPF as a tool for practical engineering, not just theoretical modeling. | - |

### E.13:8 - **Rationale**

This pattern operationalizes **Pragmatic Utility (P-7)**. While Pattern E.12 protects the *agent* from the cognitive overload of the framework, this pattern protects the *problem* from being lost in a sea of formal abstraction. It provides the necessary constitutional guardrails to keep the powerful formal methods of FPF focused on delivering tangible, real-world value.

The **MVE Mandate** ensures that every journey starts with a destination in sight. The **Proxy-Audit Loop** ensures that the compass used on that journey remains pointed in the right direction. Together, these mechanisms guarantee that knowledge generated within FPF is not only formally correct and epistemically reliable, but also meaningful, useful, and aligned with its intended purpose.

### E.13:9 - **Relations**

*   **Implements:** Pillar `P-7 Pragmatic Utility`.
*   **Complements:** `E.12 Didactic Primacy & Cognitive Ergonomics`.
*   **Provides context for:** The definition of `U.Objective` and `U.Characteristic` by establishing a formal link between them.

### E.13:End


## E.14 - Human‑Centric Working‑Model

### E.14:1 - Intent

Establish a **single, human‑centric Working‑Model** that practitioners can read, discuss, and evolve **without exposure to formal machinery**.
Each statement **declares a justification stance** (`validationMode`) and, when assurance is sought, attaches **appropriate grounding** via one or more assurance shoulders — **Mapping**, **Logical**, **Constructive** — and **may additionally attach Empirical Validation** (evidence) as defined by the Trust & Assurance calculus. Empirical Validation can accompany any stance; it is **required** when the stance is *postulate*. Assurance shoulders sit **beneath** the Working‑Model and **never define its vocabulary**.

Put bluntly: *one model people work in; three assurance shoulders — plus empirical checks when the world is the judge.*

### E.14:2 - Problem & Context

Teams need **one shared Working‑Model** to make decisions at speed. Historically this surface either:

* **drifts into jargon**—different terms for one shared working-model value, slash‑labels, partial overlaps; or
* **calcifies into machinery**—too formal for day‑to‑day design and review.

Both failure modes create friction between two audiences:
(1) **working users** (engineers, programme managers, policy owners) who need a **small, stable surface**, and
(2) **assurance authors** (ontologists, methodologists, auditors) who need **proofs that the surface is sound**.

E.14 resolves the impasse by **separating concerns**:

* A **Working‑Model layer**: curated kinds and relations expressed in plain terms, governed by simple human rules.
* An **Assurance stack** beneath it - **Mapping**, **Logical**, **Constructive** - that carries the heavy arguments (concept alignment, relational semantics, generative traces) and **never leaks back** into the Working-Model narrative.

This pattern dovetails with the framework’s unification stance (**small Working‑Model surface, rigorous foundations**) and with our constructional mereology commitments (**sum/set/slice** provide extensional identity), while keeping the Kernel minimal and meta‑only.

### E.14:3 - Forces

1. **Cognitive economy vs. semantic precision.**
   Managers and engineers must navigate with a handful of names and relations; assurance authors must still certify that those names and relations **are unambiguous and extensional**.

2. **Speed of change vs. guarantees.**
   The Working‑Model must accommodate rapid iteration; the Assurance stack must **lag just enough** to check, without blocking practical progress.

3. **Parsimony vs. expressivity.**
   The Working‑Model should **not proliferate relation types or ad‑hoc categories**; fine‑grained distinctions live in the Assurance layers and are surfaced **only when they materially change a decision**.

4. **Downward grounding vs. upward contamination.**
   Grounding must always flow **down** (Working‑Model → Mapping → Logical → Constructive). No dependence **up** is allowed: proofs and traces never dictate wording or layout in the Working‑Model.

5. **Trans‑disciplinary unification vs. local dialects.**
   The Working‑Model must reconcile different disciplines’ habits **without erasing them**; Mapping captures dialects, while the Working‑Model exposes a **single usable choice**.

6. **Auditability vs. readability.**
   Every Working‑Model statement must be **auditable on request**, yet day‑to‑day views **hide the scaffolding** unless summoned.


### E.14:4 - Solution

#### E.14:4.1 - Human-Centric principles
##### E.14:4.1.1 - Recognition text and assurance text
Human-facing patterns also need governed-object stability across recognition text and assurance text. The working reader should not meet one object in the recognition text and a different ontological kind in the assurance text. If the pattern distinguishes a governed object, the interpretive or operational move applied to that object, and the wider review or work process around it, those distinctions should be made explicit rather than hidden behind stylistic noun-swapping.

Working-Model-first drafting therefore also means subject-domain-first drafting. If a pattern is meant to help with a real review, design, cultural, research, or operational problem, the recognition text should open from that problem-owning moment before internal taxonomy or package architecture. If a broader umbrella head and a narrower operative branch are both live, the pattern should state that stack plainly enough that a cold reader can tell what the umbrella names, what branch is current, what object is governed, what move is being carried, and what wider work remains outside.

Under `F.18` local-first naming, the canonical pair here is **recognition text** and **assurance text**.
The earlier provisional `...shell` wording is retired.
These names refer to two reading-order surfaces inside one pattern, not to new publication-surface kinds or owner kinds.

For human-facing canonical patterns, Working-Model-first discipline should appear in a two-surface reading order.
The **recognition text** is the working text that a cold practitioner, manager, or researcher should be able to understand first: what situation this pattern is for, what it buys, what it is not for, and what ordinary mistake it helps prevent.
The **assurance text** is the heavier text that carries declaration, object discipline, modeling lens, law, reroute conditions, and other review work.

The assurance text may justify, tighten, or audit the working text, but it must not silently replace or strengthen the recognition-text claim.
Where semio-heavy or transform-heavy patterns need a compact ontological account, the assurance text should make three things explicit:
- the ontic target or governed object;
- the modeling substrate or mathematical lens when one is load-bearing;
- the publication or working surface by which the claim is presented.

This is a reading-order rule rather than a demand that every reader read the assurance text first.
The point is to keep the human-facing Working-Model surface primary while preserving a recoverable, auditable second surface beneath it.
> **E.14‑P.1 – Working‑Model first, stance explicit.**  **
> Operate one **Working‑Model** for all human‑facing discussion. For **each** assertion, the author **SHALL declare** a justification stance (`validationMode`) and choose the **appropriate assurance shoulder(s)**: **Mapping** (term↔kind alignment via **Lang‑CHR** / D‑Projection), **Logical** (CT2R alias semantics, scope/constraints), **Constructive** (Γₘ generative trace), and **Empirical Validation** (evidence via `U.EvidenceRole` in a declared `U.BoundedContext`).

> **E.14‑P.2 – Downward‑only dependency.**
> Information **may** flow from the Working‑Model down into any Assurance layer; **no Assurance layer may impose vocabulary or shape back upward** into the Working‑Model.
>
> **E.14‑P.3 – Small surface, big proof.**
> The Working‑Model exposes a **minimal set** of names (L‑1/L‑2 registers) and **a compact family of relations** used in everyday reasoning; precision and completeness are **proved below**.

> **E.14‑P.4 – Human registers first.**
> Terms in the Working‑Model are deliberately curated for **human legibility** (register‑badged, synonym‑aware). Synonym capture and language variance belong to Mapping; **only the chosen canonical label appears on the Working‑Model surface**.

> **E.14‑P.5 – Justification modes are explicit.**
> Each Working‑Model relation **declares** `validationMode ∈ {axiomatic, inferential, postulate}`.
