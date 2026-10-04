---
chunk_kind: "child"
pattern_id: "C.28.CM"
pattern_title: "Construct and Challenge a Causal Model"
section_id: "C.28.CM:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28.CM/C.28.CM__005_solution.md"
commit_sha: "28bf3bdf302e08b71ba981fb267281a6e1d88f1e"
heading_path:
  - "C.28.CM — Construct and Challenge a Causal Model"
  - "C.28.CM:4 — Solution"
line_start: 64548
line_end: 64628
dependencies:
  - "A.15.9"
  - "B.5.2"
  - "B.5.FM"
  - "C.11.DUA"
  - "C.16"
  - "C.27"
  - "C.28"
  - "C.28.MR"
  - "C.29"
keywords:
---

### C.28.CM:4 - Solution

Construct the account around the question, then challenge the relations on which its useful consequence depends. The following moves can return to one another. A discovered measurement error may change the outcome definition; a missing mechanism may change the question.

#### C.28.CM:4.1 - Fix the contrast and the time that matter

State what needs explaining or changing. Name the outcome and the cases it concerns, the relevant time, and any proposed action or comparison. “Why did this queue start?”, “Why does it remain?” and “What will shorten it now?” can require different mechanisms.

Distinguish an observed comparison from an intervention query. Observing X=x supplies information about the mechanisms already operating; imposing X=x replaces a mechanism. When the question concerns the same past case under another action, preserve its factual observations and the underlying conditions they constrain. C.28.MR develops the corresponding model calculation; C.28 determines what supports that use.

Keep the question small enough for a useful contrast. If two retained accounts permit the same sufficient next action under its own grounds, C.11.DUA can settle whether distinguishing them is worth the effort.

#### C.28.CM:4.2 - Turn the story into variables with subject meaning

Choose quantities or distinctions that can vary across the relevant cases or times. Give each a meaning, possible values and observation time. A particular late delivery is a case; its lateness is a value of a selected variable. Whether a variable is binary, ordinal or continuous depends on the question and measurement.

Separate the subject quantity from its registration when that difference matters. For example, distinguish an identifier present in the submitted report, a log entry reporting its absence, and inclusion of that report in an incident sample. Recover how the observation is produced through C.16 when needed. A copied ticket is another report of the same event, not another occurrence of it.

Retain enough distinctions for the proposed contrast. Combining two stages is unsafe when the action can change one while leaving the other unchanged. Conversely, a single “ready for dispatch” variable may suffice until readiness failures require different responses.

#### C.28.CM:4.3 - Propose mechanisms and serious alternatives

For each consequential relation, explain how changing a proposed cause could change its effect under the relevant conditions. Use the process arrangement, physical law, subject theory, observations or qualified source that supports that proposal. Mark a conjecture as such. A chronological sequence can suggest a mechanism while leaving common causes unresolved.

Construct a material alternative: another cause, a common influence, a recording difference, or a model in which the proposed direct influence is absent. Causes may coexist. An account of overload need not remove an effect of missing information. Keep the outcome and horizon comparable, and specify the same intervention in each model when that is the question.

A directed arrow X → Y represents a proposed direct causal influence in the chosen model. “Direct” is relative to the variables retained. Explain a consequential omitted influence as carefully as an included one: excluding it may be what makes the answer follow.

For an equation-based model, write the relevant mechanisms in a form such as Y=f(X,U), where U represents inputs left outside that mechanism. Specify shared inputs or their dependence when needed. A graph supplies qualitative restrictions; it does not supply an omitted functional form, effect size or disturbance law. Ask for these only when the receiving calculation needs them.

#### C.28.CM:4.4 - Inspect the whole relevant structure

Follow possible paths between the proposed cause and outcome. Look for common causes, intermediate mechanisms, measurement processes and selection of cases. A common cause can coexist with a causal path. The role of a node is relative to a path and question, not a permanent label attached to the variable.

For a **directed acyclic graph (DAG)**, the following path test makes that inspection precise. A path joins distinct nodes along edges, ignoring arrow direction when finding the path. At an internal node, two arrowheads meeting there make it a collider on that path; other internal nodes are noncolliders.

Given a conditioning set W disjoint from the endpoints, a path is open when every noncollider on it is outside W and every collider is itself in W or has a descendant in W. Otherwise it is blocked. If every path between two variable sets is blocked, the sets are d-separated by W. For a distribution satisfying the graph's Markov property, d-separation implies the corresponding conditional independence. An open path permits dependence; it does not guarantee it for every parameter choice. Inferring graph structure from observed independences needs further assumptions, often faithfulness (no extra independences beyond those entailed by the graph), as well as adequate data.

