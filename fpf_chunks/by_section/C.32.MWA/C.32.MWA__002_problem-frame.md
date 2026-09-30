---
chunk_kind: "child"
pattern_id: "C.32.MWA"
pattern_title: "Synthesize an Architecture Account of Methods and Their Use"
section_id: "C.32.MWA:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.MWA/C.32.MWA__002_problem-frame.md"
commit_sha: "181b9e798f6ebae07c0eb871c0a91e6c9b1fbce8"
heading_path:
  - "C.32.MWA — Synthesize an Architecture Account of Methods and Their Use"
  - "C.32.MWA:1 — Problem frame"
line_start: 73990
line_end: 74017
dependencies:
  - "A.15.1"
  - "A.22"
  - "A.3.1"
  - "B.1.5"
  - "B.2"
  - "C.17"
  - "C.18"
  - "C.30"
  - "C.30.AD"
  - "C.30.ILC"
  - "C.30.STRAT"
  - "C.32"
  - "C.32.MLAO"
  - "C.36"
  - "E.23.CDI"
  - "E.4.DPF"
  - "E.4.PFAD"
  - "F.6"
keywords:
---

### C.32.MWA:1 - Problem frame

Use this pattern when a decision about related methods and their use depends on several structures that do not line up one-for-one: how methods are composed, how work is performed, what supports it, and how methods are developed or retained. The question may involve different wholes and relations even when one source shows them in aligned rows.

The subject is one or several related Methods considered together with their performance, support and development. Identify the relevant Methods, performed or planned Work, participating or supporting Systems, descriptions and models, capabilities and providers, and cultural relations separately. Select only what can change the decision. The account can include relations beyond a Method's constituents: using a platform to perform a Method does not make that platform part of the Method. Each precise C.30 architecture claim still names its own holon and selected structure.

Here **method** is the main name for a reusable way of doing. **Practice** can name the same way, often emphasizing its established use, as E.10:0.2c.21a explains. A claim about performed Work, a community or a description requires those separately identified objects; the wording itself introduces no broader Practice whole.

The primary working reader is an architect, methodologist, practice designer, or domain-framework author who has already found useful source material but cannot safely copy its table, stack, lifecycle, or diagram as the architecture account.

**First useful move.** State whether the architecture question concerns arrangements already used in representative Work or a proposed organization of Method use. These are the obtaining and possible-future entries. Keep that status for each relied-on claim: an existing provider or development activity does not make the proposed use actual. Then write the architecture question in one sentence and select only the structures that can change its answer.

**What goes wrong if missed.** A source layout is mistaken for the arrangement it describes. A list becomes levels, a procedure becomes a hierarchy, overlapping activities become a sequence, a model becomes the thing modeled, or a future design acquires fictitious performed Work. A local repair may also look successful only because its unresolved burden moved to another structure or scope.

**What this buys in practice.** The reader gets a short, usable account of the selected Methods and their use, structures and relations, their correspondences, the main conflict or moved burden, and the alternative that changes the current decision. The account can remain ordinary prose; a table or symbolic form is optional assurance.

**Not this pattern when.**

- Use the direct Method, Work, subject, description, capability, provider, or cultural-change pattern when only one such claim is unclear.
- Use base `C.32` when the need is a palette of architecture candidates for one already grounded architecture question, rather than one coherent answer about Methods and their use from several non-isomorphic structures.
- Use `C.30.ILC` and `C.32.MLAO` when an already recovered cross-scope conflict or residual is the main subject.
- Do not use this pattern for one clear Method decomposition, one procedure order, a carrier index, a universal level stack, a mandatory record schema, domain filling, product-roster generation, or lifecycle design.
- A practitioner can use this Method to prepare evidence for a framework or project decision. Making that decision, establishing a product, publishing a description, or putting a proposed organization of Method use into effect remains separate work.

For the smaller question of what encompassing work is being done through one current action, start with **B.1.5.EW**. It can expose a missing constituent or a changed condition without requiring this full synthesis. Use **B.1.5.RS** when the difficulty is preserving encompassing uses while replacing one constituent. Return here when the answer depends on several structures that do not correspond one-for-one.

The result is an **architecture synthesis for Methods and their use**: a readable account connecting the selected Methods, Work and other identified objects through the relations relevant to one architecture question, with their consequences for the decision. The account describes how these objects fit together; whether any Methods form a composite Method remains a separate claim under B.1.5.

