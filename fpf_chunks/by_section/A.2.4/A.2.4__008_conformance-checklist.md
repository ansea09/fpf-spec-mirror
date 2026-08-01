---
chunk_kind: "child"
pattern_id: "A.2.4"
pattern_title: "Episteme Evidence-Use and Status-Use Relations"
section_id: "A.2.4:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.4/A.2.4__008_conformance-checklist.md"
commit_sha: "1eb56cd0cfd6dccad65143e03d28509373bd8dd5"
heading_path:
  - "A.2.4 — Episteme Evidence-Use and Status-Use Relations"
  - "A.2.4:7 — Conformance Checklist"
line_start: 4356
line_end: 4372
dependencies:
  - "A.10"
  - "A.2"
  - "A.2.1"
  - "A.6.5"
  - "B.3"
  - "C.2.1"
  - "C.28"
  - "E.10.D2"
  - "E.17"
  - "F.10"
  - "G.11"
  - "G.6"
  - "U.Role"
  - "U.RoleAssignment"
keywords:
  - "claim"
  - "episteme"
  - "evidence-use"
  - "provenance"
  - "source-use"
  - "status-use"
---

### A.2.4:7 - Conformance Checklist

| Check | Pass condition |
| --- | --- |
| `CC-A2.4-1` First-use object | One exact episteme and one target claim or governed status assertion are named. |
| `CC-A2.4-2` Admitted job | The statement is only an evidence-use or status-use classification; no `U.EvidenceRole`, episteme role-holder, or generic result kind is created. |
| `CC-A2.4-3` Scope | Bounded context, grounding holon, claim/status scope, polarity or value, and relevance/status window are explicit when they change the use. |
| `CC-A2.4-4` Work | Any source-producing, measurement, proof-checking, evaluation, transformation, or receiving work is dated `U.Work` with role assignment, method, and direct/A.6.1 bindings. |
| `CC-A2.4-5` Local result | The domain-local result points to its exact formal, measurement, causal, diagnostic, conformance, comparison, selection, acceptance, gate, permission, commitment, role, or decision governor. |
| `CC-A2.4-6` Result episteme | The C.2.1 episteme that states the local result remains distinct from that result, carrier, and work. |
| `CC-A2.4-7` Provenance/currentness | A.10/G.6 own source recovery and provenance; G.11 owns currentness when it affects use. |
| `CC-A2.4-8` Receiving use | The later dated work and exact premise/reference/decision-use/operation-argument relation are named; citation or availability does not establish actual use. |
| `CC-A2.4-9` Reliance/assurance | A.10 owns the bounded `RelianceDisposition`; B.3 opens only for an assurance claim or material reliance. |
| `CC-A2.4-10` Publication/display | Publication face, generated explanation, credential view, evidence profile, ledger edge, or dashboard cell does not establish status, result, work, gate, permission, or decision by presence. |
| `CC-A2.4-11` Causal boundary | C.28 owns causal-support classes and verdicts; source wording cannot promote simulation-only or observational evidence. |
| `CC-A2.4-12` Unsupported overread | The stronger claim not carried by this first-use classification and its reopen condition are stated. |

