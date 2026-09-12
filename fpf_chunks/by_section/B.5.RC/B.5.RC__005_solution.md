---
chunk_kind: "child"
pattern_id: "B.5.RC"
pattern_title: "Recover a Construction from Its Description"
section_id: "B.5.RC:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.RC/B.5.RC__005_solution.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "B.5.RC — Recover a Construction from Its Description"
  - "B.5.RC:4 — Solution"
line_start: 41842
line_end: 41903
dependencies:
  - "A.6.3.RT"
  - "B.5"
  - "B.5.RA"
  - "C.29.1"
  - "C.29.2"
  - "C.39"
keywords:
---

### B.5.RC:4 - Solution

Recover the construction in two connected directions: from the required result toward its prerequisites, then from the available inputs toward a result. Keep the needed property in view throughout. The following actions form a useful working order; return to an earlier action when a missing condition changes the construction.

#### B.5.RC:4.1 - Fix the result and starting situation

Say what the next user needs to obtain and what they will do with it. Recover the conditions that distinguish a usable result: for example, a triangle on a supplied side, a display design that uses the supplied fittings, or data in the format required by a calculation.

Identify the starting objects and information already available. Distinguish an object supplied by the task from one the construction must produce. If a property alone answers the question, keep that smaller task. When an instance is needed, locate the operation that could obtain one.

Choose a small case that retains the troublesome dependency. A case that omits the unfamiliar operation cannot resolve how that operation works.

#### B.5.RC:4.2 - Recover the operations

Read the description for ways of forming, transforming or combining the objects. For each operation needed by the case, recover:

- what it takes as input;
- the conditions under which it can be used;
- what it produces.

This information can appear in a definition, diagram, earlier construction or convention used by the source. A verb such as “combine” is enough only when its operation is already recoverable. Otherwise ask which parts are combined and how.

In a mathematical account, include the formation and equality rules that the construction uses. A rule for forming an object and a claim about its properties do different work: the first supplies an object for a later operation, while the second may justify applying that operation. Both can be needed.

Use the rules of the account being recovered. For a physical assembly, a joining operation may require compatible fittings and available components. For a mathematical expression, using one value at two places depends on the rules of that expression. Recover the relevant condition where the construction actually relies on it.

#### B.5.RC:4.3 - Follow prerequisites backward

Start with an operation that produces the required result. Ask what must be available just before it can be applied. Repeat for any prerequisite not yet supplied.

Keep **joint prerequisites** together: drawing a segment between two points requires both points. Keep **alternative constructions** separate: either one complete construction or another may produce an acceptable result. Where several later steps use an intermediate object, retain that shared dependency instead of silently creating several unrelated objects.

Stop tracing a branch when it reaches an available input or an understood subconstruction whose starting inputs are available. The resulting dependency structure may have shared parts and alternatives. Draw it when that helps retain them; the structure does not have to be expressed as a graph.

If tracing returns to a result that it already requires, examine the source. It may describe an iterative construction with a starting value and stopping rule, a simultaneous problem with a separate solving method, or an omitted prerequisite. Recover that method or prerequisite before treating the circular description as executable steps.

A missing operation gives a focused question: “How is this intermediate object obtained under these conditions?” Return to the relevant source passage or specialist with that question. When you propose an operation yourself, treat it as a contribution to the construction and establish the conditions for using it.

#### B.5.RC:4.4 - Work the small case forward

Begin with the available inputs. Apply an operation when its prerequisites and conditions hold, retaining the output needed by later operations. At an unfamiliar transition, write, draw or perform enough of it to see what changes.

If the construction uses a notation you can read but cannot operate with, use A.6.3.RT to prepare a usable expression under its rules. If interpreting the notation itself remains the difficulty, obtain that missing preparation. A more legible expression helps only when it preserves the relation required by the operation.

Where an operation admits several outputs, select one that permits the intended continuation. If the source only guarantees that some suitable object exists, determine whether its account also provides a way to obtain the instance your next use needs.

Retain the difference between the construction being described and the particular trial. One successful trial can reveal the method and expose a gap. A claim about a whole class of inputs additionally needs the argument or other subject support appropriate to that claim.

#### B.5.RC:4.5 - Establish the useful property and continue

Recover why the constructed object has the property the next use requires. An auxiliary construction can make the argument possible; an established property can permit the next construction step. Use B.5.RA when the argument is present but its reasoning remains unclear.

The useful stopping point can be:

- the required object and a sufficient account of the property being used;
- a conditional construction whose unresolved condition matters to the next decision;
- an identified missing input or operation, with enough context to obtain it.

Select the support needed for that next use under C.11.DUA and the relevant subject method. A design calculation, mathematical proof and trial assembly answer different questions. If an existing result already supplies the needed support, use it.

An explanation to a collaborator should let them continue from the recovered result or address the localized gap. Use the working drawing, expression or conversation when it already carries that information.

