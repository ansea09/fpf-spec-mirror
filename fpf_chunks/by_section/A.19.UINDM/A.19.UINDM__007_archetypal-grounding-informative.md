---
chunk_kind: "child"
pattern_id: "A.19.UINDM"
pattern_title: "Indicatorization (UINDM): Select Indicators Under a Declared Policy"
section_id: "A.19.UINDM:5"
section_title: "Archetypal Grounding (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UINDM/A.19.UINDM__007_archetypal-grounding-informative.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "A.19.UINDM — Indicatorization (UINDM): Select Indicators Under a Declared Policy"
  - "A.19.UINDM:5 — Archetypal Grounding (informative)"
line_start: 35247
line_end: 35284
dependencies:
keywords:
  - "CHR suite stage indicatorize"
  - "CN-Spec.indicator_policy"
  - "IndicatorChoicePolicy"
  - "indicator set"
  - "indicatorization"
  - "tri-state admissibility (pass"
---

### A.19.UINDM:5 - Archetypal Grounding (informative)

#### A.19.UINDM:5.1 - Tell

Think of UINDM as a **policy‑bound projection**:

* Input: “the declared characteristic basis for this exact bearer, claim scope and selected slices, qualification window, evidence basis, and intended use, plus an explicit indicator choice policy”
* Output: “the selected positions of this exact basis, each retaining its Characteristic, Scale and meaning for downstream use”

The key didactic boundary is: **UINDM chooses coordinates; it does not alter coordinates.**

#### A.19.UINDM:5.2 - Show (U.System) — cross‑unit engineering dashboard

A program manager maintains a `U.CharacteristicSpace` for manufacturing sites, including ~30 characteristics (quality, safety, cost, throughput, sustainability).

* The CN‑Spec’s `indicator_policy` for the “weekly executive dashboard” selects a subset:
  `{DefectRate, IncidentRate, UnitCost, LeadTime, EnergyPerUnit, OnTimeDelivery}`.
* In this example each named Characteristic has one basis position. UINDM resolves the six names to those exact positions and returns S; each position retains its original Scale.
* One site lacks reliable incident reporting for the last week. The indicator policy is evidence‑gated; `IndicatorizeEligibility` returns `degrade` (not `pass`), and the audit records the effective MinimalEvidence and the edition pins used.

Downstream mechanisms can now be held to the invariant: **they may only score/compare/select using the declared indicator profile (or explicitly abstain/degrade).** This avoids “dashboard drift” where different teams silently score on different subsets.

#### A.19.UINDM:5.3 - Show (U.Episteme) — robust evaluation across environments

A research lead wants indicators for model robustness under distribution shift (different hospitals, sensors, geographies).

* The declared characteristic-space basis includes many candidate metrics (accuracy slices, calibration, subgroup error, OOD detection quality).
* The indicator choice policy is “invariance‑driven”: prefer indicators whose semantics remain stable under environment changes; deprioritize proxy metrics known to be environment‑sensitive.
* UINDM returns an indicator set used by the scoring and comparison stages; uncertain indicators are handled via tri‑state guarding rather than coerced to zero or silently dropped.

#### A.19.UINDM:5.4 - One Characteristic at two Scale positions

Let the exact space declaration `CS7` have ordered positions `i1=(Temperature, Celsius)` and `i2=(Temperature, kelvin)`, followed by an unrelated cost position. A state contains `x_i1=20 °C` and `x_i2=293.15 K`. The policy “select Celsius temperature” returns `S={i1}`. The explicit all-matches policy “all Temperature positions” returns `{i1,i2}`, with `x|_S` in the original order and both Scale meanings retained. UINDM converts neither value.

For the first policy, a separately admitted USCM scoring use can read the Celsius value under its declared method `g_C(c)=(c-0)/(40-0)` on Celsius interval `[0,40]`, returning `0.5` at 20. The interval endpoints are part of this illustrative scoring declaration. Supplying 293.15 as though it were Celsius violates that method's input basis; a TemperatureRef alone would not reveal the error. All-matches selection requires a receiving method that accepts those two Scale-specific positions, or a narrower selection; it is not a universal default.

Suppose a new declaration `CS8` reverses these two positions. Resolving “Celsius temperature” now selects its CS8-local position i2. Reusing CS7's naked integer 1 would select kelvin and is invalid. If the policy merely says “Temperature” and supplies no rule for the two matches, return its unresolved/abstain disposition. A missing indicator policy retains the defined abstain result, and evidence gating still applies only when the selected policy requires it.

