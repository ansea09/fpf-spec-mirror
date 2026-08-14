---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF"
section_id: "E.10:7"
section_title: "Minimal Generality and Domain Anchoring (MG-DA) — names neither parochial nor vacuous"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__009_minimal-generality-and-domain-anchoring-mg-da-names-neither-parochial-nor-vacuous.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF"
  - "E.10:7 — Minimal Generality and Domain Anchoring (MG-DA) — names neither parochial nor vacuous"
line_start: 75315
line_end: 75411
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.2"
  - "A.15.PROD"
  - "A.19.SPR"
  - "A.2"
  - "A.2.1"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.3.2"
  - "A.6.0"
  - "A.6.5"
  - "A.6.6"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.7"
  - "B.1"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.D1"
  - "E.10.MOVE"
  - "E.10.ROLE"
  - "E.17"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.5"
  - "F.17"
  - "F.18"
  - "F.19"
  - "F.5"
  - "F.6"
  - "F.9"
  - "U.SystemRoleAssignment"
keywords:
---

### E.10:7 - Minimal Generality and Domain Anchoring (MG-DA) — names neither parochial nor vacuous

> **Principle (MG-DA).** A minted name is **as general as necessary and no more**, and its **head noun is anchored to the FPF kind being named**. First classify the **NameToken (name of a concept: term, lexical unit) itself** using **`LEX.TokenClass`**, then apply the guardrails corresponding to that class: kernel tokens unify **across domains**; discriminator tokens and context tokens make the **domain legible** *from the name itself*. Names too general to have an obvious domain fail MG-DA.

#### E.10:7.1 - `LEX.TokenClass` (meta‑lexical; not a USM Scope)
**Definition.** `LEX.TokenClass : NameToken → {KernelToken | ContextToken | DiscriminatorToken}`.
This is a local lexical classification function on NameTokens with the closed value set `{KernelToken | ContextToken | DiscriminatorToken}`, used by the LEX registry and MG-DA checks. It is not thereby a `U.Characteristic` or a `CharacteristicSpace`; that CHR reading would require a separately named `U.Characteristic` with one declared CSLC scale.
It is **not** a USM scope and carries **no** truth or validity semantics.

#### E.10:7.2 - `KernelToken` — Minimal Generality (MG‑K)
**MG-K1 (Tri-domain witness).** A DRR note or Glossary note provides at least three heterogeneous arenas where the invariants hold, for example manufacturing, healthcare, and cloud operations. Otherwise reject or narrow the `KernelToken` candidate and recover each word or qualifier under the object and rule that define it. Use a `ContextToken` only after the context-local lexical use and semantic locality are recovered. Use an A.19 `CharacteristicSpace` only when one named `U.Characteristic`, one declared CSLC scale, the governing context, and the exact receiving use make that construction current; an assignment-state relation remains under A.2.5.
**MG-K2 (No parochial nouns).** Kernel names contain no domain nouns such as *Ticket, Microservice, Patient,* or *Developer*. Domain-looking wording is a recovery trigger, not a destination: it may denote a C.3 local kind, exact system-role kind, system-role assignment, system or architecture object, episteme or record kind, declared Characteristic and scale, source wording, ordinary qualifier, recovered `ContextToken` use, or another value whose kind and use are already defined. Bare *role* has no default Tech reading. `SystemRole` appears only inside a concrete context-local kind designation admitted through C.3 and A.2; lexical shape alone creates neither that kind nor an assignment.
**MG-K3 (No vacuity).** Avoid vacuous heads such as *Thing, Event, Process,* or *Resource*. Use existing U-kind heads such as `U.Holon`, `U.Work`, and `U.Method`.
**MG-K4 (Intent after recovery).** U-kind names and labels for an exact local system-role kind or its F.4 `SystemRoleKindDescription` encode recovered semantic intent rather than notation, implementation, or local-realizer accidents. Algorithm, hardware-form, and recipe-flavor wording is a recovery trigger, not one ontological family: name one `U.Method`, qualifying `U.MethodDescription`, `U.Capability`, `U.Mechanism`, system or architecture object, A.19 `CharacteristicSpace`, A.2.5 `SystemRoleAssignmentStateRelation`, C.29 representation, formal substrate, source wording, or another value only when the predicate for that value is satisfied. Do not use Capability, CharacteristicSpace, assignment-state relation, or mechanism as disposal bins for unlike cases.
**MG‑K5 (Notation independence, SHOULD).** The EntityOfConcern-side kind criterion is separable from any one notation or toolchain.
**MG-K6 (Refactoring safety).** If a name fails MG, record a DRR and apply F.13 **Lexical Continuity and Deprecation** rather than mutating it silently.

