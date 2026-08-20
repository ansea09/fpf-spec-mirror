---
chunk_kind: "child"
pattern_id: "A.6.S"
pattern_title: "U.SignatureEngineeringPair - Signature engineering via a ConstructorSignature and a TargetSignature"
section_id: "A.6.S:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.S/A.6.S__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "A.6.S — U.SignatureEngineeringPair - Signature engineering via a ConstructorSignature and a TargetSignature"
  - "A.6.S:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 20951
line_end: 20961
dependencies:
  - "A.12"
  - "A.3"
  - "A.6.0"
  - "A.6.2"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "A.6.6"
  - "A.6.B"
  - "A.7"
  - "C.2.1"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.19"
keywords:
  - "ConstructorSignature"
  - "EFEM"
  - "MVPK views (no new semantics)"
  - "TargetSignature"
  - "appear"
  - "claim register"
  - "editioning"
  - "no epistemic agency"
  - "quadrant classification is governed by A.6.B)"
  - "retargeting"
  - "signature engineering"
  - "slot/base change lexicon"
  - "two-signature arrangement"
---

### A.6.S:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern                                    | Symptom                                                                                                   | Why it fails                                                                | How to avoid or repair                                                                       |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **One publication tries to be TargetSignature plus ConstructorSignature work record** | The same publication mixes the TargetSignature, ConstructorSignature construction notes, review notes, and operational gates. | Collapses TargetSignature, ConstructorSignature, and Work evidence; quadrant mixing becomes inevitable. | Split into TargetSignature plus ConstructorSignature; classify gates as mechanism-side admissibility conditions and duties as deontic commitments. |
| **Silent semantic edits**                       | A law or applicability quietly changes; consumers discover it through breakage.                           | Treats a new TargetSignature edition as the same TargetSignature edition.                                 | Require retargeting to a new SoI edition for semantic changes.                              |
| **Retargeting disguised as “editing”**          | Ref changes and by‑value edits are described with the same verb.                                          | Loses the slot discipline stratification and review clarity.                | Use A.6.5 canonical verbs and `Edit<SlotQualifier>` vs `Retarget<SlotQualifier>`.           |
| **Views become “alternative truths”**           | PlainView says one thing, TechCard says another, and nobody knows which is canonical.                     | A view gained semantics rather than projecting them.                        | Treat MVPK faces as viewings; put canonical semantics in the SoI and reference it.          |
| **Contract talk without quadrant discipline**   | “The interface promises…” is used to state invariants, obligations, and entry conditions interchangeably. | Blends laws, deontics, admissibility, and evidence.                         | Use A.6.B claim classes and claim register entries; rewrite claims into the proper quadrant. |
| **Episteme‑as‑actor** | Text says “the ConstructorSignature builds, validates, or publishes the SoI”. | Violates no epistemic agency and hides the admitted System and dated Work; a system-role kind or assignment may also be mistaken for the actor. | Rewrite: the episteme describes constructor operations; an admitted System performs the Work; F.6 identifies the assignment under which it acted. A short account may omit an unused assignment identifier. |

