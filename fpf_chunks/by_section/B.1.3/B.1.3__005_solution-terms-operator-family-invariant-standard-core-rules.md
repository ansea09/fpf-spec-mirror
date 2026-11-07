---
chunk_kind: "child"
pattern_id: "B.1.3"
pattern_title: "Knowledge Aggregation (Γ_epist): Synthesis and Target-Scheme Compilation"
section_id: "B.1.3:4"
section_title: "Solution — Terms, operator family, invariant Standard, core rules"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.3/B.1.3__005_solution-terms-operator-family-invariant-standard-core-rules.md"
commit_sha: "870fb0c2a5dcfe1e0165a111fdf2cf8659c85a54"
heading_path:
  - "B.1.3 — Knowledge Aggregation (Γ_epist): Synthesis and Target-Scheme Compilation"
  - "B.1.3:4 — Solution — Terms, operator family, invariant Standard, core rules"
line_start: 41679
line_end: 41798
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
  - "A.7"
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
---

### B.1.3:4 - Solution — **Terms, operator family, invariant Standard, core rules**

#### B.1.3:4.1 - Terms (didactic recap)

* **U.Episteme** — a claim-bearing knowledge holon. C.2.1 identifies it through the participant-determined `EpistemeConstitutionRelation` over `<claim content, exact EntityOfConcern, effective ReferenceScheme>`. These three participant identities determine its identity. Claim content and ReferenceScheme are epistemic constituents; EntityOfConcern is the independently governed subject related through aboutness. Empirical grounding uses the separate `EpistemeEmpiricalGroundingRelation`, while text, code, figures, datasets, SCR/RSCR references, publication forms, and presentation carriers remain separately governed provenance, representation, publication, or carrier material.
* **Constitution participants and typed positions.** When the receiving use needs a reusable designation of the EntityOfConcern, C.2.1:4.2.1 supplies `EntityOfConcernSlot` with `ValueKind=U.Entity` and `refMode=U.EntityRef`. It is a participant meaning in the relation declaration, not an internal slot of the episteme. Exact claim content and effective interpretation rules remain necessary constituents without being additional SlotKinds. A receiving relation declaration that needs `ClaimGraphSlot` or `ReferenceSchemeSlot` must supply each independently governed ValueKind and complete A.6.5 SlotSpec; the constituent name alone provides neither.
* **Evidence/Provenance Graph** — an A.10 descriptive account whose edges cite independently established direct support, source, measurement or use relations. Display labels such as `evidences` do not create generic relation kinds.
* **Semantic mapping** — the exact correspondence rule used by this composition. When it crosses semantic contexts, identify the source and receiving F.17 `SchemeSenseCell` values and an obtaining F.9 `Bridge`; keep the proposed use, direction, use-specific rule, permitted loss, and reliance separate. Retain a **CL** summary when the receiving rule uses one, including the applicable KD-CAL substitution or cross-notation reasoning rule in C.2. CL alone neither grants the use nor supplies a numerical penalty.
* **Source and carrier record (SCR)** — a recoverable account of which sources and concrete carriers materially contributed to one identified synthesis or compilation result, and what each contributed. Keep the source versions, methods and carrier information needed to reconstruct that aggregation. The account may be expressed as prose, a table or a graph. An account meeting C.2.1's episteme criterion is one `U.Episteme`: its claim content records those participation facts, its EntityOfConcern is the aggregate, and its effective ReferenceScheme determines their interpretation. Apply C.2.1 to its identity: a corrected participation claim changes the episteme, while another layout can express the same claims. Working notes can precede that completed account.
* **Semantic context** — Plain shorthand for the local interpretation basis recovered from one exact F.17 `SchemeSenseCell` as `<ReferenceScheme, LocalSenseClaim>`. It is not another operation argument or entity. Crossing between two such contexts uses F.9 and the separate bounded-use and reliance steps above.

> **Didactic reminders.**
> • A collection's own rule establishes which epistemes belong to it; belonging is not a semantic argument link and does not by itself make a holon. Use **ConstituentOf** for logical or evidential composition.

#### B.1.3:4.2 - The operator family (companion flavours)

Γ_epist has two companion operations with different semantic questions and the composition conditions below. Their declarations contain the values on which the result depends. A performer, local system-role kind, or assignment is not an operator argument: the fold can be specified before staffing and applied in Work performed by different Systems without changing its result semantics. This preserves the design/run distinction under A.15.

