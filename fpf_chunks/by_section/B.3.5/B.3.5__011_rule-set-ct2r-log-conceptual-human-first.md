---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
section_id: "B.3.5:9"
section_title: "Rule‑set — CT2R‑LOG (conceptual, human‑first)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__011_rule-set-ct2r-log-conceptual-human-first.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "B.3.5 — Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
  - "B.3.5:9 — Rule‑set — CT2R‑LOG (conceptual, human‑first)"
line_start: 45358
line_end: 45453
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
---

### B.3.5:9 - Rule‑set — CT2R‑LOG (conceptual, human‑first)

**Intent (one line).** Publish readable Working-Model relation claims, resolve a useful alternative designation through an optional alias, and supply the assurance account required for assertions covered by an elected B.3.5 profile or named current requirement.

#### B.3.5:9.1 - Vocabulary and meanings in this pattern

* **Working-Model relation.** A human-oriented direct relation statement using a public name such as `ut:ComponentOf`, `ut:PortionOf`, or `ut:AspectOf`, or an ordinary sentence such as “this edition belongs to this product series.” It is the canonical public layer for readers; the direct pattern keeps the relation meaning fixed.

* **Assurance Layer.** Within the branch requirements, an author may combine these grounding contributions:

  * **Constructive** grounding: an inspectable account in one of the three C.13 forms (`Γ_m.sum | Γ_m.set | Γ_m.slice`). It names independently grounded participants, direct relation occurrences, the applicable construction rule, and identity or reidentification conditions. No formal notation is required, and the account does not create the relation it reports.
  * **Logical** grounding: a *reasoned* chain (think KD‑CAL style arguments) that shows why the relation follows from stated premises.
  * **Mapping** grounding: support for interpreting a relation designation or for a claimed correspondence between meanings. E.10/F.18 govern a same-meaning alias; F.9 governs a required correspondence between distinct local meanings.
    These contributions can be combined. Mapping supports interpretation or cross-context use; the assertion still needs the construction account, argument or evidence required by its branch in :4.

* **Empirical Validation.** Observations and calibration results support claims about the relation under the applicable conditions. Assess their contribution under B.3.

* **Grounding vocabulary (`tv:`).**

  * `tv:AliasOf` — links a local relation designation to the accepted Tech designation of that same relation under :5.
  * `tv:groundedBy` — links the covered assertion to the **author’s grounding account** required by its branch in :4. Interpretation or correspondence support may accompany that account; it cannot replace the branch’s required basis for the asserted relation. When a construction trace is recorded, it is a C.2.1 episteme with its own edition and currentness.
    The `tv:` namespace is part of the Core conceptual lexicon; it is **notation‑agnostic** and **tool‑agnostic**.

* **`tv:validationMode ∈ {postulate, inferential, axiomatic}`.** A **declaration by the author** of the *justification posture* for a relation instance:
  *postulate* — a pragmatic working claim;
  *inferential* — a reasoned consequence;
  *axiomatic* — the author declares that a constructive account is the assurance basis for this assertion. Assess that account under the relation's conditions and its receiving use.

> Use these terms consistently across notations; their meanings do not depend on one notation or execution environment.

#### B.3.5:9.2 - Normative rules (MUST/SHALL clauses for thinking‑and‑writing)

**S‑1 (Working-Model first).**
Authors **SHALL** state each covered direct relation claim in Working-Model form. Assurance accounts remain below that public layer. Electing this profile adds branch-specific trace and mode obligations; it is not a precondition for direct use.

**S‑2 (Alias declaration).**
When an alternative relation designation helps readers and carries the same meaning, the author **SHOULD** declare its `tv:AliasOf` link to the accepted Tech designation under :5. State the local use and cite the defining passage so readers can recover the intended relation. A direct claim using an already clear Tech designation needs no alias.

**S‑3 (Grounding by mode).**
For every relation instance covered by an elected B.3.5 profile, the author **MUST** set `validationMode` and follow the corresponding grounding stance:

* **S‑3.a `postulate`.** For a branch that permits it, state the working scope, link `tv:groundedBy` to an admissible evidence object, and give the empirical cues that would challenge the claim. No construction trace is required by this mode.

* **S‑3.b `inferential`.** For a branch that permits it, link `tv:groundedBy` to a short reasoned chain from admitted statements that a peer can follow.

* **S‑3.c `axiomatic`.** The author links the assertion to the current C.2.1 trace episteme required by its branch. A competent peer can recover the exact participants, direct relation occurrence, applicable rule, and identity or reidentification conditions. The account makes those facts inspectable.

