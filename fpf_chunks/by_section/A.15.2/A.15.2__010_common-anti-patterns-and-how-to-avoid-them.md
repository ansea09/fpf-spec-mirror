---
chunk_kind: "child"
pattern_id: "A.15.2"
pattern_title: "U.WorkPlan"
section_id: "A.15.2:7b"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.2/A.15.2__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "A.15.2 — U.WorkPlan"
  - "A.15.2:7b — Common Anti-Patterns and How to Avoid Them"
line_start: 25045
line_end: 25057
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.3"
  - "A.15.4"
  - "A.15.5"
  - "A.2.1"
  - "A.2.2"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "A.6.5"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.1.4"
  - "B.1.6"
  - "B.3"
  - "C.2.1"
  - "C.32.P2S"
  - "E.17"
  - "E.24"
  - "E.24.UK"
  - "F.9"
  - "U.Method"
  - "U.MethodDescription"
  - "U.RoleAssignment"
  - "U.Work"
keywords:
  - "PlanItem content"
  - "horizon"
  - "intended-work episteme"
  - "no actuality by plan"
  - "performer and capability conditions"
  - "positive or governed-negative local fulfilment assertion"
  - "possible future performance"
  - "present EntityOfConcern"
  - "reusable predicate semantics"
  - "variance"
---

### A.15.2:7b - Common Anti-Patterns and How to Avoid Them

- **Future-work-as-entity.** Do not use a possible future performance or PlanItem designator as C.2.1's already identified EntityOfConcern or as a dated Work occurrence; keep it in plan claim content until an exact direct entity or occurrence exists.
- **Plan-as-actual.** Do not treat a Gantt bar, Kanban ticket, shift rota, or calendar booking as performed work; create or cite an exact Work occurrence admitted under `U.Work` only when A.15.1's occurrence basis is present.
- **Workflow-as-schedule.** Do not treat a method description or flowchart as a plan; make a `U.WorkPlan` only when present subject, intended-performance designator, horizon, window, constraints, performer or role conditions, and baseline are current.
- **Assignment-or-capability-by-plan.** Do not treat an intended holder, role, threshold, or capability reference as an obtaining `U.RoleAssignment`, capability instance, or fit result for later Work; apply A.2.1/A.2.2 at the exact interval and use.
- **Budget-as-cost.** Do not book planned budgets as performed resource use; establish performed facts on exact A.15.1 Work and any aggregate ledger or allocation under B.1.6.
- **Plan-shape overreach.** Do not force performed Work to match plan decomposition, infer non-fulfilment from a missing link or unavailable facts, or mint a fulfilment relation from a local comparison. Stop at a positive or governed-negative local compound assertion when it suffices; use a predicate-definition episteme for repeated semantics without occurrence identity; open relation-kind admission only for a named occurrence-facing need.
- **Context-bridge overreach.** Do not bridge contexts as wholes or use F.9 to convert planned values, commitments, criteria, or verdicts. F.9 relates exact `SenseCell` values and only grants its stated admitted use.
- **Evidence-note-as-claim.** Do not treat evidence-reference notes, gate-preparation notes, or source-currentness requests as evidence, gate passage, assurance, or release authorization.
- **Description-as-planned-filling.** Do not turn a method-description phrase such as input or output into a planned slot. Use A.15.3 only against one exact governed declaration member whose direct pattern owns the member's reusable meaning and corresponding later actual-use predicate, while A.15.2/A.15.3 own the intended-use claim; otherwise keep ordinary plan content or return the exact missing-governor blocker.
- **Expected-as-actual.** Do not treat a desired filling, expected effect, output, result, outcome, deliverable, or handoff as an actual participant, change, returned value, produced entity, delivery, acceptance, or downstream effect.

