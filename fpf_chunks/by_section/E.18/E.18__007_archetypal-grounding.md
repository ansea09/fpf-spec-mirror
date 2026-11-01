---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:6"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__007_archetypal-grounding.md"
commit_sha: "a3513ddf768f1e504658ce987d34ccecb751fa1c"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:6 — Archetypal Grounding"
line_start: 110769
line_end: 110830
dependencies:
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.6.RCD"
  - "A.7"
  - "C.29"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.17"
  - "E.18.1"
  - "E.18.2"
  - "E.18.NET"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.18:6 - Archetypal Grounding

**Worked case: one measured result, two checks and their joint decision.** A practitioner is considering a welding job. Its separately identified WorkScope admits humidity below 60%, current from 35 to 45 A, wire ER70S-6 and controller FW-2.1. The job has the stated wire/controller and humidity 55%; current must be obtained from the measurement. Qualification is checked separately. This is a constructed case.

The sensor-read declaration identifies an application by its actual acquisition cycle on sensor S7. Each calculation declaration identifies an application by the controller invocation from accepted arguments to return. The A.6.1 binding rules apply within those extents. Equal argument values in another invocation do not make it the same application.

The argument sourceResult has a **declaration-local range of result-binding occurrences**: a member must be an actual binding under the sensor-read result declaration, resolve to its independently identified application on S7 in the applicable sample window, and bind a value in that declaration's raw-count range. The range is the ValueKind; rM17 below is an individual argument value. A/B result arguments used by the join have their own local range: actual result bindings under the respective check declarations, with the declared current-assessment and recognition-result meanings. No universal result-binding kind or common input/output range is introduced.

| Application | Actual arguments and operation | Return |
| --- | --- | --- |
| M17 | Acquire sensor S7's raw indication in its independently identified sample cycle 17 | 40 counts, through result binding rM17 |
| A17 | Bind sourceResult to rM17, calibration to C3 and criterion to RA. Read rM17's returned count, apply C3, then test corrected current in [35,45] A | (40 A, true), through rA17 |
| B17 | Bind sourceResult to the same rM17, calibration to C3 and criterion to RB. Apply C3, then test corrected current <= 43 A | (40 A, true), through rB17 |
| J17 | Bind leftResult to rA17, rightResult to rB17 and joinRule to JP1. Require both recognition results true and one applicable calibration edition for both | true, through rJ17 |

C3's independently established calibration rule supplies 1 A/count for S7 and this window. Its applicability and calibration facts are part of the case, not consequences of citing C3. The numeric current channel contains numeric quantities. A declaration may return a recognition judgement unknown when an identified, admissible input lacks a deciding value; that does not insert unknown into the numeric range. An unresolved argument, a notRun application and an evaluation error remain different cases.

bA-source(A17,rM17) and bB-source(B17,rM17) obtain because the exact result-binding occurrence actually participates under the declared argument meaning. A stored “40” or an unused reference fails that test. bA-cal(A17,C3) and bB-cal(B17,C3) separately establish both calibration uses. The claim that A17 used M17's result follows from those actual bindings and the operation semantics; it does not require another transfer occurrence.

J17's declaration-local ApplicationPredicate has the complete participants <controller, leftResult, rightResult, joinRule, returnedValue>. It obtains when one completed invocation actually consumes those two result bindings, applies JP1 and returns that value. Its occurrence identity follows the invocation and its call/return extent. j17 denotes that same application occurrence; rJ17 is its distinct result binding. Two incoming lines in a drawing do not replace the five participants.

OperationalGate G17 separately applies GP1 to J17's check result and the independently identified qualification result Q17. GP1 maps true and qualification pass to pass; it maps false or qualification failure to block. Its explicit rule also maps a required unknown, error, missing or notRun result to block while retaining that source outcome and the condition for reconsideration. Here the check and qualification pass. The resulting GateDecisionResult does not establish later Work or an actual change to a weld; those use A.15.1 and A.3.4.

**Select and use the organization.** S17's constituents are the named applications, sensor/controller, calibration and rule values, their actual arguments and returns, the result bindings used as arguments, and the gate/check-result participants. R contains the four operations' declared actual argument/result bindings, j17 and the independently established GP1 check-consumption relations. Selecting every mandatory binding of those exact declarations fixes the participant closure; Q17's internal performance need not be selected. C requires exact source-result identity, complete arity, both calibration-dependent branches, their joint basis and separation of check results from gate decision. F asks which results of episode 17 support current launch reliance and which uses must reopen when that basis changes; it stops a stronger continuation at unresolved participants, relations or incomplete join input.

