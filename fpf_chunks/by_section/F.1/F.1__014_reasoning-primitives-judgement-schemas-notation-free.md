---
chunk_kind: "child"
pattern_id: "F.1"
pattern_title: "Domain‑Family Landscape Survey"
section_id: "F.1:13"
section_title: "Reasoning primitives (judgement schemas, notation‑free)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.1/F.1__014_reasoning-primitives-judgement-schemas-notation-free.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "F.1 — Domain‑Family Landscape Survey"
  - "F.1:13 — Reasoning primitives (judgement schemas, notation‑free)"
line_start: 80127
line_end: 80166
dependencies:
  - "A.11"
  - "A.7"
  - "D.CTX"
  - "E.10.D1"
  - "F.0.1"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.9"
  - "G.0"
  - "G.1"
keywords:
  - "authoritative source"
  - "canon"
  - "context map"
  - "domain‑family survey"
  - "scope notes"
  - "versioning"
---

### F.1:13 - Reasoning primitives (judgement schemas, notation‑free)

> These are **mental moves**, not queries. They read “given these thoughts, this conclusion is safe to hold (conceptually).”

1. **Context set for a line**
   `line L declared ⊢ Contexts(L) = {C₁,…,Cₙ}`
   *Reading:* For a unification line **L**, the Contexts you deliberately keep in view are `{C₁,…,Cₙ}` (from your Cards).

2. **Heterogeneity check**
   `families(L) = F ⊢ heterogeneous(L) ≡ (|distinct(F)| ≥ 3)`
   *Reading:* Your cut is heterogeneous if it spans at least three **domain families**.

3. **Parsimony check**
   `Contexts(L)=R, families(L)=F ⊢ parsimonious(L) ≡ (∀f∈F: 1≤|R∩f|≤3)`
   *Reading:* Each family contributes a few Contexts, not a phonebook.

4. **Locality assertion**
   `term w, C∈Contexts(L) ⊢ meaning(w)@C is local`
   *Reading:* A word’s sense is **context‑local**; no global meaning is implied.

5. **Time‑stance guard**
   `C has stance s∈{design,run} ⊢ claims@C must respect s`
   *Reading:* If a Context is design‑time, do not make run‑time claims in it (and vice versa).

6. **Trip‑wire recall**
   `C lists tripWires T ⊢ for any w∈T, require Context‑prefix when speaking`
   *Reading:* Words on the trip‑wire list must be spoken with the Context name.

7. **Bridge embargo**
   `C₁≠C₂ ⊢ no‑equivalence(C₁,C₂) within F.1`
   *Reading:* F.1 never asserts equivalence across Contexts; postponement is principled, not procrastination.

8. **Context sufficiency probe**
   `common‑word w used in L ∧ w not covered by any trip‑wire ⊢ consider adding a Context that makes w differ`
   *Reading:* If a frequent word has no deliberate sense‑split in your cut, you may be missing a Context.

9. **Memory rule**
   `|Contexts(L)| too large ⊢ reduce until a careful mind can recite them unaided`
   *Reading:* The survey should live in memory, not in a registry.

