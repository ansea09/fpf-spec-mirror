---
chunk_kind: "child"
pattern_id: "B.5.MPC"
pattern_title: "Connect Physical, Mathematical and Computational Reasoning"
section_id: "B.5.MPC:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.MPC/B.5.MPC__006_archetypal-grounding.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "B.5.MPC — Connect Physical, Mathematical and Computational Reasoning"
  - "B.5.MPC:5 — Archetypal Grounding"
line_start: 41536
line_end: 41672
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

### B.5.MPC:5 - Archetypal Grounding

The following are constructed cases under stated assumptions. They show how the coordinating Method obtains a jointly interpretable consequence. Physical motion, an assembled gear mechanism and an operating admission system require their corresponding physical arrangements and evidence.

#### B.5.MPC:5.1 - Construct a robot command from a motion question

An engineer wants a robot to advance by 1 m along a straight guide. The guide keeps its direction fixed. For this calculation, the effective rolling radius of the driven wheel is 0.05 m; rolling occurs without slip; the transmission makes ten motor revolutions for one wheel revolution; and successful execution advances the motor by one thousand commanded increments per motor revolution. Positive motor motion is defined to produce forward travel. The initial question is a conditional command design under those assumptions.

First construct the relation from the participants. One wheel revolution rolls through its circumference, 2π × 0.05 m. The motor makes ten revolutions during that wheel revolution, so that travel corresponds to 10 × 1,000 = 10,000 motor increments. Let N be the signed number of motor increments completed after the command begins. The modeled displacement s is:

~~~text
wheel revolutions = N / (1,000 × 10)
s = [N / (1,000 × 10)] × 2π × 0.05 m
distance per motor increment = 0.0000314159265359 m
~~~

The factors expose the two distinct revolutions and the command unit. A statement that the wheel turns through 2π radians would give orientation change for one turn; the present N retains accumulated turns because the receiving quantity is accumulated travel.

Invert this relation for the target displacement:

~~~text
N_ideal = 1 m / (2π × 0.05 m) × 10 × 1,000
        = 31,830.9886183791 motor increments
N_command = nearest integer to N_ideal = 31,831
~~~

The computational procedure reads the target distance and the three parameters, computes the ideal count and rounds it to the nearest integer. Use enough numerical precision to determine that integer; if arithmetic uncertainty straddles a rounding boundary, refine the calculation or retain the resulting command uncertainty.

Now supply the realization input. The interface accepts signed relative motor-increment commands in the range −32,768 to 32,767. It performs a command to completion before reporting successful completion. Thus 31,831 is representable and its unit and relative-command meaning agree with the calculation. A different interface would require its own preparation relation.

Read the completed command back through the physical model:

~~~text
s_command = 31,831 / 10,000 × 2π × 0.05 m
          = 1.00000035756417 m

maximum error from rounding to the nearest increment
          = 0.5 / 10,000 × 2π × 0.05 m
          = 0.0000157079632679 m
~~~

The rounding bound concerns discretization of the command. It leaves slip, effective-radius error and unsuccessful motor execution outside that numerical bound. If the engineering question is actual travel within a tolerance, those contributions determine whether this command is adequate. For example, motor counts alone cannot discriminate successful rolling from wheel rotation with slip; a displacement measurement needs its own relation to position.

The joint result is the command 31,831 and its modeled consequence under the physical and interface conditions. Physics supplies the rolling and transmission account. Mathematics supplies the relation, its inversion and the error bound. Computation supplies the integer and range check. The coordination connects their meanings and returns the supported displacement.

The same interface's largest positive relative command represents about 1.0294056648 m under this model. If the requested distance and tolerated error require a larger positive count, use another realization or a procedure using several commands whose combination is justified. If the wheel radius, the count's meaning or the use of initial position changes, reconstruct the affected relation before reusing the command. Those changes can affect the physical parameter, mathematical expression and command preparation together; recover the disagreement and its dependent contributions as in :4.6.

#### B.5.MPC:5.2 - Use two-colouring to answer a gear question

A designer asks whether every gear in a connected arrangement can rotate while all specified meshes remain engaged. The supplied idealized account has parallel, fixed axes, external gear contacts and positive pitch radii. View every rotation from the same side. At each external mesh, the two gears have opposite signs of angular velocity. Contact geometry and tooth compatibility are additional physical conditions; this first question concerns the consistency of rotation directions.

