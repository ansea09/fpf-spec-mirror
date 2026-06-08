---
chunk_kind: "child"
pattern_id: "A.6.0"
pattern_title: "U.Signature - Universal, law‑governed declaration for a SubjectKind on a BaseType"
section_id: "A.6.0:11"
section_title: "Lowering, repair, and refresh conditions"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.0/A.6.0__018_lowering-repair-and-refresh-conditions.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "A.6.0 — U.Signature - Universal, law‑governed declaration for a SubjectKind on a BaseType"
  - "A.6.0:11 — Lowering, repair, and refresh conditions"
line_start: 9005
line_end: 9018
dependencies:
  - "A.2.6"
  - "A.6.1"
  - "A.6.5"
  - "D.CTX"
  - "E.10"
  - "E.10.D1"
  - "E.5.3"
  - "E.8"
  - "U.Mechanism"
  - "U.RelationSlotDiscipline"
keywords:
  - "RFC 2119"
  - "applicability"
  - "bounded context"
  - "laws"
  - "signature"
  - "vocabulary"
---

### A.6.0:11 - Lowering, repair, and refresh conditions

A `U.Signature` remains usable while the four-row Block is stable and all downstream use can recover the same SubjectBlock, Vocabulary, Laws, Applicability, and imported-symbol dependencies.

Repair the signature, or mint a new signature when monotone repair is impossible, if any of these conditions holds:

* a realization, handler, work authorization, evidence proof, bridge policy, or measurement comparison has been written into the Signature Block;
* a downstream use depends on a symbol, law, policy, or edition not exported by this signature or by an imported signature;
* a profile application weakens a law, widens Applicability, or adds operational admission;
* a current SoTA change in algebraic effects, session types, typed effect systems, `profile=FormalSubstrate` signatures, or context normalization changes the declared operation vocabulary, inference kinds, law shape, or no-realization boundary;
* a renamed SubjectKind, BaseType, SlotKind, RefKind, or exported SymbolId no longer recovers the same FPF kind under E.10 and F.18.

Do not repair the signature merely because a later realization, work plan, measurement run, bridge, or evidence record changed. Repair the object governed by that later relation unless the change alters the signature declaration itself or the exact dependency relation by which the later object cites the signature.

