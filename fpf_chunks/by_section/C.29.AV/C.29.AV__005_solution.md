---
chunk_kind: "child"
pattern_id: "C.29.AV"
pattern_title: "Derive a Condition from an Admissible Variation"
section_id: "C.29.AV:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.AV/C.29.AV__005_solution.md"
commit_sha: "f965ffb27d69ec5e4ae94f1bb0092c15fa13c991"
heading_path:
  - "C.29.AV — Derive a Condition from an Admissible Variation"
  - "C.29.AV:4 — Solution"
line_start: 64645
line_end: 64716
dependencies:
  - "B.5.MPC"
  - "B.5.RR"
  - "C.29"
  - "C.29.2"
keywords:
---

### C.29.AV:4 - Solution

**Construct an admissible family → calculate the change → derive the condition → establish what it settles → use or revise the result.**

#### C.29.AV:4.1 - Fix the comparison

State the candidate, the conditions to retain, the scalar quantity and the conclusion sought. Write the candidate as `x` and the quantity as `J(x)` when that notation helps. For minimization, smaller values of J are preferred; for maximization, reverse the comparisons below.

Keep the meaning of J visible. It might be a supplied allocation cost, an approximation error or a physical action functional, which assigns a number to a history. A physical principle can require stationarity of an action without selecting its minimum. Recover that principle and its conditions before using the variational calculation to describe physical behavior.

Distinguish a search for one improving change from a claim of local or global optimality. Local optimality concerns a specified neighborhood of the candidate; global optimality concerns all candidates admitted by the problem.

#### C.29.AV:4.2 - Construct changes that remain admissible

Build a family `x(h)` with `x(0)=x`. State the allowed values of the parameter h and substitute the family into the constraints. The parameter may be a scalar, a vector or a discrete choice.

For a fixed total `x1+x2=b`, the change `(x1+h, x2-h)` preserves the total. If both components must stay nonnegative, its range is `-x1 <= h <= x2`. A further capacity limit can shorten that range.

For a history with fixed endpoint values, try `q_h(t)=q(t)+h*eta(t)`, where eta vanishes at both endpoints and has the regularity required by the functional. Check any additional path constraint as well.

A direction tangent to a constraint may preserve it only to first order. At `(1,0)` on the unit circle, `(1,h)` has squared length `1+h^2` and leaves the circle whenever h is nonzero. The curve `(cos(h),sin(h))` stays on it. Use an admissible curve for a finite comparison, or keep a tangent calculation at the first-order scope its mathematical argument supports.

When a useful family cannot yet be constructed, the missing result is concrete: a parameterized change that retains the named constraint. Obtain the corresponding mathematical construction rather than continue with an inadmissible substitute.

#### C.29.AV:4.3 - Calculate the effect of the variation

Form the difference

`DeltaJ(h) = J(x(h)) - J(x(0)).`

Substitute the whole changed candidate, including dependent values. Simplify enough to determine the sign or magnitude relevant to the question.

For a differentiable comparison with a scalar parameter h near zero, write

`DeltaJ(h) = a*h + r(h), with r(h)/h -> 0,`

when that expansion is justified. The coefficient a is the first variation along this family. Higher-order terms or a bound on the remainder can be needed when a vanishes, or when choosing a finite step.

A derivative tells how sufficiently small changes behave under its limit assumptions. To select a particular step, check the finite difference or a bound that covers that step. For a discrete family, compare its admissible members directly; differentiability is not an entry requirement.

If the calculation uses a numerical approximation, relate its error to the sign or comparison being used. C.29.2 develops that computational task. A difference interval entirely below zero can establish improvement for minimization; an interval spanning zero leaves that comparison unresolved.

#### C.29.AV:4.4 - Derive a condition with the allowed directions

For minimization, an admissible h with `DeltaJ(h)<0` supplies an improvement. For a local conclusion, use families whose candidates approach the base candidate as h approaches zero, under the neighborhood notion of the problem.

At a local minimum, a differentiable family allowing sufficiently small changes of both signs must have `a=0`: a positive or negative a would give a decrease in one of those directions. If only small nonnegative h are allowed, the necessary condition is `a>=0`. For other parameter domains, test the directions actually available.

When a is zero, inspect the remaining change. The differences `h^2`, `-h^2` and `h^3` all have zero derivative at zero but respectively give a minimum, a maximum and neither on a two-sided neighborhood. This distinction changes whether the candidate is selected, rejected or needs a stronger argument.

For a vector of variation parameters, keep their joint constraints. Checking one coordinate at a time can miss an improving combination.

#### C.29.AV:4.5 - Establish the reach of the conclusion

Say which candidates the family reaches and which conclusion the calculation proves.

If every admissible candidate can be represented by a member of the family, and `DeltaJ(h)>=0` throughout its allowed domain, the base candidate is a global minimizer. If equality occurs only for the base candidate, it is the unique minimizer. An argument restricted to a neighborhood establishes the corresponding local result.

A narrower family can still supply an improving candidate or a necessary condition. Extending that condition to a stronger conclusion requires coverage of the relevant variations or an applicable sufficiency theorem. A convexity argument can sometimes supply the latter; recover its hypotheses before using it. Repeated failure of a chosen local move supplies no general global-optimality guarantee.

For a physical action, derive the stationarity condition required by the physical model. Establish a minimum only if the functional and allowed histories support that stronger conclusion. The free-history example below does so by a nonnegative finite difference.

#### C.29.AV:4.6 - Return the result to the working question

Use the obtained change or condition in the calculation, model or decision that needed it. Keep the admissible family and the reason for the conclusion in the explanation so another practitioner can alter the comparison.

When a criterion changes, recalculate its difference. When a constraint changes, rebuild the parameter domain or family first. B.5.RR helps revise the dependent reasoning while retaining what remains valid.

The mathematical comparison can be completed before any physical change is performed. B.5.MPC supplies the return to physical interpretation and use. If the question is whether an actual intervention causes a result, C.28 supplies the causal-use question.

Stop at the result sufficient for the current use. An improving feasible candidate can be enough to continue; a demand for the global optimum calls for the stronger argument.

