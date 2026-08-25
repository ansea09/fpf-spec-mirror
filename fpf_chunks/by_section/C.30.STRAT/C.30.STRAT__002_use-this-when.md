---
chunk_kind: "child"
pattern_id: "C.30.STRAT"
pattern_title: "Stratification Wording Precision Restoration"
section_id: "C.30.STRAT:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.STRAT/C.30.STRAT__002_use-this-when.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "C.30.STRAT — Stratification Wording Precision Restoration"
  - "C.30.STRAT:0 — Use this when"
line_start: 58241
line_end: 58254
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.SPR"
  - "A.2"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.17"
  - "E.18"
  - "E.8"
  - "F.18"
  - "G.5"
  - "G.6"
  - "I.2"
keywords:
---

### C.30.STRAT:0 - Use this when

Use this pattern when a source uses a compact architecture or stratification label and that word alone does not tell you what technical claim is being made.

Typical labels are `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, and architecture-operation words such as `block`, `expert`, `cache`, `router`, and `gate`.

**What goes wrong if missed.** A useful local label starts acting as ontology. A `layer` is assumed to be a holon level, control layer, publication layer, scale window, or module boundary without deciding which. A `stack` becomes architecture by name; a `block` becomes a module; an `expert` becomes a system-role kind or performer; a `cache` becomes a state or memory relation; a `router` becomes a decision policy; a `gate` becomes a gate decision. Word shape establishes none of these.

**What this buys.** The reader can keep the source word while making its actual meaning and safe use explicit. Once the object, relation, or claim is clear, use the pattern that defines, constrains, or tests it.

**First useful move.** Copy the sentence and ask: “What does this label name here, what may I infer from it, and what must I do next?” If it is ordinary wording, keep it and stop. If the answer is already clear, use the applicable pattern directly. Otherwise write one line: `label -> recovered meaning; allowed use; blocked overread; next pattern or blocker`. Do not fill an author-facing E.10.ARCH routing row during ordinary project work.

**Not this pattern when.** Do not detour through C.30.STRAT when the object, relation, or claim is already clear. Do not use it merely because a familiar word appears. Ordinary source prose with no FPF claim remains ordinary prose or a quotation.

