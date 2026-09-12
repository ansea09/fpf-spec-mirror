---
chunk_kind: "child"
pattern_id: "B.5"
pattern_title: "Canonical Reasoning Cycle"
section_id: "B.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5/B.5__005_solution.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "B.5 — Canonical Reasoning Cycle"
  - "B.5:4 — Solution"
line_start: 41092
line_end: 41207
dependencies:
  - "A.10"
  - "B.5.1"
  - "B.5.2"
  - "B.5.4"
  - "C.29"
keywords:
---

### B.5:4 - Solution

Choose reasoning by the result the current question needs. The abductive–deductive–inductive loop remains the canonical route for **hypothesis-led empirical inquiry**: propose a conjecture, derive consequences that make a test interpretable, and compare them with relevant observations. Construction, exploratory observation and question formation can precede, interrupt or follow that route. A mathematical inquiry may finish with a construction, counterexample or proof.

#### B.5:4.1 - Form or recover the question

Say what an answer would help someone understand, construct, explain, decide or investigate. An epistemic aim, such as exposing an obstruction or finding a more informative theory, can justify inquiry without an immediate product application. Recover an adequate existing answer before commissioning new work.

Separate the subject from its description, the intended result from a convenient proxy, and established premises from assumptions. Use ordinary language, a sketch or a small mathematical example at the precision needed to expose the difficulty.

When the current formulation is inadequate, vary a consequential element. Useful operations include:

- change the quantity or distinction that the answer must preserve;
- restrict or widen a domain, scale, boundary or assumption;
- construct a small case that defeats the current claim;
- introduce a new object, relation, operation or representation and ask what it makes expressible;
- ask what observation or argument would distinguish the remaining possibilities.

Keep a changed formulation when it changes the construction, evidence, explanation, comparison or next action.

C.22.2 helps make a problem-side claim and its next use inspectable. C.29 helps when choosing a mathematical lens or its mapping is the live question. Use their supplied actions at those boundaries; an ordinary mathematical problem need not acquire a separate card.

When you can follow a concept's explanation but cannot yet interpret the situation through it, use [B.5.4][fpf-b5-4-ref] to construct and test the correspondence. Return with the interpreted participants and relations, then choose the reasoning contribution the question needs.

##### B.5:4.1.1 - Propose a first model


When the situation has no usable model yet, begin with the contrast the answer must resolve. Inspect one case or the actual arrangement. Describe what happens and which proposed change or comparison matters. Separate observations from the explanation you are about to try.

1. **Choose what must remain distinguishable.** Identify participants, states or quantities whose differences could change the answer. Use observed differences and possible interventions to propose a boundary: what can vary separately, what connects those parts, and what surrounding conditions affect them? Keep a distinction when you can explain its consequence for the question.
2. **Propose how they are connected.** Draw or state a dependency and explain how it could produce the observed behavior. Use the relevant subject account to identify the interaction and what it preserves or changes. If that account is unfamiliar, use §4.3 to recover its concept of use. Mark the assumptions that let you omit other interactions or treat a quantity as fixed. For a physical model, use physical knowledge to choose the law that the mathematical account will express.
3. **Obtain a cheap consequence.** Follow the proposed relation far enough to answer a useful part of the question. A direction of change, limiting case or rough bound may suffice before parameter fitting or detailed computation. Show which premise makes that consequence follow.
4. **Challenge a consequential choice.** Ask what observation, omitted interaction or changed condition could defeat the answer. Compare a plausible alternative when the observations leave materially different explanations. Revise the model or obtain the missing observation when that difference matters.

Return the provisional model and what follows under its assumptions. If a missing domain account or formal construction prevents the next contribution, use A.15.9 to request that specific help from the working description. Section 5.6 shows this entry before a heat-transfer calculation has been formulated.

#### B.5:4.2 - Perform the contribution that is missing

The following are common alternatives, not an exhaustive classification or a sequence to complete.

| Missing result | Useful operation | What the result can establish |
| --- | --- | --- |
| An object, procedure or structure with desired properties | Construct it from stated elements and permitted operations; test examples and counterexamples; prove the relevant properties or expose the obstruction. | A construction, existence or impossibility result under its mathematical premises. |
| A consequence or a mathematical justification | Make premises explicit and derive the consequence. Identify the step that carries the argument and the conditions on which it depends. | The implication or theorem within the stated domain and inference rules. |
| An explanation of an anomaly, opportunity or probe result | Use B.5.2 to generate serious rival conjectures and compare their explanatory fit, constraints and prospects for criticism. | A qualified explanatory conjecture, with its grounds and unresolved rivals. |
| A better description of an insufficiently understood phenomenon | Make a purposeful observation or exploratory measurement; vary a condition and inspect what becomes distinguishable. | Observations and possible regularities that can generate or change questions. |
| An empirical consequence of a conjecture | Derive the expected contrast, obtain relevant observations and compare the actual result with it. | Bounded corroboration, a discrepancy or a qualified basis for rejecting or revising the claim. |

