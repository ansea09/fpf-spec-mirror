---
chunk_kind: "child"
pattern_id: "E.14"
pattern_title: "Human‑Centric Working‑Model"
section_id: "E.14:6"
section_title: "Archetypal Grounding (System and Episteme cases)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.14/E.14__009_archetypal-grounding-system-and-episteme-cases.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "E.14 — Human‑Centric Working‑Model"
  - "E.14:6 — Archetypal Grounding (System and Episteme cases)"
line_start: 80723
line_end: 80754
dependencies:
  - "B.3.5"
  - "C.13"
  - "C.2.3"
  - "E.10"
  - "E.7"
  - "E.8"
keywords:
  - "assurance layers"
  - "grounding"
  - "human-centric"
  - "publication surface"
  - "working model"
---

### E.14:6 - Archetypal Grounding *(System and Episteme cases)*

> **Tell–Show–Show.** The principle is stated once, then shown on a `U.System` case (structural) and on a `U.Episteme` case (knowledge‑bearing), in line with the authoring template.

#### E.14:6.1 - `U.System` — Working‑Model first, Constructive grounding available

* **Publication (Working‑Model).** Authors state structure using familiar relations (e.g., *Impeller* **ut\:ComponentOf** *Pump*; *Pump* **ut\:ComponentOf** *Skid*). Nothing else is required for readers to follow the design.
* **Assurance (downward grounding).** When the publication elects `B.3.5`, first recover the exact skid, parts, direct fastening, coupling, enclosure, terminal, flange, and seal occurrences, the applicable skid assembly rule, and the skid reidentification rule. Then link the readable claim to one current C.2.1 `sum` trace that reports those facts and declare `validationMode=axiomatic`. If another named current requirement calls for a construction account, follow its stated obligations instead of borrowing `B.3.5` automatically. The account remains below the Working-Model; order and time stay in their own relation families.
* **Canonization move.** Readers continue to see Working‑Model relations as the primary Working-Model text; the constructive story is *supporting*, not *defining*.

#### E.14:6.2 - `U.Episteme` - Working-Model first; Logical, Mapping, and exact empirical support as appropriate

* **Publication (Working-Model).** Authors connect meaning-bearing epistemes or publications using exact knowledge relations (for example, **RepresentationOf** or **UsageOf**) in the same human-oriented style.
* **Assurance (downward grounding).** If the direct knowledge relation is sufficient, stop after the readable claim. When interpretation or alignment needs assurance, select Logical or Mapping support. When observation is the right currency, name the target claim, scope and window, dated evaluation or measurement Work, every performer System, and the Method the Work enacted. First recover each performer's A.13 core and independently admit the Work under A.15.1. Because this branch also asks under which assignment the Work was performed, check that exact link afterward with F.6 and use A.2.1 for the assignment itself. Cite a MethodDescription or local system-role-kind classification only when the claim uses it. Then name the participants or A.6.1 bindings, domain-local result and result episteme, A.10 evidence-provenance path, and any B.3 assurance claim that the assurance use consumes. A record, provenance value, assignment, or assurance tuple is not the observation, Work, performer, or result.
* **Canonization move.** Working-Model text remains the public form; the exact result and support chain stays available underneath without leaking method, record, or time semantics into the subject claim.

#### E.14:6.3 - Pump-vibration measurement: short recognition, exact assurance underneath

**Recognition text.** `Pump-37 vibration at 09:00 was 2.1 mm/s with stated uncertainty 0.2 mm/s under the current inspection method.` A maintenance reader can use that bounded statement and stop before the machinery below. It does not by itself say the pump passes a maintenance criterion, that work may start, or that any gate or permission is current.

**Assurance text.** This worked slice elects empirical assurance for a current reliance question. `Pump37InspectionPlan-E3`, admitted as a `U.WorkPlan`, had designated the intended measurement and selected `PumpVibrationMeasurementMethod-E2`, admitted as a `U.Method`; it cited `PumpVibrationProcedure-E5`, admitted as a `U.MethodDescription`, only for the setup and calibration claims used by the plan.

The measurement domain declares `PumpVibrationMeasurementAssignment` as the assignment species for this work. `RA-ConditionMonitoring-7-E4` is its occurrence, is held by `ConditionMonitoringSystem-7`, and covers the measurement interval. That System performed the admitted Work `Pump37VibrationMeasurement-2026-07-31T0900` under the assignment, and the Work enacted `PumpVibrationMeasurementMethod-E2`. Check the Work and enacted Method with A.15.1, and the Work-assignment attribution with F.6. The applicable A.6.1 bindings identify `Pump-37`, the sensor indication, calibration coefficients, and returned measurement value. Classification of the System under `PumpVibrationMeasurementSystemRole` is a separate claim.

Use C.16 to characterize the domain-local measurement result by its exact Characteristic, Scale, unit, uncertainty, time stance, and interpretation basis. C.2.1 identifies `Pump37VibrationResult-E4`, the episteme that states that result. A.10 path `Pump37MeasurementProvenancePath-E6` cites the calibration, Work, bindings, and source publications; B.3 assurance claim `Pump37MeasurementAssurance-E2` qualifies only the stated use and window. Neither provenance nor assurance is the measurement result. No A.15.PROD claim is needed merely because the result episteme exists; open that pattern only if a separately current question asks whether the exact measurement Work first constituted that episteme.

**What changes in practice.** A reader sees the usable statement first, can inspect the exact Work, result, and support chain when reliance matters, and uses the applicable maintenance-criterion, readiness, gate, or permission pattern if the next decision asks one of those different questions.

#### E.14:6.4 - Pattern lesson

The **Working-Model layer remains the canonical publication face** for authors and assurance readers. A direct claim outside an elected profile carries no E.14 assurance fields. When assurance is current, Mapping, Logical, Constructive, and Empirical support remain purpose-selected shoulders beneath the claim. They preserve a short recognition route while keeping the facts, Work, local results, provenance, assurance, and currentness consumed by that use recoverable through the patterns that define them.