When one particular operation application matters, use A.6.1 for that application and its argument and result bindings. A practitioner sentence may still say "the engineer compiled the guidance". If no particular dated `U.Work` claim is current, that ordinary sentence needs no classification or assignment apparatus. If one is current, recover every actual performer System's A.13 core and independently admit the Work under A.15.1 from its performance history, enacted Method, temporal extent, and containing System. Add F.6 afterward only when precise assignment-bound attribution is current. A short B.1.3 projection may omit an assignment identifier unused by its receiver only when every relation it consumes remains recoverable. An operation result binding says which value the application returned; it establishes neither production nor first existence of that value, publication, release, acceptance, nor a carrier. Open A.15.PROD or the publication patterns only when one of those separate questions is current.

**Synthesis (design-time semantic fold).** Compose exact input epistemes into a draft aggregate. The displayed signature is a family template. A concrete operation declaration states which receiving claim, use and composition rules are fixed and how varying values are supplied; it determines the result's claim content, EntityOfConcern and interpretation basis from its admitted inputs. Its domain is restricted by the applicable conditions in :4.4. Ordinary bounded synthesis may state this basis in its explanation without a separate operation declaration.

```
Γ_epist^synth : ( D_know : DependencyGraph< U.Episteme > ) ⇀ U.Episteme
```

* **Domain.** `D_know` designates exact source epistemes and the relations used in their composition: governed **ConstituentOf**, **UsageOf** and **ReferenceTo** relations; support and derivation relations under their direct predicates; and collection belonging under each collection's own rule. It also identifies the mappings used by the fold. Those relations must independently obtain; graph labels do not establish them.
* **Result.** One synthesized episteme whose claim content, exact EntityOfConcern, and effective reference scheme satisfy C.2.1. Its ClaimGraph integrates the retained content. Keep material source contributions recoverable, adding the SCR when the receiving use requires reconstruction of the particular aggregation. State its formal basis, scope, and supported conclusion with limitations. Calculate an aggregate R only where B.3 and C.2.2 establish the input meanings, scales, and dependency model. Otherwise keep support separate and return a bounded reasoned synthesis. Neither a higher formality level nor an axiomatic mode requires an invented numerical score or an irrelevant empirical study.

**Compilation (target-scheme fold).** Map one synthesized episteme into one exact target reference scheme. Recover the operative target rules through C.2.1:4.1.1 and fix them as `S` for this compilation operation. A journal's name or the document describing its rules does not by itself identify those rules. Compare S with the source scheme by its interpreted rules, their domains and dependencies under C.2.1:4.1.1. A different spelling or encoding can express the same rules. A changed semantic rule or domain identifies a different target scheme even when a selected answer agrees; this compilation then identifies the result with that target S.

```text
Γ_epist^{compile,S} : ( E_synth : U.Episteme ) ⇀ U.Episteme
```

`S` is fixed in the operation's declaration. The declaration states how input claims are mapped into `S` and the conditions for admitting the result. The partial arrow means that an identified input episteme alone does not establish an admissible compilation: the mapping, preservation, and reliance conditions in :4.5 must hold. An unresolved interpretation or required mapping leaves the affected compilation unresolved.

* **Domain.** One synthesized episteme whose retained claims can be interpreted in `S` under the declared mapping. For every meaning that crosses semantic contexts, the fold also relies on exact source and receiving `SchemeSenseCell` values, an obtaining F.9 Bridge, and a separately stated bounded-use claim. Reliance on that claim requires the ordinary A.10 evidence-provenance path and same-use `RelianceDisposition` under F.9:4.2: `pass` supports the named use; `degrade` supports only its named narrower use. An actual named assurance claim additionally requires a B.3 result supporting that same bounded assurance use.
* **Result.** One compiled episteme with explicit mapping and loss information and a C.2.1 identity determined by its claim content, exact EntityOfConcern, and effective target scheme `S`. The result is not thereby a publication, release, carrier, or accepted artifact.

**When the target must be replaceable.** A receiving use that selects or substitutes a target scheme within one operation needs an independently governed range for that argument. Use C.3 to identify the candidate rules, their identity criterion, and the membership condition required by that use; then declare the argument and its binding conditions under A.6.1. Range membership does not establish that the chosen scheme can express this input's claims or that a proposed mapping preserves the required meaning. Those application conditions still need :4.5. E.24.UK:4.2c supplies no admitted general `U.ReferenceScheme` range. Fixing one `S` permits the compilation above without claiming that general range; changing the fixed rules requires reconsidering the declaration, mappings, and affected results.

