---
chunk_kind: "child"
pattern_id: "C.39.RO"
pattern_title: "Turn a Construction into a Reusable Operation"
section_id: "C.39.RO:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.39.RO/C.39.RO__006_archetypal-grounding.md"
commit_sha: "0caf9a10acfc0ee17c32fc71f6173b542393f0a4"
heading_path:
  - "C.39.RO — Turn a Construction into a Reusable Operation"
  - "C.39.RO:5 — Archetypal Grounding"
line_start: 74930
line_end: 74978
dependencies:
  - "A.3.1"
  - "A.3.2"
  - "B.5.QD"
  - "B.5.RC"
  - "B.5.RR"
  - "B.5.TU"
  - "C.39"
  - "C.40"
keywords:
---

### C.39.RO:5 - Archetypal Grounding

#### C.39.RO:5.1 - Generalize a timing correction and obtain an impossibility result

A recording has picture-to-sound offsets of 40, 42 and 45 milliseconds at three matching markers. The available correction subtracts one constant from the sound times. Centering the extreme offsets gives 42.5 milliseconds and residuals -2.5, -0.5 and +2.5 milliseconds.

The receiving use needs that construction for any nonempty finite set of marker offsets, expressed in one common unit and reference. Let m be the smallest offset and M the largest. Construct:

- correction c = (m + M)/2;
- largest residual magnitude r = (M - m)/2.

Every marker offset lies between m and M, so subtracting c leaves each residual between -r and +r. Any constant correction leaves the two extreme residuals separated by M - m. At least one therefore has magnitude at least (M - m)/2. The proposed correction attains that lower bound: it minimizes the largest residual magnitude at these markers.

The reusable operation takes the marker offsets and returns c and r. For a stipulated tolerance T, r at most T supplies a feasible constant correction at the markers; r greater than T shows that no constant correction can meet that marker tolerance. One marker gives r = 0. An empty set supplies no extremes for this construction.

Now add a marker with offset 48 milliseconds. The operation gives c = 44 and r = 4. For a tolerance of 3 milliseconds, every constant correction fails. The two extreme offsets differ by 8 milliseconds, while two residuals each within 3 could differ by at most 6. This failure witness lets the practitioner stop searching among constant shifts and consider another time correspondence or a changed use.

The derivation concerns the supplied marker offsets. Applying a correction throughout a recording also needs the relation between markers and a qualified editing operation; C.39:5.2 retains that receiving question. Unknown drift between markers remains unresolved by this finite calculation.

#### C.39.RO:5.2 - Turn a partition construction into an allocation operation

A workshop has activities A, B, C and D and two sessions. Its stated constraints are pairwise incompatibilities: AB, BC and CD cannot share a session. Activities have no other scheduling or capacity constraints in this constructed case.

B.5 supplies a construction that returns either a two-colouring of a finite undirected graph or an odd-cycle witness. To make it usable for workshop allocation, construct the connection:

1. Make one vertex for each activity and one undirected edge for each incompatibility.
2. Apply the two-colouring operation.
3. Interpret the two colour classes as the sessions. If an odd cycle is returned, read its edges as the incompatible pairs preventing a two-session allocation.

For the supplied path, the operation returns sessions {A,C} and {B,D}. Every incompatibility has endpoints in different sessions.

Generalize from these four activities to any finite set with the same form of pairwise constraint. The encoding preserves exactly the stated prohibition on sharing a session. A two-colouring therefore yields an allocation satisfying every such prohibition. An odd cycle cannot alternate between two sessions all the way around, so it gives a failure witness.

Add incompatibility AC. The triangle A-B-C-A is now an odd-cycle witness. Changing only the session labels cannot repair it. The receiving choice concerns another session, a changed incompatibility or a different activity arrangement.

The reusable contribution is the composition of encoding, the available graph operation and interpretation. If session capacities or precedence constraints are introduced, this operation supplies only the pairwise-compatibility part of the allocation. Those additional constraints need their own construction.

#### C.39.RO:5.3 - Retain a physical condition when reusing a dispensing operation

A dispenser supplied 50 millilitres during a 2.5-second open interval. A proposed reusable operation would dispense a requested volume V by opening for V/20 seconds.

A subject model can justify that operation under a constant flow of 20 millilitres per second over the chosen interval, with the opening and closing effects already accounted for. Under that model, a request for 80 millilitres gives 4 seconds.

Suppose the receiving setup instead has a stated constant flow of 10 millilitres per second. Keeping the old four-second action would supply 40 millilitres. Exposing flow q as an input repairs the construction to duration V/q, for positive q under the stated constant-flow conditions; 80 millilitres then takes 8 seconds.

When flow changes during discharge, V/q with an unqualified constant no longer supplies the volume-duration relation. C.16.MR can construct the measurement relation, and A.3.3.TR can supply the changing-state account. The useful outcome here may be the identified missing relation and continued use of the earlier operation where its original conditions hold.

The numerical cases instantiate supplied models. The single 50-millilitre observation itself supports that observed outcome; a repeatability claim for the real apparatus needs its corresponding physical basis.

