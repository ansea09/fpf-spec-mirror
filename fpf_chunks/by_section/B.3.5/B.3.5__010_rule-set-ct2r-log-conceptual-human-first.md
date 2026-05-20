---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:9"
section_title: "Rule‑set — CT2R‑LOG (conceptual, human‑first)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__010_rule-set-ct2r-log-conceptual-human-first.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:9 — Rule‑set — CT2R‑LOG (conceptual, human‑first)"
line_start: 31290
line_end: 31382
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
  - "CT2R"
  - "Compose-CAL"
  - "assurance layer"
  - "constructive trace"
  - "grounding"
  - "working model"
---

### B.3.5:9 - Rule‑set — CT2R‑LOG (conceptual, human‑first)

**Intent (one line).** Make **Working‑Model** relations the canonical interface for authors, while providing a **clean, optional bridge** to formal assurance by way of *aliasing* and *grounding* semantics.

#### B.3.5:9.1 - Vocabulary & Roles (what the words mean in this pattern)

* **Working‑Model relation.** A human‑oriented statement an engineer would naturally write, using U.Type relations such as `ut:ComponentOf`, `ut:PortionOf`, `ut:AspectOf`, `ut:MemberOf`. This is the **canonical publication surface** for structure for readers and reviewers in Part B. (Didactic primacy governs this choice.)

* **Assurance Layer.** Three complementary kinds of support an author MAY attach:

  * **Constructive** grounding: a *generative* narrative that reconstructs the relation via the three mereological aggregators (`Γ_m.sum | Γ_m.set | Γ_m.slice`) from **Compose‑CAL**. (No formal notation is required in this pattern—only a reconstructible *story of construction*.)
  * **Logical** grounding: a *reasoned* chain (think KD‑CAL style arguments) that shows why the relation follows from stated premises.
  * **Mapping** grounding: a *type/lexical alignment* that shows the domain label truly denotes the intended U.Type relation (Kind-CAL / Lang‑CHR stance).
    These three kinds of support are *complementary*, not exclusive.

* **Empirical Validation.** How a published relation meets reality (observations, calibration scenarios). It lives beside, not inside, the relation. (See B.3 family.)

* **Grounding vocabulary (`tv:`).**

  * `tv:AliasOf` — declares that a Working‑Model relation is the **canonical projection** of a more general pattern (its “principle of use”).
  * `tv:groundedBy` — points to the **author’s grounding narrative** (Constructive, Logical, or Mapping, as applicable).
    The `tv:` namespace is part of the Core conceptual lexicon; it is **notation‑agnostic** and **tool‑agnostic**.

* **`tv:validationMode ∈ {postulate, inferential, axiomatic}`.** A **declaration by the author** of the *confidence stance* for a relation instance:
  *postulate* — a pragmatic working claim;
  *inferential* — a reasoned consequence;
  *axiomatic* — a constructively grounded identity (mereological extensionality is exhibited). (Modes align with the B.3 cluster’s trust model.)

> **Authoring note.** This pattern defines *meanings*, not formats. The words above SHALL be used consistently and without reference to any specific notations or execution environments (Guard‑Rails: Notational Independence).


#### B.3.5:9.2 - Normative rules (MUST/SHALL clauses for thinking‑and‑writing)

**S‑1 (Working-Model first).**
Authors **SHALL** publish structural claims in the **Working‑Model** form (`ut:*Of` relations). This is the canonical interface for human readers and cross‑disciplinary teams. Formal reconstructions are **optional** and live in the Assurance Layer.

**S‑2 (Alias declaration).**
If a Working‑Model relation follows a known general principle, the author **SHOULD** declare `tv:AliasOf <Principle>`, thereby making the intended *use‑pattern* explicit for reviewers and future readers. (This improves comparability without introducing extra formality.)

**S‑3 (Grounding by mode).**
For every relation instance the author **MUST** set `validationMode` and follow the corresponding grounding stance:

* **S‑3.a `postulate`.** The author **MAY** omit `Γ_m` grounding; the relation stands as a pragmatic working claim within a stated scope. The author **SHOULD** supply brief empirical cues (where the claim tends to hold) to ease later validation. (Empirical Validation is tracked in B.3.)

