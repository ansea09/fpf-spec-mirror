---
chunk_kind: "child"
pattern_id: "E.20"
pattern_title: "Mechanism Introduction Protocol"
section_id: "E.20:4"
section_title: "Solution — the Mechanism Introduction Protocol (MIP)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.20/E.20__005_solution-the-mechanism-introduction-protocol-mip.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "E.20 — Mechanism Introduction Protocol"
  - "E.20:4 — Solution — the Mechanism Introduction Protocol (MIP)"
line_start: 87348
line_end: 87573
dependencies:
  - "A.15.3"
  - "A.6.1"
  - "A.6.7"
  - "E.10"
  - "E.15"
  - "E.18"
  - "E.19"
  - "E.8"
  - "E.9"
  - "F.18"
  - "G.2"
  - "G.Core"
  - "G.x"
keywords:
  - "MIP-run manifest"
  - "P2W seam"
  - "PQG profiles"
  - "SlotKind lexicon discipline"
  - "alias docking"
  - "authoring protocol"
  - "canonical card-first"
  - "governing-definition assignment"
  - "mechanism introduction"
  - "no dangling …IntensionRef"
  - "regression envelope"
  - "suite boundary hygiene"
  - "typed RSCR triggers"
---

### E.20:4 - Solution — the Mechanism Introduction Protocol (MIP)

#### E.20:4.0 - Terminology note (disambiguation)

*This protocol and any MIP-run manifest are authoring-side semantic-governing-definition assignment maps.* A manifest is not an approval packet, gate, runtime decision, or pass/fail result. It names where mechanism meaning is governed and what must not be inferred from suites, plans, wiring, aliases, or gates.

MIP governs **how changes are assigned to their governing definitions**, not how systems execute.

**MIP trigger triage.** Not every reference cleanup is a MIP-run. Classify the proposed edit before requiring a manifest:

* **MIP not triggered:** pure currentness, reference, typo, or old-label cleanup that changes no mechanism, suite, planned-baseline, wiring, governing-definition, or citeable-token semantics.
* **Local wording or alias-docking only:** wording clarifies an already-governed mechanism relation, or `F.18` alias docking preserves citeability of an old token without changing what the token denotes.
* **MIP-run manifest required:** the edit changes mechanism meaning, suite denotation, suite closure, suite obligations, suite pins, suite protocol semantics, planned-baseline pins, wiring semantics, governing-definition assignment, or what a citeable token denotes.

Only the third outcome uses the manifest in `E.20:4.2`. The first two still name the current governing locus or alias-docking relation when the text will be published. When the only current result is no denotation change, the published content should not carry MIP-run vocabulary except as a short non-trigger note.

#### E.20:4.0.1 - Mint vs reuse

**Mints:**
* **MIP** — Mechanism Introduction Protocol (this pattern).
* **MIP-run** — an authoring event that applies this protocol to a concrete change set, captured as a short manifest (recorded as a DRR-linked change record or an equivalent, explicitly citeable change record).

**Reuses:**
* A.6.1 `U.Mechanism` epistemes, their `MechanismDefinitionRef` designators, non-mechanism reference-reservation stubs, suite descriptions (`MechSuiteDescription` and specializations), exact A.15.2 `U.WorkPlan` epistemes and their declaration-local A.15.3 planned-filling rows, alias docking (F.18), RSCR triggers (G.Core), and PQG profiles (E.19).

#### E.20:4.1 - Step 1: Classify the introduction

A MIP-run SHALL first classify the change, because different classes have different governing definitions:

1. **New declared operation family or archetypal grounding.** The `EntityOfConcernRef` names an operation family not previously declared at the selected governing locus.
2. **New mechanism declaration or semantic edition.** One A.6.1 `U.Mechanism` episteme receives new identity-bearing content or a new effective `U.ReferenceScheme`.
3. **Neighboring mechanism-relation change.** A realization, refinement, conservative extension, equivalence, bridge, evaluation, evidence-use, or publication relation changes while the mechanism content does not.
4. **Suite change** (membership, obligations, spec pins, or suite protocols).
5. **Planned-baseline change** (new or revised declaration-local planned-filling rows inside one exact `U.WorkPlan`, or changes to their pins).
6. **Wiring change** (new or revised Part-G extension modules, SoTA method packs, or selectors).
7. **Terminology migration** (renames, token splits or merges, or register changes).
8. **Deprecation, supersession, or retirement** (status change, successor relation, and preserved citeability; apply E.20:4.9.1).

