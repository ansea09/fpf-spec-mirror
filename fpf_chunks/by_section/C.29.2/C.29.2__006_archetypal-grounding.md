---
chunk_kind: "child"
pattern_id: "C.29.2"
pattern_title: "Computational Formulation"
section_id: "C.29.2:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.2/C.29.2__006_archetypal-grounding.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "C.29.2 — Computational Formulation"
  - "C.29.2:5 — Archetypal Grounding"
line_start: 60681
line_end: 60832
dependencies:
  - "A.10"
  - "A.3.1"
  - "A.3.3"
  - "A.6.1"
  - "A.6.3.RT"
  - "B.1.5"
  - "B.1.6"
  - "B.3"
  - "B.5"
  - "C.16"
  - "C.2.1"
  - "C.29.1"
  - "C.29.3"
  - "C.39"
  - "C.40"
keywords:
---

### C.29.2:5 - Archetypal Grounding

The cases construct an interpreter, a bounded numerical approximation, a resource-sensitive representation, two computations from one system of relations, and a probability estimate with an error guarantee. Their conclusions follow under the stated mathematical and physical premises.

#### C.29.2:5.1 - Make calculation rules available as data

**Question.** A team must change an integer calculation without changing the executor. The input is an integer `x0` and a finite sequence `P` consisting of `n` instructions chosen from `increment` and `double`, followed by one `stop`. Other sequences are outside this procedure's admitted input class.

**Construction.** Store the ordered sequence and use mutable state `(p, x)`: the position of the next instruction and the current integer. Positions start at zero. The meaning of the output is the left-to-right composition of the arithmetic instructions applied to `x0`.

```text
p := 0
x := x0
while P[p] != stop:
    if P[p] == increment:
        x := x + 1
    else:                         # the admitted alternative is double
        x := 2*x
    p := p + 1
return x
```

This explains the elementary operations and their order. A parser or caller admitting other strings must validate the sequence or define the additional cases; it must not silently interpret an unknown instruction as doubling.

| Instructions and input | Initial state | After first operation | After second operation | Read at stop |
| --- | --- | --- | --- | --- |
| `increment, double, stop`; `x0 = 3` | `(0,3)` | `(1,4)` | `(2,8)` | `8` |
| `double, increment, stop`; `x0 = 3` | `(0,3)` | `(1,6)` | `(2,7)` | `7` |

**Argument.** After `p` arithmetic steps, `x` is the result of applying exactly the first `p` instructions to `x0`, and `0 <= p <= n`. Initialization gives the empty composition. Each branch applies the next specified operation and advances the position, preserving that statement. While an arithmetic instruction remains, `n-p` decreases by one and cannot be negative. At `p=n` the next instruction is `stop`, so the returned integer is the requested composition. With `P = [stop]`, the same procedure returns `x0` immediately.

**Cost changes with representation.** Counting one step for each arithmetic instruction and the final `stop` gives `n+1` instruction steps, apart from validation and input/output costs. That does not make arbitrary-size arithmetic constant-time. Represent the magnitude in binary and retain the sign separately. Let `b0` be the binary length of `|x0|`, counting zero as one bit. Each operation increases the magnitude's length by at most one, so the current magnitude needs at most `b0+n` bits, plus one sign bit. The position and stored program need additional space.

With simple materialized binary arithmetic that scans or copies the current digits, an arithmetic step on `b` bits costs at most proportional to `b`. Summing the growing lengths gives an arithmetic-work upper bound proportional to `n*b0 + n^2` for that implementation, before any separately material program-access costs. A representation that treats doubling differently requires another estimate. On a fixed-width integer implementation, enough increments or doublings can instead overflow; the exact-integer argument then requires a range restriction or a different realization.

