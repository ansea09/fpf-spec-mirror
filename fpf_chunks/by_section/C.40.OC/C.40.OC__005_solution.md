---
chunk_kind: "child"
pattern_id: "C.40.OC"
pattern_title: "Characterize a Subject for a Possible Change"
section_id: "C.40.OC:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.40.OC/C.40.OC__005_solution.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "C.40.OC — Characterize a Subject for a Possible Change"
  - "C.40.OC:4 — Solution"
line_start: 86343
line_end: 86474
dependencies:
  - "C.11.CRC"
  - "C.16"
  - "C.40.DC"
  - "C.40.JF"
  - "C.40.OI"
  - "C.40.PC"
keywords:
---

### C.40.OC:4 - Solution

Build a characteristic account sufficient for this inquiry, exposing every material unknown and protected coordinate.

#### C.40.OC:4.1 - Bind the characterization to one subject, use, and horizon

Name the exact subject and configuration. For an AI case, distinguish model, data, scaffold, tools, oversight, access, and surrounding operating arrangement when their differences matter. For an organization, name the organization or bounded arrangement rather than treating its chart or provider as the subject. For a person, name the person and relevant later-Work context.

State the receiving use, horizon, scenarios, and evidence window. A characterization for today's incident-review Work is not automatically valid for a future management role. A model benchmark in one configuration does not characterize another configuration with the same product label.

If those boundaries are missing, use `C.40.OI` and return only after they are adequate for the current question.

#### C.40.OC:4.2 - Select characteristics by decision difference

For each candidate characteristic, ask: if its current reading, intended reading, polarity, or uncertainty were different, could the worthwhile problem, contribution, direction, reachability, protection, advice, or next question change?

Keep it when the answer is yes. Otherwise omit it from the working account, while naming any intentionally unsearched area whose omission could reverse the result.

Start from several directions when useful:

- the receiver's required result or acceptance expectation;
- resources and burdens needed to obtain it;
- consequences for affected Systems or groups;
- conditions that must not worsen;
- the subject's current limitations or enabling strengths;
- prerequisites, complements, constraints, interactions, and transition conditions; and
- uncertainty or information whose resolution could change the next action.

A generic capability, maturity, readiness, quality, or performance catalogue is a source of questions, not an automatic closed set.

#### C.40.OC:4.3 - Define each selected characteristic and reading

For every selected characteristic, state in ordinary language:

1. what exact subject or relation bears it;
2. what the characteristic means for this receiving use;
3. its scale or admissible levels and any unit;
4. polarity—higher-is-better, lower-is-better, target-is-best, or no simple order;
5. time stance and evidence window;
6. current reading and uncertainty, or `unknown`;
7. intended, threshold, exploratory, or comparison reading;
8. explicitly protected reading or boundary when current;
9. source, method, and qualification needed for reliance; and
10. the next claim that this reading can change.

