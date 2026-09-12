---
chunk_kind: "child"
pattern_id: "B.5.RC"
pattern_title: "Recover a Construction from Its Description"
section_id: "B.5.RC:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.RC/B.5.RC__006_archetypal-grounding.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "B.5.RC — Recover a Construction from Its Description"
  - "B.5.RC:5 — Archetypal Grounding"
line_start: 41904
line_end: 41931
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

The recovered dependency is reusable for another positive side length. The value of the coordinates changes, while the two equal-radius circles and the common-point construction retain their roles. If A and B coincide, the initial requirement of a nondegenerate triangle fails; that case needs distinct endpoints before this construction can begin.

The Euclidean account supplies the circle and segment operations and their justification.

#### B.5.RC:5.2 - Recovering a display-stand assembly design

A specification asks for a portable display. It supplies a base, an upright and a panel, together with these rules: the upright can be joined to the base when their fittings match; the panel can be attached to the mounted upright when their fittings match.

Working backward from an assembled display yields a mounted upright and a compatible panel. Recovering the mounted upright yields the base, upright and their fitting condition. Working forward gives the assembly order: join base and upright, then attach the panel.

Inspection of the supplied parts reveals that the panel fitting differs from the upright fitting. The method has localized the obstruction. Available continuations include obtaining a compatible panel, developing an adapter with usable connection rules, or choosing another assembly design. “Assemble the display” alone does not select among them.

Suppose a compatible panel is supplied. The recovered design now connects the three components in the required order. Portability is still assessed against the actual carrying requirement, and stability against the loading and support conditions. Those engineering questions can change the design, but they are distinct from the recovered answer about how its parts connect.

The first useful result is the assembly design or the fitting mismatch that prevents it. Physically assembling and testing the stand are subsequent work selected by the intended use.

