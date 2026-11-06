---
chunk_kind: "child"
pattern_id: "A.19.CN"
pattern_title: "CN-frame: Specify and Maintain Comparability and Normalization"
section_id: "A.19.CN:4"
section_title: "Solution — Specify the comparison basis and maintain it when reused"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CN/A.19.CN__005_solution-specify-the-comparison-basis-and-maintain-it-when-reused.md"
commit_sha: "d8dd955fddb923b5b946d2c5865d0665cff5a67e"
heading_path:
  - "A.19.CN — CN-frame: Specify and Maintain Comparability and Normalization"
  - "A.19.CN:4 — Solution — Specify the comparison basis and maintain it when reused"
line_start: 36457
line_end: 36546
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

### A.19.CN:4 - Solution — Specify the comparison basis and maintain it when reused

#### A.19.CN:4.1 - The **CN‑Spec** (comparability and normalization specification)

A **CN‑frame** is described by a compact, notation-free specification. The specification names the bearer and the exact boundary within which its readings may be compared:

```
CN‑Spec {
  name              : CN‑frameName
  edition           : <edition>
  bearer_ref        : <evaluated bearer or bearer kind>
  characteristic_space_ref : <CharacteristicSpaceRef>
  characteristicSpaceDescriptionRef? : <U.EpistemeRef to the exact defining/description episteme>
  scope_ref?        : <ClaimScopeRef>
  window?           : <qualification interval>
  reference_or_comparison_basis : <corpus, baseline, reference state, or declared comparison set>
  cs_basis          : [{
    slot_id         : <tech-token>,
    characteristic  : <Characteristic defined under A.17>,
    scale           : { type: nominal|ordinal|interval|ratio, unit?: <measurement unit under A.18/C.16>, bounds?: <…> },
    polarity?       : <preference rule when ranking desirability; e.g. up, down or target-range>,
    // if needed: missingness?, admissible_domain? (MM‑CHR-consistent metadata)
  }]
  chart             : { reference_state, coordinate_patch, measurement_protocol_ref?, value_ascription_basis? }
  normalization?    : {
    UNM_id?,
    methods: [NormalizationMethodId],
    instances?: [NormalizationMethodInstanceId],
    method_descriptions: [NormalizationMethodDescriptionRef],
    admissible_reparameterizations,
    invariants,
    fix?: <NormalizationFixSpec>
  }
  comparability     : { mode ∈ {coordinatewise, normalization-based}, minimal_evidence }
  intended_use      : <claim, comparison, admission, or aggregation use>
  indicator_policy? : { IndicatorChoicePolicyRef, scope, edition }
  acceptance        : { checklist_for_admission, window?, evidence_anchors }
  aggregation?      : { Γ_fold, selected WLNK/COMM/LOC/MONO claims, time_policy }
  alignment?        : { semantic_uses?: <Bridges and separate bounded-use claims under §4.3>, plane_relation_refs?: <applicable plane relations> }
  maintenance?      : { responsibility, DRR_links?, applicable_deprecation_arrangement }
}
```

**Reading:** the CN-frame is the selected characteristic space and chart for one named bearer and use. The normalization block is needed for normalization-based comparison; direct coordinatewise comparison can omit it. Add maintenance arrangements when the specification is retained for later reuse or maintained as a shared edition. `CN‑Spec` fixes the editions, comparison basis, qualifying scope/window and admission evidence needed by that use, with normalization references and aggregation choices when used. A.19.UNM defines normalization semantics, A.19.UINDM defines indicatorization, C.16 supplies measurement and evidence backing, and G.0 supplies the applicable admission conditions. An actual `Γ_fold` cites its law and applicability basis. Its property codes express only the claims needed by this use; A.9 supplies an unresolved law choice or property check, while ULSAM retains the actual CHR fold and admissibility rules.

The space reference selects the space itself. Add `characteristicSpaceDescriptionRef` when the selected use needs one exact definition or description edition; UNM and UINDM require this pin for their applications. Resolve the pair under A.19:5.1.1.1 and check that the description supplies the basis of that same space. An unchanged space may have a different description episteme, and a changed basis may require a different space even when the description retains its familiar title.

