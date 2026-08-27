---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:9"
section_title: "Rule‑set — CT2R‑LOG (conceptual, human‑first)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__011_rule-set-ct2r-log-conceptual-human-first.md"
commit_sha: "3f6714ae3235e0d771dce32835be7696f626d2ee"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:9 — Rule‑set — CT2R‑LOG (conceptual, human‑first)"
line_start: 39324
line_end: 39418
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
---

### B.3.5:9 - Rule‑set — CT2R‑LOG (conceptual, human‑first)

**Intent (one line).** Make **Working-Model** relations the canonical relation vocabulary for authors, while providing a clean, purpose-selected bridge to assurance through aliasing and grounding semantics; the bridge is required only for the published assertions covered by an elected B.3.5 profile or named current requirement.

#### B.3.5:9.1 - Vocabulary and meanings in this pattern

* **Working-Model relation.** A human-oriented direct relation statement using a public name such as `ut:ComponentOf`, `ut:PortionOf`, or `ut:AspectOf`, or an ordinary sentence such as “this edition belongs to this product series.” It is the canonical public layer for readers; the direct pattern keeps the relation meaning fixed.

* **Assurance Layer.** Three complementary assurance modes an author MAY attach:

  * **Constructive** grounding: an inspectable account in one of the three C.13 forms (`Γ_m.sum | Γ_m.set | Γ_m.slice`). It names independently grounded participants, direct relation occurrences, the applicable construction rule, and identity or reidentification conditions. No formal notation is required, and the account does not create the relation it reports.
  * **Logical** grounding: a *reasoned* chain (think KD‑CAL style arguments) that shows why the relation follows from stated premises.
  * **Mapping** grounding: a *relation-label alignment* that shows the domain label truly denotes the intended Working-Model relation (Kind-CAL / Lang-CHR stance).
    These three assurance modes are *complementary*, not exclusive.

* **Empirical Validation.** How a published relation meets reality (observations, calibration scenarios). It lives beside, not inside, the relation. (See B.3 family.)

* **Grounding vocabulary (`tv:`).**

  * `tv:AliasOf` — declares that a Working‑Model relation is the **canonical projection** of a more general pattern (its “principle of use”).
  * `tv:groundedBy` — points to the **author's grounding account** (Constructive, Logical, or Mapping, as applicable). When a construction trace is recorded, it is a C.2.1 episteme with its own edition and currentness.
    The `tv:` namespace is part of the Core conceptual lexicon; it is **notation‑agnostic** and **tool‑agnostic**.

* **`tv:validationMode ∈ {postulate, inferential, axiomatic}`.** A **declaration by the author** of the *confidence stance* for a relation instance:
  *postulate* — a pragmatic working claim;
  *inferential* — a reasoned consequence;
  *axiomatic* — the author declares that a constructive account is the assurance basis for this assertion. The mode does not classify the world-side relation and guarantees neither identity nor timelessness.

> **Authoring note.** This pattern defines *meanings*, not formats. The words above SHALL be used consistently and without reference to any specific notations or execution environments (Guard‑Rails: Notational Independence).

#### B.3.5:9.2 - Normative rules (MUST/SHALL clauses for thinking‑and‑writing)

**S‑1 (Working-Model first).**
Authors **SHALL** state each covered direct relation claim in Working-Model form. Assurance accounts remain below that public layer. Electing this profile adds branch-specific trace and mode obligations; it is not a precondition for direct use.

**S‑2 (Alias declaration).**
If a Working‑Model relation follows a known general principle, the author **SHOULD** declare `tv:AliasOf <Principle>`, thereby making the intended *use‑pattern* explicit for reviewers and future readers. (This improves comparability without introducing extra formality.)

**S‑3 (Grounding by mode).**
For every relation instance covered by an elected B.3.5 profile, the author **MUST** set `validationMode` and follow the corresponding grounding stance:

* **S‑3.a `postulate`.** For a branch that permits it, the author may omit constructive grounding, state the working scope, and give the empirical cues that would challenge the claim.

* **S‑3.b `inferential`.** For a branch that permits it, the author gives a short reasoned chain from admitted statements that a peer can follow.

* **S‑3.c `axiomatic`.** The author links the assertion to the current C.2.1 trace episteme required by its branch. A competent peer can recover the exact participants, direct relation occurrence, applicable rule, and identity or reidentification conditions. The account supports inspection; it creates none of those facts.

* **S‑3.d Structural parthood.** A covered `ComponentOf`, `PortionOf`, or `AspectOf` assertion requires `validationMode=axiomatic` and the applicable current C.13 construction account; `postulate` is not available.

* **S‑3.e Collection belonging.** A covered belongs-to assertion uses the rule defined for that collection and requires `validationMode=axiomatic` and one current C.13 `set` trace. The trace reports already established belonging and collection identity. A logical argument or evidence object may support the inclusion decision separately, but neither substitutes for the elected set trace, turns belonging into parthood, or prohibits a separately grounded part claim.

**S-4 (Relation-kind sense-making).**
* For structural `ComponentOf`, `PortionOf`, and `AspectOf` claims, the elected profile requires the applicable current construction account and `validationMode=axiomatic`.

* For collection belonging, the elected profile requires one current `C.13 set` trace and `validationMode=axiomatic`. The collection's own rule still decides whether the occurrence obtains.

* For other epistemic or constitutive links, constructive grounding remains optional and the branch may prefer inferential or postulate reasoning with empirical cues.

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
  Any machinery that *executes* checks; any binding to specific notations; any process/workflow mechanics; any discussion of file formats. (Those belong to tooling publications, pedagogy publications, and companion records; they SHALL NOT be imported by the Conceptual Core.)

* **Edge placements.**
  When a claim is chiefly about *naming fit* across Contexts, prefer **Mapping** grounding (Kind-CAL/Lang‑CHR stance). When it is chiefly about *why* it follows, prefer **Logical** grounding. When it is about *what the whole is, from its parts*, prefer **Constructive** grounding. (Authors MAY combine them.)

#### B.3.5:9.4 - Author’s working moves (micro‑playbook, notation‑free)

**M‑1.** State the relation in **Working‑Model** form (e.g., “Impeller `ComponentOf` Pump”).
**M‑2.** If a publication choice or named current requirement elects this profile, pick `validationMode`; otherwise keep the direct relation claim and stop:

* For a permitted exploratory claim, choose **postulate** and state scope plus challenge cues.
* For a permitted conclusion from known statements, choose **inferential** and list the short argument.
* For structural parthood covered by the profile, choose **axiomatic** and link the applicable current construction account.
* For collection belonging covered by the profile, choose **axiomatic** and link one current `C.13 set` trace that reports the already established relation under the collection's own rule.

**M‑3.** Add `tv:AliasOf` only when a named direct relation principle helps reviewers recognize the intended reading; do not alias the relation to a constructor result.
**M‑4.** Keep *order/time* adjacent, not embedded: if you need “assembled in two parallel lines”, write that as a **method/time** statement next to the structure, not as a part‑of edge.
**M‑5.** Stop when the selected readable relation and remaining non-use boundary are clear and, if this profile is elected, its validation mode and required current support are recoverable without guessing.

