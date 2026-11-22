---
chunk_kind: "child"
pattern_id: "A.2.9"
pattern_title: "U.SpeechAct — Communicative Work and Its Intended Use"
section_id: "A.2.9:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.9/A.2.9__004_problem-frame.md"
commit_sha: "4ee69807f8e5d4fa438e8c9b5de001d91275cc31"
heading_path:
  - "A.2.9 — U.SpeechAct — Communicative Work and Its Intended Use"
  - "A.2.9:1 — Problem frame"
line_start: 9202
line_end: 9220
dependencies:
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.2.8"
  - "A.2.9"
  - "A.6.C"
  - "A.7"
  - "F.6"
  - "U.Work"
keywords:
  - "A.13-qualified actual performer"
  - "containment"
  - "enacted Method"
  - "evidence carrier"
  - "independently admitted speech-act Work"
  - "institutional target and effect"
  - "named receiving use"
  - "optional SpeechActRecord"
  - "publication relation"
  - "response versus achievement"
  - "same obtaining assignment"
  - "separate later performedUnderAssignment"
  - "smallest repair or stop"
  - "time"
  - "utterance description"
---

### A.2.9:1 — Problem frame

FPF repeatedly needs to reference “someone said/did the approving/authorizing/declaring thing”:

* System-role-assignment eligibility and enactability checklists often depend on the **presence of an approval or authorization act** within a freshness window.
* Governance patterns and boundary writing (A.6 stack) need **provenance**: “this obligation or commitment, or this separately represented granted permission, was instituted by *that* act”.
* Operational patterns need auditable **notices** (“depletion notice”, “override invoked”) whose existence and timing matter.

The same separation matters before formal occurrence modeling. An observed response can satisfy an order for that response, with the agreed authority, subject and timing. A claim that the communication enabled another action needs grounds for that action. A claim that it caused a later change needs grounds for causation. Ordinary receiving-use judgments can usually be stated directly.

Without a first-class kind for such communicative Work and a separate way to describe each occurrence, authors tend to:

* attribute agency to descriptions (“the spec approves…”, “the interface guarantees…”),
* collapse “utterance text” and “speech act event”,
* leave provenance dangling as “if modeled”,
* encode gates as prose obligations, or treat obligations as gates.

The definition below admits `U.SpeechAct` as an explicit Work kind and states the identity conditions for actual speech-act occurrences; their optional records remain separate from `U.Commitment`, utterance descriptions, and carriers.

