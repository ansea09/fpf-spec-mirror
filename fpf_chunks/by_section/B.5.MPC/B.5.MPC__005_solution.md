---
chunk_kind: "child"
pattern_id: "B.5.MPC"
pattern_title: "Connect Physical, Mathematical and Computational Reasoning"
section_id: "B.5.MPC:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.MPC/B.5.MPC__005_solution.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "B.5.MPC — Connect Physical, Mathematical and Computational Reasoning"
  - "B.5.MPC:4 — Solution"
line_start: 41410
line_end: 41535
dependencies:
  - "A.15.9"
  - "A.3.3"
  - "A.6.1"
  - "A.6.3.RT"
  - "B.3"
  - "B.3.3"
  - "B.5"
  - "B.5.4"
  - "C.11.DUA"
  - "C.16"
  - "C.29"
  - "C.29.1"
  - "C.29.2"
  - "C.29.3"
  - "C.39"
  - "C.40"
  - "U.Dynamics"
keywords:
---

### B.5.MPC:4 - Solution

Construct the answer by connecting the contributions it actually needs. For each connection, identify the supplied result, the receiving operation and the condition that makes the result usable there. Follow those meanings through a small instance. If the connection is missing, construct it, obtain it from a suitable contributor, or return the particular missing result that prevents the next move.

The long mantra keeps the whole question available while attention moves between contributions:

**Orient by the physical question → propose the relevant physical account → construct a mathematical question and its interpretation → obtain a result and, where needed, a computation → connect its execution and observations to the intended quantities → return the consequence to the physical question → choose the useful action or the next missing contribution.**

The arrows recall result dependencies. They do not prescribe the order in which people must discover, receive or develop every contribution. A ready theorem, algorithm, measurement or physical mechanism can be the first available input.

#### B.5.MPC:4.1 - Recover the physical difference the answer should resolve

Identify the thing or situation being understood or changed. Say which difference would make an answer useful: a displacement within a stated tolerance, the possibility of coupled rotation, a capacity bound during entry, or another consequence the work needs. Include the relevant boundary and operating conditions when changing them could change the answer.

Then recover what is already available. An engineer may have a trusted motion model but an unfamiliar command interface. A mathematician may have an odd-cycle theorem and ask which physical arrangements its obstruction describes. A room attendant may have a reliable card procedure and want to extend it to a second entrance. Enter through that available contribution and recover only the other results needed to answer the question.

Use B.5:4.1 when the question itself needs formation or revision. B.5.4 helps recognize the participants and relations of an explained concept in a concrete situation. If the receiving use is still unclear, work one small consequence of the available result and ask what it would let someone decide or do. Retain a theoretical question when its answer could enable a worthwhile construction, explanation or later inquiry.

#### B.5.MPC:4.2 - Propose the physical account and the observations it needs

Identify the participants, interactions and configurations that could determine the requested difference. Give separately used quantities their participants and reference conditions: the robot's distance to a wall before motion, its distance afterwards and its displacement are three quantities, even though each is called a distance. Start from the arrangement and relevant subject knowledge. For a rolling robot, distinguish wheel, motor, transmission and ground contact. For gears, distinguish an actual contact from proximity in a drawing. For admission cards, distinguish a material card, its holder, the room boundary and the permitted transfers.

State the applicable physical or operating rules. Explain why a rule supplies the needed relation and where it is an assumption. Wheel rotation yields a distance relation only under the chosen rolling and geometry conditions. Exclusive possession of a card supports an admission limit only when the entrance procedure connects possession to entry and return. A.3.3 helps construct configurations, retained state and allowed continuations; the subject practice supplies the laws and mechanisms those continuations use.

Choose a sufficient account for the present question. A direction or impossibility result may need less physical detail than a trajectory, speed or load calculation. Make an omitted interaction explicit when it could defeat the inference: slip changes wheel travel, a moving gear carrier changes relative rotation, and uncontrolled entry breaks the visitor-to-card association.

When observations supply an input or test a consequence, construct the relation between the sought quantity and the indication. Use C.16:5.3 and C.16:5.4 for the measurement method and model. Motor counts can indicate motor rotation under an encoder account; using them to establish travel additionally consumes the transmission and ground-contact account. If the available indication cannot distinguish the cases needed by the question, obtain a different observation, use an adequate bound, or change the question.

Return a proposed physical account and its consequences under stated conditions. An unknown interaction or calibration is a useful missing contribution when it determines which mathematical question can be constructed.

#### B.5.MPC:4.3 - Construct an interpretable mathematical question and expression

Choose mathematical objects and operations that retain the distinctions needed by the physical question. State what their important elements mean. For instance, let a vertex denote one particular gear, an edge denote a specified mesh, and a colour denote the sign of rotation when viewed from one common side. A colour number has meaning through that interpretation.

Construct the relation that connects the physical rules to the mathematical constraints. Derive a distance per motor increment from wheel circumference and transmission ratio; derive an opposite-colour constraint from the external-contact rule; derive a count invariant from a fixed stock and its permitted transfers. C.29:4.1 supplies the general correspondence-and-return method. When an operation or a compressed representation must preserve a result, use C.29.1 to compare performing the source operation and then transferring its result with transferring the inputs and then performing the receiving operation.