**Recover a construction before trying to execute it.** Use this continuation when the source names a desired object or property but you cannot yet obtain the result needed by the question. B.5.RC expands the method below with worked cases and explanations of shared prerequisites, alternative constructions and missing operations.

1. Identify the starting objects or data that are available. State what must be produced and which property the receiving use needs.
2. Find the source's operations for producing or combining those objects. For each needed operation, recover its inputs, application conditions and output. Keep a statement that an object exists with certain properties as an existence claim; seek a way to obtain an instance when the next use requires one.
3. Work backward from the desired result to the required intermediate results and starting inputs. Preserve joint dependencies and alternative ways where the source supplies them. A missing operation is a question for the source or the relevant specialist; a rule you propose is an addition to be tried and justified.
4. Work a small instance from the available inputs, applying each recovered operation when its conditions hold. If the notation prevents the operation, use A.6.3.RT to prepare and compare a more usable expression. For a mathematical account, use its formation and equality rules; identify where a proposed identification changes the operations or property being used.
5. Establish the needed property by the appropriate argument or test. Return the construction and what follows under its premises, or the input, rule or unsupported transition that still prevents the result. Stop when this supplies the receiving use.

For example, a stand specification calls for a portable display. Its assembly rules allow a compatible upright to be joined to a base and a compatible panel to be attached to that upright. Those rules yield the assembly order and the connections to check. Portability remains a requirement to check on the resulting design. If the supplied panel does not fit, the next contribution is a compatible panel, an adapter with its connection rules, or another assembly design. The construction result here is the assembly design; whether the erected stand is stable needs its physical-design argument.

Construction and deduction can work together: an auxiliary object can make a proof possible, and a theorem can suggest a new construction. Novelty does not belong exclusively to one inference type.

For a hypothesis-led test, derive the consequences needed to interpret the test before treating its outcome as corroboration. Keep the prediction, observations, measurement conditions and inference recoverable. A simulation establishes a result of the simulated model; applying it to the physical target needs a supported model–world correspondence.

An exploratory finding can supply a hypothesis. Its subsequent empirical assessment must account for how that hypothesis was obtained and for the dependence or selection involved. Use the domain's appropriate design and inference; merely relabeling the same data as a later test does not create independent evidence.

A bounded result may be sufficient at any of these contributions. Assurance belongs to the particular claim and receiving use under B.3 and B.3.3, including the applicable domain proof or validation obligations.

#### B.5:4.3 - Make the result understandable for its use

Explain what was obtained, why the decisive step works, and where the result can be used. The needed depth depends on whether the receiver will apply, criticize, extend or teach the argument.

**Recover the argument needed for that use.** Begin with the conclusion or proposed change the receiver needs to understand. B.5.RA develops both the main reason for the result and the local transitions needed to use it.

1. Read the claim with its domain and conditions. For a mathematical statement, recover the meanings of its objects and quantifiers.
2. Work backward from that conclusion through the intermediate claims or constructions it uses. At each needed transition, identify the premises, the operation or inference, and what it establishes. Follow a shared premise wherever the conclusion depends on it; keep jointly needed premises together.
3. Reconstruct a transition the receiver cannot follow from the source's definitions, rules or worked cases. Obtain the missing explanation or specialist contribution when those do not suffice. A conditional argument can be useful while one premise remains to be established; state that premise and the consequence its failure would have for this use.
4. If a premise or requested result changes, carry that change through the dependent steps and derive what still follows. Stop at a sufficient argument for the receiving use or a named unsupported transition. An unchanged, adequately supported part can be reused; a full reproof is needed only when the question calls for it.

For instance, a team expects to recover a drawing because a backup exists. Recovering that conclusion requires the needed data in a readable format and an available way to decode it. If the backup is encrypted and its key is unavailable, the next question concerns access to that key or another copy of the drawing. Repeating the fact that a backup exists leaves that prerequisite unresolved.

