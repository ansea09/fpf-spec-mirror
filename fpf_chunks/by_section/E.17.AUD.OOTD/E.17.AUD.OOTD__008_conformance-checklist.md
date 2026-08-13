---
chunk_kind: "child"
pattern_id: "E.17.AUD.OOTD"
pattern_title: "PublicationUnit Stability Discipline and PublicationUnit Primary-Subject Discipline - publication-unit stability over one primary subject"
section_id: "E.17.AUD.OOTD:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.AUD.OOTD/E.17.AUD.OOTD__008_conformance-checklist.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "E.17.AUD.OOTD — PublicationUnit Stability Discipline and PublicationUnit Primary-Subject Discipline - publication-unit stability over one primary subject"
  - "E.17.AUD.OOTD:7 — Conformance Checklist"
line_start: 83901
line_end: 83923
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.16.0"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.RT"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.2.2a"
  - "E.10"
  - "E.14"
  - "E.17.AUD.LHR"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.19"
  - "F.18"
keywords:
---

### E.17.AUD.OOTD:7 - Conformance Checklist

**Checklist scope.** Use this checklist when checking a claimed application of this pattern, not as nine required authoring steps. The one- or two-sentence ordinary declaration remains a complete result; inspect only the rows implicated by the actual unit, transition, `EntityOfConcern` projection, neighboring claim, or unit-architecture choice, and do not publish a nine-row record by default.

1. **CC-OOTD-1 - One publication unit is explicit.**
   The publication unit under review is explicitly identifiable as one note, memo, sheet, screen, table, or section meant to be read as one unit.
2. **CC-OOTD-2 - Primary subject is explicit.**
   The unit states what it is mainly about in ordinary language rather than asking readers to infer it from tone.
3. **CC-OOTD-3 - Any `EntityOfConcern` projection is exact and conditional.**
   The unit uses `EntityOfConcern` only for the exact entity participant of one identified claim-bearing episteme under `C.2.1`; a topic, kind, question, or interpretation is never substituted for that participant.
4. **CC-OOTD-4 - Concern, carried move, downstream use, and outside work are distinct.**
   The unit states which question it foregrounds, what it asserts or communicates, how readers may use it, and which wider work, approval, execution, decision, or reliance remains outside.
5. **CC-OOTD-5 - Any transition is typed and explicit.**
   If subject, concern, claim or carried move, downstream use, or the exact entity participant changes, the unit names which change occurred rather than quietly absorbing all of them into one interpretation.
6. **CC-OOTD-6 - Local vs publication-unit repair choice is honest.**
   Apply `E.17.AUD.LHR` (`Local Head Restoration`) first when local repair is enough; apply this pattern only when publication-unit interpretation instability remains after local repair.
7. **CC-OOTD-7 - Neighboring-pattern boundary is explicit.**
   If an entityOfConcernRef-preserving transform, explanation, bridge, comparative-review, ontology, gate, approval, or execution claim becomes primary, use the neighboring pattern that defines or constrains that claim rather than pretending this pattern still carries the case.
8. **CC-OOTD-8 - Claim-bearing lens is stated when needed.**
   If a minimal modeling lens, exact `C.2.1` projection, or downstream-decision policy is materially claim-bearing, it is stated rather than silently assumed.
9. **CC-OOTD-9 - Unit architecture is the least-cost honest choice.**
   Retaining one unit, declaring a transition, keeping a sectioned multi-subject unit, or splitting is chosen from the current reader, use, reuse, dependency, and overread costs. The author does not split to satisfy a count and does not retain a vague umbrella to avoid a necessary split.

