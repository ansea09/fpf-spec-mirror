---
chunk_kind: "child"
pattern_id: "A.1.CSD"
pattern_title: "Discovering Systems That May Bear Consequences"
section_id: "A.1.CSD:5"
section_title: "Four First-Screen Situations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.CSD/A.1.CSD__008_four-first-screen-situations.md"
commit_sha: "14f263bd90d449803a2ec6cb57ee7f620cc41bed"
heading_path:
  - "A.1.CSD — Discovering Systems That May Bear Consequences"
  - "A.1.CSD:5 — Four First-Screen Situations"
line_start: 2731
line_end: 2764
dependencies:
  - "A.1"
  - "A.1.SCR"
  - "A.10"
  - "A.14"
  - "A.15.9"
  - "A.6.RCD"
  - "B.1"
  - "B.1.2"
  - "B.2"
  - "B.2.2"
  - "C.11"
  - "C.11.CRC"
  - "C.11.DUA"
  - "C.13"
  - "C.2.1"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30.ILC"
  - "D.1"
keywords:
---

### A.1.CSD:5 - Four First-Screen Situations

| Working situation | First action | First useful result or stop |
| --- | --- | --- |
| A flood-pump modernization may shift load, maintenance demand, downstream flow, and failure exposure. | Name the configuration decision, trace the finite change through supported plant relations and modal operating paths, and challenge the selected boundary. | One additional pump, maintenance, downstream, or containing-System claim changes a design constraint or monitoring condition; otherwise stop with the exact missing relation. |
| An on-call and platform arrangement is being reorganized. | Trace the proposed Work and assignment changes to employee, provider, service, customer, and neighboring organization Systems without treating those names as a level ladder. | Keep workload, capability, service, and organization consequences separate; return the missing bearer or relation to the organization-change Method. |
| A public appointment service is being redesigned through facilitated inquiry. | Trace service and policy alternatives to applicant, staff, provider, transport, and other material Systems; use participation as a discovery source, not proof of systemhood or authority. | Return descriptive bearer claims to the facilitated inquiry; route participation, concern, and authority questions to their direct practice. |
| A nutrient pulse in a bioreactor may change living and engineered Systems. | Trace supported feed and effluent relations separately from modal biological and operating paths, and recover actual whole/part facts. | Return the separate consequence claims and current limit; select spatial sampling, pressure observation, or effluent measurement only when their individual and combined contribution warrants the programme. |

The same discovery action changes all four situations. Their domain Methods, quantities, evidence rules, and decisions remain different.

#### A.1.CSD:5.1 - Minimally Viable Worked Case: Nutrient Pulse

In this constructed case, `FeedPulsePlan-FP4` proposes a larger nutrient pulse for `BioreactorOperatingSystem-BR7`. The receiving investigation is `ProbeDecision-PD4`: decide whether and which further observations are worthwhile before changing the feed setting for the next 48 hours. The plan is the account's one exact focus EntityOfConcern; the ClaimGraph examines the possible feed-operation occurrence it specifies rather than treating the plan as a physical cause. The probe decision is the account's neighboring use.

Baseline instrumentation supports one obtaining substrate-transfer occurrence from `FeedLine-F2` into the reactor medium and one obtaining effluent-flow occurrence from `BR7` to `TreatmentTrain-TT2`. Microscopy and persistence observations support the constructive recognition of individual bacterial Systems and `BiofilmPatch-BP3`: matrix-linked constituents, persistent assembly, whole-level nutrient-processing and shear-resistance characteristics, and actual participation in nutrient transformation establish the patch as a distinct System. The exact constituent relations used for the patch are recorded under their part-whole governors. No generic impact edge is added.

The proposed larger pulse has not occurred. The account therefore keeps four paths modal:

| Candidate bearer | Modal path and possible changed characteristic | Support and uncertainty | Receiver connection |
| --- | --- | --- | --- |
| sampled individual bacterial Systems near the inlet | Larger pulse -> higher local substrate concentration -> changed individual metabolic states and sample-level viability distribution. | Baseline gradient observations support plausibility; the proposed concentration field is unmeasured. | Retain the local-exposure limit; spatial sampling could distinguish inlet and bulk responses in a selected bounded trial. |
| `BiofilmPatch-BP3` | Larger pulse -> changed growth and matrix production -> changed patch coverage and shear resistance. | Current patch identity and coverage obtain; the proposed growth response remains model-supported and uncertain. | Preserve the current pulse alternative; short-window images may leave the growth response unresolved. |
| `BioreactorOperatingSystem-BR7` | Changed patch coverage and local transfer -> changed transfer efficiency and pressure drop. | Baseline pressure and transfer measurements obtain; the coupling under the larger pulse remains modal. | Preserve the pressure/transfer constraint; a trace during a selected trial could test the proposed coupling. |
| `TreatmentTrain-TT2` | Changed reactor effluent composition -> changed incoming load and treatment performance. | The effluent connection obtains; the proposed composition and downstream response are unmeasured. | Keep the downstream-load limit visible; an effluent observation could change whether a tested pulse may continue. |

The account keeps bacterial, biofilm, reactor, and treatment-train characteristics separate. It does not average them into one score. Its discovery residual names an observed unattached aggregate outside `BiofilmPatch-BP3`. Current evidence supports treating the observed members as a collection; whether that collection also forms a whole/System remains `unknown` because assembly, persistence, and the kind-specific A.1 facts are unsupported. The aggregate's whole identity does not alter this receiving decision in the case, so it remains an explicit unknown. If later reliance needs that identity, the relevant A.1/C.13 evidence would concern stable assembly, persistence, and whole-level behavior across observations; acquiring it still needs a worthwhile receiving contribution. Recover those facts before classifying it; only supported failure of a required A.1 component or condition warrants a negative System result.

The current pulse remains available while the larger pulse's consequences are modal. For the inquiry choice, suppose the domain investigation supplies these attainable contributions and full efforts, including preparation, any required trial operation, observation, and individual interpretation: spatial sampling can distinguish local exposure within 48 hours for one staff-hour; a pressure trace can qualify the transfer constraint for one hour; and an effluent observation can address downstream load for one and a half hours. Those answers could change the admissible pulse comparison. A two-hour imaging series would not discriminate the growth response in this window. These are illustrative planning premises, not biological thresholds or observed effects.

The programme has four available staff-hours after existing duties and adds half an hour of shared coordination and joint interpretation. All four observations would take six hours and exceed that capacity; selecting each in isolation would overcommit it. Spatial sampling, pressure observation, and effluent measurement together take four hours, finish in the receiving window, and supply the worthwhile discriminating contribution. The inquiry selects that programme while retaining the current pulse alternative and the unresolved biofilm-growth and aggregate-identity claims. If access, interpretation capacity, protection, or trial authority cannot support it, the available result is the qualified account with the current setting retained.

The domain practice governs whether any trial or subsequent feed change is admissible. Selecting observations neither performs them nor establishes their outcomes, causal effects, or permission. Reopen when a new whole becomes material, the feed configuration changes, an observation reverses a path claim, or the programme's contribution or feasibility changes.

