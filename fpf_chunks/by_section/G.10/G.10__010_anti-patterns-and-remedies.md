---
chunk_kind: "child"
pattern_id: "G.10"
pattern_title: "SoTA Pack Shipping"
section_id: "G.10:8.1"
section_title: "Anti‑patterns and remedies"
source_path: "FPF-Spec.md"
output_path: "by_section/G.10/G.10__010_anti-patterns-and-remedies.md"
commit_sha: "ea8c54542bf017f36659167f36e816fad4de88cb"
heading_path:
  - "G.10 — SoTA Pack Shipping"
  - "G.10:8.1 — Anti‑patterns and remedies"
line_start: 131063
line_end: 131073
dependencies:
  - "A.10"
  - "A.15.3"
  - "C.18"
  - "C.21"
  - "E.18"
  - "E.5.2"
  - "F.17-F.18"
  - "G.11"
  - "G.12"
  - "G.12-G.13"
  - "G.13"
  - "G.2"
  - "G.2-G.9"
  - "G.3"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.8"
  - "G.9"
  - "G.Core"
keywords:
  - "AuditPins"
  - "CrossingBundle"
  - "MOOManifest"
  - "PathId/PathSliceId"
  - "PortfolioRosterId"
  - "RSCR wiring"
  - "SoTA-Pack(Core)"
  - "UTS publication"
  - "edition pins"
  - "no semantic respecification"
  - "notation-independent pack"
  - "pack-boundary governing definition"
  - "parity pins"
  - "selector-ready publication surface"
  - "shipping"
  - "telemetry pins"
---

### G.10:8.1 - Anti‑patterns and remedies

* **AP‑1 Format‑as‑governing‑specification.** Remedy: keep Core surfaces conceptual (E.5.2); move serialisation to Annex/Interop; enforce `CC‑G10.1`.
* **AP‑2 Hidden edition drift.** Remedy: require `…Ref.edition` pins in AuditPins and treat edition changes as RSCR‑relevant via canonical trigger kinds.
* **AP‑3 “QD archive present” but missing definition pins.** Remedy: enforce `CC‑G10.2` and the `G.10:Ext.QDArchiveShippingPins` pin declarations.
* **AP‑4 Telemetry silently becomes dominance.** Remedy: keep telemetry report‑only unless an explicit CAL policy promotes it; require policy‑id recorded (ties to `CC‑G10.3` and MOO discipline).
* **AP-5 Missing required PathSlice key.** Remedy: enforce PathSlice‑keyed telemetry and path citations (`G.10‑5`, `G.10‑6`).
* **AP‑6 Cross-context reuse without its required grounds or anchors.** Remedy: cite the actual relation and the receiving-use and reliance grounds required by its governor; include calibration and policy pins when that account requires them. For an independently applicable `E.18` flow crossing or `A.21` gate, expose its required bundle or gate anchors and fail on missing or non-conformant ones (`CC‑G10.7`, `CC‑GCORE‑CROSS‑1`).
* **AP‑7 Interop ingestion rewrites semantics.** Remedy: ingest interop as cited notes only; semantics remain in `G.13` (`G.10‑7`, `G.10:Ext.InteropCitation`).
* **AP‑8 Derived-view collapse.** Remedy: ship `sourceSetFamily`, `derivedViewKind`, `basePaletteRef`, and the declared `Q` or reachability basis with enough explicitness that one derived tradition view cannot masquerade as the default palette meaning.