#### E.10:7.3 - `DiscriminatorToken` and `ContextToken` — Domain Anchoring (DA‑D)
**DA-D1 (kind anchoring).** The head noun names the **FPF kind being classified** (for example *Sense*, *Context*, *Bridge*, or *Characteristic*). A concrete local system-role-kind designation may use the `SystemRole` compound, for example `ReviewerSystemRole`; bare *Role* fails this test because it does not reveal whether the claim concerns classification, assignment, participation, declaration, representation, episteme use, or ordinary wording. Readers can answer “**X of what?**” without external context.
**DA-D2 (Enumeration rule, not axis).** An enumerated property is a CHR construction only when one named `U.Characteristic` is bound to one declared CSLC scale in a `CharacteristicSpace`. Otherwise recover the closed value set, classified kind, local classifier, state/status frame, source wording, C.29 representation, example or alternative set, or another construction defined for that value. Avoid spatial metaphors (*axis, dimension, plane, lane, tier, layer*) unless the metaphor is a pattern-defined primitive in this spec.
**DA-D3 (Enum clarity).** If the term denotes an enumeration, the value set is **small and closed**, membership criteria are obvious from the definition, and the **kind being classified** is explicit in the name (e.g., `SenseFamily`, not bare *Family*, *RowPlane* or overly general *Facet*).
**DA-D4 (Anti-recipe).** Do not bake *how-to* or local methods into discriminator names. The way of doing belongs in one exact `U.Method`; a claim-bearing episteme belongs in `U.MethodDescription` only when that method is its exact EntityOfConcern and A.3.2's positive threshold is met. Use `U.Capability` instead when the kind under repair is an ability envelope.
**DA-D5 (Mapping discipline).** Cross-context interpretations go through a **Bridge** (F.9). Discriminator names do not suggest global identity.
**DA-D6 (Register discipline).** Keep normative tokens stable; synonyms belong in the **Plain** register only and stay outside constraints and tests.
**DA-D7 (Ban generic combinators).** Reject vague composites like *NameUseMode*, *NamingScope*, `RowFacet`, `RowPlane`, or `RowLane`. Each candidate passes **DA-D1** and **DA-D3** for a kind-anchored head, explicit classified kind, and closed-value interpretation under its classification rule. Require a `CharacteristicSpace` only when one named `U.Characteristic` and its CSLC scale have independently been declared.

