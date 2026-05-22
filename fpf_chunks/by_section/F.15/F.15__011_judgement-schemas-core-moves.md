---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "SCR/RSCR Harness for Unification"
section_id: "F.15:10"
section_title: "Judgement schemas (core moves)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__011_judgement-schemas-core-moves.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "F.15 — SCR/RSCR Harness for Unification"
  - "F.15:10 — Judgement schemas (core moves)"
line_start: 66620
line_end: 66645
dependencies:
  - "B.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.0.1"
  - "F.1"
  - "F.1-F.14"
  - "F.14"
keywords:
  - "SenseCell testing"
  - "acceptance tests"
  - "regression tests"
  - "static checks"
  - "validation"
---

### F.15:10 - Judgement schemas (core moves)

> Representative mental moves; each “fires” one cluster of SCRs.

1. **Anchoring**
   `Seed σ : context C, C ∈ Contexts(L) ⊢ anchored(σ)`  *(S1)*

2. **Local clustering**
   `∀σ∈Σ: context(σ)=C ⊢ cluster_C(Σ) = Local‑Sense λ`  *(S3)*

3. **Role-Description anchoring**
   `Role Description τ names ⟨C,λ⟩ ⊢ singleCell(τ)`  *(S7)*

4. **Row reuse**
   `intent(ρ') ≈ intent(ρ) ⊢ reuse(ρ) ∨ justify_mint(ρ')`  *(S11)*

5. **Bridge assertion**
   `C₁≠C₂ ∧ compare(⟨C₁,λ₁⟩,⟨C₂,λ₂⟩) ⊢ Bridge(CL,kind,loss)`  *(S12–S13)*

6. **Windowing**
   `Status Σ exhibits temporal/scale variance ⊢ define windows(Σ); forbid Σ‑splitting`  *(S14)*

7. **SoD guard**
  `SoD(τᵢ ⟂ τⱼ) ⊢ ¬exists Role Description υ that conflates {τᵢ,τⱼ}`  *(S15)*