* **S‑3.b `inferential`.** The author **SHALL** outline a *reasoned chain* (plain‑language steps) that makes the relation a consequence of previously admitted statements. No formal calculus is required in this pattern; the outline must be sufficient for a peer to follow. (Think KD‑CAL stance, conceptually.)

* **S‑3.c `axiomatic`.** The author **SHALL** provide a *constructive grounding narrative* that reconstructs the relation as a `Γ_m.sum | Γ_m.set | Γ_m.slice` composition and **SHALL** link it with `tv:groundedBy`. The narrative **MUST** be reconstructible by a competent peer *without introducing new primitives* (parsimony). (Compose‑CAL’s three aggregators are the only constructive moves assumed here.)

* **S-3.d Structural constraint.** For **structural** edges, `tv:groundedBy → Γ_m.*` is **REQUIRED regardless of `validationMode`**; the `postulate` mode **MUST NOT** be used for structural mereology.

**S-4 (Relation-kind sense-making).**
* For **structural** subtypes of `ut:StructPartOf` (Component/Portion/Aspect), constructive grounding (`tv:groundedBy → Γ_m.*`) is **REQUIRED** in all modes; **`postulate` MUST NOT be used** for structural mereology (see S-3.d).

* For **epistemic/constitutive** links (e.g., representation, usage), constructive grounding is **OPTIONAL** in all stances; authors prefer *inferential* or *postulate* with empirical cues.

**S‑5 (Order and time are not mereology).**
Authors **SHALL NOT** encode execution order, parallelism, or temporal slicing as part‑whole. Such concerns belong to `Γ_method` and `Γ_time` families and **SHOULD** appear as method/time statements adjacent to, not inside, Working‑Model structure. (This prevents conceptual leakage between planes.)

**S‑6 (Unidirectional dependence).**
CT2R‑LOG may *consume* Compose‑CAL and KD‑CAL conceptually; it **SHALL NOT** redefine them. Meaning flows **downward only** (Kernel → Extention → Context → Instance).

**S‑7 (Register discipline).**
When naming principles in `tv:AliasOf`, authors **SHOULD** use Tech/Plain *twin labels* where available and obey minimal‑generality and rewrite rules (LEX‑BUNDLE), so that aliases are recognisable across context of meaning.

**S‑8 (No tool talk).**
Core prose **MUST NOT** introduce CI/CD terms, file formats, APIs, or machine‑oriented notations in place of concepts. If examples are needed, they **MAY** be plain‑language narratives or domain vignettes. (This pattern is conceptual by Standard.)


#### B.3.5:9.3 - Scope & Non‑Goals (to keep the plane clean)

* **In scope.**
  Canonical publication of relations for humans; alias‑to‑principle clarity; conceptual grounding stories; author‑declared *validationMode*; separation of structure vs order/time.

* **Out of scope.**
  Any machinery that *executes* checks; any binding to specific notations; any process/workflow mechanics; any discussion of file formats. (Those belong to tooling publications, pedagogy publications, and supporting records; they SHALL NOT be imported by the Conceptual Core.)

* **Edge placements.**
  When a claim is chiefly about *naming fit* across Contexts, prefer **Mapping** grounding (Kind-CAL/Lang‑CHR stance). When it is chiefly about *why* it follows, prefer **Logical** grounding. When it is about *what the whole is, from its parts*, prefer **Constructive** grounding. (Authors MAY combine them.)


#### B.3.5:9.4 - Author’s working moves (micro‑playbook, notation‑free)

**M‑1.** State the relation in **Working‑Model** form (e.g., “Impeller `ComponentOf` Pump”).
**M‑2.** Pick `validationMode`:

* If you’re sketching and exploring → choose **postulate**; add one‑sentence scope.
* If you’re justifying from known statements → choose **inferential**; list the 2–4 steps in plain language.
* If you require extensional identity → choose **axiomatic**; narrate the `Γ_m.*` reconstruction in a short paragraph.

**M‑3.** Add `tv:AliasOf` to the principle you intend readers to recognise (e.g., “Component = sum of parts”).
**M‑4.** Keep *order/time* adjacent, not embedded: if you need “assembled in two parallel lines”, write that as a **method/time** statement next to the structure, not as a part‑of edge.
**M‑5.** Stop when the *reader can follow without guessing*. This is the stopping rule for Quarter 2: clarity before formality. (Didactic primacy.)