beta(pA)=A17 and beta(pJ)=J17. rho(qA-source)=bA-source and rho(qA-result)=rA17. rA17 is also an argument of J17, so its participant node and result-binding relation node are identified as specified in 5.1. The complete source-use walk is pM17 → qM-result=p-rM17 → qA-source → pA17 → qA-result=p-rA17 → qJ=pJ. Each step follows the corresponding application, sourceResult or leftResult incidence. At qJ retain rB17, JP1, the controller and returnedValue as well. The path shows actual source use; A17 and B17 may run in parallel.

For a concrete cut at J, choose the entry boundary {p-rA17, p-rB17, p-JP1, p-controller} and exit boundary {qJ=pJ}. The path family contains exactly the four one-incidence paths from those entries to qJ under j17's argument/application meanings. The cut kJ consists of its leftResult, rightResult, joinRule and controller incidences. It intersects each named path. Preserve the full qJ, including its returnedValue incidence, even though that incidence is not in this cut. A cut valuation may return the role-indexed tuple <left:rA17, right:rB17, rule:JP1, controller:the identified controller>; it is not a count of independent measurements.

nu0 reports the historical returns on their connection positions and has a separate channel for present reliance suitability. It retains that A and B used the same sample and calibration. sigma3 uses L with current 40 A, one ReferencePlane P with declared raw-count and corrected-current channels, historicalCalibration:C3 and currentCalibration:C3 in Evec, and the design tag consumed by this work-entry use. A/B perform their declared calibration arithmetic; a raw connection carries rM17 under the unchanged channel declaration. PublicationScope constrains use of L and supplies none of these bindings.

ConstrainTo at qA-result applies the named current-region rule. CalibrateTo cites C3 for the identified measurement claim. CiteEvidence retains the measurement evidence and the claim it supports. AttributeTo cites the actual result/argument chain supporting the provenance claim. The four annotations preserve sigma3 and the historical occurrences; an ordinary sentence can carry them when no durable replay record is needed.

**Change the shared basis and complete the join.** Suppose independently grounded C4 applies to the same raw sample and window with 1.1 A/count, and the currentness rule now requires C4 for continued use. First nu1 can reassess reliance on the unchanged S17: its historical return is still (40 A,true), while both dependent uses and their joint result require reconsideration. Preserve historicalCalibration:C3; change currentCalibration to C4 with its from/to account and required GateCrossing. Establish a changed L when the corrected current is obtained. These use changes do not rewrite bA-cal or bB-cal.

The actual dependence closure contains A, B, J, the consuming gate use and dependent publication faces. It excludes new acquisition of the unchanged raw sample and rerunning independently supported Q17. If recalculation is chosen, new A18/B18 use rM17 and C4. Their returns are (44 A,true) and (44 A,false). J18 consumes those exact result bindings and returns false; the new GP1 application returns block. Selecting the new occurrences yields another S18 under A.22, not a rewritten episode 17.

Mixed rA18/rB17 with known different calibration editions yields false under JP1 even if both individual recognition values are true. With admissible identified arguments but an unavailable deciding value, JP1 returns unknown; with an unresolved required argument, the application is not yet established. GP1 retains that distinction while blocking continuation. Refreshing only the first detected slice cannot produce the required joint result.

A useful short note is enough for immediate coordination:

> C4 now governs current reliance on sample M17. Reconsider both current checks and their JP1/GP1 decision; retain the raw sample and independent qualification. The corrected current is 44 A: the work region admits it, but the 43 A limit does not. Retain the old episode's results and cite the new application/result bindings for the recalculation.

For replay, retain the exact source/result bindings, C3/C4, rules, application extents, both refreshed results, joint decision and affected faces. The note and record report the grounds; they do not create the occurrences.

A second acquisition M18 may return the same 40 counts with another rM18; equality does not change which result A17 used. In a continuing stream application, two equal-value episodes are distinct only when its declaration and facts establish separate maximal binding extents; two log rows during one continuous binding do not. A new uncertainty or suitability valuation may preserve S; substituting a selected occurrence reopens it. Corrected 42 A remains inside the original WorkScope, while 46 A falls outside it without changing that scope's extension. A publication scope containing two admissible slices still selects no unique L or P/Evec/D. These variations apply the same identity, valuation and dependency rules.


