---
chunk_kind: "child"
pattern_id: "E.4"
pattern_title: "FPF Ecosystem Family Architecture"
section_id: "E.4:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4/E.4__012_sota-echoing.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "E.4 — FPF Ecosystem Family Architecture"
  - "E.4:11 — SoTA-Echoing"
line_start: 67694
line_end: 67706
dependencies:
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.1"
  - "E.11"
  - "E.11.DSG"
  - "E.11.PFP"
  - "E.11.PUR"
  - "E.17"
  - "E.19"
  - "E.2"
  - "E.2.DA"
  - "E.21"
  - "E.23"
  - "E.24.PUB"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.4.FPF"
  - "E.4.PFAD"
  - "E.4.PFR"
  - "E.5.3"
  - "E.9"
  - "F.18"
  - "G.11"
  - "G.2"
  - "G.5"
keywords:
---

### E.4:11 - SoTA-Echoing

| Claim | Exact source ref and status | Pattern locus changed | Adoption status |
| --- | --- | --- | --- |
| Product and service are management-relevant output distinctions, but their labels do not settle every direct subject in a framework ecosystem. | `ISO 9000:2026, Quality management - Fundamentals and vocabulary`, current fifth edition, `https://www.iso.org/standard/9000`. It distinguishes an organizational product output from a service whose delivery necessarily includes provider-customer activity. | Section 4.1 declares *product* to be Plain management wording and requires the direct subject and relation before a technical claim; `CC-E4.8` repeats that test. | **Adapt** the inexpensive product-versus-service question when it changes provision or maintenance. **Reject** the QMS vocabulary as a universal FPF ontology and do not require a quality-management system merely to place one support unit. |
| A maintained service, its provider, and the system used to manage its life cycle are different concerns. | `ISO/IEC 20000-1:2018, Information technology - Service management - Part 1: Service management system requirements`, confirmed current in 2023 with Amendment 1:2024, `https://www.iso.org/standard/70636.html`. It separates the organization and service-management system from the services planned, delivered, and improved. | The programme paragraph names provider and maintaining Systems, accepted commitments, any admitted service state, bounded Work, and result epistemes separately. | **Adapt** provider, service-life-cycle, and continual-maintenance distinctions for an actual access or inquiry service. **Reject** an IT-service scope and full service-management system for a bounded publication or guide; that effort is justified only by the selected service claim. |
| Publication identity, expression, issued manifestation, physical or digital item, and aggregation should not be collapsed into one carrier. | `IFLA Library Reference Model`, July 2024 maintained edition, `https://repository.ifla.org/handle/20.500.14598/40.2`. Its Work-Expression-Manifestation-Item relations and aggregate treatment make publication-level identity and embodiment explicit. | Sections 4.1 and 4.2 keep edition, publication unit, snapshot, projection, carrier, and neutral combined exposure separate. | **Adapt** the identity-versus-embodiment and aggregate-versus-component discipline for framework publications. **Reject** bibliographic entities as the ontology of services, programmes, Systems, or Methods; applying the full cataloguing model would add effort without answering those boundaries. |
| Reusable user and service information benefits from an explicit content boundary, life-cycle management, and tool-independent assembly. | `ISO/IEC/IEEE 26531:2023, Systems and software engineering - Content management for product life cycle, user and service management information for users`, current second edition, `https://www.iso.org/standard/81703.html`. | Section 4.1 groups support publication units by shared use, edition, access, maintainer, and cadence, while independent content gets its own exact edition or state and snapshot return. | **Adapt** the content-selection, reuse, maintenance, and multi-output discipline when the information scale warrants it. **Reject** a component-content system or complete software-documentation process as the default; a separately stored unit is not automatically a separate product. |
| Architecture descriptions separate architecture expression from the architecture and require concern, view, viewpoint, correspondence, and rationale discipline. | `ISO/IEC/IEEE 42010:2022, Software, systems and enterprise - Architecture description`, official current standard ref, `https://www.iso.org/standard/74393.html`. | `Solution` distinguishes the ecosystem-architecture record from publication carriers; `Common Anti-Patterns` repairs publication-only architecture; `Relations` cites the exact neighboring assertions and subject-pattern locators in `C.30`, `C.33`, `C.34`, `E.11`, and `E.17`. | Adopt the separation and correspondence discipline; adapt it to selected structures of a holonic FPF pattern ecosystem. |
| Reuse across related family members needs reusable core assets, variation, adoption, tooling, and evolution discipline. | Nazar, `Software Product Line Engineering: Adoption, Tooling and AI Era Challenges`, arXiv:2605.21353, 2026 current survey and reopen trigger for stronger post-2026 SPLE synthesis, `https://arxiv.org/abs/2605.21353`. | Family table separates FPF Core, domain frameworks, and local frameworks; `E.5.3` dependency direction is made a conformance check. | Adapt reusable-core and variation discipline; reject feature-model or software-product ontology as universal FPF architecture. |
| Pattern ecosystems need validation, worked cases, and relation clarity rather than recipe-book pattern lists. | Riehle, Harutyunyan, Barcomb, `Pattern Discovery and Validation Using Scientific Research Methods`, arXiv:2107.06065, 2021 current validation-practice source; Iba, `Pattern Languages as Media for the Creative Society`, arXiv:1308.1178, lineage for pattern-language social use. | `Archetypal Grounding` now includes a filled ecosystem-architecture record; `Conformance Checklist` and anti-pattern rows require source-return, exact relation definitions, and explicit repair conditions. | Adopt validation and example pressure; adapt it through `E.21`, `E.23`, worked slices, and near-miss repairs. |
| Relation-rich architecture should be stated as constraints rather than read as performed-work order. | `Dyad 3.3`, current release dated 2026-08-06, `https://help.juliahub.com/dyad/stable/manual/changelog.html`, with current syntax and analysis documentation at `https://help.juliahub.com/dyad/stable/manual/syntax.html` and `https://help.juliahub.com/dyad/stable/manual/analyses.html`. Dyad components carry variables, parameters, connectors, subcomponents, and relations, while analyses are separate workflows that produce solutions or artifacts. `Modelica Language Specification 3.7`, 2026, `https://specification.modelica.org/maint/3.7/MLS.html`, is retained only as historical declarative/acausal lineage and is intentionally not used as the current SoTA comparator. | Boundary wording in `Solution`, `Rationale`, and `E.4.PFR` keeps relation assertions declarative and separates them from dated Work and its results. | **Adapt** Dyad's separation between relation-rich component description and analysis that produces results. **Reject** its physical-model, equation, solver, simulation, component-language, and analysis ontology for FPF; reject Modelica as the current SoTA basis. |

