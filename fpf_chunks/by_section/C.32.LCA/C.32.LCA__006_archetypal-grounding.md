---
chunk_kind: "child"
pattern_id: "C.32.LCA"
pattern_title: "Construct and Compare a Control Architecture"
section_id: "C.32.LCA:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.LCA/C.32.LCA__006_archetypal-grounding.md"
commit_sha: "fcd12ecc699c236021602dde85b5daf345e17c0b"
heading_path:
  - "C.32.LCA — Construct and Compare a Control Architecture"
  - "C.32.LCA:5 — Archetypal Grounding"
line_start: 76916
line_end: 76985
dependencies:
  - "A.3.3.PI"
  - "B.2.5"
  - "C.30.LCA"
  - "C.32"
  - "C.32.MWA.PP"
keywords:
---

### C.32.LCA:5 - Archetypal Grounding

#### C.32.LCA:5.1 - Retain a qualified loop and change how it receives targets

Consider a constructed discrete model, in normalized units,

\[
x_{k+1}=x_k+u_k,\qquad
u_k=\tfrac12(r_k-x_k).
\]

The actuator condition is \(|u_k|\leq0.06\), and the state must remain in \([-1,1]\). The state is available without delay or error in this first case. The controller computation fits each update. These are premises of the example, not claims about a physical device.

For a fixed target, the error contracts by one half per update. Nevertheless, if \(x_0=0.5\) and a planner immediately applies \(r_0=0.7\), the commanded input is \(0.1\), outside the actuator limit. The separate tracking result did not qualify that reference change.

One alternative is to redesign the controller and planner together. Another candidate retains the controller and limits the applied target from the desired goal \(g_k\in[-1,1]\):

\[
r_k=x_k+\operatorname{clip}(g_k-x_k,-0.12,0.12).
\]

Here \(\operatorname{clip}(a,l,h)=\min(\max(a,l),h)\). Substitution gives
\[
u_k=\tfrac12\operatorname{clip}(g_k-x_k,-0.12,0.12).
\]
Thus the actuator condition holds. The next state lies between \(x_k\) and \(g_k\), so an initial state in \([-1,1]\) stays there. This establishes the stated discrete constraints for this model. It does not establish intersample physical safety or a prescribed arrival time.

For the constant goal \(0.7\), the first three applied targets are \(0.62,0.68,0.7\); the corresponding inputs are \(0.06,0.06,0.04\), and the resulting states are \(0.56,0.62,0.66\). The limiter uses the loop's remaining action capability and returns a different progress forecast to the planner. It is a simple state-dependent governor construction, not a reason to add a new tracking layer.

Now request \(x_2\geq0.68\) from \(x_0=0.5\). Under the actuator bound, even an arbitrary control law can increase the state by at most \(2(0.06)=0.12\), giving \(x_2\leq0.62\). That requirement is impossible under the stated model and limit. The next choice concerns the deadline, attained position or available actuation; faster planning alone cannot obtain it. The participant authorized to change the demanded result must receive this bound.

Change the governor's observation condition instead. Suppose the governor receives only \(\hat x_k\), with a qualified current bound \(|x_k-\hat x_k|\leq0.02\), while the local tracker retains the original state-based feedback law. Limiting \(|r_k-\hat x_k|\) to \(0.12\) would allow \(|r_k-x_k|=0.14\) and input \(0.07\). A sufficient repair is to limit \(|r_k-\hat x_k|\leq0.10\) and require \(r_k\in[-1,1]\). Then \(|r_k-x_k|\leq0.12\), while the original convex update preserves the state interval. The set of targets satisfying both conditions must be nonempty; it is nonempty here when the state lies in the interval and the stated estimate bound holds.

The error bound must describe the current state. A bound for a stale measurement cannot be reused without accounting for intervening motion. If the tracker also loses its state measurement, its response equation and the convexity argument need reconsideration. Replacing it with a learned policy likewise reopens the calculation: the old response equation no longer supplies its proof.

This case shows the common method's contribution: recover the violated join, compare a governor with joint redesign, construct the admissible interface, calculate its consequence for the goal, and reopen the affected condition when observation or policy changes.

#### C.32.LCA:5.2 - Obtain a timely organizational decision

An exhibition panel must be installed by 16:00. Under a constructed operating arrangement, the following bounds are available:

| Contribution | Upper duration and its conditions |
| --- | --- |
| Detect a material content change | 20 minutes, including the wait for the scheduled check and the checking work |
| Deliver the complete change to the editor | 5 minutes through an available channel |
| Decide and send the approved file | 10 minutes, including waiting; the editor is available and the change is within the editor's authority |
| Print and install | 25 minutes; material, access and the allocated performer are available |

These contributions are serial for this arrangement. A change occurring by 15:00 can therefore be handled by 16:00. The latest sending time is 15:20; delivery is by 15:25, approval reaches the performer by 15:35, and installation finishes by 16:00. A later change can still succeed in a favorable case, but the hour-long bound no longer establishes the promise.

The useful state includes the current content, its approval status, the required materials and the availability of the people and means. “The file was sent” does not distinguish an approved file from an unapproved proposal, or a delivered message from one awaiting a decision.

Compare three changes to the arrangement.

1. **Shorten detection to five minutes.** If every other premise remains true, the bound becomes 45 minutes. This helps changes that occur by 15:15. It adds observation effort and does not repair a missing decision right.
2. **Authorize a defined local exception in advance.** If the current change needs an extra expenditure outside the editor's authority, the ten-minute decision premise fails. An effective limited authorization, available reserve and competent decision maker can restore a bounded path. A proposal to delegate does not do so until those conditions hold.
3. **Retain central authority and change the commitment or work.** Obtain an available central decision window, agree to freeze content earlier, use an already accepted substitute panel, or omit the affected panel where the receiving commitment permits it. Compare the changed result, delay and cost; these are not equivalent ways to meet the unchanged promise.

A forecast of a likely change can allow reversible preparation before approval. Establish which materials or capacity may be reserved, what another job loses, and how the reservation is released if the forecast changes. Printing an unapproved final panel is a different action with different consequences.

The control mechanism is now explicit: a dated observation changes a decision made within actual authority, that decision supplies a usable input to an available performer, and the resulting installation or failure returns to the responsible participants. One person may perform several contributions, provided their demands still fit. No three-level management hierarchy follows from the four duration bounds.

The timing implication is mathematical under its premises. The premises about people, authority, resources and duration need organizational support and observation; they are not supplied by the equation. In actual use, distinguish a committed service bound, an empirical estimate and a planning assumption.

#### C.32.LCA:5.3 - The smaller sufficient result

A machine already has an applicable controller, command range, state estimate, timing qualification and recovery procedure. The proposed change only redraws their representation for a maintenance team. Use C.30.LCA to make the obtaining relations and limits recoverable. Do not repeat architecture synthesis unless that reading exposes a consequential missing or changed relation.

Similarly, a team can retain an adequate allocation when a new report does not change any action, deadline or protected condition. More communication is not a required improvement.

