---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent/Extent, and Typed Reasoning (Kind‑CAL)"
section_id: "C.3:1"
section_title: "Purpose & Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__002_purpose-rationale.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "C.3 — Kinds, Intent/Extent, and Typed Reasoning (Kind‑CAL)"
  - "C.3:1 — Purpose & Rationale"
line_start: 37176
line_end: 37192
dependencies:
  - "A.1"
  - "A.2.6"
keywords:
  - "classification"
  - "extension"
  - "intension"
  - "kind"
  - "subkind"
  - "type"
  - "typed reasoning"
  - "vocabulary"
---

### C.3:1 - Purpose & Rationale

**What you get.**

1. A **neutral typed layer**: name *what* a claim quantifies over (**Kinds**) without binding to any particular “type technology” (OWL, PL types, shapes…).
2. A clean **split of characteristics**:
   – **Scope (G)** = *where* a claim holds (USM, set‑valued over **Context slices**).
   – **Kind extent** = *which instances* belong to a kind **inside** a given slice.
   – **F** = *how strictly* content is expressed (C.2.3).
   – **R** = *how well supported* (evidence & congruence penalties).
3. **Typed reuse across Contexts**: a dedicated **KindBridge** with **`CL^k`** (type‑congruence), so you can predict risk **without** touching F or G.
4. **Manager‑oriented maps**: when to invest in **formalization** (F), when to expand/narrow **Scope** (ΔG), when to test across **subkinds** (R), and what kind of **bridge** you should expect.

**Why it helps.**
Teams routinely overspend on proofs for **instance‑level** questions and underspecify scope for **class‑level** claims. By naming the **Kind**, you plan **ΔF/ΔR** correctly and keep **G honest**. Typed checks also block unsafe compositions (“we were talking about different things”).


