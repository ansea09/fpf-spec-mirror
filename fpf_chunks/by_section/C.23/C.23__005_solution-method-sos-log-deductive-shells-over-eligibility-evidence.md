---
chunk_kind: "child"
pattern_id: "C.23"
pattern_title: "MethodFamily Evidence & Maturity (Method‑SoS‑LOG)"
section_id: "C.23:4"
section_title: "Solution — Method‑SoS‑LOG: deductive shells over Eligibility & Evidence"
source_path: "FPF-Spec.md"
output_path: "by_section/C.23/C.23__005_solution-method-sos-log-deductive-shells-over-eligibility-evidence.md"
commit_sha: "2c16067fe8c7f34ea3313d66d36738870f5c2087"
heading_path:
  - "C.23 — MethodFamily Evidence & Maturity (Method‑SoS‑LOG)"
  - "C.23:4 — Solution — Method‑SoS‑LOG: deductive shells over Eligibility & Evidence"
line_start: 60775
line_end: 60883
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
  - "admission rules"
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

**R2 — Degrade.** Apply R0 and, when applicable, R0.QD before any degrade branch, including U2, U3, and R7. Failure returns `Abstain` for the attempted use. After those gates pass, return `Degrade(mode)` only through a declared family branch when an admitted unknown or an unmet acceptance condition permits a narrower scope or execution mode under the applicable CAL failure behavior; `mode ∈ {scope-narrow | sandbox | probe-only}`. An eligibility violation still requires R3 abstention. Record the exact S2 unknowns or unmet conditions, narrowed claim scope or execution mode, qualification window, governing policy edition, and result. If the branch changes the intended use, re-evaluate R0 and eligibility for that bounded use before relying on it. LOG-Degrade never changes CHR scales or planes or turns a failed CAL verdict into a pass.
**Note (CAL vs LOG).** CAL‑level **`degrade.order`** (fall‑back to order‑only comparisons) is governed by **G.4**/**CG‑Spec** and is **not** a LOG mode. **SoS‑LOG never overrides CAL outcomes**; a LOG branch **only narrows** `Scope(G)` or **execution mode** (e.g., `sandbox`, `probe‑only`), it **does not** alter CHR scales or admissible orders.
`probe‑only` MUST cite an **E/E‑LOG policy id** (exploration budget) and Acceptance‑bound guards.

**R3 — Abstain.** If S2 violates **Eligibility** or R0 fails, return `Abstain` with the failed rule, reasons, and available policy, evidence-profile, scope, and qualification-window basis. Report missing references and unperformed judgements under §4.2.1. Abstain is mandatory for illegal CHR operations and when a conclusion depends on an F.9 Bridge, kind relation, or plane relation that has not been established.

**R4 — Relation and loss routing.** Cite an F.9 Bridge, kind relation, or plane relation only when the admission decision actually relies on that obtaining relation. Record its participants, direction, what meaning is preserved and what is lost, receiving use, and applicable policy edition. When the admission use makes a separate named assurance claim, identify its exact target claim and receiving use under B.3. Apply a supported loss penalty only under that assurance policy's declared rule; route it to `R_eff` only, leaving `F` and `G` unchanged. A changed registry row, evidence profile, claim scope, qualification window, or intended use is not by itself a crossing.

**R5 — Proof hooks.** Every branch **MUST** retain its **A.10 evidence/source basis** for the conclusion it makes. For an early `Abstain`, cite the available basis for the failed prerequisite and name the required evidence that could not be recovered. Evidence used by a branch retains the lane tags (TA/VA/LA) and freshness windows required by its CG-Spec.MinimalEvidence and EvidenceProfile; missing requirements remain explicit gaps under §4.2.1. Cite **Bridge ids + loss notes** when the branch relies on a Bridge; the decision is **SCR‑visible**. When **G.6 EvidenceGraph** is present, also **publish EvidenceGraph path id(s)** for the branch (admit/degrade/abstain). **A branch verdict is not its own evidence basis**.

**R6 — QD archive / PortfolioMode semantics (if applicable).** If `PortfolioMode=Archive`, G.5 selection after `Admit` may return a **QD archive** (per `ArchiveConfig`) instead of only a Pareto set. Unless **CAL** authorises `DominanceRegime=ParetoPlusIllumination` (**policy‑id recorded in SCR**), **IlluminationSummary** is a **report‑only telemetry summary** and any **coverage/regret** are **telemetry metrics** (reported) that **do not** affect dominance.

**R7 — GeneratorFamily branches (open‑ended).** If S2 includes `GeneratorIntent`, SoS‑LOG **MUST**:
 (i) verify **`EnvironmentValidityRegion`** is declared and lawful;
 (ii) verify **`TransferRulesRef`** exists; if `unknown` ⇒ `Degrade(scope‑narrow)` or `Abstain` per family policy;
 (iii) treat the selection surface as **pairs `{environment, method}`**; publish **coverage/regret** and **IlluminationSummary** as **report‑only telemetry** (IlluminationSummary = telemetry summary; coverage/regret = telemetry metrics); dominance participation per **R6**.

**R8 — Telemetry & Refresh hooks.** On any illumination increase or archive change, publish the current editions and any actual **edition increments** for **CharacteristicSpaceRef**/**DistanceDefRef**/**EmitterPolicyRef** and the applicable **policy‑id** (Emitter/Acceptance); expose **PathSliceId** for refresh/decay in SCR only when an E.18 path slice is current.

> *Aphorism.* **“Admit on admissibility and sufficiency; degrade on uncertainty; abstain on inadmissibility.”**

##### C.23:4.2.1 - Report the branch actually reached

An early `Abstain` completes the admission result for the attempted use. Keep the failed rule, reasons, known family and registry edition, TaskSignature, intended use, claim scope, qualification window, and available source and policy references. Name any required reference that could not be resolved and the available basis for that finding. The report can stop there without completing later judgements.

Retain each premise or result that was established or validly reused for this branch, with its source edition and the scope, window, evidence profile, and use that make it applicable. Reuse does not require recomputing the result. An earlier result whose applicability is unresolved remains unavailable as a premise for this use.

Distinguish these situations for each affected entry:

| Situation | What the report says | Result value |
| --- | --- | --- |
| A required basis is missing or unavailable | Name the missing profile, reference, or evidence and why it could not support this use. | Leave the dependent judgement value unestablished. |
| A judgement was not evaluated | Name the judgement and the reason; use `not reached after R0` or `not reached after R3` when an earlier rule stopped evaluation. | No judgement result was established or reused for this entry. |
| A live S2 value is the admitted `unknown` | Retain that value under its C.22 value rule and cite the family branch that handles it. | `unknown` remains the supplied value; U2/R2 govern the branch. |
| An evaluated predicate or AcceptanceClause returned `false` | Cite the predicate or clause, its result, and the basis of that evaluation. | Retain the computed `false`; apply R3 or the declared CAL failure behavior as appropriate. |

These descriptions qualify report entries; they do not extend the S2 value sets, the closed maturity rungs, or the Acceptance verdict domain. An applicable earlier judgement used by the branch is reported as reused, not as unevaluated merely because it was not recomputed. A known result not used by this branch may be cited separately with that limited purpose.

**First use.** A registered family resolves, but the evidence profile required by R0 cannot be recovered. Report `Abstain`, the missing profile and available source basis, maturity `not evaluated` when no applicable judgement is available, and Acceptance `not reached after R0`. Do not insert L0 or `false` to fill those result positions. If R0 passes but Eligibility evaluates to `false`, report that predicate result and R3 `Abstain`; later Acceptance may remain `not reached after R3`. Keep a previously established maturity result if it is applicable and used.

`Admit` still requires the complete R1 evidence, Eligibility, and Acceptance basis. A declared `Degrade(mode)` retains the premises that selected its branch and any consumed maturity results. An unmet Acceptance condition stays unmet when its failure behavior permits a narrower use. R2 still requires R0 and eligibility to be checked for that changed use before reliance; a failed R0 or an Eligibility violation for the original attempted use remains `Abstain`.

#### C.23:4.3 - Maturity ladder (poset, not a scalar; Description, not Spec)

When a maturity judgement is established for an admission use, publish or cite its editioned **`MaturityCardDescription`** for the exact evaluated `MethodFamily`, G.5 registry edition, evidence profile, claim scope and selected slices, qualification window, and intended admission use (UTS enum ids; scale kind = ordinal; reference plane declared). Cite an existing card when its judgement remains applicable. If no applicable judgement is available at an early stop, report that state under §4.2.1 without creating a card or assigning a rung. Do not embed acceptance thresholds here; an admission floor remains a G.4 AcceptanceClause cited by R1.

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

**W1.** Register the SoS-LOG rule ids. Publish or cite a `MaturityCardDescription` for an established maturity judgement under §4.3; use §4.2.1 when an early stop leaves that judgement unavailable. RSCR tests cover `Admit`, `Degrade`, `Abstain`, and unknown paths, including early reports with missing bases or unperformed judgements. Relation and loss-policy ids appear only where a branch actually relies on them.
**W2. Admissibility Ledger.** Publish an editioned `AdmissibilityLedger`. Each selector-facing row identifies the exact `MethodFamilyId`, G.5 registry edition, TaskSignature, RuleId and rule edition, intended admission use, claim scope, qualification window, decisive branch, and decision result. Record its MaturityRung, EvidenceProfile, AcceptanceClause and policy references, verdicts, evidence paths, DominanceRegime, and PortfolioMode according to §4.2.1: retain established or applicable reused values and explain any required but unresolved reference or unperformed judgement. An explanation of a missing or unperformed result accompanies its unfilled value position; it is not a substitute verdict or rung. Include obtaining relation and loss-policy ids only when actually used, and G.6 path ids under R5's condition. UTS registers the row vocabulary; the ledger records the admission result and its basis.
**W3. Strategy composition.** For a selection composition called a strategy, cite its governing G.5 rule and **E/E-LOG** policy.
**W4.** Selector (G.5) **consumes** these rules; results appear in the **Dispatcher Report** with reasons in/out and cited anchors/bridges.

