---
chunk_kind: "child"
pattern_id: "E.4.DPF"
pattern_title: "Domain Principle Framework Authoring and Publication-or-Access Carrier Assembly"
section_id: "E.4.DPF:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.DPF/E.4.DPF__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "d1f696e7c7767705206a8cacd9f6ed48e4dc5b02"
heading_path:
  - "E.4.DPF — Domain Principle Framework Authoring and Publication-or-Access Carrier Assembly"
  - "E.4.DPF:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 69859
line_end: 69889
dependencies:
  - "C.33"
  - "C.33-C.35"
  - "C.34"
  - "C.35"
  - "E.10"
  - "E.11"
  - "E.17"
  - "E.19"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.4"
  - "E.4.DPF.DA"
  - "E.4.PFAD"
  - "E.4.PFR"
  - "E.8"
  - "F.18"
  - "G.11"
  - "G.2"
keywords:
---

### E.4.DPF:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Checklist promoted to framework | Local tips are published as a principle framework without source, relation, or quality work. | Treat the checklist as local process text until `G.2`, `E.8`, `E.4.PFR`, and `E.21` are satisfied. |
| Source summary as SoTA | A literature summary replaces adopted and rejected source payload. | Build a `G.2` source pack and carry each load-bearing source into solution, boundary, or example text. |
| Ontology catalog as framework | The package classifies the domain or defines terms, but it does not tell a practitioner what typical problem is live or what SoTA solution move avoids a known failure. | Keep ontology as support material; draft or repair DPF patterns around problem frames, positive solution moves, worked cases, anti-patterns, and refresh. |
| Publication carrier as architecture | The publication or access carrier hides relation and dependency records. | Add `E.4.PFAD`, `E.4.PFR`, and source-return records before relying on the carrier as architecture evidence. |
| Invisible framework story | A DPF carrier reads as a neutral list of principles, but the reader cannot tell what source or domain structures were selected, why this route is for them, what was deliberately coarsened, abstracted, omitted, or left to source return, or whether the carrier is a second-step coarsening after an architecture description or view. | Add a short carrier structure-account in the readme, Preface, or equivalent carrier, then evaluate it through `E.4.DPF.DA` rather than scattering explanation into every pattern body. |
| Generated candidate authority | Search or LLM output becomes the framework because it is fluent. | Use `C.35` for admission, then decide candidate selection through `E.4.PFAD` or `C.32`. |
| Skeleton carrier as DPF | A file has a ToC, headings, and very short pattern-shaped sections, but readers still cannot apply the patterns without reconstructing the missing guidance from the DRR or source notes. | Keep it as `seedOnly`; harden each DPF pattern through `E.8`, evaluate through `E.21`, and only then assemble the user publication carrier. |
| Access carrier as framework | A skill pack, MCP endpoint, retrieval route, or assistant integration is treated as the framework itself because it is what agents call. | Record it as an access carrier through `E.4.PFR`, expose framework edition and currentness refs, and route generated, tool, evidence, currentness, or work claims to their governing patterns. |
| Future framework fabricated | A pre-PFAD record points to the absent framework or claims its actual structures. | Create a current intended-result description and one proposal episteme; wait for PFAD and realization before architecture-description use. |
| Claim wrapper collection | Every candidate organization claim becomes another episteme. | Keep typed claim nodes in the proposal's one ClaimGraph unless a separately grounded claim episteme has its own EoC and use. |
| Proposal layout as subject organization | Headings or ClaimGraph organization are treated as the proposed framework organization. | Recover described position kinds, proposed subject relation signatures, constraints, invariants, dependency directions, alternatives, basis, and questions. |
| Coverage and acceptance union | One field mixes coverage criterion with WorkPlan acceptance target. | Keep the coverage node complete and cite the plan target separately. |
| Availability as relevance | A missing dependency is assumed blocking, or an available dependency is assumed current for next use. | Fill availability and use relevance independently; only the exact combined state determines the next-use consequence. |
| Local grounding bridge | Unequal proposal and description grounding is admitted to avoid returning. | Stop and return to C.2.1 and A.6.2; add F.9 only for an actual cross-context bridge. |

Adoption risk tripwires:

| Risk | Early repair |
| --- | --- |
| Public name settles before the kind is settled. | Keep the intake name as a source alias and route durable naming through `F.18`. |
| Generated or searched material is trusted because it uses familiar FPF words. | Admit the carrier through `C.35`, then decide selected use through `E.4.PFAD`, `E.4.PFR`, or the pattern governing that use. |
| Core, domain, or local edition changes but old users keep following stale guidance. | Add dependency, compatibility, migration, deprecation, supersession, and refresh records through `E.4.PFR` and `G.11`. |
| Enterprise evidence is confidential or proprietary. | Publish a safe local carrier while keeping internal source packs, examples, role assignments, and approval evidence under an explicit local stewardship assignment. |
| No assigned steward can answer whether the framework is current, adopted, or broken in use. | Assign steward roles for the framework edition, source pack, relation records, local publication, quality evidence, and refresh plan. |
| Reader errors and skipped records are treated as training noise. | Treat repeated misuse as adoption telemetry and route it to `E.23` improvement or `G.11` refresh. |
| Compatibility debt hides behind a version label or package manifest. | Record the impacted relations, compatibility boundary, migration work, and blocked runtime or build reading in `E.4.PFR`. |

