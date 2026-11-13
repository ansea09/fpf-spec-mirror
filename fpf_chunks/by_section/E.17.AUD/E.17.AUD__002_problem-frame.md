---
chunk_kind: "child"
pattern_id: "E.17.AUD"
pattern_title: "Keep a Publication Unit Stable (PublicationUnit Stability Discipline)"
section_id: "E.17.AUD:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.AUD/E.17.AUD__002_problem-frame.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "E.17.AUD — Keep a Publication Unit Stable (PublicationUnit Stability Discipline)"
  - "E.17.AUD:1 — Problem frame"
line_start: 115960
line_end: 115977
dependencies:
  - "A.16.0"
  - "A.7"
  - "C.2.1"
  - "C.2.2a"
  - "E.10"
  - "E.14"
  - "E.17"
  - "E.17.AUD"
  - "E.17.AUD.LHR"
  - "E.17.AUD.OOTD"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.19"
  - "E.21"
  - "F.18"
keywords:
---

### E.17.AUD:1 - Problem frame

Use this pattern when people read a note, memo, sheet, table, screen, or short section as one stable unit but it leaves a change in its main subject, its publication move, or its boundary with a decision, gate, work, or reliance claim unmarked.

A typical case starts with one bounded architecture or status question and ends by sounding like rollout, approval, assignment, or assurance. One reviewer wants to repair a vague word, another wants to rewrite the whole unit, and a third sees a comparison or explanation problem. Before they patch different defects, identify the bounded publication unit and its current interpretation.

Name the unit's primary subject. When it carries or exposes a claim-bearing `U.Episteme` or episteme-side `U.View`, use that item's `EntityOfConcern` value only when it is also the unit's primary subject. Otherwise name the ordinary topic or subject and do not invent an `EntityOfConcernRef`. Keep the publication unit distinct from the episteme, publication occurrence, form, face, carrier, and any downstream project claim.

The primary reader is an author or reviewer who needs one usable repair choice. Architects, managers, and program leads are secondary readers when the same unit is being over-read as architecture, approval, or work guidance.

If this check is missed, teams repair one word when the whole interpretation has shifted, rebuild a whole unit when one local head was enough, or polish a comparison, explanation, or status note until it looks like evidence or approval.

The check helps the team choose one response early: keep the unit as it is, repair one local head, stabilize the whole unit, treat it as a bounded comparison, or leave this pattern for the applicable neighboring pattern and project record.

Use `E.17.AUD.LHR` when an overloaded local head is the only defect. A stable unit presenting a bounded comparison calls for `E.17.ID.CR`; an explanation-use problem calls for `E.17.EFP`. If the text is already being used to approve, direct, assign, adjudicate, or support reliance, use the applicable decision, gate, work, evidence, or reliance pattern. In those cases the narrower or neighboring pattern governs the work.

The first useful result is one of those five repair choices. If the unit, its primary subject, its publication move, and its outside boundary are already clear enough for the current reader, return `stable for current use` and stop. Use the checks and examples as needed. Their order is optional.

