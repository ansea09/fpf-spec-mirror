---
chunk_kind: "child"
pattern_id: "B.2.5"
pattern_title: "Supervisor-Subholon Feedback Relation"
section_id: "B.2.5:10"
section_title: "SoTA-Echoing — establish the feedback claimed for this interval"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.5/B.2.5__013_sota-echoing-establish-the-feedback-claimed-for-this-interval.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "B.2.5 — Supervisor-Subholon Feedback Relation"
  - "B.2.5:10 — SoTA-Echoing — establish the feedback claimed for this interval"
line_start: 41834
line_end: 41845
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15.1"
  - "A.2.1"
  - "A.20"
  - "A.21"
  - "A.3.3"
  - "A.3.4"
  - "A.6.M"
  - "A.6.RCD"
  - "B.1"
  - "B.2"
  - "B.2.P"
  - "B.3"
  - "C.13"
  - "C.2.1"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30.LCA"
  - "E.10"
  - "F.19"
  - "G.6"
keywords:
---

### B.2.5:10 - SoTA-Echoing — establish the feedback claimed for this interval

**Practice question.** What is enough to say that a named controller and holon participated in feedback during a specified interval? The selected line requires observation, returned influence and their rule-governed coupling. A serious cheaper alternative describes the intended controller, feedback channel and command channel in a functional control structure. That description can answer a design question before any operation occurs; it cannot alone settle an assertion about an actual interval.

[Åström and Murray's Feedback Systems, Chapter 1 summary](https://fbswiki.org/wiki/index.php/Introduction) supplies the selected control-theoretic line: feedback involves reciprocal influence, and sensing, computation and actuation form the basic control loop. The same source treats stability and useful closed-loop behavior as further design questions. **Adapt** reciprocal influence into the three propositions in §4, retaining each domain's actual coupling rule. This supports a minimal descriptive assertion, not an import of continuous-time dynamics into organizational or episteme examples.

The [STPA Handbook, MIT-STAMP-001, March 2018, Chapter 2, pp. 22–25 and 45–48](https://psas.scripts.mit.edu/home/get_file.php?name=STPA_Handbook.pdf) supplies the substantive control-structure comparator and failure analysis. It distinguishes a functional structure of possible information flow from physical structure, and examines missing, delayed or incorrectly used feedback. **Adopt** those distinctions for the view boundary in §4.4 and the interruption cases in §5.1. **Reject** using the diagram alone as an actual-interval witness; that shortcut is not a claim of the handbook. The handbook remains a source for analysis of control and unsafe scenarios, not a certificate that B.2.5's assertion establishes safety.

The difference is visible at ticks 10–14 in §5.1. The intended diagram can stay unchanged while a delivered broadcast is unrelated to the observation, a command is absent, or the link is broken. Testing the three propositions distinguishes those cases and treats an unavailable trace as unresolved. The comparison therefore governs §4.1's coupling and absence tests and `CC-B2.5-2–3`, while leaving C.30.LCA to describe the structure.

For an operational claim, both approaches can reuse the same controller rule and available trace; checking the relevant observation/return pair adds local work but closes a question the diagram leaves open. For an intended design, retain the cheaper structural description. A full dynamics model or STPA analysis costs more and answers stronger questions; it is needed only when those questions are selected. Reopen when the coupling rule, interval or member set changes, or a receiving use needs to reidentify one feedback occurrence across interruptions. These sources do not supply that new occurrence's identity rule or establish the FPF Holon classification of an organizational example.

