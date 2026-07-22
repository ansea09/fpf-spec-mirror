---
chunk_kind: "child"
pattern_id: "C.19.2"
pattern_title: "Use-Bounded Apparatus Application"
section_id: "C.19.2:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19.2/C.19.2__014_relations.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "C.19.2 — Use-Bounded Apparatus Application"
  - "C.19.2:12 — Relations"
line_start: 49426
line_end: 49433
dependencies:
  - "A.15.1"
  - "A.15.2"
  - "A.7.1"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.22.1"
  - "C.31.ASAP"
  - "E.23"
keywords:
  - "configuration or adaptation work"
  - "declared result and guarantee"
  - "one selected apparatus"
  - "reuse horizon"
  - "setup cost"
  - "use-bounded apparatus application"
---

### C.19.2:12 - Relations

- **Coordinates with:** `C.18` for candidate generation and reframing; `C.19` for candidate/front stewardship; `C.19.1` for scale-amenable bearer preference; `C.22.1` for adaptation signatures; `E.23` for repeated improvement; and `C.31.ASAP` for architecture-scale preference.
- **Uses conditionally:** `C.11` only when an actual local-choice question over a live eligible set exists. It consumes, but does not extend, the four `ChoiceResult` dispositions.
- **Hands off enactment to:** `A.15.2` for work plans, `A.15.1` for dated work, and `C.24` only for tool-call enactment planning. The direct domain pattern owns the practical result.
- **Is specialized by:** the method described in `A.7.1`. That specialization always inherits declared use/result/guarantee/horizon, useful threshold, plan/work/result separation, stop, and reopen; it inherits the candidate/choice branch only when that branch is actually triggered. This is a method-description relation, not `U.SubkindOf` and not a world relation.
- **Does not replace:** durable U-kind admission in `E.24`/`E.24.UK`, parsimony in `A.11`, evidence and assurance owners, or any candidate's direct kind.