* **S‑3.d Structural parthood.** A covered `ComponentOf`, `PortionOf`, or `AspectOf` assertion requires `validationMode=axiomatic` and the applicable current C.13 construction account; `postulate` is not available.

* **S‑3.e Collection belonging.** A covered belongs-to assertion uses the rule defined for that collection and requires `validationMode=axiomatic` and one current C.13 `set` trace. The trace reports already established belonging and collection identity. A logical argument or evidence object may support the inclusion decision separately, but neither substitutes for the elected set trace, turns belonging into parthood, or prohibits a separately grounded part claim.

**S-4 (Relation-kind sense-making).**
* For structural `ComponentOf`, `PortionOf`, and `AspectOf` claims, the elected profile requires the applicable current construction account and `validationMode=axiomatic`.

* For collection belonging, the elected profile requires one current `C.13 set` trace and `validationMode=axiomatic`. The collection's own rule still decides whether the occurrence obtains.

* For other epistemic or constitutive links, constructive grounding remains optional and the branch may prefer inferential or postulate reasoning with empirical cues.

**S‑5 (Order and time do not establish parthood).**
Execution order, parallelism or interval inclusion alone **SHALL NOT** establish a part-whole relation. State Method composition under B.1.5 and temporal facts under C.27; use B.1.4 when those recovered relations must be aggregated. Independently established A.15.1 Work-part relations and A.14 proper-phase relations for unchanged non-Work carriers remain admissible under their own rules.

**S‑6 (Unidirectional dependence).**
CT2R‑LOG may *consume* Compose‑CAL and KD‑CAL conceptually; it **SHALL NOT** redefine them. Meaning flows **downward only** (Kernel → Extension → Context → Instance).

**S‑7 (Register discipline).**
When naming relations in an alias declaration, authors **SHOULD** use the accepted Tech designation and, where available and permitted by E.10, its Plain twin. Obey the minimal-generality and rewrite rules (LEX-BUNDLE). Keep the declared local meaning and use recoverable when comparing labels across contexts.

**S‑8 (No tool talk).**
Core prose **MUST NOT** introduce CI/CD terms, file formats, APIs, or machine‑oriented notations in place of concepts. If examples are needed, they **MAY** be plain‑language narratives or domain vignettes.

#### B.3.5:9.3 - Scope & Non‑Goals (to keep the plane clean)

* **In scope.**
  Canonical publication of relations for humans; clarity of relation designations and their semantic sources; conceptual grounding stories; author‑declared *validationMode*; separation of structure vs order/time.

* **Out of scope.**
  Any machinery that *executes* checks; any binding to specific notations; any process/workflow mechanics; any discussion of file formats. (Those belong to tooling publications, pedagogy publications, and companion records; they SHALL NOT be imported by the Conceptual Core.)

* **Edge placements.**
  Choose the contribution for the question: resolve a same-meaning alias under E.10/F.18; use **Mapping** under F.9 for a required correspondence between distinct local meanings; use **Logical** grounding for an inference from premises and **Constructive** grounding for an account of a whole from its parts. Combine contributions when needed, retaining the claim support required by the elected branch, including its structural-parthood or collection-belonging trace.

#### B.3.5:9.4 - Author’s working moves (micro‑playbook, notation‑free)

**M‑1.** State the relation in **Working‑Model** form (e.g., “Impeller `ComponentOf` Pump”).
**M‑2.** If a publication choice or named current requirement elects this profile, pick `validationMode`; otherwise keep the direct relation claim and stop:

* For a permitted exploratory claim, choose **postulate**, link its empirical support, and state scope plus challenge cues.
* For a permitted conclusion from known statements, choose **inferential** and link the short argument.
* For structural parthood covered by the profile, choose **axiomatic** and link the applicable current construction account.
* For collection belonging covered by the profile, choose **axiomatic** and link one current `C.13 set` trace that reports the already established relation under the collection's own rule.
* For another permitted epistemic or constitutive claim whose chosen basis is a qualifying C.13 account, choose **axiomatic** and link that account.

**M‑3.** When an alternative designation helps readers, link that designation through `tv:AliasOf` to the accepted Tech designation of the same relation. State its local use and cite the definition; apply :5 when the meaning or participant order differs.
**M‑4.** If assembly uses two parallel lines, state the actual Method/Work and temporal facts. Add any independently obtaining part relation under its own rule; parallelism alone does not establish it.
**M‑5.** Stop when the selected readable relation and remaining non-use boundary are clear and, if this profile is elected, its validation mode and required current support are recoverable without guessing.

