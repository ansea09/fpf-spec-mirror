---
chunk_kind: "child"
pattern_id: "B.2.2"
pattern_title: "Test the Proposed New Whole as a System"
section_id: "B.2.2:5"
section_title: "Archetypal Grounding (Worked Cases)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.2/B.2.2__007_archetypal-grounding-worked-cases.md"
commit_sha: "9d38fbfe4ce5b72d8fe05e839cbca0025a5b31cf"
heading_path:
  - "B.2.2 — Test the Proposed New Whole as a System"
  - "B.2.2:5 — Archetypal Grounding (Worked Cases)"
line_start: 46046
line_end: 46074
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2.1"
  - "A.2.2"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "B.1.2"
  - "B.2"
  - "B.2.4"
  - "B.2.5"
  - "B.3"
  - "B.3.5"
  - "C.13"
  - "C.16"
  - "C.27"
  - "C.30"
  - "C.30.ASV"
  - "C.30.TFS-REL"
  - "E.24.UK"
keywords:
---

### B.2.2:5 - Archetypal Grounding (Worked Cases)

#### B.2.2:5.1 - Search-And-Rescue Swarm

In this constructed case, B.2 has compared an established drone-system whole with the proposed coordinated search arrangement. Its supported result is that the prior whole cannot meet the search use while retaining its identity, and it names the proposed search-and-rescue swarm as the candidate new whole. The project retains individual-drone navigation and maintenance records. Test the candidate below; its mission objective, coordination relation, external command relation, capability envelope and swarm-level risks retain their own grounds.

- **Candidate new whole:** the search-and-rescue swarm named by B.2.
- **A.1 basis:** drone constituents, obtaining formation and coverage-coordination relations, the governed swarm assembly, the swarm reidentification rule, and the whole-level area-search characteristic; its boundary, command and mission interfaces, operating characteristics, and identity-preservation conditions also fit the applicable larger rescue-system construction rule.
- **System criterion:** the swarm has acting eligibility. This case also has its command-and-operating-area delimitation, mission objective, coordination relations, and external commitments.
- **Assurance:** swarm-level tests support claims about the candidate; individual drone certificates remain component evidence. Their contribution to a swarm-level claim depends on that claim and the evidence's applicability.

Choose the assurance claim about the swarm. If it requires every current member to hold a specified certificate, a complete membership list and a valid certificate for each member can settle it. If it requires the swarm to cover the search area, establish how the members’ paths together cover that area under the mission conditions. The same set of certified drones can fly overlapping paths that leave part of the area unsearched.

#### B.2.2:5.2 - Cloud Platform

Consider independent services proposed as one platform with a shared control plane, system-level SLO, deployment and rollback coordination, platform-level evidence, and external commitments. Establish those case facts under their patterns and test the proposed whole under :4.1.

If a better dashboard or an additional service is sufficiently explained as a change of the existing whole under its identity rule, use the relevant architecture-description, publication, measurement, or component pattern.

Use B.2.2 when B.2 identifies the operating platform as the candidate new whole to be tested under A.1 and the `U.System` criterion. Claim a system result only after those tests pass; retain a failed or unresolved evaluation under :4.1.

#### B.2.2:5.3 - Production Cell

A proposed production cell has a machine, robot, fixture, workpiece carrier, and inspection station as candidate constituents. Apply :4.1 to recognize the whole. For the operating-cell case, separately establish its delimitation, objective, coordination relations, transformation structure, Work occurrences, and capability envelope, with evidence for those claims.

Suppose the order asks for inspected workpieces by closing time. An available outside station with an assured handoff and enough time for inspection and delivery can supply a viable route. This can finish a request to choose a route. An order for inspected workpieces is fulfilled when the agreed inspection and delivery have taken place by closing time. If the order also requires a cell that retains inspection while the outside station is unavailable, work back from that use to the provision for inspection under those conditions. An installed station is one possibility. Determine its interfaces and the assembly relations that would make it part of this cell. A plan for the installation gives a conditional design result. A claim that this cell did the inspection requires grounds for what happened on the order.

A fixture being manufactured as a workpiece is not part of the machine merely because the machine changes it. The production cell claim needs a result system; the manufacturing relation remains transformation and work.