Construct a finite undirected graph. A vertex represents one gear and an edge represents one of the stipulated external meshes. Assign colour 0 to one rotation direction and colour 1 to the other. An edge requires different colours at its endpoints. This expression makes the physical question a mathematical one: can the vertices be assigned two colours while satisfying every edge?

The graph records actual contact, not geometric closeness on the page. A drawing with crossing lines does not add a mesh between the gears at that crossing. If an actual contact is absent from the list, the result answers only the incomplete list.

Obtain either a colouring or a witness of failure by the following procedure.

1. Choose an uncoloured vertex as a root. Give it colour 0, depth 0 and no parent; place it on a waiting list.
2. Remove the first vertex from the list and inspect its neighbours. Give each uncoloured neighbour the opposite colour, record the removed vertex as its parent, give the neighbour depth one greater and append it to the list.
3. For an already coloured neighbour, compare colours. If they agree, use that edge and the two parent paths to construct the odd-cycle witness explained below, and return it.
4. Continue until the list is empty. Start another root if an uncoloured vertex remains. If every edge joins different colours, return the colouring.

A vertex is added to the waiting list only once. Each recorded parent has smaller depth, so parent paths reach their root. A finite graph therefore yields a result after all relevant vertices and edges have been examined, or after a contradiction has been found. With adjacency lists, constant-cost access to a vertex's recorded data, and constant-cost insertion and removal in the FIFO waiting queue, the work is proportional to the number of vertices plus edges.

Work a square contact cycle with gears A, B, C and D and contacts AB, BC, CD and DA. Starting at A gives A colour 0; B and D colour 1; and C colour 0. Every contact joins opposite colours. The groups {A,C} and {B,D} therefore give compatible direction choices. Reversing both groups gives the other choice. Four equal pitch circles can be placed with centres at the corners of a square of side twice the pitch radius to obtain those contact incidences; tooth engagement and motion under load still require the corresponding mechanical design.

Now work three gears with contacts AB, BC and CA. Starting at A gives B and C colour 1. Edge BC then joins equal colours. Its endpoints' parent paths B–A and C–A, together with BC, give the three-edge closed path B–A–C–B. Alternating directions around three external contacts asks B to have both directions at once.

The same reasoning constructs a failure witness in a larger graph. For a same-colour edge, follow its endpoints' parent paths until their nearest common vertex. Discard the shared path beyond that vertex. The retained paths have even total length because the endpoints have the same depth parity. The extra edge closes a simple odd cycle. Alternating two colours cannot satisfy every edge of an odd cycle. Conversely, if the procedure finishes without such an edge, its returned colours satisfy every listed constraint.

The physical interpretation can be made quantitative without hiding the direction question. Let rᵢ be a gear's pitch radius and ωᵢ its signed angular velocity. Ideal external meshing with fixed axes gives:

~~~text
rᵢωᵢ + rⱼωⱼ = 0 at each mesh
qᵢ = rᵢωᵢ, so qⱼ = −qᵢ
~~~

For a two-colouring, choose any nonzero value q for one colour and −q for the other, then set ωᵢ = qᵢ/rᵢ. This satisfies those kinematic equations. For an odd cycle, following the equations around the cycle gives q = −q and hence q = 0. In a connected graph all gears then have zero angular velocity. Thus the odd cycle excludes the requested nonzero coupled rotation under the stipulated contact model; a stationary arrangement remains compatible with the equations.

Return the cycle as the particular set of physical contacts responsible for the obstruction. Removing one actual contact from the triangle leaves a chain and permits alternating directions. Deleting only its graph edge leaves the physical obstruction in place. An internal gear contact or a moving carrier changes the contact rule and requires a revised physical account before the colouring test is reused.

A compatible direction assignment answers this bounded question. It does not establish adequate torque, tooth phasing, freedom from interference or motion under the intended load. For those questions, retain the graph result and obtain the missing mechanical contribution. The common Method supplies the contact interpretation, the connection to the computational witness and the return to the design. The gear account and graph argument supply the substantive rules that make that return possible.

