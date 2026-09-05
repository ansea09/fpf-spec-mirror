---
chunk_kind: "child"
pattern_id: "C.23"
pattern_title: "MethodFamily Evidence & Maturity (Method‑SoS‑LOG)"
section_id: "C.23:4"
section_title: "Solution — Method‑SoS‑LOG: deductive shells over Eligibility & Evidence"
source_path: "FPF-Spec.md"
output_path: "by_section/C.23/C.23__005_solution-method-sos-log-deductive-shells-over-eligibility-evidence.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "C.23 — MethodFamily Evidence & Maturity (Method‑SoS‑LOG)"
  - "C.23:4 — Solution — Method‑SoS‑LOG: deductive shells over Eligibility & Evidence"
line_start: 53177
line_end: 53264
dependencies:
  - "A.10"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.22"
  - "E.10"
  - "E.18"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.8"
  - "G.9"
keywords:
  - "MethodFamily"
  - "SoS-LOG"
  - "abstain"
  - "admit"
  - "degrade"
  - "evidence"
  - "maturity"
  - "selector"
---

### C.23:4 - Solution — **Method‑SoS‑LOG**: deductive shells over Eligibility & Evidence

#### C.23:4.1 - Objects & heads (LEX/I‑D‑S)

*Tech heads; Plain twins are published via UTS.*
**`MethodFamily`** (registered in G.5) carries **Eligibility** and artefact identity; **`MaturityCard`** (this pattern) carries evidence‑aware maturity; **`SoS‑LOG.Rule`** (this pattern) is an executable rule schema; evaluating a rule returns one of `{Admit | Degrade(mode) | Abstain}` for a `(TaskSignature, MethodFamily)` pair. A qualifying description episteme uses `…Description`; `…Spec` names that same episteme only after the E.10.D2 specification-use gate grants the named use.

#### C.23:4.2 - Rule schema (normative)

For each `MethodFamily` **f**, author an **executable** rule set:

```
LOG.Deduce_f(TaskSignature S2) → {Admit | Degrade(mode) | Abstain}
```

with the following **branch obligations**:

**R0 — CG-Spec gate (precondition).** For the exact G.5 registry row and `MethodFamily`, verify the cited `CG-Spec.MinimalEvidence` and EvidenceProfile for every CHR characteristic used by the family's acceptance clauses and flows, under the declared claim scope and selected slices, qualification window, and intended selector use. Failure ⇒ `Abstain` with reasons. Publish the consulted CG-Spec, EvidenceProfile, registry, and policy editions.
*Rationale:* selector legality requires the CG‑Spec gate to be explicit, not implicit in prose. Publish associated **ReferencePlane** notes alongside the consulted ids.

**R0.QD — QD/OEE pre‑gates (if applicable).** If S2 declares **CharacteristicSpaceRef/ArchiveConfig/EmitterPolicyRef** or `PortfolioMode=Archive`, verify:
(i) **CharacteristicSpaceRef** characteristics are CHR‑typed, d≥2, **ReferencePlane** per characteristic declared;
(ii) **ArchiveConfig** is lawful (topology, resolution, **K**>0, `InsertionPolicyRef`, `DistanceDef` with **edition id** and declared metric/pseudometric status);
(iii) **EmitterPolicyRef** present (with **edition id**);
 (iv) resolve **DominanceRegime**; if absent, use **default= ParetoOnly**.
 Failure of any ⇒ `Abstain` with reasons.

**R1 — Admit.** `Admit` **IFF**
(a) S2 satisfies **Eligibility** predicates of *f* (tri‑state aware),
(b) the exact **EvidenceProfile minima** referenced by Acceptance/Flows for *f* are met for the declared claim scope and selected slices, qualification window, and intended selector use (post R0),
(c) all relevant **CAL.AcceptanceClauses** (G.4) evaluate to true under lawful CHR comparisons,
(d) any **maturity gating** (e.g., a floor on Maturity rungs) is expressed as an **AcceptanceClause** and referenced here by id (no acceptance thresholds inside LOG).
*LOG never sets acceptance thresholds; its rules use and cite Acceptance verdicts.*

