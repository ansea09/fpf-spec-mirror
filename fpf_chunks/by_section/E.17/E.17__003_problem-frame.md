---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:2"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__003_problem-frame.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:2 — Problem frame"
line_start: 82816
line_end: 82824
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

### E.17:2 - Problem frame

* Different readers often need different slices or presentations of the same accepted account, but a current task may need only one or two faces rather than the full quartet.
* Informal renderings can drift semantics, hide omissions, or sever source return; composite morphisms can also lose traceability when their publication claims are used compositionally.
* `PlainView`, `AssuranceLane`, and a packaged `viewpointRef` are easy to overread as `U.View` membership, assurance, or conformance even though none establishes those claims by itself.
* Exact publication identity, pins, carrier relations, and evidence references matter for some receiving uses, but putting all of them before the first readable face makes ordinary publication unnecessarily hard.

**MVPK** therefore starts from the current source, reader/use, and minimum useful face set. It then adds viewpoint conformance, E.24.PUB occurrence/form/carrier identity, pins, bridge records, evidence, or assurance only when a named use depends on those distinctions. The optional morphism profile retains the functorial publication discipline for Description epistemes, including Description epistemes admitted for specification use. **Part E is conceptual:** no machine-exchange formats are specified here.

