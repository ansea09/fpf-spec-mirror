---
chunk_kind: "child"
pattern_id: "E.4.PFAD"
pattern_title: "Principle-Framework Architecture Decision"
section_id: "E.4.PFAD:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFAD/E.4.PFAD__002_problem-frame.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "E.4.PFAD — Principle-Framework Architecture Decision"
  - "E.4.PFAD:1 — Problem frame"
line_start: 70388
line_end: 70401
dependencies:
  - "A.15.1"
  - "A.22"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.1.5"
  - "C.30.AD"
  - "C.30.STRAT"
  - "C.32.ADR"
  - "C.32.MWA"
  - "C.32.PAD"
  - "C.36"
  - "E.11.DSG"
  - "E.17"
  - "E.19"
  - "E.21"
  - "E.23"
  - "E.23.CDI"
  - "E.24.PUB"
  - "E.4"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.4.PFR"
  - "E.9"
  - "F.18"
  - "F.19"
  - "G.11"
  - "G.2"
keywords:
---

### E.4.PFAD:1 - Problem frame

Use this pattern when an author is choosing among a new or revised principle framework, a contribution to an existing framework, another product that is not a framework, a thinner publication or access route, and no new product, and that choice will settle an identity, edition, relation, intended-use, or publication decision that later work must use. The decision may concern the public field and first use, framework edition, dependencies, initial pattern placement or relations, the kind and identity or change rule of a non-framework product, or the publication or access consequence. Another author or reviewer must need the answer and its rationale for later action.


Here *product* has the Plain management meaning declared in `E.4:4.1`; it is not a technical kind. When a non-framework product is selected, the answer names its direct subject, kind, and the identity, current-state, provision, publication, availability, or other relations used by the decision. Name a maintenance relation only when that stronger claim separately obtains and changes the answer. If a kind or relation that can change the answer is unresolved, keep it as an explicit decision question and do not invent `U.Product`.


A proposed new or substantially revised DPF also needs an answer about its field boundary. That answer says who can first use the framework and for what, which connected problem families and useful results it covers, what the current FPF and admitted DPFs already provide, and what remains uncovered. It compares serious alternatives, tests one representative case that crosses problem families, states where the evidence runs out, and names the change that will require a refresh. Together these must support one independently usable pattern language. One pattern or a narrow authoring slice is not a DPF merely because it has a broad title or a coherent carrier.

If a cheap search, curated reading route, useful contribution to an existing framework, suitable non-framework product, or stop answers the immediate need without settling such a boundary, use that result and stop. Do not open a framework-architecture DRR merely because `E.4.PFAD` exists.

When the architecture question is live, use `E.4.PFAD` to state the framework-specific content of one ordinary `E.9` DRR. Decision Work selects the answer; the DRR records it. This pattern is a practitioner-facing profile and locator. No PFAD relation or second decision record is created, and acceptance remains separate.