Apply this rule to all relevant paths, including those opened by the way the sample was selected. Conditioning on an incident being reported can matter even when “reported” is absent from the regression.

Consider the complete small graph:

~~~text
Z → X → M → Y
Z → Y
X → S ← Y
S → D
~~~

There are three simple X-to-Y paths. X → M → Y carries the proposed causal mechanism; X ← Z → Y carries a common cause; X → S ← Y is blocked at S before conditioning. Conditioning on Z blocks the common-cause path and retains the causal path. Conditioning on M blocks that causal path. Conditioning on S, or its descendant D, opens the collider path. Inspecting only the fork would miss that selection effect.

For a total effect in an appropriate causal DAG, the back-door criterion provides one sufficient adjustment rule: choose measured covariates that are not descendants of X and block every path entering X through an arrowhead. This leaves the directed causal paths available. The resulting identification still relies on the model's causal interpretation, suitable data and support for the required comparisons. Failure of this sufficient criterion is not proof that the effect is unidentified. Use C.28 for the identification question rather than inventing an adjustment from one recognizable three-node shape.

The ordinary d-separation rule above applies to DAGs. If feedback matters, distinguish times: an outcome at t may affect workload at t+1. A finite time-unfolded model still needs its initial conditions and omitted influences justified. An equilibrium with simultaneous causal feedback needs an appropriate cyclic model, its solution conditions and its separation rule. Do not erase feedback merely to obtain an acyclic picture.

#### C.28.CM:4.5 - Derive a consequence that can distinguish the accounts

Work the same question through each retained model. Start with a direction, a possible or impossible outcome, a conditional independence, or an observation that one account can explain only by adding another premise. Show which relation makes the consequence follow.

Keep three operations distinct. Conditioning restricts attention using an observed value. Intervention replaces the specified mechanism. Omitting a variable from a report or marginalizing it out leaves its possible influence in the subject model. Treating all three as “fix the variable” can reverse the conclusion.

When the mechanisms are specified, C.28.MR derives an intervention consequence while retaining the relevant other mechanisms and underlying inputs. Use C.29 when expressing or computing the model requires further mathematical construction. If the needed function or input law is missing, return that precise gap along with any qualitative result that survives.

Two graphs may entail the same observed independences. Two mechanisms may produce the same measurements in the available range. Retain both when the present material does not distinguish them. A causal-discovery procedure can contribute within its declared model class and assumptions; its returned graph does not remove those conditions.

#### C.28.CM:4.6 - Challenge the consequence with available evidence

Compare the consequence with an observation, contrasting case, subject argument or feasible intervention that bears on it. First check that the observation concerns the modeled variable, cases and time. A contradiction can arise from the mechanism, measurement, implementation of a proposed action, or a changed operating condition.

Distinguish a contradicted implication, an untested implication and compatibility with the inspected material. A graph with no relevant testable implication cannot acquire support merely from an absence of contradiction. Conversely, failure to reject an implied independence does not establish the graph. Deterministic constraints, measurement error, missing cases and sampling uncertainty can all change the interpretation.

Revise only as far as the finding warrants. Preserve a valid observation when its causal interpretation fails. Restore a rival when its rejected premise changes. If an additional study could change the answer, C.28:4.8 helps specify the evidence question and C.11.DUA helps choose whether to obtain it. A useful model may end with an unresolved distinction.

#### C.28.CM:4.7 - Return the model with the use it can support

Give the recipient the question, the relevant mechanisms and alternatives, their source basis and assumptions, the derived consequence, and the uncertainty that changes its use. A short explanation can carry this result; no universal record form is required.

Recognition can stop at “these two accounts imply different responses”. Consequential reliance requires the corresponding subject and evidential grounds. C.28 qualifies causal support; a statistical estimate or bound requires its own identification and estimation result. A controlled direct effect is a different query from a total effect. A claim about the cause of one historical outcome or responsibility also needs its chosen concept and subject standard; a population effect does not settle it.

Return the next useful contribution by what it must establish: for example, whether a log reflects an actual omission, whether a controller reads a display, or whether an apparent AI effect survives comparable task selection. Temporary mitigation can remain available under its own evidence, costs and authority while the causal question is open.

