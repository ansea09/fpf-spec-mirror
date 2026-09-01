---
chunk_kind: "child"
pattern_id: "A.7.2"
pattern_title: "FPF Ontology-Premise Reconciliation"
section_id: "A.7.2:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7.2/A.7.2__002_use-this-when.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "A.7.2 — FPF Ontology-Premise Reconciliation"
  - "A.7.2:0 — Use this when"
line_start: 21971
line_end: 21980
dependencies:
  - "A.10"
  - "A.7.1"
  - "A.7.2"
  - "A.7.CP"
  - "C.2.1"
  - "C.29"
  - "E.17"
  - "G.11"
keywords:
  - "actual source-use relations"
  - "context split"
  - "dated FPF applications"
  - "exact used clauses and premises"
  - "optional convergence"
  - "result claims or decisions"
  - "same receiving claim or consequence"
---

### A.7.2:0 - Use this when

Use this pattern when two or more dated applications of current FPF methods or patterns yield ontology-claim or decision epistemes whose claims or practical consequences cannot jointly support the same receiving claim or consequence in the same scope. Trace each result to the exact pattern or method clauses, premises, and accepted source-use occurrences that the application actually used; a difference between texts alone is not a conflict. One material contradiction is enough; recurrent conflict is not required.

The first useful move is to name the smallest receiving ontology claim and, for each dated application, the result claim or decision, the practical consequence it would support, and the exact clause, premise, or source use on which it relied. If the result claims or consequences differ by scope, stop with a context split instead of forcing agreement.

**Not this pattern when.** A vocabulary difference, unlike source function, or different subject with no shared practical consequence is not a premise conflict. Use `A.7.1` for one engineering ontology defect, `C.2.P`/`E.10` for wording use, direct evidence-use or formal patterns for missing warrant, and source-currentness patterns for stale editions.

The primary reader is an FPF maintainer, architecture steward, or pattern author responsible for a material cross-pattern contradiction. This pattern is a `U.MethodDescription` episteme that describes a `U.Method`. For any precise dated reconciliation `U.Work`, use A.13 to identify the actual performer System and let A.15.1 independently admit the occurrence. If the case or receiving result must also identify the assignment under which the reconciliation Work was performed, check that relation separately through F.6 against the assignment used by A.13. A short result may omit an assignment identifier it does not use; no unused assignment or attribution is presumed. The pattern episteme, described Method, reader, performing System, any separately established assignment species and occurrence, optional assignment check, Work, source uses, and returned FPF decision remain distinct.

