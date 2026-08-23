---
chunk_kind: "child"
pattern_id: "E.4.PFAD"
pattern_title: "Principle-Framework Architecture Decision"
section_id: "E.4.PFAD:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFAD/E.4.PFAD__012_sota-echoing.md"
commit_sha: "5801dc610c657ac7b1efee349b18e80ce6d7df6f"
heading_path:
  - "E.4.PFAD — Principle-Framework Architecture Decision"
  - "E.4.PFAD:11 — SoTA-Echoing"
line_start: 68143
line_end: 68162
dependencies:
  - "A.15.1"
  - "A.22"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.1.5"
  - "C.30.AD"
  - "C.30.STRAT"
  - "C.32.ADR"
  - "C.32.MWA"
  - "C.32.PAD"
  - "C.36"
  - "E.11.DSG"
  - "E.17"
  - "E.19"
  - "E.21"
  - "E.23"
  - "E.23.CDI"
  - "E.24.PUB"
  - "E.4"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.4.PFR"
  - "E.9"
  - "F.18"
  - "G.11"
  - "G.2"
keywords:
---

### E.4.PFAD:11 - SoTA-Echoing

| Claim | Source and status | FPF use |
| --- | --- | --- |
| A family architecture needs a boundary for common and variable material, separate from a one-off result. | `ISO/IEC 26550:2015, Software and systems engineering - Reference model for product line engineering and management`, current confirmed edition, `https://www.iso.org/standard/69529.html`; and `ISO/IEC 26552:2019, Tools and methods for product line architecture design`, confirmed current in 2025, `https://www.iso.org/standard/43111.html`. The latter separates domain and application architecture design for a family rather than one system. | **Adapt** the family-versus-single-result question, common-use boundary, variation, and lifecycle comparison when splitting or merging a DPF is live. **Reject** software-product ontology, feature machinery, and the 61-page method-and-tool burden as a DPF threshold; practitioner problem families, first use, evidence, and maintenance still decide. |
| Product-line scoping practice compares product, domain, and asset boundaries together with technical and organizational constraints rather than treating one current slice as the field. | Marchezan de Paula et al., `Software product line scoping: A systematic literature review`, Journal of Systems and Software 186, 2022, `https://doi.org/10.1016/j.jss.2021.111189`. The review analyzes 58 studies and 41 approaches and derives a generic scoping process while reporting differing contexts and limits. | **Adapt** the same-grain comparison of field promise, reusable contributions, alternatives, organizational conditions, and evidence limits. **Reject** software assets, feature scope, or the generic SPL process as the ontology or mandatory method of a DPF; practitioner problems and use still decide. |
| An architecture description can cover products, product lines, families, and business domains while remaining distinct from the architecture and from architecting methods. | `ISO/IEC/IEEE 42010:2022, Software, systems and enterprise - Architecture description`, current edition, `https://www.iso.org/standard/74393.html`. | **Use only as a boundary comparator:** keep the field or product architecture, the description that expresses it, and the Work and Methods that create or use it separate. **Reject** ISO 42010 as the starting ontology, an authoring Method, or evidence that a DPF field boundary is adequate. |
| Pattern discovery and validation need field evidence beyond a broad name or a rule-of-three count. | Riehle, Harutyunyan, and Barcomb, `Pattern Discovery and Validation Using Scientific Research Methods`, 2021, `https://arxiv.org/abs/2107.06065`. It compares qualitative survey, action research, and case-study evidence and reports three exploratory studies. Chuprina et al., `Towards an Approach to Pattern-based Domain-Specific Requirements Engineering`, 2024, `https://arxiv.org/abs/2404.17338`, is a current academia-industry proof of concept and explicitly reports that the domain-specific pattern approach is a first attempt. | **Adapt** domain evidence, representative cases, explicit limits, and the question of what domain specificity changes. **Reject** a count as validation and do not require a full research programme for the cheap exit; the 2024 line is promising evidence, not authority for one universal field grammar. |
| Product and service management distinctions can expose different provider, interaction, currentness, and maintenance questions without creating one Product kind. | `ISO 9000:2026`, current quality-management vocabulary, `https://www.iso.org/standard/9000`; and `ISO/IEC 20000-1:2018`, confirmed current in 2023 with Amendment 1:2024, `https://www.iso.org/standard/70636.html`; compared by value in `E.4:11`. | **Adapt** the product-versus-service probe only when it changes a selected alternative, and separate provider and maintaining Systems from the service. **Reject** QMS vocabulary and a full service-management system as FPF ontology or default PFAD payload. |
| Publication and content architecture distinguish edition, expression, carrier, aggregation, content boundary, and lifecycle management. | `IFLA Library Reference Model`, July 2024 maintained edition, `https://repository.ifla.org/handle/20.500.14598/40.2`; and `ISO/IEC/IEEE 26531:2023`, current content-management standard, `https://www.iso.org/standard/81703.html`; compared by value in `E.4:11`. | **Adapt** edition-versus-carrier, snapshot return, content selection, and reuse when the alternative is a guide, package, registry, or combined carrier. **Reject** bibliographic entities and a component-content process as the ontology of programmes, services, Systems, or Methods. |
| One bounded decision account carries alternatives, rationale, consequences, action, and reopen condition. | Current `E.9`; current FPF ground. | Use one ordinary E.9 DRR rather than a PFAD-specific result kind. |
| A public DPF needs a practitioner-use and problem-family coverage answer rather than a pattern count or authoring-slice test. | Current `E.4`, `E.4.DPF`, and `E.4.DPF.DA`; current FPF ground. | Require the DPF field-boundary assessment, including what existing frameworks already provide and what remains uncovered, and expose important omissions without treating carrier prose as proof. |
| Several structures of one practice may be useful and need not line up one-for-one. | Current `A.22`, `C.30.AD`, and proposed `C.32.MWA`; current FPF architecture line. | Use a readable synthesis when those differences change the framework answer; do not copy a source hierarchy into the product. |
| A relation needs actual participants, an obtaining condition, identity when later use needs the occurrence, and a receiving use. | Current `A.6.RCD`, `A.6.REL`, and `E.10:0.0a`; current FPF ground. | Refuse a PFAD relation; state material initial pattern relations directly. |
| Direct framework statements precede optional rows or manifests. | Accepted R3 decision and current `E.4.PFR`; current FPF ground. | Keep PFR representation optional under a named maintenance use. |
| Framework editions, publications, forms, and carriers remain distinct. | Current `E.24.PUB`; current FPF ground. | Treat ADR-like text, sites, and PDFs as projections or publications, not as the decision or framework. |
| Compact ADR sections help preserve decision memory but do not supply FPF ontology. | Nygard, `Documenting Architecture Decisions`, 2011; historical lineage source, `https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions`; MADR, maintained template practice, `https://adr.github.io/madr/`. | Reuse concise question, alternatives, rationale, consequences, and supersession cues only when an ADR-like projection is useful. |

The external comparisons in this section are decision aids, not authorities over the FPF boundary. Recheck their current editions and the field's stronger post-2026 scoping practice when a source changes, when a new alternative could change the answer, or when project evidence shows that the selected boundary no longer supports first use.

