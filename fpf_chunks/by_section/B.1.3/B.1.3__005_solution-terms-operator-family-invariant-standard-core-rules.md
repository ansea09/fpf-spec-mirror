---
chunk_kind: "child"
pattern_id: "B.1.3"
pattern_title: "Γ_epist - Knowledge‑Specific Aggregation"
section_id: "B.1.3:4"
section_title: "Solution — Terms, operator family, invariant Standard, core rules"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.3/B.1.3__005_solution-terms-operator-family-invariant-standard-core-rules.md"
commit_sha: "f4bad21274b54b57071afb2210a8bdb9f61a1c95"
heading_path:
  - "B.1.3 — Γ_epist - Knowledge‑Specific Aggregation"
  - "B.1.3:4 — Solution — Terms, operator family, invariant Standard, core rules"
line_start: 37028
line_end: 37143
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.13"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.15.PROD"
  - "A.6.1"
  - "B.1"
  - "B.1.1"
  - "B.1.4"
  - "B.1.6"
  - "B.2"
  - "B.3"
  - "C.11"
  - "C.19.2"
  - "C.2"
  - "C.2.1"
  - "E.17"
  - "E.24.PUB"
  - "F.6"
  - "F.9"
  - "U.Work"
keywords:
  - "KD-CAL"
  - "epistemic"
  - "knowledge aggregation"
  - "provenance"
  - "trust"
---

### B.1.3:4 - Solution — **Terms, operator family, invariant Standard, core rules**

#### B.1.3:4.1 - Terms (didactic recap)

* **U.Episteme** — a claim-bearing knowledge holon. C.2.1 identifies it through the participant-determined `EpistemeConstitutionRelation` over `<claim content, exact EntityOfConcern, effective ReferenceScheme>`. `ClaimGraphSlot`, `EntityOfConcernSlot`, and `ReferenceSchemeSlot` name participant meanings only inside that relation's reusable declaration; they are not internal slots of the episteme. Empirical grounding uses the separate `EpistemeEmpiricalGroundingRelation`, while text, code, figures, datasets, SCR/RSCR references, publication forms, and presentation carriers remain separately governed provenance, representation, publication, or carrier material.
* **Evidence/Provenance Graph** — edges like **evidences**, **derivesFrom**, **usesMethod**, **isMeasuredBy** with anchors (A.10).
* **Semantic mapping** — the exact correspondence rule used by this composition. When it crosses semantic contexts, identify the source and receiving F.17 `SchemeSenseCell` values and an obtaining F.9 `Bridge`; keep the proposed use, direction, use-specific rule, permitted loss, reliance, and **CL** evidence summary separate. F.9 does not require CL for every Bridge; B.1.3 requires the summary for a mapping used in its support account. CL alone neither grants the use nor supplies a numerical penalty.
* **SCR** — a `U.SCR` that lists all symbol carriers included in the aggregate; **never dropped**.
* **Semantic context** — Plain shorthand for the local interpretation basis recovered from one exact F.17 `SchemeSenseCell` as `<ReferenceScheme, LocalSenseClaim>`. It is not another operation argument or entity. Crossing between two such contexts uses F.9 and the separate bounded-use and reliance steps above.

> **Didactic reminders.**
> • Knowledge does **not** act. A researcher or engineer may use it while performing Work. Recover the exact System and Work only when the receiving claim consumes them; use A.12 only when the acting-side distinction is itself current.
> • A collection's own rule establishes which epistemes belong to it; belonging is not a semantic argument link and does not by itself make a holon. Use **ConstituentOf** for logical or evidential composition.
> • `PhaseOf` is only a proper temporal restriction of one unchanged episteme. Changed C.2.1 discriminators identify another episteme; test `EpistemeEditionRelation` separately. Use MHT only for a remaining whole-reidentification question, not as a substitute for C.2.1 identity.

#### B.1.3:4.2 - The operator family (companion flavours)

