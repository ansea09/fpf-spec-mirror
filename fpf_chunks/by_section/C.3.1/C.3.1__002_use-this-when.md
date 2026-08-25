---
chunk_kind: "child"
pattern_id: "C.3.1"
pattern_title: "U.Kind and U.SubkindOf Core"
section_id: "C.3.1:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.1/C.3.1__002_use-this-when.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "C.3.1 — U.Kind and U.SubkindOf Core"
  - "C.3.1:0 — Use This When"
line_start: 43670
line_end: 43683
dependencies:
  - "A.1"
  - "A.11"
  - "A.2"
  - "A.2.6"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "A.8"
  - "C.2.1"
  - "C.2.3"
  - "C.29"
  - "C.3"
  - "C.3.2"
  - "C.3.3"
  - "E.24.UK"
  - "F.5"
  - "F.8"
keywords:
  - "U.SubkindOf direct relation"
  - "classification equivalence"
  - "closed finite domain"
  - "continuity"
  - "criterion entailment"
  - "kind identity"
  - "membership criterion"
  - "participant-determined occurrence"
  - "preorder"
---

### C.3.1:0 - Use This When

Use this pattern when work must recover one reusable kind, decide whether one kind is a subkind of another, or decide whether the same kind continues across a changed `KindSignature` edition.

**What goes wrong if missed.** A source or practice label becomes an identity key, `U.SubkindOf` carries dependency or construction, a finite sample is mistaken for a universal order, mutually classifying kinds are silently merged, or a changed declaration is treated as automatically new or automatically harmless.

**What this buys.** The user gets an operational kind-continuity test, a replayable subkind test, and a small preorder that remains distinct from declaration identity, current extension, evidence, bridging, and public naming.

**Primary EntityOfConcern.** One `U.Kind` individual recovered through its candidate domain, operative membership condition, intended member/non-member distinction, and continuity rule; or one proposed `U.SubkindOf` relation between exact kind participants within declared applicability.

**First useful move.** Write the ordinary claim first: `CoolingPumpKind is a subkind of PumpKind because every candidate that satisfies the declared cooling-pump condition also satisfies the pump condition.` Then name the exact criteria and applicability that make that statement true. Introduce an occurrence designator or formal equivalence grouping only when a receiver uses it.

**Not this pattern when.** Use C.3.2 for a declaration, admissibility result, candidate classification, or extension; C.3.3 only for a claimed correspondence between independently identified distinct kinds; and `E.24.UK` when admitting another durable public kind rather than using an already admitted `U.Kind` individual.

