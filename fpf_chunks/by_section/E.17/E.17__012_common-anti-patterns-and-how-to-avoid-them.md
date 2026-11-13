---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:10"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__012_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:10 — Common Anti-Patterns and How to Avoid Them"
line_start: 114541
line_end: 114553
dependencies:
  - "A.10"
  - "A.15.4"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.3.RT.OE"
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
    *Fix:* Keep every claim in the source ClaimGraph. When a reader needs to know how a claim arose, name the authoring, measurement, observation, model, source-use, representation, or refinement relation. Use the specification-use gate, CG-Spec, or KD-CAL when it owns the requirement. Keep views declarative. Publication adds **zero** claims.
2. **Publishing only endpoint faces.**
    *Fix:* The optional formal profile constructs faces for `g o f`, not only endpoint faces for `FaceObj_s(X)`, `FaceObj_s(Y)`, and `FaceObj_s(Z)`. A system performs the construction work.
3. **Unpinned numbers.**
    *Fix:* Recover the value’s required interpretation and support. Retain the material pins and add CG or CHR references only when the applicable rule or selected profile consumes them. Withhold a numeric use whose required basis remains missing.
4. **Face presented as a view without conformance.**
    *Fix:* Resolve the viewpoint episteme and apply E.17.0 to the candidate episteme; redesign or re-emit the face only after the semantic repair.
5. **`InteropCard` equivalent to `TechCard` duplication.**
    *Fix:* `InteropCard` can refine typing or shape but cannot contradict `TechCard` (reindexing monotone).

