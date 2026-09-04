---
chunk_kind: "child"
pattern_id: "C.25"
pattern_title: "Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
section_id: "C.25:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.25/C.25__012_sota-echoing.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "C.25 — Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
  - "C.25:11 — SoTA-Echoing"
line_start: 53852
line_end: 53866
dependencies:
  - "A.10"
  - "A.15"
  - "A.16.0"
  - "A.18"
  - "A.2.6"
  - "A.6.1"
  - "B.3"
  - "C.16"
  - "C.16.P"
  - "C.16.Q"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.2.2a"
  - "C.26.3"
  - "C.33"
  - "C.34"
  - "C.35"
  - "F.9"
  - "F.9.1"
keywords:
  - "admissible quality-family use"
  - "characteristic plus scope"
  - "endpoint classification"
  - "failure mode"
  - "ility"
  - "mechanism/status slots"
  - "proxy metric"
  - "quality bundle"
  - "quality family"
  - "viability envelope"
---

### C.25:11 - SoTA-Echoing

The comparison below selects lines by the quality-family problem they can solve, not by publication popularity or by the availability of a convenient form.

| Current problem-solving line | What it solves well | Remaining limit or effort cost | C.25 disposition |
| --- | --- | --- | --- |
| [ISO/IEC 25010:2023 product quality model](https://www.iso.org/standard/78176.html) | Provides a current reference model of nine product-quality characteristics and their subcharacteristics for specification, measurement, evaluation, and acceptance criteria. It prevents one undifferentiated word *quality* from doing all the work. | Its reference taxonomy does not identify one local claim episteme, its exact bearer, use-bounded scope, window, mechanism prerequisite, or evidence reliance. A domain may also need qualities outside its ICT-product boundary. | Adopt characteristic decomposition and explicit measures; do not import the taxonomy as a universal bundle schema or bearer identity. |
| [Google SRE Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/) and [Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/) | Couples an indicator and objective to an explicit time window, error budget, stakeholder decision, and actionable response; multiwindow and multi-burn-rate alerts expose the precision/recall and management trade-off. | It is a mature service-reliability line, not a general ontology of resilience, security, maintainability, or assurance. It assumes measurement and operational-policy work whose cost is justified only for the receiving use. | Adapt the explicit measure/window/action boundary and the rule that engineering effort should match the decision; do not make an SLO or error budget mandatory for every quality family. |
| [NIST SP 800-160 Vol. 2 Rev. 1, *Developing Cyber-Resilient Systems*](https://doi.org/10.6028/NIST.SP.800-160v2r1) | Treats cyber resilience through distinct goals, objectives, techniques, approaches, and design principles for anticipating, withstanding, recovering from, and adapting to adverse conditions. It keeps resilience from becoming one score. | The line is security-specific and intentionally broad; applying its life-cycle and risk constructs can be expensive. It does not provide one lightweight local claim identity or universal aggregation law. | Adopt the separation of scenario, measures, mechanisms, and outcomes when they are load-bearing; reject a universal resilience scalar and do not copy the full handbook into a Q-Bundle. |
| [OMG SACM 2.3](https://www.omg.org/spec/SACM/2.3) | Separates structured claims, argument links, artifact references, counter-evidence, and interchange packages, making an assurance case inspectable across tools. | A complete assurance case and its interchange structure can be much heavier than an ordinary quality claim. SACM does not decide which quality contributors make the claim true or whether one bundle guard is admissible. | Keep quality claim content distinct from evidence and assurance. Open `A.10` or `B.3` only on their own trigger instead of embedding an assurance case in C.25. |

**FPF-local synthesis.** C.25 combines only the non-dominated moves needed before a direct domain pattern takes over: one exact bearer; a single-Characteristic exit; otherwise a typed separation of load-bearing measures, scopes, windows, mechanisms, statuses, and evidence references; and a guard over only the conditions the claim actually states. The tuple and this conditional guard are FPF synthesis, not a claim that contemporary practice already shares one universal Q-Bundle.

**Defeating and reopen conditions.** Prefer a direct domain pattern when it already supplies a clearer composite-quality identity, aggregation law, and practitioner route. Reopen C.25 when a useful quality claim cannot be stated through the available typed contributors without inventing filler, when a non-conjunctive trade-off or dependency cannot be named under its direct pattern, when the record costs more than the receiving decision warrants, or when a proxy repeatedly becomes the decision object despite the source claims remaining load-bearing.