To keep **design vs run** clean (A.15), Γ_epist has two companion flavours that share the same algebra but answer different semantic questions. Their declarations contain only the values on which the result depends. A performer, local system-role kind, or assignment is therefore not an operator argument: the same fold can be specified before staffing and can be applied in Work performed by different Systems without changing its result semantics.

When one particular operation application matters, use A.6.1 for that application and its argument and result bindings. A practitioner sentence may still say "the engineer compiled the guidance". If no particular dated `U.Work` claim is current, that ordinary sentence needs no classification or assignment apparatus. If one is current, recover every actual performer System's A.13 core and independently admit the Work under A.15.1 from its performance history, enacted Method, temporal extent, and containing System. Add F.6 afterward only when precise assignment-bound attribution is current. A short B.1.3 projection may omit an assignment identifier unused by its receiver only when every relation it consumes remains recoverable. An operation result binding says which value the application returned; it establishes neither production nor first existence of that value, publication, release, acceptance, nor a carrier. Open A.15.PROD or the publication patterns only when one of those separate questions is current.

**Synthesis (design-time semantic fold).** Compose exact input epistemes into a draft aggregate.

```
Γ_epist^synth : ( D_know : DependencyGraph< U.Episteme > ) → U.Episteme
```

* **Domain.** `D_know` designates exact source epistemes and the governed **ConstituentOf**, **UsageOf**, **ReferenceTo**, **evidences**, **derivesFrom**, and collection-specific belongs-to relations that obtain among them, together with the mappings used by the fold. The graph represents those objects and relations; it does not make them obtain.
* **Result.** One synthesized episteme whose claim content, exact EntityOfConcern, and effective reference scheme satisfy C.2.1. Its ClaimGraph integrates the retained content; provenance and SCR keep contributing sources and carriers traceable. State its formal basis, scope, and supported conclusion with limitations. Calculate an aggregate R only where B.3 and C.2.2 establish the input meanings, scales, and dependency model. Otherwise keep support separate and return a bounded reasoned synthesis. Neither a higher formality level nor an axiomatic mode requires an invented numerical score or an irrelevant empirical study.

**Compilation (target-scheme fold).** Map one synthesized episteme into one exact target reference scheme.

```
Γ_epist^compile : ( E_synth    : U.Episteme,
                    TargetScheme : U.ReferenceScheme ) → U.Episteme
```

* **Domain.** One synthesized episteme and the exact target reference scheme used to read the compiled claims—for example, the scheme used by a journal, standard, or program specification. For every meaning that crosses semantic contexts, the fold also relies on exact source and receiving `SchemeSenseCell` values, an obtaining F.9 Bridge, and a separately stated bounded-use claim; any relied-on use must pass A.10 or B.3.
* **Result.** One compiled, target-scheme episteme with explicit mapping and loss information and a C.2.1 identity determined by its claim content, exact EntityOfConcern, and effective reference scheme. The result is not thereby a publication, release, carrier, or accepted artifact.

