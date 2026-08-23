---
chunk_kind: "child"
pattern_id: "E.4.FPF"
pattern_title: "First Principles Framework Form and Publication-or-Access Carrier Assembly"
section_id: "E.4.FPF:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.FPF/E.4.FPF__012_sota-echoing.md"
commit_sha: "5801dc610c657ac7b1efee349b18e80ce6d7df6f"
heading_path:
  - "E.4.FPF — First Principles Framework Form and Publication-or-Access Carrier Assembly"
  - "E.4.FPF:11 — SoTA-Echoing"
line_start: 67924
line_end: 67939
dependencies:
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.11"
  - "E.11.PFP"
  - "E.17"
  - "E.2"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.4"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.4.PFAD"
  - "E.4.PFR"
  - "E.9.DA"
  - "F.18"
  - "G.11"
  - "G.2"
  - "I.2"
keywords:
---

### E.4.FPF:11 - SoTA-Echoing

The comparison below asks what each approach adds at its actual reader and maintainer cost. E.4.FPF adopts only the smallest reusable invariants; it does not turn FPF into an RFC production line or a software-documentation site.

| Claim | Exact source ref and status | Pattern locus changed | Adoption status |
|---|---|---|---|
| One definitive technical source can yield several publication versions while each object keeps its own identity and semantic-preservation rule. | [RFC 9720, *RFC Formats and Versions*](https://www.rfc-editor.org/rfc/rfc9720.html), January 2025, current RFC Series policy checked 2026-08-22. It distinguishes definitive format/version from publication formats/versions, requires the definitive version to contain the semantic content needed for rendering, and records controlled reissues and archives. | `Solution` separates the edition source, publication units and forms, exact carriers, construction result, and publication occurrence; Grounding and `CC-FPF.12` protect unchanged content. | **Adapt:** retain source-to-publication separation, semantic-preservation checks, and recoverable prior versions. **Reject:** RFCXML, the RFC Production Center process, and its higher governance burden as universal FPF requirements. |
| A versioned documentation product can collect sources from several locations, identify one component version, use stable resource coordinates, and stop on duplicate resources. | [Antora 3.1 component-version documentation](https://docs.antora.org/antora/latest/component-version/) and [resource-ID checks](https://docs.antora.org/antora/latest/page/resource-id/), current official documentation checked 2026-08-22. | `FPFEditionRebuildabilityRecord`, ordinary method step 9, and `CC-FPF.12` require exact edition/source membership, index/body agreement, and mismatch stops. | **Adapt:** exact version membership, stable source references, multi-source assembly, and duplicate rejection. **Reject:** Antora's component schema, repository conventions, and configuration burden as FPF law; Antora alone does not prove unchanged predecessor spans. |
| One declared source hierarchy can drive both split and single-output publications and warn when a source is unreachable from navigation. | [Sphinx, *Directives — Table of contents*](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#table-of-contents), current official documentation checked 2026-08-22. | Ordinary method steps 4 and 9, Grounding, and `CC-FPF.9-12` connect one logical index with every selected body across publication forms and carriers. | **Adapt:** explicit inclusion, order, reachability, and one source hierarchy for several outputs at comparatively low setup cost. **Reject:** reStructuredText, `toctree`, or a Sphinx builder as required FPF machinery; navigation warnings do not establish edition identity or source preservation. |
| Architecture descriptions and publication forms must not be confused with the architecture or `EntityOfConcern`. | `ISO/IEC/IEEE 42010:2022, Software, systems and enterprise — Architecture description`, official current standard ref already used by `E.4`. | `Solution` separates the FPF edition, Core pattern set, publication units and forms, presentation carriers, and access routes. | **Adapt:** separation and correspondence discipline. **Reject:** architecture-description vocabulary where ordinary framework-edition, publication-unit, form, carrier, and access-route wording is sufficient. |
| Reusable core assets need variation and dependency discipline across a family. | Nazar, `Software Product Line Engineering: Adoption, Tooling and AI Era Challenges`, arXiv:2605.21353, 2026 survey already used by `E.4`. | Dependency direction from FPF Core to DPF or local dependents is a checklist item. | **Adapt:** reusable-core and dependency discipline. **Reject:** software-product feature-model ontology as universal FPF architecture. |
| Whole-language adequacy is not an average of local pattern quality. | `E.2.DA`, `E.21`, `E.22`, and `E.23`, current internal FPF evaluation lineage. | `Solution` sends whole-FPF evaluation to `E.2.DA` and pattern-body evaluation to `E.21`. | **Adopt:** the object-under-improvement split. **Reject:** all-`5`, successful build, or landing status as whole-FPF adequacy. |
| Access carriers and routes need currentness and authority boundaries. | `E.11`, `E.17`, `G.11`, `C.35`, and `A.15`, current internal FPF sources for publication, refresh, generated-carrier, and System–Method–Work boundaries. | An exact skill-pack, index, or response carrier may bear an access-facing form; the skill, MCP, retrieval, or assistant service is an access route, and neither is authority or work permission. | **Adopt:** explicit carrier/route limits; route stronger claims to their subject patterns. |

Reopen these source decisions when a newer applicable standard or maintained practice changes the used distinction among edition source, publication unit, form, exact presentation carrier, access route, and publication version; offers a lower-effort way to preserve exact source membership, index/body correspondence, or unchanged predecessor content; or makes the selected rule harder for an FPF reader or maintainer than a non-dominated alternative.

