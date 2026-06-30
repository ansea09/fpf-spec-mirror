---
chunk_kind: "child"
pattern_id: "E.4.DPF.DA"
pattern_title: "Domain Principle Framework Package-Adequacy Evaluation CharacteristicSpace"
section_id: "E.4.DPF.DA:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.DPF.DA/E.4.DPF.DA__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "E.4.DPF.DA — Domain Principle Framework Package-Adequacy Evaluation CharacteristicSpace"
  - "E.4.DPF.DA:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 65178
line_end: 65195
dependencies:
  - "A.19.ECS"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.11"
  - "E.17"
  - "E.19"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.4"
  - "E.4.DPF"
  - "E.4.PFAD"
  - "E.4.PFR"
  - "F.18"
  - "G.11"
  - "G.2"
keywords:
---

### E.4.DPF.DA:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| `E.2.DA` as DPF review | The package is judged against whole-FPF Pillars and domain adequacy is blurred. | Use `E.4.DPF.DA`; invoke `E.2.DA` only for FPF-level effects. |
| `E.21` averaging | Strong individual pattern scores hide weak package architecture. | Evaluate package coordinates directly; use `E.21` only as evidence. |
| Source bibliography as adequacy | Sources are listed but do not change the package. | Return to `G.2`; carry adopted and rejected payload into pattern moves and boundaries. |
| Publication carrier as package proof | The carrier is readable but relation, edition, source, and refresh structures are unrecoverable. | Add `E.4.PFAD`, `E.4.PFR`, source-use, quality, and refresh loci; keep publication as carrier. |
| Invisible carrier structure-account | The carrier never tells what domain or local structure it selected, coarsened, abstracted, or omitted for the intended reader, so readers mistake the package for the domain itself or cannot judge coverage. | Add readme, Preface, ToC, skill-entry, or access-front-door carrier structure-account text, including source-return and structure-capture boundary, then rerun `PFM11`. |
| Skill or MCP access as package proof | The package is callable through a skill or endpoint, so the access carrier is treated as if it proved the framework edition, source, quality, or currentness. | Record the skill or endpoint as an access carrier, expose edition and relation refs, and evaluate the underlying package and patterns through `E.4.DPF.DA` and `E.21`. |
| Skeleton patterns as package proof | The package has pattern headings and canonical sections, but the bodies do not teach a working reader what to do, how to judge boundaries, or how source payload changes action. | Treat the package as `seedOnly`, then harden each body through `E.8` and `E.21` before public or reliance-bearing use. |
| Ontology or conversation package as DPF | The package explains terms, roles, or ways to talk about the domain, but it does not help the intended practitioner resolve typical domain problems with SoTA moves. | Lower `D7` and usually `D11`; keep the ontology or conversation guide as support material and add problem frames, solution moves, worked cases, and anti-pattern repairs. |
| Map hoarding | Huge maps appear before patterns and no work trigger leads to them. | Move maps after pattern bodies or make pattern relations and low-value repairs route to them. |
| Reverse dependency leak | FPF Core or the main monolith starts citing a DPF as required authority. | Move the claim into a Core amendment if it belongs in Core; otherwise keep the dependency one-directional from DPF to Core. |
| Process-state leakage | The package carrier includes `draft`, `DRR`, handoff, ledger, review, admission, or helper-state residue as package content. | Remove process state from package carriers and keep only durable user-facing package content, relation records, source-use boundaries, and refresh routes. |
| Seed promotion | A fast prompt result is treated as public DPF. | Mark `seedOnly`, name missing coordinates, and run `E.23` hardening. |
| Citation-driven `5` | Values rise because more sources, review proof, or maps were added. | Raise values only when action, source grounding, owner routing, adoption, or refresh improves. |

