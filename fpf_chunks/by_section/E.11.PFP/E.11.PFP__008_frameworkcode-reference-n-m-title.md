---
chunk_kind: "child"
pattern_id: "E.11.PFP"
pattern_title: "Framework Publication Form Profile for Markdown"
section_id: "E.11.PFP:section-007"
section_title: "<FrameworkCode>.Reference:<n>.<m> - <Title>"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PFP/E.11.PFP__008_frameworkcode-reference-n-m-title.md"
commit_sha: "73e53b7b1a40aae81d6871f327e5bf7b1c495e23"
heading_path:
  - "E.11.PFP — Framework Publication Form Profile for Markdown"
  - "E.11.PFP:section-007 — <FrameworkCode>.Reference:<n>.<m> - <Title>"
line_start: 103235
line_end: 103265
dependencies:
  - "A.3.2"
  - "C.29"
  - "E.11"
  - "E.17"
  - "E.2.DA"
  - "E.21"
  - "E.24.PUB"
  - "E.4"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.4.FPF"
  - "E.4.PFR"
  - "E.8"
  - "G.11"
keywords:
  - "& Search Queries"
  - "Dependencies"
---

### <FrameworkCode>.Reference:<n>.<m> - <Title>
```

For example, `## STR.Reference:1 - Problem frame - Direction and commitment under changing conditions` identifies the first section of a Strategy architectural-reference unit whose key is `Reference`. `#### FPF.Reference:16.8.2 - Production and situated use are different contributions` identifies a nested section in the FPF Core architectural-reference unit. Use the framework's declared public code; name the framework as well when quoting outside a context that identifies it. The enclosing H1 gives the qualified Architectural Reference title and has a product-declared ToC entry. Changing a former section key requires updating its maintained current returns; changing the title alone does not preserve a former URL fragment.

Close the complete architectural-reference unit with one content-free H2 heading, `## <FrameworkCode>.Reference:End`, after its last paragraph, list or other content and before the next publication unit. For example, the Strategy architectural-reference unit ends with `## STR.Reference:End`. This visible boundary shows where the unit ends when it is copied or retrieved separately. It closes the whole unit, not each numbered subsection; it adds neither a content section nor a pattern-index entry. A heading shown inside a fenced example does not close the unit.

Number sibling sections in reading order, starting at 1, and carry the complete parent path into nested headings. Each nesting level adds one heading level and one ordinal. These ordinals locate sections in this publication unit; their titles state the content functions. An account can combine several E.8 functions in one section or explain one function across several sections. Keep that useful arrangement instead of adding twelve empty sections to match numbers. The rule introduces no limit on useful conceptual scales; physical Markdown heading depth remains a carrier constraint.

`STR.Reference` names a publication unit. Its section addresses are `SectionRef` uses under E.8, not declarations of additional patterns: the pattern index continues to contain the individually declared pattern bodies. Apply the same self-identifying construction to a profile account or other support unit when it needs its own section addresses, using its product-declared unit key. A profile explained inside the architectural reference retains that unit's section path; this text position does not decide the profile's semantic relations.

The prefix lets a reader distinguish a whole-language Problem frame from the Problem frame of one pattern before choosing what to read or cite. Visible names and numbers also survive copying and printing, where a hidden anchor cannot help.

The visible address and title use the ASCII ` - ` separator. Build each clickable fragment from the complete rendered heading according to the target Markdown carrier's rules, including punctuation removal and duplicate handling. When a heading changes, update its direct links in the publication, source templates and public consumers together. Check that the link resolves to the intended heading, then read that target for the answer the link promises. Keep the visible address usable for search and non-clickable copies. E.8:4.1.1 excludes raw HTML from this form, including compatibility anchors.

##### E.11.PFP:4.7.2 - Make the language's long reasoning visible

Use a long mantra when readers need to keep a substantial connected account in attention across several questions, explanations or pattern contributions. Recover that account before compressing it. Identify what the reader is trying to understand or obtain, the questions that must be related, and why their answers belong together. A result dependency is one possible connection; shared assumptions, jointly necessary conditions, alternative constructions, conflicting demands and returns can be equally important. Recover missing reasons through B.5.RA and develop missing constructive joins through E.4.CM. The presence of one operational step per source topic does not preserve the explanation.

Explain how to assemble and revise the answers. Which partial answers can be used now, what remains unknown, and how do local answers constrain the whole? Which changes reopen which other answers? How can a reader choose the next inquiry or construction without mistaking the teaching order for a work sequence? Use the actual subject knowledge to answer these questions. A drawing of connected boxes or a sequence of PatternIDs cannot provide an absent inference, construction or applicability condition.

Keep the full explanation at the scale that owns its subject. E.4.CM:4.5 distinguishes completing an existing pattern, developing a separately useful recurring Method as a pattern, and explaining the material relations of several Methods in an Architectural Reference. The title or mnemonic form settles none of those choices. A framework can have several long mantras for different questions; a repertoire need not acquire one artificial total sequence. Where an existing explanation is sufficient, preserve it and repair its name or access instead of writing a shorter substitute. Where a source explanation enables readers to understand or adapt the contribution, retaining its thesis alone is insufficient.

Give the contribution a recognizable name, a stable existing kind of address, and both a compact reminder and a reachable developed account. Use F.18 when selecting a durable public name. Use the ordinary pattern or Reference section address that fits its owner; no new markup or universal mantra record is required. The compact expression may use questions, relations or actions. Choose it from the explanation rather than restricting the explanation to what fits one memorable sentence. Preserve the subject and scope across the two forms.

Make the account visible at each assembly level where it helps explain the whole. A Framework Reference explains the framework's connected reasoning and returns to its full pattern bodies. A Suite or Library Reference explains the connections introduced at that wider level and returns to the constituent accounts, without copying all their explanations. In a README, show the most consequential reasoning connection in ordinary language, name the long mantra when one is useful, and give a direct return to its full account. This overview is not necessarily a Practical-Use Card. E.11's comparison of entry forms decides whether a card helps a particular first-entry use; it does not decide whether the underlying subject reasoning is worth publishing.

Treat a compact order as a teaching unfolding of the connected reasoning. Explain material branches and returns, and use A.22.CGUS for the actual continuation and structure questions. A phrase order does not determine Work order or qualify a CGUS by itself. Different long mantras can constrain one another through a shared subject or premise: for example, a system construction changes the means of obtaining it, while a capacity limit can make that construction or its promised use worth reconsidering. State that specific connection; neither co-location in a book nor a universal instruction to read every mantra establishes it.

Check what the reader can reconstruct from the publication. Can the reader explain the needed grounds, recognize locally plausible but jointly incompatible answers, and determine which answers a consequential change reopens? Use materially different circumstances when they expose a hidden restriction. These are questions about recoverable explanation and application; fluent recitation, one completed example and a mnemonic advantage do not answer them. Conversely, a source-grounded explanation can be useful without a measured recall advantage. Claims of improved learning, memory or field performance require their own evidence.

