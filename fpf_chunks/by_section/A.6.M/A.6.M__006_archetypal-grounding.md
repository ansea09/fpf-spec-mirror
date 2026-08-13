---
chunk_kind: "child"
pattern_id: "A.6.M"
pattern_title: "Module Relation Repair"
section_id: "A.6.M:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.M/A.6.M__006_archetypal-grounding.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "A.6.M — Module Relation Repair"
  - "A.6.M:5 — Archetypal Grounding"
line_start: 19045
line_end: 19054
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

### A.6.M:5 - Archetypal Grounding

**Tell.** A module is not a little box. It is a holon related to a larger holon under a declared boundary, interface specification, admissibility conditions, substitutability policy, and change policy.

**Show.** A software package, neural-network block, chiplet, power converter, document template, or organizational unit can be treated as module-like only when the claim says what whole is at issue, what boundary it offers, what interface specification governs use, what substitutability policy makes replacement admissible, and what change policy governs separate change. That claim still does not make a direct module relation obtain.

**Show.** A port label, API endpoint label, source-local route label, flow edge, or function name may be a useful clue. It can substantiate a module-interface claim only after the relevant signature, slot, protocol, semantic condition, correspondence, mechanism, evidence relation, conformance expectation, source relation, or reliance relation named by value is declared.

Holon, relation, and episteme: the candidate module and whole retain their admitted holon kinds. A `moduleIn(...)` record is a C.2.1 claim episteme whose content may concern the module holon, one selected dependency structure, or an independently admitted direct module relation occurrence; it is not that relation. Framework and module-description epistemes, authoring Work, publication occurrence, publication form, carrier, effective reference scheme, ClaimScope, and optional model-use structure retain separate identities and direct relations. Method descriptions enter as epistemes; method values enter through their Method pattern. Stratification and architecture-operation labels named by `C.30.STRAT` remain source labels unless `C.30.STRAT` recovers module-interface claim content that A.6.M can repair.

