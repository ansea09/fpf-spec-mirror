---
chunk_kind: "child"
pattern_id: "B.5.RC"
pattern_title: "Recover a Construction from Its Description"
section_id: "B.5.RC:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.RC/B.5.RC__006_archetypal-grounding.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "B.5.RC — Recover a Construction from Its Description"
  - "B.5.RC:5 — Archetypal Grounding"
line_start: 50049
line_end: 50072
dependencies:
  - "A.6.3.RT"
  - "B.5"
  - "B.5.RA"
  - "C.29.1"
  - "C.29.2"
  - "C.39"
keywords:
---

### B.5.RC:5 - Archetypal Grounding

#### B.5.RC:5.1 - Recovering an equilateral-triangle construction

A reader has two distinct points A and B in the Euclidean plane and needs an equilateral triangle on side AB. The description says to draw two circles, each centred at an endpoint and passing through the other endpoint, and use an intersection as the third vertex.

The reader recovers three operations: draw a circle with the given centre and radius; select a common point of the two circles; join two given points by a segment. The third vertex requires both circles. The final triangle requires that vertex together with A and B. The two circles share the segment length AB as radius.

For a small case, place A at (0,0) and B at (2,0). The circles have equations x²+y²=4 and (x−2)²+y²=4. Subtracting gives x=1, and substitution gives y²=3. Thus the two common points are (1,√3) and (1,−√3). Selecting C=(1,√3) supplies the vertex above AB. Joining A to C and B to C completes the construction.

The property follows from how C was obtained: AC and BC are radii of circles of radius AB, so AC=BC=AB. The coordinate calculation also supplies the intersection in the Euclidean-plane account used for this case. A description formulated under a different set of construction rules must obtain that intersection under those rules.

To see why the same two-circle construction works for any two distinct endpoints in the Euclidean plane, use their midpoint as origin and AB as the horizontal axis. For a side of length d, the circle equations give a horizontal coordinate of zero and a vertical coordinate of either √3 d/2 or −√3 d/2. Both points are at distance d from each endpoint. Either point answers an order for one triangle. An order for every possible third vertex needs both, and the circle equations give only those two. Coincident endpoints cannot be the side of a nondegenerate triangle.

The Euclidean account supplies the circle and segment operations and their justification.

#### B.5.RC:5.2 - Recovering a display-stand assembly design

A team receives a drawing of a display stand and a base, upright and panel. The organizer wants a stand made to the drawing and asks whether its complete packed kit meets a 10 kg carrying limit. The drawing shows how to join the upright to the base and attach the panel to the mounted upright. Each operation requires matching fittings.

Work back from the mounted panel. It requires a compatible panel and an upright already connected to the base. Work forward on the supplied parts. The base and upright fit, but the supplied panel has a different fitting. That prevents assembly with this set. If the drawing specifies a particular panel, obtain the matching specified part. If the organizer permits alternatives, a compatible panel or an adapter may also be considered. An adapter adds a part and a joint. Check each changed connection and any load requirement it affects under the proposed arrangement.

Suppose the specified panel arrives and its fittings match. The team can now give the assembly sequence. For the carrying decision, identify everything that must travel together. Suppose the verified upper bounds for the base, upright, replacement panel, fittings and case sum to 9.5 kg and cover the complete kit. This establishes the mass requirement before packing, even if the exact packed mass is unknown. A request confined to how the parts connect can end with the sequence. Delivery of an assembled stand still requires someone to assemble and deliver it.