**Relationship to Γ_ctx / Γ_time.**
If the knowledge fold explicitly depends on **argument order** (for example, a derivation), the internal fold uses **Γ_ctx** for the sequence. If a **temporal storyline** matters, first identify each exact episteme and any obtaining C.2.1 edition relation; then use B.1.4/**Γ_time** to aggregate only the recovered temporal restrictions, relation order, or applicability windows required by the use. Γ_epist composes exact selected episteme inputs, not a label-defined current slice. If the result changes claim content, EntityOfConcern, or effective reference scheme, C.2.1 identifies another episteme. Use B.2 only when exact construction facts leave a separate existing-whole versus candidate-new-whole question.

#### B.1.3:4.3 - Invariant Standard (how the Quintet applies)

* **IDEM (Idempotence).** Folding a single episteme without a change of claim or scheme returns itself. Repeating the same source or data creates no additional evidence or accidental assurance upgrade.
* **COMM/LOC (Local commutativity / locality).** Reordering genuinely independent contributions does not change a result under its declared model. A derivation or other order-dependent argument uses **Γ_ctx**; source order does not establish statistical independence.
* **WLNK (Weakest-link bound).** An unsupported indispensable premise limits the conclusion that needs it. A numerical minimum is appropriate only when the named quantity and dependency model justify a bottleneck or lower-bound interpretation. WLNK does not impose minimum over every cited source or every argument.
* **MONO (Monotonicity).** A monotonicity claim names the support change and the model under which it holds. Duplicate data, a contrary result, a changed target population, or the failure of a necessary assumption is not simply “more support”.

**No universal reliability fold.** B.3 governs the quantity, scale, dependency assumptions, and calculation. For two necessary independent conditions with probabilities 0.9 each, the conjunction has probability 0.81, not 0.9. Without independence, use a warranted conditional model or leave that joint probability unresolved. A minimum or maximum can be useful under its own declared meaning; monotonicity and boundedness alone do not establish that meaning.

**Formality and calculation.** Ordinal comparisons remain ordinal. A quantitative calculation requires commensurate inputs and a model for the proposed operation, including any mapping loss; a table of numbers alone is insufficient. Formal derivations state their logic and assumptions, and constructive derivations their proof basis. When no common aggregate is justified, a qualitative synthesis can still give a complete, useful answer to a bounded question.

#### B.1.3:4.4 - Core rules for epistemic aggregation (design‑time synthesis)

When computing **Γ_epist^synth(D_know)**:

**1. Provenance preservation.**
   The **provenance/evidence graph** is **unioned with de‑duplication**; every claim in the aggregate remains traceable to its sources and methods. No source, method, or dataset that supports a retained claim may be dropped.

**2. SCR construction.**
   Build a **U.SCR** that lists all symbol carriers (texts, code, figures, datasets) that materially participate in the aggregate. Provenance nodes must be mappable to SCR entries.

**3. Object alignment.**
   Identify the result's one exact **EntityOfConcern**. Reuse the same already identified entity when the inputs concern it. A governed least common ancestor in a domain taxonomy may support that identification, but the calculation does not create the entity. If the claim requires a collection, relation occurrence, or other joint subject, identify that entity under its direct pattern and show that its identity rule obtains. A list, dependency graph, shared label, or mapping cannot create a joint subject; if none is governed, stop with the missing composition governor instead of inventing a generic composite entity. Record the semantic mappings and their **CL** evidence summaries without silently merging homonyms.

**4. Recover the support relation before combining.**
   For the exact claim and scope, distinguish:

   * **Indispensable premises:** the conclusion requires each named premise. A missing or defeated premise blocks that inference, not every narrower conclusion.
   * **Alternative sufficient arguments:** each actually sufficient argument can support the conclusion; expose shared premises, datasets, assumptions, and failure causes. Different argument names do not prove independence.
   * **Complementary evidence:** a source may constrain a rival explanation, magnitude, uncertainty, or applicability without being a necessary premise. A limited additional study need not lower the existing support.
   * **Different scope slices:** retain their populations, outcomes, conditions, and time extents separately unless an explicit transport or combination rule supports the joint claim.
   * **Counterevidence:** retain credible results that conflict with the proposed conclusion. Weak support, absence of decisive support, an uninformative study, and evidence against a claim have different consequences.

   Deduplicate actual evidence, not just citations. Account for overlapping data and shared biases before treating agreement as additional corroboration. State what each live limitation changes in the resulting claim.

**5. Compose under the receiving model, or synthesize without a score.**
   Keep F ordinal under C.2.3; any minimum for essential formal constituents concerns that formality claim, not R. Form G through the applicable C.2.2/A.2.6 scope rules; adding a study does not by itself extend applicability. For R, name the target quantity, compatible scales, dependencies, and warranted operation under B.3/C.2.2. This can justify a bottleneck minimum, a sufficient-argument choice, a probabilistic calculation, or a statistical synthesis; none is the universal default.

   For a relied-on mapping, retain its CL summary and the actual limitation. A numerical loss function needs a receiving model that establishes its meaning, units, calibration or derivation, and assumptions. An ordinal CL rank, a monotone penalty table, or clipping to [0,1] supplies none of these. If no such calculation is justified, retain the separate support and mapping limitations in a reasoned synthesis; no penalty table or new study is required merely to return that result. A receiving assurance threshold applies only to the quantity and use for which it was justified.

**6. Conflict detection and disposition.**
   Detect contradictions, including overlapping-scope `p` and `¬p`. Resolve a scope or interpretation difference only when the source facts establish it; do not explain away a credible contrary result by an invented subgroup story. Otherwise narrow, qualify, or withhold the affected conclusion and retain explicit conflict edges. A numerical synthesis may represent disagreement only under its justified model, not conceal it. Open B.2 only if exact construction facts leave a separate whole-reidentification question after the existing-whole explanation check.

**7. Handling axiomatic and world-facing support.**
   Retain each episteme's declared mode and actual support:

* For an **axiomatic** input, empirical R may be N/A. Keep the proof, its conclusion under the stated axioms, and its formal validity; `line=formal` is a useful tag, not a conversion rule. **Do not set R to F.** An ordinal F-derived proxy describes only its declared ordinal meaning. Any value proposed for an R calculation needs a receiving model establishing meaning, scale, conversion, and assumptions; rescaling F into [0,1] is insufficient.
* For a **postulative** input, retain its actual warrant and empirical or other support as applicable. Apply a B.3.4 currentness or decay policy only to the support whose use consumes that policy; changing the mode creates neither evidence nor a conversion model.
* The aggregate declares its mode. If all its operative inputs are axiomatic, it is axiomatic; if an operative input is postulative, it is postulative. Keep any formal subclaim separately usable. A proof about a model supports a claim about a real system only with the needed model-to-world assumptions; evidence violating those assumptions remains visible.
* **Constructive note.** Under **F-constructive**, equivalence claims use **isomorphism/equivalence** in the chosen UF library; **CL=2** means proof-reconstructed alignment, not mere model-theoretic appeal.

**8. Order-aware arguments (optional).**
   If the argument requires premise ordering, embed a **Γ\_ctx** fold inside Γ\_epist; record the **OrderSpec** for reproducibility (NC‑1..3).
   **Gating:** OrderSpec is **recommended** at **M‑1** and **required** at **M‑2/F**.  # [M‑1→F]

**9. No costs here.**
   Any compute/collection effort is **Γ\_work**; attach references but do not mix costs into epistemic aggregation.

#### B.1.3:4.5 - Core rules for target-scheme compilation

When computing **Γ_epist^compile(E_synth, TargetScheme)**:

**1. Reference-scheme bindings.** # [M-1+]
   Map every operative concept, unit, and claim into **TargetScheme** and record the exact mapping and its **CL** evidence summary. For a meaning that crosses semantic contexts, name the source and receiving `SchemeSenseCell` values, the obtaining F.9 Bridge, the proposed use, direction, use-specific rule, and permitted loss; establish reliance separately. C.2.1 identifies the compiled episteme from its resulting claims, exact EntityOfConcern, and target scheme. A changed identity discriminator identifies another episteme; it does not by itself open a whole-reidentification question.

**2. Re-express the assurance basis.**
   Re-express F, G, and the support account in **TargetScheme**. Preserve the formal conclusion and empirical limitations separately. Recalculate R or a mapping loss only if the target use has the required meanings, scales, and model under B.3/C.2.2; a change of vocabulary or increased formality is not additional warrant. Without a justified aggregate, carry the separate support and bounded synthesis. A quantitative or formal application proves the calculations or derivations it actually claims, not a fictitious tuple imposed by its mode.

**3. Compilation trace.**
   Produce the compiled episteme's SCR and the carrier hashes needed to reconstruct this application; at **L2** require independent re-hash verification. This trace establishes neither publication nor release. # [M-1/L2]
**4. Order/time hooks.**
   If the compiled episteme includes an internal derivation, carry the **OrderSpec**. If it selects knowledge for a time-bounded use, name the exact C.2.1 episteme identity and link to the already recovered proper temporal restriction, edition relation order, applicability window, or B.1.4/**Γ_time** aggregation actually used.

