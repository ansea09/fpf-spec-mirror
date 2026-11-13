---
chunk_kind: "child"
pattern_id: "G.13"
pattern_title: "External Interop Hooks for SoTA Discipline Packs (conceptual)"
section_id: "G.13:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/G.13/G.13__003_problem.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "G.13 — External Interop Hooks for SoTA Discipline Packs (conceptual)"
  - "G.13:2 — Problem"
line_start: 140959
line_end: 140968
dependencies:
  - "A.18"
  - "A.19"
  - "E.10"
  - "E.18"
  - "E.5.2"
  - "F.17"
  - "G.0"
  - "G.12"
  - "G.13"
  - "G.2"
  - "G.7"
  - "G.8"
  - "G.9"
  - "G.Core"
keywords:
  - "CHR-typed SoS features"
  - "ClaimMapperCard@Context"
  - "ExternalIndexCard@Context"
  - "InteropSurface@Context"
  - "RSCRTriggerKindId"
  - "UTS twins"
  - "claim mapper"
  - "edition pins"
  - "embedding spec"
  - "external index"
  - "interop"
  - "mapping policy"
  - "plane map"
  - "telemetry pin"
---

### G.13:2 - Problem

External sources publish **claim‑adjacent signals** (citations, concept graphs, “task/method” tags, replication links, dataset usage, disruption‑style indicators, benchmark metadata). These signals can support audit and the generation of new inputs, for example by helping to build a palette, explore a declared set result or discover a candidate bridge. The mapping can fail in the following ways:

* **CN/CG spec-ref leakage.** A receiver treats external numeric signals as lawful scores without showing how they are bound to the applicable CHR/CAL/CG definitions.
* **Implicit crossings.** An opaque transformation hides the actual correspondence, its receiving-use grounds or the bundle anchors required by a real flow crossing or gate.
* **Edition drift + refresh brittleness.** Snapshots change, schemas drift, indicator definitions get revised; without edition‑pinned interop surfaces and typed trigger causes, parity and dashboard stability degrade.
* **Evidence disconnect.** A derived feature without recoverable source and transformation grounds cannot be checked or repaired in the receiving use.
* **Format‑as‑norm.** A convenient serialisation (KG export, JSON schema, RO‑Crate, etc.) is taken as the specification, undermining notation independence.

