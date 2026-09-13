---
chunk_kind: "child"
pattern_id: "C.29.AV"
pattern_title: "Derive a Condition from an Admissible Variation"
section_id: "C.29.AV:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.AV/C.29.AV__006_archetypal-grounding.md"
commit_sha: "bbfb5347013400e9a895fa4b0f66992e931c0ece"
heading_path:
  - "C.29.AV — Derive a Condition from an Admissible Variation"
  - "C.29.AV:5 — Archetypal Grounding"
line_start: 64717
line_end: 64764
dependencies:
  - "B.5.MPC"
  - "B.5.RR"
  - "C.29"
  - "C.29.2"
keywords:
---

### C.29.AV:5 - Archetypal Grounding

#### C.29.AV:5.1 - Reallocate a fixed total, then change the criterion

Allocate ten divisible units between two uses: `x1>=0`, `x2>=0` and `x1+x2=10`. The supplied cost is `J=x1^2+x2^2`. Take the admissible family `(x1+h,x2-h)`, with `-x1<=h<=x2`.

Substitution gives

`DeltaJ(h)=2*(x1-x2)*h+2*h^2.`

For an interior candidate, both signs of small h are allowed. The first-order condition gives `x1=x2`, hence `(5,5)`. At this candidate, the entire finite difference is `2*h^2`. Every feasible allocation is `(5+h,5-h)` for `-5<=h<=5`, so this proves the unique global minimum, with cost 50.

Now change the cost to `J=x1^2+2*x2^2`, retaining the total and nonnegativity. The same family gives

`DeltaJ(h)=2*(x1-2*x2)*h+3*h^2.`

The condition becomes `x1=2*x2`, giving `(20/3,10/3)`. Its difference is `3*h^2` across the whole feasible interval, so its cost `200/3` is the unique minimum. Keeping the earlier equal split would miss the change introduced by the new criterion.

If the units must instead be whole, x1 and x2 are integers. Completing the square gives `J=3*(x1-20/3)^2+200/3`; the admissible integer closest to 20/3 is 7. Thus `(7,3)` has the lowest cost, 67, in that discrete problem. The continuous stationary point helped locate the candidates; the integer comparison settles their use.

Keep the weighted cost `J=x1^2+2*x2^2`, make the units divisible again, and add `x1<=6` while retaining the total and nonnegativity. The previous continuous minimizer `(20/3,10/3)` is now unavailable. At `(6,4)`, the allowed family has `-6<=h<=0` and

`DeltaJ(h)=-4*h+3*h^2>=0.`

This family covers every newly feasible allocation. Thus `(6,4)`, with cost 68, is the unique global minimizer despite its nonzero derivative along the unrestricted line. The parameter domain carries the decisive information.

These are calculations for the stated cost model. Its use in an allocation decision requires the supplied cost to represent the consequence being compared.

#### C.29.AV:5.2 - Compare histories between fixed endpoints

Consider a one-dimensional free particle with mass `m>0`, elapsed time `T>0`, and fixed positions `q(0)=0`, `q(T)=L`. The model's action is

`J[q] = integral from 0 to T of (m/2)*(qdot(t))^2 dt.`

Take the straight history `q0(t)=L*t/T`. For any continuously differentiable eta with `eta(0)=eta(T)=0`, construct `q_h(t)=q0(t)+h*eta(t)`. Expanding the square gives

`DeltaJ(h) = (m*h*L/T)*integral eta_dot(t) dt + (m*h^2/2)*integral eta_dot(t)^2 dt.`

The first integral is `eta(T)-eta(0)=0`. The remaining term is nonnegative, and it vanishes for a changed history only when its derivative change is identically zero; the fixed endpoints then force the change itself to vanish. Every continuously differentiable history with these endpoints can be expressed as q0 plus such a change. The straight history therefore uniquely minimizes this functional over that class.

The construction exposes the reason: the fixed endpoints remove the cross term, while every remaining velocity deviation adds a nonnegative contribution.

Now include a restoring potential. In dimensionless variables, use the harmonic-oscillator action `J[q]=integral from 0 to 2*pi of (qdot^2-q^2)/2 dt`, with `q(0)=q(2*pi)=0`. At the history `q=0`, every admissible family `q_h=h*eta` has zero first variation. Yet the admissible directions `eta=sin(t/2)` and `eta=sin(3*t/2)` give respectively `DeltaJ=-3*pi*h^2/8` and `DeltaJ=5*pi*h^2/8`: integration uses `integral eta^2 dt=pi` and `integral eta_dot^2 dt=n^2*pi/4` for these directions with n=1 and n=3. Arbitrarily small changes of both lower and higher action are available. The stationary history is therefore a saddle, not a minimum.

Changing an endpoint condition also requires rebuilding the allowed histories before reusing the free-particle argument. Its vanishing cross term depended on both endpoint values.

This example uses a supplied classical model. Constructing an appropriate action for an unfamiliar physical system is a further physical and mathematical modeling task.

