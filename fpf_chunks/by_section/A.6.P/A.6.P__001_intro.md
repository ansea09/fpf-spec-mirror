---
chunk_kind: "child"
pattern_id: "A.6.P"
pattern_title: "U.RelationalPrecisionRestorationSuite — Relational Precision Restoration (RPR) — Kind‑Explicit Qualified Relation Discipline"
section_id: "A.6.P:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.P/A.6.P__001_intro.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "A.6.P — U.RelationalPrecisionRestorationSuite — Relational Precision Restoration (RPR) — Kind‑Explicit Qualified Relation Discipline"
  - "A.6.P:intro — Intro"
line_start: 11999
line_end: 12048
dependencies:
  - "A.10"
  - "A.2.4"
  - "A.2.6"
  - "A.6"
  - "A.6.0"
  - "A.6.5"
  - "A.6.6"
  - "A.6.8"
  - "A.6.9"
  - "A.6.A"
  - "A.6.B"
  - "A.6.H"
  - "A.6.Q"
  - "A.6.S"
  - "A.7"
  - "C.2.1"
  - "C.2.2a"
  - "C.26"
  - "C.3.3"
  - "E.10"
  - "E.17"
  - "E.8"
  - "F.17"
  - "F.18"
  - "F.9"
keywords:
  - "QualifiedRelationRecord"
  - "RelationKind"
  - "coupling"
  - "endpoint referential compression"
  - "export"
  - "language-state seam"
  - "lexical guardrails"
  - "measurement"
  - "probe"
  - "relation precision restoration"
  - "under-specified relational language"
---

## A.6.P — U.RelationalPrecisionRestorationSuite — Relational Precision Restoration (RPR) — Kind‑Explicit Qualified Relation Discipline

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (Core)

**Plain-name.** Relational precision restoration suite.

**Intent.** Provide a family-level, reusable discipline for repairing a recurring defect in FPF texts: **under‑specified relational language** (often phrased as a seemingly binary verb) that actually hides **(i)** higher arity (missing participant positions), **(ii)** multiple semantic change classes, **(iii)** asymmetry between `U.Viewpoint` specifications and `U.View` instances, **(iv)** boundary requirements (signature invariants vs admissibility vs deontics vs evidence/work), and **(v)** endpoint referential compression (pronominal/metonymic stand‑ins and over‑broad kinds).
RPR patterns turn “umbrella relations” into **kind‑explicit, slot‑explicit, qualified relation records** with an explicit **change-class lexicon** and **lexical guardrails**, while respecting the **A.6 Signature Stack** and **A.6.B Boundary Norm Square** separation.

**Placement.** Part A → cluster **A.6 Signature Stack & Boundary Discipline** → header pattern for the **relation‑precision restoration family** (A.6.5, A.6.6, A.6.8, A.6.9, A.6.H, and future A.6.x patterns).

**Builds on.**

* **A.6** (stack layering + boundary discipline requirements).
* **A.6.B `U.BoundaryNormSquare`** (L/A/D/E routing; claim atomicity; cross‑quadrant references).
* **A.6.S `U.SignatureEngineeringPair`** (TargetSignature vs ConstructorSignature; canonical constructor verb mapping; effect‑free constructor ops).
* **A.6.0 `U.Signature`** (SlotSpec requirement for argument positions).
* **A.6.5 `U.RelationSlotDiscipline`** (SlotKind/ValueKind/RefKind stratification + canonical slot verbs; `bind` reserved for name binding).
* **E.8** (pattern authoring discipline; Tell–Show–Show; SoTA echoing hygiene).
* **F.18** (promise vs utterance vs commitment; avoids “interface‑as‑promiser” category errors).
* **E.10** (LEX‑BUNDLE discipline; I/D/S versus publication-form and carrier lanes; L‑SURF token discipline; reserved primitives; Tech↔Plain pairing). *(Referenced conceptually; no extra authoring apparatus implied.)*

**Coordinates with.**

* **A.2.4 `U.EvidenceRole`** (witness semantics: role/timespan/freshness metadata for decision‑relevant witness sets).
* **A.2.6 scope + `Γ_time` discipline** (avoid implicit “current/latest”; make time selectors explicit when time matters).
* **A.7 Strict Distinction** (Object≠Description≠Carrier; avoid treating evidence/logs as properties of prose).
* **A.6.2–A.6.4** (effect‑free episteme morphisms, epistemic viewing/retargeting as disciplined slot writes).
* **A.10 evidence discipline** (witnesses are carrier‑anchored; freshness is adjudicated in work/evidence lanes).
* **C.2.1 `U.EpistemeSlotGraph`** (slot read/write profiles for constructor operators, when declared).
* **C.3.3 `U.KindBridge` + `CL^k` discipline** (repairing endpoint kind mismatches; kind-level congruence + loss notes).
* **E.17 MVPK / multi‑view publication** (faces are views; “no new semantics”; viewpoint accountability).
* **E.19 pattern quality gates** (review/refresh discipline for guardrails and conformance lists).
* **F.17 `UTS`** (when ambiguity clusters become recurring vocabulary: publish stable `RelationKind` tokens and facet head phrases as UTS/LEX‑governed term assets, so rewrites don’t live only inside A‑patterns).
* **F.9 Bridges + CL** for cross-Context or cross-plane reuse (no silent sameness).
* **C.2.2a, A.16, A.16.1, A.16.2, B.4.1, and B.5.2.0** for the language-state seam: language-state chart positions, admissible moves, pre-threshold cue preservation, route publication, admissible retreat/reopen, and prompt-shaped continuations that are not yet stable relation publication; use **A.16.0** only when lineage, branch, loss, or handoff history itself must be published as an explicit trajectory account.
* **C.2.LS, C.2.4, C.2.5, C.2.6, and C.2.7** for language-state facet governance: articulation explicitness, closure degree, language-state anchoring mode, and the language-state representation-factor bundle may be cited by RPR patterns but are not governed here.

**Specialisations already in Core.**
These retained specialisations are current because they each carry one stable reusable repair-load family. Their mnemonic heads remain admissible entry points, but generic `A.6.P` does **not** treat token recurrence alone as sufficient to mint one new specialisation per overloaded trigger word.

* **A.6.5**: RPR for n‑ary relations and slot discipline (archetype: “putting something into a place”; explicit SlotKinds + ValueKind/RefKind + slot‑operation lexicon).
* **A.6.6**: RPR for “relative‑to / basedness” claims (explicit `baseRelation` token + scoped, witnessed base declarations + base‑change lexicon; lexical red‑flags for `anchor*`).
* **A.6.8 (RPR‑SERV)**: RPR for the “service” cluster polysemy (facet‑explicit `serviceSituation` lens; canonical rewrites for `service`/`server`/`service provider`; classification tests for clause vs access point vs provider commitment vs work+evidence).
* **A.6.9 (RPR‑XCTX)**: RPR for cross‑Context “same / equivalent / align / map” talk (explicit Bridges with direction, endpoint refinement, substitution licence, CL and loss notes; blocks silent inversion and “alignment” umbrella verbs).
* **A.6.H (RPR‑WHOLE)**: RPR for “whole/part/integrity/complete” polysemy (WHOL triggers + Boundary–Parthood–Fold–Order/Time–Completeness lens; routes turnkey/end‑to‑end into A.15 coverage; includes publication-form↔referent↔work level test).