**Mechanism-kind boundary.** `MechanismDefinitionRef` is a designator. Minting it neither creates a `U.Mechanism` episteme nor admits a new U-kind. A new U-kind claim requires E.24.UK; a new mechanism episteme must satisfy A.6.1 identity and content; a new transformation-flow structure requires E.18.

**A.6.1 compatibility.** Mechanism identity is `<content, EntityOfConcernRef, effectiveReferenceScheme>`. Identity-bearing content comprises direct subject and range fields, `OperationAlgebra`, `LawSet`, `AdmissibilityConditions`, Applicability, and an optional `SignatureManifest` when dependency replay matters. An operation index may be derived from the declaration-local `operationDesignator` values; it is not another content group. Each operation's arguments and results remain A.6.1 `ArgumentDeclaration` and `ResultDeclaration` content. A.6.5 SlotSpecs remain exclusive to a `RelationSignature` for an already governed direct relation. Realization, refinement, extension, bridge, evaluation, evidence-use, and publication relations are governed separately.

**New-declaration criterion.** Treat a change as a new declared operation family when `EntityOfConcernRef` changes. Treat changed mechanism content or effective reference scheme as a new semantic edition. A changed neighboring relation alone does not create a new mechanism identity, although it may reopen reliance on the current declaration.
A single MIP-run MAY span multiple classes, but SHALL treat each class with its correct governing-definition assignment (below).

#### E.20:4.2 - Step 2: Declare the governing-definition assignment map (mandatory)

For every new or modified change item, the MIP-run SHALL name **exactly one governing definition** and assign the change there. In FPF, that governing definition is a citeable, patchable `PatternId`, `PatternId:SectionPath`, `PatternScopeId = G.x:Ext.*`, or `DRRId` (E.9). The core MIP-run manifest in a citeable change record is limited to:

* each changed item,
* its governing definition,
* its canonical location (expressed as `PatternId:SectionPath`, `PatternScopeId`, or `DRRId`, not as prose), and
* the forbidden overread or forbidden move blocked by that assignment.

Conditional manifest fields appear only when the corresponding claim is present:

* the change class(es) from E.20:4.1 when needed to disambiguate the assignment,
* new or changed citeable tokens, including a `MechanismDefinitionRef` or a public operation, argument, or result designator, when token denotation or citeability changes,
* the actual-effect Delta-Class (`Δ-0` to `Δ-3`) and affected-reach estimate from E.15 when the run is plausibly `Δ-2` or `Δ-3`,
* intended RSCR trigger types when a refresh or regression-wiring claim is present, and
* the PQG (E.19) profile set when the run crosses an E.19-governed review boundary.

**Note (normative).** If the canonical location is a Part‑G wiring module, it SHALL be cited as a `PatternScopeId` (`G.x:Ext.*`) and the module SHALL declare `GoverningPatternId` (wiring is binding-only; meaning remains governed by its cited pattern).

**Canonical governing-definition map (normative):**

| Change kind | Governing definition | Canonical location | Forbidden move |
|---|---|---|---|
| `U.Mechanism` identity and content: exact `EntityOfConcernRef`, effective reference scheme, direct subject and range fields, operation algebra, laws, admissibility, Applicability, and optional dependency manifest | **Mechanism-subject pattern under A.6.1** | Designated mechanism-subject pattern | A suite, plan, wiring module, card layout, or MIP manifest does not supply mechanism semantics; neighboring relations stay with their direct patterns. |
| Suite membership, obligations, spec pins, and suite protocols | **Suite-subject pattern** | `A.6.7` or `A.6.7.<FamilyKey>` | SHALL NOT carry mechanism semantics, acceptance thresholds, gate criteria, DecisionLogs, or publication tails into the suite. |
| Planned baseline pins (planned slot fillings, edition-pinned refs, explicit time selector) | **One `U.WorkPlan` and the planned-filling rows kept inside it** | `A.15.2` plus `A.15.3` rows that point to declaration members defined by their own patterns | SHALL NOT embed launch values, witnesses, or gate decisions in planning, or give a row independent identity. |
| SoTA method, comparator, or generator **definitions**, including provenance and evaluation semantics | **SoTA-pack subject pattern** | `G.2` (SoTA synthesis packs) | SHALL NOT rephrase SoTA evolution as kernel semantics. |
| Wiring that binds SoTA packs into flows or tasks | **Extension module governing definition** | `G.x:Ext.*` (`GPatternExtension` with explicit `PatternScopeId`) | SHALL NOT mint new semantics; SHALL bind only. |
| Token renames and drift management | **Lexical subject pattern** | `F.18` (alias docking) plus registers per E.10/F.17 | SHALL NOT silently rewrite tokens or break citations. |
| Change-cause taxonomy and regression triggers | **RSCR subject pattern** | `G.Core` | SHALL NOT invent ad hoc “reason kinds” scattered in patterns. |
| Project specializations of a mechanism | **Project specialization pattern** | `P.*` patterns (using `⊑/⊑⁺`) | SHALL NOT mutate kernel membership to express project variants. |

