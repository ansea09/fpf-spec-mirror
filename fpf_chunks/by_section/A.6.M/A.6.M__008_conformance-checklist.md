---
chunk_kind: "child"
pattern_id: "A.6.M"
pattern_title: "Module Relation Repair"
section_id: "A.6.M:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.M/A.6.M__008_conformance-checklist.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "A.6.M — Module Relation Repair"
  - "A.6.M:7 — Conformance Checklist"
line_start: 16252
line_end: 16266
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
  - "C.30.TFS-REL"
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
| `CC-A6M-2` | The repair states whether the phrase is a module relation, component relation, function allocation, procedural or work-package relation, role-assignment or responsibility relation, deployment or placement structure, interface specification, signature, port or endpoint, transformation-flow crossing, mechanism realization, platform grammar, control relation, autonomy-like operation claim, `C.30.STRAT` source-label case, or open-architecture claim. |
| `CC-A6M-3` | No new root kind is minted for module, interface, platform, or open architecture; stratification or architecture-operation source labels use `C.30.STRAT` unless a module-interface relation has already been recovered. |
| `CC-A6M-4` | `InterfaceSpecificationRef` is recoverable when interface compatibility, substitutability, or conformance is being claimed. |
| `CC-A6M-5` | Substitution or change policy is declared when replaceability, alternate supplier, upgrade, or platform extension is being claimed. Substitutability not established by the repair is marked as not established, not implied by wording. |
| `CC-A6M-6` | Function, transformation-flow, control, work, evidence, assurance, gate, decision, causal, and mechanism claims use their governing patterns. |
| `CC-A6M-7` | A failed check gives a repair action or governing-pattern application, not only a rejection. |
| `CC-A6M-8` | A current `G.2` source row for MOSA, open systems, platform practice, Conway correspondence, team-boundary correspondence, or Amdahl-style decomposition limits appears before guidance from that source is used for practitioner-facing claims being made. |
| `CC-A6M-9` | RFC keywords are used only for pattern users, records, claims, conformance items, or publication records, evidence records, or assurance records. Modeled modules and interfaces are not written as agents with duties. |
| `CC-A6M-10` | Lower or reopen the repair when whole holon, module holon, boundary, interface specification, interface gap, substitutability policy, change policy, platform grammar, conformance expectation, relied-on evidence relation, relied-on source relation, source-label recovery, team-to-work correspondence, or neighboring governing pattern changes. |

