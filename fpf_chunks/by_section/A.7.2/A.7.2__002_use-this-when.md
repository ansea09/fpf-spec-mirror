---
chunk_kind: "child"
pattern_id: "A.7.2"
pattern_title: "FPF Ontology-Premise Reconciliation"
section_id: "A.7.2:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7.2/A.7.2__002_use-this-when.md"
commit_sha: "423f9d3fef92bafec7b092b910e8ce056a0f607d"
heading_path:
  - "A.7.2 — FPF Ontology-Premise Reconciliation"
  - "A.7.2:0 — Use this when"
line_start: 27069
line_end: 27082
dependencies:
  - "A.10"
  - "A.7.1"
  - "A.7.2"
  - "A.7.CP"
  - "C.2.1"
  - "C.29"
  - "E.17"
  - "E.24.PUB"
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

Use this pattern when FPF clauses appear to give incompatible answers to the same ontology question or practical decision. A designer can compare a proposed rule with another rule before either has been used. A practitioner investigating disagreement between actual applications can trace the result of each to the clauses, premises and sources used. One material contradiction can warrant reconciliation.

First name the disputed claim and the use it must support. To test the rules, find conditions admitted by both and work out what each would conclude there. For a report of disagreement in practice, recover the actual conclusions in their respective circumstances. A difference of scope resolves the apparent conflict only where it removes the incompatible consequences.

**Not this pattern when.** A vocabulary difference, unlike source function, or different subject with no shared practical consequence is not a premise conflict. Use `A.7.1` for one engineering ontology defect, `F.19` for wording repair with `C.2.P`/`E.10` for a remaining semantic question, direct evidence-use or formal patterns for missing warrant, and source-currentness patterns for stale editions.

The primary reader is an FPF maintainer, architecture steward, or pattern author responsible for a material cross-pattern contradiction. The procedural content describes the reconciliation Method in §4. A `U.MethodDescription` assertion requires that admitted Method as the episteme's EntityOfConcern and A.3.2 membership.

For a claimed dated reconciliation `U.Work`, use A.13 for each actual performer and admit the occurrence under A.15.1. Apply F.6 to the relevant Work and assignment when attributing that Work under the assignment. A short result may omit an assignment identifier it does not use.

The pattern episteme, described Method, reader, performing System, any separately established assignment species and occurrence, optional attribution check, Work, source uses, and returned FPF decision remain distinct.

