---
chunk_kind: "child"
pattern_id: "A.3.3.CC"
pattern_title: "Construct a Configuration Description under Constraints"
section_id: "A.3.3.CC:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3.CC/A.3.3.CC__006_archetypal-grounding.md"
commit_sha: "acc387fc7a206495eabe07f1953849217f291715"
heading_path:
  - "A.3.3.CC — Construct a Configuration Description under Constraints"
  - "A.3.3.CC:5 — Archetypal Grounding"
line_start: 9739
line_end: 9784
dependencies:
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.3.3"
  - "A.6.3.RT"
  - "B.5.FM"
  - "B.5.MPC"
  - "C.29.1"
  - "C.29.2"
keywords:
---

### A.3.3.CC:5 - Archetypal Grounding

#### A.3.3.CC:5.1 - A rigid link, then a variable length

Consider a freely placed link in a plane, with distinguishable endpoints A and B and fixed length 2 metres. Use one Cartesian reference frame. The implicit description is

`q = (xA, yA, xB, yB)`, with `(xB - xA)^2 + (yB - yA)^2 = 4`.

The tuple (0, 0, 2, 0), in metres, satisfies the relation. The tuple (0, 0, 1, 0) fails it. Each endpoint separately has a valid position in the plane, but the second pair violates the modeled link.

For locating the endpoints, use parameters X, Y and orientation phi:

`A = (X, Y)`; `B = (X + 2 cos(phi), Y + 2 sin(phi))`.

Every pair of endpoints at distance 2 has such a representation. Orientations differing by a full turn describe the same configuration. Reversing the direction while keeping A fixed changes B, so identifying opposite orientations would lose a distinction of this labeled-endpoint model.

Now allow the link to extend or contract with length `0 < r <= 3`. Replace 2 by the variable r. The formerly rejected pair (0, 0, 1, 0) is admitted at r = 1. A later motion calculation needs a law for the changing length and whatever initial data that law requires. If the question concerns force carried by a rigid constraint, retaining its equation can help express the force calculation through a multiplier; eliminating the constraint from position coordinates has not answered that force question.

#### A.3.3.CC:5.2 - Buffer counts, external arrivals and job order

Two buffers each hold at most two jobs. Exactly three jobs are distributed between them. The product of count ranges is `{0,1,2} x {0,1,2}`; the stock condition is `q1 + q2 = 3`.

Testing the nine pairs leaves `Q = {(1,2), (2,1)}`. Equivalently, choose q1 from {1,2} and reconstruct `q2 = 3 - q1`. The description now supplies both possible occupancy arrangements.

An external arrival can raise the total to four. Keeping `q2 = 3 - q1` would omit the possible arrangement (2,2). Retain both counts and use the total applicable to the new question, or include total N as a variable with `q1 + q2 = N`. Which arrival can occur, and when, comes from an arrival and transition account.

Suppose the next question asks which job a first-in-first-out buffer serves. The sequences [A,B] and [B,A] have the same count, yet they give different next jobs under that rule. Represent the ordered job identities in the relevant buffer. Counts remain recoverable as sequence lengths; the receiving operation gains the distinction it lacked.

#### A.3.3.CC:5.3 - A body must fit, not just its reference point

A rigid body occupies the one-dimensional interval `[x-r, x+r]`; x is its centre and r its half-length. It must lie wholly inside `[0,L]`. Contact with the endpoints is permitted in this model.

Containment gives `x-r >= 0` and `x+r <= L`, hence `r <= x <= L-r`. For L = 3 and r = 1, the admissible centres are [1,2]. Centre x = 0.5 lies inside the container but places part of the body outside it, so a point-only test gives the wrong fitting answer.

If clearance is required, include the clearance in the inequalities. If L = 1.5 while r remains 1, the interval for x is empty. That conditional impossibility directs the next decision to the body size, container size or permitted deformation. It was obtained by connecting a physical extent, a mathematical inequality and a calculation; no motion simulation was needed.

#### A.3.3.CC:5.4 - A velocity restriction leaves a configuration question open

For an ideal car rolling in a plane without lateral wheel slip, let (x,y) be the point halfway between the rear wheels and theta the chassis orientation. Let v be this point's velocity component along the chassis's forward direction. Then

`xdot = v cos(theta)`, `ydot = v sin(theta)`,

so `sin(theta) xdot - cos(theta) ydot = 0`. At theta = 0 the rear reference point has ydot = 0.

This equation constrains a velocity at a configuration. It does not impose a fixed y coordinate: a stationary car at another y satisfies the same velocity condition with v = 0. Whether a car can reach a selected parking position from its current one also depends on steering, obstacles and an allowed sequence of motions. Preserve those as a planning question instead of deleting the position from the configuration description.

