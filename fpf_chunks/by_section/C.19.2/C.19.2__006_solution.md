---
chunk_kind: "child"
pattern_id: "C.19.2"
pattern_title: "Use-Bounded Apparatus Application"
section_id: "C.19.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19.2/C.19.2__006_solution.md"
commit_sha: "55ef163f91d42b48785bd297b50322e072d0a950"
heading_path:
  - "C.19.2 — Use-Bounded Apparatus Application"
  - "C.19.2:4 — Solution"
line_start: 64952
line_end: 65007
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
  - "C.39"
  - "C.40"
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

#### C.19.2:4.1 - Identify the use, apparatus, method, performer and result

Before choosing how to proceed, identify what the application involves.

1. **Declared use:** the practical question, direct result kind, claimed guarantee, non-negotiable constraints, and horizon.
2. **Selected or candidate direct-kind object:** the method description, model, ontology module, formal technique, or other governed object being considered.
3. **Application guidance and Method:** use this pattern’s instructions to guide the application. When identifying a particular Method, apply A.3.1. Treat a claim-bearing episteme as its `U.MethodDescription` only when A.3.2 establishes that the already admitted Method is its EntityOfConcern and it makes substantive claims about that way of doing. Using the guidance does not itself require that classification.
4. **Performer and work:** when a claim identifies particular dated configuration or application `U.Work`, recover the admitted performing `U.System` through A.13 and independently admit the Work under A.15.1, including its enacted Method under A.3.1. Add F.6 afterward only when the present use needs precise assignment-bound attribution. In a short account, expose assignment identity, species, participants, or attribution detail only when the use relies on them, attribution is ambiguous, or source wording must be repaired.
5. **Problem-facing result:** the domain, engineering, assurance, architecture, or other subject-pattern result inspected after the work.

A person or an AI system can read these instructions and also perform the work. To attribute a particular performance, establish who actually carried it out.

#### C.19.2:4.2 - Select the application branch

**One current apparatus.** For an already selected method, recover its required operations, the inputs and settings it accepts, and the result and guarantee it supports. Check the conditions of this application and supply its inputs. The existing configuration may already suffice. If extra setup is needed, establish what it will enable and whether its cost fits the budget and the expected use. The single-apparatus path needs no `OptionSet` or `ChoiceResult`.

**Candidate generation or reframing.** If no adequate current object is available, use `C.39` to develop a missing explanation of how to obtain the result, or `C.40` to vary usable material and examine the difference. Use `C.18` when generation-account or archive/front claims are needed. The declared use and eligibility basis can guide that work.

**Local choice.** Only when two or more already-available eligible alternatives, or another genuine local-choice question over a live set, are current, use `C.11` for `OptionSet`, `ChoiceRule`, probing, and `ChoiceResult`.

**Post-choice enactment.** For a singular selected direct-kind object, use `A.15.2` to plan its application when a plan is needed and `A.15.1` for the dated application Work. `C.24` is the pattern for sequencing, budgeting, checkpointing, and replanning only when the application involves tool-call work.

#### C.19.2:4.3 - Admit candidates by one use-bounded predicate

`UseBoundedApparatusCandidateEligibilityPredicate@Context` is a local eligibility predicate, not a U-kind, relation kind, or candidate-generation method. A candidate is eligible only when it has a credible adaptation path to the same declared use, direct result kind, claimed guarantee, scope and horizon, and non-negotiable constraints. A candidate that cannot meet one of those values stays outside the current option set rather than becoming a “weaker” member of it.

When the claimed guarantee or requirement is disputed, use `C.11.DUA` to appraise its purpose, contribution, burden and current force. Keep apparatus eligibility under the current declaration separate from that appraisal. Resume application under a revised declaration only when the change is available through the authority or agreement that governs it.

Apply `C.11` to the current comparison. If the evidence or the holder’s priorities leave a requested choice open, return the supported comparison, the outstanding question and who can settle it. A completed `ChoiceResult` has one of four forms:

- `choose now` names one selected option or a retained tie-set;
- `reject current set` returns to a named candidate-generation pattern or closes with no current application;
- `probe again` retains one probe and its epistemic budget because it can still change the choice;
- `reroute` names the neighboring question and its subject pattern.

These four dispositions form the complete current `C.11` result set. “Configure the rich basis”, “adapt again”, and “use a lighter method” are option or plan contents, not extra choice-result values. A tie is not a hidden winner.

#### C.19.2:4.4 - Perform the bounded application

1. State the practical use, direct result kind, claimed guarantee, constraints, horizon, and current apparatus state.
2. For an already selected apparatus, check its configuration and conditions of use (§4.2). Under `A.3.1`, determine whether the original Method admits the proposed inputs, parameters, operations, required participants, result and acceptance conditions. If a defining condition changes, identify the revised way of doing the work or state what remains unresolved. Use the subject method to establish what guarantee the revised procedure supports. If candidates are missing, use `C.39` for an unexplained way to obtain the result or `C.40` for feasible variation and examination of usable material. Add `C.18` when a generation account or archive/front claim is needed.
3. When alternatives are current, identify them by their direct kinds and apply the shared eligibility predicate.
4. For each current path, identify what must be learned, supplied, integrated or checked to meet the required guarantee. Estimate the work still needed. An existing configuration that meets the requirements can be used immediately.
5. Compare only the dimensions that can change the current path for the declared use and horizon. These may include time and budget, prior exposure, post-threshold efficiency, transfer, retention, interoperability, downside and reversibility; use their subject-pattern values when needed. Do not compress them into an undeclared scalar.
6. Use the current comparison at the strength it supports (§4.3). If the choice remains open, give the holder the supported alternatives and the premise or priority needed to decide. A completed `C.11 ChoiceResult` may identify a worthwhile probe or another decision. A rejected set leaves no selected application. When a set is accepted, distinguish ties from incomparability and establish who may choose a member for use.
7. When one apparatus is selected for use, carry out its application. Use A.15.2 when a plan is needed and C.24 when tool-call planning is the question. A precise dated-Work claim uses the performer and admission conditions in §4.1.
8. Inspect the result against the criterion for this use. For another application, check that the accepted method, inputs and assumptions cover its conditions. To establish that the recipient can apply the method with a stated degree of help, examine that recipient’s own performance under those conditions. Keep an application or configuration note when reuse, dispute, automation or consequence makes it useful.

#### C.19.2:4.5 - Stop and reopen

Stop when the direct result is usable at the claimed guarantee and no further distinction or setup is expected to improve the declared use enough to justify its burden over the stated horizon. This is a positive result, not a claim that the unused apparatus is inferior.

Reopen when a consequential counterexample, failed result, changed use or guarantee, changed recurrence horizon, new candidate path, automation need, or changed adaptation cost alters the lawful path. Reopen only the affected application, candidate, choice, plan, or work question under its subject pattern.

