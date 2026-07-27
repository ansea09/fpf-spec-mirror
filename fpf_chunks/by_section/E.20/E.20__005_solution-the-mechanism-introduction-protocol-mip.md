---
chunk_kind: "child"
pattern_id: "E.20"
pattern_title: "Mechanism Introduction Protocol"
section_id: "E.20:4"
section_title: "Solution — the Mechanism Introduction Protocol (MIP)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.20/E.20__005_solution-the-mechanism-introduction-protocol-mip.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "E.20 — Mechanism Introduction Protocol"
  - "E.20:4 — Solution — the Mechanism Introduction Protocol (MIP)"
line_start: 83695
line_end: 83924
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
* `U.Mechanism` definition cards and `MechanismDefinitionRef`, suite descriptions (`MechSuiteDescription` and specializations), WorkPlanning plan items (`SlotFillingsPlanItem` and specializations), alias docking (F.18), RSCR triggers (G.Core), and PQG profiles (E.19).

#### E.20:4.1 - Step 1: Classify the introduction

A MIP-run SHALL first classify the change, because different classes have different governing definitions:

1. **New mechanism family, species, or archetypal grounding** (new `U.Mechanism` archetypal definition).
2. **New mechanism definition within an existing A.6.1 mechanism kind** (new `MechanismDefinitionRef`, new canonical card).
3. **Mechanism revision** (signature/laws/slots/transport/audit semantics change).
4. **Suite change** (membership, obligations, spec pins, suite protocols, suite audit obligations).
5. **Planned-baseline change** (new or revised `SlotFillingsPlanItem` specialization, or changes to its pins).
6. **Wiring change** (new or revised Part‑G extension modules, SoTA method packs, selectors).
7. **Terminology migration** (renames, token splits/merges, register changes).
8. **Deprecation / supersession / retirement** (marking mechanisms/suites/plan items as deprecated, declaring successors, and preserving citeability; apply E.20:4.9.1).

**Mechanism kind boundary.** A MIP-run may introduce a new `MechanismDefinitionRef`. It does not introduce a new `E.18` transformation-flow locus kind or transformation-flow structure unless `E.18` is explicitly updated, and it does not introduce a new C.3 `U.Kind` unless C.3 and `A.6.5` discipline is the current governing question.

**A.6.1 compatibility.** MIP assigns mechanism meaning to A.6.1-governed mechanism definitions: operation algebra, law set, admissibility conditions, `SlotIndex`, per-operation `SlotSpec`s with required input and output `SlotKind`s, transport or bridge regime, applicability, audit, and monotone realization relation when declared. Suites, planned-baseline records, and Part-G wiring modules may cite or bind that meaning; they do not supply or redefine it.

**New mechanism-family criterion.** Treat a change as a new mechanism family, species, or archetypal grounding only when the existing mechanism-governing pattern cannot express the operation algebra, law set, admissibility conditions, `SlotIndex`, per-operation `SlotSpec`s, required input/output `SlotKind`s, transport boundary, audit semantics, or monotone realization relation when declared without changing its kind invariants. Otherwise classify the change as a new mechanism definition or `MechanismDefinitionRef` within an existing A.6.1 mechanism kind.

A single MIP-run MAY span multiple classes, but SHALL treat each class with its correct governing-definition assignment (below).

#### E.20:4.2 - Step 2: Declare the governing-definition assignment map (mandatory)

For every new or modified change item, the MIP-run SHALL name **exactly one governing definition** and assign the change there. In FPF, that governing definition is a citeable, patchable `PatternId`, `PatternId:SectionPath`, `PatternScopeId = G.x:Ext.*`, or `DRRId` (E.9). The core MIP-run manifest in a citeable change record is limited to:

* each changed item,
* its governing definition,
* its canonical location (expressed as `PatternId:SectionPath`, `PatternScopeId`, or `DRRId`, not as prose), and
* the forbidden overread or forbidden move blocked by that assignment.

Conditional manifest fields appear only when the corresponding claim is present:

* the change class(es) from E.20:4.1 when needed to disambiguate the assignment,
* new or changed citeable tokens (`MechanismDefinitionRef`, `SlotKind` tokens, `PatternScopeId`, etc.) when token denotation or citeability changes,
* the best-known Delta-Class (`Δ-0` to `Δ-3`) and impact radius estimate (E.15) when the run is plausibly `Δ-2` or `Δ-3`,
* intended RSCR trigger types when a refresh or regression-wiring claim is present, and
* the PQG (E.19) profile set when the run crosses an E.19-governed review boundary.

