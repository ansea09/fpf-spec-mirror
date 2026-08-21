---
chunk_kind: "child"
pattern_id: "A.6.P.WMR"
pattern_title: "Exact Relation Recovery for Method and Work Claims"
section_id: "A.6.P.WMR:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.P.WMR/A.6.P.WMR__006_archetypal-grounding.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "A.6.P.WMR — Exact Relation Recovery for Method and Work Claims"
  - "A.6.P.WMR:5 — Archetypal Grounding"
line_start: 16214
line_end: 16300
dependencies:
  - "A.15.1"
  - "A.15.1-A.15.3"
  - "A.15.2"
  - "A.15.3"
  - "A.15.PROD"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "A.6.P"
  - "A.6.RCD"
  - "C.2.P"
  - "E.10"
  - "E.10.ARCH"
  - "E.18.1"
  - "F.18"
keywords:
---

### A.6.P.WMR:5 - Archetypal Grounding

**Informative worked examples.** Start each case with the ordinary decision and result. Section 5.1 then expands one machining case as the sole author-side relation-declaration replay. Sections 5.2-5.7 retain only the situation, deciding fact or blocker, ordinary result, and stop needed to demonstrate a different branch. These cases add no RFC duty. Their identifiers, relation tokens, and assumed project settlements add no FPF ontology.

#### A.6.P.WMR:5.1 - Inspection and machining: one ordinary result, one assurance replay

A source says, `the inspection report is the result of inspection`. First identify report episteme `R-17` and ask what it is relative to. If exact inspection application `P-17` actually returned `R-17` under its declaration-local result predicate, write: `Inspection application P-17 returned report R-17.` If the current question is when exact Work first constituted the report, apply A.15.PROD. If neither relation is governed, return `missing-governor` naming `R-17`, the proposed application or Work participant, proposed predicate, affected use, and absent definition; name a future pattern or declaration need only when one is identifiable. Do not invent `WorkResult`.

Now a traveler says, `raw stock WP-204 and cutting fluid CF-17 are inputs; the machined part and inspection report are outputs of machining`. Exact machining Work `W-204-MACHINE` and continuing workpiece `WP-204` are already identified. The ordinary result is:

- `Applying A.15.1 identifies W-204-MACHINE with affectedReferent WP-204.`
- `Cutting-fluid quantity CF-17 was consumed by W-204-MACHINE during I-204 under MachiningWorkConsumesResource.`
- `T-WP204-GEOMETRY is the bounded geometry change of continuing WP-204; W-204-MACHINE caused it under MachiningWorkCausesGeometryChange.`

The workpiece remains `WP-204`, not a newly constituted output. A report binding or inception claim stays open until its own application or A.15.PROD basis is present. If the consumption fact fails, the proposed positive fluid claim is `factually unsupported`; if it is unavailable, return `missing-information`; if the relation governor is absent, return `missing-governor` and name the missing machining-resource predicate and its defining pattern or declaration.

A later measurement-result episteme `R-204`, diagnostic finding, evaluation verdict, or accepted-deliverable claim is a separately governed claim; delivery or physical transfer of continuing `WP-204`, and transfer or publication of `R-204`, are separate again. Shared chronology and one machining case entail none of them: each current claim needs its own direct governor and facts.

**Author-side assurance replay — the one fully expanded relation-declaration fixture.** Exact published relation-declaration episteme `MFG-WORK-REL-2026` contains the defining ClaimGraph for these case-local predicates:

| RelationKind | Direct participants and extent | Obtaining condition and applicability |
| --- | --- | --- |
| `MachiningWorkConsumesResource` | exact consumed resource quantity, exact Work individual admitted under `U.Work`, and `Γ_time` | the quantity was actually consumed by that Work during the named extent; applicable only to Plant-7 machining Work |
| `MachiningWorkCausesGeometryChange` | exact Work, independently A.3.4-grounded geometry transformation, and governed extent | that Work actually caused that transformation at the extent; applicable only to the named Plant-7 case |

Separately stipulated world-side facts say that `CF-17` was consumed by `W-204-MACHINE` during `I-204` and that this Work caused `T-WP204-GEOMETRY`. The declaration episteme, work and transformation identities, chronology, and assertion epistemes `MFG-RU-CF17-W204` and `MFG-WC-W204-TWP204` supply none of those facts. The formal replay therefore yields the same ordinary sentences and the same three failure reasons. This is assurance for the result above, not the entry price for reading it.