When beginning with an unfamiliar theory, reconstruct its concept of use for one working question. State what the practitioner wants to explain, predict, construct or decide; which objects and relations the theory lets them describe; what information and operations the application needs; and how its result answers that question. Use a source application when it answers the question. Otherwise propose a small application from the theory's stated objects and operations, work it through and test the correspondence. Keep that constructed trial distinguishable from an application already supported by the source. The first result is a usable explanation of that application, or the particular missing premise or operation that prevents it. Use the intended application to choose what to learn next. Study the construction deeply enough to perform or change the contribution the work requires.

To compare theories or ways of using them, ask the same question of each account. Preserve each source's meanings while comparing what is given, what operations are allowed and what answer follows. If the results differ, identify whether the difference comes from the question, assumptions, mathematical structure, inference or proposed physical mechanism. If one account answers a different question, state that complementary use. Choose or change an account for the distinction the receiving work needs. Use C.29 for a proposed mathematical-lens transfer or local candidate choice; domain prediction and intervention claims still need their applicable Methods and evidence.

When the correspondence between a formal account and its intended use is the difficulty, reconstruct one small instance. Name the variables and their domains, the given inputs, the assumptions and permitted operations, and the statement the calculation or proof establishes. Relate the decisive quantities and conditions to the intended use. A source's worked case can supply this reconstruction; recover the omitted step if the receiver cannot yet carry it out.

Challenge the correspondence with a case that could change the answer. Look for a formally admissible answer that the intended use excludes, or two situations identified by the representation that require different answers. If this exposes a mismatch, repair the domain, constraint, quantity or correspondence, or use the existing result for a weaker question that it does answer. A relaxation can remain useful as a bound even when its optimizer cannot be enacted. The worked case below makes both uses explicit.

For a physical application, connect the mathematical objects and quantities to the phenomenon, measurement and operating conditions. Ask which approximation, omitted interaction, scale or uncertainty could change the conclusion. A rigorous derivation from a model and evidence that the model applies answer different questions.

Use the explanation to test the formulation: does the result answer the intended question, or only the conveniently formalized one? If a distinction was lost, determine whether the use can tolerate that loss, whether a bound suffices, or whether another representation is needed.

#### B.5:4.4 - Settle the question or change the next inquiry

Return the result at its supported scope. Stop when it answers the current use. Continue only for a remaining question whose possible answers could change understanding or action and whose investigation is worthwhile under the available conditions. Account for the effort of learning, obtaining, explaining, checking and maintaining the result as well as calculation cost.

When the result exposes a limitation, identify what must change:

- **The answer or construction for the same question:** repair it or investigate a serious alternative.
- **The formulation:** revise the target, assumptions or boundary and state which earlier results still apply.
- **The available Methods or ways of constructing candidates:** compare retaining, modifying or extending that repertoire. E.23 supplies improvement under an appropriate evaluation; C.18 applies when generation rules, retained alternatives or the effective space of possibilities are the question.
- **A participant's ability to contribute:** distinguish the capability question from missing access or support; use E.23.CAE and E.23.CDI where their conditions hold.

Use E.10.DEV if “development” hides the intended subject and C.36 for an actual cultural-generation, transmission or selection question.

Retain a construction or unresolved alternative when a named future inquiry makes keeping it worthwhile. C.17 can characterize novelty, value and diversity on a declared basis; C.18 distinguishes the archive from a comparison front and a new point from a change in admissible possibilities.

#### B.5:4.5 - Organize human and AI contributions around the work

Calculation, conjecture, proof, explanation, criticism and question formation may be performed with different combinations of people, AI and other tools. Choose that allocation from their actual capabilities, available support, constraints and the evidence needed for the receiving use. Revisit it when those conditions change.

When the question depends on a result from another practice, use [A.15.9][fpf-a15-9-ref] to use the available answer or select a worthwhile missing contribution. State the working question, available inputs, result needed and intended use in terms the receiver can check. If the formal formulation is itself missing, ask the mathematician, physicist or supported AI for that formulation and its correspondence to the working question.

For an engineer, derive the needed capability from representative later work: what must this person be able to understand, ask, construct, criticize or arrange with the assistance that will actually be available? The answer can include interpreting a proof's central idea or recognizing that a measured proxy omits the intended quantity, even when a tool performs most calculations. It can also justify deeper mathematical study when constructing or modifying the theory is the required contribution.

When assessing that capability, use representative work under the declared support and inspect the person's relevant contribution. A completed AI-assisted report alone leaves that contribution underdetermined.

