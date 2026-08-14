---
chunk_kind: "child"
pattern_id: "E.4.PFAD"
pattern_title: "Principle-Framework Architecture Decision"
section_id: "E.4.PFAD:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFAD/E.4.PFAD__012_sota-echoing.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "E.4.PFAD — Principle-Framework Architecture Decision"
  - "E.4.PFAD:11 — SoTA-Echoing"
line_start: 70602
line_end: 70611
dependencies:
  - "A.6.RCD"
  - "A.6.REL"
  - "C.32.ADR"
  - "C.32.PAD"
  - "E.17"
  - "E.19"
  - "E.21"
  - "E.23"
  - "E.24.PUB"
  - "E.4"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.4.PFR"
  - "E.9"
  - "F.18"
  - "G.11"
  - "G.2"
keywords:
---

### E.4.PFAD:11 - SoTA-Echoing

| Claim | Source and status | FPF use |
| --- | --- | --- |
| One bounded decision account carries alternatives, rationale, consequences, action, and reopen condition. | Current `E.9`; current FPF ground. | Use one ordinary E.9 DRR rather than a PFAD-specific result kind. |
| A relation needs actual participants, an obtaining condition, identity when later use needs the occurrence, and a receiving use. | Current `A.6.RCD`, `A.6.REL`, and `E.10:0.0a`; current FPF ground. | Refuse a PFAD relation; state material initial pattern relations directly. |
| Direct framework statements precede optional rows or manifests. | Accepted R3 decision and current `E.4.PFR`; current FPF ground. | Keep PFR representation optional under a named maintenance use. |
| Framework editions, publications, forms, and carriers remain distinct. | Current `E.24.PUB`; current FPF ground. | Treat ADR-like text, sites, and PDFs as projections or publications, not as the decision or framework. |
| Compact ADR sections help preserve decision memory but do not supply FPF ontology. | Nygard, `Documenting Architecture Decisions`, 2011; historical lineage source, `https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions`; MADR, maintained template practice, `https://adr.github.io/madr/`. | Reuse concise question, alternatives, rationale, consequences, and supersession cues only when an ADR-like projection is useful. |

