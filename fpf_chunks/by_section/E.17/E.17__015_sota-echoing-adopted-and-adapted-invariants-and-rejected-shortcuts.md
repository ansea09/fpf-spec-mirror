---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:12"
section_title: "SoTA-Echoing: Adopted And Adapted Invariants And Rejected Shortcuts"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__015_sota-echoing-adopted-and-adapted-invariants-and-rejected-shortcuts.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:12 — SoTA-Echoing: Adopted And Adapted Invariants And Rejected Shortcuts"
line_start: 83290
line_end: 83302
dependencies:
  - "A.10"
  - "A.15.4"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.2"
  - "A.6.3"
  - "A.6.9"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.10"
  - "E.10.D2"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.17.AUD"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.24.PUB"
  - "E.8"
  - "F.9"
  - "F.9.1"
  - "U.View"
keywords:
---

### E.17:12 - SoTA-Echoing: Adopted And Adapted Invariants And Rejected Shortcuts

**SoTA and local-rationale alignment rule.** Read each external-source row as source idea -> local FPF invariant -> practical local test -> shortcut rejected. A cited source contributes only the idea translated into this pattern. A row deduced from named current FPF patterns is labelled local design rationale and is not presented as external SoTA evidence.

| Current source idea or explicit local design rationale | Local FPF invariant and practical local test | Adopted, adapted, or rejected shortcut |
| --- | --- | --- |
| Joint ISO, IEC, and IEEE 42010:2022 architecture-description practice, used as established practice lineage rather than current architecting SoTA, separates architecture description, stakeholder concern, viewpoint, view, model kind, correspondence, and correspondence rule. | MVPK publishes one source-pinned face over an exact selected episteme edition; when `U.View` membership is material, it separately resolves the exact viewpoint episteme and E.17.0 conformance. Publication occurrence, form, carrier work, rendering work, correspondence relation, exchange envelope, and evidence envelope remain distinct and are identified only when the receiving use depends on them; the no-new-claim diff always applies. | Adopt the object distinctions; reject the shortcut where a readable face or standards label becomes a view, evidence, work occurrence, gate passage, release permission, bridge relation, or exchange authority by presentation alone. |
| Pickering, Gibbons, and Wu, *Profunctor Optics: Modular Data Accessors* (ICFP 2017; arXiv [`1703.10857`](https://arxiv.org/abs/1703.10857)), and Clarke et al., *Profunctor Optics, a Categorical Update* (2020; arXiv [`2001.07488`](https://arxiv.org/abs/2001.07488)), used as a research/theory lineage rather than downstream-reliance evidence, provide the concrete compositional-optics source idea. | MVPK adopts only local publication-composition tests: identity, composition witness, no-new-claim diff, monotone promotion, and scope non-widening. | Adopt the five-test publication-composition bundle; reject optics vocabulary as proof by analogy or as a replacement for local witnesses. |
| **Local design rationale, not external SoTA evidence:** current FPF `C.16` defines characteristics, scales, measurement procedures, and result interpretation; `A.19` defines admitted `U.CharacteristicSpace` values and their slots. E.17 reuses those definitions because omitting a material unit, scale, reference plane, or edition can change the value read from a publication form. | A numeric or comparable value exposed through a publication form retains the characteristic reference and every pin that changes interpretation; focused test: remove each pin in turn and reject the form for the bounded use only when the interpreted value changes or becomes unresolved. | Adopt the existing characteristic and scale discipline; reject readable numbers and a local PC label as self-validating values or new kinds. |
| **Local design rationale, not external SoTA evidence:** current FPF `E.24.PUB` separates selected episteme, publication form, carrier, bounded use, and publication occurrence; `A.10` supplies source-to-use evidence/provenance paths and bounded reliance, `G.6` supplies addressable path citation, slicing, and local refresh, and `G.11` supplies currentness. E.17 combines only the references needed to stop a reader from mistaking an envelope or carrier for the carried claim. | A publication form may expose an exchange envelope, carrier, evidence pointer, or provenance pointer, but the source or evidence relation remains separately recoverable; focused test: removing the envelope leaves the source claim unchanged, while removing the source or evidence relation blocks only the use that relied on it. | Adopt the existing object separation and source-return discipline; reject envelope presence as semantic authority, evidence sufficiency, performed work, or gate passage. |

(External references are retained only for the payload they contribute; named local rationales are deductions from current FPF patterns rather than claims of external SoTA support. MVPK remains notation-agnostic.)

