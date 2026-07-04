---
chunk_kind: "child"
pattern_id: "C.32.P2S"
pattern_title: "Problem-to-Structure Architecturing Transformation Flow"
section_id: "C.32.P2S:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.P2S/C.32.P2S__008_conformance-checklist.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "C.32.P2S — Problem-to-Structure Architecturing Transformation Flow"
  - "C.32.P2S:7 — Conformance Checklist"
line_start: 59660
line_end: 59674
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.3.4"
  - "B.2"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.2"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.HCS"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.17"
  - "E.18"
  - "E.23"
  - "E.24.PUB"
  - "G.11"
  - "G.5"
keywords:
  - "ProblemToStructureArchitecturingFlowCard@Project"
  - "actual-structure feedback"
  - "architecture work flow"
  - "owner-specific return"
  - "problem-to-structure architecturing flow"
  - "selected structures"
  - "structural uncertainty"
---

### C.32.P2S:7 - Conformance Checklist

| Check | Pass condition |
|---|---|
| `CC-C32P2S-1` | The card names described holon, bounded context, problem pressure, first owner, and at least one architecture-relevant structure or unknown-structure slot. |
| `CC-C32P2S-2` | The architecture claim, when made, is grounded through `C.30` over selected structures of the described holon; no description or publication record carries the architecture by itself. |
| `CC-C32P2S-3` | Architecture characteristics are separate from functional demands, measurements, eval programs, eval results, Q-bundles, comparison rules, and decisions. |
| `CC-C32P2S-4` | The structural-information lane records unknown, selected, expected, actual, captured, handed-off, latent or hidden, lost, and returned structure when those slots are live. |
| `CC-C32P2S-5` | Candidate synthesis exits to `C.32`, comparison and selection claims exit to their owners, and the P2S card does not choose a winner by score or prose preference. |
| `CC-C32P2S-6` | A project architecture decision, when current, exits to `C.32.PAD`; ADR-like publication exits to `C.32.ADR` and publication owners. |
| `CC-C32P2S-7` | Method, work-plan, readiness, and performed-work claims exit to A.15-family owners; the P2S card carries refs and expected structure effects. |
| `CC-C32P2S-8` | Measurement, Q-bundle, mathematical-lens, eval, improvement, `G.11` currentness refresh, and `E.18` transformation-flow slice-local refresh claims exit to `C.16`, `C.25`, `C.29`, `C.32.ACE`, `E.23`, `G.11`, or `E.18`. |
| `CC-C32P2S-9` | Transformer/transformed cases name the changing relation, both holons, selected structures on both sides when load-bearing, and the `C.32.CONWAY` correspondence frame. |
| `CC-C32P2S-10` | The pattern use covers at least one realized-structure feedback route that checks actual selected structures, architecture-characteristic results, and relevant functional-characteristic or capability implications through operation, use, inspection, measurement, eval result, telemetry, decay, source-return, or decision-repair trigger. |