#### A.6.P.WMR:5.2 - ETL data: direct participation, then a receiving-use stop

An ETL note says, `RawOrders is the source input and WarehouseOrders is the delivered output`. Exact Work `ETL_Nightly_0811` and both dataset entities under their admitted subject kinds are known. Exact relation-declaration episteme `ETL-DATA-REL-2025` contains the defining ClaimGraph for `SourceDatasetParticipatesInETLWork` and `DestinationDatasetParticipatesInETLWork`; separate case facts say that `RawOrders_0811` and `WarehouseOrders_0811` satisfy the declared source-dataset and destination-dataset participant meanings and predicates for that job.

Write: `RawOrders_0811 participated as the source dataset in ETL_Nightly_0811`, and `WarehouseOrders_0811 participated as the destination dataset in ETL_Nightly_0811.` Those facts establish neither delivery nor use by analytics. If decision Work `D-0811` is now claimed to use `WarehouseOrders_0811` as a premise but no premise-use, reference-use, or application-binding governor is available, stop with `missing-governor` and name the missing analytics-decision predicate and receiving use. This case demonstrates a positive direct relation followed by a distinct blocked receiving use.

Before calling `WarehouseOrders_0811` a new output, decide which dataset continues. If the ETL job updates the same dataset in place, identify that dataset's bounded change under A.3.4. If a derived dataset begins, apply its dataset-identity rule and use A.15.PROD only when the exact inception basis closes. When a catalog entry, lineage view, or publication is the source from which a reader reaches either dataset, use C.2.P to identify the exact source expression, source-to-use path, allowed use, and reopen condition. An E.17 face or form, or an E.24.PUB publication or availability occurrence, neither creates the dataset nor proves that analytics used it. Row-count, quality, latency, and drift results remain separate measurement or evaluation objects; each evaluation names its own criterion and predicate and cites the `SubjectPatternLocator` for their defining or constraining content.

#### A.6.P.WMR:5.3 - Clinical work: administration is not a health outcome

A case note says, `the patient and dose were inputs; the summary and good outcome were results`. Exact clinical Work `Appendectomy_Case_8472` has affected referent `Patient_8472`. Exact relation-declaration episteme `MED-ADM-2026` contains the defining ClaimGraph for `ClinicalWorkAdministersDoseToPatient`; a separate case fact says that `MedicineDose_8472` was actually administered during the named interval.

Write: `Appendectomy_Case_8472 administered MedicineDose_8472 to Patient_8472 during the named interval.` Keep `DischargeSummary_8472` as an episteme whose binding or inception needs its own basis. The phrase `good outcome` names no health-effect relation here, so return `missing-governor` for the proposed patient effect rather than treating a summary, discharge, or verdict as that effect. This case demonstrates a positive administration claim and an independently blocked downstream effect.

Administration is only one possible relation for `MedicineDose_8472`. The same medicine quantity may instead be a constituent of an administered preparation or compound therapy, or a resource consumed by the clinical Work; each alternative needs its own exact direct governor and case fact, and the positive administration sentence proves neither. If a patient-state change is current, first identify that exact transformation under A.3.4. Then ask separately whether a declared work-to-patient-change predicate with the exact Work, transformation, applicability, and a satisfying case fact obtains. Administration alone proves neither the change nor that the clinical Work caused it.

Keep a measured value, diagnostic finding, evaluation verdict, and claimed health effect as four different objects or claims. A discharge summary may cite any of them without becoming them. Each current claim names its own participants, temporal extent, predicate, criterion when applicable, and the content that supplies that predicate or criterion; a measurement or diagnosis does not establish a verdict, and a verdict does not establish the patient's later health effect.

#### A.6.P.WMR:5.4 - Pump 14: continuing entity and later decision use

