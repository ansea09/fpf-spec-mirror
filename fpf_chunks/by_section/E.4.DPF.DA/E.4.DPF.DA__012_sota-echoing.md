---
chunk_kind: "child"
pattern_id: "E.4.DPF.DA"
pattern_title: "Domain Principle Framework Package-Adequacy Evaluation CharacteristicSpace"
section_id: "E.4.DPF.DA:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.DPF.DA/E.4.DPF.DA__012_sota-echoing.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "E.4.DPF.DA — Domain Principle Framework Package-Adequacy Evaluation CharacteristicSpace"
  - "E.4.DPF.DA:11 — SoTA-Echoing"
line_start: 70602
line_end: 70625
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.19.ECS"
  - "A.2.1"
  - "A.2.6"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "B.1.5"
  - "C.2.1"
  - "C.30.AD"
  - "C.32.MWA"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.11"
  - "E.11.PFP"
  - "E.17"
  - "E.19"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.23.CDI"
  - "E.24.PUB"
  - "E.4"
  - "E.4.DPF"
  - "E.4.PFAD"
  - "E.4.PFIP"
  - "E.4.PFR"
  - "F.18"
  - "F.6"
  - "G.11"
  - "G.2"
  - "U.Method"
keywords:
---

### E.4.DPF.DA:11 - SoTA-Echoing

| Claim | Exact source ref and status | Pattern locus changed | Adoption status |
| --- | --- | --- | --- |
| Xtext grammar definitions and example instances often evolve together, while many studied repositories contain no example instance. | Zhang, Struber, Hebig, `Development and Evolution of Xtext-based DSLs on GitHub: An Empirical Investigation`, arXiv:2501.19222, 2025 current empirical DSL-evolution source. | **Adopt narrowly:** use the empirical result only for grammar-definition/example-instance co-evolution and missing-example pressure. **Adapt by local rationale:** when a domain account changes, check whether the DPF vocabulary and worked examples must change together; use `D2`, `D10`, and their direct sources for usability and package evaluation rather than attributing those claims to this study. | Reject Xtext grammar or metamodel ontology for DPF unless a specific DPF defines it; the study establishes neither DPF terminology quality, usability, nor package adequacy. |
| Reusable-core and domain-variation work needs explicit dependency, adoption, tooling, and evolution discipline. | Nazar, `Software Product Line Engineering: Adoption, Tooling and AI Era Challenges`, arXiv:2605.21353, 2026 current survey and reopen trigger for stronger future SPLE synthesis. | Coordinates `D4`, `D5`, `D9`, and `D10`, plus `PFM4` and `PFM7`, require Core dependency, relation records, edition pins, blocked reverse dependency, and refresh. | Adapt reusable-core discipline; reject software feature-model semantics as the default DPF ontology. |
| Field-scale framework adequacy needs connected family scope, common and variable architecture, representative use, and lifecycle evidence rather than a component count or carrier pass. | `ISO/IEC 26550:2015, Software and systems engineering — Reference model for product line engineering and management`, current edition, `https://www.iso.org/standard/69529.html`; and `ISO/IEC 26552:2019, Tools and methods for product line architecture design`, current edition, `https://www.iso.org/standard/43111.html`. | `D12` checks the public field promise, selected problem-family sets and material relations, representative cross-problem use, omissions, internally usable first use, external dependencies, and reopen condition. | **Adapt** explicit family scope, common/variable architecture, application use, and lifecycle comparison. **Reject** software-product ontology, feature-model machinery, tool burden, and any numeric or form-only adequacy threshold. |
| Pattern-language adequacy needs domain-use and validation evidence, not only section presence. | Riehle, Harutyunyan, and Barcomb, `Pattern Discovery and Validation Using Scientific Research Methods`, final publication 2025, `https://doi.org/10.1007/978-3-662-70810-1_6`; Chuprina et al., `Towards an Approach to Pattern-based Domain-Specific Requirements Engineering`, 2024 academia-industry proof of concept, `https://arxiv.org/abs/2404.17338`; Iba, `Pattern Languages as Media for the Creative Society`, 2013 historical lineage, `https://arxiv.org/abs/1308.1178`. | `D8`, `D12`, Archetypal Grounding, and anti-patterns require representative and heterogeneous cases, the domain-specific contribution question, explicit limits, important omissions, and a source-backed reopen condition. | **Adapt** qualitative survey, action research, case studies, practice-media pressure, and the question of what domain specificity changes. The 2024 line is a first attempt and Iba is lineage; neither establishes package adequacy or a universal field grammar. |
| Architecture descriptions and publication carriers do not equal the architecture or package adequacy. | `ISO/IEC/IEEE 42010:2022`, current architecture-description standard ref. | Coordinates `D5` and `D9`, publication-carrier anti-pattern, and map-hoarding near miss separate publication carriers from package structures. | Adopt description-boundary discipline; adapt through `C.33`, `C.34`, `E.11`, and `E.17`. |
| Quality measures can become targets and make the object worse. | Goodhart, Campbell, management-accounting surrogation, specification-gaming, and reward-hacking lines already carried through `E.2.DA`, `E.13`, `E.21`, `E.22`, and `E.23`. | `Solution`, `Conformance Checklist`, and anti-patterns forbid all-`5`, source-count, map-count, or review-proof targeting. | Adopt proxy-risk discipline; values rise only through package-use improvement. |

