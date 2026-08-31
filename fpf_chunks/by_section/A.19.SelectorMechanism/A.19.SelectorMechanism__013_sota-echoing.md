---
chunk_kind: "child"
pattern_id: "A.19.SelectorMechanism"
pattern_title: "Unified Selection Kernel, SelectorMechanism"
section_id: "A.19.SelectorMechanism:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SelectorMechanism/A.19.SelectorMechanism__013_sota-echoing.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "A.19.SelectorMechanism — Unified Selection Kernel, SelectorMechanism"
  - "A.19.SelectorMechanism:11 — SoTA-Echoing"
line_start: 34573
line_end: 34605
dependencies:
keywords:
  - "SelectEligibility"
  - "selected set"
  - "selection kernel"
  - "set-returning selection"
  - "tri-state guard (pass"
---

### A.19.SelectorMechanism:11 - SoTA-Echoing

**SoTA vs popular note.** This section records alignment to post‑2015 evidence‑backed practice. It is not a mandate to use fashionable methods; method semantics stay in SoTA packs (`G.2`) and wiring modules, while this pattern fixes the stable selection boundary.

Concrete selector-family SoTA packages are cited through their current Part G pack or claim sheet when one governs the use. They connect through `CriteriaSlot` and `TaskSignatureSlot` references while kernel semantics remain unchanged.

#### A.19.SelectorMechanism:11.1 - SoTA alignment map (normative)

| SoTA practice pointer, post‑2015+                                                                               | Primary source examples, post‑2015+                                                                           | Where it connects to SelectorMechanism                                                                             | Adoption status |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | --------------- |
| Treat the Pareto set or declared selected set as a first-class output under multi-criteria partial orders       | Quality Diversity as a decision framing, e.g., Pugh et al. 2016; Vassiliades et al. 2018                      | Expressed as set‑return default and explicit set-return criteria; method details live in specializations and wiring | Adapt           |
| Use archive-based retained sets where diversity is part of the result, but do not silently promote it to dominance | Modern QD and archive practices post‑2015, including map-elites descendants and archive insertion policies | Expressed as policy‑bound criteria and report‑only telemetry unless explicitly promoted                            | Adapt           |
| Pair environments and methods in open-ended or co-evolutionary settings without breaking kernel semantics       | Open-ended environment-method pairing, e.g., Wang et al. 2019 and successors                                  | Expressed as candidate and criteria structuring plus admissible specializations; kernel unchanged                      | Adapt           |
| Include an explicit abstain or reject option under uncertainty rather than forcing a decision                   | Selective prediction and rejection-option practice, e.g., Geifman and El‑Yaniv 2017; follow-on selective nets | Expressed as tri-state `SelectEligibility` with fail-closed discipline                                             | Adopt           |
| Keep architecture commitments traceable to one governing pattern                                                        | ISO/IEC/IEEE 42010:2022 architecture description discipline                                                   | Expressed as explicit governing-pattern assignment and Tell+Cite stubs elsewhere                                             | Adopt           |

**Notes per row** (1–2 sentences; why to adopt, adapt, or reject):
* **Selected-set-as-output (QD framing):** adopt the *decision framing* (declared selected set as a first-class result) while keeping concrete QD or retained-set algorithms out of the kernel; they belong in `G.2` packs and wiring modules, preserving evolvability.
* **Archive retained sets (diversity as result):** adapt archive thinking by keeping diversity and illumination signals report‑only unless an explicit CAL policy promotes them to dominance; this prevents silent scalarization and preserves governing-pattern defaults (typically `G.5` and CAL).
* **Open‑ended environment–method pairing:** keep the kernel unchanged; open‑ended pairing is expressed by shaping candidates and criteria (and, when needed, admissible specializations `⊑` and `⊑⁺`) with explicit edition pins and transfer and validity rules in planned baseline, not by mutating `Select`.
* **Reject or abstain under uncertainty:** adopt the rejection‑option stance as a tri‑state guard with fail‑closed semantics; explicit abstain is preferable to forced choice under missing admissibility and evidence.
* **Governing-pattern architecture discipline:** adopt governing-pattern + Tell‑and‑Cite to keep the spec teachable and reviewable; this directly reduces drift and “second centers of gravity”.

---

#### A.19.SelectorMechanism:11.2 - Currentness and smallest reopen rule

**Qualification basis and window.** The stable kernel claim is qualified by the current editions of A.6.1/A.6.5 operation and slot discipline, A.19.CPM binary application and output semantics, A.19.CN and G.0 admission and evidence rules, G.5 selector-policy discipline, A.2.6 scope semantics, and the exact current G.2 selector pack or claim sheet cited by an actual use. For that use, the effective qualification window is the intersection of those bound editions' currentness and any validity interval declared by the selector pack, TaskSignature, or policy; `post-2015+` is an orientation label, not an indefinite freshness claim.

**Reopen the SelectorMechanism kernel only when.** Reopen the smallest affected selector rule when a direct governor changes set-return semantics, inherited SlotKinds or specialization constraints, criteria or policy binding, tri-state eligibility, the finite CPM application-basis and token-provenance boundary, selection scope, or the separation of selected set, evidence, provenance, result episteme, and publication, or when qualified evidence contradicts one of those commitments. A new selection algorithm, archive or diversity method, candidate-generation method, tie-breaker, `PortfolioMode`, rejection calibration, or domain policy that still satisfies those commitments changes its G.2 pack, G.5 policy, `CriteriaSlot`, `TaskSignature`, or other direct policy binding rather than this kernel.

**Smallest affected locus.** A signature, basis, coverage, or output change reopens only the corresponding direct-signature, selection-use-binding, `OperationAlgebra`, or `LawSet` passage in `A.19.SelectorMechanism:4.1`; an admissibility or failure-semantics change reopens the matching `AdmissibilityConditions` clause. Update only the nearest exercising case in `A.19.SelectorMechanism:5.2` or `:5.3` and the corresponding `CC-A19SelectorMechanism` row. Source-family or policy churn that changes no kernel commitment updates the direct pack, policy, or claim sheet and, when its summary is stale, only the affected row or note in this SoTA map.

