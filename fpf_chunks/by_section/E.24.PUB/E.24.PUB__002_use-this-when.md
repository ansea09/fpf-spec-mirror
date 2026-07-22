---
chunk_kind: "child"
pattern_id: "E.24.PUB"
pattern_title: "Ontic Description and Publication Discipline"
section_id: "E.24.PUB:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.PUB/E.24.PUB__002_use-this-when.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "E.24.PUB — Ontic Description and Publication Discipline"
  - "E.24.PUB:0 — Use This When"
line_start: 85409
line_end: 85434
dependencies:
  - "A.19"
  - "A.19.ECS"
  - "A.22"
  - "C.2.1"
  - "C.30"
  - "C.30.AD"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "E.17.0"
  - "E.21"
  - "E.24"
  - "E.24.CD"
  - "E.24.UK"
  - "E.8"
  - "E.9.DA"
  - "F.19"
keywords:
---

### E.24.PUB:0 - Use This When

Use this pattern when a text, table, card, record, schema, diagram, view, source row, or pattern section may be confused with the ontic it describes.

Typical moments:

- a pattern file is treated as if it were the ontic rather than a publication of an ontic-description episteme;
- a card, record, table, schema, diagram, or view is cited as if its form created the governed object;
- an ontic description starts to grow generic warnings about neighboring EoCs instead of staying centered on the ontic;
- a subject pattern about architecture, structure, characteristic space, transformation, episteme, or bounded context begins with publication-use guards while the subject matter becomes background;
- a source packet or review packet is used as if it carried ontology authority by appearance.

**First useful move.** Name four objects separately: the ontic under concern, the ontic-description episteme, the publication of that description, and the publication form used by that publication.

**What goes wrong if missed.** The pattern becomes about how to talk about a thing rather than about the thing. A diagram becomes an architecture claim or selected structure, a score table becomes characteristic space, a problem card becomes problem ontology, and a pattern host becomes the ontic it publishes.

**What this buys.** The author can put publication-form and description-use issues in the right place without pushing the primary subject pattern into semio-bias.

**Not this pattern when.**

- If the current question is whether a construct deserves a durable ontic, use `E.24.CD` and then `E.24`.
- If the current question is whether a `U.*` spelling in a title, filename, heading, ToC row, table, or visible publication structure should be retained, governed by C.3 typed reasoning, or renamed, use `E.24.UK`.
- If the current question is generic multi-view publication or viewpoint packaging, use `E.17` and its dependent patterns.
- If the current question is phrase-level precision restoration, use `E.10`, `E.10.ARCH`, `F.19`, or the relevant precision-restoration pattern.
- If the current question is an architecture description as its own subject matter, use `C.30.AD`; E.24.PUB supplies only the boundary among the ontic, its ontic-description episteme, the publication, and the publication form.