#### E.10:7.4  - Global tests (apply after 7.2 and 7.3)
**MG-DA-T1 (Three-arena witness).** A **`LEX.TokenClass`(t)=KernelToken** candidate includes the tri-domain witnesses from MG-K1. Other token classes document at least one contrasting arena.
**MG-DA‑T2 (Object‑of‑talk).** The head noun uniquely signals the subject area; avoid free-floating metaphors. **MG-DA‑T3 (Implementation-word recovery).** Do not relocate mechanism- or implementation-looking wording by lexical category. First recover the object and rule; remove accidental implementation wording from the candidate token only after that recovery. Use `U.Method`, qualifying `U.MethodDescription`, `U.Capability`, `U.Mechanism`, a system or architecture object, A.19 `CharacteristicSpace`, A.2.5 `SystemRoleAssignmentStateRelation`, C.29 representation, formal substrate, source wording, or another value only when its predicate is satisfied.
**MG-DA‑T4 (Enum clarity).** For an enumeration, list the closed value set, the kind being classified, and the rule that classifies it. Add a `CharacteristicSpace` only when the enumeration is one declared CSLC scale for a named `U.Characteristic`; list shape alone does not establish CHR membership.
**MG-DA-T5 (Collision and uniqueness).** Before merge, perform a **full-text search** over the corpus and the **Reserved-Names registry**. A candidate colliding with an existing token used in another FPF sense is not admitted; rename it or raise a DRR to deprecate the prior token.
**MG-DA‑T6 (Teaching swap).** In didactic prose (E.10.D2), the term can be swapped in **without caveats**.
**MG-DA-T7 (EntityOfConcern ground).** The definition card states the EntityOfConcern-side kind criterion for membership explicitly; reviewers can check membership without consulting external narrative.

#### E.10:7.5 - Compatibility with USM (how tokens and scopes meet)
**USM applies to acts, not tokens.** Mint, rename, and use are **LexicalActs** that carry a USM scope. `LEX.TokenClass` constrains **where** a token may be used via an **AllowedScopes** policy:
**Conformance rule.** For any usage `u` of a token `t`: `LEX.TokenClass(t)=c  ⇒  USM.Scope(u) ∈ AllowedScopes(c).`

The LEX registry defines `AllowedScopes(c)` (e.g., `KernelToken` usage in normative kernel constraints is admitted; Plain-register use outside a glossary is restricted; Context emissions of `KernelToken` are admitted through a Bridge or alias).

**Audit.** Violations are flagged as **SCR‑LEX‑Sxx** (see acceptance tests below).

#### E.10:7.5a - Lexical prerequisites for a durable token

Mentioning `LEX.TokenClass`, `LEX.Reserved-Names`, or `LEX.AllowedScopes` does not create the values needed to admit a durable token. Before a NameCard can become current, the selected `FPFCoreReferenceScheme` must resolve four things: (1) the `U.NameToken`; (2) its current TokenClass classification assertion; (3) the current reserved-name or other authoritative collision-set value and the collision result; and (4) the current allowed-scope policy and a passing use-scope assertion. A prose example, full-text absence, heading, registry-shaped table, or intended policy supplies none of them by implication.

**Worked near-miss.** Suppose `SelectedRuleContentSubgraphDesignation`, `derivedUsingRuleContent`, and `evaluatedAgainstRuleContent` are proposed as `KernelToken` candidates. They can pass the tri-domain and object-of-talk tests through assembly-rule content selected in manufacturing derivation, protocol content used in healthcare derivation while evidence separately warrants case facts, and deployment-policy content selected for cloud release evaluation while service-provision Work and operational support remain separate. Even if their spellings do not collide in the inspected corpus, corpus absence is not a reserved-name or allowed-scope result. Do not publish their F.18 NameCards or F.17 rows until all four prerequisites resolve; a placeholder card or row closes none of them.

Using these names as candidate designators in declaration content changes no predicate semantics and does not admit them as public names, enumerations, Characteristics, CharacteristicSpace values, relation kinds, or U-kinds.

#### E.10:7.5b - Role-Precision Token Classes and Allowed Uses

The eight selected names below are `KernelToken` values under `FPFCoreReferenceScheme`. Each names one value already defined or constrained by its subject pattern; the lexical rule admits no kind, relation occurrence, declaration, judgment, description, structure, NameCard, row, or publication occurrence.

