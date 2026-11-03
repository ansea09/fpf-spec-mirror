---
chunk_kind: "child"
pattern_id: "A.19.CN"
pattern_title: "CN-frame: Specify and Maintain Comparability and Normalization"
section_id: "A.19.CN:5"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CN/A.19.CN__006_conformance-checklist-normative.md"
commit_sha: "d73588bdcb52ed173d7b4c1552b2ce199a548c64"
heading_path:
  - "A.19.CN — CN-frame: Specify and Maintain Comparability and Normalization"
  - "A.19.CN:5 — Conformance Checklist (normative)"
line_start: 36547
line_end: 36576
dependencies:
  - "A.19"
  - "A.6.1"
  - "C.16"
  - "F.9"
  - "G.0"
keywords:
  - "CN-Spec"
  - "CN-frame"
  - "RSG admission hooks"
  - "SCR/RSCR harness"
  - "WLNK discipline"
  - "chart"
  - "comparability modes"
  - "conformance checklist"
  - "indicator policy refs"
  - "loss evidence"
  - "maintained editions"
  - "normalization refs"
  - "optional CL"
  - "semantic relations"
  - "separate use claims"
  - "Γ-fold governance"
---

### A.19.CN:5 - Conformance Checklist (normative)

> These checks establish the declared comparison basis. Assurance and cross-team reuse still require the evidence and relation conditions of their receiving claims.

**CC‑A19.D1‑1 (Local identity and scope).** Every CN-frame **MUST** identify its name and edition, bearer, characteristic space, reference or comparison basis, intended use, and any scope/window that qualifies the readings. The same label under another scheme or edition is not evidence of the same frame.

**CC‑A19.D1‑2 (Scales, units and preference).** Each characteristic slot in `cs_basis` **MUST** declare its Scale and value meanings, and its Unit when that Scale has one. A comparison that ranks values by desirability **MUST** state its preference rule. Descriptive comparisons need no preference rule.

**CC‑A19.D1‑3 (Chart).** `chart` **MUST** name its reference state and coordinate patch. For measured values, cite the applicable measurement method and protocol under C.16; for evaluated or otherwise ascribed values, cite the rule and basis that establish those values.

**CC‑A19.D1‑4 (Normalization references, not redefinition).** When normalization is used, `normalization` **MUST** identify the admitted mechanism and provide the normalization references required by the A.19.UNM governing pattern (methods / invariants / fix, and instances when used) so that any normalization‑based comparison is auditable. This pattern does not define what a “NormalizationMethod” is — it requires that CN‑Spec can point to the governing pattern that does.

**CC‑A19.D1‑5 (Comparability mode).** `comparability.mode` **MUST** be either **coordinatewise** (same chart, Scales and applicable Units) or **normalization‑based** (“normalize‑then‑compare” via the declared **UNM**). Mixed/implicit modes are prohibited. A.19.UNM governs the directed result and any optional classes. The receiving comparison must retain its required distinctions; equality of normalized outputs alone establishes no operational congruence. CN-Spec pins the chosen result branch and its basis.

**CC‑A19.D1‑6 (Admission checklist).** `acceptance.checklist_for_admission` **MUST** state testable conditions and any interval needed for the intended use. Each admitted datum **SHALL** have the measurement, evaluation or other value-ascription basis required by that use. Cite a StateAssertion when a state claim is being made; a datum is not automatically such a claim.

**CC‑A19.D1‑7 (Aggregation discipline).** When aggregation is used, `aggregation.Γ_fold` **MUST** identify the declared scale-lawful fold, its applicable algebraic properties and any required time policy. G.0 and A.19.ULSAM govern admissibility and the fold; B.3 applies when the fold serves an assurance claim. Keep the values separate when no fold is needed.

**CC‑A19.D1‑8 (Relation and use discipline).** When reuse depends on a semantic correspondence or difference between two exact F.17 local senses, test the F.9 predicate and cite a Bridge only when it obtains. To use an obtaining Bridge, the receiving C.2.1 claim **MUST** separately state the use, direction, correspondence rule, tolerated loss and polarity. Reliance on an affirmative claim requires the A.10 disposition under F.9:4.2; a named assurance use also requires its B.3 result. Missing or unresolved required correspondence blocks the dependent use. A coordinate mapping and any applicable plane relation retain their separate grounds.

**CC‑A19.D1‑9 (Conditional non-self-certification).** When the receiving claim or control requires independent certification, the certifying holder **MUST NOT** have authored or materially selected the exact CN-Spec edition or admission basis being certified, including relevant retained earlier content. Apply §4.2 to holder/Work/history, required authority and examination. Unknown history is unresolved. An adequate use with no such requirement may remain explicitly uncertified.

**CC‑A19.D1‑10 (Maintenance, deprecation, and DRR).** A CN-Spec maintained for later reuse or as a shared edition **MUST** make its maintenance responsibility, applicable deprecation arrangement and consequential decisions recoverable. Use E.9 for decisions that need a DRR. A one-use comparison need not invent a maintenance assignment or retirement plan.

**CC‑A19.D1‑11 (Evidence for the receiving use).** An admission later used for comparison or aggregation **SHALL** retain the independently established measurement, evaluation or other value-ascription results and support relations that the receiving use needs, including applicable currentness and validity windows. Use A.10 when their provenance or bounded reliance must remain replayable. Add B.3 assurance lanes and an assurance result only when the receiving use makes that assurance claim. Missing required inputs have the disposition declared by the comparison or aggregation rule.

**CC‑A19.D1‑12 (Notation independence).** CN‑Spec content **MUST NOT** depend on a tool or file format; semantics precede notation (E.5.2 Notational Independence).

**CC‑A19.D1‑13 (Recoverable names).** Characteristic names and role labels **MUST** preserve the distinctions required by the comparison. Apply Part E lexical guidance and F.18 where a durable name or alias is needed.

