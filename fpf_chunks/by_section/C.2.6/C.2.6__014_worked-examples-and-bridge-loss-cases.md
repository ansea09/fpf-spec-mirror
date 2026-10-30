---
chunk_kind: "child"
pattern_id: "C.2.6"
pattern_title: "Sources, Evidence and Conditions for Using an Episteme"
section_id: "C.2.6:13"
section_title: "Worked Examples and Bridge-Loss Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.6/C.2.6__014_worked-examples-and-bridge-loss-cases.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "C.2.6 — Sources, Evidence and Conditions for Using an Episteme"
  - "C.2.6:13 — Worked Examples and Bridge-Loss Cases"
line_start: 53817
line_end: 53829
dependencies:
  - "A.10"
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.18"
  - "A.19"
  - "A.2.4"
  - "A.6.6"
  - "A.6.P"
  - "A.7"
  - "B.4.1"
  - "B.5.2.0"
  - "C.2.1"
  - "C.2.2a"
  - "C.2.7"
  - "C.2.LS"
  - "C.2.P"
  - "F.9"
  - "F.9.1"
keywords:
  - "bodily observation"
  - "changed use"
  - "document access"
  - "evidence use"
  - "model derivation"
  - "operator interaction"
  - "provenance"
---

### C.2.6:13 - Worked Examples and Bridge-Loss Cases

#### C.2.6:13.1 - Bodily observation and its written report
An operator first notices vibration through bodily sensation. A prose report describes that observation. A later analyst who has only the report can recover its assertions but cannot repeat the operator's sensation from the text. Distinguish the source cue from the analyst's episteme; identify which observation circumstances the intended comparison or check needs and whether the report preserves them. Apply F.9 when the use claims a semantic correspondence between local senses from different semantic contexts.

#### C.2.6:13.2 - Model-derived score used by an operator
An episteme records a probe score obtained from a model state. A receiving alert reports that score in a procedure that requires operator acknowledgement before selection of the next diagnostic check. Keep both the source/probe derivation and the acknowledgement condition visible. A console display establishes the latter connection only when the required interaction is actually provided; the displayed score alone does not show that.

#### C.2.6:13.3 - Provenance, evidence and interaction in one alert
An alert E asserts that Pump P's pressure is below 90 kPa. The software produced E from trace T. An operator has acknowledged E and selected a diagnostic check under the stated procedure. Inspection then shows that T was a measurement of Pump Q.

The derivation from T remains established. T supplies no measurement of P for the claimed pressure: return to an appropriate observation of P before using that measurement as support for this claim. The acknowledgement and selected check remain facts about the operator's work. Whether to continue, suspend or change that check follows its actual rule and purpose; neither derivation nor acknowledgement settles the truth of the pressure claim. A report can publish all these statements together with their different grounds.

