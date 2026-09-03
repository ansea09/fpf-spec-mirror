---
chunk_kind: "child"
pattern_id: "E.4.PFIP"
pattern_title: "Principle-Framework Publication Integration and Preservation"
section_id: "E.4.PFIP:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFIP/E.4.PFIP__012_sota-echoing.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "E.4.PFIP — Principle-Framework Publication Integration and Preservation"
  - "E.4.PFIP:11 — SoTA-Echoing"
line_start: 72528
line_end: 72540
dependencies:
  - "C.2.1"
  - "C.33"
  - "C.34"
  - "E.11"
  - "E.17"
  - "E.24.PUB"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.4.FPF"
  - "E.4.PFIP"
  - "E.8"
keywords:
---

### E.4.PFIP:11 - SoTA-Echoing

| Current source branch and reference | Working lesson | Adoption in this pattern | Boundary |
| --- | --- | --- | --- |
| Semantic merge: Da Silva, Borba, Maciel et al. (2024), [“Detecting semantic conflicts with unit tests”](https://doi.org/10.1016/j.jss.2024.112070) | Current empirical semantic-merge work shows that textual and structured merge can succeed while an unwanted semantic change remains; the reported method uses behavior-relevant tests as partial specifications. | **Adapt.** The Solution does not treat build or text-diff success as preservation evidence and requires a use-relevant inventory with explicit loss outcomes. | Software tests are not imported as a universal framework-publication check; each publication form supplies its own comparison basis. |
| Transformation traceability and versioned co-evolution: Höppner and Tichy (2024), [“Traceability and reuse mechanisms, the most important properties of model transformation languages”](https://doi.org/10.1007/s10664-023-10428-2), and Homolka, Marchezan, Assunção et al. (2026), [“What really happened to my models?”](https://doi.org/10.1007/s10664-025-10773-4) | The empirical survey identifies traceability and reuse as leading transformation-language capabilities while showing that their effects vary with use and scale. The later evaluated approach retains complete model and metamodel histories, links model changes to the changes that caused them, and permits several versions to coexist. | **Adapt.** Source contributions, predecessor content, and selected structures keep explicit candidate correspondences; source incorporation does not replace predecessor preservation; and pair results may be reused inside a larger allocation without replacing it. | The survey measures transformation-language practice, and the later approach evaluates model co-evolution. Neither establishes complete traceability for a framework publication. This pattern adds no transformation language, operation history, automatic correspondence claim, or generic traceability relation. |
| Reusable model migration: Bettini, Di Salle, Iovino, and Pierantonio (2024), [“Supporting reusable model migration with Edelta”](https://doi.org/10.1016/j.jss.2024.112012) | Changes to a metamodel can invalidate dependent artifacts. The evaluated approach reuses migration patterns across domains while retaining custom or interactive rules for changes that automatic migration cannot settle. | **Adapt.** One reusable comparison method covers FPF, DPF, and LPF; the pattern that defines or constrains a publication form supplies its form-specific inventory, and a changed public interface brings its direct consumers into the candidate. | The Edelta language, metamodel kinds, automatic copier, and model-migration operations are not imported into FPF publication ontology. |
| Digital-preservation planning: the current [NARA Digital Preservation Framework](https://www.archives.gov/preservation/digital-preservation/risk), its [structured-data preservation guidance](https://www.archives.gov/preservation/digital-preservation/linked-data/structureddata), and Becker (2018), [“Metaphors We Work By”](https://archivaria.ca/index.php/archivaria/article/view/13628) | NARA selects significant properties by record type and uses them as transformation-test criteria while stating that its plans are not exhaustive or universal. Becker shows why bits, records, computed performances, and preservation claims cannot be collapsed into one digital-object metaphor. | **Adapt.** The applicable FPF pattern defines or constrains the inventory basis, the maintainer selects the inventory for the declared use, and edition, content, form, carrier, and publication occurrence remain separate. | NARA record categories and archival authenticity terms are not imported as FPF kinds or as one universal significant-property list. |

These traditions support one shared stance: compare the properties and correspondences that matter for the declared use, not the easiest visible proxy. The semantic-merge row disciplines the one-to-one text case; the traceability and migration rows discipline the split-form case and direct-consumer closure; and the preservation row disciplines the diagram case and the separation of edition, form, content, and carrier. The method adapts that stance to principle-framework publications and keeps its scope narrower than general software merge, data migration, or digital preservation.

Reopen this source use when current publication-preservation or structured-transformation practice supplies a cheaper complete semantic comparison, shows that trace reuse can replace rather than only support allocation traversal, or demonstrates a non-framework use that warrants a broader pattern scope.

