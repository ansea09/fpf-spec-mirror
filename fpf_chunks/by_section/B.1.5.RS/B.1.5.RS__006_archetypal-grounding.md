---
chunk_kind: "child"
pattern_id: "B.1.5.RS"
pattern_title: "Replace a Constituent Method in Its Encompassing Uses"
section_id: "B.1.5.RS:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5.RS/B.1.5.RS__006_archetypal-grounding.md"
commit_sha: "31f4cb0b7f8000e0115098b50b44f80c8c36a671"
heading_path:
  - "B.1.5.RS — Replace a Constituent Method in Its Encompassing Uses"
  - "B.1.5.RS:5 — Archetypal Grounding"
line_start: 39540
line_end: 39565
dependencies:
  - "A.3.1"
  - "B.1.5"
  - "B.1.5.EW"
  - "B.1.5.RS"
  - "C.11.DUA"
  - "C.29"
keywords:
---

### B.1.5.RS:5 - Archetypal Grounding

#### B.1.5.RS:5.1 - Faster ordering in two encompassing uses

A team proposes replacing a stable sorting Method with a faster one that need not preserve the input order of equal keys.

One whole prepares a table showing how many records occur at each key. Internal order among equal keys does not affect those counts. Subject to the remaining input and performance conditions, the candidate can supply that contribution.

Another whole schedules requests by priority while retaining arrival order among requests of equal priority. Its method first orders records by arrival and then stably orders them by priority. Replacing the second sort with the candidate can reverse equal-priority requests. The earlier arrival ordering no longer survives the composition.

An allowed reversal of two equal-priority records with different arrival times exposes the incompatibility with the required guarantee. This is a counterexample to unrestricted replacement, not a prediction that this implementation reverses every such pair; repeated random benchmarks cannot restore the missing guarantee. Options include retaining the stable Method or sorting by an explicit compound key of priority and arrival. The compound-key candidate has changed the operation; compare its behavior and cost before using it. The same “sorted by priority” description concealed different requirements of the two wholes.

#### B.1.5.RS:5.2 - A bounded estimate and a threshold decision

A constituent estimates a quantity with absolute error at most 2. A receiving whole only needs to distinguish alternatives separated by more than 4; the bound can support their ordering when both estimates satisfy it.

Another whole must decide whether the quantity exceeds 100. An estimate of 99 is insufficient: the admitted interval is 97 to 101 and crosses the threshold. A more accurate estimate or another decision rule is needed for that case. At an estimate of 95, the same error bound puts the whole interval below 100 and can settle that particular decision.

The change from “estimate the quantity” to “support this decision” makes the scope of replacement explicit. The threshold is stipulated in this constructed example; the pattern does not supply a rule for choosing it.

#### B.1.5.RS:5.3 - A quicker observation during coordinated work

A group performs a movement sequence in response to a leader. A proposed observation Method uses occasional snapshots rather than continuous observation. It can suffice for an exercise in holding a static pose, but miss the cue that starts a coordinated transition.

Recover the timing actually needed by the encompassing sequence. If the snapshot interval exceeds the available response window, better interpretation of each snapshot cannot restore the missed cue. Keep more frequent observation, redesign the cue so it remains available, or change the coordinated sequence. Each proposal has a different burden and requires its own bounded comparison.