| `U.NameToken` | `LEX.TokenClass` | Named value and subject pattern | Stable admitted use |
| --- | --- | --- | --- |
| `U.SystemRoleAssignment` | `KernelToken` | direct assignment family under A.2.1 | exact Core definition, directly declared species, typed reference constraint, conformance check, worked case for the same family, F.18 NameCard, or F.17 row |
| `KindUseAdaptationDeclaration` | `KernelToken` | C.3.4 declaration-episteme family | exact Core definition, typed declaration or constraint, conformance check, worked case for the same family, F.18 NameCard, or F.17 row |
| `KindUseAdaptationCorrespondenceDeclaration` | `KernelToken` | C.3.4 correspondence-declaration family | exact Core definition, typed declaration or constraint, conformance check, worked case for the same family, F.18 NameCard, or F.17 row |
| `KindUseAdaptationJudgment` | `KernelToken` | C.3.4 three-valued judgment family | exact Core definition, typed judgment or constraint, conformance check, worked case for the same family, F.18 NameCard, or F.17 row |
| `SystemRoleKindDescription` | `KernelToken` | F.4 description-episteme construction | exact Core definition, typed description or constraint, conformance check, worked case for the same construction, F.18 NameCard, or F.17 row |
| `SystemRoleAssignmentStateRelation` | `KernelToken` | A.2.5 direct relation kind | exact Core definition, directly declared relation use or typed constraint, conformance check, worked case for the same relation, F.18 NameCard, or F.17 row |
| `SystemRoleAssignmentStatePredicate` | `KernelToken` | A.2.5 predicate-value family | exact Core definition, directly declared predicate use or typed constraint, conformance check, worked case for the same family, F.18 NameCard, or F.17 row |
| `SystemRoleKindRelationStructure` | `KernelToken` | A.2.7 selected-structure construction | exact Core definition, typed structure use or constraint, conformance check, worked case for the same construction, F.18 NameCard, or F.17 row |

For all eight names, Plain wording that silently turns the token into a neighboring object is prohibited. Reuse in another context requires that context's own identity rule and, when two sense cells are compared, the separately admitted Bridge and use claim. A change to the named value, TokenClass classification, or stable allowed-use rule reopens only the affected NameCard and row. A collision or conformance result for one dated corpus or candidate is evidence for its publication decision; it is not a reusable lexical rule or a currentness participant in the public pattern.

`SystemRole` alone is not a governed universal token or a NameCard subject. It is common morphology inside a concrete context-local designation such as `ReviewerSystemRole`, whose defining C.3/A.2 context decides identity. `AssignedSystemRoleKindSlot`, `SystemRoleAssignmentSlot`, and fields ending in `...SystemRoleKindRef` or `...SystemRoleAssignmentRef` remain declaration-local `ContextToken` uses; the fields are typed by existing `U.KindRef` or `U.RelationRef`, not by newly minted RefKinds. `J_kindUse` remains local notation. None receives a public row merely because the spelling recurs.

#### E.10:7.6 - Metaphor guidance (informative heuristics)

Prefer **object‑anchored heads** to metaphors. If a metaphor is unavoidable, ensure it is (a) explicitly defined by a pattern here, and (b) unambiguous within the **NameClass**. Example families (use sparingly):
* **Progression metaphors** (*level, tier, ladder*): only where a **gate or upgrade** is defined by the pattern.
* **Separation metaphors** (*lane, track*): only where parallel, non‑interfering flows are enforced by rules.
* **Grouping metaphors** (*family, class*): only for **small, closed enumerations** attached to a clearly named classified kind (e.g., `SenseFamily` rather than bare *Family*).

#### E.10:7.7 - Short‑form and acronym discipline
**SF-1 (First expansion).** On first use, expand the term and place the short form in parentheses (e.g., “Minimal Generality and Domain Anchoring (**MG-DA**)”).
**SF-2 (Uniqueness).** Register short forms in the **Reserved-Names** list and perform the collision check (MG-DA-T5).
**SF‑3 (Form, SHOULD).** Prefer typographic separators (**MG-DA**) to fused acronyms (**MGDA**). Use the fused form only in code or identifiers where punctuation is disallowed, and only after registration.

