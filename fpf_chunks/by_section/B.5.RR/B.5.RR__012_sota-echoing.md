---
chunk_kind: "child"
pattern_id: "B.5.RR"
pattern_title: "Revise Reasoning After a Premise or Question Changes"
section_id: "B.5.RR:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.RR/B.5.RR__012_sota-echoing.md"
commit_sha: "8581bcf6502498b53aaa9fd42ed925a1371c08d1"
heading_path:
  - "B.5.RR — Revise Reasoning After a Premise or Question Changes"
  - "B.5.RR:11 — SoTA-Echoing"
line_start: 43779
line_end: 43790
dependencies:
  - "B.5"
  - "B.5.MPC.R"
  - "B.5.RA"
  - "B.5.RC"
  - "C.11.DUA"
keywords:
---

### B.5.RR:11 - SoTA-Echoing

**Which part of an argument needs revision?** Adapt the assumption-sensitive reasoning of de Kleer's [*A General Labeling Algorithm for Assumption-Based Truth Maintenance* (1988), §2](https://cdn.aaai.org/AAAI/1988/AAAI88-034.pdf). Compared with discarding every conclusion that used a removed premise, §4.3 retains sufficient alternatives and their shared conditions. This historical computational method supplies a precise model of conditional support. The present method uses that insight without requiring an ATMS or exhaustive assumption labels for an ordinary inquiry.

**When is incremental repair cheaper than starting again?** Adapt the comparison in Hu, Motik and Horrocks, [*Optimised Maintenance of Datalog Materialisations* (2018), §§1–4](https://www.cs.ox.ac.uk/people/boris.motik/pubs/hmh18optimised-maintenance.pdf): eagerly finding alternative derivations can avoid unnecessary deletion, but that search can itself be costly; recursive support needs more than simple counting. Section 4.3 therefore compares recovery and repair with a fresh answer. These are results for Datalog maintenance; selecting subject premises and interpreting empirical change require further reasoning.

**What should repair preserve for its receiver?** Adapt Klowden and Tao's [*Mathematical methods and human thought in the age of AI* (2026), §§4.4–4.6](https://arxiv.org/html/2603.26524v1). An inspectable proof result can serve one use, while changing its assumptions or applying its idea needs recoverable reasoning. Sections 4.1–4.5 retain that receiving question. The trade-off is explanation and recovery effort when another use actually needs them; full exposition is unnecessary for an already adequate application.

**What does current automated proof repair contribute?** [Wang et al., *Learning to Repair Lean Proofs from Compiler Feedback* (2026), §§3–5](https://arxiv.org/html/2602.02990v1), studies repair from generated failures and compiler feedback. Adapt its use of a localized failing transition when such feedback is available. Its single-shot formal-repair result answers a narrower question than choosing changed premises or interpreting an application. Section 4.4 preserves those questions instead of using compiler success as their answer.

Reopen these choices when better dependency recovery, subject inference or repair support changes the attainable result or the cost of obtaining it.

