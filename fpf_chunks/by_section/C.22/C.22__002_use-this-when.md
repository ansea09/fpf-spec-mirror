---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__002_use-this-when.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:0 — Use This When"
line_start: 49946
line_end: 49955
dependencies:
  - "A.6.0"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.1"
  - "C.22.2"
  - "C.23"
  - "C.32.P2S"
  - "E.10"
  - "E.18"
  - "G.0"
  - "G.4"
  - "G.5"
keywords:
---

### C.22:0 - Use This When

Use this pattern when a stabilized problem-side episteme must be related to a selector-facing `TaskSignature@Context` for eligibility, acceptance, or policy-governed selection. Typical cases include solver choice, method-family eligibility, QD archive selection, open-ended generator selection, or specialization claims that need a declared task family or work target.

The working moment often sounds like this: "We are about to compare possible ways of doing, but which facts about this problem make a method family eligible, comparable, or unacceptable here?" Use C.22 to construct the smallest four-row `TaskSignature@Context` that a later selector can consume without selecting a method in advance, then assign it to the exact problem-side episteme and receiving use. If problem framing remains contested or stale, use `C.22.2`. If a sufficient signature and assignment already exist and the current question is selection, use `G.5`. If a method is selected and dated enactment is being prepared, use `A.15.2`.

**What goes wrong if missed.** A problem remains a paragraph: selector inputs drift, ordinals and units get mixed, unknowns are coerced, acceptance thresholds leak into CHR fields, and cross-context reuse happens by name instead of Bridge+CL.

**What this buys.** The downstream selection question gets one minimal `TaskSignature@Context` with typed vocabulary, laws, applicability, unknown handling, evidence relations, scope, freshness, and crossing conditions visible before any method family is admitted or compared. Its assignment to the problem-side episteme is replayable, while publication and serialization can vary without changing the signature.