**Note (normative).** If the canonical location is a Part‑G wiring module, it SHALL be cited as a `PatternScopeId` (`G.x:Ext.*`) and the module SHALL declare `GoverningPatternId` (wiring is binding-only; meaning remains governed by its cited pattern).

**Canonical governing-definition map (normative):**

| Change kind | Governing definition | Canonical location | Forbidden move |
|---|---|---|---|
| Mechanism meaning (operations, laws, invariants, admissibility, `SlotIndex`, required input/output `SlotKind`s, per-operation `SlotSpec`s, transport, audit semantics, and monotone realization relation when declared) | **Mechanism-governing pattern** | Designated mechanism-governing pattern | SHALL NOT “define” the mechanism inside a suite or a wiring module. |
| Suite membership, obligations, spec pins, and suite protocols | **Suite-governing pattern** | `A.6.7` or `A.6.7.<FamilyKey>` | SHALL NOT carry mechanism semantics, acceptance thresholds, gate criteria, DecisionLogs, or publication tails into the suite. |
| Planned baseline pins (planned slot fillings, edition-pinned refs, explicit time selector) | **WorkPlanning governing pattern** | `A.15.3` plus suite-specific specialization when needed | SHALL NOT embed launch values, witnesses, or gate decisions in planning. |
| SoTA method, comparator, or generator **definitions**, including provenance and evaluation semantics | **SoTA-pack governing pattern** | `G.2` (SoTA synthesis packs) | SHALL NOT rephrase SoTA evolution as kernel semantics. |
| Wiring that binds SoTA packs into flows or tasks | **Extension module governing definition** | `G.x:Ext.*` (`GPatternExtension` with explicit `PatternScopeId`) | SHALL NOT mint new semantics; SHALL bind only. |
| Token renames and drift management | **Lexical governing pattern** | `F.18` (alias docking) plus registers per E.10/F.17 | SHALL NOT silently rewrite tokens or break citations. |
| Change-cause taxonomy and regression triggers | **RSCR governing pattern** | `G.Core` | SHALL NOT invent ad hoc “reason kinds” scattered in patterns. |
| Project specializations of a mechanism | **Project specialization pattern** | `P.*` patterns (using `⊑/⊑⁺`) | SHALL NOT mutate kernel membership to express project variants. |

**Guard (normative).** Any proposed change that cannot name a governing definition from the table above SHALL be treated as a non-normative drafting note or candidate intake and SHALL NOT be relied upon as an FPF architectural commitment. Such material may exist only in an explicitly marked non-normative source note until assigned to its governing definition.

#### E.20:4.3 - Step 3: Card-first canonicalization (eliminate dangling refs)

If the introduction adds a new `MechanismDefinitionRef` anywhere (especially inside a suite):

1. The MIP-run SHALL first create a **canonical mechanism card** at the governing pattern location that publishes the `MechanismDefinitionRef` and the minimal identity fields (names, intent, and "this is a distinct mechanism").
2. The card MAY be a **stub** initially, but SHALL reserve:
  * the stable `MechanismDefinitionRef` (and its lexical register entry per E.10/F.17),
   * the intended mechanism family or species placement,
 and
  * a DRR pointer for completing semantics (including any missing register/twin-label work).

Only after (1) is in place MAY suites or protocols enumerate the new `MechanismDefinitionRef`.

#### E.20:4.4 - Step 4: Mechanism semantics completion (what “done” means)

**Definition-of-done note (delegated).** MIP uses two completion checkpoints for mechanism cards:

* **Stub done** - a citeability stub for a `MechanismDefinitionRef`: a resolvable canonical target created only to prevent dangling references (E.20:4.3), not semantic completion.

 A stub **SHALL** (i) exist at the mechanism-governing pattern's canonical location, (ii) reserve and publish the stable `MechanismDefinitionRef` (and its lexical/register entries), (iii) set `MechanismDefinitionHeader.status = draft`, and (iv) carry an explicit DRR pointer for completing semantics. A stub **SHALL** also list the *A.6.1* conformance checklist item IDs it does **not** yet satisfy (without duplicating that checklist here). A stub may preserve citeability for suite or protocol enumeration, but it does not authorize suite closure, gate checks, planned baselines, wiring consumption, reuse, or import unless the fields required for that use are present and marked current.

