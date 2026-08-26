---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__003_problem.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:2 — Problem"
line_start: 100741
line_end: 100753
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.1"
  - "A.2.4"
  - "A.6.1"
  - "B.1.6"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.17"
  - "E.18"
  - "E.18.2"
  - "F.10"
  - "F.6"
  - "F.9"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.9"
keywords:
  - "EvidenceGraph"
  - "NotCarried"
  - "PathCitationRecord"
  - "PathId"
  - "PathSliceId"
  - "actual-use relation"
  - "direct governors"
  - "downstream work"
  - "exact direct relations"
  - "exact represented objects"
  - "local refresh"
  - "obtaining claims"
  - "provenance ledger"
  - "representation correspondence"
  - "source/currentness"
  - "unresolved gaps"
---

### G.6:2 - Problem

Large projects often need to cite a chain that crosses measurement, evaluation, aggregation, production, publication, and later use. The chain becomes unsafe when the graph is allowed to supply facts missing from the governed objects.

The common failures are:

1. **Edge-to-fact inversion.** A drawn edge is treated as proof that work, participation, production, measurement, evaluation, or use occurred.
2. **Generic relation fallback.** Labels such as `verifiedBy`, `validatedBy`, `measuredBy`, `producedByWork`, or `evidences` replace the exact direct relation and its governor.
3. **Result collapse.** Subject result, result episteme, carrier, outcome, assurance, and later decision become one generic result node.
4. **Declaration-to-runtime collapse.** A `MethodDescription`, operation signature, policy, clause, or plan is read as an actual run and its bindings.
5. **Hidden crossing.** A path silently crosses context, reference plane, edition, source order, or currentness window.
6. **Refresh fanout.** One changed source or relation forces a global rerun because the smallest affected path slice cannot be found.