#### B.5.MPC:5.3 - Maintain an admission bound through material tokens

A demonstration room should contain at most three visitors. Initially the room is empty and three distinct material cards are available. An attendant gives a free card to one visitor before entry. That visitor keeps it while inside and returns it after leaving. A new visitor waits for a card when none is free.

For this case, every entrance and exit follows the procedure, each card is exclusively assigned to one visitor at a time, and cards are neither lost nor duplicated. The material arrangement makes exclusive acquisition possible: taking the available card removes that same card from the free stock. A photograph or printed copy of the card is not accepted for entry.

First consider a moment when every assigned card is held by a visitor inside and every other card is free. The one-card-per-visitor rule gives:

~~~text
occupancy = 3 − number of free cards
~~~

During admission and return, cards can also be held by visitors outside. A visitor may already hold a card while waiting to enter; a departed visitor may still be walking to its return point. To preserve the physical meaning during those intervals, distinguish four states for each card:

| State | Physical interpretation |
| --- | --- |
| Free | The card is available for a new admission. |
| Reserved | The card is held by a visitor who has not yet entered. |
| Inside | The card is held by its visitor inside the room. |
| Awaiting return | Its visitor has left, but the card is not yet free. |

Let F, R, I and E count cards in those four states. Every card occupies exactly one state, so F + R + I + E = 3. Under the visitor-to-card rule, occupancy = I. Therefore:

~~~text
occupancy = I = 3 − F − R − E
occupancy ≤ 3 − F ≤ 3
~~~

The transition procedure has four ordinary operations: issue one free card to a waiting visitor; admit that card's visitor; let the visitor leave with the card; and return the departed visitor's card to the free stock. Their state changes are Free → Reserved → Inside → Awaiting return → Free. A cancelled admission can return a Reserved card directly to Free while its visitor remains outside.

Each operation moves one existing card between states. Issuing a card requires a free card; entering requires its exclusive reservation; returning it requires that its visitor is already outside. Those conditions preserve the total stock and the association between visitors inside and Inside cards. The argument establishes the capacity bound for every sequence of those permitted operations, including overlapping visits.

Work two entries followed by one exit:

| Operation just completed | F | R | I | E | Occupancy |
| --- | ---: | ---: | ---: | ---: | ---: |
| Initial arrangement | 3 | 0 | 0 | 0 | 0 |
| Issue card A | 2 | 1 | 0 | 0 | 0 |
| Visitor A enters | 2 | 0 | 1 | 0 | 1 |
| Issue card B | 1 | 1 | 1 | 0 | 1 |
| Visitor B enters | 1 | 0 | 2 | 0 | 2 |
| Visitor A leaves | 1 | 0 | 1 | 1 | 1 |
| Return card A | 2 | 0 | 1 | 0 | 1 |

Counting free cards gives an upper bound on occupancy during handover and return. It gives the exact occupancy when R = E = 0. That distinction changes what an observer may infer from the same stock. The admission rule can preserve the bound without an exact instantaneous occupancy readout.

Connect the abstract transition rule to the physical means. Exclusive possession realizes consumption of a free token. Carrying it through entry preserves the visitor association. Returning it only after exit prevents its use for a fourth visitor while the first three remain inside. If a visitor passes their card to someone outside while staying inside, the allowed-transition premise fails: the reused card no longer represents one occupied or reserved place.

A second entrance needs access to the same total stock. A copied stock of three additional accepted cards permits six simultaneous admissions, even if both attendants follow their local rule correctly. A shared pool of the original three cards preserves the common bound. Partitioning those same cards, for example two at one entrance and one at the other, also preserves it. The partition can make a visitor wait at one entrance while a card is free at the other; redistribution then needs a transfer of an existing free card.

The useful result is a conditional admission design and an interpretation of its observable stock. Its computational contribution is a finite-state procedure that answers whether an admission can proceed and maintains the relevant count. People and material transfers can execute it without a digital program. The invariant does not establish fair waiting, fast entry or detection of every procedural violation; those are different questions with their own needed contributions.

The coordinating Method makes the physical card and room-boundary rules, mathematical invariant and executing procedure agree. This is also why changing the stock or the return rule changes the joint result even when the counting arithmetic remains correct.

