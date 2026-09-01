---
chunk_kind: "child"
pattern_id: "E.15"
pattern_title: "Pattern Change, Edition Continuity, and Impact Analysis"
section_id: "E.15:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.15/E.15__005_solution.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "E.15 — Pattern Change, Edition Continuity, and Impact Analysis"
  - "E.15:4 — Solution"
line_start: 80568
line_end: 80663
dependencies:
  - "C.18"
  - "C.19"
  - "E.10"
  - "E.19"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.24.PUB"
  - "E.8"
  - "E.9"
  - "F.0.1"
  - "F.1"
  - "F.15"
  - "F.9"
keywords:
---

### E.15:4 - Solution

#### E.15:4.1 - Recover the actual change

1. **Name the predecessor, candidate, question, and receiving use.** Use exact editions or recoverable source values. Add a ClaimScope, ReferenceScheme, model-use structure, or other qualifier only when the receiving use depends on it.
2. **Read the changed passage in both wholes.** Inspect enough of each pattern to recover the passage's function, not only its changed tokens.
3. **Describe the actual practitioner effect.** Ask separately whether the change alters recognition or entry, required inputs, the first or later action, applicability or stop conditions, returned result, normative claims, ontology, dependent uses, or assurance needed for reliance.
4. **Classify only after that comparison.** Use the smallest Delta-Class that matches the observed effect in §4.3. The planned label, commit subject, or amount of changed text is evidence to inspect, not the answer.

Keep wording, examples, informative rationale, normative conditions, and public naming distinct; changing one does not silently change the others. Keep `ClaimScope` and `WorkScope` distinct when both are current.

If an exact predecessor value needed for this comparison is unavailable, return that bounded continuity gap. Do not reconstruct it from a later edition, a title, or a remembered summary.

#### E.15:4.2 - Find the affected reach

Start with the changed claim or instruction and ask who uses it to read, act, check, decide, derive another statement, or preserve a public name. Search results and Relations entries help discover candidates, but neither proves dependence.

For every plausible consumer, decide one of three things:

* **depends:** its action, interpretation, condition, result, check, or public reference would change if the repaired claim changed;
* **mentions only:** it cites or describes the pattern but its current action remains valid;
* **unresolved:** the dependency cannot yet be decided from recoverable content.

Repair the exact dependent loci. Reuse an earlier result only when its conclusion and conditions remain unchanged and the changed premise lies outside its actual dependency. Reopen the smallest affected premise, consumer, example, check, or result; do not rerun an unrelated whole programme merely because an edition number changed.

An undeclared consumer can be real, and a declared dependency can be unused in the current question. Check actual and declared reach when the distinction matters.

#### E.15:4.3 - Classify the actual delta

| Class | Actual effect | Ordinary response |
| --- | --- | --- |
| **Δ-0 — editorial repair** | Spelling, punctuation, formatting, or wording changes while recognition, meaning, actions, conditions, results, checks, and dependent uses remain the same. | Make the direct repair; run the focused wording or structural check that could fail. |
| **Δ-1 — didactic re-expression** | Order, examples, or explanation changes while the same practitioner situation, action, normative conditions, result, and ontology remain recoverable. | Verify idea preservation and read the whole changed pattern for recognition, plain language, and action continuity. |
| **Δ-2 — normative clarification or refinement** | A previously intended rule becomes more explicit, bounded, or checkable, and semantic continuity is claimed, but affected instructions, checks, or consumers may need repair. | State the continuity claim, inspect the affected reach, and supply the equivalence or preservation evidence that the claim needs. Use a DRR when the refinement selects a material content decision. |
| **Δ-3 — semantic change** | Admissible inputs, actions, conditions, results, normative meaning, ontology, public identity, or dependency claims change. | Make the content decision explicit, repair the dependency-closed reach, and recheck every conclusion that relied on the changed premise. |

These are impact classes, not mandatory version-number syntax. If a publication uses SemVer or another version policy, map the already justified compatibility decision into that policy. Do not infer the class from `major`, `minor`, or `patch`.

Refine, rephrase, split, merge, generalize, constrain, rename, add, and retire remain useful edit descriptions. None has a fixed Delta-Class without its actual effect. A split that preserves every use may be Δ-1; a one-word change that reverses an obligation is Δ-3.

#### E.15:4.4 - Choose the least costly adequate route

**Direct bounded repair.** Use this ordinary route when the defect and one non-dominated repair are understood. Make the repair, inspect its actual consumers, perform the selected focused checks, and stop. Do not generate dummy alternatives or a search record.

