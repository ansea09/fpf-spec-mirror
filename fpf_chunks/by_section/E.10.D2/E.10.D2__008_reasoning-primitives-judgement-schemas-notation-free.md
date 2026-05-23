---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "Intension–Description–Specification Discipline (I/D/S)"
section_id: "E.10.D2:7"
section_title: "Reasoning primitives (judgement schemas, notation‑free)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__008_reasoning-primitives-judgement-schemas-notation-free.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "E.10.D2 — Intension–Description–Specification Discipline (I/D/S)"
  - "E.10.D2:7 — Reasoning primitives (judgement schemas, notation‑free)"
line_start: 53735
line_end: 53806
dependencies:
  - "A.7"
  - "C.2.1"
  - "C.2.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.10"
  - "F.15"
  - "F.4"
  - "F.5"
  - "F.8"
  - "F.9"
  - "U.BoundedContext"
  - "U.EpistemeSlotGraph"
keywords:
  - "I/D/S"
  - "description"
  - "intension"
  - "specification"
  - "testable"
  - "verifiable"
---

### E.10.D2:7 - Reasoning primitives (judgement schemas, notation‑free)

> Judgements are **mental moves**—they assert what follows when premises hold. They do **not** imply queries, storage, or workflows.

1. **Description link (with DescriptionContext)**

   ```
   U.T, C, Vp ⊢ isDescriptionOf(TDesc, U.T, C, Vp)
   ```

   *Reading:* `TDesc` is the Context‑local Description of `U.T` in Context `C` under Viewpoint `Vp`. Its `subjectRef` decodes to `DescriptionContext = ⟨DescribedEntityRef(U.T), C, Vp⟩` (IDS‑13, C.2.1 §6.1).

2. **Spec link (Spec‑gate, viewpoint‑local)**

   ```
   isDescriptionOf(TDesc, U.T, C, Vp) ∧ U.Formality(TSpec) ≥ F4
      ∧ testableInvariants(TSpec) ∧ harnessBound(TSpec)
      ∧ sameDescriptionContext(TSpec, TDesc)
      ⊢ isSpecOf(TSpec, U.T, C, Vp)
   ```

   *Reading:* Only when F‑mode, testability, harness, and a matching `DescriptionContext` are present may we judge `TSpec` a Specification of `U.T` in `C` under Viewpoint `Vp`.

3. **Role characterisation**

  ```
   isDescriptionOf(RoleDesc, U.Role, C, Vp)
   ∧ characterises(RoleDesc, U.RCS) ∧ characterises(RoleDesc, U.RSG)
   ⊢ characterisedBy(U.Role, {U.RCS, U.RSG}) @C
  ```

   *Reading:* The role is *characterised by* the RCS/RSG as presented in the Description (which is pinned to `(C, Vp)`), not that it “contains” them.

4. **State conformance predicate**

   ```
   checklistFor(RoleDesc, state S) = χ
   ∧ evidence E within window W
   ⊢ conformsToState(E, χ, W) ⇒ attestation(subject ∈ S @C, W)
   ```

   *Reading:* Evidence satisfies the checklist for state `S`, yielding a state attestation.

5. **Transition admissibility**

   ```
   U.RSG allows (S → S') @C
   ∧ attestation(subject ∈ S @C, W)
   ∧ conformsToState(E', checklistFor(S'), W')
   ⊢ admissibleTransition(subject : S → S' @C)
   ```

   *Reading:* A move from `S` to `S'` is admissible when RSG permits it and `S'` is satisfied.

6. **Status / state separation guard**

   ```
   statusOverKU(KU, σ) ∧ stateInRSG(ρ)
   ⊢ σ ≠ ρ  (distinct planes)
   ```

   *Reading:* A status over a knowledge unit is not a role‑state.

7. **No Cross‑context import**

   ```
   isDescriptionOf(TDescA, U.T, CA, VpA) ∧ isDescriptionOf(TDescB, U.T, CB, VpB) ∧ CA≠CB
   ⊢ ¬equateByLabel(TDescA, TDescB)  (bridges required in F.9)
   ```

   *Reading:* Identical wording across Contexts (and Viewpoints) does not grant equivalence; only Bridges may relate them.

