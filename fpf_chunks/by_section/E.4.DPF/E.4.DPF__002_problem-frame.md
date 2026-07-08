---
chunk_kind: "child"
pattern_id: "E.4.DPF"
pattern_title: "Domain Principle Framework Authoring and Publication-or-Access Carrier Assembly"
section_id: "E.4.DPF:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.DPF/E.4.DPF__002_problem-frame.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "E.4.DPF — Domain Principle Framework Authoring and Publication-or-Access Carrier Assembly"
  - "E.4.DPF:1 — Problem frame"
line_start: 64946
line_end: 64970
dependencies:
  - "C.33"
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
  - "E.4.FPF"
  - "E.4.PFAD"
  - "E.4.PFR"
  - "E.8"
  - "F.18"
  - "G.11"
  - "G.2"
keywords:
---

### E.4.DPF:1 - Problem frame

Use this pattern when a group needs to create a domain principle framework or local practice framework grounded in FPF: for example a hydroponic-cucumber framework, a neural-network architecture framework, or a Codex-process framework.

Primary `EntityOfConcern`: the authoring method for a bounded FPF-grounded framework edition. The first useful output is not a list of candidate pattern names. It is an authoring spine with context, SoTA source pack, architecture decision, name-card route, pattern drafts, relation and edition records, publication carrier, access carrier, quality loop, and currentness route.

Default artifact contract for a request such as "make a DPF about this topic" separates developer and user carriers. In a campaign or repository setting, create a developer decision carrier such as `SUBSTANTIVE-DRR.md` or `DPF-DRR.md` governed by `E.9` and checked by `E.9.DA`; it carries the source basis, selected architecture, PFAD decision, candidate pattern split, relation plan, quality plan, and rejected alternatives. Create a user-facing framework publication or access carrier named by the individual framework, such as `<DomainOrPractice>-PRINCIPLES-FRAMEWORK.md`, `<PublicFrameworkName>.md`, a split readme, pattern, and appendix set, a skill pack, or an MCP-backed access service; it is the access route through which readers or agents use the DPF edition. Optional source-pack, PFR, quality-run, package-evaluation, skill-manifest, or access-service files may be separate when they need independent maintenance, but they must not be copied into the user carrier as process state.

Use this pattern when the work creates a framework. Use `E.11` or `E.17` when the work only changes how existing material is exposed to readers.

Plain vocabulary for adoption:

| Public phrase | Use it for |
| --- | --- |
| `principle framework` | The general public phrase for an FPF-grounded framework of patterns, decisions, relation records, source basis, publication, quality, and refresh. |
| `Domain Principle Framework` | A principle framework for a domain such as greenhouse cucumbers, neural-network architecture, or safety certification practice. |
| `Local Practice Framework` | A principle framework for one organization, project, team, role context, or local operating practice. |
| `bounded context` | The domain or local situation where this framework's meanings hold. |
| `framework edition` | One versioned state of the framework with dependency, compatibility, publication, quality, and refresh records. |
| `framework publication carrier` | A reader-facing carrier for a framework edition: readme, preface, table of contents, pattern bodies, support maps, relation records, and refresh route as needed. |
| `framework access carrier` | A user-facing or agent-facing access carrier for a framework edition: all-in-one publication carrier, split document set, card set, skill pack, MCP-backed access service, retrieval route, or assistant integration. It exposes the selected framework edition; it does not define the framework architecture, source pack, quality result, runtime dependency, or work authority by itself. |
| `local monolith` | Workspace and editorial shorthand for one all-in-one framework publication carrier. Do not use it as the public framework name, and do not treat it as the framework architecture itself. |

Old intake labels such as `SPF`, `TPF`, or broad `xPF` remain source aliases until `F.18` settles a durable public name and any admissible short form. `ZPF` has a campaign-local `F.18` name card that selects `FoundationalPrinciplePatternSet` / "foundational principle pattern set" as the primary name and keeps `ZPF` only as a mnemonic alias, not as a public "zero principles" framework name.