*One first-principles P2W specialization.* A first-principles-to-work path is one path through a selected transformation-flow structure, not P2W as a whole: `U.Signature(profile=FormalSubstrate)` declaration, principle frame, mechanism, normalization, selection, planning, pre-run work-entry claim, later exact Work occurrence when one exists, and current evaluation or currentness relations occupy exact identified positions. `E.18.1` separately carries the accepted problem-side claim through whichever of those relations becomes current.

*Cooling-loop first use.* For an emergency-load review, begin with the independently grounded cooling-loop stabilization Transformation, its control-law mechanism, the measurement and setting-change WorkPlan, and any dated test-run Work that actually occurred. Select only the relations whose predicates and case facts connect the participants for that review, then apply the constraints and use frame in 5.1. A work-to-change or production claim uses its direct predicate or the local claim route stated in the Intent; proximity of the plan, run and stabilization supplies no such claim. Locate the needed path or slice. Stop at that first useful selection when no crossing, launch, publication, comparison, cycle, refresh or assurance claim is current. An emergency-load model valuation can reuse S only while its selected constituents and obtaining relations remain unchanged.

*Supply chain.* The loci run from procurement through inbound quality control and normalization to supplier selection; selection and planning inform each other; planning leads to execution and then refresh. Execution includes receipt Work admitted under `U.Work` and keeps its receipt records separate; refresh uses quality telemetry and re-emits the affected faces. When an incoming lot moves from the supplier-receipt position to the internal-QC position and its locality binding changes, record the crossing with `CrossingRef`, the A.2.6 locality fact, the rule that permits the change, and the A.21 gate. If the two labels also use different local senses, identify their F.17 cells and test the F.9 Bridge, the C.2.1 bounded-use claim, and current reliance separately. A penalty appears only when a current policy is cited through `PolicyIdRef`, the policy applies, its rule supports the penalty, and any separately needed authority relation and participants are established. Comparators remain pinned to the named `CG-Spec` value and edition.

*Neural-net functional structure.* Loci: `U.Signature(profile=FormalSubstrate)` declaration (typed tensor-operation declaration) -> mechanism (combinator algebra) -> UNM (dataset normalization; **TransportRegistry^Phi**) -> selection (architecture and hyperparameter set; Pareto set over accuracy@ratio and FLOPs@ratio) <-> planning (compute budget horizon) -> Work (exact training-run occurrences admitted under `U.Work`; any Delta is stated in a separate record) -> refresh (parity inserts; covering the actual dependency closure in 5.13). Faces pin **DescriptorMapRef.edition** and **DistanceDefRef.edition** when QD telemetry values are shown; illumination remains **report-only telemetry** by default.

*Developed product, then application - network case.* Development, later application, and further use keep separately identified TFS values when they have their own identified objects, Work occurrences, local position bindings, `DesignRunTag` boundaries, and change boundaries. A tool may be made, then used to make a chair, then the chair may be used while a person writes a text. Apply `E.18.NET` to select those TFS members and cite each exact production, use, participation, or other cross-member relation with its defining predicate and occurrence rule. The cross-member claim uses that direct occurrence, not an internal connection position from one member. If its required predicate or occurrence rule is absent, return `missing-governor`.

*FPF pattern development and use - network case.* Pattern development, application to an `EntityOfConcern`, and use-found evaluation keep separately identified TFS values when each has its own identified object, Work, positions, and local state. Apply `E.18.NET` and cite the exact use, evaluation, evidence-return, or repair-trigger relation that connects their positions, together with the pattern or declaration that defines its predicate and occurrence identity; if no such rule is available, return `missing-governor`. E.18 defines each member's internal structure; its 5.13 refresh rule covers every actually dependent use through the needed PathSlices. A reader-facing *role* label remains ordinary wording until E.10.ROLE recovers its meaning; neither that label nor a feedback arrow makes the members one TFS or supplies the cross-member relation.

**Cross-pattern boundary slice (QD archive).** A QD selector returns an archive. Under `E.18`, the selector occurrence and returned archive may occupy positions on one `PathSlice`; the archive is returned by the exact selector relation, not by the slice, and remains a set or archive rather than a hidden scalar. Under `A.20`, an archive insertion or update step may have exact constraint-validity results and a complete required-set summary; no acceptance is inferred. Under `A.21`, a comparability gate or `LaunchGate` publishes a decision only when its gate relation consumes the declared independent check results. Under `E.20`, a newly introduced selector-mechanism definition remains the meaning locus. These are four identified loci, not one prescribed work order.

