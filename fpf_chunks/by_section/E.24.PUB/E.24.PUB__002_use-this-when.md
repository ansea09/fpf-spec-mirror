---
chunk_kind: "child"
pattern_id: "E.24.PUB"
pattern_title: "Episteme Publication: Availability, Form and Carrier"
section_id: "E.24.PUB:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.PUB/E.24.PUB__002_use-this-when.md"
commit_sha: "e307edbd91c04c1d85661bd309b9944fac251937"
heading_path:
  - "E.24.PUB — Episteme Publication: Availability, Form and Carrier"
  - "E.24.PUB:0 — Use This When"
line_start: 116921
line_end: 116941
dependencies:
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.3.RT.OE"
  - "A.6.REL"
  - "C.2.1"
  - "C.29"
  - "C.3.2"
  - "C.30.AD"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.21"
  - "E.24"
  - "E.24.CD"
  - "E.24.UK"
  - "E.8"
  - "E.9.DA"
  - "F.19"
  - "U.EpistemePublication"
  - "U.View"
keywords:
---

### E.24.PUB:0 - Use This When

Use this pattern when an ontic or another entity is encountered through a card, table, diagram, file, pattern host, dashboard, or similar published expression and the current work depends on knowing what was described, what was made available, and what merely carries the expression.

**Primary working reader.** A practitioner or FPF author distinguishing a claim-bearing episteme, a `U.View`, its expression, a reusable publication form, a carrier or an exact publication occurrence. Open representation methods when the expression also supports reasoning through a correspondence to its subject.

**First useful move.** Put the intended receiving use in the bounded-use declaration itself. Then say which episteme is available, to which declared audience, for which bounded use, through which expression and carrier. Name a reusable form when its constraints matter. Cite a separate plan, decision question or `U.WorkPlan` only when it independently exists and changes the publication claim. Distinguish availability from a claim of actual access or use. Open fuller relation detail when needed to resolve disputed availability, its boundary or publication-occurrence identity.

**What goes wrong if missed.** A visible layout is treated as the described subject, a file is treated as the claims it carries, a diagram is treated as a view merely because it is graphical, or publication availability alone is used to admit a durable `U.EpistemePublication` kind. The receiving work then cannot tell which object changed when claims, layout, carrier, audience, or use changes.

**What this buys.** The user can change a claim, view, form, carrier, audience, or declared bounded use without silently changing all the others. A publication can be inspected and repaired while the subject pattern remains centered on its subject.

**Not this pattern when.**

- Use `C.2.1` when the question is the identity or content of the episteme itself.
- Use `E.17.0` when the question is whether an exact episteme conforms to an exact viewpoint episteme and therefore has `U.View` membership. Use `A.6.3` separately when source-to-receiving viewing construction is current.
- Use `A.6.3.RT` and `A.6.3.RT.OE` to construct or change an expression and recover its correspondence; use `C.29` when a mathematical lens and its inference or transfer conditions are current.
- Use `E.24.CD`, then `E.24`, when a durable ontic is still being considered.
- Use `E.24.UK` when a public `U.*` kind or dependent-kind disposition is unsettled.
- Use the subject pattern directly when publication does not affect the receiving use.