**Source-currentness front.** Apply the source decisions above only within the role and qualification basis below. When the named smallest change occurs, use `G.11` to reopen only the affected coordinates, case, boundary, or proxy rule and reopen the changed source use with `G.2`; a newer date alone does not reopen the package.

| Decision source | Currentness role and qualification basis | Smallest material reopen condition |
| --- | --- | --- |
| Xtext empirical study | `current empirical input` only for Xtext grammar-definition/example-instance co-evolution and the observed absence of example instances in many studied repositories. Its use as a prompt to co-evolve DPF vocabulary and worked examples is an explicit local Adapt; it supplies no evidence for DPF usability or package evaluation. | A later comparable study materially changes the grammar/example result, or the receiving DPF changes how that narrow Adapt affects `D2`, `D6`, or `D10`. |
| SPLE survey | `current survey input`, qualified through the cited 2026 arXiv edition for reusable-core dependency, adoption, tooling, and evolution practice; software feature-model semantics remain rejected as default DPF ontology. | A superseding survey or systematic review materially changes the reusable-core, reverse-dependency, adoption, tooling, or evolution discipline used by `D4`, `D5`, `D9`, `D10`, `PFM4`, or `PFM7`. |
| Product-line architecture standards | `current normative comparison input`, qualified to the cited current ISO/IEC 26550:2015 and ISO/IEC 26552:2019 editions and their software product-line scope. Feature-model, software-product, lifecycle, and tooling ontology remain rejected for default DPF use. | A revision or replacement materially changes the family-scope, common/variable architecture, representative-use, or lifecycle contribution used by `D12`. |
| Pattern-validation method | `current validation-practice input`, qualified to the cited final 2025 publication and the limits of its qualitative survey, action-research, and case-study evidence. | Replication, comparative validation research, or a changed practice line materially alters the evidence needed for `D8`, `D12`, representative cases, important omissions, or source-backed reopen conditions. |
| Domain-specific pattern approach | `current proof-of-concept input`, qualified to the cited 2024 edition, its requirements-engineering use, and its explicit first-attempt limit. | Later empirical evaluation or a competing current approach changes what domain-specific contribution, practitioner use, representative application, or source return `D12` must expose. |
| Iba practice-media paper | `lineage`, qualified to the cited 2013 edition only for the pattern-language-as-practice-media rationale; it is not current validation evidence. | A corrected or replacement lineage source changes that rationale, or current practice-media evidence materially changes how worked cases and practitioner use support rather than replace package validation. |
| ISO/IEC/IEEE 42010 | `current normative reference`, pinned to the exact 2022 edition for the architecture-versus-architecture-description boundary. | A superseding edition or amendment materially changes that boundary or the use conditions for architecture descriptions, requiring revision of `D5`, `D9`, the publication-carrier anti-pattern, or the map-hoarding near miss. |
| Proxy-risk line | Goodhart and Campbell are `lineage`; current applicability is supplied through the named current neighboring FPF sources `E.2.DA`, `E.13`, `E.21`, `E.22`, and `E.23`, qualified to their current editions and their content-evaluation use. | One of those direct FPF sources changes the proxy-risk or substantive-improvement rule, or later evidence materially changes when score, source, map, or review-proof targeting harms the evaluated package; reopen the affected Solution, checklist, or anti-pattern rule only. |

