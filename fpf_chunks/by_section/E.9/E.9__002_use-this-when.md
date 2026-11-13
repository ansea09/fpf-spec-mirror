---
chunk_kind: "child"
pattern_id: "E.9"
pattern_title: "Design-Rationale Record (DRR) for FPF Content Decisions"
section_id: "E.9:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9/E.9__002_use-this-when.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "E.9 — Design-Rationale Record (DRR) for FPF Content Decisions"
  - "E.9:0 — Use this when"
line_start: 103680
line_end: 103714
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

- A proposed normative change needs a statement of what FPF should say, why that answer is preferred, and which neighboring patterns or selected non-pattern FPF kind-reference pairs it affects.
- Several such loci must change together. An external record must keep the complete content decision available while authors distribute enduring text across Core.
- Authors would otherwise have to settle the same consequential question separately in several patterns or selected non-pattern FPF kind-reference pairs.
- Authors need to review a deprecation, narrowing, or cross-pattern amendment without reconstructing its rationale from patches, conversations, or scattered notes.

**Not this pattern when.** Normative Core rules belong in their selected loci. Keep campaign and process briefs outside the DRR. If a purely editorial `Delta-0` or `Delta-1` change needs a decision record, use the lightweight variant in `CC-DRR.5` when it fits. Use `E.9.DA` when a DRR already exists and you need to judge its answer, obligations at selected loci, source use, lexical closure, and drafting actionability for a declared downstream authoring use.

#### E.9:0.1 - What goes wrong if missed

- Later readers cannot recover why Core changed, which alternatives were rejected, or which exclusions were intentional.
- Coordinated amendments drift apart when the selected answer survives only in patches, handoffs, or a reviewer's memory.
- Later repairs can fit local wording while losing the constraints supplied by Pillars, taxonomy lenses, the impact graph, practical use, or pattern placement.

#### E.9:0.2 - What this buys

- An external record states the content of a bounded FPF change before authors rewrite Core.
- Four components keep the Problem frame, Decision, Rationale, and Consequences available for later review and replay.
- For a distributed change, the record holds the selected answer while authors draft the enduring Core text at the selected loci.

**First useful move.** State the working FPF problem, selected answer, practical change, selected loci, first substantive drafting action, and nearest boundary in plain, precise language before drafting or landing Core text.

**Cheap stop.** If local wording repair, application of an accepted pattern, or editorial cleanup preserves FPF semantics, obligations, boundaries, names, admissible uses, and normative force, it needs no full DRR.

Use `F.19` for kind-preserving plain rewriting and `E.10` for an unresolved FPF wording-use question. Use `E.17.AUD.LHR` for an overloaded local lexical head inside one publication unit and `C.2.P` for an episteme, publication, or source-use distinction still unresolved after `E.10`. Use `F.18` only for minting a durable reusable name and `E.8` for an authoring-form correction. Use `E.9` when a bounded content decision needs its rationale stated.

**Kind-or-boilerplate diagnostic.** Before proposing wording from a DRR as pattern prose, use `F.19` to separate boilerplate from substantive content. If the remaining wording still obscures its use, name, relation, claim, admissible use, selected locus, user action, or flow position, name the contribution applied: `E.10`, `E.10.ARCH`, `F.18`, or the pattern that defines the object or relation. Keep process, architecture, review, and reference boilerplate in the material it belongs to.

Before using proposed wording in a pattern, establish from the selected answer which object, relation, claim, slot, use, admissibility condition, or scope would change, or that none would change. Use `F.19` and the pattern that defines or constrains the distinction. Introduce Method, Work, application, or ClaimGraph details into ordinary wording only when that distinction changes the decision or a later reliance.

**Primary EntityOfConcern in plain terms.** The external decision-rationale record for one bounded FPF content decision or coordinated change set. The author must be able to recover the problem, selected answer, reasons, consequences, practical change, selected loci, and boundary without inventing them. Add exact C.2.1 identity only when the decision or a named later reliance needs it.

**Primary working reader.** An FPF author, reviewer, or steward uses the DRR to evaluate, challenge, or land a bounded content decision. Downstream pattern readers can use the guidance once it has been incorporated into Core.

