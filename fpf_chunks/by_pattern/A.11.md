---
chunk_kind: "parent"
pattern_id: "A.11"
pattern_title: "Ontological Parsimony"
section_id: null
section_title: null
source_path: "FPF-Spec.md"
output_path: "by_pattern/A.11.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "A.11 — Ontological Parsimony"
line_start: 19679
line_end: 19769
dependencies:
  - "A.8"
  - "C.3"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.18"
  - "F.8"
keywords:
  - "U-kind admission"
  - "composition"
  - "kernel growth"
  - "non-redundancy"
  - "parsimony"
---

## A.11 - Ontological Parsimony

> **Type:** Kernel parsimony and admission discipline pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### A.11:0 - Use This When

Use this pattern when FPF work proposes a new U-kind, core relation, dependent durable value, or public structural name and the current question is whether existing ontology can express the claim without creating a new kind.

Typical moments:

- a new U-kind feels useful after `E.24.UK`;
- a proposed root kind may actually be a dependent value, slot, relation, record, publication form, lens, local frame, or C.3 `U.Kind`;
- two candidates overlap strongly;
- a name is convenient but the ontology may already be expressible through existing patterns.

**Primary EntityOfConcern.** The EntityOfConcern is the parsimony claim for one candidate ontology addition.

**First useful move.** Recover the candidate with `E.24.UK` or the direct governing pattern, then ask what current FPF values, slots, relations, and patterns can already express.

### A.11:1 - Problem Frame

FPF needs enough primitives to be useful, but every new primitive creates learning cost, bridge cost, and future repair cost. Ontological parsimony is not anti-growth. It is the rule that FPF adds a new kind only when composition, reuse, dependent-value settlement, and direct governing patterns cannot express the action-facing claim without material loss.

When source or draft wording proposes a candidate durable value with kind force, treat that as U-kind admission pressure. A.11 is therefore applied after `E.24.UK` recovers the governed object and before naming patterns choose a public label.

### A.11:2 - Solution

Use four gates before admitting the new ontology addition:

| Gate | Test question | Pass condition |
| --- | --- | --- |
| Composition | Can existing U-kinds, slots, relations, dependent values, or direct patterns express the claim? | Pass only when expression by composition loses a reviewable distinction. |
| Non-redundancy | Does the candidate overlap an existing governed value or relation? | Pass only when overlap is bounded and the remaining difference changes admissible claims. |
| Action-facing contribution | What can users claim, compare, repair, stop, rely on, or do because this addition exists? | Pass only when the contribution is not merely naming comfort or source prestige. |
| Sharp boundary | Is there a one-sentence inclusion and exclusion test? | Pass only when readers can distinguish included and excluded cases without private author intent. |

Use this compact record:

```text
ParsimonyAdmissionRecord:
  Candidate:
  RecoveredGovernedObject:
  E24UKDecisionRef:
  ExistingExpressionAttempt:
  MaterialLossIfComposed:
  OverlapWithExistingValues:
  ActionFacingContribution:
  BoundaryTest:
  Disposition:
```

Possible dispositions:

- retain as root U-kind;
- retain as dependent durable value under a root settlement;
- apply C.3 typed reasoning;
- express as slot, relation, record, publication form, lens, local frame, or direct governed value;
- keep as source wording or local name.

### A.11:2.1 - Worked Slices And Maintenance

| Candidate pressure | Parsimony result | Why |
| --- | --- | --- |
| `CoolingPump` as a new root U-kind | Express as a `U.System` or holon holding `CoolingCirculatorRole@Context`, with capability, method, and work claims added only when current. | The useful distinction is role, capability, method, and work around an existing system, not a new universal kind. |
| `Actuator` or another transformer-like noun | Recover the system or holon that participates as transformer in a `U.Transformation`; admit a durable value only if `E.24.UK` shows irreducible action-facing gain. | The bearer of change and the transformation relation are already governed; the noun alone does not create a kind. |
| Provenance-chain wording | Try G.6 evidence-graph and provenance addressing first; admit a new durable value only if the direct evidence or provenance patterns cannot express the needed claim without material loss. | Parsimony tries direct governing patterns before minting a kernel addition. |
| `SmallPart` or similar vague size class | Reject or keep local. | The boundary depends on private scale expectations unless a direct measurement or classification pattern supplies a crisp rule. |

A retained addition also needs a reopen condition. Reopen or lower the admission when usage collapses, overlap with an existing value is discovered, composition becomes adequate, the boundary becomes fuzzy, or the name starts hiding a slot, relation, record, publication form, lens, or local frame. This is maintenance discipline, not a fixed calendar ritual.

### A.11:3 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-A11-1` | The candidate's governed object is recovered before parsimony is judged. |
| `CC-A11-2` | If the candidate uses `U.*` force, `E.24.UK` is applied before F.5, F.8, or F.18 naming. |
| `CC-A11-3` | Existing expression by composition, slots, relations, dependent values, and direct governing patterns is attempted by value. |
| `CC-A11-4` | Material loss is stated as a lost claim, lost distinction, lost boundary, or lost admissible use, not as naming discomfort. |
| `CC-A11-5` | Strong overlap lowers or rejects the candidate unless the difference changes claims. |
| `CC-A11-6` | The final disposition is one of the allowed ontology outcomes, not a vague approval to keep the word. |

### A.11:4 - Relations

- **Builds on:** `E.24.UK`, `A.8`, `C.3`, `F.8`, `F.18`, and direct subject patterns.
- **Coordinates with:** `E.24.CD` for candidate detection and `E.24.PUB` when a publication form or structural name created the pressure.
- **Does not replace:** universal-core testing in `A.8`, typed claim quantification in `C.3`, or naming discipline in Part F.

### A.11:End