* **Introduced done** - a mechanism card that can be relied upon as a `U.Mechanism` definition. "Introduced done" is defined by *A.6.1* conformance: the card **SHALL** satisfy the applicable *A.6.1:7 Conformance Checklist* items (**CC-UM.\***), with the baseline items designated by *A.6.1* (e.g., **CC-UM.0** and **CC-UM.1**) being the minimum requirement.

The list below is **informative** only (semantic orientation); the normative structure and “done” criteria are delegated to *A.6.1*’s CC items to avoid drift between this protocol and the canonical mechanism definition.

For an “introduced” mechanism beyond a stub, the useful completion target is to make the following semantic fields explicit:

* **Operation field**: the named operations that the mechanism provides (signature-scoped intent).
* **Law/invariant field**: the invariants that govern the operations, including admissibility constraints when applicable.
* **Admissibility field**: preconditions or eligibility predicates for admissible operation (not a gate decision log, and not per-run outcomes).
* **Slot discipline**: `SlotIndex`, required input and output `SlotKind`s, per-operation `SlotSpec`s, stable `ValueKind`s, and explicit ref modes.
* **Specialisation discipline (when `⊑/⊑⁺` is declared):** explicit parent+morphism kind; SlotKind invariance; monotone ValueKind narrowing; no new mandatory inputs to inherited operations (per A.6.1:4.2.1 / CC‑UM.8).
* **Transport and realization discipline**: declarative transport semantics with no hidden crossings; when a realization relation is declared, it is monotone against the mechanism declaration and may tighten laws or guards but must not relax them.
* **Audit obligations**: which evidence references are required when the mechanism is used.

If the mechanism introduces new slot kinds shared across a family/suite, apply E.20:4.5.

#### E.20:4.5 - Step 5: Suite-scoped slot-token lexicon discipline (prevent slot drift)

If the mechanism belongs to a suite or family where multiple member mechanisms share slot vocabulary:

1. The suite-governing pattern SHALL provide a **suite-scoped slot-token lexicon** referencing `A.6.5` SlotSpecs (or update it if already present) in the suite-governing pattern's canonical location (`A.6.7` / `A.6.7.<FamilyKey>`), or as a dedicated lexicon card explicitly referenced from there. The lexicon cites and organizes SlotKind tokens; it does not create new SlotKind semantics.

2. Mechanism cards SHALL cite slot kinds from that lexicon (rather than minting local near-duplicates).
3. New slot kinds SHALL be introduced into the lexicon first, then referenced by member mechanisms. If any citeable `SlotKind` tokens are minted/renamed, apply E.20:4.9.

This step is specifically intended to prevent the “same idea, different slot token” drift that makes planned baselines and audits non‑portable.

#### E.20:4.6 - Step 6: Suite integration (if the mechanism is a suite member)

If the introduction changes a suite (`MechSuiteDescription` or specialization):

1. **Membership set semantics (WF‑MS‑1).** `mechanisms` is a set: duplicates are nonconformant and list order carries no semantics.
2. **Ordering is only in protocols.** If ordering matters, express it only in `suite_protocols`.
3. **Protocol closure (WF‑MS‑2).** If `suite_protocols` is present, then for every `ProtocolStep` in every `SuiteProtocol`, `step.mechanism ∈ mechanisms`.
4. **No hidden tails.** Required stages (e.g., normalization/aggregation/Γ‑fold) are explicit protocol steps; do not hide them inside other steps.
5. **Guard/gate separation.** Suites and mechanisms SHALL NOT publish `GateDecision`/`DecisionLog`. `AdmissibilityConditions` and tri‑state `GuardDecision` remain governed by the mechanism definition; `OperationalGate(profile)` acceptance thresholds and pass/fail criteria remain gate/acceptance concerns.
6. **Suite is descriptive only (WF‑MS‑3/4).** Any publish/telemetry continuation is outside the suite protocol and terminates via publication faces, packs, or modules; suites SHALL NOT define mechanism blocks (`OperationAlgebra`, `LawSet`, `Transport`, `Audit`, …).

**Kernel stability rule (recommended).** If the suite is a kernel suite, and the change adds a new required stage, prefer creating a **suite variant** rather than mutating the kernel membership. If mutation is unavoidable, pair it with terminology continuity (E.20:4.9) and RSCR triggers (E.20:4.10).

