---
chunk_kind: "child"
pattern_id: "C.32"
pattern_title: "Architecture Candidate Synthesis"
section_id: "C.32:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32/C.32__008_conformance-checklist.md"
commit_sha: "d064720b072b822cbb2f1d41e555cf08e2904f11"
heading_path:
  - "C.32 — Architecture Candidate Synthesis"
  - "C.32:7 — Conformance Checklist"
line_start: 62228
line_end: 62240
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.HCS"
  - "C.32.MLAO"
  - "C.32.MWA"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.18"
  - "E.22"
  - "E.23"
  - "G.5"
  - "U.Structure"
keywords:
  - "CandidateArchitecturePalette@Project"
  - "architecture candidate synthesis"
  - "architecture characteristics"
  - "candidate configurations"
  - "retained alternatives"
  - "selected structures"
  - "selected-structure contribution rows"
  - "trade-off front"
---

### C.32:7 - Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-C32-1` | The use names one synthesis question, described holon, intended palette use, and the current architecture relations and selected structures that change the question; ClaimScope or a bounded model-use structure is added only when action-changing. | Keeps the palette local without a generic context premise. |
| `CC-C32-2` | The selected-structure contribution rows name the smallest useful set of selected structures and subject patterns and state what each contributes. | Prevents one-structure optimization from masquerading as synthesis. |
| `CC-C32-3` | Architecture characteristics and any quality bundles are named before candidate comparison. | Keeps functional demand distinct from architecture trade-offs. |
| `CC-C32-4` | Each candidate configuration names selected structure changes, expected gain, known loss, and constraint fit. | Makes the candidate actionable. |
| `CC-C32-5` | Compressed, generated, or view-derived candidates carry a source-return condition. | Keeps later source-use or decision-use claims tied to recoverable sources. |
| `CC-C32-6` | Archive, front, pool-treatment, G.5 result declaration, publication availability, local choice, and decision uses have named patterns for the next questions. | Keeps synthesis separate from downstream receiving claims. |
| `CC-C32-7` | Worked slices show what changes in practice across multiple selected structures. | Keeps the pattern constructive. |
| `CC-C32-8` | If an independently typed source constrains transformed-side architecture content for a changed referent, `C.32.CONWAY` is opened before Conway, mirroring, or inverse-Conway language is used as guidance; the source kind, its exact obtaining direct relation or precise provisional disposition, and both exact C.30 architecture sides or modal claims are named without inferring acting, Work, or transformation facts. | Keeps influence-source and transformed-side content distinct while making correspondence synthesis constructive. |