#### E.10:7.8 - Examples (illustrative, canonical)
Prefer **`U.PromiseContent`** (promise) over *BusinessService*; **`U.Capability`** over *Function*; **`U.Dynamics`** over *NaturalProcess*. Replace *ScheduleProcess* with `U.WorkPlan` only when one episteme passes A.15.2: one present EntityOfConcern, one horizon, at least one `PlanItem`, and substantive coordination claims about possible future performed work. Otherwise retain the schedule representation, planning cue, or other recovered construction.
Do **not** mint *ETLService* at kernel level. Recover the ETL claim first: the way of doing may be one `U.Method`; a separately identified claim-bearing episteme may be `U.MethodDescription` only when that method is its EntityOfConcern and the A.3.2 substantive-description threshold is met. An ETL label, pipeline diagram, code expression, mechanism, work plan, dated Work occurrence, or API publication establishes neither membership. If a relied-on *service* use still hides another subject or relation, apply L-SERV and A.6.P:4.11a and name the recovered claim; the suffix alone requires no promise, access, acceptance, Work, or publication branch.

#### E.10:7.9 - Acceptance and regression checks (LEX and USM)
**SCR‑LEX‑S01 (TokenClass declaration).** Every normative token has a declared `LEX.TokenClass`.
**SCR‑LEX‑S02 (Collision and uniqueness).** Full‑text + Reserved‑Names check passes (no other meaning in FPF).
**SCR‑LEX‑S03 (kind anchoring).** Heads name the FPF kind classified (DA‑D1).
**SCR‑LEX‑S04 (Enumeration rule gate).** Every enumeration names its closed value set, classified kind, and classification rule. Require a `CharacteristicSpace` only when one named `U.Characteristic` is bound to one declared CSLC scale; otherwise retain the local classifier, state/status value set, source wording or C.29 representation, example or alternative set, local kind, or another construction defined for that classification.
**SCR‑LEX‑S05 (USM compatibility).** For each LexicalAct, `USM.Scope ∈ AllowedScopes(LEX.TokenClass)`.
**SCR‑LEX‑S06 (Slot and Ref suffix discipline).** A token ending in **`…Slot`** names the declaration-local **SlotKind** inside one exact A.6.5 `SlotSpec` of one reusable `RelationSignature`. A token ending in **`…Ref`** names either a RefKind admitted by its direct reference pattern or a receiving-episteme field explicitly typed by that RefKind; the field remains designation or reference apparatus and does not become the participant or SlotSpec. No ValueKind or representation field may acquire either suffix by shape alone.
**SCR-LEX-S07 (Manifest `provides` follows exact signature claims).** If a `SignatureManifest` is present, its `provides` entry is used only when that signature's exact `U.ClaimGraph` states that the signature introduces public names for dependent use. The entry carries that claim content or visibly represents it; list membership alone establishes neither provision nor a consumer dependency. Include only names actually introduced by this signature under the patterns that define them, such as its own A.6.5 relation-participant SlotKinds and RefKinds whose direct reference patterns admit them. A RefKind defined elsewhere remains defined there, and membership in an A.6.1 operation-argument or result declaration list does not transfer its definition to the manifest. A mathematical operand, table column, tuple place, or other C.29 representation element becomes no provided SlotKind by shape; any reuse still needs its independently governed declaration and explicit correspondence.
**RSCR‑LEX‑E01 (Banned generics).** Reject tokens matching the banned combinators list (DA‑D7).
**RSCR‑LEX‑E02 (Metaphor hygiene).** If a metaphor is used, show the pattern that defines it; otherwise rename.
**RSCR‑LEX‑E03 (Strategy token minting).** Reject new Kernel tokens named **Strategy** or **Policy** as kinds; model them as **lenses**, **flows**, or **compositions** inside **G.5**, or as **…Description** or **…Spec** in Contexts. (Prevents kernel overloading; aligns with C.22 “no minted Strategy head”.)