A P2W note says, `the pressure problem was the input, adjustment was the work, and restored pressure was the result`. Keep accepted `ProblemCard@Context PC-P14-PRESSURE` as the separate problem-side object. Do not say that this accepted pressure-problem claim guided `U.WorkPlan WP-P14-2026-07-15`: the case supplies no direct relation for that use. Return `missing-governor` naming the ProblemCard and WorkPlan participants, proposed planning-use predicate, affected planning use, and absent definition; name a future declaration need only if one is identifiable. Do not infer that the problem caused `W-P14-ADJUST-1010-1020`. A.15.1 identifies that Work; A.3.4 identifies `T-P14-PRESSURE-RISE` as a bounded change of continuing `HydraulicLoop_P14`. Exact relation-declaration episteme `P14-REL-2026` contains the defining ClaimGraph for `AdjustmentWorkCausesPressureRise` and `MeasurementResultUsedByDecisionWork`; separate case facts satisfy both predicates.

Keep four values separate: `SetPointAdjustment@PlantOps-v3` is the selected `U.Method`; an A.3.2 `U.MethodDescription` episteme carries reusable claims about how that Method is done; `WP-P14-2026-07-15` states intended Work; and `W-P14-ADJUST-1010-1020` is the dated Work occurrence. Naming any of them neither identifies an additional relation nor makes one obtain, so the unsupported ProblemCard-to-plan guidance claim remains `missing-governor`.

`P14-REL-2026` is available in the current case record. Independently, a separately stipulated world-side fact satisfies its actual-causation predicate, so write: `W-P14-ADJUST-1010-1020 caused T-P14-PRESSURE-RISE`. In the explicitly earlier case record, `P14-REL-2026` is absent; at that epistemic stage, keep that Work and transformation separate and return `missing-governor` naming both participants, the proposed causation predicate, the affected use, and the absent definition. No receiver or future declaration is required to state that blocker. Separately write: `Decision Work D-P14 used measurement-result episteme MR-P14-AFTER as its declared basis.` The loop continues; no entity begins, no production-completion criterion is current, and no transformation-composition claim follows. This case demonstrates work-caused change and later epistemic use without a production reading.

#### A.6.P.WMR:5.5 - Hair styling: a changed referent and an unresolved configuration

A salon record says, `hair and gel were inputs; the hairstyle, photo, and satisfaction were outputs`. A.15.1 identifies styling Work `W-STYLE-27` with affected referent `Hair_27`; A.3.4 identifies `T-HAIR-27` as the arrangement change of that continuing hair. Exact relation-declaration episteme `SALON-RESOURCE-USE-2026` contains the defining ClaimGraph for `StylingWorkConsumesResource` and `StylingWorkCausesHairArrangementChange`; separate case facts support the work-change claim and, when known, the gel-consumption claim.

Write: `Applying A.15.1 identifies W-STYLE-27 with affectedReferent Hair_27`, and `W-STYLE-27 caused T-HAIR-27 under StylingWorkCausesHairArrangementChange.` When the separate consumption fact is present, also write: `W-STYLE-27 consumed StylingGel_27 under StylingWorkConsumesResource.` Do not yet write `EveningArrangement_27 is the resulting configuration`: the case has selected neither an A.22 structure, a characteristic-state fact, a relation occurrence, nor a description episteme and therefore has no direct configuration governor. Return that blocker. This case demonstrates a continuing changed entity plus a blocked attempt to turn `result` into an unnamed configuration kind.

`Client_27` is the person receiving the service; `Hair_27` is the continuing affected referent. A hair-to-person part claim, a service-recipient claim, or a person-level effect claim needs its own exact direct governor and case fact; naming the client beside the hair establishes none of them. Ordinary styling changes continuing `Hair_27` and does not create a new entity. A separately individuated wig, extension, or other artifact may instead open its own identity-inception question under A.15.PROD when its identity rule and inception basis close.

For gel use, distinguish the three stops. With a current `StylingWorkConsumesResource` governor, a case fact that fails its predicate is `factually unsupported`, while an unavailable consumption fact is `missing-information`; an absent conforming declaration, predicate, or applicability condition is `missing-governor`. A method-description ingredient field or appointment-plan row substitutes for none of those bases. `Photo_27` remains separately identified: its identity, photography or record-forming Work, representation of `Hair_27`, and publication are separate questions. A measured satisfaction response, an evaluation verdict, and any downstream effect of the service likewise require separate predicates and subject patterns; none constitutes the hairstyle or follows from the photo.

#### A.6.P.WMR:5.6 - Car 42: completion without inception

