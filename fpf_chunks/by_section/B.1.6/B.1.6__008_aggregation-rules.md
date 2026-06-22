---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Work-Resource Aggregation"
section_id: "B.1.6:5"
section_title: "Aggregation Rules"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__008_aggregation-rules.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "B.1.6 — Work-Resource Aggregation"
  - "B.1.6:5 — Aggregation Rules"
line_start: 32210
line_end: 32236
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "B.1"
  - "B.1.4"
  - "B.1.6"
  - "B.2"
  - "B.2-family"
  - "B.2.P"
  - "C.13"
  - "C.16"
  - "C.27"
  - "C.29"
  - "E.17"
keywords:
---

### B.1.6:5 - Aggregation Rules

**Resource vectors stay typed.** Add joules to joules, hours to hours, kilograms to kilograms, and bytes to bytes. A conversion or equivalence relation needs its governing measurement, model, or mathematical-lens owner.

**Partition additivity requires declared partitions.** Resource values may be added across disjoint boundary partitions only after the boundary and stock relation are named. Shared stock, shared meters, shared people, shared tools, or overlapping time windows require an overlap or deduplication policy.

**Time slicing requires temporal coverage.** A resource roll-up over phases uses non-overlapping phase refs and a time window. If a missing phase matters, the admissible use is narrowed or `B.1.4`/`C.27` supplies the temporal owner.

**Plan and result stay separate.** A method description or work plan may provide expected yield, expected duration, or expected resource use. Measured work-resource aggregation uses dated work occurrence evidence. Do not overwrite one with the other.

**B.1 invariant carry-through.** `B.1.6` keeps B.1 invariants only for recovered work-resource ledgers. A singleton zero-resource occurrence is idempotent for the selected resource-accounting basis. Addition is commutative only for independent partitions, non-overlapping slices, or explicitly deduplicated overlaps. Weakest-link claims must name the critical resource, availability, or threshold; monotonicity claims must name the resource characteristic being improved. Apparent "free" gains remain measurement, equivalence, or whole-reidentification questions until their direct owner is recovered.

**Proof-sketch obligations.** For idempotence, show the zero-resource or singleton ledger under the selected resource-accounting basis. For commutativity or locality, show disjoint boundary partitions, disjoint time slices, or the declared deduplication relation. For weakest-link, name the critical resource and availability condition. For monotonicity, name the exact resource characteristic that cannot get worse under the selected improvement. These are user-facing obligations for the aggregation claim, not a separate proof package.

#### B.1.6:5.1 - Compact Obligation Rows

| Obligation | What must be named | Why it matters |
| --- | --- | --- |
| Typed resource vector | Resource-accounting basis, unit, measure, evidence refs, and source refs for each component. | Prevents hours, energy, material, cost, and data volume from becoming one undifferentiated total. |
| Disjoint partition | Boundary partition, stock relation, time window, and work occurrence refs. | Allows addition only where the partitions are actually disjoint for the selected resource-accounting basis. |
| Shared-stock handling | Shared meter, shared tool, shared person, shared data, shared inventory, or overlap policy. | Prevents double counting and false savings. |
| Critical resource cap | The capacity, availability, threshold, or bottleneck resource whose limit governs the claim. | Makes weakest-link and capacity claims inspectable. |
| Yield relation | Input resource refs, output result refs, loss refs, and measurement basis. | Keeps efficiency from being asserted without a result relation. |
| Embodied and dissipated split | Which resource remains embodied in the changed entity and which is dissipated, consumed, wasted, or externalized. | Keeps conservation, loss, and waste claims from being collapsed into one spent-resource label. |
| Loss monotonicity | The exact loss, waste, delay, cost, risk, or degradation characteristic being bounded or reduced. | Allows monotone improvement claims only for a named characteristic. |
| Plan-result separation | Expected resource use from method description or work plan versus measured resource use from dated work evidence. | Prevents a plan or algorithm from proving performed-work resource use. |

