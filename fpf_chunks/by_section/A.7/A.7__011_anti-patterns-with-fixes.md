---
chunk_kind: "child"
pattern_id: "A.7"
pattern_title: "Strict Distinction (Clarity Lattice)"
section_id: "A.7:9"
section_title: "Anti‑patterns (with fixes)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7/A.7__011_anti-patterns-with-fixes.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "A.7 — Strict Distinction (Clarity Lattice)"
  - "A.7:9 — Anti‑patterns (with fixes)"
line_start: 21886
line_end: 21928
dependencies:
  - "A.1"
  - "A.10"
  - "A.13"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.21"
  - "A.3"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "E.10"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.9"
keywords:
  - "EntityOfConcern ≠ Description episteme"
  - "MethodDescription ≠ Method ≠ Capability ≠ Work"
  - "category error"
  - "system-role kind and assignment ≠ Work"
---

### A.7:9 - Anti‑patterns (with fixes)

1. **System-role-kind-as-behaviour** — calling the **system-role kind** a function or saying it acts.
   **Fix:** Name the acting System and direct behaviour or Work first. Add the local kind, assignment, Method, or Capability only when that stronger claim is current; none of them acts.

2. **Episteme‑as‑system** — “the model routed traffic” when “model” denotes an episteme rather than the deployed acting System.
   **Fix:** Name the System that used the episteme; keep recoverable deployed-System shorthand when that is the intended referent. Add Work, carrier, assignment, evidence, or source details only when the receiving claim uses them.

3. **Triad everywhere** — omitting **Work** entirely.
   **Fix:** Add a Work occurrence only when performed action is claimed; a design-time distinction diagram need not pretend that Work occurred.

4. **Operator blur** — using one “process operator” for everything.
   **Fix:** Choose among **Γ\_method**, **Γ\_time**, **Γ\_work**, **Γ\_sys**.

5. **Formal set, world-side collection, and collective collapse** — mathematical inclusion or collection belonging is used to make a grouping act or to infer constructive parthood.
   **Fix:** Keep formal inclusion with its mathematical or representation rule; state world-side belonging under the collection's own rule; require all six `A.1` matters for a collective System; state any constructive part relation separately.
6. **Unspecified evidence use** — citing content as evidence without identifying the episteme, target claim, or conditions needed for that use.
   **Fix:** Recover the evidence-use relation. Add A.10 carrier/source-currentness refs when that evidence or source use depends on them; a carrier reference alone does not establish support.

7. **Holon/system drift** — “holon maintains temperature”.
   **Fix:** Say **system**; reserve “holon” for neutral mereology.

8. **Function and system-role-kind swap in tables** — columns labelled “Function” whose entries are local system-role kinds.
   **Fix:** Rename the column to **System-role kind**. If behaviour is also being compared, give it a separate column and state the actual behaviour claim under its direct rule, including A.6.F functional behaviour or A.3.4 transformation where applicable.

9. **Process‑word leakage** — domain “process” used as FPF operator.
   **Fix:** Use the exact Γ operator for the composition claim. Keep a clear domain use of “process”; if it is ambiguous, state the actual Method, Work, transformation, mechanism, or other object intended.

10. **Carrier and episteme swap** — “we versioned the model” meaning a file was renamed.
    **Fix:** State whether the **episteme content** changed; if only a carrier was renamed, say so.

11. **Publication-as-mechanism** — modelling “publication” as if it were a Method or Mechanism.
    **Fix:** Identify the Description episteme directly through C.2.1 and keep specification use and publication separate. Name an actual authoring, measurement, observation, model, source-use, representation, or refinement relation only when current; operational build, render, or upload activity is separate Work by a System on carriers.

12. **Form-first MethodDescription** — “this is an SOP/algorithm/script, therefore it is a MethodDescription.”
    **Fix:** Identify the C.2.1 episteme, resolve one admitted Method as its exact EntityOfConcern, and find at least one substantive way-of-doing claim; otherwise retain only the source cue.

13. **Mandatory description hop** — a Method identifier or receiving `methodRef` is forced through a document or description edition.
    **Fix:** Resolve designation and the receiving reference directly to the exact Method under their effective ReferenceScheme discipline; cite `methodDescriptionRef` separately only when its claims are actually used.

14. **Lifecycle time as membership** — authoring, revision, citation, approval, publication, or use is treated as creating MethodDescription membership.
   **Fix:** Keep those Work and neighboring relations under their subject patterns; reapply the same A.3.2 membership test to the independently identified episteme.

