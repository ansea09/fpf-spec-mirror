---
chunk_kind: "child"
pattern_id: "C.30.STRAT"
pattern_title: "Stratification Wording Precision Restoration"
section_id: "C.30.STRAT:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.STRAT/C.30.STRAT__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "C.30.STRAT — Stratification Wording Precision Restoration"
  - "C.30.STRAT:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 58228
line_end: 58237
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.SPR"
  - "A.2"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.17"
  - "E.18"
  - "E.8"
  - "F.18"
  - "G.5"
  - "G.6"
  - "I.2"
keywords:
---

### C.30.STRAT:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Source label as ontology | `layer`, `block`, `expert`, `cache`, or `gate` is treated as a kind by name. | Recover the actual object or relation, or keep ordinary source wording. |
| C.30 takeover | Every structure-like word is treated as an architecture claim. | Choose from the recovered meaning; use the rule for the actual control, module, flow, scale, publication, state, evidence, work, or decision claim. |
| Local trigger fanout | C.30.LCA, A.6.M, C.31, or another pattern copies this label catalogue. | Keep one thin pointer here and the other pattern's own invariant there. |
| Expert-as-role false positive | `expert` in mixture-of-experts prose becomes a system-role kind, assignment, performer, Work, responsibility, or authority by word alone. | First test submodel, transformation, path selection, candidate selection, or ordinary non-use. If a claim-bearing use of *role* remains, use E.10.ROLE; admit each system-role, classification, assignment, performer, Work, responsibility, authority, or other relation only when it independently obtains. |
| Gate-as-decision false positive | A gating function, UI label, or source word becomes gate passage. | Use A.20 or A.21 only for actual constraint-validity or gate-decision claims; otherwise use the applicable function, flow, publication, or ordinary-label result. |