#### E.20:4.7 - Step 7: Planned baseline & P2W planning-to-work boundary (if planning changes)

If the mechanism introduction changes what a WorkPlanning baseline pins (e.g., selected comparator specs, method descriptions, time selector, guard pins):

1. Introduce or revise a `SlotFillingsPlanItem` specialization under the WorkPlanning governing pattern.
2. The plan item SHALL remain planning-only:
   * pins/refs only (ByValue or `<RefKind>`),
   * no launch values,
   * no `FinalizeLaunchValues` witnesses,
   * no gate decisions or decision logs.
   * time is explicit: include `Γ_time_selector` or `Γ_time_rule_ref` (XOR); implicit “latest/current” is nonconformant.
3. The plan item SHALL target exactly one **Description-scoped, edition-addressable** slot-bearing description via `target_slot_bearing_description_ref` (typically a kit or suite) and SHALL NOT target a `MechanismDefinitionRef`. If a "standalone mechanism baseline" is needed, introduce an explicit Description-scoped slot-bearing description wrapper (e.g., a mech kit or a suite-of-one) and target that.

This step exists to keep the P2W planning-to-work boundary crisp: planning defines **planned fillers**, enactment witnesses **actual runs**.

#### E.20:4.8 - Step 8: Wiring & SoTA updates (keep method evolution out of kernel)

If the introduction involves methods, comparators, selectors, or other SoTA-sensitive choices:

1. Put method/comparator family semantics in **SoTA packs** (G.2) and reference them by edition-pinned refs.
2. Pin the chosen SoTA refs for a baseline in WorkPlanning plan items (E.20:4.7); wiring consumes pins rather than silently overriding them.
3. Put flow/task binding logic in **wiring modules** (`GPatternExtension`), with an explicit `PatternScopeId` and declared governing pattern.
4. Wiring may bind, select, dispatch, or cite SoTA method packs; it may not redefine the operation, law, admissibility, transport, slot, or audit meaning of the mechanism it wires.
5. If a SoTA update changes a mechanism's signature/laws, that semantic change SHALL be performed in the mechanism-governing pattern, under the A.6.1 mechanism-definition template; the change SHALL emit RSCR triggers (E.20:4.10).

#### E.20:4.9 - Step 9: Terminology continuity (alias docking)

If the introduction renames any public token or changes canonical naming:

1. Use lexical alias docking (F.18) so old tokens remain citeable.
2. Update registers and twin labels per lexical discipline.
3. Avoid silent rewrites: the MIP-run SHALL make the alias relation and successor relation explicit.

#### E.20:4.9.1 - Deprecation / supersession / retirement (preserve citeability)

If the change class includes deprecation/supersession/retirement (E.20:4.1 #8), the MIP-run SHALL preserve reference continuity while making the status change explicit:

1. **Preserve the canonical target.** The deprecated mechanism card, suite description, plan item, or wiring module SHALL remain resolvable at its canonical location; deprecation MUST NOT be implemented by removal that would break citations.
2. **Keep the public token citeable.** The deprecated token (`MechanismDefinitionRef`, suite token, plan-item token, etc.) SHALL remain citeable. If a successor token/name is introduced, the old token SHALL be alias-docked per F.18 (E.20:4.9).
3. **Declare successor (or “no successor”).** The deprecated mechanism card, suite description, plan item, or wiring module SHALL declare a successor pointer (or explicitly declare that there is none) using the project’s established deprecation/supersession fields.
4. **Assign downstream updates to governing definitions.** Any needed suite denotation, closure, obligation, pin, protocol-semantic, WorkPlanning-pin, or wiring-semantic change SHALL be performed in its respective governing definition (E.20:4.2), preferably by introducing a suite variant rather than silently swapping kernel membership.
5. **Emit RSCR triggers.** Deprecation/supersession SHALL emit typed RSCR triggers and extend the regression envelope (E.20:4.10), including checks for dangling refs and alias coverage.

#### E.20:4.10 - Step 10: RSCR triggers + regression envelope

A MIP-run that changes any of:
* mechanism signatures,
* suite membership/protocols,
* planned baseline pins,
* slot vocabulary / SlotKind lexicon,
* terminology/alias docking that changes citeable tokens,
* or other reference loci

SHALL emit typed RSCR triggers via the RSCR governing pattern and SHALL extend the regression envelope to include, at minimum:

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

