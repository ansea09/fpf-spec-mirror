---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work: Dated Performed Work Occurrence"
section_id: "A.15.1:13.1"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__017_sota-echoing.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "A.15.1 — U.Work: Dated Performed Work Occurrence"
  - "A.15.1:13.1 — SoTA-Echoing"
line_start: 29505
line_end: 29516
dependencies:
  - "A.1"
  - "A.10"
  - "A.13"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "B.1.4"
  - "B.1.6"
  - "B.3"
  - "C.2.1"
  - "C.27.TA"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ROLE"
  - "E.17"
  - "F.6"
  - "U.Method"
  - "U.MethodDescription"
  - "U.ReferenceScheme"
  - "U.WorkPlan"
keywords:
  - "A.13-qualified actual performer U.System"
  - "F.6 only after admission for precise assignment-bound attribution"
  - "conditional agency profile"
  - "containing System"
  - "enacted Method"
  - "exact performance history"
  - "independent U.Work admission"
  - "optional direct bindings and resource use"
  - "separate result or consequence"
  - "temporal extent"
  - "world-side dated occurrence"
---

### A.15.1:13.1 - SoTA-Echoing


| Source tradition | Source reference and contribution | FPF use | Shortcut rejected |
| --- | --- | --- | --- |
| Occurrent and 4D occurrence ontology | [BFO 2020](https://raw.githubusercontent.com/BFO-ontology/BFO-2020/master/21838-2/owl/bfo-core.owl), standardized in [ISO/IEC 21838-2:2021](https://committee.iso.org/standard/74572.html), distinguishes occurrents and temporal parthood; [Partridge and de Cesare's 2013 BORO account](https://research.borosolutions.net/ontologydriven-reengineering-business-systems/) supplies the historical lineage of identifying individuals by spatiotemporal extent. | `U.Work` admits dated occurrence holons; each Work individual has its own temporal extent and participates in separately obtaining occurrence relations, while assertions and records about it remain separate epistemes. Parts, retries, resumptions, and overlaps stay explicit. | Treating a Method factor, diagram, system-role label, log entry, or record schema as the performed occurrence. |
| Object-centric event logging and process mining | The [OCEL 2.0 metamodel](https://vdaalst.com/slides/OCED-workshop-OCEL2-Oct2023.pdf) represents typed events, qualified event–object and object–object relations, and changing object attributes. The [OCEL 2.1 prerelease](https://www.ocel-standard.org/2.1/ocel20_specification.pdf) adds single-file CSV and bundled CSV/Parquet serializations. | For an event record, identify the candidate action and the particular claim its content supports. Several sources may jointly ground Work admission; the complete §4.1 basis must make the occurrence's A.1:4.2 construction, performance history, every actual performer's A.13 basis, enacted Method, temporal extent and local containing-system relation recoverable. Recover any relied-on object, binding, resource-use, interpretation or policy relation when the receiving claim needs it. Any precise assignment-bound attribution remains a separate later F.6 result. These admission conditions apply across serialization formats. | Treating the existence of telemetry or event rows as sufficient grounds for `U.Work` admission without inspecting the claims they support. |
| Observability and telemetry practice | [OpenTelemetry Specification 1.62.0](https://github.com/open-telemetry/opentelemetry-specification/blob/v1.62.0/specification/overview.md) for trace, metric and log representation. | Telemetry can support, replay, measure, or diagnose a claim about Work, but the occurrence still needs every actual performer's A.13 basis, independently grounded history, enacted Method, temporal extent, and local containing-system relation. Add F.6 only for a separately claimed precise assignment-bound attribution, and add another enactment, affected-referent, binding, or resource-use fact only when the receiving claim uses it. | Counting trace, metric, or log existence as the performed Work, a result, or dominance evidence without the direct evidence, comparison, or archive relation. |
| Provenance and evidence-provenance practice | [W3C PROV-O](https://www.w3.org/TR/prov-o/) is a 2013 Recommendation; the [2025 PROV-O and BFO alignment](https://www.nature.com/articles/s41597-025-04580-1) is a later interoperability contribution. | Assertions or descriptions about Work cite the evidence-provenance relations and currentness notes their use needs without letting evidence, assurance, gate, or provenance claims replace the occurrence. | Using a provenance relation, assurance statement, or gate result as if it were the performed Work. |
| Temporal-interval reasoning | [Allen's interval algebra](https://urresearch.rochester.edu/fileDownloadForInstitutionalItem.action?itemFileId=22361&itemId=10182) (1983) supplies qualitative relations among intervals; [W3C OWL-Time](https://www.w3.org/TR/2017/REC-owl-time-20171019/) (2017 Recommendation, §§3.1–3.4) represents these relations together with interval boundaries, durations and temporal reference systems. | A.15.1 supplies identified Work intervals, parts, and performed resource-use facts; use `B.1.4` for temporal aggregation and `B.1.6` for work-resource aggregation, each with its stated policy and admissible use. | Mixing union, hull, parent cost, child cost, and ordinal comparison on the Work object without a recovered Part B aggregation claim. |


