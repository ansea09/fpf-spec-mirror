---
chunk_kind: "child"
pattern_id: "A.15.9"
pattern_title: "Request and Use a Bounded Result from Another Practice"
section_id: "A.15.9:5"
section_title: "Worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.9/A.15.9__006_worked-cases.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "A.15.9 — Request and Use a Bounded Result from Another Practice"
  - "A.15.9:5 — Worked cases"
line_start: 27784
line_end: 27803
dependencies:
  - "A.10"
  - "A.13"
  - "A.15"
  - "A.15.1"
  - "A.15.7"
  - "A.2.1"
  - "A.2.2"
  - "A.2.9"
  - "C.2.1"
  - "C.38"
  - "E.18.1"
  - "F.6"
keywords:
---

### A.15.9:5 - Worked cases

#### A.15.9:5.1 - Reuse closes a payroll scheduling question

An administrator asks whether moving one contractor submission from Thursday to Friday will miss the current pay run. Before requesting new payroll Work, the administrator finds a dated payroll result for the same payroll entity, contractor batch, cutoff, and calendar edition. The source is current for employee payments but explicitly excludes the contractor batch.

The bounded disposition is: “Use the current result for employee items only. The contractor item remains blocked because the checked result does not cover that batch.” No new payroll assignment, meeting, Work occurrence, delivery, or approval is invented. The administrator either keeps the contractor date unchanged or requests the missing contractor-cutoff result.

#### A.15.9:5.2 - A heat-pump choice needs one acoustic result

An engineering team is choosing a compressor operating region. It already has a general product noise rating, but the decision concerns tonal noise in a named room, mounting configuration, and speed range. The general rating is useful source material but is not qualified for that use.

The team requests: “For the controller decision, return the observed tonal-noise and vibration limits for this compressor, mounting, room, and speed range, with the tested conditions and unsupported region. A supported limit, objection, or missing-test blocker is useful; the acoustics result does not choose the controller.” The acoustics practice keeps its Method and evidence rules; the engineering team keeps the architecture decision. If the question later becomes which complete internal, provider, reuse, or redesign way can make the same accepted control result available, leave this one-contribution question and use `C.38`.

#### A.15.9:5.3 - A fluent tool output is not specialist approval

A case worker receives a generated summary labelled *verified legal review*. The summary cites no governing edition, jurisdiction, case configuration, performing Agent, Method, or authority. It may help locate sources, but it cannot support the current eligibility decision.

The honest first result is a blocker: “The generated summary is not qualified for this case and jurisdiction. Obtain a dated legal result for the named eligibility question, or stop the decision.” If later evidence supports the tool or another Agent as the actual performer of bounded legal-research Work, those facts still do not create legal authority or make the receiving administrative decision.

