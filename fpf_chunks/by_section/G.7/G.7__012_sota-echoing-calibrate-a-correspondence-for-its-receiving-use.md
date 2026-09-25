---
chunk_kind: "child"
pattern_id: "G.7"
pattern_title: "Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)"
section_id: "G.7:11"
section_title: "SoTA-Echoing — calibrate a correspondence for its receiving use"
source_path: "FPF-Spec.md"
output_path: "by_section/G.7/G.7__012_sota-echoing-calibrate-a-correspondence-for-its-receiving-use.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "G.7 — Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)"
  - "G.7:11 — SoTA-Echoing — calibrate a correspondence for its receiving use"
line_start: 114494
line_end: 114505
dependencies:
  - "A.21"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.21"
  - "C.23"
  - "C.3.3"
  - "E.10"
  - "E.18"
  - "F.17"
  - "F.3"
  - "F.7"
  - "F.9"
  - "G.10"
  - "G.11"
  - "G.12"
  - "G.2"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.9"
  - "G.Core"
keywords:
  - "BridgeCalibrationTable (BCT)"
  - "BridgeCard"
  - "BridgeSentinel"
  - "Congruence Level (CL/CL^k/CL^plane)"
  - "GateCrossing"
  - "PathSliceId"
  - "RSCRTriggerKindId"
  - "ReferencePlane"
  - "RegressionSet"
  - "SentinelSet"
  - "UTS"
  - "bridge calibration"
  - "loss notes"
  - "waivers"
  - "Φ(CL)/Ψ(CL^k)/Φ_plane policy pins"
---

### G.7:11 - SoTA-Echoing — calibrate a correspondence for its receiving use

**Practice question.** When a correspondence has a favourable calibration, what must an engineer check before reusing it for a different task? The selected best-known line for this question keeps the exact relation, its justification and source versions recoverable, then tests the receiving task's required distinctions. The serious alternative is to select an alignment by its reference-benchmark score and carry that favourable score into downstream use.

[SSSOM 1.0's mapping model](https://mapping-commons.github.io/sssom/1.0/spec-model/) supplies the first line's concrete separation of endpoints, relation predicate and justification. Its [mapping FAQ](https://mapping-commons.github.io/sssom/1.0/faq/) distinguishes relation precision from confidence and explains why source versions and justification matter. **Adopt** that separation for the BCT row's exact correspondence and calibration basis in §4.2. These sources address exchangeable ontology mappings; they do not establish an F.9 Bridge, a C.3.3 classification or permission for an FPF receiving use.

The [OAEI 2025 Conference evaluation](https://oaei.ontologymatching.org/2025/results/conference/eval.html) is the serious benchmark comparator: its precision/recall measures assess generated correspondences against stated reference alignments and populations. That is useful for choosing a matcher on that question. **Reject** carrying its aggregate success, or one CL value, as a substitute for a different task's premises. This is a limit of the inference, not a claim that OAEI promises such transfer.

**Adapt** the mapping-and-justification line in §4.2.1 and procedure steps 2/6: retain direction, scope and losses, and use a small regression pair whose required distinction changes. In §4.5, VehicleTransportOrder can retain passenger/transport order while losing battery information. The same calibrated relation can therefore support the stated transport comparison and fail the battery-health question. Keeping that distinction prevents a concrete erroneous use that a single favourable summary cannot detect.

At comparable effort, both alternatives start with the same relation row and existing calibration evidence. The selected line adds one named use condition and the smallest counterexample or regression pair that can change the answer. That is extra effort deliberately accepted for reuse across task boundaries; ordinary one-off correspondence handling remains with F.9 when a calibration kit adds no value. SSSOM and OAEI provide the compared technical approaches, not empirical validation of this kit. Reopen when a new receiver needs a distinction outside the row's stated preservation/loss basis, or when a cheaper rule can distinguish those same allowed and failed uses with equivalent support.

