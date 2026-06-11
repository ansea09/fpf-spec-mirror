---
chunk_kind: "child"
pattern_id: "F.19"
pattern_title: "Ontology-First Plain Technical Rewriting"
section_id: "F.19:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/F.19/F.19__002_use-this-when.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "F.19 — Ontology-First Plain Technical Rewriting"
  - "F.19:0 — Use this when"
line_start: 75962
line_end: 75989
dependencies:
  - "A.19.SPR"
  - "A.6.P"
  - "A.7"
  - "C.16.P"
  - "C.2.P"
  - "C.30.P"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.18"
  - "E.19"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "F.18"
  - "I.2"
keywords:
---

### F.19:0 - Use this when

Use `F.19` when a bounded piece of technical prose is trying to say something precise, but the reader must pass through role labels, container words, status words, process traces, quality proof, repeated negative catalogues, reference boilerplate, or pattern-application metaphors before the object and action are visible.

Typical in-scope prose includes:

- FPF pattern prose;
- `DRR` text and architecture notes;
- review findings and quality-loop records;
- project-facing FPF guidance;
- source prose being rewritten for FPF use;
- other technical prose whose accepted ontology, domain model, controlled vocabulary, or role model must survive simplification.

**What goes wrong if missed.** Authors replace one official-sounding phrase with another. The text becomes smoother or shorter while the hidden kind error remains, or it becomes easy to read by losing the FPF kind, slot, role, claim boundary, or admissible-use boundary.

**What this buys.** Plain technical wording becomes an ontological discipline with less apparatus: fewer words, clearer objects, fewer repeated negative catalogues, and no loss of technical semantics.

**First useful move.** Mark the span under repair. Split it into content candidates and apparatus candidates before rewriting either side.

**Not this pattern when.**

- If the problem is only one overloaded word or head after the content is visible, apply `E.10`.
- If the problem is a durable reusable name, apply `F.18`.
- If the span already names the content-bearing relation, source-use relation, state-family value, architecture label, characteristic, quality term, function wording, evidence claim, gate claim, work claim, decision claim, or other FPF object named by value, apply the governing pattern for that object.
- If the source text is only being observed and not admitted into FPF-governed prose, keep the observation source-side.

**Primary EntityOfConcern in plain terms.** One phrase-level, sentence-level, row-level, paragraph-level, or small-section technical-prose repair whose goal is kind-preserving plain expression.

