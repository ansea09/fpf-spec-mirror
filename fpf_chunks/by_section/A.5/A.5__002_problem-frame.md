---
chunk_kind: "child"
pattern_id: "A.5"
pattern_title: "Open-Ended FPF Kernel and Extension Layering"
section_id: "A.5:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.5/A.5__002_problem-frame.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "A.5 — Open-Ended FPF Kernel and Extension Layering"
  - "A.5:1 — Problem frame"
line_start: 13551
line_end: 13560
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

**Use this when** adding or revising domain knowledge raises a question about what belongs in the shared Kernel, which assumptions belong in an extension, or which uses depend on a changed declaration.

**First useful move.** Name the contribution, its applicability and the declarations it relies on. Reuse an adequate existing contribution. For a new domain-specific assumption, keep its applicability with the extension rather than making every Kernel use depend on it.

FPF combines shared conceptual grounds with domain Methods by keeping the common commitments stable enough for reuse while allowing extensions to supply different assumptions and laws. Competing explanations can remain available under their respective conditions.

Different domains can require different assumptions and laws. Making a domain-specific assumption an unconditional Kernel commitment would impose it on uses where it may not hold and make those uses depend on its revision. Place domain-specific knowledge in extensions by default, with its applicability stated. Use **A.8** to test a U-kind’s cross-domain contribution and **A.11** to test whether a new ontological value is needed. The declaration rules in **A.5:4** expose dependencies so that a changed declaration can be followed to the uses that rely on it.