Work the distinction that could defeat the representation. A wheel orientation repeats after one turn; accumulated travel can continue to increase. A graph of opposite-direction contacts answers a different question from a graph in which an edge merely means “these parts are connected.” If two physical cases receive one mathematical representation but require different answers, retain their distinguishing information, restrict the cases or seek a weaker consequence.

Keep the relation available when the question changes. Identify which quantities are now given and which must be obtained, then derive the computational direction that serves that question. Under a model `d = v*T` and `v = k*u`, where u is a motor command setting, positive k, u and T permit `T = d/(k*u)` for a duration question or `u = d/(k*T)` for a command question. Obtain k and the range in which the speed model applies from the physical account. The device's word “power” needs its interface meaning; u is not assumed to be physical power in watts. A resulting command outside the supported range returns a realizability question.

For a conditional example, let u be dimensionless and let `k = 0.2 m/s`. A distance `d = 1 m` at `u = 0.5` takes `T = 10 s`. Changing the requested duration to `T = 5 s` requires `u = 1`. If the available range is `0 < u <= 0.8`, the shortest duration under this model is `1 / (0.2 * 0.8) = 6.25 s`. Returning that bound lets the requester change the deadline or seek a different realization.

An equality constrains the quantities in this model. A program assignment changes a stored value according to its execution rules. Construct the needed assignments or solver from the relation after selecting the givens and unknowns; C.29.2 supplies that formulation Method.

Make an expression that supports the next operation. Use A.6.3.RT:4.1 to express the givens and constraints under an available scheme and compare the result with its source. Put units and participant names where their absence permits the wrong operation. Keep a shared quantity recognizable across expressions, such as the same wheel revolution in the transmission ratio and circumference relation.

Notation can contribute to obtaining the result. A table can expose mutually exclusive card states; a graph can make a closed contact path traceable; a labelled equation can reveal the missing subtraction of an initial position. The subject Method supplies the construction or inference performed with those expressions. If the available scheme cannot express the needed distinction, change the scheme or obtain notation-design work before treating its expressions as adequate.

#### B.5.MPC:4.4 - Obtain a sufficient consequence or construct its computation

Choose the result the use needs: a value, distribution, statistic, bound or property of ongoing behavior. A witness can establish one feasible arrangement; a counterexample can refute a general claim; a proof can establish an obstruction; a bound can settle a threshold decision. Compute an exact numerical answer only when that answer contributes to the use.

When a procedure is needed, construct its inputs, retained state, elementary operations and output interpretation. Explain how it obtains the mathematical result and why it terminates, or which property it preserves during continued interaction. C.29.2 supplies this formulation work; the relevant algorithmic or mathematical Method supplies the actual construction and its argument. B.5:4.2 and B.5:4.3 help recover a construction or a decisive proof step that the available explanation leaves inaccessible.

Trace one instance with its meanings intact. In a two-colouring procedure, a waiting list records vertices still to be processed, while parent links can reconstruct a failed closed path. In a motion calculation, the integer is a count of a particular kind of increment. In an admission procedure, taking a free card changes a finite state and determines whether an entry may proceed.

For a numerical approximation, carry the error that can affect the physical use. Separate rounding of a computed command from uncertainty in radius, calibration or physical response. For a resource claim, include the cost of obtaining the input, representing it and interpreting the output when those costs matter. Counting one graph-edge inspection as one operation is useful under an adjacency-list cost model; it does not estimate the effort of discovering the actual contacts.

Use a supplied proof or computation when its premises, meaning and relevant resource conditions fit. If a necessary construction remains unknown, state the missing operation and what it must connect. C.39 supplies the search for or development of a missing way. A conditional answer or a less demanding bound can finish the current question while that larger construction remains open.

#### B.5.MPC:4.5 - Connect the computation to preparation, execution and observation

Begin with the abstract input and explain how the proposed arrangement represents it. Then identify the system actions that perform the operations and the observation or final state from which the result is read. Use C.29.3 for this realization comparison.

Compare two routes for the same input:

~~~text
abstract input → stated computation → abstract result
abstract input → prepared system → system operation → interpreted result
~~~

The comparison asks whether the second route returns the equality, bound, statistical agreement or behavioral property that the receiving use needs. Input preparation and output interpretation can use different relations. Preparing a motor command and reading robot displacement are different operations; counting free cards and authorizing one transfer use different aspects of the same arrangement.

Recover range, units, initial state, ordering and completion conditions at the point where they affect that comparison. A signed command field cannot carry every positive integer. A command meaning “add this displacement” differs from one meaning “reach this position.” A material card available for transfer cannot simultaneously be assigned to another visitor.

Include the timing and retained physical state that the comparison consumes. When a controller is paused for debugging, determine which physical processes continue and which command remains active. Observe or replay the operation with the timing it needs, or interpret the changed run under its changed conditions. Establish the event that completes the requested physical action; program termination, a command acknowledgement and motor stopping can occur at different times. For an observation, include a settling interval or other preparation when the measurement relation requires it.