**Mechanism-reference note.** `UNM_id` identifies the admitted normalization mechanism. `NormalizationMethodId` and `NormalizationMethodInstanceId` retain the meanings declared by A.19.UNM, and evidence for a relied-on instance remains with C.16. CN‑Spec neither redefines those terms nor implies transport or a cross-local relation.

**L‑CN‑Spec‑NORM‑IDs (by reference).** Cite the normalization identifiers defined by A.19.UNM.

#### A.19.CN:4.2 - CN-frame registry and conditional independent certification

First identify whether the receiving claim or applicable control requires independent certification of this exact CN-Spec edition or admission basis. When it does, the holder certifying it must not have authored or materially selected that basis. Include relevant earlier authoring whose content the certified basis retains. Renaming an assignment or waiting until an authoring assignment ends does not satisfy this condition.

Recover the actual holders, their relevant Work, the exact edition or basis and the applicable history under A.2.1 and A.2.7. Distinct assignments do not establish distinct holders. Missing history leaves independence unresolved. Different holders can satisfy this non-self-certification condition while their assignment windows overlap; any stronger organizational-independence or commissioning control still applies. The certifier's authority and adequacy of examination require their own grounds.

When no independent-certification claim or control applies, an adequately grounded one-person comparison can remain explicitly uncertified. Its measurement, comparison and reliance requirements still apply.

One named registry edition may publish the CN-frame's names, exact editions, characteristic-space and bearer references, the maintenance assignment, and the deprecation relation. When certification affects the receiving use, it also makes the applicable control, relied-on edition, certification result and supporting references recoverable. Distinguish:

* an adequate comparison for the named use with independent certification not required and no such claim made;
* a certification condition satisfied for the exact edition, with the participation, authority and examination grounds;
* a required condition that is unmet or unresolved, with its consequence for the dependent use under the applicable control.

These are different conclusions, not interchangeable registry labels. The registry helps discovery and currentness; it supplies no missing comparison, independence or certification evidence. A changed comparison basis reopens only the certification and receiving conclusions that rely on that change. A display-only registry change does not reopen them.

#### A.19.CN:4.3 - **Bridges between exact local meanings**

When a comparison or reuse needs a semantic correspondence or difference between two exact F.17 local senses, test the direct F.9 predicate. Cite a Bridge only when it obtains; otherwise retain the actual F.9 exit and its reason. A use that needs an absent or unresolved correspondence remains unsupported. A coordinate mapping or plane relation keeps its own grounds. A compact account may show an obtaining Bridge and its separate bounded-use claim together:

```
Bridge: <obtaining occurrence between exact source and receiving F.17 cells>
  predicate_profile: <relation kind, endpoint readings and obtaining condition>
BoundedUseClaim:
  applicable_use: <the receiving comparison, admission or aggregation>
  direction: <source-to-receiving use>
  correspondence_rule: <how the local claims are used together>
  tolerated_loss: <declared limit for this use>
  polarity: affirmative | negative
  grounds: <kept/lost distinctions and other support or counterevidence>
  coordinate_transform?: <separately justified pullback, pushforward, re-scaling, re-binning, etc.>
  plane_relation_ref?: <only when a separately defined plane relation obtains>
  reliance_ref?: <required reliance judgement for this use>
  assurance_ref?: <result for a current named assurance claim>
  extra_guards?: {additional evidence, required review, or an authorized exception within its applicable scope}
```

The Bridge is only the exact sense relation. The separate C.2.1 claim states whether it suits the named use, direction, rule and tolerated loss. For reliance on an affirmative claim, obtain or reuse the A.10 disposition required by F.9:4.2; a negative or unresolved claim supplies no positive use basis. Add a B.3 result only for a current named assurance claim. Matching names establish no Bridge, and a reverse use needs its own justified direction. B.3 determines any assurance consequence under the selected argument or model; CN-Spec may state additional receiving-use conditions.

