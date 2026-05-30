---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:22"
section_title: "First Practical Entry Support"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__023_first-practical-entry-support.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:22 — First Practical Entry Support"
line_start: 44199
line_end: 44236
dependencies:
  - "A.10"
  - "A.15"
  - "A.19"
  - "A.21"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "A.6.Q"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.2.P"
  - "C.22"
  - "C.22.1"
  - "C.24"
  - "C.25"
  - "C.27"
  - "C.28"
  - "C.29"
  - "E.10"
  - "E.16"
  - "E.17"
  - "E.17.ID.CR"
  - "E.18"
  - "E.2"
  - "E.9"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "P2W-ready"
  - "Thin problem card"
  - "first-principles cue"
  - "freshness and unknown disposition"
  - "problem card"
  - "problem signal"
  - "problem-side record"
  - "safe-probe-needed"
  - "setContextRef"
  - "support posture"
  - "validation boundary"
---

### C.22.2:22 - First Practical Entry Support
This section is discoverability support only. It helps a practitioner or assistant find a candidate pattern; it does not prescribe a transition sequence and does not require opening `C.22.2` for every problem-sounding text.

These likely practitioner entry phrases point to `C.22.2`:

- "We have a problem, but it is not yet clear what work should be done."
- "This looks like a ticket, but I am not sure the problem is stated."
- "A signal or anomaly keeps recurring before method selection."
- "We selected this candidate from a front, archive, pool, or selected set, but need to state why it is a problem now."
- "P2W would otherwise receive 'implement X'."
- "There is a symptom, but we do not yet know what to solve."
- "We need to know whether this problem is ready for P2W or should exit elsewhere."

Tempting wrong first patterns:

- Do not start at `C.11` if the live issue is not yet a local choice among available options.
- Do not start at `C.16` or `A.19` if the live issue is not only measurement, characterization, or indicator admissibility.
- Do not start at `C.18`, `C.19`, or `G.5` if the live object is one selected singleton problem card rather than the archive, pool, front, or selected-set object.
- Do not start at `A.15` if no method or work plan is ready.
- Do not start at `A.10`, `G.6`, or `B.3` if evidence, provenance, or assurance is not the center.
- Do not start at `A.21` or `E.16` if no gate or autonomy authority is being decided.

Not `C.22.2` anti-cases:

- "The method is accepted; now schedule the work." Use `A.15`.
- "We need proof this result is reliable." Use `A.10`, `G.6`, or `B.3`.
- "Which option should we choose among explicit options?" Use `C.11`, or `G.5` when set publication or selected-set semantics are live.
- "Can the agent call the tool?" Use `C.24`, `E.16`, or `A.21`; `ProblemCard@Context` may only name the problem-side cue or exit and does not grant tool-call, autonomy, or gate authority.
- "This is ordinary discussion with no downstream project-side move." Do not use `C.22.2`.

First-use Thin-card test:

Given a messy signal, a practitioner must be able to produce a Thin `ProblemCard@Context` in under one page and correctly choose one admissible next move: `P2W-ready`, characterize, compare or parity, search or pool, refresh, retire, `abstain/no-change`, or named neighboring-pattern exit.

Entry relation:

The entry relation is local: `C.22.2` is introduced under `C.22`, and `C.22` names the `ProblemCard@Context` relation. The `C.22.2` body carries the Problem frame, first-entry phrases, tempting-wrong-pattern boundaries, and first-use Thin-card test needed for ordinary discovery.