For a design question, use the stated model of the executing arrangement and return a conditional realization. For a claim about what happened, obtain the corresponding observations and their interpretation. A command receipt can establish that a command was accepted while leaving its successful physical completion open.

Use an existing adequate implementation directly when this comparison is already settled for the receiving use. A manual procedure, analog apparatus or controlled material transfer can supply an execution. Its adequacy follows from its permitted operations and interpretation, not from whether it contains digital software.

#### B.5.MPC:4.6 - Keep joint requirements and alternative routes distinguishable

Recover dependencies by asking, for each needed result, “What results and conditions make this operation possible, and what other operation could supply the same receiving need?” Keep the answer with the actual derivation, diagram or working explanation. A short case may need only a sentence; a shared design may need an explicit dependency diagram.

An **AND dependency** means that contributions are needed together for the stated inference. The robot's distance per motor increment uses the effective wheel radius, transmission ratio and increments per motor revolution together. Replacing any one can change the command.

An **OR alternative** is a different sufficient way to obtain the result needed by the receiving use. A proved upper bound and an exact computation can be alternatives for deciding whether a limit can be exceeded. Each route retains its own assumptions. Two different approximations do not become sufficient alternatives merely because both return a number.

For a conditional physical consequence, one useful small rendering is:

~~~text
applicable physical account
AND mathematical interpretation
AND (sufficient direct consequence OR sufficient interpreted computation)
→ consequence for the physical question
~~~

The computational branch additionally depends on a procedure and an adequate realization for any claimed execution. A claim about observed physical behavior adds the observations and measurement relation it consumes. These are different claims and can end the work at different places.

Keep a shared premise attached to every contribution that consumes it. Both an analytical calculation and a numerical simulation can depend on the same no-slip assumption. Switching between them does not remove that dependency. Conversely, when an upper bound already answers the decision, the exact optimizer need not be obtained.

Enter a ready result at the place where it is used. Recover its inputs and conditions backward, then continue forward with its consequence. When a missing input blocks one route, compare another sufficient route using the available inputs. Do not combine an output from one route with the assumptions of another without establishing their compatibility.

A failed connection can send the inquiry back to its physical account, mathematical construction, notation, procedure, realization or question. Locate the first disagreement that changes the receiving result, revise the responsible contribution and revisit its dependents. B.5:4.3 supplies argument recovery; C.29.1, C.29.2 and C.29.3 supply the transfer, formulation and realization methods respectively. Retain unaffected contributions whose conditions and meanings still hold.

#### B.5.MPC:4.7 - Return the consequence and choose what to do with it

Explain the result in the original physical terms. A count becomes a modeled displacement; an odd cycle becomes a set of contacts that prevents the stipulated nonzero rotation; a card invariant becomes a bound on occupancy under the entry rules. State what the result enables and the condition that changes that use.

When the consequence is insufficient, make the next contribution specific. “Determine whether these two wheels slip differently under this load” can direct physical work. “Find a representation that retains accumulated turns” can direct mathematical formulation. “Establish whether this interface interprets the number as an increment or an absolute target” can direct realization work. The uncertainty itself can be the result if locating it prevents further work on the wrong question.

Distinguish the consequence of an obstruction. A mathematical contradiction blocks a construction under its stated premises. A physical restriction blocks an intervention under the applicable laws. An expensive computation can remain mathematically possible while unavailable within the resources of this use. Their repairs can require different questions, arrangements or Methods.

Stop when the supported result answers the intended use. When development is the purpose, work one consequential variation far enough to reveal a new construction, obstruction or missing operation. Explain which additional action or longer inquiry it could enable. B.5:4.4, C.39 and C.40 supply the corresponding question and repertoire development; continued work is justified by that use.

#### B.5.MPC:4.8 - Divide human and AI contributions by the result they must supply

Allocate work around the dependencies above. A contributor can supply a physical account, a mathematical construction, a proof, a computation, a proposed realization or an explanation of the connection. State the working question, available inputs, missing result and intended use when obtaining help through A.15.9. Ask for the formulation itself when the equation has not yet been constructed.

Retain enough understanding at each receiving point to use and question its input. The receiver of a motion count should be able to identify its unit, the rotation it counts, its sign and its dependence on the motion model. The receiver of a two-colouring result should be able to connect the returned labels or odd-cycle witness to the actual contact list. The receiver of an occupancy bound should be able to identify the material and procedural conditions that preserve the stock.

That understanding can be held by one person or distributed across people and AI with an effective way to obtain a missing explanation. Arrange a capable contribution for each consequential connection. A completed report alone does not establish that this capability is available when a premise changes.

Choose depth from the later work. Using a stable formula may require interpretation and checks at the connection. Changing the formula requires understanding its derivation. Designing a new algorithm or physical theory requires the additional specialist capability. When assessing a person's preparation, examine their contribution on representative work with the assistance that will actually be available. Include a change of the requested result or a relevant premise when later work requires that adaptation. Ask the practitioner to recover the retained relation, the new unknown and the dependent physical operation.

