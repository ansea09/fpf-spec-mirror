---
chunk_kind: "child"
pattern_id: "A.3.3.CC"
pattern_title: "Construct a Configuration Description under Constraints"
section_id: "A.3.3.CC:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3.CC/A.3.3.CC__012_sota-echoing.md"
commit_sha: "368bb772285d22b29eaaf20180500f49f1a2c9d7"
heading_path:
  - "A.3.3.CC — Construct a Configuration Description under Constraints"
  - "A.3.3.CC:11 — SoTA-Echoing"
line_start: 9795
line_end: 9806
dependencies:
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.3.3"
  - "A.6.3.RT"
  - "B.5.FM"
  - "B.5.MPC"
  - "C.29.1"
  - "C.29.2"
keywords:
---

### A.3.3.CC:11 - SoTA-Echoing

**How should constraints determine the representation?** Tong's [Classical Dynamics, section 2.3](https://www.damtp.cam.ac.uk/user/tong/dynamics/dynhtml/S2.html) develops generalized coordinates and the alternative of retaining constraints through multipliers. At comparable effort for the linkage, reduced coordinates make positions easy to reconstruct; the implicit relation keeps the connection available for a force calculation. Sections :4.2-:4.3 adopt this choice by the receiving question. Its mechanics supplies the physical interpretation of those constraints, not a law for every modeled subject.

Lynch and Park's [Modern Robotics, section 2.3.2](https://modernrobotics.northwestern.edu/nu-gm-book-resource/2-3-2-configuration-space-representation/) compares explicit and implicit configuration representations, including singular coordinate descriptions of a sphere. Section :4.3 adopts the coverage and representation question instead of equating fewer coordinates with a better account. Their [section 2.4](https://modernrobotics.northwestern.edu/nu-gm-book-resource/2-4-configuration-and-velocity-constraints/) distinguishes holonomic configuration constraints from nonholonomic velocity restrictions. Section :5.4 carries that distinction into a small motion question. These are durable construction Methods; the particular robot geometry and kinematic assumptions must still be supplied for a new robot.

**How does physical extent enter a computational configuration?** LaValle's [Planning Algorithms, chapter 4, introduction and sections 4.2-4.3](https://lavalle.pl/planning/ch4.pdf), constructs robot configurations, transformations and collision sets. Compared with checking a reference point alone, testing the transformed body's intersection with obstacles preserves the extent that the fitting question needs. Sections :4.1-:4.2 and :5.3 adopt that connection and the need to state contact conditions. The one-dimensional containment calculation is an authored reduced case. Path planning and collision algorithms retain their own assumptions and costs.

**When should a finite constraint set be solved by enumeration?** Poole and Mackworth's [Artificial Intelligence: Foundations of Computational Agents, third edition, section 4.1](https://artint.info/3e/html/ArtInt3e.Ch4.S1.html) makes variables, value domains, assignments and constraints explicit. Their [section 4.2](https://artint.info/3e/html/ArtInt3e.Ch4.S2.html) compares complete-assignment testing with search that rejects a partial assignment once a relevant constraint fails. Sections :4.2-:4.4 adopt those operational forms. For the two-buffer case, nine combinations make full enumeration inexpensive; a large product calls for a solving Method that exploits its constraints. Early rejection saves search without changing the satisfying set; it does not make arbitrary constraint problems cheap.

Together these sources supply complementary current answers to the construction question, with older sources serving as substantive methods rather than as claims of novelty. Reconsider the representation when the needed operation, configuration coverage, contact condition, participant distinctions or computational budget changes. A faster solver cannot recover a physical distinction omitted from its input.

