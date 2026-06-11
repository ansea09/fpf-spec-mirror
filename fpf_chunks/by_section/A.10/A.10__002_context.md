---
chunk_kind: "child"
pattern_id: "A.10"
pattern_title: "Evidence Graph Referring (C‑4)"
section_id: "A.10:1"
section_title: "Context"
source_path: "FPF-Spec.md"
output_path: "by_section/A.10/A.10__002_context.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "A.10 — Evidence Graph Referring (C‑4)"
  - "A.10:1 — Context"
line_start: 18522
line_end: 18537
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2.8"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.4"
  - "A.6"
  - "B.1"
  - "B.1.1"
  - "B.3"
  - "B.4"
  - "C.16"
  - "C.26.1"
  - "C.26.2"
  - "C.26.3"
  - "C.28"
  - "E.17.EFP"
  - "F.9"
keywords:
  - "SCR/RSCR"
  - "authority-reliance evidence path"
  - "claim support"
  - "evidence"
  - "evidence carrier"
  - "exact authority reference"
  - "generated-explanation source support"
  - "probe/distributed/export/causal evidence"
  - "provenance"
  - "register excerpt"
  - "status register"
  - "traceability"
---

### A.10:1 - Context

FPF is a holonic framework: wholes are built from parts (A.1, A.14), and reasoning travels across scales via Γ‑flavours (B.1). To keep this reasoning honest and reproducible, every **published assertion** must be evidenced through concrete **symbol carriers** and **well‑typed transformations** performed by an **external TransformerRole** (A.12, A.15). Per A.7, `Describe_EoC_DescEp` is the describing morphism from `EntityOfConcern` to Description episteme; specification use is granted only by neighboring pattern governing the claiming gates such as A.6.2, C.2.3, A.21, C.16, E.17, or E.10. **Publication** makes Description epistemes available through publication forms, faces, units, renderings, or carriers and is **not execution**. Any physical/digital release, rendering, or upload is **Work** by an external transformer **on carriers**, cited in SCR.

Practitioner shorthand:
> **Claim → (Proof or Test) → Confidence badge**
> …where the proof/test is traceable to real carriers and to an external system/Transformer who executed an agreed method.

This pattern defines the **Evidence Graph Referring Standard** common to all Γ‑flavours (Γ\_sys — formerly Γ\_core, Γ\_epist, Γ\_method, Γ\_time, Γ\_work) and clarifies:
(a) the difference between **mereology** (part‑whole; builds holarchies) and **provenance** (why a claim is admissible; does *not* build holarchies);
(b) the run‑time / design‑time separation (A.4) across **Role–Method–Work** (A.15).

Use this when a model, report, metric, confidence badge, review note, or QL reading is starting to act like evidence but the carrier, transformer, method, time stance, or provenance edge is still implicit. The action is to turn the assertion into a small because-graph: name the claim, name the carriers, name the external transformer role, name the method or work trace, state the time/coverage condition, and attach the resulting evidence edge to the claim rather than to the holon itself.

Useful output: a claim that can answer "because of which carriers, by which transformer, using which method, and when?" without making provenance pretend to be part-whole structure.

