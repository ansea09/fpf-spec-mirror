---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:1"
section_title: "Intent and applicability"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__002_intent-and-applicability.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:1 — Intent and applicability"
line_start: 89536
line_end: 89557
dependencies:
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.9"
  - "B.3"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "C.29"
  - "E.10.D1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
keywords:
  - "Bridge-supported use"
  - "CL"
  - "bridge"
  - "bridge reading"
  - "cross-context alignment"
  - "direction"
  - "loss notes"
  - "state export"
  - "weakest-link scope"
---

### F.9:1 - Intent and applicability

**Intent.** Provide a conceptual discipline for relating `SenseCells` from different `U.BoundedContext`s. A Bridge states what relation holds, which direction matters, how much congruence is admitted by `CL`, what is lost, and which cross-context use remains admissible.

**Applicability.** Use this pattern when an author needs to compare local senses across contexts, reuse a familiar label, connect design-time and run-time senses, compare two standards' terms, or justify a row in the Concept-Set table.

**Primary EntityOfConcern in plain terms.** One Bridge Card relating two `SenseCells` across different `U.BoundedContext`s. The EoC is not a transport chain, not a work process, not a role assignment, and not one global meaning layer.

**Admissible move in plain terms.** Declare bridge kind, direction, `CL`, loss, and admitted use so cross-context sense use stays inspectable without collapsing local meanings into silent equivalence.

**Primary working reader.** An author, checker, or practitioner preparing one bridge card, comparative bridge note, or concept-set row that depends on cross-context sense use.

**Use this when.** Use F.9 when the same term, role name, quality label, status label, measurement label, method label, or structural label appears in more than one context and the team is about to treat that overlap as if it were already equivalence or safe substitution.

**What goes wrong if missed.** Teams fall back to shared labels, string-equals shortcuts, or informal analogies, then quietly smuggle equivalence, substitution, structural inference, or role assignment across contexts without stating kind, direction, `CL`, or loss.

**What this buys.** One explicit bridge discipline that lets a team compare contexts and reuse names while keeping direction, loss, and the limits of admissible substitution visible.

**Not this pattern when.** Not F.9 when the case is still only one local context, when the needed claim is a role assignment, performed-work attribution, evidence use, status use, source use, publication use, assurance claim, gate claim, decision claim, or mathematical-lens use. Use the direct governing pattern first; cite F.9 only when cross-context sense alignment itself is live.

**Recognition versus assurance note.** Intent, applicability, this boundary, and the first worked case are the recognition block. Bridge kinds, `CL`, conformance, and relation sections are assurance blocks; they tighten the same Bridge Card claim instead of widening F.9 into role assignment, work execution, governance, or one global meaning layer.