**Guard (normative).** Any proposed change that cannot name a governing definition from the table above SHALL be treated as a non-normative drafting note or candidate intake and SHALL NOT be relied upon as an FPF architectural commitment. Such material may exist only in an explicitly marked non-normative source note until assigned to its governing definition.

#### E.20:4.3 - Step 3: Resolve the designator before dependent use

When a change introduces `MechanismDefinitionRef`, create one resolvable target at the subject-pattern locus before another declaration cites it. Distinguish two target states:

1. **Reference-reservation stub.** This is a draft authoring episteme, not `U.Mechanism`. It reserves the designator, names the intended operation-family EntityOfConcern, cites the subject pattern, and lists the missing A.6.1 identity or content needed for introduction. A publication may expose the stub as a candidate. A suite may cite it only in an explicitly candidate-valued position; the stub cannot satisfy admitted suite membership, closure, planned-baseline, wiring, gate, reuse, or import claims.
2. **Introduced mechanism episteme.** `MechanismDefinitionRef` resolves to one A.6.1 `U.Mechanism` episteme with recoverable identity and sufficient content for the receiving use. Only this state can fill a position whose ValueKind is `U.Mechanism`.

A card, table row, file, or register entry may publish either state. Its layout and publication identity do not determine which state obtains.

#### E.20:4.4 - Step 4: Complete mechanism semantics

An introduced mechanism has the A.6.1 identity tuple:

```text
<content, EntityOfConcernRef, effectiveReferenceScheme>
```

Its minimum semantic content for ordinary reuse names:

* direct `SubjectKind` and `RangedValueKind`, with `ResultKind`, `SliceSet`, and `ExtentRule` only when current;
* `OperationAlgebra` with one exact A.6.1 `OperationDeclaration` per reused operation and one declaration-local `ArgumentDeclaration` or `ResultDeclaration` for every typed argument or result position, including its meaning, exact ValueKind, binding designation rule, binding predicate, and any semantic cardinality;
* `LawSet`;
* `AdmissibilityConditions`;
* Applicability through exact claim scope, selected time, reference plane when current, and mechanism-specific conditions;
* `SignatureManifest` only when actual imported or provided declaration content must replay.

An operation index may be derived from the declaration-local operation designators for retrieval; it is not another content group. Argument and result declarations remain inside their exact A.6.1 operation declaration and never become A.6.5 SlotSpecs. Refinement, conservative extension, equivalence, bridge use, mechanism realization, evaluation, evidence use, method use, dated work, description, representation, and publication remain neighboring objects or relation occurrences. A MIP-run names their subject patterns instead of copying them into the mechanism declaration.

Create a new semantic edition when content, `EntityOfConcernRef`, or effective reference scheme changes. Keep the current edition when only a neighboring relation occurrence or publication changes. E.20 relies on the current numbered A.6.1 conformance checklist and does not maintain a second checklist-ID family.

If a suite or family claims shared operation-member vocabulary across several mechanism declarations, apply E.20:4.5.

#### E.20:4.5 - Step 5: Suite-scoped operation-member vocabulary discipline (prevent member-name drift)

Use this step only when a suite or family claims that several mechanism declarations intentionally share operation, argument, or result vocabulary. Repeated spelling by itself does not establish that claim.

1. The suite-subject pattern SHALL name one citeable vocabulary locus and the exact member mechanism declarations to which the shared terms apply. That vocabulary coordinates names only; it creates no `OperationDeclaration`, `ArgumentDeclaration`, `ResultDeclaration`, ValueKind, binding predicate, or actual binding.

2. Each member mechanism SHALL still declare every current operation, argument, and result locally under A.6.1, including its exact meaning, ValueKind, designation rule, binding predicate, and cardinality. A cited shared term or equal spelling imports none of those semantics.
3. When a public shared term is introduced, renamed, split, or merged, update the shared vocabulary locus and every affected declaration or alias route. When only one declaration changes meaning, keep the change local unless the intended shared denotation also changes. Apply E.20:4.9 whenever citeability changes.

This step prevents one intended suite term from silently fragmenting while preserving the declaration-local semantics of every A.6.1 operation member. It supplies no operation position and no actual application binding.

