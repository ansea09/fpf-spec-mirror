---
chunk_kind: "child"
pattern_id: "A.6.M"
pattern_title: "Module Relation Repair"
section_id: "A.6.M:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.M/A.6.M__008_conformance-checklist.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "A.6.M — Module Relation Repair"
  - "A.6.M:7 — Conformance Checklist"
line_start: 14090
line_end: 14103
dependencies:
  - "A.10"
  - "A.20"
  - "A.21"
  - "A.6.5"
  - "A.6.B"
  - "A.6.F"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.28"
  - "C.30"
  - "C.30.ASV"
  - "C.30.TGA-FLOW-REL"
  - "C.31"
  - "C.31.RSA"
  - "E.18"
  - "E.20"
  - "G.5"
keywords:
  - "are used only for pattern users"
  - "claims"
  - "component"
  - "conformance items"
  - "evidence records"
  - "interface"
  - "interface specification"
  - "layer"
  - "module relation"
  - "open architecture"
  - "or assurance records. Modeled modules and interfaces are not written as agents with duties"
  - "or publication records"
  - "platform"
  - "port"
  - "records"
  - "stack"
  - "substitutability"
---

### A.6.M:7 - Conformance Checklist

| ID | Check |
| --- | --- |
| `CC-A6M-1` | The text names the whole holon, candidate module holon, bounded context, and module-interface viewpoint, or explicitly stops at ordinary non-claim-bearing wording. |
| `CC-A6M-2` | The repair states whether the phrase is a module relation, component relation, function allocation, procedural or work-package relation, role or enactor relation, deployment or placement structure, interface specification, signature, port or endpoint, TGA flow crossing, mechanism realization, platform grammar, control relation, autonomy-like operation claim, `C.30.STRAT` source-label case, or open-architecture claim. |
| `CC-A6M-3` | No new root kind is minted for module, interface, platform, or open architecture; layer and stack labels route through `C.30.STRAT` unless a module-interface relation has already been recovered. |
| `CC-A6M-4` | `InterfaceSpecificationRef` is recoverable when interface compatibility, substitutability, or conformance is live. |
| `CC-A6M-5` | Substitution or change policy is declared when replaceability, alternate supplier, upgrade, or platform extension is live. Substitutability not established by the repair is marked as not established, not implied by wording. |
| `CC-A6M-6` | Function, TGA flow, control, work, evidence, assurance, gate, decision, causal, and mechanism claims use their exact governing patterns. |
| `CC-A6M-7` | A failed check gives a repair move or exact governing pattern application, not only a rejection. |
| `CC-A6M-8` | A current `G.2` source row for MOSA, open systems, platform practice, Conway correspondence, team-boundary correspondence, or Amdahl-style decomposition limits appears before that source carries live practitioner guidance. |
| `CC-A6M-9` | RFC keywords are used only for pattern users, records, claims, conformance items, or publication records, evidence records, or assurance records. Modeled modules and interfaces are not written as agents with duties. |

