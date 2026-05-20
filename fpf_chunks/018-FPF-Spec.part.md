| CC-C26.2.4 | The QL cue / formal cue is named if QL wording is retained. |
| CC-C26.2.5 | Persistence class, decay or refresh condition, and reprobe cost are named when the claim is not momentary. |
| CC-C26.2.6 | The minimal supported claim is stated. |
| CC-C26.2.7 | At least one substantive ordinary rival explanation is named. |
| CC-C26.2.8 | The compound-state decomposition separates whole system, subsystems, local readings, factorable part, and coordination residue when the distributed-state reading is load-bearing. |
| CC-C26.2.9 | Any survey, dashboard, report, API response, or policy sentence is typed as representation, carrier, or export, not as the distributed state itself. |
| CC-C26.2.10 | Probe / measurement approximation, attempted export, faithful-enough criterion, loss cause, and higher-fidelity export possibility are stated when export or measurement carries the claim. |
| CC-C26.2.11 | Export loss is stated when the claim depends on export that is not faithful enough for the declared use. |
| CC-C26.2.12 | The evidence posture is stated when the claim is reused, contested, or higher consequence. |
| CC-C26.2.13 | Formal measurement uses `C.16`; evidence and assurance use `A.10` or `B.3`; bridge loss uses `F.9`. |
| CC-C26.2.14 | The pattern inherits `QL-NQ` from `C.26` and does not mint `U.DistributedState`. |

### C.26.2:8 - Common Anti-Patterns and How to Avoid Them


| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Group mind claim | The text says the team, market, service, or organization knows or wants something. | Rewrite as an evidence-bound state reading over a collective bearer during a window. |
| Survey-as-state | A survey answer is treated as the distributed state. | Treat the survey as probe result, emitted output, or evidence carrier and ask what it lost or changed. |
| Tacit skill overreach | A craft skill or team vibe is called distributed state. | Require coordinated work, carriers, time window, and rival explanations. |
| Routine mistaken for state | A playbook explains the action, but the text claims latent alignment. | Name the routine and keep the claim requiring additional evidence out. |
| Timeless culture | A momentary observation becomes a durable culture claim. | State window, persistence support, decay, and reprobe condition. |

### C.26.2:9 - Consequences

This pattern lets FPF discuss enacted collective states without mysticism. It gives authors a disciplined way to use traces, routines, coordinated work, and export loss in one minimal claim.

The cost is that many attractive claims become narrower. That is the point. Minimal evidence-bound claims are often more useful than confident but ungrounded stories.

### C.26.2:10 - Rationale

Existing FPF patterns can carry parts of the support requirement, but no single ordinary pattern makes the combined minimal distributed-state claim easy to write. `A.15` carries work, `A.10` and `B.3` carry evidence and assurance, `F.9` carries export loss, and `C.16` carries formal measurement. C.26.2 coordinates those neighboring-pattern applications for the specific case where coordinated work evidences a non-articulated state.

### C.26.2:11 - SoTA-Echoing