**Relationship to Γ_ctx / Γ_time.**
If the knowledge fold explicitly depends on **argument order** (for example, a derivation), the internal fold uses **Γ_ctx** for the sequence. If a **temporal storyline** matters, first identify each exact episteme and any obtaining C.2.1 edition relation; then use B.1.4/**Γ_time** to aggregate only the recovered temporal restrictions, relation order, or applicability windows required by the use. Γ_epist composes exact selected episteme inputs, not a label-defined current slice. If the result changes claim content, EntityOfConcern, or effective reference scheme, C.2.1 identifies another episteme. Use B.2 only when exact construction facts leave a separate existing-whole versus candidate-new-whole question.

#### B.1.3:4.3 - Invariant Standard (how the Quintet applies)

* **IDEM (singleton identity and source-repetition discipline).** Folding a single episteme while preserving its complete claim content, exact EntityOfConcern and effective ReferenceScheme returns that same episteme. Repeating the same source or data creates no additional evidence or accidental assurance upgrade.
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
   Keep a recoverable account of every material source contribution, method, mapping and dependency. Include concrete carriers and source versions where their identity, currentness, integrity or actual participation matters to the named use. When that use requires reconstruction of the particular aggregation, retain the SCR and the information needed for that reconstruction.

   Use the developing record to expose a missing source, shared data or an unsupported inference. Keep contrary contributions visible under rule 4. Pass the recoverable account with the aggregate or through resolvable references. When a source changes, reconsider the retained claims that actually depended on it.

**3. Object alignment.**
   Identify the result's one exact **EntityOfConcern**. Reuse the same already identified entity when the inputs concern it. A governed least common ancestor in a domain taxonomy may support that identification, but the calculation does not create the entity. If the claim requires a collection, relation occurrence, or other joint subject, identify that entity under its direct pattern and show that its identity rule obtains. A list, dependency graph, shared label, or mapping cannot create a joint subject; if none is governed, stop with the missing composition governor instead of inventing a generic composite entity. Record the semantic mappings, their actual limitations, and any **CL** summary required by the receiving rule, without silently merging homonyms.

**4. Recover the support relation before combining.**
   For the exact claim and scope, distinguish:

   * **Indispensable premises:** the conclusion requires each named premise. A missing or defeated premise blocks that inference, not every narrower conclusion.
   * **Alternative sufficient arguments:** each actually sufficient argument can support the conclusion; expose shared premises, datasets, assumptions, and failure causes. Different argument names do not prove independence.
   * **Complementary evidence:** a source may constrain a rival explanation, magnitude, uncertainty, or applicability without being a necessary premise. A limited additional study need not lower the existing support.
   * **Different scope slices:** retain their populations, outcomes, conditions, and time extents separately unless an explicit transport or combination rule supports the joint claim.
   * **Counterevidence:** retain credible results that conflict with the proposed conclusion. Weak support, absence of decisive support, an uninformative study, and evidence against a claim have different consequences.

   Deduplicate actual evidence, not just citations. Account for overlapping data and shared biases before treating agreement as additional corroboration. State what each live limitation changes in the resulting claim.

**5. Compose under the receiving model, or synthesize without a score.**
   Assess F under C.2.3 from the expression properties of essential constituents and their connecting inferences. A minimum applies only under a justified composition rule on a shared local ordered scale; it concerns that expression assessment, not R. Form G through the applicable C.2.2/A.2.6 scope rules; adding a study does not by itself extend applicability. For R, name the target quantity, compatible scales, dependencies, and warranted operation under B.3/C.2.2. This can justify a bottleneck minimum, a sufficient-argument choice, a probabilistic calculation, or a statistical synthesis; none is the universal default.

   For a relied-on mapping, retain its actual use limitations and any CL summary consumed by the receiving rule. A numerical loss function needs a receiving model that establishes its meaning, units, calibration or derivation, and assumptions. An ordinal CL rank, a monotone penalty table, or clipping to [0,1] supplies none of these. If no such calculation is justified, retain the separate support and mapping limitations in a reasoned synthesis; no penalty table or new study is required merely to return that result. A receiving assurance threshold applies only to the quantity and use for which it was justified.

**6. Conflict detection and disposition.**
   Detect contradictions, including overlapping-scope `p` and `¬p`. Resolve a scope or interpretation difference only when the source facts establish it; do not explain away a credible contrary result by an invented subgroup story. Otherwise narrow, qualify, or withhold the affected conclusion and retain explicit conflict edges. A numerical synthesis may represent disagreement only under its justified model, not conceal it. Open B.2 only if exact construction facts leave a separate whole-reidentification question after the existing-whole explanation check.

**7. Handling axiomatic and world-facing support.**
   Retain each episteme's actual support and any mode declaration needed by the receiving use:

* For an **axiomatic** input, empirical R may be N/A. Keep the proof, its conclusion under the stated axioms, and its formal validity; `line=formal` is a useful tag, not a conversion rule. **Do not set R to F.** A local ordinal formality summary describes only its declared ordinal meaning. Any value proposed for an R calculation needs a receiving model establishing meaning, scale, conversion, and assumptions; rescaling a formality rank into [0,1] is insufficient.
* For a **postulative** input, retain its actual warrant and empirical or other support as applicable. Apply a B.3.4 currentness or decay policy only to the support whose use consumes that policy; changing the mode creates neither evidence nor a conversion model.
* When the receiving use requires a mode classification, apply its rule to the support operative in the claimed conclusion. Under the axiomatic/postulative distinction, if all operative inputs are axiomatic, the conclusion is axiomatic; an operative postulative input makes that conclusion postulative. Keep any formal subclaim separately usable. A proof about a model supports a claim about a real system only with the needed model-to-world assumptions; evidence violating those assumptions remains visible.
* **Constructive derivations.** State the chosen proof basis and the correspondence needed by the conclusion. An induction proof may use its stated non-UF foundation. A UF-based equivalence claim supplies the required equivalence or isomorphism witness and the structure that the receiving theorem needs preserved. A lossy mapping cannot transport a theorem that depends on an erased distinction. If the required proof basis or correspondence is unavailable, leave that inference unresolved while retaining independently supported conclusions. A CL summary describes mapping evidence; it establishes neither equivalence nor theorem transport.

**8. Order-aware arguments (optional).**
   If the conclusion depends on premise or derivation order, identify the ordered relations and positions, declare the **OrderSpec**, and retain the branch, join and independence conditions needed by the argument. Use B.1.4:4 to check the bounded aggregation and its determinacy under those conditions.


**9. Account for resource use separately.**
   When the receiving question requires a resource account for computation or collection, use B.1.6/**Γ\_work** and reference that account separately from the epistemic support.

#### B.1.3:4.5 - Core rules for target-scheme compilation

When computing **Γ_epist^{compile,S}(E_synth)**, retain the fixed rules `S` and the mapping used for this input:

**1. Reference-scheme bindings.**
   Map every operative concept, unit, and claim into **S** and record the exact mapping, its actual limitations and any **CL** summary required by the receiving rule. For a meaning that crosses semantic contexts, name the source and receiving `SchemeSenseCell` values, the obtaining F.9 Bridge, the proposed use, direction, use-specific rule, and permitted loss; establish reliance separately. C.2.1 identifies the compiled episteme from its resulting claims, exact EntityOfConcern, and target scheme. A changed identity discriminator identifies another episteme; it does not by itself open a whole-reidentification question.

**2. Re-express the assurance basis.**
   Re-express F, G, and the support account in **S**. Preserve the formal conclusion and empirical limitations separately. Recalculate R or a mapping loss only if the target use has the required meanings, scales, and model under B.3/C.2.2; a change of vocabulary or increased formality is not additional warrant. Without a justified aggregate, carry the separate support and bounded synthesis. A quantitative or formal result needs grounds for its claimed calculations or derivations; its mode alone requires no additional numerical tuple.

**3. Compilation trace.**
   Carry the recoverable source-contribution account with the compiled episteme or through resolvable references. Add carrier hashes or other reconstruction details when the receiving claim requires carrier integrity or replay of the particular compilation. Require independent re-hash verification when the receiving claim needs independent carrier-integrity evidence under B.3 or an applicable B.3.3 assurance profile. A level label alone does not select that check. The trace establishes neither publication nor release.
**4. Order/time hooks.**
   If the compiled conclusion depends on derivational order, carry the ordered relations, positions and **OrderSpec** required by that use. If it selects knowledge for a time-bounded use, name the exact C.2.1 episteme identity and link to the already recovered proper temporal restriction, edition relation order, applicability window, or B.1.4/**Γ_time** aggregation actually used.