#### E.20:4.6 - Step 6: Suite integration (if the mechanism is a suite member)

If the introduction changes a suite (`MechSuiteDescription` or specialization):

1. **Membership set semantics (WF‑MS‑1).** `mechanisms` is a set: duplicates are nonconformant and list order carries no semantics.
2. **Ordering is only in protocols.** If ordering matters, express it only in `suite_protocols`.
3. **Protocol closure (WF‑MS‑2).** If `suite_protocols` is present, then for every `ProtocolStep` in every `SuiteProtocol`, `step.mechanism ∈ mechanisms`.
4. **No hidden tails.** Required stages (e.g., normalization/aggregation/Γ‑fold) are explicit protocol steps; do not hide them inside other steps.
5. **Guard/gate separation.** Suites and mechanisms SHALL NOT publish `GateDecision`/`DecisionLog`. `AdmissibilityConditions` and tri‑state `GuardDecision` remain governed by the mechanism definition; `OperationalGate(profile)` acceptance thresholds and pass/fail criteria remain gate/acceptance concerns.
6. **Suite is descriptive only (WF-MS-3/4).** A suite states membership, obligations, pins, and suite protocols. It does not restate `U.Mechanism` identity-bearing content. Any publication or telemetry continuation remains outside the suite protocol and requires its own exact publication or flow assertion and predicate.

**Kernel stability rule (recommended).** If the suite is a kernel suite, and the change adds a new required stage, prefer creating a **suite variant** rather than mutating the kernel membership. If mutation is unavoidable, pair it with terminology continuity (E.20:4.9) and RSCR triggers (E.20:4.10).

#### E.20:4.7 - Step 7: Planned baseline & P2W planning-to-work boundary (if planning changes)

If the mechanism introduction changes what one exact `U.WorkPlan` pins, such as selected comparator specifications, method descriptions, a time selector, or guard pins, the WorkPlan edition is the identifiable planning object.

1. Introduce or revise the `SlotFillingsPlanItem` rows as declaration-local ClaimGraph content inside that exact WorkPlan. Each row points to a declaration member whose own pattern defines its meaning and later actual-use rule.
2. Give no row an independent kind, record identity, edition, specialization lineage, canonical target, or successor relation. Changing identity-bearing row content changes the WorkPlan's claim content and is handled as a WorkPlan-edition change under C.2.1 and A.15.2.
3. Keep the declaration-local planned-filling content planning-only:
   * pins and references only, whether ByValue or through the declared reference kind;
   * no launch values;
   * no `FinalizeLaunchValues` witnesses;
   * no gate decisions or decision logs; and
   * explicit time through `Γ_time_selector` or `Γ_time_rule_ref` (XOR); implicit “latest” or “current” wording is nonconformant.
4. In this mechanism-baseline branch, the WorkPlan's planned-filling content SHALL target exactly one **Description-scoped, edition-addressable** slot-bearing description through `target_slot_bearing_description_ref`, typically a kit or suite. It SHALL NOT target a `MechanismDefinitionRef`. If a standalone mechanism baseline is needed, introduce an explicit Description-scoped slot-bearing description wrapper, such as a mechanism kit or suite-of-one, and target that.
5. When a receiver needs one row, cite it only through the exact WorkPlan edition and a stable local-content locator. The locator does not make the row independently resolvable.

This step keeps the P2W planning-to-work boundary crisp: the WorkPlan states **planned fillers**; enactment witnesses **actual runs**.

#### E.20:4.8 - Step 8: Wiring & SoTA updates (keep method evolution out of kernel)

If the introduction involves methods, comparators, selectors, or other SoTA-sensitive choices:

1. Put method/comparator family semantics in **SoTA packs** (G.2) and reference them by edition-pinned refs.
2. Pin the chosen SoTA refs in declaration-local rows inside the exact WorkPlan (E.20:4.7); wiring consumes those planned values rather than silently overriding them.
3. Put flow/task binding logic in **wiring modules** (`GPatternExtension`), with an explicit `PatternScopeId` and declared subject pattern.
4. Wiring may bind, select, dispatch, or cite SoTA method packs; it may not redefine the mechanism's identity-bearing A.6.1 content. A bridge, realization, evaluation, evidence-use, or publication claim named by wiring remains governed by its direct relation pattern.
5. If a SoTA update changes a mechanism's signature/laws, that semantic change SHALL be performed in the mechanism-subject pattern, under the A.6.1 mechanism-definition template; the change SHALL emit RSCR triggers (E.20:4.10).

#### E.20:4.9 - Step 9: Terminology continuity (alias docking)

