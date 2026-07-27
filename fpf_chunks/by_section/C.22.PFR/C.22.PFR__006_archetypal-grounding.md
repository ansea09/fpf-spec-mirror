---
chunk_kind: "child"
pattern_id: "C.22.PFR"
pattern_title: "Problematic-For Relation"
section_id: "C.22.PFR:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.PFR/C.22.PFR__006_archetypal-grounding.md"
commit_sha: "1f413fcd23f4ea26956a45d67dde57bb233f6ad9"
heading_path:
  - "C.22.PFR — Problematic-For Relation"
  - "C.22.PFR:5 — Archetypal Grounding"
line_start: 51062
line_end: 51089
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19"
  - "A.3.4"
  - "A.6.5"
  - "A.6.REL"
  - "B.3"
  - "C.22"
  - "C.22.2"
  - "E.18.1"
  - "E.23"
  - "G.11"
keywords:
  - "actual adverse condition"
  - "actual adverse episode"
  - "assessment and evidence separation"
  - "condition-to-predicate input rule"
  - "exact problem-for entity and use"
  - "independent criterion-applicability relation"
---

### C.22.PFR:5 - Archetypal Grounding

**Executable first use — `Battery-12` cannot support `Van-7`'s intended start.** At 10:02 the starter of `Van-7` is engaged. The project electrical owner identifies one obtaining `TerminalVoltageState-12` relation with bearer `Battery-12`, load condition `Van7StarterLoad-1`, and characteristic assignment `terminalVoltageUnderStarterLoad = 10.8 V` on the volt scale. That state relation actually obtains from 10:02 until `Battery-12` is removed from `Van-7` at 10:06.

The same case has one `Van7StartCriterionApplicability-12` occurrence. Its by-value predicate `Van7StartVoltageAtLeast11_8` selects the direct `terminalVoltageUnderStarterLoad` input, cut `11.8 V`, and lower-is-adverse polarity. It governs problem-for entity `Van-7`, claim scope `intended engine start at Depot-A`, and declared applicability window `[09:55, 10:15]`. The exact C.13 Working-Model occurrence `ut:ComponentOf(Battery-12, Van-7)` connects the condition bearer to that vehicle. Because the selected point is `10.8 V`, the PFR actually obtains on `[10:02, 10:06]`.

`MeterReport-88` is a separate assessment claim: it says that the terminal voltage under starter load was `10.8 V` at 10:03 and supports the claim that the PFR obtained then. The report did not make the voltage state, applicability, or PFR obtain.

The resulting ordinary sentence is:

> Battery-12 supplies 10.8 V under Van-7's starter load, below the 11.8 V start cut during the 09:55–10:15 intended-start window; this low loaded voltage is an actual Problem for Van-7's intended start from 10:02 until Battery-12 is removed at 10:06.

**Cheapest valid stop.** A mechanic who only needs to recognize this Problem records that sentence, cites the two world-side relation-occurrence references `TerminalVoltageState-12` and `Van7StartCriterionApplicability-12`, and keeps `MeterReport-88` as the separate supporting claim; no explicit PFR record or identifier is required.

**One receiving-use expansion.** A recurrence comparison that must distinguish this episode from a later low-voltage episode additionally records the two participant-occurrence references, actual inception `10:02`, stable `pfrOccurrenceId=PFR-VAN7-START-20260723-1002`, the claimed closed extent `[10:02, 10:06]`, and the separate supporting claim `MeterReport-88`. Those references let the comparison point back to this occurrence; none is an extra PFR participant.

**Near miss — same number, wrong input.** `OpenCircuitVoltageMeasurement-89` also reports `10.8 V`, but it was taken after `Battery-12` was removed from `Van-7` and supplies the coordinate `openCircuitTerminalVoltage`, not `terminalVoltageUnderStarterLoad`. The start predicate's input rule rejects that measurement, and the condition-to-vehicle/use link is absent. The same numeric value may matter under another criterion, but it does not establish a Problem for `Van-7`'s intended start.

**Distinct projected-input branch — proof gap.** `UnresolvedConsequence-17` is the exact obtaining relation inside `SafetyProof-v5`; the proof-acceptance consumer's named `RequiredObligationGapCountProjection-v1` maps only unresolved required obligations of that proof to coordinate `unresolvedRequiredObligationCount = 1` in `ProofAcceptanceSpace`, on the natural-count scale with cut `0` and greater-than-zero-is-adverse polarity. `ReleaseAssuranceClaim-3` is the problem-for entity. The exact A.10 evidence-provenance graph occurrence `SafetyProofEvidencePath-3` names `SafetyProof-v5` as its evidence episteme, `ReleaseAssuranceClaim-3` as its target claim, and the release-assurance use stated by that claim's B.3 tuple as its bounded relying use. Counting every TODO in the repository is inadmissible because those items are neither required proof obligations nor evidence for that release-assurance claim.

**Distinct claim/actuality branch — clinical diagnosis.** A patient-specific clinical-condition relation, an obtaining applicability relation, and actual adverse predicate truth can make PFR obtain before any diagnosis is authored. A later diagnosis episteme may support a claim about that PFR but does not become its condition participant, problem-for entity, or inception boundary.

**Distinct problem-for branch — missed transfer.** A missed-transfer relation can be the condition while one exact receiving Work occurrence is the problem-for entity. The coordination participants stay in the missed-transfer relation; the applicability relation names the affected Work as its problem-for entity rather than copying it into PFR.

**Distinct multiplicity branch — one condition, two uses.** One hot-surface condition paired with two applicability occurrences for different exact receiving work or systems yields two PFR occurrences when the condition satisfies both adverse predicates. The applicability references distinguish them; PFR copies neither receiving participant nor scope.

**Distinct actuality/repair branch — unnoticed and repaired.** A condition and applicability can make PFR obtain before monitoring exists. Selecting a repair method changes only the solvability claim. Performed repair work ends PFR only when its world-side result actually ends or changes an obtaining condition; work records and result claims remain separately governed.

