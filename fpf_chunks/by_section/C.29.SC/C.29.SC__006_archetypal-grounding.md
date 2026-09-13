---
chunk_kind: "child"
pattern_id: "C.29.SC"
pattern_title: "Derive a Consequence from a Symmetry"
section_id: "C.29.SC:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.SC/C.29.SC__006_archetypal-grounding.md"
commit_sha: "bbfb5347013400e9a895fa4b0f66992e931c0ece"
heading_path:
  - "C.29.SC — Derive a Consequence from a Symmetry"
  - "C.29.SC:5 — Archetypal Grounding"
line_start: 64929
line_end: 64974
dependencies:
  - "A.3.3.TR"
  - "C.29.1"
  - "C.29.2"
  - "C.29.AV"
keywords:
---

### C.29.SC:5 - Archetypal Grounding

#### C.29.SC:5.1 - A symmetric allocation and an asymmetric optimum

Let `x1,x2>=0`, `x1+x2=10`, and minimize `J=x1^2+x2^2`. Swapping x1 and x2 preserves both the feasible set and J.

The cost is strictly convex on this feasible segment, and a minimizer exists because the segment is compact and the cost is continuous. Hence the minimizer is unique. The symmetry condition requires `(x1,x2)=(x2,x1)`, so the only possible optimum is `(5,5)`. The direct calculation `J(5+h,5-h)=50+2*h^2` confirms it for every feasible h.

Now use `J=x1^2+2*x2^2` under the same resource constraint. Swapping the allocations changes the cost: `J(10,0)=100` and `J(0,10)=200`. The original exchange symmetry is gone. The optimum is `(20/3,10/3)`, as the admissible-variation construction in C.29.AV shows.

Symmetry alone also need not make individual solutions symmetric. If the original sum-of-squares criterion is maximized on the same segment, `(10,0)` and `(0,10)` are both maxima. The swap exchanges them. The midpoint is fixed by the swap but is the minimum, so selecting it from symmetry without the uniqueness and optimization premises would answer a different question.

#### C.29.SC:5.2 - A unique choice from an indistinguishable arrangement

A selector receives a three-vertex cycle with identical vertex attributes and equal edge attributes. Its output must designate exactly one vertex. Rotating the cycle is treated as a relabeling: the requested deterministic rule must rotate its selected vertex in the same way.

For this input, a one-step rotation leaves the supplied arrangement unchanged. Equivariance therefore requires the selected vertex to be fixed by that rotation. No vertex is fixed: each moves to the next vertex. The requested deterministic selector has no permitted output for this input.

One repair is to supply a distinguished attribute, such as an available unique priority, and let the rule use it. Another is to change the requested result to the set of all three equally admissible vertices. Random selection is another problem: a uniform distribution can be rotation-invariant even though a sampled vertex is not fixed. The construction of a coordinated random choice would need its own procedure.

This is a mathematical result about the given input and rule requirements. Extra identifiers, timing distinctions or other available attributes can change the input symmetry and therefore the conclusion. It does not establish that every real three-agent arrangement faces this obstruction.

#### C.29.SC:5.3 - A symmetry of motion and what a numerical step preserves

Consider the planar model `qdot=v`, `vdot=-q`. Applying the same planar rotation R to q and v preserves these equations. Thus a trajectory starting at `(q0,v0)` produces a rotated trajectory starting at `(R*q0,R*v0)`.

For `q0=(1,0)`, `v0=(0,1)`, a quarter-turn changes the initial data. The transformed trajectory solves another initial-value problem. Uniqueness for the original data therefore does not imply that its trajectory is fixed by every rotation.

In this model, `J=x*vy-y*vx` is angular momentum for unit mass. Direct differentiation gives

`Jdot = x*ay-y*ax = x*(-y)-y*(-x)=0.`

This establishes conservation along its trajectories. A radial law `vdot=-k(t)*q` gives the same cancellation. The proof uses the acceleration relation; the rotational description alone is not the argument.

Now compute with explicit Euler:

`q_next=q+h*v; v_next=v-h*q.`

The update is equivariant under the same rotations because R distributes over the linear combinations. Yet substitution gives

`J_next=(1+h^2)*J.`

Starting with J=1, h=0.1 and taking one hundred steps yields about 2.7048. Rotation equivariance of the scheme has survived while conservation of J has failed. If the question uses angular momentum, the computational construction must be changed or its error made acceptable for that use.

For this model, the update `v_next=v-h*q; q_next=q+h*v_next` preserves J by substitution. Its preservation of this quantity is one property of that scheme; questions about phase or other errors retain their own numerical analysis.

