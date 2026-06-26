---
chunk_kind: "child"
pattern_id: "F.1"
pattern_title: "Domain‑Family Landscape Survey"
section_id: "F.1:8"
section_title: "Invariants (normative, lightweight)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.1/F.1__009_invariants-normative-lightweight.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "F.1 — Domain‑Family Landscape Survey"
  - "F.1:8 — Invariants (normative, lightweight)"
line_start: 79918
line_end: 79931
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

### F.1:8 - Invariants (normative, lightweight)

1. **Context ≡ U.BoundedContext.** In this pattern, *Context* always means **U.BoundedContext** (per E.10.D1).
2. **Locality.** Words are **local to their Context**; no global meaning is implied or imported.
3. **Heterogeneity.** Each unification line considers **≥ 3 distinct Domain families** (labels are informative only).
4. **Parsimony.** Prefer few, canonical Contexts per family (1–3) that jointly expose the key sense splits.
5. **No bridging here.** No equivalence or mapping is asserted between Contexts in F.1. (Bridges live in **F.9**.)
6. **DesignRunTag honesty.** If a canon fixes a DesignRunTag, note it. Do not reinterpret.
7. **Didactic primacy.** Each Context Card must be readable by a thoughtful engineer in **under two minutes**.
8. **Domain‑family neutrality.** Domain families **carry no semantics**; they SHALL NOT be used for inheritance, inference, or bridge implication.
9. **Scope naming separation.** `Scope gist` on Cards is **didactic only**; formal *Scope/entityOfConcern* (=`USM.ScopeSlice(G)` ⊕ `entityOfConcern(GroundingHolon, ReferencePlane)`) is declared **in G.0–G.1**, not in F.1.
10. **Diversity signature present.** Each Context Card PUBLISHES a `dSig` in the 5‑characteristics form.
11. **Collision rule.** If any pair of Cards has `dSig` matching on ≥3 characteristics, mark **Near‑Duplicate** and either merge  into one slot or replace one by a Context from a different domain‑family. Record action in SCR.

