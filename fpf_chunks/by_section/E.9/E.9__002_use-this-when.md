---
chunk_kind: "child"
pattern_id: "E.9"
pattern_title: "Design-Rationale Record (DRR) for FPF Content Decisions"
section_id: "E.9:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9/E.9__002_use-this-when.md"
commit_sha: "620f1c50677894b84ea3a84209be4a22f7fb6b5a"
heading_path:
  - "E.9 — Design-Rationale Record (DRR) for FPF Content Decisions"
  - "E.9:0 — Use this when"
line_start: 85732
line_end: 85764
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.6.1"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.10"
  - "E.19"
  - "E.2"
  - "E.22"
  - "E.23"
  - "E.24.PUB"
  - "E.5.4"
  - "E.8"
  - "E.9"
  - "E.9.DA"
  - "F.10"
  - "F.19"
  - "G.11"
  - "G.6"
keywords:
---

### E.9:0 - Use this when

- one proposed normative change needs an explicit by-value account of what FPF should say, why this decision is preferred, and which neighboring patterns or selected non-pattern FPF kind-reference pairs it affects
- several patterns or selected non-pattern FPF kind-reference pairs must move together and one external decision record is needed to keep one bounded coordinated change set (one mutually dependent change set) semantically complete while enduring Core text is redistributed
- one bounded content decision question would otherwise force authors to decide the same load-bearing answer separately across several patterns or selected non-pattern FPF kind-reference pairs
- one deprecation, narrowing, or cross-pattern amendment must stay reviewable without reconstructing intent from patch history, chat memory, or scattered notes

**Not this pattern when.** Do not use `E.9` as the permanent location of normative Core law, as a campaign or process brief, or as the main vehicle for purely editorial `Delta-0` or `Delta-1` cleanup that fits the lightweight variant in `CC-DRR.5`. Use `E.9.DA` when one concrete `DRR` already exists and the question is whether its selected answer, selected-locus obligations, source use, lexical closure, and drafting actionability are adequate for a declared downstream authoring use.

#### E.9:0.1 - What goes wrong if missed

- Core text changes without one explicit rationale account, so later readers cannot recover which alternatives were rejected or which exclusions were intentional
- coordinated multi-pattern amendments drift apart because the temporary selected-answer account survives only in patches, handoffs, or reviewer memory
- future repairs overfit to local wording and silently lose Pillar, taxonomy-lens, impact-graph, practical-use, or pattern-placement discipline

#### E.9:0.2 - What this buys

- one external decision record that states the bounded FPF change by value before Core text is rewritten
- one minimum kernel that keeps Problem frame, Decision, Rationale, and Consequences recoverable for later review and replay
- one temporary convergence record that fixes the selected answer before later drafting fans out, while keeping enduring Core text in the selected patterns and selected non-pattern FPF kind-reference pairs rather than in the DRR

**First useful move.** State the working FPF problem, selected answer, practical change, selected loci, first substantive drafting action, and nearest boundary in ordinary precise language before drafting or landing Core text.

**Cheap stop.** If the change is ordinary local wording repair, application of an already accepted pattern, or editorial cleanup that does not change FPF semantics, obligations, boundaries, names, admissible uses, or normative force, do not open a full DRR. Use the lighter governing pattern for the local repair: `F.19` for kind-preserving plain rewriting, `E.10` for an unresolved FPF wording-use question, `E.17.AUD.LHR` for one overloaded local lexical head inside one publication unit, `C.2.P` for an episteme, publication, or source-use distinction left unresolved after the `E.10` check, `F.18` only when a durable reusable name is being minted, and `E.8` for authoring-form correction. Leave `E.9` for bounded content decisions that need rationale by value.

**Kind-or-boilerplate diagnostic.** When a DRR proposes wording for selected patterns, apply `F.19` to separate boilerplate from remaining content before any wording is treated as pasteable pattern prose. If the remaining content still hides wording-use, naming, relation, claim, admissible-use, selected-locus, user-action, or flow-position precision, the DRR names the applied `E.10`, `E.10.ARCH`, `F.18`, or the pattern that defines the affected object or relation. Process, architecture, review, or reference boilerplate belongs in its own carrier, not in pasteable pattern prose.

Wording proposed in a DRR is not pasteable pattern prose until the selected-answer basis shows what object, relation, claim, slot, use, admissibility, or scope would change—or explicitly says that no such semantic change occurs. Apply `F.19` and the concrete pattern that defines or constrains the live distinction. Do not expand ordinary wording into method, work, application, or ClaimGraph apparatus unless that exact distinction changes the decision or later reliance.

**Primary EntityOfConcern in plain terms.** One external decision-rationale account for one bounded FPF content decision or coordinated change set. It keeps the problem, selected answer, rationale, consequences, practical change, selected loci, and boundary recoverable enough for authoring without invention. Exact C.2.1 identity is added only when the decision or a named later reliance needs it.

**Primary working reader.** The first working reader is an FPF author, reviewer, or steward who must evaluate, challenge, or land one bounded content decision. Downstream pattern readers benefit from the landed Core text; they are not the primary reader of the DRR itself.

