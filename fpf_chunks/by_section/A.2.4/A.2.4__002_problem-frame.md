---
chunk_kind: "child"
pattern_id: "A.2.4"
pattern_title: "Episteme Evidence-Use and Status-Use Relations"
section_id: "A.2.4:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.4/A.2.4__002_problem-frame.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "A.2.4 — Episteme Evidence-Use and Status-Use Relations"
  - "A.2.4:1 — Problem Frame"
line_start: 3397
line_end: 3418
dependencies:
  - "A.10"
  - "A.2"
  - "A.2.1"
  - "A.2.4"
  - "A.6.5"
  - "B.3"
  - "C.2.1"
  - "C.28"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.2"
  - "E.17.EFP"
  - "F.10"
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

### A.2.4:1 - Problem Frame

Use this pattern when a report, proof, dataset, measurement file, standard, requirement, dashboard cell, model card, publication face, generated explanation, or other `U.Episteme` is being used as evidence, source, status bearer, assurance input, or causal-use input for a claim.

Use it when the working question is:

* which episteme is being used;
* which claim, theory statement, status assertion, use, or causal-use question the episteme is being used for;
* which bounded context, claim scope, grounding holon, polarity, relevance window, assurance use, weight model, and provenance constraints are current;
* whether source wording such as "evidence role", "status role", "standard role", or "the report plays a role" hides an evidence-use, status-use, source-use, publication-use, assurance-use, gate-use, or causal-use relation;
* whether the evidence-use or status-use relation is sufficiently specified for the intended reliance, or only enough for orientation, source-finding, a reversible probe, or a narrowed use.

**Primary EntityOfConcern.** The `EntityOfConcern` is the evidence-use relation or status-use relation around an episteme. It is not `U.Role`, not `U.RoleAssignment`, and not a system performing work.

**First useful move.** Name the episteme, the bounded context, the claim or status being addressed, and the direct governing pattern that owns the use: usually `A.10`, `B.3`, `C.2.1`, `C.28`, `F.10`, `G.6`, `E.17`, `E.10.D2`, or a direct gate, source, requirement, definition, explanation, or publication-use pattern.

**What goes wrong if missed.** A document starts acting like an agent, a dataset is treated as if it held a work-facing role, a dashboard status becomes permission, a proof becomes global evidence without a theory fence, or a simulation-only counterfactual output is relabelled as realized causal evidence.

**What this buys.** The project can use epistemes as evidence, status bearers, sources, standards, requirements, definitions, explanations, publications, or assurance inputs without creating a second role ontology for epistemes and without losing claim scope, polarity, freshness, provenance, or assurance-use distinctions.

**Not this pattern when.** If the current claim is a system or acting holon holding a work-facing role, use `A.2` and `A.2.1`. If the current claim is performed work, use `A.15.1`. If the current claim is the full evidence-provenance graph relation, use `A.10`. If the current claim is assurance, use `B.3`. If the current claim is causal use, use `C.28`. If the current claim is a status family or status mapping, use `F.10`. If the current claim is publication-use or source-use, use `E.17` and `E.10.D2` as needed.

