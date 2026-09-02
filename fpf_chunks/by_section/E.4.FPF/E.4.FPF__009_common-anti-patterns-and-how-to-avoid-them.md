---
chunk_kind: "child"
pattern_id: "E.4.FPF"
pattern_title: "First Principles Framework Form and Publication-or-Access Carrier Assembly"
section_id: "E.4.FPF:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.FPF/E.4.FPF__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "E.4.FPF — First Principles Framework Form and Publication-or-Access Carrier Assembly"
  - "E.4.FPF:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 70630
line_end: 70645
dependencies:
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.11"
  - "E.11.PFP"
  - "E.17"
  - "E.2"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.4"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.4.PFAD"
  - "E.4.PFR"
  - "E.9.DA"
  - "F.18"
  - "F.19"
  - "G.11"
  - "G.2"
  - "I.2"
keywords:
---

### E.4.FPF:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
|---|---|---|
| FPF as one DPF | FPF is treated as a domain package, so its first-principles and transdisciplinary burden disappears. | Use `E.4.FPF` for FPF form and `E.4.DPF` only for domain or local dependents. |
| Unit, form, route, or carrier as FPF | A Readme, Preface, ToC, logical index, publication form, all-in-one file or site, split-file bundle, skill-pack bundle, or MCP route is treated as the framework edition itself—or a publication unit or access route is called a carrier without an exact `U.PresentationCarrier` and bearing relation. | Record units, forms, exact presentation carriers, and access routes in their separate `FPFEditionRebuildabilityRecord` fields; keep authoritative claims in the Core patterns and their edition relations. |
| Rival FPF manifest | A DPF or LPF `FrameworkPackageManifest` or a duplicate unit, form, carrier, or route field is copied into FPF even though the rebuildability record already names the needed sources, publication units and forms, presentation carriers, access routes, projections, relations, and refresh route. | Use the `FPFEditionRebuildabilityRecord` fields and the assembly result; reopen this record decision only when a genuinely missing FPF value is shown. |
| Rival practical-entry declaration | Readme authoring, assembly, and validation keep separate ordinary-entry, card, scope, or limit lists, so the same key can change form or disappear without one reviewable change. | Consume the single current FPF declaration in `E.4.FPF`; change it only after the `E.11` reader-use comparison and propagate that one change to its true consumers. |
| Directly patched all-in-one carrier | Selected sources are correct, but the assembled carrier is edited outside the declared source assembly, so a mismatch or lost predecessor span can be hidden. | Assemble from the exact predecessor and complete selected sources with explicit replacement or insertion boundaries; stop on any source, index/body, boundary, or preservation mismatch. |
| Repository recipe as framework law | One helper, path layout, template set, insertion syntax, or campaign identifier becomes part of the public FPF Method. | State the semantic assembly invariants here; keep the current implementation recipe and examples in maintainer documentation or tool help. |
| Invisible FPF entry route | Readme or Preface helps adoption but never says what first-principles structures it foregrounds, what it leaves to the pattern bodies, or who it is written for. | Add a publication-unit structure account while preserving its thin projection status and keeping form and carrier claims separate. |
| Build apparatus as FPF front door | Generated-source comments, candidate records, digests, source paths, or machine identity fields appear before the reader can find a working question, or a new profile shifts an established compact ToC merely to display them. | Preserve the compact reader opening and direct Readme-first route; keep reproducibility and exact edition evidence in maintainer or package records, and project another cue only when its possible values change a named reader action. |
| Whole-FPF quality by local score | Good `E.21` values or successful landing are treated as whole-FPF adequacy. | Run `E.2.DA` for the scoped FPF object and declared use; use local results only as evidence loci. |
| DPF reverse dependency | A good DPF discovery is treated as a hidden Core dependency. | Propose a Core amendment and update the affected Core patterns and edition relations before FPF depends on that result. |
| Access route as authority | A skill, MCP endpoint, retrieval index, or assistant integration is read as source, decision, work, or currentness authority, or the route is silently treated as the carrier it returns. | Record an exact skill-pack, index, or response carrier only when one exists; keep the service or route separate and route generated text, tool work, evidence, assurance, and refresh claims to their subject patterns. |

