---
chunk_kind: "child"
pattern_id: "A.1.CSD"
pattern_title: "Discovering Systems That May Bear Consequences"
section_id: "A.1.CSD:5"
section_title: "Four First-Screen Situations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.CSD/A.1.CSD__008_four-first-screen-situations.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "A.1.CSD — Discovering Systems That May Bear Consequences"
  - "A.1.CSD:5 — Four First-Screen Situations"
line_start: 2668
line_end: 2697
dependencies:
  - "A.1"
  - "A.1.SCR"
  - "A.10"
  - "A.14"
  - "A.6.RCD"
  - "B.1"
  - "B.1.2"
  - "B.2"
  - "B.2.2"
  - "C.11"
  - "C.11.CRC"
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
| A nutrient pulse in a bioreactor may change living and engineered Systems. | Trace supported feed and effluent relations separately from modal biological and operating paths, and recover actual whole/part facts. | Select a spatial sample, pressure-drop observation, or effluent probe while retaining any unrecognized whole as an explicit blocker. |

The same discovery action changes all four situations. Their domain Methods, quantities, evidence rules, and decisions remain different.

#### A.1.CSD:5.1 - Minimally Viable Worked Case: Nutrient Pulse

`FeedPulsePlan-FP4` proposes a larger nutrient pulse for `BioreactorOperatingSystem-BR7`. The receiving investigation is `ProbeDecision-PD4`: choose the next observation before changing the feed setting for the next 48 hours. The plan is the account's one exact focus EntityOfConcern; the ClaimGraph examines the possible feed-operation occurrence it specifies rather than treating the plan as a physical cause. The probe decision is the account's neighboring use.

Baseline instrumentation supports one obtaining substrate-transfer occurrence from `FeedLine-F2` into the reactor medium and one obtaining effluent-flow occurrence from `BR7` to `TreatmentTrain-TT2`. Microscopy and persistence observations support the constructive recognition of individual bacterial Systems and `BiofilmPatch-BP3`: matrix-linked constituents, persistent assembly, whole-level nutrient-processing and shear-resistance characteristics, and actual participation in nutrient transformation establish the patch as a distinct System. The exact constituent relations used for the patch are recorded under their part-whole governors. No generic impact edge is added.

The proposed larger pulse has not occurred. The account therefore keeps four paths modal:

| Candidate bearer | Modal path and possible changed characteristic | Support and uncertainty | Receiver connection |
| --- | --- | --- | --- |
| sampled individual bacterial Systems near the inlet | Larger pulse -> higher local substrate concentration -> changed metabolic state and viability distribution. | Baseline gradient observations support plausibility; the proposed concentration field is unmeasured. | Add inlet-near and bulk samples before the setting change. |
| `BiofilmPatch-BP3` | Larger pulse -> changed growth and matrix production -> changed patch coverage and shear resistance. | Current patch identity and coverage obtain; the proposed growth response remains model-supported and uncertain. | Add image-based coverage observation and preserve the current pulse as a reversible alternative. |
| `BioreactorOperatingSystem-BR7` | Changed patch coverage and local transfer -> changed transfer efficiency and pressure drop. | Baseline pressure and transfer measurements obtain; the coupling under the larger pulse remains modal. | Add a pressure-drop monitoring condition to the trial. |
| `TreatmentTrain-TT2` | Changed reactor effluent composition -> changed incoming load and treatment performance. | The effluent connection obtains; the proposed composition and downstream response are unmeasured. | Add an effluent sample before deciding whether the pulse can continue. |

The account keeps bacterial, biofilm, reactor, and treatment-train characteristics separate. It does not average them into one score. Its discovery residual names an observed unattached aggregate outside `BiofilmPatch-BP3`. Current evidence supports treating the observed members as a collection; whether that collection also forms a whole/System remains `unknown` because assembly, persistence, and the kind-specific A.1 facts are unsupported. The next recognition probe images the same aggregate across two sampling intervals and records any stable assembly relation and whole-level behavior. Recover those A.1/C.13 facts before classifying it; only supported failure of a required A.1 component or condition warrants a negative System result.

The first useful result is the four-part probe: spatial bacterial sampling, image-based biofilm-coverage observation, pressure-drop monitoring, and effluent measurement. The current pulse setting remains the reversible alternative until those observations support a change. Stop when `ProbeDecision-PD4` can choose that probe set and alternative and every retained modal path has a support statement, uncertainty, and reopen observation. Reopen if a new whole is recognized, the feed configuration changes, or an observation reverses one path claim.

