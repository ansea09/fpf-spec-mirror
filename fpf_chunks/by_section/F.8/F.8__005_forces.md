---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__005_forces.md"
commit_sha: "44dd88188a07646ef23aca32627a3f670525853f"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:3 — Forces"
line_start: 85860
line_end: 85870
dependencies:
  - "A.11"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.7"
  - "A.8"
  - "C.3"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.24.UK"
  - "E.9"
  - "F.1"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.9"
keywords:
  - "decision lattice"
  - "minting new U-kinds"
  - "parsimony"
  - "reuse"
  - "type explosion"
---

### F.8:3 - Forces

| Force | Tension |
| --- | --- |
| Parsimony vs coverage | Avoid new durable names while still giving teams enough vocabulary for real recurring work. |
| Local sense vs cross-context reuse | A name can be obvious inside one bounded context and unsafe across contexts. |
| Human readability vs ontology | Short names help use; they also hide kind, scope, and relation if admitted too early. |
| Source familiarity vs FPF neutrality | A familiar source word may be useful as an alias while still being a bad selected FPF name. |
| Naming speed vs downstream cost | Quick minting is cheap now and expensive when every subsequent pattern must repair it. |
| Open-world use vs false completeness | A missing durable name may mean "not current", not "new U-kind required". |

