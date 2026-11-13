---
chunk_kind: "child"
pattern_id: "C.31.ASAP"
pattern_title: "Which Architecture Is Preferable Under Scale? (Scale Amenability)"
section_id: "C.31.ASAP:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31.ASAP/C.31.ASAP__013_relations.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "C.31.ASAP — Which Architecture Is Preferable Under Scale? (Scale Amenability)"
  - "C.31.ASAP:12 — Relations"
line_start: 79698
line_end: 79735
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.2.6"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18.1"
  - "C.19.1"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.31"
  - "C.31.RSA"
  - "C.32"
  - "C.32.PAD"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "architecture alternatives"
  - "architecture scale preference"
  - "coarse-graining"
  - "exception growth"
  - "scale amenability"
  - "scale probe"
  - "scale variable"
  - "scale window"
  - "waiver"
---

### C.31.ASAP:12 - Relations

- **Builds on:** `C.31`, `C.31.RSA`, `C.16`, `A.2.6`, `A.17`, `A.18`, `A.19`, `C.18.1`, `C.19.1`, and `C.29`; uses A.1.1 only when a selected `BoundedModelUseStructure` changes the receiving interpretation.

**Coordinates with:**

| Need or use condition | Coordinating pattern |
| --- | --- |
| Module-interface relation repair. | `A.6.M` |
| Architecture and selected-structure questions. | `C.30`, `C.30.ASV`, `C.30.LCA`, and `C.30.ILC` |
| Scale-amenability material needs captured-structure, lost-structure, preservation, or correspondence adequacy before candidate use. | `C.33` and `C.34` |
| The generated or discovered result's kind and adequacy for candidate use. | `C.35` |
| Scale-amenability pressure must continue through problem-to-structure architecturing. | `C.32.P2S` |
| The pressure is represented as a distinct project criteria row. | `C.32.ACS` |
| Scale preference informs candidate architecture generation. | `C.32` |
| Scale preference supplies one input to explicit comparison. | `A.19.CPM` |
| Source recovery and bounded reliance; addressable provenance; a named assurance claim. | `A.10`; `G.6`; `B.3`, respectively |
| Selected-set, parity, and choice claims. | `G.5`, `G.9`, and `C.11`, respectively |


**Claim boundaries:**

| Claim being made | Governing pattern |
| --- | --- |
| Architecture scale preference | `C.31.ASAP` |
| Criteria-set and criteria-row construction | `C.32.ACS` |
| Explicit comparison | `A.19.CPM` |
| Modularity characteristic | `C.31` |
| Reusable-structure accounting | `C.31.RSA` |
| Mathematical lens | `C.29` |
| Scale law | `C.18.1` |
| General method preference | `C.19.1` |
| Selected set | `G.5` |
| Parity | `G.9` |
| Local choice | `C.11` |

- **Precision-restoration relation:** source wording recovered by `E.10`, `E.10.ARCH`, or `C.30.STRAT` is governed by C.31.ASAP only when the recovered claim being made is architecture scale preference over a declared alternative set, scale variable, and scale window.

