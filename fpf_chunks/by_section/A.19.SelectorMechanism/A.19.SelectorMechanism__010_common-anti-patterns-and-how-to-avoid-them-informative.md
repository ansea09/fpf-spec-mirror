---
chunk_kind: "child"
pattern_id: "A.19.SelectorMechanism"
pattern_title: "Selection Kernel"
section_id: "A.19.SelectorMechanism:8"
section_title: "Common Anti-Patterns and How to Avoid Them — informative"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SelectorMechanism/A.19.SelectorMechanism__010_common-anti-patterns-and-how-to-avoid-them-informative.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "A.19.SelectorMechanism — Selection Kernel"
  - "A.19.SelectorMechanism:8 — Common Anti-Patterns and How to Avoid Them — informative"
line_start: 41047
line_end: 41063
dependencies:
  - "A.19.CHR"
  - "A.19.CN"
  - "A.19.CPM"
  - "A.19.ULSAM"
  - "A.19.USCM"
  - "A.6.0"
  - "A.6.1"
  - "C.22"
  - "E.18"
  - "G.0"
  - "G.5"
keywords:
  - "ComparisonResultSlot"
  - "SelectEligibility"
  - "SelectorMechanism"
  - "explicit criteria"
  - "finite basis of binary CPM applications"
  - "pass/degrade/abstain"
  - "required comparison coverage"
  - "selected candidate set"
  - "selection kernel"
---

### A.19.SelectorMechanism:8 - Common Anti-Patterns and How to Avoid Them — informative

| Anti-pattern                 | What it looks like                                                              | Remedy                                                                                                                                              |
| ---------------------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| GateDecision leakage | `Select` emits `GateDecision` or writes a decision log | Keep gate decisions in their governing patterns. `SelectEligibility` remains the mechanism predicate; the application retains its realized eligibility value and replay basis. |
| Forced single winner | `Select` always returns exactly one candidate even under incomparability | Return a declared selected set. If a singleton is required, state the choice rule in `CriteriaSlot` and derive that result from the admitted comparison basis; any ordering used must be declared and admissible. |
| Hidden tie-breakers          | “If incomparable, pick lower cost” without declaring that as policy             | Move tie-breakers into explicit criteria or into declared comparator policies; never embed inside the kernel                                        |
| Scalarization by convenience | Replace set-valued comparison with a scalar “summary score” treated as decisive | Keep summaries report-only unless declared as admissible comparator outputs                                                                  |
| Unknown coerced to pass      | Missing evidence treated as acceptable                                          | Use tri-state `SelectEligibility`; unknown maps to `degrade` or `abstain`                                                                           |
| Selection does comparison    | Selection stage recomputes scoring or comparison internally                     | Keep comparisons upstream; `SelectorMechanism` binds CPM applications and consumes only their justified-token union in `ComparisonResultSlot` |
| One binary comparison treated as a batch | One `Compare(left,right)` application is said to cover three or more candidates, or a token union loses its producing applications | Bind a finite basis of binary CPM applications, derive required pair coverage from the selection conditions, and trace every consumed token to a member output |
| Selected set as replay record | Candidate universe, comparison ref, criteria, scope, evidence, or currentness are placed inside `SelectionSlot` | Keep `SelectionSlot` to selected candidates; bind use arguments on the application and use evidence, provenance, and currentness relations |
| Boundary drift | Selection reuses a token union after comparison-basis membership, coverage, member pair or eligibility, predicate, scope, selected slices, plane, or window changed | Treat it as another selection application and perform the required binary comparisons again when their governed basis changed |
| Publish inside selection | Selection emits a publication or telemetry relation as part of mechanism semantics | Keep publication and telemetry under their governing patterns; application bindings and applicable relations retain replay |

---

