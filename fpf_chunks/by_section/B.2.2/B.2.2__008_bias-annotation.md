---
chunk_kind: "child"
pattern_id: "B.2.2"
pattern_title: "Meta-System Transition - System Specialization of MHT"
section_id: "B.2.2:5.1"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.2/B.2.2__008_bias-annotation.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "B.2.2 — Meta-System Transition - System Specialization of MHT"
  - "B.2.2:5.1 — Bias-Annotation"
line_start: 37886
line_end: 37895
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2.1"
  - "A.2.2"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "B.1.2"
  - "B.2"
  - "B.2.4"
  - "B.2.5"
  - "B.3"
  - "B.3.5"
  - "C.13"
  - "C.16"
  - "C.27"
  - "C.30"
  - "C.30.ASV"
  - "C.30.TFS-REL"
  - "E.24.UK"
keywords:
---

### B.2.2:5.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Named aggregate as system | A fleet, platform, or cell name is treated as system recognition. | Apply B.2 to one exact candidate; require the complete A.1 criterion and the direct `U.System` criterion. |
| Component evidence transfer | Component certificates are read as assurance for the proposed new whole after its recognition under `U.System`. | Re-test each claim against that exact recognized system and use exact evidence or assurance relations; do not transfer support by label. |
| Coordination as whole | A controller, protocol, or coordination relation is treated as automatic system MHT. | Recover the obtaining relation, then require B.2 whole reidentification plus complete A.1 and `U.System` recognition; keep any support separate. |
| Description as system | Dashboard, simulation, model, twin, or bill is treated as the operating system. | Use episteme, publication, source-use, and architecture-description owners for description objects. |
| Transformation as containment | An external system changes a holon and is treated as its part or containing whole without a separately obtaining part-whole relation. | Use A.12, A.3.4, A.15.1, B.2.5, and part-whole owners separately. |

