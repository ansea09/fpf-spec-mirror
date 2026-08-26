---
chunk_kind: "child"
pattern_id: "E.24.PUB"
pattern_title: "Ontic Description and Publication Discipline"
section_id: "E.24.PUB:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.PUB/E.24.PUB__013_sota-echoing.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "E.24.PUB — Ontic Description and Publication Discipline"
  - "E.24.PUB:11 — SoTA-Echoing"
line_start: 88814
line_end: 88825
dependencies:
  - "A.6.3"
  - "A.6.REL"
  - "C.2.1"
  - "C.29"
  - "C.30.AD"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.21"
  - "E.24"
  - "E.24.CD"
  - "E.24.UK"
  - "E.8"
  - "E.9.DA"
  - "F.19"
  - "U.EpistemePublication"
  - "U.View"
keywords:
---

### E.24.PUB:11 - SoTA-Echoing

| Source family | Decision-changing lesson | Adoption in this pattern | Practical implication |
| --- | --- | --- | --- |
| Modular ontology design patterns, including [Shimizu and Hitzler 2024](https://arxiv.org/abs/2411.09601) and [Eells, Dave, Hitzler, and Shimizu 2024](https://arxiv.org/abs/2402.18715) | Reusable ontology structure and the documentation or form through which it is encountered are different governed objects. | Separate the subject ontic, its description episteme, and the publication relations instead of making a reusable form the ontology. | In the inspection-card case, a layout repair does not force a pump-ontology repair. |
| [Norouzi, Hertling, Waitelonis, and Sack 2025](https://arxiv.org/abs/2509.23776) | Process-like forms can carry implicit ontology that domain experts need to recover explicitly. | Classify the claims and relations carried by a card or workflow-shaped expression before assigning publication use. | A workflow diagram can reveal an ontic candidate without becoming that ontic by notation. |
| [Nayyeri et al. 2025](https://arxiv.org/abs/2506.01232), and [Oyewale and Soru 2026](https://arxiv.org/abs/2602.01276) | Schemas and knowledge-graph pipelines help recover structure but also encourage schema or serialization overread. | Keep filled claim objects, reusable forms, C.29 representations, carriers, and publication occurrences distinct. | A table migration can change representation or carrier while preserving the published episteme edition. |
| OWL, SKOS, RDF, and triple-store practice | Labels, axioms, serializations, documents, and queries have different functions even when one tool exposes them together. | Use this lineage as an expression and implementation stress test, not as authority to identify ontology with serialization. | Tool export does not settle the kind of the exported subject or the truth of its claims. |
| FPF `C.2.1`, `A.6.REL`, `A.6.3`, `C.29`, `E.17`, and `E.24.UK` | Current FPF already separates episteme identity, direct relation identity, view membership, representation, publication use, and U-kind admission. | `E.24.PUB` coordinates those subject patterns through one publication relation and two supporting relations; it does not duplicate their identity rules. | The architecture diagram case can be repaired at the exact changed relation without reopening architecture ontology. |

Smallest currentness trigger: reopen this source use when a newer ontology-publication or knowledge-representation line changes the distinction among claim-bearing episteme, view, publication form, representation, carrier, and availability relation. A new file format or storage tool alone does not trigger reopening.

