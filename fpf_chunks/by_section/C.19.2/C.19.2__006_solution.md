---
chunk_kind: "child"
pattern_id: "C.19.2"
pattern_title: "Use-Bounded Apparatus Application"
section_id: "C.19.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19.2/C.19.2__006_solution.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "C.19.2 — Use-Bounded Apparatus Application"
  - "C.19.2:4 — Solution"
line_start: 50869
line_end: 50926
dependencies:
  - "A.15.1"
  - "A.15.2"
  - "A.7.1"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.22.1"
  - "C.31.ASAP"
  - "E.23"
keywords:
  - "configuration or adaptation work"
  - "declared result and guarantee"
  - "one selected apparatus"
  - "reuse horizon"
  - "setup cost"
  - "use-bounded apparatus application"
---

### C.19.2:4 - Solution

#### C.19.2:4.1 - Keep the five positions separate

Use this minimal lens before taking a branch:

1. **Declared use:** the practical question, direct result kind, claimed guarantee, non-negotiable constraints, and horizon.
2. **Selected or candidate direct-kind object:** the method description, model, ontology module, formal technique, or other governed object being considered.
3. **Application MethodDescription and described Method:** this pattern's `U.MethodDescription` episteme and the admitted `U.Method` it describes. A practitioner uses its claims to guide the Work.
4. **Performer and work:** when an admitted `U.System` performs dated configuration or application `U.Work` using the described Method, recover its A.13 core and independently admit the Work under A.15.1. Add F.6 afterward only when the present use needs precise assignment-bound attribution. In a short account, expose assignment identity, species, participants, or attribution detail only when the use relies on them, attribution is ambiguous, or source wording must be repaired.
5. **Problem-facing result:** the domain, engineering, assurance, architecture, or other subject-pattern result inspected after the work.

The intended reader may also be the person-system that performs the Work, but reader position and performer relation remain different.

#### C.19.2:4.2 - Select the truthful application branch

**One current apparatus.** When one direct-kind apparatus is already selected and still has a credible path to the declared result and guarantee, create no `OptionSet` and no `ChoiceResult`. Compare the smallest next adaptation/configuration work with the useful-result threshold, plan when needed, perform the work, and inspect the result.

**Candidate generation or reframing.** When no adequate current object is available and the live question is to invent, expand, retain, or reframe candidates, use `C.18`. This pattern may supply the declared use and eligibility basis, but candidate-generation work is not a choice result.

**Local choice.** Only when two or more already-available eligible alternatives, or another genuine local-choice question over a live set, are current, use `C.11` for `OptionSet`, `ChoiceRule`, probing, and `ChoiceResult`.

**Post-choice enactment.** For a singular selected direct-kind object, use `A.15.2` to plan its application when a plan is needed and `A.15.1` for the dated application Work. `C.24` is the pattern for sequencing, budgeting, checkpointing, and replanning only when the application involves tool-call work.

#### C.19.2:4.3 - Admit candidates by one use-bounded predicate

`UseBoundedApparatusCandidateEligibilityPredicate@Context` is a local eligibility predicate, not a U-kind, relation kind, or candidate-generation method. A candidate is eligible only when it has a credible adaptation path to the same declared use, direct result kind, claimed guarantee, scope and horizon, and non-negotiable constraints. A candidate that cannot meet one of those values stays outside the current option set rather than becoming a “weaker” member of it.

When choice is current, preserve the exact `C.11` contract:

- `choose now` names one selected option or an honestly retained tie-set;
- `reject current set` returns to a named candidate-generation pattern or closes with no current application;
- `probe again` retains one probe and its epistemic budget because it can still change the choice;
- `reroute` names the actual neighboring question and its subject pattern.

These four dispositions form the complete current `C.11` result set. “Configure the rich basis”, “adapt again”, and “use a lighter method” are option or plan contents, not extra choice-result values. A tie is not a hidden winner.

#### C.19.2:4.4 - Perform the bounded application

1. State the practical use, direct result kind, claimed guarantee, constraints, horizon, and current apparatus state.
2. If one apparatus is already selected, test its credible adaptation path without inventing choice. If candidates are missing, use `C.18` first.
3. Name available alternatives by their direct kinds and apply the shared eligibility predicate.
4. For each current path, state the smallest adaptation/configuration work and the useful-result threshold: what must be learned, evidenced, integrated, or reviewed before the path can improve the use.
5. Compare available time and budget, prior exposure, post-threshold efficiency, transfer, retention, interoperability, downside, reversibility, and expected reuse using values supplied by their subject patterns. Do not compress them into an undeclared scalar.
6. If choice is current, consume one lawful `C.11 ChoiceResult`; otherwise continue on the one-apparatus path.
7. On a branch that proceeds to application, prepare the needed `A.15.2` plan or, for tool-call enactment, `C.24` call plan. Have the admitted system perform `A.15.1` work.
8. Inspect the separately governed problem-facing result. Keep an application/configuration note only when reuse, dispute, automation, or consequence makes it useful.

#### C.19.2:4.5 - Stop and reopen

Stop when the direct result is usable at the claimed guarantee and no additional distinction or setup burden has an expected practical return for the declared use and horizon. This is a positive result, not a claim that the unused apparatus is inferior.

Reopen when a consequential counterexample, failed result, changed use or guarantee, changed recurrence horizon, new candidate path, automation need, or changed adaptation cost alters the lawful path. Reopen only the affected application, candidate, choice, plan, or work question under its subject pattern.

#### C.19.2:4.6 - Optional demonstration, not an admitted structure

A short branch presentation may show one-apparatus, candidate-generation, choose, probe/reject, application, result, and reopen continuations as a `ProvisionalUnfoldingDemonstrationDescription@Context`. It is an episteme for teaching. The presentation alone establishes no admitted `U.Structure`, CGUS, work plan, work occurrence, or problem-facing result; CGUS admission requires every `A.22.CGUS` coordinate independently.

