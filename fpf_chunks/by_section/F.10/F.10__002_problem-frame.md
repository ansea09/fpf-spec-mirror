---
chunk_kind: "child"
pattern_id: "F.10"
pattern_title: "Status Families Mapping: Evidence, Standard, and Requirement Status"
section_id: "F.10:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/F.10/F.10__002_problem-frame.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "F.10 — Status Families Mapping: Evidence, Standard, and Requirement Status"
  - "F.10:1 — Problem frame"
line_start: 93810
line_end: 93825
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.4"
  - "A.6.1"
  - "B.3"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.17"
  - "E.24.PUB"
  - "F.17"
  - "F.18"
  - "F.9"
  - "G.11"
  - "G.6"
keywords:
  - "applicability windows"
  - "evidence"
  - "polarity"
  - "requirement"
  - "standard"
  - "status"
---

### F.10:1 - Problem frame

**Use this when.** Use F.10 when a receiving use depends on a word such as *observed*, *measured*, *validated*, *approved*, *deprecated*, *satisfied*, *violated*, *waived*, *pending*, *current*, or *ready*, and the exact status value, governed target, scope, window, source, rule, or use is still implicit.

Use it especially when evidence, standards, and requirements are being mixed: a dashboard says a service is ready, a standard says a method is approved, a measurement is cited as requirement satisfaction, a model card says a model is validated, or a requirement register says a clause is waived.

**Primary EntityOfConcern.** The live object is one exact status-use relation around an already governed bearer or target, one local status value, one ClaimScope/use scope, one validity window, and one intended receiving use. F.10 does not define or create the target and does not turn a display, source, list membership, approval act, evaluation rule, result, or evidence item into the status-use relation.

**First useful move.** Recover the exact target and its direct domain result first. Then name the status-value SchemeSenseCell and family under the effective ReferenceScheme, status scope/window, exact source and provenance/currentness constraints, intended use, and stronger use not carried. If a rule must be applied, name the dated evaluation work, rule application, and result separately.

**What goes wrong if missed.** One compact word does the work of domain result, evidence standing, standard approval, requirement satisfaction, gate passage, release readiness, permission, and assurance at once. A dashboard list or traffic-light cell is treated as actual status use. An F.9 Bridge or family edge is treated as the explanation or evaluation rule. Design approval becomes runtime satisfaction.

**What this buys.** Status words remain local, typed, comparable, and usable without hiding the target or the work that justified the status. Evidence status says only what evidential standing is being asserted for a claim; standard status says only what a named governing source sanctions; requirement status says only what is being asserted about an exact clause after its direct evaluation. Cross-local vocabulary and cross-modality interpretation remain explicit and loss-aware.

**Not this pattern when.** Use the subject's direct pattern for its target and domain result; `A.2.4` for first evidence/status-use classification; `A.10`/`G.6` for source recovery, provenance, and bounded reliance; `G.11` for currentness; `B.3` for assurance; `C.28` for causal use; `A.21` for a gate; the direct permission, commitment, requirement, standard, acceptance, release, or decision pattern for those results; `E.17`/`E.24.PUB` for publication; and `A.15.1`/`A.6.1` for performed evaluation work and actual bindings.

