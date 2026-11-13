---
chunk_kind: "child"
pattern_id: "E.4.FPF"
pattern_title: "FPF Edition Assembly: Publication Forms, Carriers and Access Routes"
section_id: "E.4.FPF:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.FPF/E.4.FPF__007_bias-annotation.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "E.4.FPF — FPF Edition Assembly: Publication Forms, Carriers and Access Routes"
  - "E.4.FPF:6 — Bias-Annotation"
line_start: 98832
line_end: 98843
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
  - "F.19"
  - "G.11"
  - "G.2"
keywords:
---

### E.4.FPF:6 - Bias-Annotation

**Scope:** This pattern covers the publication units and forms, assembly, exact presentation carriers, access routes, and whole-framework evaluation route of an FPF edition. Repository layout, assembly tool, carrier split, and publication service remain implementation choices. A one-sentence repair that leaves these FPF-level values unchanged uses its direct wording and source route.

| Lens | Likely drift | Repair |
|---|---|---|
| Gov | A successful assembly or form check is read as acceptance, publication, availability, currentness, or adequacy. | Keep construction results separate from the decisions and relations that establish those claims. |
| Arch | The current all-in-one layout, source tree, or helper is treated as the only possible FPF architecture. | Preserve edition, selected Core, publication-unit/form, presentation-carrier, access-route, index/body, and unchanged-content invariants while allowing another repository, tool, carrier split, or publication service. |
| Onto-Epist | The edition, one publication unit, its particular expression, the form whose rules that expression follows, the presentation carrier bearing that expression, an access route, the rebuildability record, the assembly Method, and performed assembly Work collapse into one object. | Name them separately where the distinction changes the claim. The record describes reconstruction inputs and routes. The assembly Work is the construction occurrence. The edition contains the coordinated framework content. An independently identified physical or digital carrier bears the particular expression. |
| Prag | Every small source edit is forced through FPF-level assembly paperwork, or exact source return is omitted to save effort. | Use this pattern only when FPF publication units, form, carriers, access routes, edition assembly, or whole-FPF evaluation are at issue. Keep the record minimal while retaining complete selected sources and unchanged-predecessor protection. |
| Did | Build apparatus meets the reader before a working question, or a smooth front hides where authoritative pattern content resumes. | Apply `E.11.PFP` to the reader-facing opening and keep paths, commands, digests, and diagnostics in maintainer evidence or tool help. |

