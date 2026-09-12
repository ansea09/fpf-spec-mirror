---
chunk_kind: "child"
pattern_id: "C.29.3"
pattern_title: "Computational Realization"
section_id: "C.29.3:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.3/C.29.3__006_archetypal-grounding.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "C.29.3 — Computational Realization"
  - "C.29.3:5 — Archetypal Grounding"
line_start: 60669
line_end: 60768
dependencies:
  - "A.3.3"
  - "A.6.1"
  - "B.5.MPC"
  - "C.16"
  - "C.29.2"
keywords:
---

### C.29.3:5 - Archetypal Grounding

These constructed cases expose different realization failures. They establish consequences of the stated models; using an actual apparatus also requires the relevant physical and operating knowledge.

#### C.29.3:5.1 - Carry a calculated count through a finite command interface

A robot's supplied motion model uses rolling without slip, effective wheel radius 0.05 m, ten motor revolutions per wheel revolution and one thousand commanded increments per motor revolution. Positive motor increments produce forward travel. Successful execution completes the requested relative increment.

For a requested distance d, calculate and round:

~~~text
N = nearest integer to ((d / (2π × 0.05 m)) × 10 × 1000)
modeled displacement = N / 10000 × 2π × 0.05 m
~~~

One metre gives 31,831 increments and a modeled displacement of approximately 1.0000003576 m. Rounding contributes at most half an increment, approximately 0.0000157080 m. This bound concerns command discretization under the supplied motion relation.

The interface accepts signed 16-bit values from -32,768 to 32,767. The one-metre input is representable. Two metres require 63,662 increments, which cannot be prepared as one positive value in that field.

Suppose the interface wraps modulo 65,536 and interprets the result as signed. Then:

~~~text
63,662 − 65,536 = -1,874
modeled displacement ≈ -0.0588734463 m
~~~

The calculation of the desired count remains correct; input preparation changes the delivered count. An interface that rejects the value would produce a different failure, so the actual interface behavior matters.

One repair uses two completed commands of 31,831. Under the relative-addition rule, their total is 63,662 and their modeled displacement is approximately 2.0000007151 m. The preparation now supplies two representable values, and the execution argument uses addition across their completed displacements.

If a command means "reach this absolute count," repeating 31,831 leaves the same target. For an absolute interface, reconstruct the target from the initial count and check that the resulting target is representable. B.5.MPC supplies the wider comparison when the motion model or the count's physical meaning also changes.

A range restriction is another useful repair. The largest positive relative command corresponds to approximately 1.0294056648 m under this model. Whether that restriction is adequate depends on the requested motion. A deadline can make two commands unsuitable even when their displacements add.

The result is a command procedure with a stated input range and composition rule. For actual travel, determine whether the commands were completed and use a measurement or physical relation that accounts for consequential slip and effective radius.

#### C.29.3:5.2 - Read an analog sum with the output scale it needs

An existing analog channel is intended to supply the sum of two numbers x and y in the range 0 to 10. Its input preparation sets voltages:

~~~text
Vx = x / 10 volts
Vy = y / 10 volts
~~~

Each source is connected through an equal resistor R to one common node. The supplied electrical model has ideal voltage sources, equal resistances, settled behavior and a readout drawing negligible current. The resistor-current relation and current balance at the node give:

~~~text
(Vx − Vout) / R + (Vy − Vout) / R = 0
Vout = (Vx + Vy) / 2
~~~

The arrangement physically produces an average voltage. To obtain the intended sum, derive its readout:

~~~text
decoded result = 20 × [Vout expressed in volts]
               = x + y
~~~

For x = 8 and y = 6, preparation gives 0.8 V and 0.6 V. The node gives 0.7 V. Decoding returns 14. Reusing the input scale, ten units per volt, would return 7.

The abstract and physical routes now agree. Input preparation and output interpretation use different factors because the intervening operation halves the voltage sum.

Now allow each prepared input voltage an error of at most 0.001 V. Suppose the readout indication has an additional error of at most 0.002 V under the same circuit model. The worst-case error in the indicated output is:

~~~text
0.5 × 0.001 V + 0.5 × 0.001 V + 0.002 V = 0.003 V
decoded-result error ≤ 20 × 0.003 = 0.06
~~~

An absolute tolerance of 0.1 is therefore met under these bounds. A tolerance of 0.01 is not established by them. Better input setting or readout, a different realization, or a weaker receiving requirement would need comparison. The bound is deterministic; no cancellation or probability distribution has been assumed.

If the instrument loads the node or the resistor values differ, the stated averaging relation needs revision. Those changes belong in the circuit and measurement account, through C.16 where appropriate. The common realization method supplies the preparation/execution/readout comparison and the receiving error calculation. Electrical design supplies the physical law and actual component behavior.

#### C.29.3:5.3 - Preserve a bound during material admission operations

A demonstration room has a capacity of three visitors. It starts empty with three distinct cards in a free stock. One card is issued to a visitor before entry; the visitor retains it inside and returns it after exit. Every entry follows this rule, each visitor inside holds one card, each card is exclusively assigned, and cards are not lost or duplicated.

The computation is the continuing admission decision and preservation of the capacity bound. People and material transfers execute its finite-state procedure.

A card can be Free, Reserved outside, Inside with its visitor, or Awaiting return after exit. Let F, R, I and E count those states. The fixed stock gives:

~~~text
F + R + I + E = 3
occupancy = I
occupancy = 3 − F − R − E ≤ 3 − F ≤ 3
~~~

Issuing a card changes Free to Reserved. Entry changes Reserved to Inside. Exit changes Inside to Awaiting return. Return changes Awaiting return to Free. Cancellation can return a Reserved card to Free while its visitor remains outside.

Every operation moves one existing card between states. Entry requires its exclusive reservation. Return requires that its visitor is outside. These conditions preserve both the stock and the association between visitors inside and Inside cards. They establish the capacity bound throughout permitted histories, including overlapping admissions.

After two cards have been issued, one visitor may be inside and the other waiting outside. Then F = 1, R = 1, I = 1 and E = 0. The count of unavailable cards is 2, while occupancy is 1. Reading occupancy as 3 − F would be wrong. That count is an upper bound until R = E = 0.

A second entrance can share the same stock or receive a partition of it, such as two cards at one entrance and one at the other. Both preserve the total of three. Giving the second entrance three copied cards instead permits six simultaneous admissions, despite each attendant following their local procedure.

Partitioning can cause waiting at one entrance while a card is free at the other. Moving an existing free card preserves the total; creating another accepted card changes it. This separates the capacity property from the additional question of useful service across entrances.

The result is a conditional admission arrangement, its preserved bound and a qualified reading of the free stock. The administrative method supplies controlled entry, exclusive possession and return. The mathematical construction makes explicit which physical and procedural properties the computation consumes.

