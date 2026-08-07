---
chunk_kind: "child"
pattern_id: "E.14"
pattern_title: "Human‑Centric Working‑Model"
section_id: "E.14:6"
section_title: "Archetypal Grounding (System / Episteme)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.14/E.14__009_archetypal-grounding-system-episteme.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "E.14 — Human‑Centric Working‑Model"
  - "E.14:6 — Archetypal Grounding (System / Episteme)"
line_start: 78577
line_end: 78606
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

### E.14:6 - Archetypal Grounding *(System / Episteme)*

> **Tell–Show–Show.** The principle is stated once, then shown on a `U.System` case (structural) and on a `U.Episteme` case (knowledge‑bearing), in line with the authoring template.

#### E.14:6.1 - `U.System` — Working‑Model first, Constructive grounding available

* **Publication (Working‑Model).** Authors state structure using familiar relations (e.g., *Impeller* **ut\:ComponentOf** *Pump*; *Pump* **ut\:ComponentOf** *Skid*). Nothing else is required for readers to follow the design.
* **Assurance (downward grounding).** When higher assurance is sought, first recover the exact skid, parts, direct fastening, coupling, enclosure, terminal, flange, and seal occurrences, the applicable skid assembly rule, and the skid reidentification rule. Then link the published claim to one current C.2.1 `sum` trace that reports those facts and declare the assurance posture. The account remains below the Working-Model; order and time stay in their own relation families.
* **Canonization move.** Readers continue to see Working‑Model relations as the primary Working-Model text; the constructive story is *supporting*, not *defining*.

#### E.14:6.2 - `U.Episteme` - Working-Model first; Logical, Mapping, and exact empirical support as appropriate

* **Publication (Working-Model).** Authors connect meaning-bearing epistemes or publications using exact knowledge relations (for example, **RepresentationOf** or **UsageOf**) in the same human-oriented style.
* **Assurance (downward grounding).** Logical or Mapping assurance often suffices for interpretation and alignment. When observation is the right currency, name the exact target claim, scope and window, dated evaluation or measurement Work, performer system and obtaining assignment, enacted Method, any relied-on MethodDescription, actual direct participants or A.6.1 bindings, domain-local result and result episteme, A.10 evidence-provenance path, and any B.3 assurance claim. A record, provenance value, or assurance tuple is not the observation, Work, or result.
* **Canonization move.** Working-Model text remains the public form; the exact result and support chain stays available underneath without leaking method, record, or time semantics into the subject claim.

#### E.14:6.3 - Pump-vibration measurement: short recognition, exact assurance underneath

**Recognition text.** `Pump-37 vibration at 09:00 was 2.1 mm/s with stated uncertainty 0.2 mm/s under the current inspection method.` A maintenance reader can use that bounded statement and stop before the machinery below. It does not by itself say the pump passes a maintenance criterion, that work may start, or that any gate or permission is current.

**Assurance text.** `Pump37InspectionPlan-E3 : U.WorkPlan` had designated the intended measurement and selected `PumpVibrationMeasurementMethod-E2 : U.Method`; it cited `PumpVibrationProcedure-E5 : U.MethodDescription` only for the setup and calibration claims used by the plan. Dated `Pump37VibrationMeasurement-2026-07-31T0900 : U.Work` was performed by `ConditionMonitoringSystem-7 : U.System` under obtaining `RA-ConditionMonitoring-7-E4`, enacted that Method, and used exact C.16/A.6.1 bindings for `Pump-37`, the sensor indication, calibration coefficients, and returned measurement value.

C.16 owns the domain-local measurement result and C.2.1 identifies `Pump37VibrationResult-E4`, the episteme that states it under the exact Characteristic, Scale, unit, uncertainty, time stance, and interpretation basis. A.10 path `Pump37MeasurementProvenancePath-E6` cites the calibration, Work, bindings, and source publications; B.3 assurance claim `Pump37MeasurementAssurance-E2` qualifies only the stated use and window. Neither provenance nor assurance is the measurement result. No A.15.PROD claim is needed merely because the result episteme exists; open that pattern only if a separately current question asks whether the exact measurement Work first constituted that episteme.

**What changes in practice.** A reader sees the usable statement first, can inspect the exact work/result/support chain when reliance matters, and returns to the maintenance-criterion, readiness, gate, or permission owner if the next decision asks one of those different questions.

#### E.14:6.4 - Pattern lesson

The **Working-Model layer remains the canonical publication face** for authors and assurance readers. Mapping, Logical, Constructive, and Empirical assurance are purpose-selected shoulders beneath it. They preserve a short recognition route while keeping exact direct facts, work, local results, provenance, assurance, and currentness recoverable under their own governors.

