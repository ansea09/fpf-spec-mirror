---
chunk_kind: "child"
pattern_id: "C.41.TF"
pattern_title: "Construct a Checklist Template That Preserves Its Questions"
section_id: "C.41.TF:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.41.TF/C.41.TF__006_archetypal-grounding.md"
commit_sha: "a5ac87ac15e78517d12bc66155b9da3ca254b643"
heading_path:
  - "C.41.TF — Construct a Checklist Template That Preserves Its Questions"
  - "C.41.TF:5 — Archetypal Grounding"
line_start: 88702
line_end: 88728
dependencies:
  - "C.37"
  - "C.41"
  - "C.41.OF"
keywords:
---

### C.41.TF:5 - Archetypal Grounding

The selected card questions become this reusable template:

| Set and comparison description | All described cards present and readable? | Wording matches the described edition? | Set assembled for delivery? |
| --- | --- | --- | --- |
| Identify the physical set and the description of its contents | Answer; count/inspection basis; observation time when reused | Answer; comparison basis and observation time | Answer; assembly observation and time |

A constructed instance supplies the references and grounds:

| Set and comparison description | All described cards present and readable? | Wording matches the described edition? | Set assembled for delivery? |
| --- | --- | --- | --- |
| S; twenty cards, wording v2 | Yes: twenty present and readable, observed 10:00 | Yes: all cards compared with v2, observed 10:05 | Yes: assembled, observed 10:10 |

Suppose the wide table on a small screen separates the answer from its S/v2 reference. Transpose the same information so the recipient can recover both together:

| Question for S against the description of twenty cards with wording v2 | Answer and basis |
| --- | --- |
| All described cards present and readable? | Yes: twenty present and readable, observed 10:00 |
| Wording matches v2? | Yes: all cards compared with v2, observed 10:05 |
| Set assembled for delivery? | Yes: assembled, observed 10:10 |

If entries are recorded at 10:12, that time describes the recording. It neither changes the observation times nor shows when each condition first became true. A split view for counting and a view for wording comparison retain the S/v2 references and the relevant observation grounds. A detached green square cannot do that.

For an AI-assisted importer, a template can ask for an observed catalogue before and after a malformed input, with a reference to the input and the comparison performed. A field headed “Tests pass” loses the specific question if it is detached from those cases. When an observation tool fails, the form supports “unknown: post-import catalogue was not obtained”; it does not coerce the agent into a positive completion entry.


