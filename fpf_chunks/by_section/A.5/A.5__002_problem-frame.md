---
chunk_kind: "child"
pattern_id: "A.5"
pattern_title: "Open-Ended FPF Kernel and Extension Layering"
section_id: "A.5:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.5/A.5__002_problem-frame.md"
commit_sha: "996ae39ce00b4a9c9b59b48a4f1446b2175dcffb"
heading_path:
  - "A.5 — Open-Ended FPF Kernel and Extension Layering"
  - "A.5:1 — Problem frame"
line_start: 13728
line_end: 13738
dependencies:
keywords:
  - "FPF architecture"
  - "declarative modularity"
  - "dependency versus specialization"
  - "domain extensions"
  - "extensibility"
  - "kernel boundaries"
---

### A.5:1 - Problem frame

FPF helps practitioners combine shared conceptual grounds and reusable methods with suitable domain methods.
FPF can support that use across changing disciplines only if it:

* **(i)** remains *stable* and *self‑consistent* over multi‑decade timespans;
* **(ii)** *invites*, rather than resists, the continual influx of new disciplinary knowledge; and
* **(iii)** allows multiple, even competing, explanatory lenses to coexist without forcing a “winner‑takes‑all” unification.

Different domains can require different assumptions and laws. Making a domain-specific assumption an unconditional Kernel commitment would impose it on uses where it may not hold and make those uses depend on its revision. Place domain-specific knowledge in extensions by default, with its applicability stated. Use **A.8** to test a U-kind’s cross-domain contribution and **A.11** to test whether a new ontological value is needed. The declaration rules in **A.5:4** expose dependencies so that a changed declaration can be followed to the uses that rely on it.

