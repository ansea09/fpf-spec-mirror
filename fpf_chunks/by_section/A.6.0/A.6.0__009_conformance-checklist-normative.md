---
chunk_kind: "child"
pattern_id: "A.6.0"
pattern_title: "U.Signature - Universal, law-governed declaration for a SubjectKind over a RangedValueKind"
section_id: "A.6.0:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.0/A.6.0__009_conformance-checklist-normative.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "A.6.0 — U.Signature - Universal, law-governed declaration for a SubjectKind over a RangedValueKind"
  - "A.6.0:7 — Conformance Checklist (normative)"
line_start: 10236
line_end: 10263
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

### A.6.0:7 - Conformance Checklist (normative)

| ID | Requirement |
| --- | --- |
| **CC‑A.6.0‑1** | A conformant text labelled **`U.Signature`** **SHALL** expose the **four‑row Signature Block**: *SubjectBlock; Vocabulary; Laws; Applicability*. A visual split of SubjectBlock into **Subject** and **Quantification** lines is allowed; it still counts as **one** conceptual row. |
| **CC‑A.6.0‑2** |  The Signature Block MUST remain conceptual: no code or CI metadata, no tool bindings, no execution steps, no implementation details, and no Γ-builder exports. Dependency and export metadata belongs in the `SignatureManifest` (§4.4.1), not inside the four-row Block. |
| **CC‑A.6.0‑3** | Applicability **binds** a `U.BoundedContext`; if cross-context use is intended, a **Transport clause** is *named* (Bridge reference) without re-stating Part F and B.3 details (including any **CL^plane**). |
| **CC‑A.6.0‑4** | Where numeric comparability is implied, Applicability **binds** to **CG-Spec and MM-CHR** legality (normalize-then-compare; scale and unit alignment). |
| **CC‑A.6.0‑5** | Families that specialise A.6.0 (e.g., A.6.1, method profiles, or discipline profiles) MAY add extra constraints and projection views, but MUST preserve the four-row Block as the canonical core (no extra semantic rows). |
| **CC‑A.6.0‑6** | Under E.10 and E.5, tokens MUST respect strata and family segregation: never redefine Kernel tokens in an Extension, Context, or Instance signature; instead, import and align. |
| **CC‑A.6.0‑7** | The **Laws** row contains **axioms and invariants** only; **AdmissibilityConditions** and operational admissions **MUST** appear only in **A.6.1 Mechanisms** that consume this Signature. |
| **CC‑A.6.0‑8 (No‑Realization on Signatures with EffectDiscipline).** | If **EffectDiscipline** appears in **Vocabulary**, faces **MUST** carry a **`No‑Realization` pin** and **MUST NOT** publish handler semantics; any **EffectRealization** is referenced (A.6.1) by id only. |
| **CC‑A.6.0‑9 (CHR‑binding without units or Transport).** | Signatures that declare **measurability intent** (e.g., PrincipleFrame) **SHALL NOT** publish **units, ReferencePlane, ComparatorSet, or Transport**; those are declared only by **UNM** and cited by edition or ref-id where consumers require numeric comparability. |
| **CC‑A.6.0‑10 (UNM‑priority on faces).** | Any numeric or comparable claim on a Signature face **pins** **CG-Spec and ComparatorSet edition ids** and, where scale or plane conversion occurs, **UNM.TransportRegistry edition** with **CL and CL^plane policy-ids**; **penalties are recorded only in `R` or `R_eff`**. |
| **CC‑A.6.0‑11 (Bridge‑only crossings).** | Cross-context or cross-plane reuse of Signature claims **MUST** name a **Bridge** (UTS row) and **MUST NOT** imply implicit equivalence by label; losses are recorded via **CL** (penalties → **R**). |
| **CC‑A.6.0‑12 (Profile conformance).** | If the Signature declares `profile=FormalSubstrate` or `profile=PrincipleFrame`, the corresponding **profile pins** in §4.2 are **mandatory**; failure to emit them makes the Signature **non‑conformant** for that profile. |
| **CC‑A.6.0‑13 (Profile morphism discipline).** | Applying a profile **SHALL** satisfy §4.6 (structure‑preserving morphism: SubjectBlock preserved, Vocabulary and Laws monotone, Applicability restrictive, no admissibility or handlers). |
| **CC‑A.6.0‑14 (SlotSpec for argument positions).** | Any `U.Signature` whose **Vocabulary** declares n‑ary relations or operators **SHALL** provide, for each argument position, a **SlotSpec** triple `⟨SlotKind, ValueKind, refMode⟩` (with `refMode ∈ {ByValue \| RefKind}`) as per A.6.5 `U.RelationSlotDiscipline`. |
| **CC‑A.6.0‑15 (Slot and Ref lexical discipline on signatures).** | Names of SlotKinds and RefKinds used in SlotSpecs **MUST** obey E.10 and A.6.5 lexical guards: tokens ending with **`…Slot`** denote SlotKinds only; tokens ending with **`…Ref`** denote either RefKinds or episteme fields whose type is a RefKind; no ValueKind ends with these suffixes. |
| **CC‑A.6.0‑16 (SlotSpecs for n‑ary relations).** | Any `U.Signature` whose **Vocabulary** declares an **n‑ary relation or morphism** **SHALL** assign to each parameter position a `SlotSpec_i = ⟨SlotKind, ValueKind, refMode⟩` as defined in **A.6.5 `U.RelationSlotDiscipline`**; SlotSpecs live inside the Vocabulary row’s per‑relation parameter block and **MUST NOT** introduce additional rows beyond the four‑row Block. |
| **CC‑A.6.0‑17 (SlotSpec-based substitution laws).** | Specialisations of A.6.0 that define **substitution, retargeting, or profile application** over n-ary relations or morphisms (e.g., **A.6.2–A.6.4**) **SHALL** phrase their rules in terms of **SlotSpecs** (SlotKind, ValueKind, and RefKind) rather than unnamed parameter indices and **SHALL** obey the `…Slot` and `…Ref` lexical discipline in **A.6.5** and **F.18**. |
| **CC‑A.6.0‑18 (Manifest required for reuse).** | If a signature is intended to be imported or reused, it MUST include a `SignatureManifest` (§4.4.1) with explicit `id`, `version`, `imports`, and `provides`. |
| **CC‑A.6.0‑19 (Imports acyclicity).** | If `imports` is present, it MUST be acyclic (no cycles in the signature import graph). |
| **CC‑A.6.0‑20 (No redeclare across imports).** | If `imports` is present, `provides(S)` MUST NOT re‑declare any symbol already provided by any transitive import of `S`. |
| **CC‑A.6.0‑21 (No ghost dependencies).** | If `imports` is present, any non-Kernel **SymbolId** referenced in the **SubjectBlock** or **Vocabulary** rows that is **not** provided by this signature MUST be provided by some imported signature. ClaimIds, BridgeIds, policy-ids, and EditionIds are exempt. |
| **CC‑A.6.0‑22 (Realization opacity).** | If a family publishes any Realization of a `U.Signature`, that Realization **MUST** treat imported Signatures as **opaque** (depend only on their `provides` symbols and cited ClaimIds), and **MUST NOT** reference internal structure of imported Signatures. |
| **CC‑A.6.0‑23 (Monotone Realization).** | A Realization **MAY** tighten but **MUST NOT** relax the Signature’s Laws; if weaker laws are needed, publish a new Signature (or publish an explicit refinement morphism) rather than weakening the existing Signature Laws. |