A finishing note says, `the last nut was the input and completed Car 42 was the output`. Car 42 already satisfies its identity rule before `NutFasteningWork-42`. Exact relation-declaration episteme `CAR42-WORK-REL-2026` contains the defining ClaimGraph for `FastenerParticipatesInFasteningWork` and `FasteningWorkCausesFastenerChange`; separate case facts say that `Nut-42-LAST` participated and the Work caused the two independently identified fastening transformations.

Write: `Nut-42-LAST participated in NutFasteningWork-42 under FastenerParticipatesInFasteningWork`, and `NutFasteningWork-42 caused the two named fastening transformations under FasteningWorkCausesFastenerChange.` Do not open entity inception: the car continues.

For the narrowly bounded finishing use, `NutFasteningWork-42` can be the whole Work selected by a local A.15.PROD production-work claim only when the fastening method's intended production effect and applicability, the exact work-to-change facts, and the current completion facts supply that narrow production basis. For the broader factory use, the same occurrence can be a proper operational part of `CarProductionWork-42` only when an exact A.15.1 work-part relation obtains and the containing Work has its own separate production basis. Neither reading supplies the other, and neither proves that the two fastening transformations are parts of one composite transformation.

When completion is current, use exact completion-criterion episteme `CAR-COMP-ED-42`, its named applicability basis, exact boundary state, and production Work to ask A.15.PROD for the historically indexed completion claim. The suffix `ED-42` and the criterion's publication establish no edition continuity. If a later criterion episteme continues an earlier one, state the separate C.2.1 `EpistemeEditionRelation`; otherwise treat it as a non-continuing replacement. If Car 42 had already completed earlier, classify the fastening separately as rework, repair, or maintenance. This case demonstrates completion distinct from inception and from automatic criterion lineage.

Production completion establishes neither delivery, acceptance, release, nor Car 42's present condition. Each current claim needs its own direct governor and facts.

#### A.6.P.WMR:5.7 - Authoring: changed episteme, publication, and review use

An authoring note says, `research notes were inputs; the draft was the output handed off to review`. First apply C.2.1. If claim content, exact `EntityOfConcern`, and effective `U.ReferenceScheme` are unchanged, keep `DraftEpisteme_31` and state only the changed carrier, rendering, publication, evidence, or transfer relation. If a discriminator changes, identify distinct `LaterDraftEpisteme_31`; assert `EpistemeEditionRelation(DraftEpisteme_31, LaterDraftEpisteme_31)` only when C.2.1's historical-continuation predicate obtains.

Exact relation-declaration episteme `AUTHORING-USE-REL-2026` contains the defining ClaimGraph for source-premise use and review-reference use. With separate case facts, write: `Authoring Work W-AUTHOR-31 used SourceNotes_31 as a premise`, and `Review Work W-REVIEW-31 used DraftEpisteme_31 as a reference.` A saved file, bibliography entry, or handoff record supplies neither fact.

`DraftFile_31` is a separately identified form-bearing entity, not `DraftEpisteme_31`. Rendering work, changed bits, or adjacency to the draft establishes neither the file's first existence nor a new episteme. When either first-existence question matters, ask A.15.PROD separately for the inception of `DraftFile_31` or of already distinct `LaterDraftEpisteme_31` and consume its local claim or exact blocker. File inception neither creates nor replaces the claim-bearing episteme.

When publication is current, exact publication occurrence `PUB-31` obtains under E.24.PUB only while its five fixed participants—the selected episteme edition, audience declaration, bounded-use declaration, exact publication form, and presentation carrier—satisfy its availability predicate. Those participants together with the maximal continuous availability interval identify the occurrence. E.17 instead governs the multi-view face or form; it does not identify `PUB-31`. Publication or availability proves none of delivery, acceptance, transfer, access, reliance, or use by review Work, and the declaration-local phrase `selected episteme edition` creates no edition continuity.

If ordinary `handed off` wording already names one exact transfer relation, apply its direct pattern and stop. A transfer package or handoff record establishes neither that transfer nor use by the receiver. Apply E.10.MOVE only when the wording still hides an FPF-governed move, workflow, next action, or readiness claim; its recovery creates no process move, transfer, Work, permission, or receiving-use relation. This case demonstrates identity first, conditional edition continuity, direct source or review use, exact publication identity, and bounded transfer-word recovery.

