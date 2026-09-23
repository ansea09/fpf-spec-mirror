---
chunk_kind: "child"
pattern_id: "A.6.P.RI"
pattern_title: "Recover Agent-Relative References for Action"
section_id: "A.6.P.RI:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.P.RI/A.6.P.RI__006_archetypal-grounding.md"
commit_sha: "4ddaf71557d4159e988cc61d2bd3088bfc1d2803"
heading_path:
  - "A.6.P.RI — Recover Agent-Relative References for Action"
  - "A.6.P.RI:5 — Archetypal Grounding"
line_start: 18042
line_end: 18077
dependencies:
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "B.5.EA"
  - "C.2.1"
keywords:
---

### A.6.P.RI:5 - Archetypal Grounding

The following constructed cases show different things a transfer can preserve.

#### A.6.P.RI:5.1 - Preserve a displacement across orientations

A faces north and asks B to displace a crate one metre in the direction A calls left. B faces south. The assignment is to preserve the external displacement, and both headings are known.

The source direction is west. For B, facing south, west is right. The receiving instruction is therefore to move the crate one metre to B's right. If B turns east before acting, west becomes backward. Copying “left” would now send the crate north.

Change the assignment to “move the crate one metre toward your own left”. With B facing east, the correct displacement is now north. The known headings did not settle the instruction; the preservation condition did.

If B's heading is unavailable, “one metre west” can still be a complete instruction for a performer who can act in that frame. Otherwise the body-relative instruction remains unresolved. The method asks for the information needed by the chosen means, not for every possible position description.

A mobile robot receiving the same external displacement needs a usable relation between the shared frame and its action representation. Obtaining that relation and the capability to perform the movement is a separate technical task. The example does not prescribe its learning or control architecture.

#### A.6.P.RI:5.2 - Preserve the speaker when relaying a request

Dana writes to an assistant: “Put the comparison in my project folder.” The assistant sends the request to another worker. Replacing “my” with the new worker's own project folder would change the destination.

The receiving purpose preserves Dana's destination. The assistant identifies Dana's project folder through the available project information and relays: “Put the comparison in Dana's project folder,” with a usable reference to it. The worker uses its own authorized means of access; Dana's request does not grant access that the worker lacks.

If the next assignment is instead “each worker puts a copy in its own project folder”, the rule is applied relative to each worker. That is a changed distribution task, not another wording of the original destination.

Where the workspace contains several Dana projects and the intended one cannot be recovered, the useful result is a question selecting the project. Producing another fluent paraphrase leaves the same action unresolved.

#### A.6.P.RI:5.3 - Relate a dancer's report to an observer's account

A dancer facing the teacher says, “I feel a pull along my left side when I turn in this figure.” The teacher sees movement on the teacher's right. Both accounts can concern the dancer's left side even though the spatial words differ.

The first receiving task is to understand the report. Recover the dancer as the experiencing participant, the dancer's orientation and the turn being described. The teacher can say, “You report a pull along your left side during that turn,” and ask the dancer to correct the expression if needed.

A second task is to decide how to change the movement. The report and external observation can inform that inquiry, but do not themselves identify the tissue, force, cause or suitable exercise. The relevant bodily practice must supply the further operation.

In this figure, maintaining balance during the turn contributes to performing the figure; regulating bodily effort helps enact that balance, while the steps keep their required rhythm. Changing whose account is used can make another question accessible; it does not by itself identify which constituent needs development. B.1.5.EW supplies that vertical inquiry, and B.5.EA helps articulate a distinction the dancer cannot yet express.