| Pattern claim | Practice source | Pattern implication | Adoption stance |
| --- | --- | --- | --- |
| Coordinated work can evidence state-like organization without reducing that state to one participant report. | [Representing distributed cognition in socio-technical systems](https://www.sciencedirect.com/science/article/abs/pii/S2405896316321164), team cognition, shared mental models, transactive memory, [organizational routine dynamics resources](https://routines.broad.msu.edu/resources), work traces, and socio-technical systems. | Make these the primary grounding; infer only minimal evidence-bound state readings from carriers, traces, and work. | Adapt as primary non-QL grounding. |

| Probe/export conditions can change or thin the state reading. | [Quantum-like modeling in biology with open quantum systems and instruments](https://www.sciencedirect.com/science/article/pii/S0303264720301994) / [arXiv](https://arxiv.org/abs/2010.15573) and [Open Systems, Quantum Probability, and Logic for Quantum-like Modeling in Biology, Cognition, and Decision-Making](https://www.mdpi.com/1099-4300/25/6/886). | Activate QL only when probing, formalizing, exporting, or bridging changes or loses load-bearing structure. | Adapt as secondary modeling support. |
| Contextual judgment and previous judgments can alter the state being reported. | [Quantum Cognition](https://www.annualreviews.org/content/journals/10.1146/annurev-psych-033020-123501). | Treat surveys, interviews, reports, and dashboards as possible probes of enacted state, not faithful copies by default. | Use as probe/export caution with ordinary evidence routes. |
| Some sequential data can be carried by classical instrument models. | [Quantum-like Cognition in Process Theories: An Analysis](https://arxiv.org/abs/2604.08604). | Keep non-necessity visible: EDSE is a useful FPF evidence pattern, not proof that only QL formalism works. | Use as rival-model discipline. |
| Carrier plurality is normal in operational evidence. | Observability, incident-management, audit, work-trace, and assurance practice. | Use logs, traces, dashboards, meeting records, commitments, artifacts, and operational changes as carriers, not as faithful copies of the whole state. | Adopt through `A.10` / `B.3` routes. |

Worked-slice discipline from these rows:

- ground the claim in coordinated work before QL vocabulary appears;
- state the evidence carriers and time window before stating the state reading;
- name rivals before retaining a distributed-state claim;
- treat survey/report/dashboard outputs as carriers or probes, not as the state;
- escalate to measurement, evidence, assurance, or authority patterns when the use requires measurement, evidence, assurance, or authority support.

### C.26.2:12 - Relations


- Builds on: `C.26`, `A.15`, `A.10`, `B.3`, `F.9`, `C.16`, `E.17.EFP`, `C.11`.
- Coordinates with: `C.26.1` when the probe changes the state being evidenced; `C.26.3` when the coordinated state is part of viability-envelope regulation.
- Does not mint: `U.DistributedState`, a bearer-independent group entity, or a durable state beyond declared evidence and time window.
- Name posture: `Enacted Distributed State Evidence` names an evidence-bound `U.Episteme` reading over work carriers, not `Distributed Mind`, `Collective Consciousness`, `Social Field`, or `Organization Knows`.

### C.26.2:End
## C.26.3 - Viability-Envelope Boundary Regulation

> Type: Architectural pattern
> Status: Stable
> Normativity: Normative unless explicitly marked informative

### C.26.3:1 - Problem frame

Use this pattern when architecture work is maintaining, recovering, or changing viable operating ranges across boundaries. The working problem is not "optimize one metric"; it is "keep a bundle of characteristics inside a viable region while disturbances, probes, actuators, boundary conditions, and operating regimes change."

Most envelope work covered by this pattern is ordinary control, quality, SRE, causal, or work discipline, not QL. FEP, allostasis, and active inference are source analogies for envelope discipline, sensor and action coupling, and partial observability; ordinary control, SRE, quality-bundle, causal, and work patterns remain primary unless probe, order, export, or coarsening cue remains load-bearing after ordinary viability, quality, dynamics, measurement, boundary, and work patterns have carried their part.


| Working surface | Value |
| --- | --- |
| Primary reader | Architect, platform lead, reliability lead, product manager, or operations lead preserving viability under changing conditions. |
| Governed object | A viability-envelope claim or plan over a declared viability bearer, with protected promise/function named separately. |
| Governed move | Name the bearer, envelope variables, disturbance, sensors/probes, actuators, boundary condition, adaptation cost, and failure mode. |
| Outside work | One-metric quality tuning, generic control theory, biological proof, full FEP doctrine, and ordinary feedback without an envelope/boundary claim. |
| What changes in practice | The team stops treating one dashboard value as viability and designs the actual envelope-regulation move. |

Plain glosses:
- `viability bearer`: the `U.System`, collective system, delivery system, role configuration, organism-as-system, or explicitly modelled market slice whose viable range is being regulated.
- `protected promise / function`: the `U.PromiseContent`, stakeholder value, function, operating regime, commitment payload, or delivery promise the bearer is trying to keep viable.
- `service situation`: an `A.6.8` facet-binding lens that identifies access point, delivery system, provider principal, promise content, commitment, delivery work, and evidence; it is not itself a new root bearer unless the relevant system facet is declared.
- `viability envelope`: the region where the bearer can still keep the relevant promise or function, across several dimensions.
- `envelope variable`: one characteristic that must stay within bounds, such as latency, reliability, support load, compliance exposure, safety margin, energy, or operator attention.
- `actuator`: a work move that can change the situation, such as cache policy, throttle, staffing, routing, bridge rewrite, protocol, access, escalation, or measurement design.
- `allostasis`: preserving function by changing settings, environment, boundary condition, actuation, or operating regime when circumstances change.

### C.26.3:2 - Problem

Teams often collapse viability into one dashboard value or fixed target. They optimize latency and damage operator load. They improve availability and increase compliance exposure. They preserve one metric while exhausting the team, hiding risk, or making recovery slower.

A second failure is passive sensing. A metric, probe, dashboard, alert, or health check is treated as a neutral window into viability, even when it changes behavior, hides unmeasured dimensions, or becomes an actuator through Goodhart effects.

A third failure is static stability. Teams say "keep the system stable" as if stability always means holding one internal variable fixed. In real architecture work, preserving viability may require changing environment, access, staffing, caching, throttling, routing, protocol, context split, or measurement design.

### C.26.3:3 - Forces

| Force | Tension |
| --- | --- |
| Bundle vs scalar | Viability usually concerns a bundle, but dashboards often expose one or two proxies. |
| Stability vs change | The system may preserve function by changing internal settings, external environment, boundary conditions, or operating regime. |
| Sensing vs actuation | Measurements may be sensors, probes, or actuators, depending on how they change behavior. |
| Ordinary control vs QL lens | `C.25`, `U.Dynamics`, `A.6`, `A.15`, and `C.16` remain primary patterns; QL enters only for probe, frame, export, or coarsening cue. |
| Light use vs dynamics detail | Rate, inertia, damping, actuator latency, and effort matter only when load-bearing. |

### C.26.3:4 - Solution

Use `C.25` / `U.Dynamics` alone for ordinary envelope work. Use C.26.3 only when the viability-envelope reading is distorted or constrained by probe, frame, export, coarsening, or incompatible representation cue. Otherwise use ordinary viability, quality-bundle, dynamics, measurement, boundary, and work patterns.

Start with this recognition note:

| Mini-entry | Question |
| --- | --- |
| Viability bearer | Which `U.System`, collective system, delivery system, role configuration, organism-as-system, or explicitly declared bearer is being kept viable? |
| Protected promise / function | Which `U.PromiseContent`, stakeholder value, function, operating regime, commitment payload, or delivery promise is protected? |
| Envelope variables | Which two to five variables matter, rather than one comfort scalar? |
| Disturbance | What pushes the bearer outside the envelope? |
| Sensor / probe / actuator | What reads the situation, and what can actually change it? |
| Trade-off / failure | What gets worse, what cost is paid, and what failure would show the envelope move did not work? |

Use the fuller envelope-regulation record below when the viability reading will change a metric, actuator, boundary, staffing, routing, promise, or evidence decision.

Full envelope-regulation record:

| Field | Question |
| --- | --- |
| Viability bearer | Which `U.System`, collective system, delivery system, role configuration, organism-as-system, or explicitly declared bearer is being kept viable? |
| Protected promise / function | Which `U.PromiseContent`, stakeholder value, function, operating regime, commitment payload, or delivery promise is protected? |
| Service situation facets, if used | Which `A.6.8` facets are involved: access point, delivery system, provider principal, promise content, commitment, delivery work, and evidence? |
| Envelope variables | Which characteristics or quality-bundle dimensions define viability? |
| Viable region / bounds | What counts as inside, near edge, degraded, or outside the envelope for this use? |
| QL cue or formal cue if retained | Which probe, order, export, coarsening, incompatible-frame, open-information-system update law, probe-frame relation, export admissibility, or measurement-changing-state cue remains after ordinary viability patterns are active? |
| Disturbance | What pushes the bearer outside the envelope? |
| Sensors / probes | Which metric, dashboard, alert, health check, review, trace query, observation setup, or probe reads the envelope, and can it change behavior or hide unmeasured dimensions? |
| Available actuators | What work, method, boundary action, staffing change, cache, throttle, bridge, access, protocol, or routine can change the situation? |
| Boundary condition preserved / changed | Which access, ownership, context, interface, promise, or environment condition matters? |
| Trade-off posture | Which envelope dimension is protected, relaxed, delayed, made more expensive, or deliberately held constant? |
| Adaptation cost | What is spent, delayed, damaged, risked, or made harder by the adaptation? |
| Failure mode | What breakdown, drift, unsafe persistence, or loss of viability shows that the move failed? |

#### C.26.3:4.1 - Homeostasis and allostasis reading

`Homeostasis` means keeping a parameter or bundle inside viable bounds. `Allostasis` means preserving functioning by changing internal settings, external environment, boundary conditions, actuation, or operating regime when circumstances change.

Do not say that all architecture is homeostasis. Say that some architecture decisions are viability-envelope decisions.

#### C.26.3:4.2 - Finish conditions

This pattern emits one of these results:

| Result | Meaning |
| --- | --- |
| Envelope-regulation claim | State bearer, protected promise/function, envelope variables, viable region/bounds, disturbance, sensors/probes, actuators, boundary condition, trade-off posture, authority, latency, adaptation cost, and failure mode. |
| Actuator redesign | Change cache, throttle, routing, staffing, protocol, access, bridge, escalation, measurement, or context split because the existing actuator cannot keep the envelope viable. |
| Measurement/probe redesign | Redesign a dashboard, alert, health check, readiness score, or review process because it distorts the envelope it reports. |
| Ordinary neighboring-pattern application | Use `C.25`, `C.16`, `A.6`, `A.15`, `U.Dynamics`, `C.18`, `C.19`, or `A.19` when the QL cue is not load-bearing. |
| No envelope claim | Drop the viability-envelope wording when bearer, protected promise/function, viable region/bounds, disturbance, actuators, adaptation cost, and failure mode cannot be stated. |

#### C.26.3:4.3 - Metric-induced distortion

Treat sensors, probes, dashboards, alerts, and metrics as possible participants in the viability relation, not as neutral windows by default.

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| Metric-as-envelope | A proxy is treated as the whole envelope. | Recover bearer, protected promise, full envelope, unmeasured dimensions, and admissible use. |
| Goodharted viability | Actors optimize measured slots while damaging unmeasured survivor relations or future adaptability. | Route probe-caused behavior through `C.26.1`; add evidence for unmeasured envelope dimensions. |
| Actuator overfit | An action preserves one parameter while pushing another cost, latency, boundary relation, or promise outside bounds. | Add trade-off posture, actuator authority, latency, adaptation cost, and failure mode. |

#### C.26.3:4.4 - Conditional dynamics detail

When rate, acceleration, second-order change, inertia, damping, resistance, effort, or actuator strength is load-bearing, state:

- what rate or acceleration matters;
- what slows or speeds the change;
- whether the rate of change itself is changing, rebounding, overshooting, or damping out;
- which inertia is useful and which is harmful;
- which actuator can actually change the envelope fast enough;
- which evidence shows the dynamic posture.

If those variables are not load-bearing, do not force dynamics machinery into the case. The short recognition note or the full envelope-regulation record is enough.

#### C.26.3:4.5 - Governed object and operational sequence

The governed object is a viability-envelope claim or plan. It is not a generic quality score, not a control-theory survey, and not a biological analogy. The claim says that some bearer can keep a promise, function, or operating regime viable only if a set of variables remains inside a usable region under declared disturbances, probes, sensors, actuators, boundary conditions, and adaptation costs.

The governed move is to turn a one-scalar stability story into an inspectable envelope-regulation decision.

Action path:

1. Name the viability bearer and the promise or function being preserved; if service or market language is used, declare whether the bearer is a collective `U.System`, delivery system, trace population, evidence set, or relevant `A.6.8` facet-binding before treating the situation as a bearer.
2. Name the envelope variables and the viable range or qualitative boundary for each.
3. Name the disturbance or regime change.
4. Name sensors/probes and say whether they only report, also frame, or also change behavior.
5. Name available actuators and who or what can enact them in time.
6. State the boundary condition being preserved or changed.
7. State the trade-off posture and adaptation cost.
8. State the failure mode and re-probe/destabilization condition.
9. Add dynamics detail only if rate, inertia, damping, latency, resistance, or acceleration changes the decision.

Ordinary output: produce a viability-envelope record with envelope variables and viable region, a disturbance/sensor/actuator map, and a trade-off, adaptation, and failure posture that tells the practitioner what changes in the work.

The output should tell a practitioner what changes in the work: redesign the metric, change cache policy, adjust staffing, reroute traffic, split or merge a context, add a bridge note, change an escalation promise, or drop the envelope claim.

#### C.26.3:4.6 - Viability envelope record

A usable envelope record is a pattern-local writing card, not a constructor. Use the fields below when envelope regulation is load-bearing:

```text
bearer: ...
protected promise or function: ...
envelope variables: ...
viable region: ...
disturbance: ...
sensors or probes: ...
available actuators: ...
actuator authority and latency: ...
boundary condition: ...
trade-off posture: ...
adaptation cost: ...
failure mode: ...
re-probe or destabilization condition: ...
```

The record is not `U.ViabilityEnvelopeRegulation`, not a new kernel kind, and not a universal architecture constructor. It is a pattern-local normal form for writing envelope work clearly.

Well-formedness constraints:

- the bearer is a declared `U.System`, collective system, delivery system, role configuration, organism-as-system, explicitly modelled market slice, or other explicitly bounded bearer of viability;
- service-situation language identifies its `A.6.8` facets rather than treating the situation label as a root bearer by itself;
- at least two envelope dimensions are visible when the claim says "viability" rather than one ordinary metric;
- at least one actuator is named when the text proposes regulation rather than only diagnosis;
- the actuator has an authority and latency story, otherwise the recommendation is only a wish;
- the adaptation cost is named, because allostasis hides cost when phrased as "stability through change";
- the failure mode is named, because viability is otherwise indistinguishable from optimism.

#### C.26.3:4.7 - Sensor, probe, actuator, and metric split

Do not let one dashboard value stand for the whole envelope.

| Role | Viability-facing question |
| --- | --- |
| Envelope variable | Which quality, resource, promise, risk, or operating dimension is inside/outside viable range? |
| Sensor | Which metric, alert, trace, health check, survey, review, or observation reports part of the envelope? |
| Probe | Which measurement setup, dashboard, readiness check, review, experiment, or incident query may change behavior or expose hidden dimensions? |
| Actuator | Which cache, throttle, routing rule, staffing change, protocol, escalation, access change, bridge rewrite, or context split can change the envelope? |
| Boundary condition | Which access, ownership, context, interface, promise, environment, or information constraint shapes the envelope? |
| Adaptation cost | Which latency, risk, effort, attention, support load, compliance exposure, energy, trust, or future flexibility is spent? |

A metric value or dashboard carrier is not an actuator by itself. A measurement regime, publication act, alerting workflow, or governance routine may function as an actuator when the system responds through work: routing changes, escalation changes, staffing changes, cache policy changes, access changes, or boundary changes. An actuator can damage another envelope variable while repairing the one that triggered the work.

#### C.26.3:4.8 - Homeostasis, allostasis, and architecture work

Homeostatic wording is useful when the work preserves one variable or bundle inside a stable range. Allostatic wording is useful when the work preserves function by changing settings, boundary conditions, environment, access, staffing, routing, protocol, cache policy, or operating regime.

Use the minimal reading that carries the case:

| Reading | Use when | Practical output |
| --- | --- | --- |
| Scalar quality repair | One characteristic or Q-bundle dimension is enough. | Apply `C.25`, measurement patterns, or evidence patterns as appropriate. |
| Homeostatic envelope | The target is to keep a bundle inside a stable range under disturbance. | State variables, range, disturbance, sensor, actuator, and failure mode. |
| Allostatic envelope | Function is preserved by changing settings, boundary, environment, access, work routine, or operating regime. | State what changes, why function is preserved, and what cost moves elsewhere. |
| Probe-coupled viability | The measurement, dashboard, review, or readiness check changes the envelope it reports. | Coordinate with `C.26.1`. |
| Enacted viability state | Coordinated work evidences the envelope state better than one report. | Coordinate with `C.26.2`. |

Do not call every adaptation allostasis. The term earns its place only when stability-through-change is the useful architecture reading.

#### C.26.3:4.9 - Case bank and near misses

| Case | Supported C.26.3 reading | Near miss / reroute |
| --- | --- | --- |
| Checkout cache under spike | Cache aggressiveness preserves latency but increases stale payment-failure status and support load. | If only cache latency is at issue, use ordinary performance and quality-bundle patterns. |
| Smart-building energy control | Energy, comfort, privacy, occupancy, and abrupt weather changes form one envelope with sensors and actuators. | If the case only tunes one thermostat setting, use ordinary control/measurement language. |
| Incident staffing | Adding responders preserves recovery time but increases coordination overhead and error risk. | If staffing is merely a work allocation issue, use `A.15` / planning patterns. |
| Compliance exposure | A fast remediation path lowers outage time but increases evidence gaps and audit risk. | If audit evidence is primary, apply `A.10` or `B.3`; keep C.26.3 only for envelope trade-off. |
| Service boundary split | Splitting a service reduces deployment coupling but increases bridge loss and operational support transfer cost. | If the issue is only semantic bridge loss, use `F.9`; if the split changes the envelope, use C.26.3. |
| Body-temperature analogy | Function may be preserved by clothing, room air, activity, or exposure, not only internal heat production. | Use only as explanatory analogy; do not make biology the proof for software. |

#### C.26.3:4.10 - Source-to-pattern translation

Allostasis, active inference, FEP, Markov blankets, and computational-boundary sources are useful here only after translation into FPF architecture terms:

| Source-side term | FPF-facing translation |
| --- | --- |
| Homeostasis | Keep one parameter or bundle inside viable bounds. |
| Allostasis | Preserve function by changing settings, environment, boundary condition, actuation, or operating regime. |
| Active inference / perception as action | Measurement, sensor placement, and action have cost and can change later state estimates. |
| Markov blanket / computational boundary | Boundary as a statistical or functional separation for measure/model/act; not a new substance. |
| Criticality / metastability | Stability may be regime-bounded and fluctuation-bearing, not one final fixed point. |
| Expected free energy / precision control | Information gathering, action, and confidence have cost; use only when those costs change the architecture decision. |

This translation keeps the pattern practical for architects. The reader should be able to move from a source line to an action: change a metric, change a probe, change an actuator, change a boundary condition, state a trade-off, or reroute.

### C.26.3:5 - Archetypal Grounding


Tell: A platform team tries to preserve checkout latency during a traffic spike. The first move is to increase cache aggressiveness. Latency improves, but support load rises because stale payment-failure status causes confused customer contacts.

Show, System side: the viability bearer is the checkout/payment service situation. Envelope variables include latency, payment correctness, support load, customer-promise reliability, and operator attention. Actuators include cache policy, retry policy, routing, dashboard query, escalation promises, and context bridge changes.

Show, Episteme side: the supported claim is not "latency is the viability state." It is an envelope-regulation claim: latency was preserved by an actuator that damaged another envelope dimension. The repair is to state the trade-off, adaptation cost, actuator authority, and failure mode.

### C.26.3:6 - Bias-Annotation

This pattern biases authors against scalar comfort. That bias prevents "green dashboard" from replacing viability.

It also biases authors toward actionable architecture work. The pattern asks who or what can actually change the boundary, access, protocol, staffing, cache, throttle, bridge, or measurement setup, and how quickly that action can matter.

The pattern may feel too broad if it is applied to every quality concern. It is not for every quality concern. Use `C.25` alone when one quality bundle or metric can be handled without envelope, disturbance, boundary condition, actuator, adaptation cost, or viability failure mode.

### C.26.3:7 - Conformance Checklist

| ID | Check |
| --- | --- |
| CC-C26.3.1 | The viability bearer is named. |
| CC-C26.3.2 | The protected promise or function is named. |
| CC-C26.3.3 | Envelope variables or quality-bundle dimensions and the viable region / bounds are named. |
| CC-C26.3.4 | Disturbance class and scenario/window are named. |
| CC-C26.3.5 | Sensors/probes and their possible behavior-changing or dimension-hiding effects are named when measurement carries the envelope claim. |
| CC-C26.3.6 | Available actuators and actuator authority/latency are named. |
| CC-C26.3.7 | Boundary condition, trade-off posture, and adaptation cost are stated. |
| CC-C26.3.8 | Failure mode and re-probe/destabilization condition are stated. |
| CC-C26.3.9 | Metrics or dashboards are not treated as the envelope itself. |
| CC-C26.3.10 | The QL cue / formal cue is named if QL wording is retained. |
| CC-C26.3.11 | QL wording appears only when probe, order, export, coarsening, or incompatible frame interaction remains load-bearing. |
| CC-C26.3.12 | Rate/inertia/damping/effort and second-order dynamics variables appear only when load-bearing. |
| CC-C26.3.13 | Homeostasis, allostasis, active inference, and Markov-boundary wording are translated into FPF-facing architecture terms before they carry the claim. |
| CC-C26.3.14 | The pattern does not mint `ViabilityParameter`, `HomeostasisOntology`, or a new control ontology. |

### C.26.3:8 - Common Anti-Patterns and How to Avoid Them


| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| One metric as viability | Availability, latency, or score stands for the whole envelope. | Add the bearer, protected promise, other dimensions, and failure mode. |
| Fixed setpoint thinking | Stability means one variable must never move. | Ask whether allostasis preserves function by changing settings, environment, boundary, or regime. |
| Passive sensor assumption | A dashboard is treated as neutral even after it changes behavior. | Use `C.26.1` and evidence patterns. |
| Actuator without authority | The text recommends a change no one can enact in time. | State actuator authority and latency. |
| Biological proof jump | Homeostasis or FEP language is used as proof for software or organizations. | Treat it as modeling discipline and apply existing FPF patterns to claims. |

### C.26.3:9 - Consequences

This pattern helps architects see stability-through-change. It supports decisions such as throttling, staffing, routing, protocol redesign, context split/merge, cache changes, measurement redesign, and escalation changes as envelope-regulation moves.

The cost is that simple metric stories become less simple. That is acceptable when the metric story hides the actual viability relation.

### C.26.3:10 - Rationale

Ordinary quality-bundle work does not always show boundary conditions, actuators, disturbances, adaptation cost, and failure modes together. C.26.3 coordinates those elements while preserving ordinary FPF patterns.

The QL lens is secondary. It matters when the way viability is probed, exported, or coarsened changes the state reading or admissible use of the representation.

### C.26.3:11 - SoTA-Echoing

| Pattern claim | Practice source | Pattern implication | Adoption stance |
| --- | --- | --- | --- |
| Viability maintenance is not fixed-value homeostasis only; stability can be relational, variational, dynamic, allostatic, metastable, and resilient. | [Conceptual foundations of physiological regulation incorporating the free energy principle and self-organized criticality](https://www.sciencedirect.com/science/article/pii/S0149763423004281). | Use viability envelopes and stability-through-change; reject one-scalar optimization and "all architecture is homeostasis." | Adapt as architecture-facing envelope discipline. |
| Action and perception are coupled under partial observability and cost. | [Active inference as a theory of sentient behavior](https://www.sciencedirect.com/science/article/pii/S0301051123002612). | Treat sensors, probes, dashboards, and actuators as part of the envelope relation when they change behavior or viability. | Adapt for measurement-as-action and planning cost. |
| Active-inference engineering already appears in energy/building control under privacy, partial observability, evolving conditions, and abrupt changes. | [Active Inference for Energy Control and Planning in Smart Buildings and Communities](https://arxiv.org/abs/2503.18161). | Use engineering examples cautiously: they show the kind of control problem, not settled FPF doctrine. | Use as emerging engineering anchor. |
| Boundaries can be statistical/computational descriptions of what a system can measure, model, and affect. | [The Computational Boundary of a Self](https://philpapers.org/rec/LEVTCB-3) and [The Markov blankets of life](https://philarchive.org/rec/KIRTMB). | Name boundary conditions and information constraints without reifying a boundary substance. | Adapt with map-territory caution. |
| Excess Bayesian / active-embodied inference shows the cost of moving sensor, body, instrument, or access point to obtain a discriminating observation. | [Connecting the free energy principle with quantum cognition](https://www.frontiersin.org/articles/10.3389/fnbot.2022.910161/full). | Treat probe placement, access placement, and observation cost as part of viability-envelope work when they change the decision. | Adapt for probe/action cost, not as a replacement for ordinary Bayesian or active-inference routes. |
| Platform and software engineering already treats many quality concerns as trade-off bundles. | Reliability, incident, platform, compliance, energy, support, operator-load practice, and [Google SRE SLO / error-budget practice](https://sre.google/workbook/implementing-slos/), coordinated with `C.25`. | Make the quality bundle explicit and state actuator authority, latency, adaptation cost, and failure mode. | Adopt through FPF quality-bundle routes. |


Worked-slice discipline from these rows:

- state the envelope before importing source terminology;
- translate source terms into FPF architecture objects;
- keep sensors, probes, actuators, and metrics distinct;
- state adaptation cost and failure mode;
- apply ordinary quality and measurement patterns to one-scalar quality concerns.

### C.26.3:12 - Relations

**C.27 temporal-claim relation.**

- C.27 may flag: braking, throttling, cadence, recovery, or stabilization moves in claims such as slow rollout protecting support capacity, request throttling preventing collapse, or cadence change preserving attention/team health.
- This pattern keeps: viability bearer, protected promise/function, viable region, disturbance, sensor/probe/action split, adaptation cost, and failure mode.
- Non-admissible use: stabilization wording is not a viability envelope, and C.27 is not the pattern for all stability-through-change claims.
- Exit: if the live claim is only better quality, healthier team, or more resilient service without a declared viability envelope, use C.25, E.13, or the relevant quality/proxy/value pattern rather than C.26.3 or a C.27 profile.


- Builds on: `C.26`, `C.25`, `U.Dynamics`, `A.6`, `A.15`, `C.16`, `A.10`, `B.3`, `A.3`, `A.19`, `C.18`, `C.19`.
- Coordinates with: `C.26.1` when sensors, probes, dashboards, or metrics change represented state; `C.26.2` when coordinated work evidences the envelope state.
- Does not replace: ordinary quality-bundle patterns, generic control theory, full FEP doctrine, or biological homeostasis claims outside FPF bridge and loss discipline.
- Name posture: `Viability-Envelope Boundary Regulation` names architecture work over a viability envelope and boundary/action conditions, not `Homeostasis Pattern`, `Allostasis Doctrine`, `Control Ontology`, `Quality Optimization Pattern`, or `Viability Substance`.

### C.26.3:End
## C.27 - Temporal Claim Adequacy: State Readings, Temporal Trends, and Intervention-Sensitive Temporal Change


> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Temporal claim adequacy.

**Governed object.** C.27 governs authored temporal claims: descriptions in prose, plans, benchmark lines, dashboards, method notes, promises, or explanations that treat state, rate, rhythm, recovery, braking, coasting, redirection, stabilization, or rate-change as sufficient for some use.

**Described-system, description, and carrier discipline.** The described system, work, practice, method, service, or benchmark is not the C.27 record. A `Dyn2TemporalClaimAdequacyCard` or `Dyn2TemporalClaimProfile` is an authored description of temporal-claim adequacy. A document, table, page, report, or card may carry that description; it is not the temporal claim, not the dynamic system, and not the work trace.

**Use-context and basis discipline.** When this pattern says `supportedUse`, it means the decision, plan, diagnosis, comparison, publication, promise, assurance-facing relation, or other practical use that this exact C.27 record can carry given its claim posture, basis, windows, resistance or cost statement, and reopen condition. `unsupportedUse` means one nearby downstream claim, effect, or use that this exact record does not carry. These fields do not create permission; they state the pragmatic reach of the authored temporal-claim description.

Bare "support" should not do hidden ontology work in C.27. Use `supportedUse` and `unsupportedUse` only for the pragmatic reach of a temporal-claim record; use `evidence basis`, `model basis`, `source basis`, or `assumption` for the reason a reading is credible; use `RouteRef` or a named FPF pattern relation when an existing FPF pattern governs the other question.

**Boundary-crossing claim use.** The object remains an authored temporal claim. What changes is the use context: the claim is used as citable basis outside the immediate local discussion, published, benchmarked, promised, assured, made durable rationale, repeated in a reusable method description, used in a gate/public dashboard/Part G pack, or carried across context or scale. Casual reuse in a neighboring chat is not enough by itself. Boundary-crossing use is what can require a `Dyn2TemporalClaimProfile`.

**Use this pattern when** a claim about speed, rhythm, throughput, recovery, convergence, rollout, adoption, braking, coasting, redirection, or stabilization is used to change action and therefore needs effort, window, resistance, basis, supported-use, unsupported-use, and reopen discipline.

**Do not use this pattern when** the temporal wording is ordinary prose, a state reading or snapshot, a rate reading or trend reading whose measurement construction is enough, a formal `U.Dynamics` model, an actual work trace, a benchmark harness, a service promise, a quality judgement, or a residual quantum-like probe case without an intervention-sensitive temporal claim.

**C.27 in 60 seconds.** Use C.27 only if:

1. temporal wording is used to justify action, comparison, budget, gate, promise, assurance, or an explicit relation to another FPF pattern;
2. the difference between state, rate, and rate-change changes admissible use;
3. the text can name at least target, intervention, window, resistance or cost, basis, supported use, and unsupported use or reopen trigger.

Otherwise stop at ordinary prose, a Dyn0 state reading, a Dyn1 rate reading or trend reading, C.16 measurement discipline, `U.Dynamics` model discipline, or the existing FPF pattern that governs the other question.

For local diagnosis or planning, C.27 usually ends with one `Dyn2TemporalClaimAdequacyCard`. Plain references are enough while the use stays local. A local card should normally fit in 5-9 short lines; if it does not, clarify the claim, narrow it, or cite the existing FPF pattern that governs the other question. `RouteRef`, `C16RouteRef`, `G9ParityPlanRef`, and similar references appear only when the use is load-bearing beyond the local note.

**Quick refusals.** "Backlog is 120" is Dyn0; no C.27 record. "Backlog fell 20/week" is Dyn1, with C.16 if the measure is load-bearing; no C.27 record unless a rate-change use appears. "This section accelerates orientation" is ordinary prose unless the `PublicationUnit` carries that acceleration claim as method-effectiveness evidence.

**Dyn2 is not maturity.** Dyn2 classifies the use made of an authored temporal claim, not the system, team, method, or service being described. Higher `DynOrder` is not better; it only says what the authored temporal claim treats as sufficient for supported use.

**Local refresh boundary.** A local card carries only a reopen, downgrade, or pattern-reference condition. G.11, B.3.4, and assurance refresh discipline become relevant only when the temporal claim is public, Part G-facing, assurance-facing, or otherwise durable beyond local planning/diagnosis.

### C.27:1 - Problem frame
#### C.27:1.1 - Causal-use boundary

`C.27` can say that a temporal claim is dynamic, intervention-sensitive, rate-sensitive, inertia-sensitive, braking-sensitive, coasting-sensitive, or rhythm-sensitive. When the temporal claim already depends on causal-use question, `causalInterventionSpecRef`, comparator/counterfactual, estimand, assignment or intervention window, causal follow-up window, outcome measure, `causalAssumptionSetRef`, `rivalCauseSetRef`, identification strategy, realizability posture, `CausalUseEvidenceDesignRecord`, supported causal use, or unsupported causal use, cite `C.28` as the governing causal-use source.


What changes in practice: a sentence such as "this effort changes adoption speed" may remain a `Dyn2` temporal claim, but "this intervention causes adoption speed to improve" must also declare its `C.28` causal-use class and causal-use support.

What this does not authorize: `C.27` does not estimate causal effects, certify counterfactual comparisons, or judge counterfactual sampling realizability; it keeps temporal claim adequacy, rate-change, effort, inertia, rhythm, braking, coasting, and intervention-sensitive temporal wording.


FPF already has established constructs and patterns for time, work, resources, measurement,
CharacteristicSpace, dynamics laws, planning, publication, and quantum-like
probe and frame issues. What is missing is a cheap claim-adequacy lens for authored
temporal claims when a state/rate reading is used as if it supplied the basis for a
rate-change, rhythm-change, regime-change, braking, coasting, redirection,
recovery, or stabilization claim.

The first-minute working situation is simple: a manager, method author,
researcher, operator, or agentic-tool planner says that something should speed
up, slow down, converge faster, recover sooner, sustain rhythm, improve
throughput, accelerate learning, brake risk, or redirect effort. FPF should
help the reader ask whether the claim is only a state reading, only a
rate/trajectory reading, or an intervention-sensitive claim about changing a
rate under effort, resistance, rhythm, feedback, constraint, or cost.

What goes wrong if missed: the text measures or names a rate and then behaves
as if it knows how to change that rate. This produces speed-only management,
benchmark theater, hidden promises, causal overclaim, effort-free acceleration,
rhythm-as-vibe, and false QL relevance.

The intended FPF gain is not "add physics metaphors". The gain is a compact
thinking-and-action discipline for cases where speed talk hides effort,
timing, resistance, evidence, scale, reversibility, and admissible use.

Anti-case: if a phrase uses speed or rhythm only as ordinary explanatory prose,
or if a state/rate reading is enough for the use, C.27 should be easy not to
use.

Use C.27 because it gives a working reader a useful pause before acting
on speed talk. The intended use is not to formalize every temporal sentence.
The intended use is to stop a small set of expensive mistakes:

- a rate is measured and then treated as if the intervention mechanism is known;
- visible throughput improves while hidden queues, rework, quality loss, or
  burnout worsen;
- a past slope is treated as a future control model;
- a local rate-change is projected across scale without aggregation basis or evidence;
- rhythm or cadence is used as a vibe label with no bearer, anchor, window,
  proxy/evidence, or supported use;
- a planning note becomes a `C.28`-governed causal-use claim, benchmark result, service promise, or
  assurance claim;
- quantum-like modeling is treated as relevant merely because the text contains discreteness,
  types, probes, tokens, or state-space wording.

The positive reader use compact is short:

1. If the statement is only a state reading, use the ordinary state/evidence
   relation.
2. If the statement is only a rate or trajectory reading, use measurement and
   sampling-window discipline.
3. If the statement claims that effort, policy, input, rhythm, constraint, or
   resistance changes the rate, use the least-committing C.27 record that changes admissible use.
4. If the claim crosses the local working boundary into comparison, benchmark,
   publication, gate, assurance, public promise, durable rationale,
   reusable method, formal/control/prediction use, or cross-context transfer,
   strengthen the C.27 record and name the existing patterns that carry the
   specialist claim questions. Local decision-use can often remain a
   `Dyn2TemporalClaimAdequacyCard`.

This is the central anti-bureaucracy invariant: no C.27 record unless the
Dyn0, Dyn1, and Dyn2 distinction changes interpretation, decision-use, evidence posture,
resource allocation, benchmark reading, supported use, or reopen trigger.

Dyn2-Affordability: a correct C.27 use leaves less work behind than the ambiguity
would have caused. If applying C.27 creates more work than the temporal
distinction changes, exit.

At the point of use, the C.27 question is concrete. Before adding a C.27
record, recover:

- what rate, rhythm, trajectory, regime, or stability claim is in play;
- whether the text is reading state, reading rate, or claiming rate-change;
- what effort, input, policy, method, intervention actor/role assignment, or resource envelope is supposed
  to change the temporal behavior;
- what resists, delays, stores momentum, introduces lag, or makes reversal
  costly;
- what evidence, trace, assumption, model, or posture supplies the basis for the reading;
- what use the claim can carry and what downstream claim, effect, or use remains unsupported;
- when the simplified reading should reopen, downgrade, or cite the fuller
  FPF pattern that governs the other question.

The pattern buys practical action, not a vocabulary test. A person can explain
the check as: "A trend is not yet an intervention model; show the effort,
window, resistance, use, and reopen condition, or keep the claim narrower."

Some useful temporal observations arrive before they are claim-ready:


- the team may not only be slow; it may be unable to brake;
- the problem may not be throughput but rhythm mismatch;
- a metric may improve while operational-support load accumulates;
- "the process sped up" may hide orders, invoices, shipments, support tickets,
  PRs, tests, and deployments moving through different paths and interaction
  windows;
- more tool calls may accelerate activity traces without accelerating reasoning
  or repair.

These are temporal-claim adequacy cues, not C.27 records. C.27 should preserve
their cue-only posture. When the reader suspects a hidden Dyn2 claim question but cannot yet
state target, intervention, window, resistance or cost basis, evidence or
assumption, and supported use, the correct output is a partly-said material cue held through A.16, A.16.1, B.4.1, or B.5.2.0, with possible later C.27 record.

The cue may become a `Dyn2TemporalClaimAdequacyCard` only when a rate-change,
rhythm-change, braking, coasting, recovery, stabilization, or intervention
claim becomes explicit enough to name the card minimum. If the live question is
not temporal-claim adequacy, use the pattern that carries that question: C.16
for measurement, C.26 for residual QL cue, E.17.AUD for publication-unit stability, or
viability/assurance patterns when the observation has insufficient evidence, witness,
or currentness support for staying inside a viability or assurance boundary.


### C.27:2 - Problem

C.27 governs the adequacy of intervention-sensitive temporal claims.

C.27 does not govern:

- transition laws or reusable dynamics models, which `A.3.3 U.Dynamics` carries;
- state-space or coordinate construction, which `A.19` and `C.16` carry;
- measurement legality, evidence construction, provenance, assurance posture,
  or evidence decay, which `C.16`, `A.10`, `B.3`, `B.3.4`, and `G.6` carry as
  applicable;
- work actuals and resource burn, which `U.Work` and `Gamma_work` carry;
- planning structures and authorized work, which `U.WorkPlan`,
  `U.MethodDescription`, `C.24`, and relevant planning patterns carry;
- autonomy-budget declarations, guard checks, ledgers, depletion, pause/resume,
  or freedom-of-action governance, which `E.16` carries;
- state-change or evolution loops and language-state movement, which `A.4`, `B.4`,
  `A.16`, and `B.4.1` carry;
- `C.28`-governed causal-use claim, which `C.28` carries, or evaluation/evidence claim, which the relevant evaluation/evidence patterns carry;
- metric proxy/value substitution, which `E.13` carries;
- service promises, agreement text, SLA-like statements, release gates, public
  commitments, and service-acceptance bindings, which `A.2.3`, `A.2.8`,
  `A.2.9`, `A.6.C`, `F.12`, and assurance patterns carry;
- benchmark harnesses, which `G.9` carries;
- dashboard time-series, telemetry pins, path/slice publication, pack shipping,
  discipline-health slots, and refresh orchestration, which `C.21`, `G.12`,
  `G.6`, `G.10`, and `G.11` carry;
- selector publication roles, which `G.5` carries only when a concrete
  selector-publication case consumes a dynamic benchmark result;
- quantum-like probe, frame, export, or coarsening residues, which `C.26` carries;
- publication roles, MVPK faces, governed objects of related FPF patterns, or Kernel `U.*` kinds.

Dynamic-order labels are pattern-local claim classifications, not FPF kinds.
C.27 does not mint `U.Force`, `U.Mass`, `U.Acceleration`,
`U.Rhythm`, `U.Practice`, or `U.SecondOrderProcess`.

FPF gains a compact discipline for claims that otherwise hide behind words such
as speed, agility, throughput, adoption, rhythm, velocity, convergence,
debugging speed, service recovery, faster improvement, acceleration, braking,
redirection, or cadence.

The main failure to prevent is:

> A text measures or names a rate and then behaves as if it knows how to change
> that rate.

C.27 should make three distinctions cheap:

- `Dyn0`: state or snapshot reading;
- `Dyn1`: rate, trend, trajectory, flow, throughput, tempo, or cadence
  reading;
- `Dyn2`: intervention-sensitive temporal reading: rate-change, regime
  transition, braking, redirection, coasting, pause, stabilization, rhythm fit,
  effort profile, resistance, inertia, policy effect, feedback, uncertainty, or
  constraint handling.

C.27 protects against the managerial speed cult. Faster is
not the default value. Braking, pausing, stabilizing, redirecting, coasting,
delaying, widening before narrowing, or slowing rollout can be the correct C.27
outcome.

Local temporal-value boundary:

> C.27 can classify the temporal move. It does not decide that acceleration,
> braking, stabilization, coasting, recovery, convergence, or release speed is
> valuable. The FPF patterns for value alignment, assurance, promise, ethics,
> safety, legal, or proxy/audit concerns carry value, utility, constraint fit,
> harm, promise impact, and proxy distortion.

This boundary applies to claims such as "faster onboarding is better", "more
throughput is better", "faster convergence is better", or "rapid release is our
goal". C.27 may make the temporal claim adequate enough to inspect, but it does
not turn speed into value by default.

These are claim-relation boundary tests, not keyword exclusions. C.27 may still supply a
short temporal-claim note when the state/rate/rate-change/rhythm/regime reading
changes admissible use. The named neighbouring pattern then carries the
non-C.27 question. If the temporal distinction does not change admissible use, exit
C.27 completely.

Do not make C.27 the governing pattern when:

- the text only reports a state or snapshot and no rate/use distinction changes
  interpretation;
- the text only reports a rate, trend, throughput, cadence, or trajectory and no
  intervention-sensitive rate-change claim is made;
- a word such as speed, rhythm, acceleration, agility, or inertia is only a
  teaching metaphor or casual Plain wording;
- the live issue is publication-unit stability: one overloaded local head,
  drifting primary described entity, bounded comparison, explanation faithfulness, or
  approval/action wording should use E.17.AUD, E.17.ID.CR, E.17.EFP, or the
  pattern that governs the downstream claim, effect, or use before C.27;
- the live question is whether a measure is legal, comparable, or interpretable:
  `C.16` carries measurement construction, with C.27 only citing the temporal
  C.27 relation if the measure supplies evidence for an intervention-sensitive claim;
- the live question is a transition law, simulation, prediction, or control model:
  `A.3.3 U.Dynamics` and formal/evidence patterns carry the formal dynamics,
  with C.27 only naming the admissible-use limit of the authored claim;
- the live question is work/resource actuals: `U.Work` and `Gamma_work` carry the
  evidence, with C.27 only using it as effort basis for a Dyn2 claim;
- the live question is scaling-law or elasticity adequacy: C.18.1 carries scale
  variables, scale window, scale probes, and elasticity posture, with C.27
  only naming the temporal-claim adequacy question if scale change is used as the basis for
  rate-change, learning, recovery, throughput, or stabilization;
- the live question is a work plan, call plan, method description, or authorized
  intervention actor/role assignment: the planning pattern carries the plan, with C.27 only active
  when the plan's admissible use depends on rate-change, recovery, stabilization,
  or braking;
- the live question is task-family specialization: C.22.1 carries adaptation
  signature fields, with C.27 only naming the temporal-claim question when
  learning or adaptation speed changes admissible use;
- the live question is preserving a viability envelope under disturbance,
  adaptation cost, latency, operational-support load, or boundary regulation: C.26.3 carries
  the envelope claim, with C.27 only naming the temporal move if
  braking, throttling, cadence change, recovery timing, or stabilization changes
  supported use;
- the live question is causal attribution: `C.28` carries causal-use claim,
  and evaluation/evidence patterns carry non-causal evaluation/evidence claims;
  C.27 may mark the temporal claim's causal use as unsupported until that `C.28`
  relation is satisfied;
- the live question is a benchmark, budget, promise, service boundary, SLA-like
  statement, public commitment, assurance, or release gate: the relevant
  benchmark, boundary, promise, service, assurance, or planning pattern carries
  that claim/use, with C.27 only naming the temporal claim that the other pattern
  inspects;
- the live question is residual quantum-like probe, frame, export, or coarsening cue:
  `C.26` carries it only after ordinary dynamics, work, measurement, benchmark,
  proxy, and assurance patterns have carried their parts.

Overlap example: "Adding review capacity for two sprints will double backlog
reduction rate and justify a budget increase" is not solved by C.27 alone. C.27
types the Dyn2 temporal-claim question; the planning pattern carries planned effort,
`C.16` carries the rate/rate-change measure, the budget/planning pattern carries
approval, and `C.28` carries any causal-use claim. The short
temporal-claim note is a `Dyn2TemporalClaimAdequacyCard`: it prevents those
patterns from missing the hidden rate-change question, but it does not replace
them.

C.27 does not introduce:

- literal Newtonian or physical ontology for organizations, practices, services,
  dances, learning, or work cycles;
- physical quantum ontology or quantum-like superiority;
- mandatory ODE/PDE/calculus formalism for all temporal claims;
- new Kernel types for force, mass, acceleration, rhythm, or practice;
- a new publication role, separate pattern, law sheet, or MVPK face;
- default C.27 profiling for every temporal word;
- thin C.27 echo records when a local C.27 card or profile can cite the FPF
  FPF pattern that governs the other question.


### C.27:3 - Forces


The source article contributes three practical ideas that should survive into
C.27 prose.

First, the useful question is an effort-profile question, not a derivative-word
question. In management, learning, tool-use, incident response, practice
transfer, dance, and service operations, the relevant change is often a profile
of effort over windows: impulse, scheduled push, feedback policy, adaptive
regime, brake, pause, coast, or redirect. C.27 should preserve effort over time,
not just a scalar acceleration label.

Second, rhythm is interval-structured. A rhythm claim needs an anchor, bearer,
window, evidence proxy or observation basis, and admissible use. "Rhythm" as mood
or vibe is not enough; it must be possible to recover whose rhythm, across which
intervals, by which observation or proxy, and for which decision. Coupling,
phase, synchronization, or entrainment-like wording is only needed when the
claim depends on a relation between bearers.

Third, useful formalization improves replicable practice code. C.27 should help
make a practice transferable by recording effort windows, rhythm anchors,
bearer, resistance proxy, evidence basis, and reopen condition. It should not force
equations merely because the source analogy used dynamics language.

Borrowed-frame translation:

| Borrowed idea | C.27 use |
| --- | --- |
| State, rate, and rate-change distinction | Adopted as Dyn0, Dyn1, and Dyn2 claim-reading discipline. |
| Effort windows, acceleration, braking, redirection, coasting, recovery, and stabilization | Adopted as the central temporal-claim adequacy question, with acceleration bias explicitly rejected. |
| Time-scale plurality: spot, episode, sprint, lifecycle, learning-cycle, technoevolution, lifetime, or domain-local time scale | Adapted as optional `temporalScalePosture` for boundary-crossing rhythm use, practice, learning, lifecycle, or evolution claims; not mandatory for ordinary local cards. |
| Speed as result of effort, input, and resistance rather than explanation of its own future change | Adopted as the rate-as-cause-of-rate-change anti-pattern: observed speed does not by itself explain how to change speed. |
| Rhythm as interval-structured effort/rate-change pattern | Adopted with bearer, anchor, window, basis/proxy, admissible use, and cross-bearer coupling only when a named cross-bearer relation is live. |
| Dance/practice style as replicable temporal code | Adapted as replicable practice-description basis: if a training rhythm, review cadence, learning routine, or practice style is meant for boundary-crossing use, name what rhythm/effort pattern is transmitted, which bearer carries it, which anchor/window makes it reproducible, and what error accumulates if only static poses or rate words are transmitted. |
| Typed/discretized compact dynamic representation | A.19, C.16, and C.26 carry it only when the representation, measurement, or residual QL cue is live. |
| Quantum-like or active-inference superiority claim | Not adopted in C.27; C.26 carries the residual probe, frame, order, export, or coarsening claim after ordinary C.27, C.16, work, benchmark, and proxy pattern relations are named. |
| Universal search for force/mass analogues everywhere | Rejected as literal ontology; physical words may remain Plain diagnostic cues, but C.27 mints no `U.Force`, `U.Mass`, `U.Acceleration`, `U.Rhythm`, `U.Practice`, or `U.SecondOrderProcess`. |

| Design alternative | C.27 outcome | Reason |
| --- | --- | --- |
| Do nothing | Insufficient | Leaves FPF vulnerable to speed-only, rate-only, rhythm-as-vibe, and effort-free intervention claims. |
| Add examples only | Insufficient | Examples would not create a reusable adequacy lens or pattern-relation discipline. |
| Put the whole question in `A.3.3 U.Dynamics` | Wrong governed object | `U.Dynamics` governs transition law/model, not the cross-pattern recognition and escalation lens. |
| Put the whole question in `C.16` | Wrong governed object | Measurement construction is necessary but does not govern effort windows, planning, inertia proxies, promises, or intervention adequacy. |
| Put the whole question in `C.24` | Too narrow | Agentic tool-use is one application, not the general pattern for temporal claim adequacy. |
| Put the whole question in `C.26` | Wrong residual QL relation | This would make quantum-like modeling relevant too early; C.26 remains residual for probe, frame, export, or coarsening cues. |
| Add new Kernel types such as `U.Force`, `U.Mass`, `U.Acceleration`, `U.Rhythm`, `U.Practice`, or `U.SecondOrderProcess` | Wrong ontology | The repeated value is a claim-adequacy lens, not a stable Kernel ontology. |
| Create a new publication role or separate pattern for C.27 cards | Wrong object kind | Dyn2 temporal-claim records are pattern-local records, not publication roles or separate patterns. |
| Use C.27 with explicit references to the FPF patterns that govern the other questions | Chosen C.27 shape | One C-pattern can govern the adequacy lens while preserving measurement, dynamics-law, work, benchmark, promise, quality, viability, and QL relations in the patterns that carry them. |
| Duplicate C.27 claim-adequacy content across every related pattern | Too broad | Broad distribution would make ordinary temporal wording expensive. A C.27 card or profile cites the FPF pattern that governs the other question instead of creating a duplicate temporal record. |


### C.27:4 - Solution


Use the least-committing dynamic-order output that changes the admissible use. Dyn0 and Dyn1 are readings in ordinary prose, not C.27 record classes; C.27 records start only when a `Dyn2TemporalClaimAdequacyCard` or `Dyn2TemporalClaimProfile` for boundary-crossing claim use is needed.

| Level | User-visible move | Stop condition |
| --- | --- | --- |
| **Skip** | Leave as ordinary prose | temporal wording does not change claim/use |
| **Dyn0 reading** | state reading or snapshot only | snapshot is enough |
| **Dyn1 reading** | rate, trend, or trajectory only, or C.16-compatible measure when load-bearing | no intervention-sensitive claim |
| **Dyn2TemporalClaimAdequacyCard** | one-screen `Dyn2TemporalClaimAdequacyCard` | local plan, diagnostic, rhythm, effort, or intervention clarity is enough |
| **Dyn2TemporalClaimProfile** | `Dyn2TemporalClaimProfile` with active profile blocks only | the authored temporal claim is used beyond the local working context, is published, benchmarked, promised, assured, made durable rationale, repeated in a reusable method description, used in a gate/public dashboard/Part G pack, or carried across context/scale |
| **Formal-model relation** | C.27 states the temporal-claim question and cites the pattern that carries the formal claim | reusable law, simulation, prediction, control, calibrated model, or assurance-bearing comparison is claimed |

A Dyn2 classification is not evidence that a `U.Dynamics` model exists. It is
only evidence that the authored claim is using temporal change in a way that may
need a dynamics pattern relation if a downstream claim, effect, or use is claimed.

Normativity follows boundary-crossing use:

- normative when the claim carries decision, gate, budget, benchmark,
  publication, assurance, public promise, or reusable method;
- advisory when the claim is exploratory, abductive, or early planning;
- informative when the pattern teaches examples, vocabulary, or anti-patterns.

This is the ordinary first-minute reader-facing form and the main visible C.27 record
for ordinary C.27 use. It remains anchored to an authored claim rather than
becoming a free-standing consulting card.

```text
Dyn2TemporalClaimAdequacyCard

claimText / claimRef:
  What sentence, claim, plan line, benchmark line, or promise-like wording is being read?

target:
  What rate, rhythm, regime, recovery, trajectory, or stability reading is being changed?

move:
  accelerate | decelerate | brake | redirect | coast | pause |
  stabilize | recover | sustain | widen | narrow | domain-local

intervention:
  What effort, input, policy, method, resource, tool-use change, or action is supposed to change it?

window:
  Over what claim, sampling, effort, rhythm, or validity window?

resistanceOrCost:
  What resists, delays, stores momentum, creates residue, or makes the change costly?

basis:
  What evidence, trace, model, assumption, or diagnostic judgement supplies the basis for this reading?

basisPosture?:
  assumption | observedTrace | measured | modelled | diagnostic |
  planning | benchmark-referenced | causal-use-referenced |
  promise/assurance-referenced | unknown

supportedUse:
  What decision, plan, diagnosis, comparison, or pattern relation can this record carry?

unsupportedUse / reopen:
  What downstream claim, effect, or use is unsupported, and what would reopen, downgrade, or add a pattern reference to this claim?
```

Window default: for a local card, one `window` line may stand for claim, sampling,
effort, rhythm, and validity when the distinction does not change admissible use.
Split windows only when evidence is sampled over a different interval than the
claim, effort or intervention occurs over a different interval than the outcome,
benchmark baseline/adaptation/follow-up windows differ, the rhythm anchor/window
differs from the measurement window, or validity/refresh depends on a separate
freshness window.

Optional `basisPosture?` is the card-level bridge to profile posture. It names the
local evidence-support or source-support posture without making the card a full
profile. When the claim later crosses a boundary, `basisPosture?` helps choose
the matching `dynClaimPosture`; it does not strengthen the claim by itself.

`claimText` and `claimRef` keep C.27 tethered to the `PublicationUnit` or claim-bearing `U.EpistemePublication` that carries the temporal claim. `target`
separates the bearer/reading from the intervention, so "we accelerate the team"
gets repaired into a rate/rhythm/trajectory question. `move` protects against
acceleration bias: braking, pausing, stabilization, recovery, coasting,
widening, and narrowing are also Dyn2 moves when they change admissible use.

If the author cannot answer these in short lines, the correct repair is usually
to clarify the claim, not to escalate immediately to a full `Dyn2TemporalClaimProfile`.

Compact C.27 rhythm-claim discipline:

```text
dyn2RhythmClaimBlock? / Dyn2TemporalClaimAdequacyCard fields:
  rhythmBearerRef : whose or what rhythm?
  rhythmAnchor : beat | cadence | cycle | sprint | epoch | release train | attention window | domain-local anchor
  rhythmWindowRef : over what interval?
  instrumentProxyOrEvidenceRef? : trace | proxy | observation | measurement reference
  supportedUse : what decision or reading this record can carry
  couplingMode? : only when cross-bearer synchronization, phase relation, dependency, coordination, or entrainment-like practice relation is claimed
  validityWindowRef? : only when the rhythm reading is used beyond the immediate working window
```

Cadence as observed interval rate may be Dyn1. Rhythm becomes Dyn2 only when
interval structure, effort pattern, coordination, recovery, stabilization, or
intervention-sensitive use changes admissible use.

This discipline keeps rhythm connected to a dynamic claim. A plain "release cadence" or "workshop rhythm" does not need phase or entrainment language unless the admissible use depends on a relation between bearers. If the rhythm wording does not change a rate, intervention, recovery, coordination, or admissible-use reading, it should remain ordinary prose rather than make C.27 relevant.

Compact C.27 coasting-claim discipline:

```text
dyn2CoastingClaimBlock? / Dyn2TemporalClaimAdequacyCard fields:
  coastingClaim : movement, stability, adoption, quality change, queue drain, operational-support load, or practice persistence continues after effort changes or stops
  coastingBasis : habit | automation | stored work | queue pressure | learned capability | commitment momentum | social norm | physical inertia | unknown
  coastingWindowRef : over what interval after effort changes or stops?
  supportedUse : what decision, plan, diagnosis, comparison, or local practice reading this record can carry
  unsupportedUse : what downstream claim, effect, or use this coasting reading does not support
  reopenTrigger : what change, decay, stall, reversal, hidden cost, or new evidence reopens the claim
```

Coasting becomes a full `Dyn2TemporalClaimProfile` block only when a promise,
gate, assurance, benchmark, cross-scale transfer, or public comparison depends
on continued movement or stability after effort changes or stops. Local cases
such as adoption continuing after incentives stop, quality degrading after
acceleration stops, operational-support load continuing after rollout, a trained practice
persisting after training, or a queue draining after intervention ends usually
need only the card fields above.

Coasting/debt fork:

- Use `dyn2CoastingClaimBlock?` when supported use depends on continued
  movement, stability, adoption, queue drain, practice persistence, or
  operational-support load after effort changes or stops.
- Use `dyn2DebtHysteresisBlock?` when supported use depends on residue,
  reversibility, hidden cost, delayed damage, repayment, braking, or recovery
  plan.
- If both are live, coasting describes continued motion or stability; debt and
  hysteresis describe what remains and how costly reversal or recovery is.

**Rare boundary-crossing escalation.** Use the `Dyn2TemporalClaimProfile` only for authored temporal claims used beyond the local working context. It is a pattern-local authored temporal-claim adequacy record, not a model of the dynamic system itself, not a publication role, not a Part G record, not an MVPK face, and not the default C.27 record.

Read the profile-block menu only when boundary-crossing use is already live. The list below is a pattern-relation menu, not a form. The absence of an inactive block is normal; it is not a missing field.

The shape is a header plus present profile blocks. The header carries the minimum boundary-crossing claim-use posture. Each block should be read from its applicability sentence first, and a block appears only when `supportedUse` relies on that claim relation. These blocks are not fields of one universal dynamic object; they are different evidence descriptions and pattern relations made relevant by supported use.

Profile-block closure rule: every present block is either defined by C.27,
a pattern-reference-only block that cites the existing FPF pattern carrying the
other question and adds no new C.27 object, or absent from `activeBlocks`.
A block name is not a new governed object.

Active-block naming rule: read each `activeBlocks` name by one of three statuses.
`localAdequacyBlock` means C.27 states local adequacy fields for an authored
temporal claim. `patternReferenceOnly` means C.27 states only the temporal
move/window/supported-use boundary and cites the FPF pattern that carries the
other question. `relationOnly` means the concern appears in relations or
examples but not as an active block. `dyn2PromiseBoundaryRoute?`,
`dyn2HighStakesTemporalMoveRoute?`, and `dyn2PolicyTransferRoute?` are
pattern-reference-only by default; `dyn2PolicyTransferRoute?` is folded into
`dyn2ControlPolicyRoute?` when behavior-policy/evaluation-policy transfer is
load-bearing.


```text
Dyn2TemporalClaimProfile {
  header:
    claimRef
    describedEntityRef
    temporalBearerRef?
    profileCarrierRef?
    dynClaimPosture
    dynOrder
    baseCharacteristicRef?
    claimWindowRef
    supportedUse
    unsupportedUse
    reopenTrigger

  activeBlocks:
    c16RateMeasurementRouteRef? // if rate/rate-change measurement evidence is load-bearing
    dyn2EffortWorkBlock? // if effort, resource, work, intervention actor, or authority basis is load-bearing
    dyn2ResistanceInertiaBlock? // if resistance, delay, residue, reversibility, or cost is load-bearing
    dyn2RhythmClaimBlock? // if rhythm or cadence changes admissible use
    dyn2CoastingClaimBlock? // if boundary-crossing use depends on continued movement or stability after effort changes or stops
    dyn2CausalUseRoute? // if rate-change or intervention is used as a causal-use basis
    dyn2BenchmarkParityBlock? // if comparison/benchmark depends on rate, rate-change, rhythm, recovery, or intervention effect
    dyn2MetricTargetEffectBlock? // if metric publication or target use changes temporal behavior or admissible use
    dyn2ObjectCentricTraceBlock? // if work-cycle or service-process evidence depends on object-centric or multi-bearer traces
    dyn2ScaleVariableClaimBlock? // if changing a resource or scale variable is claimed to change rate, learning, recovery, or throughput
    dyn2TaskFamilyAdaptationRoute? // if learning/adaptation-rate claim depends on a declared task-family specialization signature
    dyn2ControlPolicyRoute? // if control, feedback, policy update, adaptive regime, or MPC/RL-style evaluation basis is load-bearing
    dyn2PolicyTransferRoute? // pattern-reference-only alias inside dyn2ControlPolicyRoute? when behavior-policy/evaluation-policy transfer is load-bearing
    dyn2CrossScaleTransferBlock? // if dynamic claim transfers across bearer, level, scale, or aggregate
    dyn2ViabilityEnvelopeRoute? // if rate-change, braking, rhythm, or stabilization is used to keep a viability envelope inside usable bounds
    dyn2DebtHysteresisBlock? // if admissible use relies on sustained acceleration, braking, recovery, stabilization, or residue after effort changes
    dyn2PromiseBoundaryRoute? // pattern-reference-only when promise, SLA/SLO, gate, assurance, or public commitment is live
    dyn2HighStakesTemporalMoveRoute? // pattern-reference-only when high-stakes acceleration, braking, redirection, or rollout is live
    dyn2QLResidualRoute? // if residual probe, frame, order, export, or coarsening cue remains after ordinary FPF pattern relations
}
```

Absence of an inactive block is normal. It is not a missing field. A block
becomes active only when the admissible use relies on it; otherwise the `Dyn2TemporalClaimProfile`
should stay smaller or downgrade to a `Dyn2TemporalClaimAdequacyCard`, Dyn1 reading, or ordinary prose.

Pattern-reference-only blocks:

- `dyn2PolicyTransferRoute?` is handled inside `dyn2ControlPolicyRoute?` when
  behavior-policy/evaluation-policy or off-policy transfer is load-bearing. C.27
  names `behaviorPolicyRef`, `proposedPolicyRef`, `offPolicyRisk`, and the
  evaluation/control pattern relation; it does not create a separate policy-transfer
  pattern.
- `dyn2PromiseBoundaryRoute?` states only the temporal move, window,
  supported use, unsupported downstream claim, effect, or use, and references to the patterns that
  carry promise, commitment, instituting speech act, service acceptance,
  contract unpacking, and assurance: `A.2.3`, `A.2.8`, `A.2.9`, `A.6.C`,
  `F.12`, and assurance patterns.
- `dyn2HighStakesTemporalMoveRoute?` states only the high-stakes temporal move, window,
  unsupported downstream claim, effect, or use, and reference to the pattern that carries the harm,
  quality, safety, ethics, legal, financial, operational-support, or
  human-wellbeing question.

Header discipline: for a `Dyn2TemporalClaimProfile` for boundary-crossing claim use, `claimRef`,
`describedEntityRef`, `dynClaimPosture`, `dynOrder`, `claimWindowRef`,
`supportedUse`, `unsupportedUse`, and `reopenTrigger` are mandatory.
`temporalBearerRef` is present when the temporal bearer differs from the
described entity or is otherwise load-bearing. `profileCarrierRef` is present
when publication or evidence needs the authored carrier named. `baseCharacteristicRef`
is mandatory only when measurement, comparison, or C.16 relation is load-bearing; for a Plain diagnostic claim it may remain a local phrase in the `target` line.

Window split rule: one local window is enough only when the claim window,
sampling window, effort/intervention window, validity window, baseline window,
and follow-up window are the same for the admissible use. Split them when the
evidence is sampled over a different interval than the claim, effort is applied
before or after the measured change, a comparison needs a baseline, an outcome is
observed after exposure, or the claim remains valid only for a shorter period
than the historical trace. If the split is unknown and the admissible use depends
on it, downgrade the use or add the relevant window reference before relying on
the temporal claim.

C.16 rate-measurement relation: when rate or rate-change is load-bearing, C.27
cites the C.16 measurement relation. C.27 does not define measurement
legality.

```text
c16RateMeasurementRouteRef? {
  baseCharacteristicRef
  stateMeasureRef?
  rateMeasureRef?
  rateChangeReadingMeasureRef?
  DHCMethodRef?
  samplingWindowRef
  scaleUnitPolarityRef?
  evidenceStubRefs?
  stabilityOrNoisePosture?
  C16RouteRef
}
```

C.27 effort/work block: when a rate-change claim depends on effort, resource,
method, intervention actor, or role-assignment capacity, C.27 separates planned
effort, method description, resource envelope, actual work trace, and
authority/capability posture. It does not turn work evidence into a dynamics law.

```text
dyn2EffortWorkBlock? {
  causalInterventionSpecRef?
  plannedEffortRef?        // WorkPlan / MethodDescription / resource envelope
  actualEffortTraceRef?    // U.Work / Gamma_work evidence
  effortWindowRef?
  interventionActorRef? {
    actorOrRoleAssignmentRef
    authorityPosture: authorized | proposed | hypothetical | unknown
    capabilityOrScopeRef?
  }
  resourceEnvelopeRef?
  A15RouteRef?
}
```

`interventionActorRef` means the actor, role assignment, tool, system, policy
rule, or human/work arrangement claimed to apply the intervention, plus an
authority/capability posture. If a planning claim says "add review capacity", C.27
should make it visible whether that capacity is assigned, capable, available,
authorized, proposed, hypothetical, or unknown, while leaving role, method, work-plan, and work-occurrence
alignment to A.15 and work patterns.

C.27 resistance/inertia block: `dyn2ResistanceInertiaBlock?` is present when admissible use depends on what resists, delays, stores momentum, creates residue, or makes the change costly. This is core C.27 content because it prevents effort-free acceleration claims. The `Dyn2TemporalClaimAdequacyCard` asks the question locally; the `Dyn2TemporalClaimProfile` uses a separate active profile block only when that answer matters beyond the local working context.

```text
dyn2ResistanceInertiaBlock? {
  resistanceOrInertiaProxy
  resistanceProxyFamily
  resistanceProxyBasisPosture: qualitative | measured | modelled | assumed | unknown
  evidenceRef?
  unsupportedUse?
}
```

`resistanceProxyBasisPosture = unknown` is an acceptable C.27 result. Unknown resistance need not
block a local diagnostic `Dyn2TemporalClaimAdequacyCard`, but it should block durable
acceleration, causal, benchmark, promise-like, or assurance use until a higher evidence-support class
or carrying pattern reference is supplied.

C.27 control/policy relation: `dyn2ControlPolicyRoute?` is present only when `dynClaimPosture` is `controlModel`, `policyRule`, `adaptive`, a feedback-bearing `planningModel`, or an explicit C.24/C.19/evaluation relation. This relation says that the authored temporal claim has crossed into control/policy model or policy-evaluation use. It does not make C.27 an MPC, reinforcement-learning, or policy-evaluation pattern.

```text
dyn2ControlPolicyRoute? {
  interventionRegime
  controlHorizon?
  closedLoopUpdate?
  behaviorPolicyRef?
  proposedPolicyRef?
  offPolicyRisk?
  stopRule?
  controlPolicyRouteRef -> U.Dynamics / C.19 / C.24 / evaluation pattern
}
```

C.27 causal-use relation: `dyn2CausalUseRoute?` is present only when the authored temporal claim uses a rate-change, intervention, effort, workshop, policy, or practice change as a causal-use basis. Core rule: C.27 can say a claim is Dyn2 and intervention-sensitive; C.27 cannot turn that basis into a `C.28`-governed causal-use claim. The fields below are `C.28` refs consumed by C.27, not `C.27`-defined causal aliases.

```text
dyn2CausalUseRoute? {
  causalInterventionSpecRef
  comparatorOrCounterfactualRef
  timeZeroOrAssignmentWindow
  followUpWindowRef
  outcomeMeasureRef
  estimandRef?
  causalAssumptionSetRef?
  rivalCauseSetRef?
  causalIdentificationProfileRef?
  causalUseEvidenceDesignRef?
  offPolicyCausalEvaluationProfileRef?
  supportedCausalUse
  unsupportedCausalUse
}
```

C.27 dynamic benchmark requirement: `dyn2BenchmarkParityBlock?` is present only when a comparison or benchmark depends on rate, rate-change, recovery speed, rhythm improvement, intervention effect, effort budget, or dynamic outcome. Content rule: C.27 declares the dynamic claim question of the benchmark; `G.9` carries parity.

```text
dyn2BenchmarkParityBlock? {
  comparedClaimRefs
  dynOrderCompared: Dyn1 | Dyn2
  baselineWindowRef
  adaptationOrInterventionWindowRef?
  budgetOrEffortParityRef?
  rateOrRateChangeReadingMeasureRef?
  G9ParityPlanRef
  G9ParityReportRef?
}
```

C.27 metric-target effect block: `dyn2MetricTargetEffectBlock?` is present only
when metric publication, target use, incentive use, dashboard use, gate use, or
public comparison changes temporal behavior or admissible use. C.16 carries the
measure; E.13, assurance, or governance patterns carry proxy/utility distortion;
C.26 is relevant only if residual probe, frame, order, or export cue remains.

```text
dyn2MetricTargetEffectBlock? {
  publishedOrTargetedMeasureRef
  targetOrIncentiveUse
  dashboardGatePromiseOrBudgetUse?
  behaviorChangeRisk
  temporalWorkChangeVsMeasurementChangeNote
  C16RouteRef?
  E13ProxyAuditRef?
  C26RouteRef? // only if residual probe, frame, order, or export cue remains
}
```

C.27 object-centric trace block: `dyn2ObjectCentricTraceBlock?` is present only
when a work-cycle/process rate claim depends on several object bearers, event
traces, interactions, or aggregation basis rather than one scalar speed label.
C.27 records why scalar throughput is insufficient; object-centric process
mining or local process evidence carries the detailed log discipline.

```text
dyn2ObjectCentricTraceBlock? {
  bearerKind: single-object | multi-object | aggregate | proxy
  objectTypeRefs
  eventTraceRef
  interactionOrCouplingNote?
  convergenceDivergenceRisk?
  aggregationRoute?
  supportedUse
  unsupportedUse
}
```

C.27 cross-scale transfer field: `dyn2CrossScaleTransferBlock?` is present only when a dynamic claim transfers rate, rate-change, rhythm, recovery, acceleration, braking, or agility from one bearer/level/aggregate to another. Aggregate rate-change and local rate-change are different readings unless aggregation basis and bearer continuity are declared.

```text
dyn2CrossScaleTransferBlock? {
  sourceBearerRef
  targetBearerRef
  aggregationRoute?
  mixShiftRisk?
  dynamicTransferPosture
}
```

C.27 scale-variable claim block: `dyn2ScaleVariableClaimBlock?` is present only when the
authored temporal claim says that changing a resource or scale variable changes
rate, improvement, learning, recovery, throughput, or stabilization. This is
not the same as cross-scale transfer: scale-variable claim asks which variable is
changed and over what scale window; cross-scale transfer asks whether a dynamic
reading is carried across bearer, level, or aggregate. C.18.1 carries scale
variables, scale windows, scale probes, and elasticity posture; C.27 records
only that the scale change is being used as the basis for a temporal-claim reading.

```text
dyn2ScaleVariableClaimBlock? {
  scaleVariableRef
  scaleWindowRef?
  scaleElasticityPosture: rising | knee | flat | declining | unknown
  C18_1RouteRef?
  G9ParityPlanRef?
}
```

C.27 task-family adaptation relation: `dyn2TaskFamilyAdaptationRoute?` is present
only when the temporal claim says that a holder, dyad, team, specialist
portfolio, method, or agent reaches usable specialization faster on one declared
`TaskFamilyRef` or `TaskSignature`. C.22.1 carries the task-family adaptation
signature. C.27 records only the learning/adaptation-rate question and the
admissible use that made it relevant.

```text
dyn2TaskFamilyAdaptationRoute? {
  TaskFamilyRef?
  TaskSignature?
  thresholdOrUsableSpecializationRef?
  timeToThresholdRef?
  budgetToThresholdRef?
  C22_1RouteRef
}
```

C.27 viability-envelope relation: `dyn2ViabilityEnvelopeRoute?` is present only when
a temporal claim says braking, slowing rollout, throttling, cadence change,
recovery timing, adaptation cost, operational-support load, or stabilization keeps a
viability bearer inside usable bounds. C.27 may type the temporal move and its
window. C.26.3 carries the viability-envelope claim: protected promise or
function, viable bounds, disturbance, sensor/probe/action split, adaptation
cost, and failure mode. Do not make C.27 the pattern for all "stability through
change" claims.

```text
dyn2ViabilityEnvelopeRoute? {
  viabilityBearerRef?
  protectedPromiseOrFunctionRef?
  temporalMoveRef?
  C26_3RouteRef
}
```

C.27 residual QL relation: `dyn2QLResidualRoute?` is present only when ordinary FPF
patterns have already carried the temporal-claim, measurement, work, benchmark,
value/proxy, scale, adaptation, viability, promise, or evidence basis and a
residual probe, frame, order, export, or coarsening cue still changes the admissible
reading. C.26 carries the residual QL reading. C.27 only records that the authored
temporal claim has a residual QL relation; this block stays hidden by default when
no such residue exists.

```text
dyn2QLResidualRoute? {
  residualQLCue?
  residualQLRouteRef?
  ordinaryRouteBasisRef?
  C26RouteRef
}
```

C.27 debt/hysteresis block: `dyn2DebtHysteresisBlock?` is present only when admissible use depends on sustained acceleration, braking, recovery, stabilization, domain residue after effort changes, or a public promise/gate/assurance/high-stakes decision about rate-change. Unknown reversibility is allowed, but it bounds supported use.

```text
dyn2DebtHysteresisBlock? {
  debtKind?
  debtWindowRef?
  evidenceRef?
  reversibilityPosture: reversible | costlyToReverse | irreversibleWithinWindow | unknown
  hysteresisOrResidue?
  repaymentOrBrakePlan?
  debtHysteresisRouteRef -> planning / assurance / quality / wellbeing / safety pattern
}
```

These C.27 dynamic-claim profile-block field definitions are boundary-crossing
material for `Dyn2TemporalClaimProfile` and for higher-stakes authored temporal
claims used beyond the local working context. They are not the default C.27 user
interface, not a data model, and not a universal C.27 dynamic-claim field list
that every user must fill.


C.27 uses physical words only as Plain analogies. Tech prose uses effort,
input, and work references rather than force; resistance/inertia proxies rather
than mass; rate-change readings rather than acceleration as a new kind; and
rhythm bearer/anchor/window rather than `U.Rhythm`.

Each field-definition item either carries a small local C.27 temporal-claim adequacy value or points
back to the existing FPF pattern that governs the referenced object. A field name
is not a pattern.
Metric, process, service, practice, policy, harm, operational-support, and envelope wording
does not create a free C.27 slot. It must resolve to a local C.27 value, an
existing FPF kind and reference, or a governing-pattern relation; otherwise it remains
Plain example language.

| Field/question | Definition | Kind discipline |
| --- | --- | --- |
| claimText / claimRef | The sentence, claim, plan line, benchmark line, or promise-like wording being read. | Anchors C.27 to an authored claim/source; not a free-standing consulting card. |
| target | The temporal reading whose adequacy is in question: rate, cadence, flow, convergence, recovery, narrowing, widening, stabilization, regime, or trajectory. | Local description plus `baseCharacteristicRef` or measurement relation when load-bearing. |
| move | The temporal move: accelerate, decelerate, brake, redirect, coast, pause, stabilize, recover, sustain, widen, narrow, or domain-local. | Prevents acceleration-only bias; braking, pausing, recovery, and coasting can be positive Dyn2 moves. |
| effort, input, policy, method, or intervention | The planned or claimed source of rate-change. It may be work, method change, policy rule, resource input, tool-use change, or control action. | References planning, work, method, policy, or control patterns; it is not stored as a new force object. |
| window | The time interval over which the claim is made, effort is applied, rate is sampled, rhythm is observed, or validity is asserted. | Use a time/window reference appropriate to the pattern; do not collapse all windows into `U.Dynamics.timeBase`. |
| resistance, delay, momentum, or cost | The reason rate-change is not free or immediate: constraint, lag, habit, queue pressure, coordination cost, technical debt, operational-support load, friction, or domain-local resistance proxy. | Domain-local proxy, not literal mass; evidence or assumption should be named when the authored temporal claim is used beyond the local working context. |
| evidence or assumption | The basis that makes the `Dyn2TemporalClaimAdequacyCard` more than a slogan: observed trace, measurement, work evidence, model assumption, planning assumption, or diagnostic judgement. | Cites C.16, work/evidence, causal, benchmark, or assurance patterns when a downstream claim, effect, or use is claimed. |
| basisPosture? | Optional compact basis kind: assumption, observed trace, measured, modelled, diagnostic, planning, benchmark-referenced, causal-use-referenced, promise/assurance-referenced, or unknown. | Bridges a local card to `dynClaimPosture` if the claim later becomes boundary-crossing; it does not strengthen the claim by itself. |
| supported decision or use | The practical use that this `Dyn2TemporalClaimAdequacyCard` can carry: orientation, plan choice, budget, benchmark, gate, replan, publication, or local diagnosis. | Must stay within the evidence basis and `dynClaimPosture`. |
| unsupported downstream claim, effect, or use | A nearby use that this `Dyn2TemporalClaimAdequacyCard` cannot carry, such as `C.28`-governed causal-use claim, release approval, public promise, cross-context transfer, benchmark superiority, or service guarantee. | Prevents laundering a light `Dyn2TemporalClaimAdequacyCard` into a heavier temporal-claim record. |
| reopen, downgrade, or pattern-reference condition | A condition that requires revisiting the `Dyn2TemporalClaimAdequacyCard`, downgrading to Dyn0 or Dyn1, escalating to a profile or formal pattern, or citing another pattern. | This is an evolvability trigger, not a status note. |
| rhythmBearerRef | The entity, practice, work cycle, service, learner, body part, system component, or other named bearer whose rhythm is described. | Must resolve to a named FPF kind and reference or explicitly remain Plain example language; C.27 does not mint a new rhythm kind. |
| rhythmAnchor | The temporal reference for a rhythm claim: beat, cadence, cycle, sprint, epoch, release train, attention window, or domain-local anchor. | It is an anchor for interpretation, not `U.Rhythm`. |
| rhythmWindowRef | The time window across which rhythm is asserted or measured. | Separate from claim, sampling, effort, and validity windows when they differ. |
| instrumentProxyOrEvidenceRef | The measurement or observation proxy used for rhythm, such as tapping task, cadence log, work trace, event sequence, survey, sensor, or domain evidence reference. | Uses C.16 and evidence discipline when load-bearing. |
| couplingMode | How rhythm in one bearer or signal is related to another: synchronization, phase relation, dependency, coordination, entrainment-like practice relation, or domain-local coupling. | Active only when cross-bearer relation is claimed; otherwise ordinary cadence does not need coupling language. |
| validityWindowRef | The period or condition under which the rhythm reading is valid. | Prevents stale rhythm claims from boundary-crossing indefinitely. |

Claim posture discipline: in `Dyn2TemporalClaimProfile`, `dynClaimPosture` is a
pattern-relation declaration, not a maturity scale. A `diagnosticReading` does not mature
into a `causalClaim` by adding fields; `C.28` carries causal-use
claim posture. A `planningModel` does not become `promiseBoundaryUse` by
publication; promise, boundary, commitment, service, or assurance patterns carry
promise-like posture. Changing posture may change the governing relation, pattern,
evidence basis, or assurance-facing relation.
No C.27 field completion upgrades the posture; a higher-stakes posture is a
relation change.


| Field | Definition | Kind discipline |
| --- | --- | --- |
| claimRef | The authored claim, sentence, plan line, benchmark line, or promise-like wording that the profile for boundary-crossing claim use describes. | Mandatory; anchors the profile to authored temporal-claim content. |
| describedEntityRef | The entity, work object, system, practice, service, method, or other governed described entity whose temporal claim is being described. | Reference to the described entity through its named FPF kind and reference; not the `Dyn2TemporalClaimProfile` itself. |
| temporalBearerRef | The object that bears the rate, rhythm, regime, trajectory, or rate-change. It may differ from the described entity in aggregate or proxy cases. | Use only when bearer distinction matters; avoid loose `carrierOrSubject`. |
| profileCarrierRef | The document, card, profile, report, benchmark record, or other authored carrier that contains the Dyn2 claim record. | Carrier of the description, not the dynamic system. |
| dynClaimPosture | The kind and support posture of the dynamic temporal claim: assumption, conjecture, observed trace, diagnostic reading, planning model, control model, calibrated model, causal claim, benchmark claim, assurance claim, or promise-like claim. This is not a maturity sequence: a causal claim is differently governed from a diagnostic reading, and a promise-like claim is differently governed from a benchmark. Changing posture may change the governing relation, pattern, evidence basis, or assurance pattern. | Reading a dynamic temporal claim as carrying a different claim posture is a relation change; use the FPF pattern that governs the target claim, effect, or use. |
| dynOrder | Pattern-local classification: `Dyn0`, `Dyn1`, or `Dyn2`. | Classification of a claim, not a Kernel kind. |
| baseCharacteristicRef | The characteristic whose state/rate/rate-change is being discussed. | Mandatory only when measurement, comparison, or C.16 relation is load-bearing; otherwise the `target` line may carry a local Plain phrase. |
| stateMeasureRef | Measurement reference for a state reading or snapshot. | C.16-compatible when used as evidence or comparison. |
| rateMeasureRef | Measurement reference for rate, tempo, throughput, cadence, flow, trend, or trajectory. | C.16-compatible and separate from state measure when load-bearing. |
| rateChangeReadingMeasureRef | Measurement reference used as evidence for an acceleration, deceleration, braking, redirection, stabilization, hazard-change, queue-pressure-change, or other rate-change reading. | C.16-compatible; this is evidence for a reading, not a new primitive acceleration measure. |
| publishedOrTargetedMeasureRef | The measure being used as reading, dashboard signal, target, gate, incentive, budget input, or public comparison. | C.16 carries measurement legality and comparability; target/proxy use belongs outside C.27 when load-bearing. |
| targetOrIncentiveUse | How the metric is used as a target, incentive, optimization proxy, management signal, or behavior-shaping prompt. | E.13, assurance, or governance patterns carry proxy/utility distortion. |
| dashboardGatePromiseOrBudgetUse | Whether the metric appears in a dashboard, gate, promise, budget, review, or public comparison. | Names boundary/assurance pattern relations when those uses are live. |
| behaviorChangeRisk | How publication, target pressure, incentive, or gate use may change behavior. | C.27 records temporal intervention risk; causal-use claim still needs `C.28` causal-use relation. |
| temporalWorkChangeVsMeasurementChangeNote | Split between real work/process rate change, measurement/probe effect, gaming/selection effect, and causal effect if claimed. | Prevents metric improvement from being read as system improvement. |
| C16RouteRef | Route/reference for admissible measurement construction, comparability, and evidence. | C.27 cites it; C.27 does not define metric legality. |
| E13ProxyAuditRef | Route/reference for proxy-metric distortion, pragmatic utility, or value/proxy divergence. | Keeps metric-as-target work out of C.27 when the dynamic temporal claim is not live. |
| C26RouteRef | Reference for residual probe, frame, order, export, or coarsening cue. | Only present after ordinary C.27, C.16, and E.13 pattern relations leave a residual quantum-like cue. |
| residualQLCue | The cue that a remaining probe, frame, order, export, coarsening, or similar representational condition may change the admissible reading after ordinary FPF patterns have carried their parts. | Plain cue; vocabulary alone does not make QL relevant. |
| residualQLRouteRef | The specific residual QL cue, if any, that still matters to supported use after ordinary temporal, measurement, work, benchmark, value/proxy, scale, adaptation, viability, promise, or evidence pattern relations are named. | C.26 carries the QL discipline; C.27 only records the pattern-reference need. |
| ordinaryRouteBasisRef | Reference or short basis showing which ordinary FPF pattern relation already carries the non-QL relation. | Prevents QL from stealing measurement, work, value, benchmark, scale, adaptation, viability, or promise work. |
| DHCMethodRef | Reference to the declared method for constructing or interpreting the characteristic/measure. | Existing C.16 relation; not a new measurement primitive. |
| scaleVariableRef | The resource or scale variable whose change is claimed to change rate, improvement, learning, recovery, throughput, or stabilization: review capacity, tool-call budget, token budget, sprint count, data volume, model capacity, parallelism, freedom of action, or domain-local scale variable. | Resolves through `C.18.1` or through the named FPF kind and reference that carries the resource or scale variable; not a new force or effort kind. |
| scaleWindowRef | The scale range or window over which the scale-variable claim is asserted. | C.18.1 carries scale-window discipline; G.9 carries parity when compared. |
| scaleElasticityPosture | Qualitative C.18.1 posture for the scale claim: rising, knee, flat, declining, or unknown. | Not a numeric scaling law and not proof that more scale is better. |
| C18_1RouteRef | Route/reference for C.18.1 scaling-law lens adequacy when a scale-variable or elasticity claim is live. | C.27 cites it; C.27 does not define scaling-law discipline. |
| TaskFamilyRef | The declared task family whose time-to-usable-specialization or adaptation speed is being discussed. | C.22.1 carries the task-family adaptation signature; C.27 only states the temporal-claim question. |
| TaskSignature | The declared task signature or specialization signature used by C.22.1. | Not a C.27 kind; used only to prevent generic learning-speed talk. |
| thresholdOrUsableSpecializationRef | The threshold, criterion, or usable-specialization target that makes "adapted faster" inspectable. | Keeps adaptation-speed claims from becoming vague improvement claims. |
| timeToThresholdRef | The time window or time-to-threshold reference for reaching the declared adaptation target. | C.27 may type the temporal-claim question; C.22.1 carries adaptation-signature meaning. |
| budgetToThresholdRef | The effort, resource, exposure, or budget reference needed to reach the declared adaptation target. | Routes budget/exposure detail through C.22.1 and work/resource patterns when load-bearing. |
| C22_1RouteRef | Route/reference for C.22.1 task-family adaptation signature reference. | Mandatory when `dyn2TaskFamilyAdaptationRoute?` is active. |
| viabilityBearerRef | The system, collective system, delivery system, role configuration, organism-as-system, service situation, or declared bearer whose viability is being discussed. | C.26.3 carries viability-envelope discipline; C.27 only names the temporal move when live. |
| protectedPromiseOrFunctionRef | The promise, function, or operating regime that the viability envelope is meant to preserve. | Uses C.26.3 and promise, boundary, or service patterns when load-bearing. |
| C26_3RouteRef | Route/reference for C.26.3 viability-envelope boundary regulation when temporal change is used to preserve viable bounds. | Mandatory when `dyn2ViabilityEnvelopeRoute?` is active; C.27 does not define viability envelopes. |
| timeBase | Time basis of an underlying dynamics model, if a model is live. | Do not use it as a catch-all for every claim/sampling/effort/rhythm window. |
| claimWindowRef | The time window over which the Dyn2 claim is asserted. | Separate from evidence and effort windows when needed. |
| samplingWindowRef | The time window over which state/rate/rate-change evidence is sampled. | Required for noisy derivative-like readings used in claims requiring additional evidence. |
| effortWindowRef | The time window over which planned or actual effort or input is applied. | Applies planning and work patterns. |
| rhythmWindowRef | The window over which rhythm/cadence/phase relation is asserted. | Uses rhythm-bearing note discipline; not `U.Rhythm`. |
| temporalScalePosture | Optional declaration of the time scale that carries the authored temporal claim used beyond the local working context: spot, episode, sprint, lifecycle, learning-cycle, technoevolution, lifetime, or domain-local. | Use only when scale changes the claim's admissible use, bearer, evidence, or reopen condition; it is not a new temporal kind. |
| validityWindowRef | The period or condition over which the `Dyn2TemporalClaimProfile` remains valid. | Carries the refresh/reopen basis. |
| rateChangeIntent | The intended temporal move: accelerate, decelerate, brake, redirect, coast, pause, stabilize, widen, narrow, recover, sustain, or domain-local move. | Avoids acceleration-only bias. |
| interventionRegime | The intervention pattern: impulse, scheduled, feedback, adaptive, exploratory, or policy rule. | Uses planning, control, or policy patterns when formal. |
| controlHorizon | The horizon over which a control-style intervention is evaluated or adjusted. | Only live for `dyn2ControlPolicyRoute?` claims. |
| closedLoopUpdate | The feedback/update rule by which later observations change the intervention. | Uses control or model patterns when reusable or formal. |
| behaviorPolicyRef | The source policy, regime, or practice that produced the evidence being reused. | Only live when policy/regime evidence is used as the basis for another policy or adaptive claim. |
| proposedPolicyRef | The proposed or evaluation policy, regime, rollout, or intervention rule being argued for. | Separate from `behaviorPolicyRef`; otherwise off-policy transfer is hidden. |
| offPolicyRisk | Risk that evidence from one policy/regime does not carry another policy/regime use. | Uses sequential decision or evaluation discipline. |
| stopRule | Condition for stopping, braking, pausing, replanning, or exiting the intervention. | Carries affordability and harm-control basis. |
| controlPolicyRouteRef | The FPF pattern relation used when the claim needs formal dynamics, search/policy health, agentic action, or evaluation basis: `U.Dynamics`, C.19, C.24, or an evaluation pattern. | C.27 records the crossing; the referenced pattern carries the required control or policy discipline. |
| plannedEffortRef | Reference to planned effort in WorkPlan, MethodDescription, resource envelope, or planning pattern. | Ex ante plan, not actual burn. |
| actualEffortTraceRef | Reference to observed work/resource/time burn or trace. | Cites `U.Work` / `Gamma_work`, not `U.Dynamics`. |
| inputCharacteristicRefs | Characteristics treated as inputs to a dynamics or intervention claim. | Existing characteristic/model discipline. |
| effortProfile | Mapping from time window to effort or input posture. | Pattern-local description of effort timing; not a new law. |
| interventionActorRef | The actor, role assignment, tool, system, policy rule, or work arrangement claimed to apply the intervention. | Resolves through A.15, planning, role, method, work, or agentic-action patterns; not a new physical-mechanism kind. |
| interventionAuthorityPosture | Whether the intervention actor/role is authorized, proposed, hypothetical, unknown, assigned, available, or otherwise scoped. | Missing authority or capability bounds admissible use rather than creating proof of executable work. |
| capabilityOrScopeRef | Reference to the scope, capability, assignment, or availability basis for the intervention actor/role. | Requires A.15 or a work pattern for role, method, work-plan, or work-occurrence alignment; C.27 only makes the supported-use limit visible. |
| resistanceOrInertiaProxy | Domain-local reason that changing the rate is hard, delayed, sticky, or costly. | Proxy with `resistanceProxyBasisPosture` and evidence; not literal mass. |
| resistanceProxyFamily | Pattern-local grouping of resistance/inertia proxy: lag, queue, habit, constraint, coordination cost, technical debt, operational-support load, physical inertia, or domain-local family. | Not a `U.Kind`; Plain/Tech mapping must stay explicit. |
| resistanceProxyBasisPosture | Whether a resistance/inertia proxy is qualitative, measured, modelled, assumed, unknown, or otherwise declared. | Prevents unsupported assumptions from being treated as evidence support. |
| evidenceRef | Evidence reference that supplies the basis for a field. | Uses evidence patterns. |
| interventionConstraintRefs | Resource, safety, service, legal, ethical, quality, or domain constraints that bound the intervention. | These constraints are not governed by C.27; C.27 records that they are active. |
| resourceEnvelopeRef | Resource boundary for the intervention. | Planning/resource pattern. |
| safetyEnvelopeRef | Safety boundary for the intervention. | Assurance/safety pattern. |
| serviceEnvelopeRef | Service boundary or operational envelope. | Service/promise/boundary pattern. |
| legalOrEthicalEnvelopeRef | Legal, ethical, or compliance boundary. | Legal/ethics/assurance pattern. |
| qualityEnvelopeRef | Quality boundary affected by acceleration, braking, or rate-change. | Quality pattern such as C.25 where applicable. |
| uncertaintyPosture | Declared uncertainty around model, measurement, evidence basis, stability, or transfer. | May force downgrade or a higher evidence-support relation. |
| dyn2CausalUsePosture | Declared causal-use posture and its details for a Dyn2 temporal claim. | C.27 does not supply a `C.28`-governed causal-use claim by itself; use `dyn2CausalUseRoute?` only when causal use is live. |
| causalInterventionSpecRef | The intervention, effort, workshop, policy, regime, practice change, or other action being treated as causal. | C.27 may name it; `C.28` carries the causal intervention spec, estimand, assumptions, identification, realizability, and evidence design, and supported causal-use judgement. |
| comparatorOrCounterfactualRef | Comparator, contrast case, counterfactual, control group, prior regime, or declared absence of one. | Required when causal reading is live; otherwise the claim remains planning/diagnostic. |
| timeZeroOrAssignmentWindow | The start, assignment, exposure, or intervention window for the causal reading. | Keeps before/after slope claims from hiding timing ambiguity. |
| followUpWindowRef | The outcome observation window after intervention/exposure. | Separate from claim, sampling, effort, rhythm, and validity windows when they differ. |
| outcomeMeasureRef | The measured outcome whose change is being causally read. | Uses C.16 and evidence discipline when load-bearing. |
| estimandRef | The `U.CausalEstimand` being estimated when causal-use basis is claimed. | Defined by `C.28`; C.27 only cites it when a temporal claim is used causally. |
| causalAssumptionSetRef | Assumptions under which the causal/model/evaluation claim holds. | Uses `C.28`; not hidden inside C.27 shorthand. |
| rivalCauseSetRef | Alternative causes that could explain observed rate-change. | Uses `C.28`; required when causal reading is live. |
| causalIdentificationProfileRef | Identification strategy, graph proof, calculus proof, data-regime basis, or bound used for the causal claim. | Delegates to `C.28`; absent identification limits supported causal use. |
| causalUseEvidenceDesignRef | Experiment, quasi-experiment, target-trial emulation, counterfactual sampling, simulation validation, or other causal evidence-design reference. | Uses `C.28`; absent design limits supported causal use. |
| offPolicyCausalEvaluationProfileRef | Off-policy/sequential/adaptive policy evaluation route when rate-change or policy-improvement wording depends on logged behavior or replay. | Uses `C.28`; C.27 does not own off-policy causal evaluation. |
| supportedCausalUse | The causal conclusion or decision use carried by the `C.28` causal-use relation. | Must stay within the declared design, assumptions, outcome evidence, and uncertainty. |
| unsupportedCausalUse | Causal conclusion, action, or assurance claim not carried by the `C.28` causal-use relation. | Prevents C.27 temporal adequacy from laundering into causal-use claim. |
| comparedClaimRefs | Claims, methods, variants, practices, agents, or regimes being compared by dynamic outcome. | `G.9` carries parity; C.27 names the dynamic claim question of the comparison. |
| dynOrderCompared | Whether the comparison is Dyn1 rate or trend comparison, or Dyn2 intervention-sensitive rate-change comparison. | Prevents rate comparison from being laundered into intervention superiority. |
| baselineWindowRef | Baseline or starting window used by the comparison. | Must not be mixed silently across compared claims. |
| adaptationOrInterventionWindowRef | Window in which adaptation, effort, intervention, rollout, training, or practice change occurs. | Optional; required when Dyn2 comparison depends on intervention timing. |
| budgetOrEffortParityRef | Budget, effort, resource, or work-parity reference needed for fair dynamic comparison. | Uses `G.9`, work, and resource patterns when load-bearing. |
| rateOrRateChangeReadingMeasureRef | Measurement reference used as evidence for compared rate, recovery, rhythm, throughput, or rate-change reading. | Uses C.16 measurement discipline. |
| G9ParityPlanRef | `G.9` parity plan reference for baseline, freshness, comparator, bridge, and evidence pins. | Mandatory when benchmark parity is load-bearing. |
| G9ParityReportRef | Optional `G.9` parity report reference carrying outcomes/evidence. | Needed for published or benchmark used beyond the local working context result. |
| evidenceBranches | Decomposition of evidence by state, rate, rate-change, effort, resistance, rhythm, or causal effect. | Shows which branches are evidence and which remain assumptions. |
| stateEvidenceRefs | Evidence for state reading or snapshot. | Evidence relation or C.16 relation. |
| rateEvidenceRefs | Evidence for rate, trend, or trajectory reading. | Evidence relation or C.16 relation. |
| rateChangeEvidenceRefs | Evidence for rate-change/intervention-sensitive reading. | Evidence/C.16 relation. |
| effortEvidenceRefs | Evidence for planned or actual effort. | Planning/work relation. |
| resistanceEvidenceRefs | Evidence for resistance/inertia proxy. | Domain evidence relation. |
| rhythmEvidenceRefs | Evidence for rhythm/cadence/coupling. | Rhythm proxy/evidence relation. |
| causalEvidenceRefs | Evidence for causal attribution. | `C.28` causal-use relation. |
| dyn2CrossScaleTransferBlock | Declared relation when a Dyn2 temporal claim moves across levels, bearers, or aggregation. | Unsupported unless aggregation basis, bearer continuity, and mix-shift risk are addressed. |
| sourceBearerRef | Bearer where evidence or claim originates. | Existing object reference. |
| targetBearerRef | Target bearer for boundary-crossing use. | Existing object reference. |
| aggregationRoute | Rule or evidence path by which local/aggregate readings are related. | Uses aggregation, model, or evidence pattern. |
| mixShiftRisk | Risk that composition changes explain the apparent rate-change. | Must be named before cross-scale transfer. |
| dynamicTransferPosture | Whether cross-scale transfer is carried by declared bearer continuity and aggregation basis, remains unsupported, or is unknown. | Prevents aggregate acceleration laundering. |
| accelerationDebt | Consequence or residue created by sustained acceleration, braking, recovery, stabilization, or redirection: rework, operational-support load, quality loss, burnout, risk, hidden queue, or coordination cost. | Use only when admissible use relies on sustained acceleration/braking/recovery/stabilization or when the domain can retain residue after effort changes or stops. |
| debtKind | Kind of debt or residue. | Domain-local, with evidence if load-bearing. |
| debtWindowRef | Window over which debt appears or must be repaid. | Separate from effort and claim windows when needed. |
| reversibilityPosture | Whether the dynamic change is reversible, costly to reverse, irreversible within window, or unknown. | `unknown` is allowed; it bounds supported use instead of forcing theory-building. |
| reversibilityNote | Short explanation of why reversibility has that posture. | Captures hysteresis and residue only when load-bearing. |
| hysteresisOrResidue | What remains after effort changes or stops. | Domain-local description requiring evidence when load-bearing. |
| repaymentOrBrakePlan | Plan to repay debt, brake, recover, or stabilize. | Planning/assurance pattern if load-bearing. |
| debtHysteresisRouteRef | Route/reference for planning, assurance, quality, wellbeing, or safety relation when debt/hysteresis is load-bearing. | C.27 records the temporal-claim question; referenced patterns carry the required discipline. |

| brakeOrRecoveryPlan | Plan for braking, recovery, stabilization, or rollback. | Planning/assurance pattern when load-bearing. |
| supportedUse | The uses this C.27 temporal-claim record can carry. | Must match `dynClaimPosture` and evidence. |
| unsupportedUse | Nearby uses this note/profile does not support. | Prevents hidden escalation. |
| reopenTrigger | Condition that requires refresh, downgrade, a higher evidence-support relation, or reference to another pattern. | Evolvability trigger for the claim. |

C.27 has a small core. Specialized cases are C.27 dynamic-claim relations
or optional profile blocks for authored temporal claims used beyond the local working context; they are not mandatory rules
for every C.27 use.

These entries are not a general relation list. They apply only after an
authored temporal claim already has C.27 relevance because it changes admissible use.
Each entry names the neighbouring FPF pattern to inspect when that C.27-typed
dynamic claim also depends on one non-C.27 question. If the text has no state,
rate, rate-change, rhythm, regime, recovery, stabilization, transfer, or
intervention relation that changes admissible use, no entry here applies.

| Dynamic-claim relation | C.27 relation and next FPF pattern |
| --- | --- |
| Formal dynamics | Reusable law, simulation, prediction, control, or calibrated dynamics is carried by `A.3.3 U.Dynamics`, `C.16`, work evidence, `G.9`, and assurance patterns. |
| C.16 rate measurement relation | Rate and rate-change readings used as evidence, benchmark, gate, control, or C.27 profile use include `c16RateMeasurementRouteRef?`; C.27 cites `C16RouteRef` and does not define measurement legality. |
| C.27 effort/work block | `dyn2EffortWorkBlock?` separates planned effort, method description, resource envelope, actual `U.Work` trace or `Gamma_work` aggregation trace, effort window, intervention actor/role assignment, and authority/capability posture; A.15 and work patterns carry role, method, work-plan, and work-occurrence alignment. |
| C.27 resistance/inertia block | `dyn2ResistanceInertiaBlock?` names resistance proxy family, resistance proxy basis posture, evidence, and unsupported downstream claim, effect, or use; `resistanceProxyBasisPosture = unknown` may carry local diagnostic use but blocks durable acceleration, causal, benchmark, promise-like, or assurance use. |
| C.27 rhythm claim block | `dyn2RhythmClaimBlock?` names bearer, anchor, window, proxy/evidence, and admissible use; coupling, phase, synchronization, or entrainment-like details appear only when the supported use depends on a relation between bearers. |
| C.27 causal-use relation | `dyn2CausalUseRoute?` is present only when a rate-change/intervention claim is used as a causal-use basis; it requires `causalInterventionSpecRef`, contrast/counterfactual, timing, outcome, assumptions, rival causes, supported causal use, unsupported causal use, and `C.28` causal-use relation. |
| C.27 dynamic benchmark requirement | `dyn2BenchmarkParityBlock?` declares the rate/rate-change/rhythm/recovery/intervention-effect requirement of a comparison; it is a benchmark input declaration, not a benchmark harness. `G.9` carries baseline, freshness, comparator, bridge, parity plan, and parity report discipline. |
| C.27 metric-as-target block | `dyn2MetricTargetEffectBlock?` splits metric-as-measure, metric-as-target or incentive, metric publication as temporal intervention, and residual probe, frame, or export cue; C.16 carries measurement, E.13 or an assurance pattern carries proxy distortion, and C.26 applies only after ordinary FPF pattern relations leave residual QL cue. |
| C.27 cross-scale transfer field | `dyn2CrossScaleTransferBlock?` keeps local and aggregate dynamic readings separate; cross-scale use needs source bearer, target bearer, aggregation basis, bearer continuity, mix-shift risk, and explicit `dynamicTransferPosture`. |
| Object-centric dynamic trace | Workflow/process rate claims need bearer, object/event trace, interaction, and convergence/divergence discipline rather than one generic process-speed label. |
| Method composition or emergent work cycle | If the live claim is about how method parts compose, how an adaptive work cycle becomes a capability, or how repeated practice changes shape, C.27 handles only the temporal adequacy of the rate, rhythm, recovery, stabilization, or rate-change claim. `B.1.5` carries order-sensitive method composition and work enactment; `B.2.4` carries meta-functional transition and capability-emergence questions. |
| State-change or evolution loop and language-state movement | If the live claim is that a system, episteme, method, cue, branch, or language-state relation evolved, reopened, stabilized, operationalized, retired, or moved through a named state-change sequence, C.27 handles only the temporal adequacy of any speed/rhythm/recovery/stabilization claim. `A.4` / `B.4` carry temporal duality and canonical evolution loops; `A.16` / `B.4.1` carry language-state move and cue-stabilization discipline. |
| C.27 scale-variable claim block | `dyn2ScaleVariableClaimBlock?` is present only when changing review capacity, tool calls, tokens, sprints, data, model capacity, parallelism, freedom of action, or another declared scale variable is used as the basis for a rate-change, learning, recovery, throughput, or stabilization claim; C.18.1 carries scale variables, scale windows, scale probes, and elasticity posture. |
| Autonomy-budget or freedom-of-action claim | If freedom of action, action tokens, decision tokens, guard cadence, depletion, pause/resume, or autonomy-gated work is used as the basis for a rate-change or stabilization claim, C.27 states the temporal claim only. `E.16` carries autonomy budgets, guard checks, ledger evidence, depletion behavior, and override speech acts. |
| C.27 viability-envelope relation | `dyn2ViabilityEnvelopeRoute?` is present only when braking, throttling, rollout speed, cadence change, recovery timing, adaptation cost, or stabilization is used to keep a declared viability bearer inside usable bounds; C.26.3 carries viability-envelope boundary regulation. |
| Publication-unit stability around temporal wording | When a paragraph, note, working section, comparison, explanation, or decision-facing text mixes method-description, repeated-practice, service-boundary, rhythm, capability-claim, improvement, benchmark, and promise wording so that the primary described entity or active claim question is unstable, use E.17.AUD, E.17.ID.CR, or the relevant publication-unit pattern first. C.27 is active only when a temporal-claim adequacy question remains after that stabilization. |
| C.27 control/policy relation | `dyn2ControlPolicyRoute?` is present only for `controlModel`, `policyRule`, `adaptive`, feedback-bearing `planningModel`, or explicit C.24/C.19/evaluation relations; C.27 records the crossing and names the pattern that carries formal control/MPC/RL/policy evaluation. |
| Dynamic policy transfer | Pattern-reference-only inside `dyn2ControlPolicyRoute?`: sequential decision/evaluation discipline carries behavior-policy/evaluation-policy and off-policy transfer claims rather than default C.27 fields. |
| Explore/exploit | C.19 carries policy health for search, convergence, narrowing, widening, and switching-rate claims. |
| Creative or open-ended search speed | Claims about faster novelty, illumination, archive growth, frontier coverage, candidate generation, or candidate-set improvement use C.17 for novelty/value measures, C.18 for open-ended search calculus, and C.19 for pool policy; C.27 only names the temporal adequacy question when speed or change affects admissible use. |
| Task-family adaptation speed | If the claim concerns acquiring usable specialization on one declared `TaskFamilyRef` or `TaskSignature`, C.27 types the learning/adaptation-rate question and C.22.1 carries threshold target, time-to-threshold, budget-to-threshold, prior exposure, transfer, retention, downside, and corridor-entry evidence. |
| C.27 debt/hysteresis block | `dyn2DebtHysteresisBlock?` is present only when admissible use depends on sustained acceleration, braking, recovery, stabilization, residue after effort changes, or high-stakes/promise/gate use; `unknown` reversibility is allowed but bounds supported use. |
| Promise / boundary / service acceptance | `A.2.3`, `A.2.8`, `A.2.9`, `A.6.C`, `F.12`, and assurance patterns carry service promises, SLA-like statements, agreement-language expectations, release gates, public commitments, boundary obligations, and service-acceptance bindings. |
| Evidence/provenance path | If a C.27 card/profile cites traces, assumptions, work evidence, evidence carriers, `PathId`, `PathSlice`, validity window, or evidence decay, C.27 states the temporal reading that needs an evidence basis. `A.10` / `G.6` carry evidence graph referring, provenance anchors, citable path/slice discipline, and SCR/RSCR-visible evidence bindings; `B.3` / `B.3.4` carry assurance posture and evidence decay / epistemic debt. |
| Dashboard telemetry, pack shipping, or refresh use | If a dashboard, time-series, telemetry pin, RSCR trigger, shipped pack, discipline-health slot, or dashboard slice is used as evidence for improvement, decay, recovery, stabilization, or rate-change, C.27 names the temporal-claim adequacy question. `C.21` carries discipline-health slot meaning; `G.12` carries DHC series/row/slice and telemetry-pin publication; `G.10` carries pack shipping; `G.11` carries refresh/decay orchestration; `G.6` carries path/slice evidence visibility. |
| Transduction gate or flow use | If a C.27-typed temporal claim is used as a `GateCheckRef` input, `GateDecisionRationale`, `LaunchGate` condition, `PathSlice` refresh trigger, crossing condition, or published flow condition, C.27 states only the temporal-claim adequacy question. `E.18` / `A.20` / `A.21` carry the transduction graph, `OperationalGate(profile)`, `ConstraintValidity`, `GateFit`, `DecisionLog`, `PathSlice`, `SquareLaw`, `Gamma_time`, and crossing pins. |
| Derivative noise | Noisy rate-change readings used for comparison, benchmark, gate, or control need sampling-window and stability posture, or downgrade. |
| Coasting | Coasting needs a basis when continued movement or stability after effort changes or stops carries the claim. |
| High-stakes temporal move | Pattern-reference-only relation: high-stakes acceleration, braking, or redirection claims name the temporal move, window, and unsupported use and cite the harm, resource, quality envelope, assurance, ethics, legal, safety, financial, or human-wellbeing pattern that governs the other question. |
| C.26 residual relation | C.27 does not add QL relation. If a Dyn2 claim also depends on probe, frame, order, export, or coarsening residue that ordinary FPF patterns cannot carry, C.26 carries the residue after ordinary C.27, C.24, C.16, G.9, and E.13 pattern relations are named. |
| No new publication object | `Dyn2TemporalClaimAdequacyCard` and `Dyn2TemporalClaimProfile` are pattern-local records/cards, not new Part G publication roles, MVPK faces, governed objects of related FPF patterns, or Kernel types. |
| Use-triggered lint | Useful lint requires temporal-improvement wording plus decision, comparison, budget, benchmark, gate, promise, publication, assurance, or intervention-plan use. |

Plain words may remain didactic. Tech prose must name the FPF pattern that carries the load-bearing question.
Problem frames, Forces, and worked examples may use speed, force, inertia,
acceleration, rhythm, cadence, agility, or process-speed language when it helps
recognition. Field definitions, conformance requirements, and governing-pattern
relations should use the Tech readings below.
Minted C.27-local labels must carry the dynamic claim question in the label: use
`Dyn2`, `Temporal`, `RateChange`, `Rhythm`, `Inertia`,
`CrossScale`, `MetricTarget`, `ControlPolicy`, or another explicit dynamic
qualifier. A generic head such as `Profile`, `Card`, `Process`, `Service`,
`Practice`, `Policy`, `Harm`, `OperationalSupport`, or `Envelope` is not enough by itself.
Ordinary prose may use those words only as Plain examples or after resolving the
actual FPF kind and reference or governing pattern.

| Plain wording | FPF-safe Tech reading |
| --- | --- |
| speed | rate, throughput, tempo, or trajectory reading with C.16 basis when load-bearing |
| acceleration | rate-change, regime transition, policy effect, or finite-difference reading |
| effort / force | planned effort, input characteristic, intervention actor/role assignment, actual work/resource trace, or resource envelope |
| mass / inertia | domain-local resistance or inertia proxy: lag, switching cost, coordination cost, queue pressure, habit persistence, physical inertia, or constraint |
| rhythm / cadence | interval-structured bearer/anchor/window/evidence relation; coupling only for cross-bearer claims |
| agility | braking, redirection, acceleration, stabilization, recovery, and constraint handling |
| process sped up | first resolve the bearer as system, work, method description, service promise/boundary, or event-log view; then add the C.27 temporal-claim question only if rate-change use is live |
| more calls / more context | agentic action whose target rate must be named, not automatic acceleration |

Avoid as Tech tokens unless already governed by the named pattern:
`carrierOrSubject`, `D2DynamicsProfile`, `Metric`, `Axis`, `Dimension`,
`Process`, `Practice`, `Service`, generic card names, `Profile`, `ProcessBearer`,
`PolicyEvaluation`, `HarmEnvelope`, `force`, `mass`, `acceleration`, and
`rhythm`.

Prefer: `DynOrder`, `Dyn2TemporalClaimAdequacyCard`, `Dyn2TemporalClaimProfile`,
`describedEntityRef`, `temporalBearerRef`, `profileCarrierRef`,
`baseCharacteristicRef`, `MeasureRef`, `DHCMethodRef`, `claimWindowRef`,
`samplingWindowRef`, `effortWindowRef`, `rhythmWindowRef`,
`plannedEffortRef`, `actualEffortTraceRef`, `inputCharacteristicRefs`,
`interventionActorRef`, `interventionAuthorityPosture`, `capabilityOrScopeRef`,
`resistanceOrInertiaProxy`, `resistanceProxyBasisPosture`,
`dyn2MetricTargetEffectBlock?`, `dyn2ObjectCentricTraceBlock?`,
`dyn2CrossScaleTransferBlock?`, `dyn2HighStakesTemporalMoveRoute?`,
`supportedUse`, `unsupportedUse`, and `reopenTrigger`.

The dynamic-order labels are values of a claim classification, not kinds of
things. Dyn0, Dyn1, and Dyn2 classify what a temporal claim treats as sufficient
for its use. They do not become `U.Dyn0`, `U.Dyn1`, `U.Dyn2`,
`U.Acceleration`, `U.Rhythm`, `U.Practice`, `U.Force`, or
`U.SecondOrderProcess`.

Kind-locality rule: `DynOrder`, `Dyn0`, `Dyn1`, `Dyn2`,
`Dyn2TemporalClaimAdequacyCard`, and `Dyn2TemporalClaimProfile` name readings
or records of authored temporal claims. They do not classify the governed object
itself unless an existing FPF pattern separately types that object. "Team
throughput accelerated" may receive a Dyn2 claim reading; the team does not
become a `Dyn2System`, throughput does not become `U.Acceleration`, and the
card/profile does not become a dynamics law.

`Dyn2TemporalClaimProfile` is a pattern-local episteme record about the adequacy of
a temporal claim. It is not `U.Dynamics`, `U.Work`, `U.WorkPlan`,
`U.MethodDescription`, `U.Measure`, or `CharacteristicSpace`. If materialized
as a document, card, table, or file, that material is a carrier of the `Dyn2TemporalClaimProfile`
content, not the actual work, process, law, practice, or system being discussed.

A.7 object/description/carrier split: `Dyn2TemporalClaimAdequacyCard` and
`Dyn2TemporalClaimProfile` are authored descriptions of temporal-claim adequacy.
They are not the dynamic system, not the work trace, not the measure, not the
service promise, not the intervention actor/role, not the dynamics law, and not identical to the
document/card/page that carries them.

The object split is:

| Object | Meaning |
| --- | --- |
| `describedEntityRef` | the entity/work/method/system/practice-like object the claim discusses, resolved through existing FPF kinds where load-bearing |
| `temporalBearerRef` | the object whose state, rate, rhythm, or regime is being read |
| `profileCarrierRef` | optional card/file/page carrier of the `Dyn2TemporalClaimProfile` content, only when publication/evidence needs it |
| `plannedEffortRef` | plan/method/resource-envelope basis for intended effort |
| `actualEffortTraceRef` | `U.Work` or `Gamma_work` basis for actual burn |
| `dynamicsModelRef` | `U.Dynamics` basis when a law/model of change is claimed |

Loose words require resolution in Tech prose. A process may be a method recipe,
dated work run, transition law, event-log view, or service situation. A practice
may be method description plus work traces. A service claim may involve system,
promise content, delivery work, boundary semantics, or assurance. C.27 should
not use these as untyped substitutes for named FPF kinds/references.


**Copy-paste authoring forms (informative).** These forms make C.27 cheap enough
to use without jumping straight to a full profile.

Dyn0 or Dyn1 exit:

```text
C.27 exit: this is a Dyn1 rate reading only.
No intervention-sensitive temporal claim is used here.
Measurement relation: <C16RouteRef or N/A>.
```

Local Dyn2 card:

```text
C.27 card:
claim:
target:
move:
intervention:
window:
resistance/cost:
basis:
supportedUse:
unsupportedUse/reopen:
```

Boundary-crossing profile header:

```text
C.27 profile header:
claimRef:
describedEntityRef:
temporalBearerRef?:
dynClaimPosture:
dynOrder:
claimWindowRef:
supportedUse:
unsupportedUse:
reopenTrigger:
activeBlocks:
```

**AI-assisted drafting posture (informative).** An AI-assisted draft may propose
that C.27 is relevant, but a profile appears only after the admissible use and the
boundary-crossing reason are named. First classify the prose as ordinary prose,
Dyn0, Dyn1, Dyn2 card, or profile/pattern relation. The draft does not infer:
more tool calls means better reasoning; faster narrowing means better search;
higher throughput means better quality; metric improvement means system
improvement; or trend means intervention model.

### C.27:5 - Archetypal Grounding

Read these cases before the fuller field definitions. They show admissible stopping points for ordinary work:

- no C.27 record for ordinary state, metaphor, or unsupported broad-use language;
- Dyn1 or C.16 when the live issue is only measured rate;
- `Dyn2TemporalClaimAdequacyCard` when a local temporal intervention, rhythm, braking, coasting, or tool-use rate-change claim needs bounded basis;
- `Dyn2TemporalClaimProfile` or a named FPF pattern relation only when the authored temporal claim is used beyond the local working context, benchmarks, promises, assures, becomes causal, crosses scale, or carries decision-use that affects gate, release, assurance, benchmark, or work-planning posture.

**Example breadth (informative).** C.27 appears across several work domains, not
only project-velocity prose.


| Domain | Example | Why C.27 cares |
| --- | --- | --- |
| Software operations | Incident recovery became faster after a playbook. | Promise, viability, and service-boundary risk can hide inside a recovery-speed claim. |
| Team work cycle | Backlog reduction under added reviewers. | Effort, window, resistance, and hidden work must be named. |
| AI agent | More tool calls speed debugging. | Tool-call count is effort evidence or input evidence, not reasoning-quality evidence. |
| Benchmark | Method A improves faster than Method B. | Dynamic comparison needs G.9 parity, not only C.27 prose. |
| Metric target | Velocity target improves velocity. | Metric-as-measure, target pressure, work change, proxy distortion, and residual probe cue stay distinct. |
| Search | Faster shortlist. | Faster narrowing can damage exploration health and frontier coverage. |
| Learning | Time-to-threshold on one task family. | C.22.1 carries task-family adaptation signature. |
| Rhythm/practice | Daily drills stabilize review rhythm. | Rhythm needs bearer, anchor, window, basis/proxy, and admissible use. |
| Scale | More tokens, data, or reviewers improve rate. | C.18.1 carries scale variable and elasticity posture. |
| Cross-scale | Team throughput becomes organization agility. | Aggregation basis, bearer continuity, and mix shift must be visible. |
| Viability | Slow rollout protects support capacity. | Braking can be the adequate temporal move; slowing down is a supported envelope-regulation outcome when acceleration would damage recovery, support load, or promise reliability. |
| QL negative | Dashboard or probe wording appears. | C.26 is relevant only for residual probe, frame, export, or coarsening cue after ordinary pattern relations. |


| Teaching case | Example | Expected classification |
| --- | --- | --- |
| Snapshot | "Backlog is 120 items today." | Dyn0; no C.27 record unless use changes. |
| Trend | "Backlog fell by 20 items/week." | Dyn1 with C.16 measurement basis if load-bearing. |
| Intervention | "Adding review capacity for two sprints will double backlog reduction rate." | `Dyn2TemporalClaimAdequacyCard`; full `Dyn2TemporalClaimProfile` usually overkill unless the authored temporal claim is used beyond local pilot or plan use. |
| Benchmark or publication | "Method A improves faster than Method B and should be published as superior." | `Dyn2TemporalClaimProfile` or pattern reference is justified: G.9 benchmark parity, C.16 measurement, possible `C.28` causal-use relation, and C.27 dynamic-claim relation declaration. |
| Dynamic anti-leaderboard | "Both methods reached the same final score, so they are equivalent." | Not enough if adaptation window, effort parity, hidden rework, validity window, or recovery profile differs; G.9 carries parity and C.27 names the temporal parity question. |
| Agentic tool-use | "More tool calls will speed debugging." | C.24 plus `Dyn2TemporalClaimAdequacyCard`; tool-call count is effort evidence or input evidence, not task-success, evidence-quality, repair-success, or cost evidence, so the claim names task outcome, evaluation harness, stop or replan condition, validity window, and non-admissible use as a benchmark claim. |
| Scale trap | "Doubling reviewers, data, or model capacity will double improvement rate." | C.18.1 carries scale variable, scale window, probes, and elasticity posture; C.27 is live only if the scale claim is used as a rate-change basis, and linear temporal improvement remains unsupported without evidence. |


| Rhythm / practice | "Daily drills stabilize training rhythm." | `Dyn2TemporalClaimAdequacyCard` with rhythm bearer, anchor, window, basis/proxy, and admissible use; coupling only if the claim depends on synchronization between bearers. |
| False positive | "This chapter accelerates reader orientation." | Usually ordinary prose; no C.27 record unless used as a claim about method effectiveness. |
| Causal trap | "Velocity rose after the workshop, so the workshop caused it." | C.27 marks the temporal-claim question only; `C.28` causal-use relation and evidence relation are required before causal use. |
| Cross-scale trap | "Team throughput accelerated, so every service improved." | `dyn2CrossScaleTransferBlock?` is unsupported without source bearer, target bearer, aggregation basis, bearer continuity, mix-shift risk, and `dynamicTransferPosture`. |
| Braking | "Slow rollout protects support capacity." | `Dyn2TemporalClaimAdequacyCard` or `Dyn2TemporalClaimProfile` depending on supported decision; the move may be a correct protection of viability, not a failure to accelerate. |


Additional dynamic near-misses:

| Case | Example | Expected classification |
| --- | --- | --- |
| Coasting | "Adoption continues after incentives stop." | `Dyn2TemporalClaimAdequacyCard` with coasting basis and reopen trigger. |
| High-stakes temporal move | "We can cut review time in half for this regulated release." | Pattern-reference-only `dyn2HighStakesTemporalMoveRoute?` plus assurance/legal/quality relation, or claim downgraded. |
| Premature convergence | "The search process is better because we reached a shortlist faster." | C.19 relation; distinguish faster narrowing from healthy search. |
| Metric target | "Velocity improved after becoming the quarterly target." | `dyn2MetricTargetEffectBlock?` only if target publication changes temporal behavior and admissible use; C.16 carries measurement, E.13 or proxy audit carries utility distortion, and C.26 applies only for residual probe, frame, or export cue. |
| Scale-variable fantasy | "More data, model capacity, reviewers, tokens, or parallelism will improve twice as fast." | C.18.1 carries scale variables, scale windows, scale probes, and elasticity posture; C.27 only names the temporal claim when the scale variable is used as the basis for rate-change, learning, recovery, throughput, or stabilization. |
| Off-policy transfer | "The old rollout policy improved recovery, so the new rollout policy will too." | `dyn2ControlPolicyRoute?` must name `behaviorPolicyRef`, `proposedPolicyRef`, `offPolicyRisk`, and evaluation/control relation; one observed slope under policy A does not carry policy B. |
| Object-centric process trace | "The process sped up" while orders, invoices, shipments, and support tickets move through different paths. | `dyn2ObjectCentricTraceBlock?` recovers object types, event trace, interactions, aggregation basis, and unsupported whole work-cycle truth; one scalar throughput line is not enough. |
| Harmful acceleration and viability | "Faster rollout improved release velocity while support load and recovery time degraded." | C.27 names acceleration, braking, throttling, recovery timing, and unsupported downstream claim, effect, or use; C.26.3, C.25, assurance, safety, legal, ethics, or wellbeing patterns carry the envelope or harm claim. |

These slices show what C.27 changes in use. They are action examples, not extra forms to fill.

Operations / backlog acceleration:

```text
Claim:
Adding two triage engineers for two sprints will double backlog reduction rate.

C.27 reading:
Dyn2, because a rate-change is tied to a planned intervention.

Minimum useful note:
- rate being changed: backlog reduction per week;
- effort or input: two triage engineers assigned through a WorkPlan for two sprints;
- effort window: sprint N and N+1;
- resistance proxy: review queue coordination cost and domain ramp-up;
- evidence posture: planning assumption plus prior work trace if available;
- supported use: staffing discussion and local plan choice;
- unsupported use: `C.28`-governed causal-use claim with estimand and identification relation, long-term capacity model, benchmark superiority;
- reopen trigger: queue mix shift, triage saturation, quality loss, or no
  measured reduction after the first sprint.
```

The value is not that every backlog sentence gets a profile. The value is that a
decision-bearing acceleration claim cannot hide effort, window, resistance, and
unsupported downstream claim, effect, or use.

Learning / practice transfer:

```text
Claim:
Daily 20-minute drills stabilize the learner's problem-solving rhythm.

C.27 reading:
Dyn2 only if the claim is used to select, compare, publish, or justify the
practice. Otherwise it may remain didactic.

Minimum useful note:
- rhythm bearer: learner practice session;
- rhythm anchor: daily drill window and task cycle;
- rhythm proxy/evidence: task completion cadence, error pattern, recall delay,
  or observed practice trace;
- effort profile: short scheduled effort repeated across days;
- resistance proxy: fatigue, attention drift, task novelty, or habit formation;
- supported use: local practice design;
- unsupported use: general proof that the method improves all learning;
- reopen trigger: retention falls, task family changes, or rhythm proxy stops
  matching actual performance.
```

This carries the source article's replicable-practice idea: the useful formal
payload is an effort/rhythm/window description that can be copied and checked,
not a forced equation.

Rhythm/practice style vignette:

```text
Claim:
A training note says "this practice rhythm improves retention", or a dance note
says "this style keeps swing content".

C.27 reading:
Dyn2 only when the rhythm/style claim is used to teach, replicate, compare,
judge, benchmark, or promise a practice outcome. Otherwise it may remain
ordinary explanatory prose.

Minimum useful questions:
- rhythm of what bearer: learner, team, body movement, practice session,
  release cycle, or other named FPF kind and reference?
- anchored to what beat, cycle, release train, attention window, task cycle, or
  domain-local interval?
- what effort or rate-change pattern occurs in which intervals?
- what evidence or instrument proxy supplies the basis for that reading?
- what use is carried: teaching orientation, replication, judging, benchmark,
  or promise?
```

This keeps the article's useful dance/practice insight: style distinction may
depend on effort and rate-change patterns over rhythm intervals, not only on
static poses, single trajectories, mood words, or a general rhythm theory.

Rhythm / embodied or team coordination:

```text
Claim:
The team's release rhythm became smoother after moving review earlier in the
cycle.

C.27 reading:
Dyn2 when this carries a method-change, staffing-decision, or benchmark use.

Minimum useful note:
- rhythm bearer: team release cycle, not the repository file or dashboard;
- rhythm anchor: release cycle and review window;
- intervention regime: scheduled shift of review earlier in the cycle;
- instrument proxy: event log, review queue cadence, rework trace, or survey
  only if its resistance proxy basis posture is stated;
- resistance proxy: transfer delay, queue pressure, coordination lag;
- supported use: local method adjustment;
- unsupported use: proof of organizational agility or service promise;
- reopen trigger: work mix changes, release train changes, or hidden rework
  appears.
```

The important correction is that rhythm has a bearer and proxy. It is not a
decorative label for good mood or smoothness.

Agentic tool-use / AI work cycle:

```text
Claim:
More tool calls will speed debugging.

C.27 reading:
Dyn2 only if the extra calls are used as an intervention claim, not merely as a
local tactic.

Minimum useful note:
- rate being changed: bug localization, evidence confirmation, repair
  iteration, uncertainty reduction, or rollout stabilization;
- effort or input: extra tool calls, broader search, or deeper context retrieval;
- intervention actor: agent, tool runner, or human operator capable of making the calls;
- resistance proxy: noisy output, context overload, search branching, cost, or
  stale evidence;
- outcome/evaluation basis: task success, repair success, evidence quality,
  cost, and validity window if the claim is benchmark-facing;
- stop/replan trigger: no new evidence, conflicting evidence, timeout, rising
  cost, expired validity window, or growing false-positive load;
- unsupported use: "more calls means better reasoning", "faster narrowing is
  always better", or "tool-call count proves benchmark superiority."
```

This keeps C.24 useful without turning tool-use quantity into a proxy for
thinking quality.

Benchmark / faster improvement:

```text
Claim:
Method A improves faster than Method B.

C.27 reading:
`G.9` governs benchmark parity; `dyn2BenchmarkParityBlock?` types the dynamic
outcome and records unsupported benchmark use.

Minimum useful note:
- compared claims: Method A and Method B;
- dynamic order: Dyn1 if only rates are compared, Dyn2 if interventions,
  effort budgets, or rate-change are compared;
- comparable windows: baseline, sampling, claim, validity, and adaptation or
  effort windows;
- comparable effort: planned budget and actual effort trace if relevant;
- G.9 parity: `G9ParityPlanRef` for baseline/freshness/comparator/bridge pins,
  and `G9ParityReportRef?` if a published or reused report exists;
- hidden costs: rework, operational-support load, quality loss, burnout, or debt;
- supported use: benchmark interpretation under stated parity;
- unsupported use: causal superiority, universal method superiority, or release
  gate unless another FPF pattern governs that claim.

```

This prevents "faster" from hiding unequal effort, unequal windows, or unequal
measurement templates.

Service / boundary promise:

```text
Claim:
We recover incidents faster after the new playbook.

C.27 reading:
Dyn2 if the playbook is claimed to change recovery rate. If the statement is
used outside the local working context, as an SLA-like expectation, or as readiness evidence, C.27 only
types the temporal-claim question.

Minimum useful note:
- rate being changed: detection-to-mitigation or mitigation-to-recovery time;
- effort or input: playbook, staffing, automation, triage method, or escalation
  policy;
- resistance proxy: incident mix, dependency lag, tool latency, coordination
  bottleneck;
- evidence posture: diagnostic, benchmark, causal, assurance, or promise-like;
- supported use: local incident-response improvement claim;
- unsupported use: formal guarantee, audit closure, release gate, or causal
  proof unless the relevant boundary/evidence/assurance pattern carries it.
```

The key point is that C.27 does not become a hidden promise pattern. It prevents
temporal claims from silently widening into promises.

Aggregate or cross-scale transfer:

```text
Claim:
Team throughput accelerated, so the organization became more agile.

C.27 reading:
`dyn2CrossScaleTransferBlock?` is live; local team rate-change and organization
agility are different dynamic readings unless aggregation basis and bearer
continuity are declared.

Minimum useful note:
- source bearer: team work cycle and its measured throughput;
- target bearer: organization, portfolio, service family, or ecosystem;
- aggregation basis: how local rate-change maps upward;
- bearer continuity: whether the same work, service, value stream, or population
  remains comparable;
- mix-shift risk: easier work, hidden queues, reassigned work, changed scope, or
  invisible rework;
- dynamicTransferPosture: supported, unsupported, or unknown;
- supported use: local team improvement if evidence supports it;
- unsupported use: organization-level agility claim unless aggregation and
  quality-bundle relations are present.

```

This protects multi-scale FPF reasoning: a rate-change does not transfer across
levels merely because the same speed word appears at each level.

Goodhart / performative metric:

```text
Claim:
Velocity improved after it became the quarterly target.

C.27 reading:
`dyn2MetricTargetEffectBlock?` may be live if metric publication or target use is a
temporal intervention. The central distinction is measurement, target or incentive,
real process change, and residual probe, frame, or export cue.

Minimum useful note:
- metric measure: the published velocity/throughput reading, with C.16 relation if
  measurement legality or comparability is load-bearing;
- target or incentive use: quarterly target, gate, dashboard, budget signal, or
  public comparison;
- possible behavior change: smaller tickets, hidden work, quality reduction,
  postponed rework, selection of easier tasks;


- process-vs-measurement split: measurement/probe effect, real work change,
  gaming/selection effect, causal effect if claimed;
- E.13 or proxy relation: proxy distortion or utility distortion if velocity diverges from the
  actual work objective;
- C.26 relation: only if residual probe, frame, order, or export cue remains after
  C.27, C.16, and E.13 pattern relations;
- supported use: diagnostic investigation or metric design review;
- unsupported use: proof that the underlying work system improved.

```

This is the practical bridge between C.27, C.16, C.26, and evidence patterns.


### C.27:6 - Bias-Annotation

Use C.27 only where it improves FPF as a first-practical entry and pattern relation
pattern for temporal-claim adequacy. It is not enough for C.27 to be a correct
dynamic-claim schema. The useful result is that a cold reader can notice when a
state/rate reading is being used as a rate-change, rhythm-change, intervention,
braking, coasting, recovery, stabilization, benchmark, promise, or assurance
claim; choose the least-committing admissible next output; and stop or cite the carrying pattern without making
C.27 absorb that pattern's governed concern.

The missing-question content belongs here only where it strengthens
three practical abilities:

- how a reader finds C.27 from ordinary working language such as speed up, slow
  down, recover, stabilize, sustain cadence, improve faster, change direction,
  or reduce risk faster;
- how source ideas become FPF-facing guidance without turning physical or dynamic metaphors into new ontology: adopted, adapted,
  carried by another FPF pattern, or rejected as literal dynamics ontology;
- how C.27 keeps higher-demand claim relations with existing FPF patterns instead of
  becoming a general pattern for measurement, dynamics law, work, search,
  benchmarks, promises, assurance, viability, publication-unit stability, or QL.

Additional detail is useful only when it improves one of those three abilities
or clarifies a stopping condition. More fields, case notes, or pattern-relation prose is
rejected when they only make C.27 harder to refuse, harder to stop, or easier to
misread as a general theory of change.

**Gov.** C.27 reduces hidden decision-claim inflation: local diagnosis, planning basis, benchmark use, public promise, and assurance use remain different claim uses.

**Arch.** C.27 is biased against stealing work from neighbouring patterns. It types authored temporal-claim adequacy question while measurement, formal dynamics, work, search, benchmark, promise, causality, quality, value, viability, scale, adaptation, and QL relations remain with the patterns that govern those concerns.

**Onto/Epist.** C.27 is biased toward described system, description, and carrier separation and toward explicit claim posture. It treats Dyn0, Dyn1, and Dyn2 as readings of authored temporal claims, not as kinds of systems.

**Prag/Did.** C.27 is biased toward cheap stopping, card-first use, and teaching through cases before field machinery. The first lesson is: a trend is not yet an intervention model.

### C.27:7 - Conformance Checklist

Use these requirements to judge whether a C.27 record or C.27-facing paragraph
is sufficiently supported for the use it is making. Ordinary local use can stay small.

| Requirement | C.27 content |
| --- | --- |
| Applicability | A C.27 record exists only when the temporal distinction changes supported use, governing-pattern relation, evidence posture, or decision interpretation. |
| DynOrder | The body distinguishes state reading, rate reading, and intervention-sensitive rate-change, rhythm, or regime reading. |
| Minimal output | The output is the minimal one that changes use: no C.27 record, Dyn0 reading, Dyn1 reading, `Dyn2TemporalClaimAdequacyCard`, `Dyn2TemporalClaimProfile`, or formal-model relation. |
| Card minimum | A `Dyn2TemporalClaimAdequacyCard` names target, move, intervention, window, resistance or cost, basis, supported use, unsupported downstream claim, effect, or use, and reopen or pattern-reference condition. |
| Boundary-crossing profile | `Dyn2TemporalClaimProfile` appears only when the authored temporal claim is used beyond the local working context into benchmark, publication, assurance, promise-like, gate, reusable method, cross-context, cross-scale, or formal/control use. |
| Governing-pattern relation | C.27 does not carry measurement, transition law, Work actuals, planning, `C.28`-governed causal-use claim, benchmark parity, promise or boundary claim, assurance, or QL residue. |
| Neighboring-pattern-use block | If supported use relies on measurement, causal attribution, benchmark parity, control/policy, cross-scale transfer, debt/hysteresis, promise, high-stakes temporal move, or QL residue, the corresponding governing-pattern relation or present profile block is named. |
| Profile-block closure | Every present block is defined by C.27, pattern-reference-only, or absent from `activeBlocks`; a block name is not a new governed object. |
| Pattern-relation economy | Add a C.27 relation note to another pattern only when that pattern has a concrete boundary reason to inspect temporal-claim adequacy; otherwise a C.27 card or profile cites the FPF pattern that governs the other question instead of creating a thin duplicate temporal record. |
| Exit | If no downstream claim, effect, or use changes, the claim remains ordinary prose, Dyn0 reading, Dyn1 reading, C.16 measurement, `U.Dynamics`, or another governing pattern. |


**Value and harm boundary.** A temporally adequate claim is not automatically a
valuable claim. A valuable claim is not automatically temporally adequate. If
value, harm, safety, legal, ethics, quality, or promise impact is load-bearing,
C.27 states only the temporal move, window, supported use, unsupported
downstream claim, effect, or use, and pattern relation. The value, harm, safety, legal, ethics, quality, or
promise pattern governs the other question.

**Conceptual lint classes (informative).** These labels describe cheap
inspection faults, not a required tool.

| Lint | Failure | Repair |
| --- | --- | --- |
| `C27-KEYWORD-OVERREACH` | A speed/rhythm word creates a profile without a supported-use change. | Downgrade to ordinary prose, Dyn0, or Dyn1. |
| `C27-MISSING-CARD-MINIMUM` | Dyn2 card lacks target, move, intervention, window, resistance or cost, basis, supported use, or reopen condition. | Complete the card or downgrade. |
| `C27-PROFILE-WITHOUT-BOUNDARY-USE` | A profile is used for a local note. | Downgrade to a local card. |
| `C27-PATTERN-RELATION-THEFT` | C.27 carries measurement, dynamics-law, work, benchmark, promise, or QL content. | Keep that content with the FPF pattern that governs the other question. |
| `C27-DYNORDER-AS-KIND` | Teams, systems, services, or methods become Dyn2 objects. | Repair to an authored-claim reading. |
| `C27-CAUSAL-LAUNDERING` | Rate changed after effort, therefore effort caused it. | Add `C.28` causal-use relation or mark causal use unsupported. |
| `C27-METRIC-TARGET-CONFLATION` | Metric improved, therefore the system improved. | Split measure, target pressure, work change, proxy distortion, and residual probe cue. |
| `C27-PROMISE-LAUNDERING` | Planning temporal claim becomes SLA, service guarantee, or commitment. | Keep promise/boundary/service content with the patterns that carry it. |

**Common failure modes after adoption (informative).**

| Failure mode | Correction |
| --- | --- |
| Profile inflation | Every temporal phrase gets a profile; keep profile use for boundary-crossing claim use. |
| Pattern-relation theft | C.27 carries measurement, work, promise, benchmark, or QL; return the other question to the FPF pattern that governs it. |
| Card laundering | A local card is cited as `C.28`-governed causal-use claim, benchmark result, release approval, or service promise; mark that use unsupported. |
| DynOrder reification | A team or system becomes "Dyn2"; keep DynOrder as a reading of authored temporal claims. |
| Relation-note inflation | Every nearby pattern gets a C.27 note just in case; add a note only when the pattern must inspect temporal-claim adequacy directly. |

### C.27:8 - Common Anti-Patterns and How to Avoid Them

C.27 starts with the anti-patterns most likely to make a working reader misuse a
state/rate reading as a Dyn2 temporal claim. Less frequent traps belong in the
extended bank and should not become a first-screen checklist.

| Core anti-pattern | What it looks like | Repair |
| --- | --- | --- |
| Rate -> intervention laundering | "We measured throughput, therefore we know how to accelerate it." | Ask whether the claim is Dyn0 state, Dyn1 rate, or Dyn2 rate-change under effort/resistance/window; add only the least-committing C.27 record that changes admissible use. |
| Effort-free acceleration | "Velocity will double" with no effort, input, intervention actor/role, resistance proxy, window, evidence, or supported use. | Add a `Dyn2TemporalClaimAdequacyCard` or downgrade to Dyn1 measurement. |
| Past slope as control model | A historical trend is treated as a future intervention law. | Separate observed Dyn1 trend from Dyn2 intervention claim and formal-model relation. |
| C.27 as `C.28`-governed causal-use claim | Rate changed after effort, therefore effort caused it. | Mark planning/diagnostic posture or include `dyn2CausalUseRoute?` with `causalInterventionSpecRef`, contrast/counterfactual, timing, outcome, assumptions, rival causes, supported causal use and unsupported causal use, and `C.28` causal-use relation. |
| Rhythm as decoration | Rhythm names vibe/cadence with no bearer, anchor, window, proxy, evidence, or supported use. | Name bearer, anchor, window, instrument/evidence proxy, and supported use; add coupling/phase/entrainment only when the claim depends on a cross-bearer relation. |
| Metric-accelerated theater | The measured rate improves after becoming a target while hidden work worsens. | Separate real work-rate change, measurement/probe effect, gaming risk, and temporal intervention effect. |
| Aggregate acceleration laundering | Local speed or aggregate speed is laundered across levels. | Separate local bearer, aggregate bearer, mix shift, aggregation basis, and `dynamicTransferPosture`. |
| Acceleration bias | Faster is treated as better by default. | Make braking, pause, stabilization, redirection, coasting, and slower rollout legitimate outcomes. |

Use the negative cases to make non-use easy. They are not profile triggers.

| Negative case | Correct C.27 outcome |
| --- | --- |
| "This section accelerates orientation." | No C.27 record unless the `PublicationUnit` carries that acceleration claim as the basis for a decision, promise, intervention, or comparison. |
| "The chart shows throughput rising." | Dyn1; C.16 only if the measurement construction is load-bearing. No C.27 record unless a rate-change intervention claim appears. |
| "The team has a strong rhythm." | No C.27 record unless rhythm carries a decision-use; then name bearer, anchor, window, evidence proxy, and admissible use. |
| "We use a dashboard of velocity." | C.16/E.13/C.26.1 when the live issue is measurement, proxy distortion, or probe/publication effect; C.27 only when the dashboard is claimed to change a temporal outcome. |
| "The model is dynamic." | `U.Dynamics` when a state-space or transition law is being described; no C.27 record unless authored prose makes a rate-change adequacy claim. |
| "The agent used more calls." | C.24/work-trace relation; C.27 only when more calls are claimed to change debugging, search, learning, recovery, or stabilization rate. |
| "The process is agile." | A.6.P/local-head restoration first when "agile" is overloaded; C.27 only when braking, redirection, or rate-change question is live. |

Use the extended anti-patterns only when the live temporal claim actually raises
that trap.

| Extended anti-pattern | What it looks like | Repair |
| --- | --- | --- |
| Keyword-triggered bureaucracy | Any speed, rhythm, agility, throughput, velocity, accelerate, or slow-down word forces a profile. | Use supported-use relevance, not keyword matching. |
| Derivative label without template | Acceleration, velocity, momentum, or cadence number lacks base characteristic, unit, scale, sampling window, method, and evidence. | Use C.16 measurement construction. |
| Rhythm bearer mismatch | Evidence from one bearer/window is applied to another. | Add bridge/evidence relation or mark transfer unsupported. |
| Effort window hidden in plan prose | Plan says "push harder" without WorkPlan, method, resource envelope, or actual burn evidence relation. | Attach planned effort to planning patterns and actual burn to work patterns. |
| Dynamics law as work log | Work trace or telemetry is treated as the law of change. | Keep `U.Dynamics` separate from `U.Work` evidence. |
| Agility as cornering speed | "Change direction fast" hides braking and redirection cost. | Name braking, redirection cost, intervention constraints, evidence, and admissible use. |
| Premature convergence by acceleration | Faster narrowing collapses diversity, novelty, or frontier coverage. | Use C.17, C.18, and C.19 as applicable and distinguish exploitation speed from healthy search. |
| Dyn2 profile as hidden promise | A planning note becomes a service guarantee, SLA-like statement, or public commitment. | Separate planning basis from promise content and boundary obligation. |
| Noisy acceleration worship | Small variation is overread as meaningful rate-change. | Widen sampling, add uncertainty, downgrade, or collect higher-quality or more directly relevant evidence. |
| Tool-call acceleration theater | More calls or more context are treated as faster reasoning. | Name the target rate-change and stop/replan trigger. |
| Harmful acceleration | Work is accelerated while safety, ethics, legality, operational-support load, or human wellbeing becomes worse. | Use pattern-reference-only `dyn2HighStakesTemporalMoveRoute?` to name the high-stakes temporal move, window, and unsupported use and cite the assurance, ethics, legal, safety, quality, or wellbeing pattern that governs the other question. |
| Coasting claim without basis | Continued motion after effort stops is treated as free evidence of success. | Name coasting basis: habit, automation, stored work, learned capability, social norm, commitment momentum, physical inertia, queue pressure, or unknown. |
| Reversibility fantasy | Effort is removed and the system is assumed to return cleanly. | Include `dyn2DebtHysteresisBlock?` only when supported use depends on residue/reversibility; record `unknown` if needed and bound supported use, with brake/recovery relation when load-bearing. |


### C.27:9 - Consequences

C.27 should make FPF better at planning and reviewing dynamic
claims while keeping ordinary state and rate claims cheap. Its main cost is one
more C-pattern and several neighbour notes in existing FPF patterns. The mitigation is the
central affordability rule: C.27 must be easier not to use than to misuse.


C.27 claims decay over time. Refresh or reopen when:
Refresh posture stays proportional:

```text
Local C.27 card:
  has reopenTrigger only.

Boundary-crossing C.27 profile:
  has validityWindowRef and evidence valid_until when load-bearing.

Part G / benchmark / SoTA / public method claim:
  C.27 reopenTrigger feeds G.11 refresh orchestration;
  C.27 does not become a refresh ledger.
```


- sampling window, cadence, or time base changes;
- effort envelope or resource budget changes;
- intervention actor/role capacity, authority, or availability changes;
- inertia/resistance proxy changes: new tooling, team, queue topology, domain,
  work mix, constraints, or service environment;
- metric becomes a target, incentive, gate, dashboard, or public comparison;
- cross-scale transfer is attempted;
- outcome reverses, overshoots, oscillates, or becomes unstable;
- hidden queues, rework, burnout, quality loss, operational-support load, safety load, or
  coordination debt appear;
- rhythm bearer, anchor, window, proxy, or coupling changes;
- claim posture changes from assumption/diagnostic to benchmark, assurance,
  causal, promise-like, publication, or formal model use;
- the claim is reused outside its original validity window or domain;
- a coasting, braking, or recovery claim continues after effort changes or stops.

Local `Dyn2TemporalClaimAdequacyCard`s normally need only a reopen, downgrade,
or pattern-reference condition. `Dyn2TemporalClaimProfile`s for boundary-crossing claim use should cite
`validityWindowRef` or evidence `valid_until` when the claim carries a
benchmark, gate, assurance, promise-like use, reusable method, publication, or
formal-model relation. If rate-change evidence decays, freshness and epistemic-debt
handling belongs with B.3.4 or G.11 rather than becoming a C.27 freshness calculus.

When a Dyn2 benchmark, task-family adaptation claim, public method claim,
selector-facing claim, SoTA-bearing publication claim, or other Part G publication carries a
temporal-claim record, C.27 `reopenTrigger` is not enough by itself. C.27 states
the temporal-claim question and its validity/reopen basis; G.9 carries benchmark parity
when comparison is live; G.11 carries refresh orchestration such as refresh
queue, refresh plan, refresh report, deprecation notice, or edition bump when
evidence, comparator editions, method editions, claim windows, or validity
windows drift.

### C.27:10 - Rationale

The source basis is most relevant where it replaces
the question "what is the speed?" with "what effort profile, over which windows,
changes speed, rhythm, direction, or stability under resistance and cost?" The
C.27 keeps that practical move while rejecting physics ontology,
mandatory calculus, false QL relevance, and default full-profile
bureaucracy.


C.27 acts in FPF as a small modern correction for one recurring failure:
working texts observe or name a rate and then behave as if they know how to
change that rate. The pattern brings FPF up to modern practice only in the
following shape:

- the state/rate/rate-change distinction remains the cheap recognition gain;
- control, policy evaluation, causal inference, process mining, benchmarking,
  rhythm, and high-stakes temporal-move cases appear as present profile blocks;
- quantum-like residual cases appear only as C.26 relations, not as C.27 claim-adequacy content
  blocks or fields of one universal dynamic object;
- control fields stay absent by default and appear only for control-style use;
- behavior-policy versus evaluation-policy discipline is visible when
  off-policy or sequential-policy transfer is claimed;
- causal claims carry intervention contrast, time zero, follow-up, outcome,
  assumptions, and identification/evaluation relation rather than C.27 shorthand;
- performative and Goodhart cases separate metric-as-measure,
  metric-as-target, and metric-as-intervention;
- work-cycle/process claims name bearer, object/event trace, interaction, and
  convergence/divergence rather than one generic process-speed label;
- dynamic benchmarks use C.27 to type the temporal-claim question while G.9 carries
  parity;
- rhythm claims stay bearer+anchor+window+basis+supported-use by default, with
  entrainment or coupling claims with cross-bearer evidence commitments only when the claim needs them;
- quantum-like use stays out of C.27 unless a residual probe/order/frame/export
  cue remains after ordinary C.27, C.24, C.16, G.9, and E.13 pattern relations;
- full `Dyn2TemporalClaimProfile`s remain rare, and the pattern improves action quality more than
  it increases paperwork.

One-line SoTA formulation for C.27: it makes
intervention-sensitive temporal claims explicit - policy, effort, window,
resistance, feedback, evidence, bearer, and supported use - while refusing to
treat every speed/rhythm phrase as control theory, `C.28`-governed causal-use claim, benchmark
superiority, or quantum-like modeling.

### C.27:11 - SoTA-Echoing

C.27 should be shaped by current modeling practice without becoming a survey
paper. The C.27 SoTA posture is: C.27 is intervention-sensitive temporal
claim adequacy with explicit epistemic/claim posture, not literal second
derivative everywhere and not universal control theory.

Source binding used by this section:

| Source line | C.27 use | Adopt / adapt / reject posture |
| --- | --- | --- |
| `D2-SRC-1` - the source article on state, first-derivative dynamics, second-derivative dynamics, effort intervals, and rhythm practice. | Sets the working question: are we only reading speed/rhythm, or claiming that effort over time changes speed/rhythm? | Adopt the question shift and dance/practice usability examples; adapt physical vocabulary into authored temporal-claim adequacy; reject new Kernel `force`, `mass`, `acceleration`, or `rhythm` kinds. |
| `D2-SRC-2` - learning-based MPC and engineering MPC practice. | Disciplines control-style temporal claims with horizon, constraints, uncertainty, feedback update, and stability only when control language is live. | Adapt into optional `dyn2ControlPolicyRoute?`; reject making every Dyn2 card a control model. |
| `D2-SRC-3` - safe RL, off-policy evaluation, conservative/offline RL, and dynamic treatment-regime practice. | Disciplines policy/regime transfer, policy-overlap, unsafe exploration, behavior policy, evaluation policy, and repeated intervention timing. | Adapt into `dyn2ControlPolicyRoute?` when a policy/regime claim is live; reject policy-transfer evidence basis from one observed slope alone. |
| `D2-SRC-4` - causal inference for intervention effects. | Separates planning/diagnostic Dyn2 claims from causal effect claims. | Adopt causal question, comparator/counterfactual, estimand, timing, outcome, assumptions, rival causes, and evidence-design discipline for `dyn2CausalUseRoute?`; reject `C.28` causal-use claim completion inside C.27 itself. |
| `D2-SRC-5` - performative prediction and Goodhart variants. | Shows that metric publication, target use, incentives, or gates may change behavior rather than merely report it. | Adapt into `dyn2MetricTargetEffectBlock?`; C.16 carries measurement, E.13 or an assurance pattern carries proxy distortion, and C.26 carries residual probe, frame, or export cues; reject a generic Goodhart catch-all. |
| `D2-SRC-6` - object-centric process mining and object-centric event logs. | Shows why scalar throughput often hides multiple object bearers, event traces, interactions, and aggregation risks. | Adapt into `dyn2ObjectCentricTraceBlock?` and object-centric trace requirements; reject one scalar rate as whole work-cycle truth when multi-object interaction is live. |
| `D2-SRC-7` - active inference / active sensing practice. | Reminds C.27 that measurement can be action, while ordinary FPF pattern relations remain primary. | Adapt as a local relation test for measurement, state-space, planning, evidence, control, causal, or process-log basis; reject automatic QL relevance from planned measurement or typed states. |
| `D2-SRC-8` - rhythm, beat synchronization, groove, entrainment, and compliant-system timing work. | Disciplines rhythm claims with bearer, anchor, window, proxy/evidence, and admissible use; coupling/phase/entrainment appear only for cross-bearer claims with explicit coupling, phase, or entrainment commitments. | Adapt into rhythm fields on `Dyn2TemporalClaimAdequacyCard`; reject a standalone `U.Rhythm` kind or decorative rhythm vocabulary. |

SoTA lesson -> FPF obligation map:

| Modern lesson | C.27 obligation | Pattern that governs the other question |
| --- | --- | --- |
| MPC/control practice separates horizon, constraints, uncertainty, and feedback update. | Name control horizon/update only when the temporal claim is control-style. | `A.3.3 U.Dynamics`, C.16, C.19/C.24, evidence/assurance patterns. |
| OPE/safe RL separates behavior policy, evaluation policy, policy overlap, and unsafe-exploration risk. | Do not transfer evidence from policy A to policy B without behavior-policy, evaluation-policy, and `offPolicyRisk`. | `dyn2ControlPolicyRoute?` plus evaluation/control relations. |
| Causal inference separates intervention timing, comparator/counterfactual, estimand, follow-up, assumptions, and rival causes. | Keep planning/diagnostic Dyn2 distinct from `C.28`-governed causal-use claim. | `C.28` and evidence patterns. |
| Performative prediction and Goodhart variants show that published targets can change behavior. | Split metric-as-measure, target or incentive use, temporal intervention, and proxy distortion. | C.16, E.13 or an assurance pattern, C.26 only for residual probe or frame cue. |
| Object-centric process mining shows scalar throughput can hide multi-object interaction. | Recover object types, event trace, interaction note, and aggregation basis when process speed is load-bearing. | Local process evidence/OCPM discipline plus C.27 object-centric trace block. |
| Rhythm research treats rhythm as bearer/anchor/window/proxy/coupling-if-live. | Keep cadence/rhythm claims tied to bearer, anchor, evidence, supported use, and optional coupling only when cross-bearer relation matters. | C.27 rhythm card plus C.16/evidence when measured. |
| Scaling-law practice separates scale variable, scale window, probe, and elasticity. | Do not infer linear improvement from more data, tokens, calls, reviewers, or capacity. | C.18.1 and G.9 when compared. |
| Benchmark practice needs parity pins, baselines, freshness, budgets, and comparator editions. | Do not read faster improvement as benchmark superiority without parity plan/report. | G.9. |

Source id references:
- `D2-SRC-1`: [Статика, динамика первой производной, динамика второй производной](https://ailev.livejournal.com/1648977.html).
- `D2-SRC-2`: [Learning-Based Model Predictive Control: Toward Safe Learning in Control](https://www.annualreviews.org/eprint/2STMCYXGPHBRMTDP9W2D/full/10.1146/annurev-control-090419-075625) and [Review on model predictive control: an engineering perspective](https://link.springer.com/article/10.1007/s00170-021-07682-3).
- `D2-SRC-3`: [A Survey of Constraint Formulations in Safe Reinforcement Learning](https://www.ijcai.org/proceedings/2024/0913.pdf), [A Review of Off-Policy Evaluation in Reinforcement Learning](https://arxiv.org/pdf/2212.06355), [Conservative Q-Learning for Offline Reinforcement Learning](https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html), and [Methods in dynamic treatment regimens using observational healthcare data](https://www.sciencedirect.com/science/article/pii/S0169260725000756).
- `D2-SRC-4`: [Causal Inference: What If](https://miguelhernan.org/whatifbook) and [Causal Inference About the Effects of Interventions From Observational Studies in Medical Journals](https://jamanetwork.com/journals/jama/fullarticle/2818746).
- `D2-SRC-5`: [Performative Prediction](https://proceedings.mlr.press/v119/perdomo20a.html), [Performative Prediction: Past and Future](https://arxiv.org/pdf/2310.16608), and [Categorizing Variants of Goodhart's Law](https://arxiv.org/abs/1803.04585).
- `D2-SRC-6`: [OCEL 2.0](https://www.ocel-standard.org/) and [Object-Centric Event Logs: Specifications, Comparative Analysis and Refinement](https://arxiv.org/html/2405.12709v1).
- `D2-SRC-7`: [Active Inference: A Process Theory](https://activeinference.github.io/papers/process_theory.pdf) and [Embodied decisions as active inference](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1013180).
- `D2-SRC-8`: [Neural entrainment underpins sensorimotor synchronization to dynamic rhythmic stimuli](https://www.sciencedirect.com/science/article/pii/S1053811923003774), [A review of psychological and neuroscientific research on musical groove](https://www.sciencedirect.com/science/article/pii/S0149763423004918), and [Finding the rhythm](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1011478).

Control and MPC. Control-style claims need horizon, constraints, uncertainty,
feedback update, and stability only when control language is live. A local
`Dyn2TemporalClaimAdequacyCard` can say "we plan to brake rollout for two weeks to protect operational-support
capacity" without becoming MPC. If the claim is not control-style, do not fill
control fields. A control claim used beyond the local working context needs the neighboring governing-pattern relation.

C.27 control/policy relation: `dyn2ControlPolicyRoute?` is present only when
`dynClaimPosture` is `controlModel`, `policyRule`, `adaptive`, a feedback-bearing
`planningModel`, or an explicit C.24/C.19/evaluation relation. The block says that
the temporal claim has crossed into control/policy claim-use; it does not make
C.27 an MPC, reinforcement-learning, or policy-evaluation pattern.

Sequential decision and reinforcement-learning practice. Many real rate-change
claims are policy/regime claims, not one-shot effort claims. Policy-transfer
control/policy details live inside `dyn2ControlPolicyRoute?`, not in the default
`Dyn2TemporalClaimAdequacyCard`. When live, the block should recover behavior policy, evaluation policy,
overlap note, uncertainty or bound reference, unsafe-exploration note,
and pattern reference to C.19, C.24, `U.Dynamics`, or the evaluation pattern. This matters for
adaptive rollouts, agentic tool-use, clinical-like treatment regimes, and
repeated operational interventions.

Causal inference. C.27 is not a `C.28` causal-use claim pattern. Effort plus observed rate-change may
carry a planning or diagnostic reading, but a causal attribution needs a separate
`C.28` causal-use relation. When `dyn2CausalUseRoute?` is present, it should name the causal question,
intervention reference, comparator or counterfactual, estimand, time-zero or
assignment window, follow-up window, outcome measure, assumptions, rival causes,
identification strategy or evidence design when available, supported causal use,
and unsupported causal use.

Core rule: C.27 can say a claim is Dyn2 and intervention-sensitive. C.27 cannot
turn that basis into a `C.28`-governed causal-use claim with estimand, identification, realizability, evidence design, and supported-use judgment. Dyn2 can describe an intervention-sensitive
temporal-claim question; it does not estimate causal effect unless `dyn2CausalUseRoute?`
is active and `C.28` causal-use discipline carries the causal question.

Performative prediction, Goodhart, and metric-induced behavior. When a metric
becomes a target, dashboard, incentive, gate, or public comparison, it may
change behavior. C.27 should branch the case instead of becoming a Goodhart
pattern.

`C.27:4 - Solution` defines the `dyn2MetricTargetEffectBlock?` fields; this
section explains why metric publication and target use must be split from
measurement legality, proxy distortion, and residual probe or frame cue.

Content split:
- C.16 carries metric-as-measure;
- E.13, assurance, or governance patterns carry metric-as-target, incentive,
  proxy, utility distortion, or optimization target;
- metric publication as temporal intervention may make C.27 relevant;
- C.26 carries metric/probe changes to the admissible state reading only if residual
  probe, frame, order, or export cue remains after ordinary C.27, C.16, and E.13 pattern relations are
  named.

This keeps Goodhart from becoming a catch-all warning and keeps C.27 focused on
the dynamic effect of metric publication or metric-target use.

Process mining and object-centric process mining. Scalar throughput is often a
thin view. Some dynamic claims need trace topology, multiple object bearers,
interaction notes, and evidence about how queues, tickets, incidents, customers,
orders, services, engineers, deployments, or review windows interact. When this question is live, `C.27:4 - Solution` defines the
`dyn2ObjectCentricTraceBlock?` fields. This section explains why multi-object
trace requirements should be named instead of pretending that one scalar
throughput rate says enough.

Active sensing and active inference. Measurement may be an action rather than a
passive read, but that is still usually ordinary FPF pattern relations: measurement,
state-space, planning, evidence, control, causal, or process-log basis. QL is
not made relevant by typing, discreteness, state reduction, tokenization, or planned
measurement. C.27 may notice dynamic or probe pressure, but it must not promote
active inference, quantum cognition, or QL mathematics unless C.26 remains
relevant after ordinary-pattern exit tests.

Rhythm and embodied dynamics. Load-bearing rhythm claims need bearer, anchor,
window, basis, and admissible use. Coupling, phase relation, entrainment-like
relation, perturbation response, tempo drift, or synchronization evidence are
downstream claim, effect, or use fields only when the claim depends on coordination between bearers.
This preserves the useful dance/practice analogy without minting a rhythm
ontology.

C.27 is a middle recognition-and-relation lens, not a general dynamic-theory
pattern. It notices when a claim has moved from state/rate reading to
intervention-sensitive temporal adequacy, then keeps higher-demand claim relations with
the existing FPF pattern that carries them:

| Claim question noticed by C.27 | Existing FPF pattern relation |
| --- | --- |
| admissible measurement or comparable rate/rate-change reading | `C.16` |
| transition law, reusable dynamics model, prediction, simulation, or control model | `A.3.3 U.Dynamics` plus evidence/assurance patterns |
| actual work/effort trace or resource burn | `U.Work` / `Gamma_work` |
| scale-variable or elasticity claim | `C.18.1` scaling-law lens |
| search policy, exploration/exploitation, premature narrowing, convergence health | `C.19` |
| agentic tool-use planning or tool-call rate-change | `C.24` call-planning discipline |
| task-family learning/adaptation speed or time-to-usable specialization | `C.22.1` task-family adaptation signature |
| viability-envelope temporal regulation | `C.26.3` viability-envelope boundary regulation |
| reproducible dynamic benchmark or faster-improvement comparison | `G.9` |
| causal-use claim or effect estimate | `C.28` and evidence patterns |
| promise, SLA/SLO, gate, public commitment, release claim | promise, boundary, service, and assurance patterns |
| residual probe, frame, export, coarsening, or order-effect cue | `C.26` |

The following lines connect common failures to C.27 action, not to a literature catalog:

| Popular failure | Modern correction | C.27 action |
| --- | --- | --- |
| Past slope is treated as a future control law. | Control/policy claims need horizon, update rule, constraints, and evidence/model relation. | If local, make a `Dyn2TemporalClaimAdequacyCard`; if reusable/control-bearing, include `dyn2ControlPolicyRoute?` and cite `U.Dynamics`, C.16, and assurance patterns as the patterns governing the other question. |
| Data from one policy/regime is used to justify another. | OPE/RL practice asks behavior policy, evaluation policy, policy-overlap, uncertainty, and unsafe-exploration risk. | Keep ordinary `Dyn2TemporalClaimAdequacyCard` cheap; include `dyn2ControlPolicyRoute?` only when policy transfer is load-bearing. |
| One effort impulse is treated as the whole dynamic regime. | Dynamic-treatment/regime practice treats some interventions as sequences of decision rules. | Record policy/regime only in active block; do not make every Dyn2 a policy model. |
| Rate changed after effort, so effort caused it. | Causal inference needs contrast/counterfactual, estimand, timing, outcome, assumptions, rival causes, and design. | Mark planning/diagnostic posture or include `dyn2CausalUseRoute?`; `C.28` causal-use discipline carries the causal-use claim. |
| Metric improves after publication, so process improved. | Performative or Goodhart cases split measurement, target use, incentive use, proxy distortion, temporal intervention, and residual probe, frame, or export effects. | Include `dyn2MetricTargetEffectBlock?` only for temporal intervention and supported-use change; C.16 carries measurement, E.13 or an assurance pattern carries proxy distortion, and C.26 carries residual probe, frame, or export cue. |
| Scalar throughput is read as whole work-cycle truth. | OCPM/process mining separates object bearers, event traces, interactions, and aggregation. | Include `dyn2ObjectCentricTraceBlock?` / `dyn2CrossScaleTransferBlock?` only when scalar rate is insufficient. |
| Measurement-as-action triggers QL too early. | Active sensing may matter, but ordinary FPF pattern relations come first. | Keep C.27 ordinary; treat QL as C.26 content only after ordinary-pattern exits. |
| Rhythm is decorative cadence/vibe. | Rhythm work needs bearer, anchor, window, basis/proxy, and admissible use; coupling belongs only in downstream claim, effect, or use fields. | Use `Dyn2TemporalClaimAdequacyCard`; include coupling, phase, or entrainment only when the claim depends on cross-bearer relation. |


### C.27:12 - Relations

C.27 is the pattern for authored temporal-claim adequacy. It asks whether a
claim about speed, rhythm, throughput, recovery, convergence, rollout, adoption,
braking, coasting, redirection, or stabilization is sufficiently supported for the use
being made of it. It does not become the pattern for the described system, work,
measurement, benchmark, promise, quality bundle, or formal dynamics model.

When a temporal claim also touches another FPF concern, use the FPF pattern that
governs that concern and let C.27 state only the temporal-claim adequacy question.

| Related FPF pattern or discipline | Use C.27 for | Keep in that pattern or discipline |

| --- | --- | --- |
| C.27 itself | First-use entry and exit rule; Dyn0, Dyn1, and Dyn2 distinction; least-demand admissible output sequence; `Dyn2TemporalClaimAdequacyCard`; `Dyn2TemporalClaimProfile` for boundary-crossing claim use; anti-patterns; refresh and reopen triggers. | Nothing outside C.27 is needed when the claim remains only a local temporal-claim adequacy question. |
| `C.16` | Naming the rate, rate-change, rhythm, recovery, or intervention-effect requirement that the measure is being asked to carry. | Measurement construction, evidence, comparability, units, sampling windows, and admissible metric use. |
| `C.26` | Keeping ordinary dynamics, measurement, work-effort, rhythm, braking, coasting, and intervention-timing questions outside QL before any residual QL cue is considered. | Residual probe, frame, order, export, or coarsening cue after ordinary C.27, C.16, work, benchmark, and proxy pattern relations. |
| `A.3.3 U.Dynamics` | Deciding that an authored temporal claim is being used with enough commitment to need a reusable transition-law, simulation, prediction, formal model, or calibrated control relation. | State space, transition law, observation/model constraints, validity discipline, simulation, prediction, and calibrated control model semantics. |
| `A.19` and `C.16` together | Showing that derivative-like wording needs base characteristic, scale/unit, time base or sampling window, construction method, evidence, and admissible use. | Characteristic-space legality and measurement construction. C.27 does not create a parallel coordinate system. |
| `B.1.4` and `B.1.6` | Preventing temporal slices, phase names, work logs, resource burn, or effort traces from being read as acceleration or transition laws. | Temporal-slice composition, phase composition, work/resource aggregation, and actual work evidence. |
| `B.1.5` and `B.2.4` | Naming the temporal-claim adequacy question only when method composition, work enactment, adaptive work cycle, or capability-emergence prose also claims faster/slower improvement, recovery, stabilization, braking, or rhythm change. | Order-sensitive method composition, work enactment, adaptive work cycle, and meta-functional transition. C.27 does not become a method-composition or emergence pattern. |
| `A.4` / `B.4` / `A.16` / `B.4.1` | Naming a temporal-claim adequacy question inside state-change, evolution-loop, cue-stabilization, reopen, operationalize, retire, or language-state movement prose. | Temporal duality, canonical evolution loops, language-state move legality, and observe-notice-stabilize relation discipline. C.27 does not become a lifecycle or language-state movement pattern. |
| `C.24` | Tool-use plans whose tool-call sequence is claimed to change debugging speed, repair rate, learning rate, candidate discovery, evidence confirmation, bug localization, rollout stabilization, or uncertainty reduction. | Call planning, tool-use sequence, and work trace. More calls or more context are not dynamic improvement by themselves. |
| `C.17` and `C.18` | Naming the temporal-claim adequacy question only when a creativity, novelty, open-ended search, archive-growth, illumination, or candidate-generation claim also claims faster/slower improvement, coverage, discovery, or convergence. | Creativity characteristics, novelty/value measurement, NQD generation/update/illumination/select-front calculus, archive semantics, and provenance pins. |
| `C.19` | Convergence, narrowing, widening, exploration, exploitation, or search-speed question when that temporal reading changes supported use. | Pool-policy result and explore/exploit governance. |
| `C.18.1` | A scale-variable change used as the basis for rate-change, learning, recovery, throughput, or stabilization. | Scale variables, scale windows, scale probes, elasticity posture, and scaling-law adequacy. |
| `C.22.1` | Learning or adaptation-rate question for a declared `TaskFamilyRef` or `TaskSignature`. | Task-family adaptation signature, threshold target, prior exposure, transfer, retention, and corridor-entry evidence. |
| `C.26.3` | Braking, throttling, cadence change, recovery timing, adaptation cost, or stabilization as a temporal move inside a viability-envelope claim. | Viability bearer, protected promise/function, viable region, disturbance, sensor/probe/action split, adaptation cost, and failure mode. |
| `E.13` | Naming when a temporal metric, proxy, or dashboard trend is being treated as practical value or target. | Pragmatic utility, value alignment, proxy audit, and Goodhart repair. C.27 does not decide value adequacy. |
| `E.16` | Naming the temporal-claim adequacy question when autonomy budgets, guard cadence, ledger evidence, depletion, override, or freedom-of-action language is used as the basis for acceleration, braking, recovery, or stabilization. | Autonomy budget declaration, guard checks, autonomy ledger, depletion behavior, pause/resume speech acts, and scale policy under autonomy. |
| `A.10` / `B.3` / `B.3.4` / `G.6` | Naming which temporal reading needs an evidence basis, provenance path, assurance posture, freshness window, decay note, or reopen condition. | Evidence graph referring, evidence carriers, provenance anchors, assurance posture, evidence decay / epistemic debt, and citable path/slice discipline. |
| `G.9` | Dynamic benchmark requirement: rate-change, rhythm change, recovery speed, intervention effect, effort budget, or dynamic outcome. | Baseline, freshness, comparator, bridge discipline, parity plan, parity report, and reproducible benchmark publication. |
| `C.25` | Dynamic quality-family slot when agility, resilience, adaptability, recovery, or robustness depends on braking, redirection, stabilization, recovery rate, or rhythm under effort. | Quality-family bundle structure, scope, measures, mechanisms, evidence, and endpoint discipline. |
| `G.5` | Only the selector-publication case where a selector report consumes a dynamic benchmark result. | Method-family registry use and selector publication. C.27 does not add a default G.5 object. |
| `A.2.3` / `A.2.8` / `A.2.9` / `A.6.C` / `F.12` and assurance patterns | Promise-like or boundary-facing temporal claims: release speed, recovery guarantee, SLA/SLO-like cadence, public commitment, gate, service acceptance, or assurance use. | Promise content, commitments, instituting speech acts, contract unpacking, service acceptance binding, assurance posture, and release/gate evidence. |
| `E.18 E.TGA` / `A.20` / `A.21` | Naming the C.27 temporal-claim adequacy question when a flow, gate, crossing, `PathSlice`, `LaunchGate`, or published decision uses that temporal claim. | The TGA carcass: `U.Transfer`, `OperationalGate(profile)`, GateCheck publication shape, `ConstraintValidity`, `GateFit`, `DecisionLog`, `PathSlice`/sentinel refresh, `Gamma_time` pins, `SquareLaw`, and crossing visibility. |
| `C.21` / `G.10` or `G.11` / `G.12` | Naming the temporal claim when a discipline-health value, shipped pack, dashboard time-series, telemetry pin, RSCR trigger, refresh plan, refresh report, or dashboard slice is read as evidence for improvement, decay, recovery, stabilization, or rate-change. | Discipline-health slot meaning, SoTA pack shipping, DHC series/row/slice construction, telemetry-pin publication, refresh/decay orchestration, and RSCR trigger discipline. |
| `C.28` | A rate-change, intervention, effort, workshop, policy, or practice change is used as a causal-use basis. | Causal-use question, `C.28` causal-use class, causal intervention spec, contrast/counterfactual, estimand, timing, outcome, assumptions, rival causes, identification strategy, realizability posture, evidence design, supported causal use, and unsupported causal use. |

Use pattern references before expanding a C.27 record. When measurement,
transition law, work evidence, planning, benchmark parity, `C.28` causal-use
claim, promise content, assurance posture, quality, viability, or residual QL
discipline governs the other question, the C.27 record cites that pattern and
keeps only the temporal-claim adequacy question.

When a temporal claim touches neighbouring work, keep these boundaries:


1. Fields in a C.27 card do not imply new Kernel kinds.
2. State space, measurement, transition law, work, planning, benchmark,
   causality, promise, service, quality-bundle, publication, and QL questions
   stay with the FPF pattern that governs each question.
3. The described entity, temporal bearer, profile content, and profile carrier
   remain distinct.
4. If the text says process, work cycle, practice, service, method, system, or
   rhythm, the real bearer is named through a named FPF kind and reference rather than
   treated as one generic moving thing.
5. Derivative-like readings remain C.16-compliant.
6. Full `Dyn2TemporalClaimProfile`s remain rare and justified rather than default.
7. At least one golden case exits or downgrades from Dyn2 correctly.
8. Braking, pause, stabilization, redirection, and coasting are first-class
   temporal moves rather than failures to accelerate.
9. QL relevance stays inactive unless ordinary pattern relations leave residual
   probe, frame, export, or coarsening cue.
10. Causal, benchmark, promise-like, and assurance claims cite the governing
    pattern relation that carries the claim rather than relying on an ordinary `Dyn2TemporalClaimAdequacyCard`.

At use time, the concrete relation is enough: name the temporal-claim adequacy
question, name the pattern that governs the other question, state the
unsupported downstream claim, effect, or use, and choose the minimal C.27 output or the pattern relation that carries the other claim.

This informative matrix states the neighbouring-question boundaries. Ordinary
C.27 use does not fill it as a separate form.


| Existing FPF discipline / dynamic collision theme | C.27 relation | Collision risk | Boundary |
| --- | --- | --- | --- |
| A.7 strict distinction | C.27 records are authored descriptions of temporal-claim adequacy. | Card/profile content is confused with the described entity, work, dynamics law, or carrier. | Keep described entity, temporal-claim description, and carrier distinct in C.27 and in any neighboring C.27 relation text. |
| E.10 / F.5 / F.8 naming discipline | C.27 uses local labels and Plain/Tech mapping. | Dyn2, rhythm, force, inertia, speed, or acceleration become new FPF kinds. | Use pattern-local dynamic-claim labels; introduce no new `U.*` kind and no pattern-number-prefixed term. |
| A.3.3 `U.Dynamics` | C.27 types the authored temporal-claim adequacy question before a formal-model relation is needed. | C.27 steals transition law, simulation, prediction, or reusable control model work. | Keep formal laws, simulations, predictions, and calibrated control models with `U.Dynamics` and evidence/assurance patterns. |
| A.19 `CharacteristicSpace` | C.27 may point to base characteristic, state reading, rate reading, or rate-change reading. | C.27 informally creates derivative coordinates or spaces. | Use A.19 and C.16 for characteristic-space and measure construction when the reading is load-bearing. |
| C.16 MM-CHR | C.27 cites measures, rate readings, rate-change readings, and evidence. | C.27 invents measurement legality or comparability. | C.16 carries measurement construction; C.27 only names the temporal-claim question and cites the measurement relation. |
| A.15 / `U.Work` / WorkPlan / MethodDescription | C.27 relates effort timing, intervention, resource envelope, and work trace to a temporal claim. | C.27 stores actual work, assigns plan authority, or treats planned effort as performed work. | Planning/method description carries planned effort; work evidence carries actuals; C.27 records only the temporal-claim adequacy question. |
| B.1.5 / B.2.4 | C.27 can type the temporal adequacy question when method-composition or capability-emergence prose also claims rate, rhythm, recovery, stabilization, braking, or redirection. | C.27 becomes a method-composition, work-enactment, or emergence pattern. | B.1.5 carries order-sensitive method composition and work enactment; B.2.4 carries meta-functional transition. |
| A.4 / B.4 / A.16 / B.4.1 | C.27 can type the temporal adequacy question inside state-change, evolution-loop, cue-stabilization, reopen, operationalize, retire, or language-state movement prose. | C.27 becomes a state-change, evolution-loop, language-state movement, or cue-stabilization pattern. | Those patterns carry state-change or evolution-loop and language-state movement; C.27 only states the temporal claim and its `supportedUse` and `unsupportedUse` fields. |
| C.18.1 | C.27 can type temporal-claim question when a scale-variable change is used as the basis for rate-change, learning, recovery, throughput, or stabilization. | C.27 becomes a scaling-law or elasticity pattern. | C.18.1 carries scale variables, scale windows, scale probes, and elasticity posture; C.27 only states temporal-claim adequacy. |
| C.17 / C.18 | C.27 can type the temporal adequacy question inside creativity, novelty, open-ended search, archive-growth, illumination, or candidate-generation prose. | C.27 becomes a creativity, novelty, or NQD-calculus pattern. | C.17 carries creativity characteristics and novelty/value measurement; C.18 carries NQD generation, archive, illumination, and selection calculus. |
| C.19 | C.27 can type convergence, narrowing, exploration, exploitation, or search-speed question. | C.27 becomes a pool-policy result pattern. | C.19 carries pool-policy result; C.27 only states temporal-claim question when speed or change affects admissible use. |
| C.24 | C.27 can flag tool-use acceleration, repair-rate, learning-rate, or stabilization claims. | C.24 is asked to carry C.27 fields whenever tool-use prose mentions speed. | Use a C.27 card/profile reference first; add local C.24 fields only if repeated concrete cases show that C.24 itself must inspect the temporal-claim question. |
| C.22.1 | C.27 can type learning/adaptation-rate question for one declared `TaskFamilyRef` or `TaskSignature`. | C.27 becomes a generic learning-speed or specialization pattern. | C.22.1 carries the task-family adaptation signature; C.27 only states the temporal-claim question when it changes supported use. |
| C.26.3 | C.27 can type braking, throttling, cadence, recovery, or stabilization claim inside a viability-envelope claim. | C.27 becomes a viability-envelope or stability-through-change pattern. | C.26.3 carries the viability-envelope record; C.27 only states the temporal move and pattern relation. |
| E.13 | C.27 can flag a temporal metric, proxy, dashboard trend, or target-effect reading. | C.27 becomes value-alignment or proxy-audit law. | E.13 carries pragmatic utility, value alignment, and proxy audit; C.27 only states the temporal claim. |
| E.16 | C.27 can flag temporal adequacy inside autonomy-budget, guard-cadence, depletion, pause/resume, or freedom-of-action language. | C.27 becomes autonomy governance or guard-budget law. | E.16 carries autonomy budget declarations, guard checks, autonomy ledger, depletion behavior, and override speech acts. |
| G.9 | C.27 can flag dynamic benchmark parity requirement. | C.27 becomes the benchmark parity harness. | G.9 carries baseline, freshness, comparator, bridge, parity plan, and parity report discipline; C.27 names only the dynamic claim question. |
| A.10 / B.3 / B.3.4 / G.6 | C.27 can name evidence basis, provenance path, freshness/decay posture, and reopen condition for a temporal claim. | C.27 becomes evidence graph, assurance, decay, or provenance law. | A.10, B.3, B.3.4, and G.6 carry those evidence/provenance/assurance questions; C.27 only names the temporal reading that needs them. |
| C.21 / G.10 / G.11 / G.12 | C.27 can flag the temporal claim inside discipline-health values, pack shipping, dashboard telemetry, refresh triggers, RSCR inputs, or dashboard slices. | C.27 becomes discipline-health characterization, SoTA pack shipping, dashboard, or refresh orchestration. | C.21 carries discipline-health slot meaning; G.10 carries pack shipping; G.12 carries dashboard time-series and telemetry-pin publication; G.11 carries refresh/decay orchestration. |
| C.26 | C.27 carries ordinary temporal adequacy before QL is considered. | Dyn2 vocabulary escalates into quantum-like modeling. | C.26 applies only for residual probe, frame, order, export, or coarsening cue after ordinary C.27, C.16, work, benchmark, and proxy pattern relations. |
| A.2.3 / A.2.8 / A.2.9 / A.6.C / F.12 and assurance patterns | C.27 may flag promise-like, boundary-facing, or service-acceptance temporal claims. | C.27 becomes an SLA, commitment, instituting speech-act, boundary-semantics, service-acceptance, or assurance pattern. | Those patterns carry promise content, commitment, speech act, contract unpacking, service acceptance, and assurance; C.27 only states the temporal claim and its `supportedUse` and `unsupportedUse` fields. |

Core discipline: C.27 does not name new objects in the world. It names when an
authored temporal claim has started to need intervention-sensitive temporal
adequacy, then keeps each higher-demand claim relation with the FPF pattern that already
governs that concern.


Practitioner-readable problem:

> A trend is not yet an intervention model. Use C.27 when a claim about speed,
> rhythm, throughput, recovery, convergence, rollout, or adoption is used to
> change action and therefore needs effort, window, resistance, basis, and
> reopen discipline.

One-minute working script:

> When a text says something should get faster, slower, recover, stabilize, or
> keep rhythm, first ask: are we only reading a state, only reading a rate, or
> claiming that an intervention changes the rate, rhythm, recovery, or
> stabilization? If it is only state or rate, stop. If it is an intervention
> claim, write the smallest `Dyn2TemporalClaimAdequacyCard`: what changes, by
> what effort, in what window, against what resistance or cost, on what basis,
> for what admissible use, and what downstream claim, effect, or use is not carried by the temporal-claim record. Only boundary-crossing
> claims need a `Dyn2TemporalClaimProfile`. Formal laws, measurements, work,
> `C.28` causal-use claim, benchmarks, promises, assurance, viability envelopes,
> scale-variable claims, adaptation signatures, and QL residues stay with the
> existing FPF patterns that govern those concerns.

C.27 also carries an early non-improvement boundary:

> C.27 is not a temporal theory of everything.
> It is the smallest useful repair for one recurring authored-claim failure:
> rate talk pretending to know rate-change.

C.27 does not present itself as improving all temporal reasoning, all
process modeling, all practice description, all rhythm theory, all
control/RL/causal inference, all performance management, all QL or
active-inference modeling, all scaling claims, or all adaptation claims. It
improves one narrow working failure: it prevents state/rate readings from being
laundered into intervention-sensitive temporal claims without effort, window,
resistance, basis, and `supportedUse` and `unsupportedUse` field discipline.

The first C.27 record should be the one-screen `Dyn2TemporalClaimAdequacyCard`, not a full `Dyn2TemporalClaimProfile`.
The `Dyn2TemporalClaimProfile` is a boundary-crossing claim-use C.27 record. Existing formal patterns carry formal models; a C.27 record cites them when the other question is live instead of copying C.27 theory into another pattern relation.


The durable bottom line is:

> C.27 improves FPF only if it improves first-practical entry and pattern relation:
> it notices state/rate-to-rate-change laundering, produces the least-committing admissible
> next output, and keeps every higher-demand claim relation with the existing FPF pattern
> that governs that concern.

It should help FPF users act more carefully with speed, rhythm, effort,
inertia, braking, coasting, and redirection claims. It does not make FPF carry
mathematical theater, physics ontology, false QL relevance, or a hidden
compliance backpack.
### C.27:12a - C.29 MLA relation

> `C.29` may state that a mathematical lens supports a prediction, distinction, obstruction, diagnostic boundary, or validation posture. If the claim-bearing text is about forecast, rate, trajectory, rhythm, recovery, convergence, stabilization, speed, temporal window, or rate-change as sufficient for a use, `C.27` supplies the temporal-claim adequacy record or states that the temporal concern is not live. Formal transition-law, prediction, or control-model semantics stay with `A.3.3` plus evidence and assurance loci where those uses are live.

### C.27:End
## C.28 - CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability

> **Type:** Calculus (C)
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Causal-use calculus.

**Intent.** Govern live causal questions and decision-bearing causal use: improvement, intervention effect, causal fairness, counterfactual comparison, causal policy optimality, realized counterfactual-rung evidence, identified counterfactual estimate, or simulation-only counterfactual output.

**Governed object.** A causal-use question or claim together with the support basis and follow-on records needed to use it admissibly: causality-ladder rung, estimand or contrast, evidence support basis, identification posture, counterfactual sampling realizability posture, supported use, unsupported use, and next move.

**Not a physical ontology.** `C.28` governs how FPF authors, reviewers, and operators use causal models, evidence, and counterfactual reasoning in records, policy claims, fairness claims, method comparisons, and work plans. It does not define physical causality in general and does not replace local domain science.


### C.28:0 - Use This When

Use `C.28` when a claim is being used causally:

- "method A improves result";
- "users who received intervention X had better outcomes";
- "this practice is fair";
- "the agent chose optimally";
- "the model simulates what would have happened";
- "the system can collect counterfactual data";
- "this benchmark shows a causal method is better";
- "this policy should be deployed because it would have changed the outcome".

Use `C.28` especially when the claim must distinguish:

- observed association;
- intervention or action effect;
- counterfactual comparison;
- direct counterfactual-rung data collection;
- identified counterfactual estimate;
- simulation-only counterfactual output;
- causal policy class;
- causal fairness use;
- causality-ladder parity in method comparison.

**Not this pattern when.** If no causal use is claimed, keep the work in the neighboring pattern: `C.16` for measurement, `C.27` for temporal trend or rate-change adequacy, `B.3` for assurance posture, `A.10` for evidence graph reference, `G.9` for ordinary parity, `C.11` for local choice, `C.19` for pool policy, `C.24` for call planning, or `C.26` for a surviving quantum-like modeling cue after ordinary causal explanations have been tried.

**Activation boundary.** `C.28` activates at `CausalUseActivation`: causal wording changes what the claim makes admissible for publication, choice, deployment, assurance, audit, benchmark, or support treatment. The trigger is admissible downstream use, not the presence of a causal-looking word. If the wording is only exploratory prose and no causal use governed by `C.28` is made, rewrite to association, trend, measurement, or simulation-only wording and stop.

Exploratory causal-looking prose is not a `CausalUseActivation` by itself. A note may say that a relation is plausible, worth probing, or suggested by traces and still remain in `C.16`, `C.27`, `A.10`, `C.11`, `C.19`, `C.24`, `G.5`, or `G.9` until the text makes a causal use governed by `C.28` admissible. The moment the text makes publication, choice, deployment, assurance, audit, benchmark, or support treatment depend on causal support, `C.28` governs the causal-use boundary.

#### C.28:0.1 - What Goes Wrong If Missed

A causal-looking phrase backed only by association, proxy, simulation-only, or rhetorical support gets promoted into a causal use that requires a named `C.28` support basis and verdict.

Correlation becomes intervention effect. Interventional proxy becomes counterfactual fairness. A simulation becomes realized counterfactual-rung evidence. A benchmark compares methods across different causality-ladder rungs and still publishes one scalar superiority claim. An agentic policy is called optimal without saying whether it is a natural behavior policy, an interventional policy, or a counterfactual policy.

The practical error is laundering: the reader sees causal language but cannot recover what rung, estimand, evidence basis, and supported use are actually admissible.

#### C.28:0.2 - What This Buys

`C.28` gives FPF one cheap first stop for causal use.

The first useful result is not a heavy record. It is one small causal-use triage that says whether causal use is present, which causality-ladder rung is being used, what comparator or counterfactual is in play, what evidence posture supports it, and what the next move is.

Durable cards and profiles appear only when the claim needs them. The pattern buys explicit causal discipline without turning every causal word into a paperwork exercise.

#### C.28:0.3 - First-Minute Questions

`C.28` in 60 seconds is the operational entry into `CausalUseTriageRecord`:

1. Detect whether the claim reaches `CausalUseActivation`: it changes what publication, choice, deployment, assurance, audit, benchmark, or support treatment is admissible.
2. Stop with `nextMove.cheapStop` if the claim only reports association, trend, description, measurement, or simulation-only output.
3. If causal use is live, fill `targetCausalityLadderRung`, `comparatorOrCounterfactualRef`, and `evidencePosture`.
4. Fill `supportedUse: CausalUseSupportStatement` and `unsupportedUse: CausalUseUnsupportedStatement` as one action pair.
5. Fill `nextMove: CausalUseNextMove`: choose `cheapStop` or escalate only when the claim is decision-bearing, publication-bearing, assurance-bearing, fairness-bearing, benchmark-bearing, or reusable.

#### C.28:0.4 - First Output

The first output is a `CausalUseTriageRecord`:

```text
CausalUseTriageRecord:
  causalUse: yes | no | unclear
  targetCausalityLadderRung?: CausalityLadderRung
  comparatorOrCounterfactualRef?
  evidencePosture: CausalEvidencePostureTriageValue
  supportedUse?: CausalUseSupportStatement
  unsupportedUse?: CausalUseUnsupportedStatement
  nextMove: CausalUseNextMove
```

```text
CausalUseNextMove:
  cheapStop:
    stopNoCausalUse |
    publishAssociationOnly |
    rewriteAsTrendOrAssociation |
    keepSimulationOnlyModelUse |
    downgradeCausalWording |
    abstainFromCausalUse |
    rerouteToNeighborPattern
  escalateOnlyIfLoadBearing:
    openLocalCausalUseQuestionCard |
    openDurableCausalUseQuestionCard |
    buildCausalIdentificationProfile |
    buildCounterfactualSamplingRealizabilityProfile |
    planCausalUseEvidenceDesign |
    openCausalFairnessUseAuditCard |
    openCausalMethodRungParityRecord
```

```text
CausalEvidencePostureTriageValue =
  observationalAssociationSupportBasis |
  interventionalActionSupportBasis |
  realizedCounterfactualSampleSupportBasis |
  identifiedCounterfactualEstimateSupportBasis |
  simulationOnlyCounterfactualOutputBasis |
  missing
```

`cheapStop` values are terminal or downgrade actions. They close the local causal-use question for now by saying what narrower use remains admissible, which neighboring pattern governs the remaining non-causal question, or that causal use is declined. `escalateOnlyIfLoadBearing` values are record-opening actions. They are admissible only when the supported-use and unsupported-use boundary cannot safely carry the reader's next action by itself.


If this first output cannot be written honestly, the causal-use claim is not ready.

`CausalUseSupportStatement` is one concrete causal-use action the current support makes admissible, such as publish association-only wording, use a bounded interventional estimate for a named decision, deploy only under a named policy constraint, run a fairness audit under a named causal estimand, or compare methods only inside one declared causality-ladder rung. It is not a confidence label, graph name, method name, or generic "evidence exists" phrase.

`CausalUseUnsupportedStatement` is the matching concrete causal-use action the current support does not make admissible, such as intervention-effect wording, realized counterfactual sample wording, causal fairness certification, causal policy optimality, cross-rung benchmark superiority, or release/deployment use. The supported and unsupported statements travel as a pair so the reader can act without inferring the boundary from prose tone.

The triage record may be the final causal-use carrier. Triage lines are enough when they block the overclaim and tell the reader what narrower use remains admissible. Do not open a local card merely because the word "cause", "effect", or "counterfactual" appears.

The triage `evidencePosture` field is the first-pass alias for `CausalEvidenceSupportBasis | missing`. If a claim escalates beyond triage, the value must dock to `CausalEvidenceSupportBasis`; `missing` becomes `unsupportedUse`, `CausalUseSupportVerdict = unsupported`, or `abstain`.

### C.28:1 - Problem Frame

FPF already has dedicated neighboring patterns for measurement, evidence, assurance, temporal claims, decisions, exploration, call planning, fairness, method dispatch, parity, and quantum-like modeling. None of those neighbors should become the general authority for causal use.

`C.28` exists because causal use cuts across those neighbors. The same sentence can be:

- a measurement description handled by `C.16`;
- a temporal trend handled by `C.27`;
- an assurance claim handled by `B.3`;
- an evidence graph reference handled by `A.10`;
- a decision record handled by `C.11`;
- a pool-policy record handled by `C.19`;
- a call-planning record handled by `C.24`;
- a fairness audit handled by `D.5`;
- a parity report handled by `G.9`;
- a quantum-like residual handled by `C.26`;
- or a causal-use claim governed here.

The first pattern task is therefore not to classify wording for its own sake. It is to recover the live causal question, the target causality-ladder rung, the support basis currently available, and the cheapest truthful next move. Sometimes that move is to downgrade the claim to association, temporal change, metric-only fairness, or simulation-only use. Sometimes it is to open identification, realizability, evidence-design, fairness, policy-evaluation, or benchmark-parity work. `C.28` exists to keep those moves distinct and to stop teams from acting as if an identification, realizability, or intervention-support basis had already been earned.


### C.28:2 - Problem

Causal language is easy to overclaim because ordinary prose hides the difference between association, action, counterfactual comparison, realized counterfactual sample, identified estimate, and simulation.

Three collapses are especially dangerous:

1. **Rung collapse.** Observational association, interventional action/effect, and counterfactual comparison are treated as one causality-ladder rung.
2. **Support collapse.** Observed data, experimental data, direct counterfactual-rung samples, identified estimates, and simulations are treated as one evidence basis.
3. **Use collapse.** A result that supports one use, such as association reporting, is reused for another use, such as causal fairness, policy optimality, or method superiority.

`C.28` prevents those collapses by making rung, support, and use explicit before claims requiring higher causal support are admitted.

### C.28:3 - Forces

| Force | Tension |
| --- | --- |
| Causal safety vs cognitive affordability | FPF must block causal laundering without forcing every causal word into a full causal dossier. |
| Rung clarity vs ordinary language | Ordinary language says "improves", "causes", "fair", or "would have"; FPF must recover whether that means association, intervention, or counterfactual comparison. |
| Identification vs realizability | A counterfactual estimand may be identifiable from other data but not directly sampleable, or directly sampleable under action constraints but not generally available. |
| Graph/formalism precision vs reader usability | SCM, DAG, ADMG, SWIG, SCM twin network, AMWN, and counterfactual graphical model names matter, but they must not bury the first practical move. |
| Domain plurality vs one FPF pattern | SCM/PCH, potential outcomes, target-trial emulation, causal ML, transportability, causal representation learning, causal RL, and causal fairness must all remain recognizable without making `C.28` a one-school vocabulary. |
| Neighbor fit vs authority creep | Neighbor patterns need causal-use hooks, but they must not redefine causal-use question, rung, estimand, identification, or realizability. |

### C.28:4 - Solution

Use a three-level causal-use escalation:

1. Start with `CausalUseTriageRecord`.
2. Escalate to `LocalCausalUseQuestionCard` or `DurableCausalUseQuestionCard` only when the claimed use needs a reusable causal-use record.
3. Add profiles or specialized records only when the claim triggers that exact need: identification, realizability, evidence design, fairness, policy evaluation, transportability, estimation validity, causal-variable representation, or parity.


The default move is cheap. The heavy move is triggered.

| Record or profile kind | Ordinary size | Trigger |
| --- | --- | --- |
| `CausalUseTriageRecord` | one short record; usually `5-8` lines covering activation, rung, comparator/counterfactual, evidence posture, supported use and unsupported use pair, and next move | any live causal wording or suspected causal laundering |
| `LocalCausalUseQuestionCard` | one small card; usually one causal-use question, one rung, optional comparator/estimand, one support basis, one supported use and unsupported use pair, and one next move | the team needs a reusable local record but not a publication/release/fairness/benchmark/assurance object |
| `DurableCausalUseQuestionCard` | one durable card with causal-use kind, estimand, timing/outcome when needed, assumptions, rival causes, support basis, supported use and unsupported use pair, next move, and reopen/exit condition | the claim is decision-bearing, publication-bearing, fairness-bearing, benchmark-bearing, assurance-bearing, or reusable |
| heavy profile or specialized record | only the fields needed for the named triggered question or work item; absent fields remain absent rather than becoming implied dossier requirements | identification, realizability, target-trial emulation, parameter estimation, transportability, off-policy evaluation, causal representation, evidence design, fairness audit, or causal parity is materially needed |


#### C.28:4.0 - Causal-use governance and consumer carry-through boundary

`C.28` governs causal-use objects and causal-use support roles. Neighbor patterns keep their local authority and consume only the causal-use pieces they need: measurement, evidence path, assurance, fairness, decision, exploration, call-planning, dispatch, parity, and refresh records do not become causal-use governing patterns by carrying `C.28` fields.

| Object or decision | `C.28` governs | Neighbor may carry | Neighbor must not do |
| --- | --- | --- | --- |
| Causal-use kind and rung | `CausalUseClaimKind`, `CausalityLadderRung`, causal-use question, comparator/counterfactual, estimand, supported use, unsupported use | `causalUseSpec?`, `causalActionUseSpec?`, method dispatch spec, parity record, fairness audit card | Infer causal-use kind from local vocabulary alone or publish a higher `CausalityLadderRung` without C.28 support |
| Causal evidence support basis | `CausalEvidenceSupportBasis` and its five values | Evidence path refs in `A.10`, evidence-role specializations in `A.2.4`, consumer fields in `B.3`, `C.19`, `D.5`, `G.5`, and `G.9` | Mint another support-basis value set, add assumption-only/no-support values, or let simulation-only output become realized evidence by name |
| Identification and realizability | `CausalIdentificationProfile`, `CounterfactualSamplingRealizabilityProfile`, their verdicts, and supported use and unsupported use | Evidence, assurance, decision, exploration, call-planning, fairness, dispatch, and parity refs to those profiles | Treat identification as direct sampling, or treat direct-sampling infeasibility as absence of all possible causal support |
| Graph and calculus naming | `CausalGraphRepresentationKind`, `GraphSeparationCriterionKind`, `CausalInferenceCalculusKind`, `StructuralCausalModel`, `CausalDiagramRef` | Named graph refs and calculus refs when the neighbor records the causal-use support basis and cited formalism | Use generic graph prose where a graph formalism or calculus is load-bearing |
| Assurance consequence | `CausalUseSupportVerdict` as causal-use action grammar | `B.3` degrade/block/abstain consequences for `F-G-R/CL` assurance | Let assurance prose certify causal identification, realizability, or fairness |
| Fairness, policy, and parity specialization | Causal-use question/rung/estimand/support basis/support verdict for fairness, policy, and causal method comparison | `D.5` ethical/fairness audit card, `C.11` choice result, `C.19` pool policy, `C.24` call plan, `G.5` method dispatch spec, `G.9` parity report with local refs to consumed `C.28` support | Collapse metric disparity, policy replay, method dispatch, or benchmark score into a causal-use verdict |

A neighbor may quote the `C.28` values it consumes for by-value readability. Quoting the values does not transfer governing authority. A neighbor pattern governs only its local record and must cite `C.28` when the causal-use question or causal-support basis is live.


Compact crosswalk:

| Field or decision slot | Question answered | Typical values | Do not confuse with |
| --- | --- | --- | --- |
| `CausalityLadderRung` | What kind of causal question or use is being claimed? | observational association, interventional action, counterfactual comparison | the evidence source or the method family |
| `CausalEvidenceSupportBasis` | What support posture is being used for that causal use? | observational association, interventional action, realized counterfactual sample, identified counterfactual estimate, simulation-only output | the rung itself, a raw evidence-role name, or a no-support verdict |
| `supportedUse` / `unsupportedUse` | What may the reader do next, and what must they not do? | `CausalUseSupportStatement`, `CausalUseUnsupportedStatement` | a confidence score, a graph name, a method name, or a neighboring governing pattern |

Rung-support-use examples:

| Rung | Support basis | Supported use | Unsupported use |
| --- | --- | --- | --- |
| `observationalAssociationRung` | `observationalAssociationSupportBasis` | association report, descriptive risk comparison, probe selection | intervention-effect claim, causal fairness certification, policy optimality |
| `interventionalActionRung` | `interventionalActionSupportBasis` | declared action-effect use inside assignment, follow-up, and outcome limits | counterfactual sample claim, cross-population policy claim without transportability |
| `counterfactualComparisonRung` | `identifiedCounterfactualEstimateSupportBasis` | identified or bounded counterfactual estimate under assumptions and profile refs | realized sample wording or assumption-free counterfactual certainty |
| `counterfactualComparisonRung` | `simulationOnlyCounterfactualOutputBasis` | bounded model-supported simulation use | realized counterfactual sample evidence, intervention-effect evidence |

#### C.28:4.1 - Causality-Ladder Rung

`CausalityLadderRung` is a controlled value set:

```text
CausalityLadderRung =
  observationalAssociationRung |
  interventionalActionRung |
  counterfactualComparisonRung
```

- `observationalAssociationRung` means passive observation, natural behavior, association, or seeing-only posture.
- `interventionalActionRung` means `do(x)`, intervention, action setting, experiment, policy change, or action-effect posture.
- `counterfactualComparisonRung` means counter-to-fact comparison, unit-history-conditioned comparison, potential-outcome contrast, or imagining posture.

A higher causal-use rung is not supported by lower-rung data unless a `CausalIdentificationProfile`, `CounterfactualSamplingRealizabilityProfile`, or bounded-use statement says exactly what is supported and what is not.

#### C.28:4.1a - Causal-Use Claim Kind

`CausalUseClaimKind` is the controlled value set for the local causal-use claim being made:

```text
CausalUseClaimKind =
  causalEffectClaim |
  counterfactualComparisonClaim |
  causalFairnessClaim |
  causalPolicyClaim |
  causalBenchmarkParityClaim |
  causalEvidenceSupportClaim |
  causalAssuranceSupportClaim
```

- `causalEffectClaim` means a result is used as an effect, improvement, harm, or intervention/outcome claim.
- `counterfactualComparisonClaim` means a counter-to-fact, potential-outcome, or unit-history-conditioned comparison is being used.
- `causalFairnessClaim` means fairness is claimed through a causal path, intervention, counterfactual, or causal estimand rather than only a metric.
- `causalPolicyClaim` means a policy, action rule, exploration rule, or agentic strategy is claimed as causally preferable.
- `causalBenchmarkParityClaim` means causal methods are compared for parity, superiority, or benchmark consumption.
- `causalEvidenceSupportClaim` means an evidence path is being used as causal-use support.
- `causalAssuranceSupportClaim` means an assurance tuple or support verdict is being used for a causal-use claim.

Simulation-only causal use stays inside the existing claim-kind set. `simulationOnlyCounterfactualOutputBasis` is a support/use posture, not a new `CausalUseClaimKind`. Use the relevant claim kind, usually `counterfactualComparisonClaim`, `causalPolicyClaim`, `causalBenchmarkParityClaim`, or `causalEvidenceSupportClaim`, and set `CausalEvidenceSupportBasis = simulationOnlyCounterfactualOutputBasis` with bounded model-supported use and unsupported use. Bounded model-supported simulation use does not become realized counterfactual sample evidence or intervention-effect evidence. Do not mint a separate simulation-only claim kind merely to avoid naming the support posture.

Encoding rule: choose the causal-use claim kind by the question being answered, then choose `simulationOnlyCounterfactualOutputBasis` as the support basis and write `CausalUseSupportStatement` / `CausalUseUnsupportedStatement` for the bounded simulation use.

#### C.28:4.2 - Causal-Use Cards

Use a local card when the claim needs a small working record:

```text
LocalCausalUseQuestionCard:
  causalUseQuestionRef: U.CausalUseQuestion
  targetCausalityLadderRung: CausalityLadderRung
  causalUseClaimKind?: CausalUseClaimKind
  comparatorOrCounterfactualRef?
  estimandRef?
  causalEvidenceSupportBasis: CausalEvidenceSupportBasis
  supportedUse: CausalUseSupportStatement
  unsupportedUse: CausalUseUnsupportedStatement
  nextMove: CausalUseNextMove
```

Use a durable card when the claim is decision-bearing, publication-bearing, fairness-bearing, benchmark-bearing, assurance-bearing, or reusable:

```text
DurableCausalUseQuestionCard:
  causalUseQuestionRef: U.CausalUseQuestion
  targetCausalityLadderRung: CausalityLadderRung
  causalUseClaimKind: CausalUseClaimKind
  causalInterventionSpecRef?
  comparatorOrCounterfactualRef?
  estimandRef: U.CausalEstimand
  potentialOutcomeContrastRef?
  targetTrialProtocolRef?
  assignmentOrInterventionWindowRef?
  causalFollowUpWindowRef?
  outcomeMeasureRef?
  causalAssumptionSetRef
  rivalCauseSetRef?
  causalEvidenceSupportBasis: CausalEvidenceSupportBasis
  causalIdentificationProfileRef?
  counterfactualSamplingRealizabilityProfileRef?
  causalParameterEstimationProfileRef?
  causalTransportabilityProfileRef?
  causalVariableRepresentationRef?
  falsificationOrNegativeControlRef?
  sensitivityAnalysisRef?
  rivalCauseStressTestRef?
  supportedUse: CausalUseSupportStatement
  unsupportedUse: CausalUseUnsupportedStatement
  nextMove: CausalUseNextMove
  reopenOrExitCondition
```

The durable card is not the default. It is the record used when a causal note without the required `C.28` support basis would be unsafe.

#### C.28:4.3 - Causal Evidence Support Basis

`CausalEvidenceSupportBasis` is a controlled value set:

```text
CausalEvidenceSupportBasis =
  observationalAssociationSupportBasis |
  interventionalActionSupportBasis |
  realizedCounterfactualSampleSupportBasis |
  identifiedCounterfactualEstimateSupportBasis |
  simulationOnlyCounterfactualOutputBasis
```

This is the `C.28`-governed value set for causal evidence support basis. `causalAssumptionOnlySupport` and `noCausalEvidenceSupport` are not values of `CausalEvidenceSupportBasis`: assumption-only posture belongs in `causalAssumptionSetRef` plus supported use and unsupported use; no-support posture belongs in `CausalUseSupportVerdict`, `unsupportedUse`, or `abstain`.

Simulation-only output never becomes realized counterfactual-rung evidence by name alone. It may support model-based use only when assumptions, validation, and supported use and unsupported use are declared.

`realizedCounterfactualSampleSupportBasis` does not mean observing two incompatible outcomes for the same unit in one realized world. It means physically obtaining samples from the declared target counterfactual distribution under the profile's constraints.

`CausalEvidenceSupportBasis` names a support posture. It is distinct from an evidence source, an `A.2.4` evidence role, and an `A.10` evidence path. Some support bases are direct empirical postures, such as observational or interventional support. Other support bases are inferential postures, such as identified counterfactual estimate support. Do not read this value set as only a raw evidence-source kind.

`realizedCounterfactualSampleSupportBasis` does not mean observing two incompatible outcomes for the same unit in one realized world. It means physically obtaining samples from the declared target counterfactual distribution under the profile's physical, ethical, operational, unit-history, and graph constraints.

#### C.28:4.4 - Identification Profile

`CausalIdentificationProfile` answers whether a causal or counterfactual estimand can be expressed from available data plus assumptions, graph representation, and inferential calculus.

```text
CausalIdentificationProfile:
  causalUseQuestionRef: U.CausalUseQuestion
  estimandRef: U.CausalEstimand
  targetCausalityLadderRung: CausalityLadderRung
  sourceCausalEvidenceSupportBasis?: CausalEvidenceSupportBasis
  structuralCausalModelRef?: StructuralCausalModelRef
  causalDiagramRef?: CausalDiagramRef
  causalGraphRepresentationKind?: CausalGraphRepresentationKind
  graphSeparationCriterionKind?: GraphSeparationCriterionKind
  causalInferenceCalculusKind?: CausalInferenceCalculusKind
  causalAssumptionSetRef
  availableDataRegimeSetRef: AvailableCausalDataRegimeSetRef
  realizedCounterfactualDataRefs?: RealizedCounterfactualDataRefSet
  counterfactualDataIdentificationMethodRef?: CounterfactualDataIdentificationMethodRef
  counterfactualDataBoundRef?: CounterfactualDataBoundRef
  causalBoundOrPartialIdentificationRef?
  falsificationOrNegativeControlRef?
  sensitivityAnalysisRef?
  rivalCauseStressTestRef?
  verdict: identified | nonidentified | bounded | unknown
  supportedUse
  unsupportedUse
```

Identification is inferential support. It is not direct physical sampling.

Realized counterfactual data may change an identification route, tighten a bound, or change which assumptions are still needed. When it does, the profile names the data refs, identification method, and bound ref that changed the result. It does not erase the distinction between identification and direct sampling; the profile must still state what is identified, bounded, unknown, or not identified.

#### C.28:4.5 - Counterfactual Sampling Realizability Profile

`CounterfactualSamplingRealizabilityProfile` answers whether samples from a counterfactual-comparison target distribution can be physically obtained through admissible actions under physical, ethical, operational, unit-history, and graph constraints.

```text
CounterfactualSamplingRealizabilityProfile:
  causalUseQuestionRef: U.CausalUseQuestion
  targetCounterfactualDistributionRef
  targetCausalityLadderRung: counterfactualComparisonRung
  structuralCausalModelRef?: StructuralCausalModelRef
  causalDiagramRef?: CausalDiagramRef
  causalGraphRepresentationKind?: CausalGraphRepresentationKind
  graphSeparationCriterionKind?: GraphSeparationCriterionKind
  causalInferenceCalculusKind?: CausalInferenceCalculusKind
  graphChildInterventionConstraintRef?
  sameUnitConflictCheck
  ancestorRegimeConflictCheck
  physicalConstraintSetRef
  ethicalConstraintSetRef
  operationalConstraintSetRef
  unitHistoryAvailabilityRef?
  counterfactualSamplingActionSetRef
  counterfactualRandomizationCapabilityRef?
  counterfactualSamplingWorkPlanRef?
  verdict: realizable | nonrealizable | bounded | unknown
  supportedUse
  unsupportedUse
```

Realizability is operational. It asks what work can be done, by which system, with which action primitives, under which constraints.

#### C.28:4.6 - Applied Causal-Inference Profiles

Target-trial and potential-outcomes claims use `TargetTrialProtocolRecord` and `U.PotentialOutcomeContrast` when the causal-use claim is an applied intervention-effect claim.

```text
TargetTrialProtocolRecord:
  causalUseQuestionRef: U.CausalUseQuestion
  targetPopulationRef?
  eligibilityCriteriaRef?
  treatmentStrategySetRef
  treatmentAssignmentProcedureRef?
  timeZeroAlignmentRef?
  causalFollowUpWindowRef
  outcomeMeasureRef
  potentialOutcomeContrastRef?
  estimandRef: U.CausalEstimand
  causalAnalysisPlanRef?
```

Target-trial emulation from observational data adds a mapping/reporting record. `TargetTrialEmulationMappingRecord` records the fit between the protocol and the observed data; `TargetTrialProtocolRecord` alone does not state emulation adequacy.

```text
TargetTrialEmulationMappingRecord:
  targetTrialProtocolRef: TargetTrialProtocolRecord
  observationalDataSourceRef: ObservationalDataSourceRef
  eligibilityMappingRef: TargetTrialEligibilityMappingRef
  treatmentStrategyMappingRef: TargetTrialTreatmentStrategyMappingRef
  assignmentOrTimeZeroMappingRef: TargetTrialAssignmentOrTimeZeroMappingRef
  followUpMappingRef: TargetTrialFollowUpMappingRef
  outcomeMappingRef: TargetTrialOutcomeMappingRef
  emulationGapRef?: TargetTrialEmulationGapRef
  residualConfoundingAssessmentRef?: ResidualConfoundingAssessmentRef
  sensitivityOrAdditionalAnalysisRef?: TargetTrialSensitivityOrAdditionalAnalysisRef
  supportedEmulationUse: CausalUseSupportStatement
  unsupportedEmulationUse: CausalUseUnsupportedStatement
```

Numerical causal estimates use `CausalParameterEstimationProfile` when estimation validity is live:

```text
CausalParameterEstimationProfile:
  estimandRef: U.CausalEstimand
  causalIdentificationProfileRef?
  estimatorRef
  nuisanceModelSetRef?
  orthogonalScoreRef?
  crossFittingPlanRef?
  positivityOrOverlapCheckRef?
  sensitivityAnalysisRef?
  uncertaintyIntervalRef?
  supportedEstimateUse
  unsupportedEstimateUse
```

Transported support uses `CausalTransportabilityProfile`:

```text
CausalTransportabilityProfile:
  causalUseQuestionRef: U.CausalUseQuestion
  sourcePopulationRef
  targetPopulationRef
  sourceContextRef?
  targetContextRef?
  selectionDiagramRef?
  domainShiftAssumptionSetRef?
  transportFormulaOrBridgeRef?
  supportedTransportUse
  unsupportedTransportUse
```

Off-policy causal evaluation uses `OffPolicyCausalEvaluationProfile` when a policy is evaluated from data generated by another behavior or logging policy:

```text
OffPolicyCausalEvaluationProfile:
  evaluationPolicyRef
  behaviorPolicyRef
  causalUseQuestionRef: U.CausalUseQuestion
  sequentialHorizonRef?: SequentialPolicyHorizonRef
  adaptivePolicyClassRef?: AdaptivePolicyClassRef
  unitHistoryConditioningRef?: UnitHistoryConditioningRef
  confoundingAssumptionSetRef?
  supportOrOverlapCheckRef?
  policyTransportabilityRef?: CausalPolicyTransportabilityRef
  offPolicyEstimatorRef?
  uncertaintyIntervalRef?
  supportedPolicyUse
  unsupportedPolicyUse
```

Causal representation learning uses `CausalVariableRepresentationRecord` when abstract causal variables are learned, selected, abstracted, or represented from fine-grained observations rather than given by the domain:

```text
CausalVariableRepresentationRecord:
  causalUseQuestionRef?: U.CausalUseQuestion
  structuralCausalModelRef?: StructuralCausalModelRef
  causalVariableSetRef
  representationSourceRef
  abstractionOrSelectionMethodRef?
  interventionValidityRef?: CausalRepresentationInterventionValidityRef
  mechanismInvarianceRef?: CausalRepresentationMechanismInvarianceRef
  abstractionFidelityRef?: CausalRepresentationAbstractionFidelityRef
  counterfactualQueryPreservationRef?: CausalRepresentationCounterfactualQueryPreservationRef
  representationShiftRef?: CausalRepresentationShiftOrOODRef
  validationRef?
  supportedCausalVariableUse
  unsupportedCausalVariableUse
```

#### C.28:4.7 - Causal Graph Representation Names

Use names that causal inference specialists can recognize:

```text
CausalGraphRepresentationKind =
  causalDirectedAcyclicGraphRepresentation |
  acyclicDirectedMixedGraphRepresentation |
  singleWorldInterventionGraphRepresentation |
  structuralCausalModelTwinNetworkRepresentation |
  ancestralMultiWorldNetworkRepresentation |
  counterfactualGraphicalModelRepresentation
```

When graph separation or graphical calculus is part of the causal-use support, use controlled values rather than open prose:

```text
GraphSeparationCriterionKind =
  dSeparationCriterion |
  mSeparationCriterion |
  singleWorldInterventionGraphSeparationCriterion |
  ancestralMultiWorldNetworkSeparationCriterion |
  counterfactualGraphSeparationCriterion

CausalInferenceCalculusKind =
  doCalculus |
  ctfCalculus |
  potentialOutcomeCalculus |
  gFormulaCalculus
```

`CausalGraphRepresentationKind`, `GraphSeparationCriterionKind`, and `CausalInferenceCalculusKind` are formal-support classification values, not minted model objects. They classify the formal support form being used for causal support. Concrete `...Ref` fields point to actual models, diagrams, proof objects, assumptions, or epistemes and must be present when that formal support form is load-bearing. For example, `StructuralCausalModelRef` cites a concrete SCM object, while `structuralCausalModelTwinNetworkRepresentation` classifies a representation form.

`StructuralCausalModel` is the causal model kind with endogenous variables, exogenous variables, structural assignments, and intervention semantics. `structuralCausalModelTwinNetworkRepresentation` means the SCM twin-network representation used in counterfactual reasoning with shared exogenous variables. It is not a deep-learning twin network.

Acronyms such as SCM, DAG, ADMG, SWIG, and AMWN may appear as source/plain labels and bridge notes. FPF Tech values expand the source name when expansion reduces alias risk.

#### C.28:4.8 - Causal Use Evidence Design

Use `CausalUseEvidenceDesignRecord` when the causal-use claim needs evidence planning, evidence graph support, experiment or quasi-experiment design, counterfactual randomization, mixed-design accountability, or simulation validation.

```text
CausalUseEvidenceDesignRecord:
  causalUseQuestionRef: U.CausalUseQuestion
  targetCausalityLadderRung: CausalityLadderRung
  estimandRef?
  causalInterventionSpecRef?
  targetTrialProtocolRef?
  potentialOutcomeContrastRef?
  causalIdentificationProfileRef?
  causalParameterEstimationProfileRef?
  counterfactualSamplingRealizabilityProfileRef?
  causalTransportabilityProfileRef?
  causalVariableRepresentationRef?
  causalEvidenceSupportBasis: CausalEvidenceSupportBasis
  causalEvidenceWorkRefs?
  causalEvidenceRoleRefs?
  causalEvidenceMethodRef?
  causalEvidenceWorkPlanRef?
  structuralCausalModelRef?
  causalDiagramRef?
  causalGraphRepresentationKind?: CausalGraphRepresentationKind
