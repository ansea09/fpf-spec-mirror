---
chunk_kind: "child"
pattern_id: "E.17.AUD"
pattern_title: "PublicationUnit Stability Discipline - keep one publication unit stable enough to read honestly"
section_id: "E.17.AUD:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.AUD/E.17.AUD__002_problem-frame.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "E.17.AUD — PublicationUnit Stability Discipline - keep one publication unit stable enough to read honestly"
  - "E.17.AUD:1 — Problem frame"
line_start: 84146
line_end: 84161
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.16.0"
  - "A.20"
  - "A.21"
  - "A.7"
  - "B.3"
  - "C.11"
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

Use this pattern when people still read one note, memo, sheet, table, screen, or short section as one stable unit even though it has quietly changed what it is mainly about, the publication move it makes, or the boundary between that move and a decision, gate, work, or reliance claim.

A typical case starts with one bounded architecture or status question and ends by sounding like rollout, approval, assignment, or assurance. One reviewer wants to repair a vague word, another wants to rewrite the whole unit, and a third sees a comparison or explanation problem. Before they patch different defects, identify the bounded publication unit and its current interpretation.

When the unit carries or exposes a claim-bearing `U.Episteme` or episteme-side `U.View`, use that item's primary `EntityOfConcern` value. Otherwise name the ordinary topic or subject and do not invent an `EntityOfConcernRef`. Keep the publication unit distinct from the episteme, publication occurrence, form, face, carrier, and any downstream project claim.

The primary reader is an author or reviewer who needs one usable repair choice. Architects, managers, and program leads are secondary readers when the same unit is being over-read as architecture, approval, or work guidance.

If this check is missed, teams repair one word when the whole interpretation has shifted, rebuild a whole unit when one local head was enough, or polish a comparison, explanation, or status note until it looks like evidence or approval. The check buys one early choice: keep the unit as it is, repair one local head, stabilize the whole unit, treat it as a bounded comparison, or leave this pattern for the applicable neighboring pattern and project record.

Do not use this pattern when one overloaded local head is the only defect; when the stable unit already presents a bounded comparison; when the live issue is explanation use; or when the text is already being used to approve, direct, assign, adjudicate, or support reliance. Apply `E.17.AUD.LHR`, `E.17.ID.CR`, `E.17.EFP`, or the applicable decision, gate, work, evidence, or reliance pattern instead.

The first useful result is one of those five repair choices. If the unit, its primary subject, its publication move, and its outside boundary are already clear enough for the current reader, return `stable for current use` and stop. The checks and examples below are aids, not a mandatory engineering sequence.