If the introduction renames any public token or changes canonical naming:

1. Use lexical alias docking (F.18) so old tokens remain citeable.
2. Update registers and twin labels per lexical discipline.
3. Avoid silent rewrites: the MIP-run SHALL make the alias relation and successor relation explicit.

#### E.20:4.9.1 - Deprecation / supersession / retirement (preserve citeability)

If the change class includes deprecation, supersession, or retirement (E.20:4.1 #8), the MIP-run SHALL preserve reference continuity while making the status change explicit:

1. **Preserve each identifiable target.** A deprecated `U.Mechanism` episteme, reference-reservation stub, suite description, exact WorkPlan edition, or wiring module SHALL remain resolvable at its canonical location. Deprecation MUST NOT remove it and break citations. A declaration-local planned-filling row is not another canonical target.
2. **Keep the public token citeable.** A deprecated token such as a `MechanismDefinitionRef`, suite token, WorkPlan token, public local-content locator, or wiring token SHALL remain citeable. If a successor token or name is introduced, alias-dock the old token under F.18 (E.20:4.9). A local-content locator still resolves only through its exact WorkPlan edition and creates no independent row identity or edition.
3. **Declare a successor or state that none is current.** Apply that obligation to the deprecated mechanism episteme, reference-reservation stub, suite description, WorkPlan edition, wiring module, public locator, or alias under its direct supersession or deprecation pattern. A changed planned-filling row contributes to changed WorkPlan claim content; it has no separate successor relation.
4. **Update the definition that owns each change.** Make each needed change to suite denotation, closure, obligation, pin, protocol semantics, WorkPlan content, or wiring semantics at its definition locus in E.20:4.2. Prefer a suite variant to silently swapping kernel membership.
5. **Emit RSCR triggers.** Deprecation or supersession SHALL emit typed RSCR triggers and extend the regression envelope (E.20:4.10), including checks for dangling references and alias coverage.

#### E.20:4.10 - Step 10: RSCR triggers + regression envelope

A MIP-run that changes any of:
* mechanism signatures,
* suite membership/protocols,
* planned baseline pins,
* shared operation-member vocabulary or declaration-local operation, argument, or result designators,
* terminology/alias docking that changes citeable tokens,
* or other reference loci

SHALL emit typed RSCR triggers via the RSCR subject pattern and SHALL extend the regression envelope to include, at minimum:

* no dangling `MechanismDefinitionRef` enumerations,
* suite membership set semantics + protocol closure,
* guard/gate separation preservation,
* P2W planning-to-work boundary preservation (planning vs enactment).

**Guard (normative).** Trigger kind identifiers (e.g., `RSCRTriggerKindId`) SHALL be selected from the RSCR trigger catalogue governed by `G.Core`. A MIP-run SHALL NOT mint ad hoc trigger kinds (“reason kinds”) scattered in arbitrary patterns/modules.

**Manifest hook (recommended).** The MIP-run manifest SHOULD list emitted trigger types and the regression envelope deltas as checkable items.

#### E.20:4.11 - Step 11: Apply PQG profiles (E.19) and close the run

Every MIP-run SHALL be reviewed using PQG (E.19) with:

* **PCP‑BASE** always, and
* the triggered profiles implied by the change class (at least):
  * **PCP‑SUITE** if any suite locus changed,
  * **PCP‑P2W** if any planned-baseline locus changed,
  * **PCP‑TERM** if any new terms/renames are introduced,
  * **PCP‑SOTA** if SoTA packs are introduced/modified,
  * **PCP‑NORM** if the run introduces/changes normative requirements or conformance items,
  * **PCP‑DEONT** if RFC keyword clauses are introduced/modified (or if invariant/predicate vs deontic form is ambiguous),
  * **PCP‑BRIDGE** if cross-context reuse, crossings, or bridges are introduced or changed,
  * **PCP‑REFRESH** if refresh-sensitive claims (SoTA lists, “current practice”, enumerations) are touched,
  * plus any applicable modularity / boundary / normativity profiles required by the delta.

**MIP-run outcomes (normative set).**
A reviewed MIP-run SHALL be closed as one of:

1. **Proceed (single change set).**
2. **Proceed via governing-definition split** (mandatory when semantics were placed under the wrong governing definition; the change is split into governing-definition-correct edits).
3. **Proceed via suite variant** (preferred when kernel stability is threatened by adding new required stages).
4. **Block with explicit missing condition** (insufficient semantics; stub exists but completion condition is DRR-tracked).
5. **Reject** (violates invariants such as suite-as-gate, plan-as-enactment, or governing-definition ambiguity).

