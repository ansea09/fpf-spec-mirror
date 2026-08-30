---
chunk_kind: "child"
pattern_id: "E.24.PUB"
pattern_title: "Ontic Description and Publication Discipline"
section_id: "E.24.PUB:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.PUB/E.24.PUB__002_use-this-when.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "E.24.PUB — Ontic Description and Publication Discipline"
  - "E.24.PUB:0 — Use This When"
line_start: 91237
line_end: 91257
dependencies:
  - "A.6.3"
  - "A.6.REL"
  - "C.2.1"
  - "C.29"
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

**Primary working reader.** A practitioner or FPF author deciding whether a visible thing is a claim-bearing episteme, a `U.View`, a publication form, a C.29 representation, a `U.PresentationCarrier`, or evidence of one publication occurrence.

**First useful move.** Put the intended receiving use in the bounded-use declaration itself. Then say, in one sentence, which episteme edition is available, to which declared audience, for which bounded use, in which publication form, and on which presentation carrier. Cite a separate plan, decision question, or `U.WorkPlan` only when it independently exists and changes the publication claim; it is not a second required statement of intended use. Availability establishes none of actual access, reliance, use, Work, or result. When a precise performed-Work claim is independently current, recover each exact actual performer through A.13 and let A.15.1 independently admit the dated Work; add F.6 only when that claim or its receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment. F.6 identifies neither assignment nor performer, and missing or failed F.6 leaves the Work intact. Follow A.6.1 for an operation binding, C.11 for a `ChoiceResult`, or the exact access, reliance, or use relation without reproducing its test here. Open the heavier publication-relation declarations only when the receiving use depends on availability, its declared boundary, or publication-occurrence identity.

**What goes wrong if missed.** A visible layout is treated as the described subject, a file is treated as the claims it carries, a diagram is treated as a view merely because it is graphical, or a currently available episteme is turned into a durable `U.EpistemePublication` kind. The receiving work then cannot tell which object changed when claims, layout, carrier, audience, or use changes.

**What this buys.** The user can change a claim, view, form, carrier, audience, or declared bounded use without silently changing all the others. A publication can be inspected and repaired while the subject pattern remains centered on its subject.

**Not this pattern when.**

- Use `C.2.1` when the question is the identity or content of the episteme itself.
- Use `E.17.0` when the question is whether an exact episteme conforms to an exact viewpoint episteme and therefore has `U.View` membership. Use `A.6.3` separately when source-to-receiving viewing construction is current.
- Use `C.29` when representation elements and the operations admitted by a representation are current.
- Use `E.24.CD`, then `E.24`, when a durable ontic is still being considered.
- Use `E.24.UK` when a public `U.*` kind or dependent-kind disposition is unsettled.
- Use the subject pattern directly when publication does not affect the receiving use.