**R2 — Degrade.** If (a) holds but (b) or (c) is **partially** satisfied or **unknown**, return `Degrade(mode)` where `mode ∈ {scope-narrow | sandbox | probe-only}`. Record the exact S2 unknowns or evidence minima, narrowed claim scope or execution mode, qualification window, governing policy edition, and result. LOG-Degrade never changes CHR scales or planes.
**Note (CAL vs LOG).** CAL‑level **`degrade.order`** (fall‑back to order‑only comparisons) is governed by **G.4**/**CG‑Spec** and is **not** a LOG mode. **SoS‑LOG never overrides CAL outcomes**; a LOG branch **only narrows** `Scope(G)` or **execution mode** (e.g., `sandbox`, `probe‑only`), it **does not** alter CHR scales or admissible orders.
`probe‑only` MUST cite an **E/E‑LOG policy id** (exploration budget) and Acceptance‑bound guards.

**R3 — Abstain.** If S2 violates **Eligibility** or R0 fails, return `Abstain` with the failed rule, policy edition, evidence profile, claim scope, qualification window, and reasons. Abstain is mandatory for illegal CHR operations and when a conclusion depends on an F.9 Bridge, kind relation, or plane relation that has not been established.

**R4 — Relation and loss routing.** Cite an F.9 Bridge, kind relation, or plane relation only when the admission decision actually relies on that obtaining relation. Record its participants, direction, what meaning is preserved and what is lost, receiving use, and applicable policy edition. When the admission use makes a separate named assurance claim, identify its exact target claim and receiving use under B.3. Apply a supported loss penalty only under that assurance policy's declared rule; route it to `R_eff` only, leaving `F` and `G` unchanged. A changed registry row, evidence profile, claim scope, qualification window, or intended use is not by itself a crossing.

**R5 — Proof hooks.** Every branch **MUST** cite **Evidence Graph Ref** (A.10), the lane tags (TA/VA/LA) and freshness windows required by its cited CG-Spec.MinimalEvidence and EvidenceProfile, and **Bridge ids + loss notes** when the branch relies on a Bridge; the decision is **SCR‑visible**. When **G.6 EvidenceGraph** is present, also **publish EvidenceGraph path id(s)** for the branch (admit/degrade/abstain). **A branch verdict is not its own evidence basis**.

**R6 — QD archive / PortfolioMode semantics (if applicable).** If `PortfolioMode=Archive`, G.5 selection after `Admit` may return a **QD archive** (per `ArchiveConfig`) instead of only a Pareto set. Unless **CAL** authorises `DominanceRegime=ParetoPlusIllumination` (**policy‑id recorded in SCR**), **IlluminationSummary** is a **report‑only telemetry summary** and any **coverage/regret** are **telemetry metrics** (reported) that **do not** affect dominance.

**R7 — GeneratorFamily branches (open‑ended).** If S2 includes `GeneratorIntent`, SoS‑LOG **MUST**:
 (i) verify **`EnvironmentValidityRegion`** is declared and lawful;
 (ii) verify **`TransferRulesRef`** exists; if `unknown` ⇒ `Degrade(scope‑narrow)` or `Abstain` per family policy;
 (iii) treat the selection surface as **pairs `{environment, method}`**; publish **coverage/regret** and **IlluminationSummary** as **report‑only telemetry** (IlluminationSummary = telemetry summary; coverage/regret = telemetry metrics); dominance participation per **R6**.

**R8 — Telemetry & Refresh hooks.** On any illumination increase or archive change, publish the current editions and any actual **edition increments** for **CharacteristicSpaceRef**/**DistanceDefRef**/**EmitterPolicyRef** and the applicable **policy‑id** (Emitter/Acceptance); expose **PathSliceId** for refresh/decay in SCR only when an E.18 path slice is current.

> *Aphorism.* **“Admit on admissibility and sufficiency; degrade on uncertainty; abstain on inadmissibility.”**

#### C.23:4.3 - Maturity ladder (poset, not a scalar; Description, not Spec)

Publish one editioned **`MaturityCardDescription`** for the exact evaluated `MethodFamily`, G.5 registry edition, evidence profile, claim scope and selected slices, qualification window, and intended admission use (UTS enum ids; scale kind = ordinal; reference plane declared). Do not embed acceptance thresholds here; an admission floor remains a G.4 AcceptanceClause cited by R1.

* **L0 — Anecdotal.** Claims exist; lanes sparse; examples ad‑hoc.
* **L1 — Worked‑Examples.** Multiple **worked examples** with lane tags and **Scope slices** declared; *no replication yet*.
* **L2 — Replicated.** Independent replications identify their distinct bearers or operating conditions and declare the claim scope and selected slices, source and method editions, and qualification windows used; lane separation is observed and decay windows are explicit.
* **L3 — Benchmark‑Severe.** Repeated wins or parity on **community baselines** or **severe tests**; cross‑Tradition bridges declared with **loss notes**.

*Optional rung (for QD/OEE‑heavy families; ordinal, closed enum):*
* **L4 — QD‑Hardened.** Archive stability under declared **InsertionPolicy/DistanceDef** editions; reproducible **IlluminationSummary** improvements under controlled budgets; OEE generators pass **EnvironmentValidityRegion** severe tests.

**Norms.**
**M1.** The ladder is **lane‑aware** (TA/VA/LA) and **freshness‑aware**; it is **not** a global numeric score. Declare **Scale kind=ordinal** and the **closed enumeration** of rungs; register the enum at **UTS** (twin labels; editioned).
**M2.** Transitions **MUST** be justified by **EvidenceGraph** paths (once G.6 is available) and published at UTS; missing anchors ⇒ no advance.
**M3.** Any maturity floor used for admission—for example, a run-critical selector use requiring at least L2—MUST be authored as a CAL.AcceptanceClause and cited by R1 with its policy edition, claim scope, qualification window, and verdict; SoS-LOG does not embed acceptance thresholds.
**M4.** Declare the MaturityCard reference plane. If an admission decision relies on a relation to another plane, cite that exact obtaining plane relation, its direction and loss, and the applicable policy edition; a supported loss penalty selected under R4 affects `R_eff` only.

> *Rationale note.* Treating maturity as a **poset** aligns with B.3's requirement for lawful comparisons and avoids **scalarisation across ordinal/ratio** scales; assurance penalties selected under R4 affect **`R_eff`**, never **F/G**.

#### C.23:4.4 - Unknowns & Shift classes (tri‑state discipline)

**U1. (LEX).** Enumerations for `Degrade(mode)` and Maturity rungs **MUST** be declared as **closed value sets** and **registered at UTS** (twin labels). **Lexical SD** (**E.10**) applies.
**U2.** A live S2 characteristic or predicate admits `unknown` only when its C.22 value rule permits it; `unknown` **MUST** map to a branch (`Degrade` or `Abstain`) declared on the **family** (no coercions). Each branch publishes a **branch‑id** and (where used) a `mode` from a **closed enum** registered at **UTS** (LEX enum clarity).
**U3.** `ShiftClass` semantics follow **C.22**. If `ShiftClass ∈ {covariate‑shift, concept‑drift, adversarial}` or `unknown`, default outcome is `Degrade(scope‑narrow)` unless a CAL.AcceptanceClause explicitly guards the regime.

#### C.23:4.5 - Publication & wiring

**W1.** For each evaluated `MethodFamily`, publish an editioned `MaturityCardDescription` naming the registry edition, evidence profile, claim scope, qualification window, reference plane, and intended admission use; register the SoS-LOG rule ids. RSCR tests cover `Admit`, `Degrade`, `Abstain`, and unknown paths. Relation and loss-policy ids appear only where a branch actually relies on them.
**W2. Admissibility Ledger.** Publish an editioned `AdmissibilityLedger`: each selector-facing row names the exact `MethodFamilyId`, G.5 registry edition, RuleId and rule edition, MaturityRung, EvidenceProfile, claim scope, qualification window, BranchIds, AcceptanceClause and policy ids, decision result, evidence paths, DominanceRegime, PortfolioMode, and any obtaining relation and loss-policy ids actually used. UTS registers the row vocabulary; the ledger records the admission result and its basis.
**W3. Strategy composition.** For a selection composition called a strategy, cite its governing G.5 rule and **E/E-LOG** policy.
**W4.** Selector (G.5) **consumes** these rules; results appear in the **Dispatcher Report** with reasons in/out and cited anchors/bridges.

