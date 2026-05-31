---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:17"
section_title: "Problem-Card Use Invariants"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__018_problem-card-use-invariants.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:17 — Problem-Card Use Invariants"
line_start: 44390
line_end: 44402
dependencies:
  - "A.10"
  - "A.15"
  - "A.19"
  - "A.21"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.Q"
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

### C.22.2:17 - Problem-Card Use Invariants

These invariants govern use of one `ProblemCard@Context`; they do not add card fields.

| Invariant | Required reading |
|---|---|
| One card, one current problem-side representation | One `ProblemCard@Context` instance carries one problem-side representation under one declared context. If the represented problem changes, the card states the changed representation or exits to the representation pattern that carries the change. |
| No hidden companion records | A card may mature, but it does not fork into hidden `TaskSignature`, `WorkPlan`, evidence, gate, autonomy, archive, portfolio, selected-set, or mathematical adequacy records. |
| Heavy relations exit | Evidence, provenance, assurance, gate, autonomy, work, archive, selected-set, comparison, acceptance, representation-transition, temporal, causal, and mathematical adequacy authority stays with the receiving pattern that owns the live relation. |
| `P2W-ready` is problem-side readiness | `P2W-ready` means problem-side input ready, not work ready, not gate-passed, not method-selected, and not evidence-proved. |
| Stale or blocked cards need a disposition | A stale, unknown-blocked, changed-representation, or missing-basis card cannot silently remain `P2W-ready`; it states refresh, retirement, bounded use, `abstain/no-change`, or a named neighboring exit. |
| Smallest truthful card wins | The smallest card that gives an honest next move is sufficient. Full field completion is not required when a Thin card already gives the truthful next move. |