Use [`C.16`](https://github.com/ailev/FPF/blob/main/FPF-Spec.md) when a value, score, sensor indication, rating, or comparison must be made interpretable as a measurement. A display or source link can report or locate a result; reliance still needs its measurement basis and supported relation to the subject. A MethodDescription explains a way of obtaining a result without establishing that the result was obtained.

#### C.40.OC:4.4 - Orient the complete comparison coordinate set

When a finite candidate change is current, use [`C.11.CRC`](https://github.com/ailev/FPF/blob/main/FPF-Spec.md) to compare an actual or relied-on configuration `S0`, finite change `Δ`, and realizable candidate configuration `S1` under the same boundary, horizon, scenarios, constraints, interactions, transition basis, evidence window, and receiving decision.

Keep four coordinate families visible:

- **result coordinates:** what useful results may improve, worsen, or remain unchanged;
- **resource coordinates:** time, attention, capital, computation, energy, materials and other consumed means;
- **affected-System and distributional coordinates:** consequences for other Systems, groups, services, or environments and how gains and burdens are distributed; and
- **explicitly protected coordinates:** values that may not be silently exchanged for a gain elsewhere.

State required authority separately as a condition for proceeding. Include the time, fees or other resources needed to obtain or maintain permission when they matter, without treating permission itself as a consumed quantity.

Do not hide one family inside another or average incomparable scales. A Pareto-improvement claim is warranted only when the declared complete set has no worsening coordinate and at least one improving coordinate under the same basis. Otherwise use only supported language such as `beneficial`, `harmful`, `dominated`, `non-dominated`, or `indeterminate`. None of these selects the direction.

#### C.40.OC:4.5 - Return characteristic meaning and evidence to direct owners

Use the practice that owns the substantive characteristic:

- human capability and representative later-Work evidence require the applicable capability assessment for that person, receiving Work and permitted support;
- organization contribution, positions, assignments, arrangements, culture, and change remain with current organization and strategy practices;
- AI/model evaluation, data, safety, security, oversight, and deployment claims remain with their direct engineering and governance owners;
- service, flow, reliability, safety, and operability remain with operations, engineering, safety, and domain practices as applicable;
- architecture characteristics use `C.32.ACS` or `C.32.ACE` only when architecture is the bearer;
- measurement meaning and work use `C.16`; and
- evidence reliance, provenance, and currentness use their direct FPF owners.

Record an available MethodDescription as a way a result might be obtained, not as the result. Mark a source-qualified unknown when measurement, access, or currentness is insufficient.

When a reading was established for a different bearer or configuration, rely on it only when the direct practice that owns the receiving characteristic supplies a qualified transfer basis covering the receiving bearer and configuration, characteristic meaning, scale, intended use, evidence window, and uncertainty. Without that basis, keep the receiving reading `unknown` and limit the affected opportunity claim. This can finish a useful characterization. Use A.15.9 and C.11.DUA to select an evidence request only when its obtainable contribution warrants formulation, qualification, supplier Work, delivery, interpretation, delay, and displaced work.

#### C.40.OC:4.6 - Write the bounded characterization

Use ordinary prose first. This compact form can carry a characterization across a multi-practice handoff:

```text
ChangeRelevantCharacterization@Context:
  subjectAndConfiguration:
  receivingUse:
  horizonScenariosAndEvidenceWindow:
  selectedCharacteristics:
    - characteristicAndBearer:
      meaningForThisUse:
      scaleUnitPolarityAndTimeStance:
      currentReadingAndUncertainty:
      intendedOrExploratoryReading:
      protectedReadingOrBoundary:
      directOwnerAndSource:
      affectedOpportunityClaim:
  completeCoordinateSet:
    resultCoordinates:
    resourceCoordinates:
    affectedSystemOrDistributionalCoordinates:
    explicitlyProtectedCoordinates:
  materialUnknowns:
  selectedFurtherContributionIfNeeded:
  stopOrReopenCondition:
```

Include only fields that serve the receiving use; an inactive request needs no field or explanation. This local form is not a universal characteristic space, measurement result, diagnosis, criterion verdict, capability profile, decision, or authorization. Several selected characteristics may use different scales and result epistemes.

#### C.40.OC:4.7 - Choose the next truthful result

Return one of these outcomes:

- an adequate characterization ready for opportunity search or construction;
- a worthwhile obtainable measurement or evidence request tied to one affected claim;
- a comparison question with the complete coordinate set;
- a narrower characterization that supports only part of the opportunity;
- a blocker because a protected or decision-reversing reading is unavailable;
- an explicit unknown that limits the answer while the supported characterization remains useful; or
- a stop because the existing characterization already serves the receiving use.

Continue to `C.40.NU` when material opportunity-generating dimensions are now visible, to `C.40.DC` when a direction needs a finite characteristic change and support configuration, to `C.40.JF` when joint reachability is current, or to the applicable professional engagement Method when a formed advice question needs an admissible relationship. These are conditional continuations, not a fixed order.

#### C.40.OC:4.8 - Reopen the smallest affected scope

Reopen when the subject or configuration, receiving use, horizon, scenario, characteristic meaning, scale, polarity, measurement method, evidence window, protected condition, or decision-relevant unknown changes. Trace that change to the smallest affected opportunity, comparison, or advice claim.

Do not discard unaffected readings merely because one characteristic changed. Do not retain a composite maturity score when its underlying meaning or weighting changed.

#### C.40.OC:4.9 - What changes in practice

The practitioner replaces “more mature,” “AI-ready,” “senior,” or “platform-capable” with the characteristics that alter this inquiry. Current, intended, protected, and unknown readings stay distinct. Missing evidence limits the affected reading; a worthwhile further contribution becomes a directed request. Later comparison retains benefits, burdens, affected Systems, distribution, and protections on their own scales.