**Alternative comparison.** Open this branch only when at least two materially plausible designs remain, a current SoTA choice can change the action, or a repeatable search is itself useful. State what the alternatives differ on and which intended use decides among non-dominated candidates. C.18 and C.19 may generate and retain alternatives when novelty or diversity is genuinely part of the question; E.22 and E.21 frame and evaluate pattern qualities.

Keep hard constraints separate from quality comparisons. A failed identity rule, broken reference, missing required result, or unreadable first action is a defect to repair, not a low score to trade away. Compare readability, precision, assurance cost, breadth, or other qualities on their applicable scales. Select by the stated intended use and protected trade-offs; do not add heterogeneous values into an undeclared winner score.

**Return a decision gap.** If the repair depends on an unresolved ontology, authority, source choice, or architecture decision, return that exact gap to its pattern or decision record. More variants do not compensate for a missing governing distinction.

#### E.15:4.5 - Preserve the predecessor by independent probes

For a material rewrite, derive a predecessor-use inventory from the predecessor itself before relying on the author's preservation map. Include each distinct working situation, first move, input, condition, result, prohibition, example function, consequence, source-derived contribution, and consumer-facing promise that the predecessor actually carried.

Then test each probe against the candidate:

* **preserved:** the same practical or semantic function remains;
* **changed intentionally:** the successor decision names the new function and why;
* **moved:** an exact current locus still supplies it without making discovery worse;
* **retired:** an explicit decision removes it and states the affected use;
* **lost or unresolved:** repair it or return it before claiming continuity.

Exact copied text may close by identity. A large deletion, compression, move, or rewrite does not close through line count, author intent, or a high-level summary. The independent inventory need not become a permanent row-by-row file when the receiving workflow needs only the verified candidate and aggregate result, but the inspection itself must be complete.

#### E.15:4.6 - Check the candidate proportionately

Select checks from the actual change and intended conclusion. A small Δ-0 repair may need one focused check. A Δ-2 or Δ-3 change may require semantic, ontological, consumer, source, preservation, or independent quality checks. Reuse a current check result when candidate, question, conclusion, and conditions are unchanged.

After a material ontological or formal repair, read the **whole changed pattern** as a cold practitioner. A local token scan cannot establish precise plain language. Check that the working situation, first action, examples, conditions, and result remain understandable without reconstructing the ontology from elsewhere. Simplify the expression, not the distinction. Keep a technical term when it names a real needed object or relation; remove stacked qualifiers and formal notation when they do no action-changing work.

Author-side use of E.10, E.19, or E.21 questions is development evidence. It does not become the independent review, complete quality result, admission, or landing conclusion that a later use may require.

#### E.15:4.7 - Keep one useful change account

Use the receiving workflow's existing record. A compact change account normally needs only:

| Question | Minimum useful answer |
| --- | --- |
| What changed? | Exact predecessor and candidate, changed loci, and ordinary-language actual effect. |
| How material is it? | Delta-Class with the reason from §4.3, not the desired label. |
| What may be affected? | Dependent loci and unresolved reach; mention-only citations need no repair recital. |
| What was preserved? | Material predecessor functions and any intentional change, move, or retirement. |
| Why this repair? | Direct repair reason, or alternatives and intended-use trade-off when a real choice existed. |
| What was checked? | The focused or whole-pattern results required for the claimed conclusion. |
| What reopens? | Only a source, premise, consumer, or condition whose change could invalidate the result. |

These answers may live in a DRR, review package, campaign result, source-use account, or landing preservation result as that workflow requires. Cite an existing E.21 or E.22 evaluation, F.15 result, source-use record, or decision instead of copying it. Do not mint a dedicated authoring trace, publish a work log with the pattern, or treat a file or publication occurrence as proof that the change was performed well.

#### E.15:4.8 - Edition continuity and stop rule

Keep accepted historical editions immutable and recoverable. A successor does not rewrite what an earlier edition meant. A source-edition change reopens only claims and actions that relied on the changed source value; unchanged exact inputs and unaffected premises remain reusable.

E.15 finishes when the candidate answers the change question, every actual dependent locus in scope is repaired or explicitly unresolved, material predecessor functions have dispositions, and the selected checks support the claimed Delta-Class and continuity. Publication, acceptance, registration, and landing remain separate later decisions.

Schedule a living refresh only for a high-value claim likely to change and only when someone will use the signal. Name the trigger and affected claim. Otherwise use ordinary periodic review; a generic “watch SoTA” obligation is not useful work.

