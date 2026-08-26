---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:10"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__012_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:10 — Common Anti-Patterns and How to Avoid Them"
line_start: 80600
line_end: 80612
dependencies:
  - "A.10"
  - "A.15.4"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.2"
  - "A.6.3"
  - "A.6.9"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.10"
  - "E.10.D2"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.17.AUD"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.24.PUB"
  - "E.8"
  - "F.9"
  - "F.9.1"
  - "U.View"
keywords:
---

### E.17:10 - Common Anti-Patterns and How to Avoid Them

1. **“Presentation logic” as semantics.**
    *Fix:* Keep every claim in the source ClaimGraph. When a reader needs to know how a claim arose, name the exact authoring, measurement, observation, model, source-use, representation, or refinement relation. Use an exact specification-use gate, CG-Spec, or KD-CAL when it owns the requirement; keep views declarative; publication adds **zero** claims.
2. **Publishing only view objects.**
    *Fix:* The optional formal profile constructs faces for `g o f`, not only endpoint faces for `FaceObj_s(X)`, `FaceObj_s(Y)`, and `FaceObj_s(Z)`. A system performs the construction work; MVPK does not act.
3. **Unpinned numbers.**
    *Fix:* Reject card; supply **pins** plus CG and CHR references.
4. **Face presented as a view without conformance.**
    *Fix:* Resolve the exact viewpoint episteme and apply E.17.0 to the exact candidate episteme; redesign or re-emit the face only after the semantic repair.
5. **`InteropCard` equivalent to `TechCard` duplication.**
    *Fix:* `InteropCard` can refine typing or shape but cannot contradict `TechCard` (reindexing monotone).

