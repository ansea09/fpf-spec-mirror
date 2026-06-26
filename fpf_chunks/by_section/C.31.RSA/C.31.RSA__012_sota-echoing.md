---
chunk_kind: "child"
pattern_id: "C.31.RSA"
pattern_title: "Reusable Structure Accounting"
section_id: "C.31.RSA:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31.RSA/C.31.RSA__012_sota-echoing.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "C.31.RSA — Reusable Structure Accounting"
  - "C.31.RSA:11 — SoTA-Echoing"
line_start: 58253
line_end: 58272
dependencies:
  - "A.10"
  - "A.19"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.31"
  - "C.31.ASAP"
  - "C.32.P2S"
  - "G.5"
  - "G.6"
keywords:
  - "accounting basis"
  - "bespoke residue"
  - "refactoring opportunity"
  - "report-only share"
  - "reusable share"
  - "reusable-structure accounting"
  - "source return"
---

### C.31.RSA:11 - SoTA-Echoing

| Source or practice | Currentness or lineage use | Adopt and adapt for C.31.RSA | Rejected overread | Governing-pattern use and action consequence |
| --- | --- | --- | --- | --- |
| C.25 Q-Bundle discipline inside FPF | Landed FPF-local governing discipline for quality-family claims. | Adopt separation of scope, measures, mechanisms, windows, evidence, and admissible use. In C.31.RSA this changes `ReusableStructureShare`: the share is report-only accounting under declared `accountingBasisRef` until the relevant outside-RSA use is governed by its governing pattern. | A reusable-structure share does not replace the underlying Q-Bundle, description, evidence relation, or decision record. | Apply `C.25` and `C.16` when reuse becomes a quality claim or measurement claim; the practitioner may report a share locally but must not use it as proof without the governing pattern for that use. |
| ISO/IEC/IEEE 42010:2022 architecture-description, viewpoint, model-kind, and correspondence discipline (`https://www.iso.org/standard/74393.html`; `https://www.iso-architecture.org/ieee-1471/cm/`) | Current international standard and conceptual-model source for architecture-description and view discipline for this source-use decision. | Adopt explicit architecture description, source view, viewpoint, model-kind, correspondence, and conformance pressure. In C.31.RSA this changes source-return use: reusable-structure accounting names the structure refs, source view or architecture-description refs, correspondence refs, and source-return condition before any cross-view share is used. | A view, diagram, model kind, or correspondence label is not the reusable structure itself and does not make a share comparable, admissible for decision use, or assurance-bearing. | Apply `C.30`, `C.30.ASV`, or `E.17.0` when source views or architecture descriptions are being used; RSA may count only after the selected structure refs and accounting basis are recoverable. |
| Modular Open Systems Approach (MOSA) and open-system acquisition or engineering practice (`https://www.cto.mil/sea/mosa/`; `https://www.cto.mil/wp-content/uploads/2025/03/MOSA-Implementation-Guidebook-27Feb2025-Cleared.pdf`) | Current engineering and acquisition practice family for modular interfaces, conformance, replacement, and supplier-diversity pressure. | Adopt the pressure to make reusable interface, conformance, substitution, and supplier-diversity structure explicit. In C.31.RSA this changes interface reuse: reusable interface accounting remains report-only until A.6.M has repaired interface grammar, substitution policy, version or change policy, conformance work, source or evidence relation, and the supplier-diversity relation when that relation is being made. | Open interface label, API label, platform label, or supplier-diversity goal is not reusable structure, procurement suitability, assurance, gate passage, or decision authority by itself. | Apply A.6.M for interface grammar, substitution policy, version or change policy, conformance expectations, source or evidence relation, and supplier-diversity relation before RSA comparison or decision use; use `G.5` or `C.11` for supplier-set selection or procurement decision use when that use is being made. |
| DSM, dependency, and product-architecture practice, including Eppinger and Browning DSM lineage | Mature architecture-analysis lineage still used for dependency and product-architecture reasoning; lineage, not a complete current standard. | Adopt typed dependency structures as possible source for reusable loci and bespoke-residue diagnosis. In C.31.RSA this changes dependency use: dependency counts, partitions, and clusters become candidate source fields only when declared `structureRefs`, structural aspects, and accounting basis are present. | Dependency count, cluster count, or DSM modularity score is not architecture amount, quality proof, or decision verdict. | Apply `C.16` and `C.31` for characteristic and scale admissibility; apply `C.29` when graph, partition, compression, or C.29 lens-use result changes action. |
| Goodhart and Campbell proxy-pressure laws | General proxy-risk lineage for report-only shares, reuse scores, and benchmark-like accounting. | Adopt proxy-risk discipline for reusable-share use. In C.31.RSA this changes share use: a reusable-structure share remains report-only until the relevant outside-RSA use is governed by governing patterns. | Reusable-share improvement, coverage improvement, or benchmark improvement is not value, assurance, evidence sufficiency, gate passage, or architecture decision by itself. | Apply `C.16`, `C.25`, `G.5`, `C.11`, or the evidence and assurance patterns before a reuse number can guide selection or reliance. |
| System-evolution, information-hiding, and effective-interface lineage | General holon-architecture lineage for reusable structure that changes over time and hides variation-prone structure. | Adopt evolution and hidden-change discipline. In C.31.RSA this changes residue interpretation: reusable loci, bespoke residue, hidden interface behavior, source-return conditions, and bounded exceptions are reopened when the structure edition, accounting rule, implicit interface, or reliance relation changes. | One-time reusable-share accounting is not sustainable fitness; a stable-looking interface or template does not prove future substitutability. | Reopen or lower the RSA result when hidden variation, implicit dependency, source distinction, or continuing adaptation changes the accounting meaning. |
| Software product-line engineering and variability-management practice, including Pohl, Boeckle, and van der Linden lineage plus current product-line and variability work (`https://www.sei.cmu.edu/library/variability-in-software-product-lines/`; `https://arxiv.org/abs/2605.21353`) | Mature product-line variability lineage plus current SPLE-review cues for variability slots, product-line reuse, platform extension rules, and reuse-rule discipline. | Adopt variability-slot and reuse-rule pressure. In C.31.RSA this changes product-line use: reusable structure may be located in template, interface, work, evidence, and exception loci, and bespoke residue must name repair direction, bounded exception, or source-return condition instead of being averaged into one share. | Product-line label, shared code base, feature model, or platform name is not enough to infer reusable structure or architecture scale-preference evidence. | Apply A.6.M for platform claims or interface claims, C.31.ASAP for architecture scale preference, and C.11 or G.5 for choice or candidate-set use. |
| GSN Community Standard v3 and assurance-case reuse and safety-case reuse practice (`https://scsc.uk/gsn`; `https://arxiv.org/abs/2506.11023`) | Current assurance-case standard family plus current formalization work for this source-use decision; assurance validity remains context-sensitive. | Adopt the distinction between reusable assurance argument structure, reusable evidence structure, and context-specific validity witnesses. In C.31.RSA this changes evidence and assurance reuse: reuse remains accounting until evidence validity, safety-case use, or assurance reliance is governed by its own pattern. | Evidence reuse share or assurance-argument template reuse does not infer assurance, safety-case success, gate passage, or release permission. | Apply `A.10` and `G.6` for evidence validity and safety-case use, and `B.3` for assurance reliance; add source-return condition and validity-window check before reliance. |
| Architecture-operation language, with neural-network and software-system discussions as source examples, including the GonzoML architecture-operation intake | Current practitioner-language source for structural substitution, gating, memory placement, cache placement, routing, ablation, pruning, distillation, and architecture search; not used as a current standard by itself. | Adopt the recognition that replacement and search expose reusable and bespoke structural loci. In C.31.RSA this changes architecture-operation use: source labels such as block, layer, expert, cache, router, gate, or pruning mask remain source labels until `C.30.STRAT` and the governing pattern for the claim being made recover `structureRefs`, aspect refs, accounting basis, repair actions, and source-return conditions. | Block, layer, expert, cache, router, gate, benchmark, ablation, pruning mask, or distillation success is not RSA slot ontology, architecture decision, evidence sufficiency, gate passage, assurance, or architecture adequacy by itself. | Apply `C.30.STRAT` first where source-label recovery is needed, then `C.30` or `C.30.ASV` for architecture claim and structural view, `C.30.TFS-REL` for flow changes, `C.29` for mathematical-lens or compression claims, `A.10` or `G.6` for benchmark or evidence use, and `C.28` for causal claims. |

**Source-currentness front.** Use the table's `Currentness or lineage use` cell as the source-use boundary. Rows named current, such as ISO/IEC/IEEE 42010:2022, MOSA guidance, current product-line or variability work, GSN Community Standard v3, current safety-case reuse work, and the architecture-operation corpus material used as current practitioner language, require source refresh before outside-RSA use when the named standard, guide, practice family, or corpus role changes. Rows named lineage, such as DSM or product-architecture lineage, Eppinger and Browning lineage, Goodhart and Campbell proxy-pressure lineage, system-evolution and information-hiding lineage, and Pohl, Boeckle, and van der Linden lineage, stay lineage unless a current source relation is explicitly recovered.

Refresh or lower the RSA result when a source-role change alters the reusable locus, bespoke-residue locus, accounting basis, source-return condition, comparator admission, evidence-validity relation, assurance or safety-case reliance, architecture scale-preference relation, or any outside-RSA use. A source row may explain why an accounting distinction matters, but it does not make an RSA share current for comparison, decision, assurance, gate, or publication without the governing pattern for that outside-RSA use.

Older or local sources may serve as lineage or worked examples only when the row says so. They do not stand in for current competitive source, and they do not make an RSA share admissible for outside-RSA use without the governing pattern for that use.