**What became possible.** The executor can perform any calculation in this finite instruction class by receiving another sequence. [Turing's 1936 construction, §§5–7](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf), makes encoded computation rules available to an interpreter; this small case uses that constructive idea. Turing's universal-machine result concerns a much richer simulation construction. Adding jumps or continuing input to this case changes its progress and cost questions and requires their own argument.

#### C.29.2:5.2 - Turn a root condition into a bounded approximation

**Question and representation.** Return a rational approximation `y` to the positive root of `z^2 = 2` with `|y - sqrt(2)| <= 0.001`. The equation characterizes the root. The requested rational output still needs a way to compute it. Use exact rational arithmetic in this construction.

The initial interval is `[l,u] = [1,2]` because `1^2 <= 2 <= 2^2`. For nonnegative arguments squaring is increasing, so a comparison of the midpoint's square with 2 determines which half still contains the root.

```text
l := 1
u := 2
epsilon := 1/1000
while u - l > 2*epsilon:
    m := (l + u)/2
    if m*m < 2:
        l := m
    else:
        u := m
return (l + u)/2
```

**Meaning and argument.** The preserved statement is `1 <= l <= sqrt(2) <= u <= 2`. The square comparison preserves it, and every iteration halves the interval width. After `k` iterations that width is `2^(-k)`. The returned midpoint therefore differs from the root by at most `2^(-k-1)`. Choosing the first `k` for which this is at most `epsilon` supplies both the stopping rule and a finite bound on the iteration count for every positive requested tolerance.

| Halvings | Retained interval |
| --- | --- |
| 0 | `[1, 2]` |
| 1 | `[1, 1.5]` |
| 2 | `[1.25, 1.5]` |
| 3 | `[1.375, 1.5]` |
| 8 | `[1.4140625, 1.41796875]` |
| 9 | `[1.4140625, 1.416015625]` |

After nine halvings, return `1449/1024 = 1.4150390625`. Its error is at most `1/1024 = 0.0009765625`, which satisfies the requirement. The interval argument establishes the bound without requiring a previously calculated decimal expansion of the root.

**Resource and accuracy consequences.** There are nine midpoint-square comparisons in this case. For finer tolerances, the dyadic numerators and denominators grow; a count of comparisons alone does not include the growing cost of exact squaring. A finite precision version must preserve the bracket decisions and avoid a midpoint that rounds to an endpoint while the tolerance remains unmet. Output rounding also consumes accuracy. These are returns to arithmetic and representation choices, not evidence that the exact rational construction failed.

For a costly general continuous function, an established bracketed method using interpolation may save function evaluations. Bisection remains useful when a simple interval argument and predictable reduction are worth the extra evaluations. For a function not known to be continuous, a sign change alone does not justify this root argument. A demand for an exact finite decimal expansion of this irrational root changes the answer format to an impossible one; an exact symbolic expression or a rational approximation is a different, obtainable request.

#### C.29.2:5.3 - Count a dense state before allocating it

**Question.** Can a proposed dense numerical pure-state array for 50 qubits fit in a 64 GiB memory budget? The representation stores one complex amplitude for each binary string of length 50. There are two choices at each position, hence `2^50` entries. Stipulate 16 bytes per stored complex value: two 8-byte components.

The payload alone is:

`16 × 2^50 = 2^54 = 18,014,398,509,481,984 bytes`,

or `16 PiB = 16,777,216 GiB`, where `1 GiB = 2^30 bytes` and `1 PiB = 2^50 bytes`. Since `64 GiB = 2^36 bytes`, the payload exceeds the budget by a factor of `2^18 = 262,144`. Workspace, copies and indexing cannot reduce this payload requirement. This rejects the proposed dense allocation without building the simulator.

**The count is tied to a representation.** It says nothing by itself about the cost of every way of answering a quantum-modeling question. Using 8 bytes per amplitude halves the payload to 8 PiB and still fails this budget; it also changes numerical precision. Discarding small amplitudes requires an error argument for the requested output. Calling the representation sparse supplies no bound on the number of retained entries or on growth during its operations.

**Construct a restricted alternative.** Suppose the admitted states are products of 50 normalized single-qubit pure states, every operation is a single-qubit unitary gate, and the requested output is the probability that a named qubit is read as 1. Store the 50 pairs `(alpha_i, beta_i)` instead of the full array. The corresponding joint amplitude for bit string `s` is the product, over positions `i`, of `alpha_i` when `s_i=0` and `beta_i` when `s_i=1`.

Initialize each pair from its supplied single-qubit state. For a gate with unitary 2-by-2 matrix `U` on qubit `i`, replace just that pair by `U*(alpha_i,beta_i)`, retaining the old two values while computing both new ones. The tensor-product rule preserves the product form, and unitarity preserves the pair's normalization. For normalized pairs, return `|beta_i|^2`. The payload is now `50 × 2 × 16 = 1,600 bytes`, with additional algorithm and representation overhead to be counted separately.

Starting with all pairs `(1,0)`, apply the Hadamard operation `(a,b) -> ((a+b)/sqrt(2),(a-b)/sqrt(2))` to the first pair. It becomes `(1/sqrt(2),1/sqrt(2))`, and the requested probability for the first qubit is `1/2`. The construction uses a fixed number of complex operations per gate and stores only the pairs. Its structural factorization is exact under the admitted model; stored numerical coefficients still require their precision account.

An entangling gate can invalidate that representation. The two-qubit state with nonzero amplitudes `1/sqrt(2)` at `00` and `11` and zeros at `01` and `10` cannot be one product: nonzero `alpha_0*alpha_1` and `beta_0*beta_1` would make all four factors nonzero, contradicting a zero cross term. The product procedure must therefore reject that extension or receive a richer representation and update algorithm. Even in the product class, requesting all `2^50` amplitudes explicitly restores an exponential output count.

**First result and next contribution.** The original dense proposal is ruled out. The factorized procedure answers the separately stated restricted question; it is not a replacement for an unspecified general circuit. To continue, recover the actual input-state and gate family, requested observable or samples, and tolerated error, then obtain and cost an applicable domain algorithm. The general method supplied the count and the construction question; quantum simulation supplies the representations and update/readout algorithms.

#### C.29.2:5.4 - Obtain different computations from the same circuit relations

**Model and questions.** An ideal resistor and capacitor are connected in series to a voltage source. Let `i` flow toward the capacitor's positive plate, `v_R` be the resistor's voltage drop in that direction, and `v_C` the capacitor voltage. Use `R = 10 ohm`, `C = 0.1 F` and these relations:

```text
v_s = v_R + v_C
v_R = R*i
i = C*dv_C/dt
```

The equalities do not assign a computational direction. One question supplies the source voltage and asks for current; another supplies a desired current and asks for the source voltage. Keep the component relations while changing which quantities are given and which must be obtained.

**Voltage given: construct the trajectory and its readouts.** Take constant `v_s = 12 V` and the initial condition `v_C(0) = 2 V`. Substitute the first two relations into the third:

`dv_C/dt = (v_s - v_C)/(R*C)`.

The reduced differential state is `v_C`. Retain `v_R = v_s - v_C` and `i = (v_s - v_C)/R` as readout expressions, so eliminating those variables from the state does not remove the requested outputs.

Here `tau = R*C = 1 s`. Put `z = v_s - v_C`; then `dz/dt = -z/tau` and `z(0) = 10 V`. Thus `z(t) = (10 V)*exp(-t/tau)`: differentiation gives `dz/dt = -z/tau`, and substitution at zero gives the prescribed initial value. Recover the original quantities as `v_C = 12 V - z`, `v_R = z` and `i = z/R`. At `t = tau*ln(2)`, the exponential is `1/2`, so the returned quantities are `v_C = 7 V`, `v_R = 5 V` and `i = 0.5 A`.

**Current given: choose another computational dependency.** Now require `i(t) = 0.5 A` and keep `v_C(0) = 2 V`; the source voltage is to be found. The same relations give `dv_C/dt = i/C = 5 V/s`, hence `v_C(t) = 2 V + (5 V/s)*t`. Then `v_R = R*i = 5 V` and `v_s(t) = 7 V + (5 V/s)*t`. At `t = 0.1 s`, return `v_C = 2.5 V`, `v_R = 5 V` and the required `v_s = 7.5 V`.

Release the earlier condition `v_s = 12 V` when making `v_s` an unknown. Keeping it would contradict the new question already at `t=0`, where the relations require `v_s = 7 V`. This change chooses another computation from the model; whether a source can deliver the resulting waveform is a C.29.3 question.

**Structural reduction and numerical choice are separate.** The substitutions remove algebraic unknowns and retain their reconstruction formulas under `R,C > 0`. They do not select a time-stepping algorithm. The closed form is adequate for the constant-voltage question above. A numerical variant could instead take a forward Euler step:

`v_C_next = v_C + h*(v_s - v_C)/(R*C)`.

With `h = 0.1 s`, its first step gives `v_C_next = 3 V`, from which the readouts are `v_R = 9 V` and `i = 0.9 A`. The closed form gives `v_C(0.1 s) = 12 V - (10 V)*exp(-0.1) ≈ 2.95162582 V`; this step's voltage error is about `0.04837418 V`. Selecting a step rule and size therefore needs the requested accuracy. The exact elimination of `v_R` and `i` did not cause that time-discretization error.

**Consistent initialization is another problem.** In the voltage-given question, the prescribed `v_C(0)=2 V` and `v_s(0)=12 V` force `v_R(0)=10 V`, `i(0)=1 A` and `dv_C/dt(0)=10 V/s`. An initializer's guess `i(0)=0 A` may be replaced while finding these values. Making `i(0)=0 A` an additional required condition instead contradicts the relations. The capacitor's prescribed initial voltage represents an initial physical condition in this model. A starting guess guides numerical search; the resulting numerical approximation is assessed against the initial constraints and required accuracy.

For a larger differential-algebraic model, obtain the needed consistent-initialization, tearing or index-reduction Method from that discipline. Return the actual equations, givens, initial constraints and requested readouts with the unresolved question. A numerical initialization failure alone does not establish that the constraints are inconsistent; the contradiction in this small case follows from the displayed algebra.

#### C.29.2:5.5 - Construct a probability estimate with a specified error guarantee

**Question and available operation.** Estimate a fixed unknown probability p from independent binary observations X_1,...,X_n with the same probability p of 1. Require the procedure's probability of an error of at least 0.05 to be at most 0.05, for every p in [0,1]. The sampling operation and its independence are premises supplied to this construction; C.29.3 examines their realization.

**State and procedure.** Retain two integer counters: observations read j and ones observed s, initially zero. For each observation x, set s = s+x and j = j+1. After the selected n observations, return p_hat = s/n. The invariant is that s counts the ones in the first j observations. Thus the counters obtain the sample mean without retaining every observation.

**Choose n from the guarantee.** For a binary observation, E[X]=p and Var(X)=p*(1-p) ≤ 1/4. Independence gives E[p_hat]=p and Var(p_hat) ≤ 1/(4*n). On the event |p_hat-p| ≥ epsilon, the squared error is at least epsilon². Therefore

~~~text
epsilon² * P(|p_hat-p| ≥ epsilon)
    ≤ E[(p_hat-p)²]
    = Var(p_hat)
    ≤ 1/(4*n).

P(|p_hat-p| ≥ epsilon) ≤ 1/(4*n*epsilon²).
~~~

Taking n = 2,000 makes the bound 0.05 at epsilon = 0.05. The guarantee concerns repeated executions under the sampling model; it is not a posterior probability assigned to p after seeing one estimate. For instance, s=1,100 returns 0.55, while the guarantee still belongs to the stated procedure.

This construction consumes 2,000 observations and counter updates. Each counter needs 11 bits to represent values through 2,000; the output can be retained as the rational s/2,000. Include the cost of obtaining an observation when that cost matters. This conservative bound already supplies a finite construction; a sharper concentration argument can reduce the required observations when that saving is worth obtaining.

**Change the sampling premise.** If every read repeats one sampled bit B, then p_hat=B for every n. At p=0.5, its error is always 0.5, so the requested guarantee fails. More reads of that retained bit do not repair the construction. Obtain a sampling operation with the required independence, or recompute the error bound from the dependence actually supplied.

