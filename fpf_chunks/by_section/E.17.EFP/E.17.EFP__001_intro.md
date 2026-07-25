---
chunk_kind: "child"
pattern_id: "E.17.EFP"
pattern_title: "ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
section_id: "E.17.EFP:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.EFP/E.17.EFP__001_intro.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "E.17.EFP — ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
  - "E.17.EFP:intro — Intro"
line_start: 78700
line_end: 78759
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.6.3.CSC"
  - "A.6.4"
  - "A.6.B"
  - "A.7"
  - "B.3"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.ID.CR"
  - "F.18"
  - "F.9"
  - "U.MultiViewDescribing"
keywords:
---

## E.17.EFP - ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**One-line summary.** `ExplanationFaithfulnessProfile` states how explanation-facing renderings over already available claims, traces, and pins on existing MVPK faces can be used. It helps a publication-side reviewer or explanation reader distinguish source-pinned rendering, source-linked reconstruction, didactic retelling, and speculative retelling without creating a second face family or a second semantic rule track.

**Explanation-facing rendering in plain terms.** One explanation-facing rendering on an existing MVPK face; not the whole face family, not the whole source `U.Episteme` or source `U.EpistemePublication`, and not a second semantic track.

**Explanation-use relation in plain terms.** State how that rendering relates to already available source `U.Episteme` or source `U.EpistemePublication`, source pins, traces, and provenance references, which explanation-use class it belongs to, and what downstream claim or effect still stays outside the profile.

**Use this when.** Use this profile when one note, memo, sheet, screen, table, or short section is trying to help a reader understand an already available source `U.Episteme` or source `U.EpistemePublication` on an existing face and you need to say what kind of explanation it is without turning that help into a second semantic rule track.

**Start here when.** The first decision is about one explanation-facing rendering on an existing MVPK face, and the real question is whether it stays source-pinned, becomes bounded reconstruction, is openly didactic, or has already shifted into speculation or blocked downstream claim or effect.

**What goes wrong if missed.** Helpful explanation quietly turns into a second semantic rule track, hidden bridge-comparison load, or unsupported downstream guidance because the rendering is interpreted as canonical content.

**What this buys.** One honest explanation class on an existing face with visible source references, bounded-use boundary, and explicit neighboring-pattern boundaries when the rendering has stopped being merely explanatory help.

**Not this pattern when.** Not this profile when the real job is same-entity rewrite (`A.6.3.CR`), representation change (`A.6.3.RT`), bounded comparison over a comparative review unit (`E.17.ID.CR`), changed EntityOfConcern (`A.6.4`), deliberately coarsened rendering that now needs narrower bounded claim or effect, blocked downstream claim or effect, and reopen to the source `U.Episteme` or source `U.EpistemePublication` (`A.6.3.CSC`), downstream work or reliance (`A.15`, `A.15.4`), assurance or engineering justification (`B.3`), or gate-bearing content (`A.20`, `A.21`).

**First output.** One compact explanation-use note: explanation class, source reference, bounded explanation-reader use, blocked downstream use, and reopen or boundary condition. MVPK face, pins, provenance, and source fields are inherited by reference unless ambiguity or a load-bearing source-relation question makes them relevant to the claim.

**Ordinary-output claim inventory.** After `ExplanationFaithfulnessProfile`, the author has claimed only that this explanation-facing rendering has this explanation class, this source relation, this source-reference state, and this bounded use. The author has not claimed model truth, evidence path, assurance, safe reliance, gate passage, work occurrence, release reliance, or source replacement unless the neighboring FPF pattern governing that claim and project-side FPF kind and reference named by value are named.

**Working explanation move.** Name the one explanation-facing rendering, classify it as source-pinned rendering, bounded reconstruction, didactic retelling, or speculative retelling, and state its bounded reader use. If reliance, evidence, work, gate, engineering justification, comparison, narrower-use rendering, or new-claim load appears, use the neighboring FPF pattern governing that claim. Use `E.17:5.1c` for `orientation use`, `reliance use`, `operative claim`, `blocked downstream use`, and `reopen trigger`; use `E.17:5.1d` when the primary question under repair belongs to same-entity rewrite, representation change, coarsening, comparison, bridge or substitution, work or reliance, gate, evidence, assurance, retargeting, carrier work, or front-end work rather than explanation-facing rendering.

**Ordinary use.** If the explanation only helps reader understanding, source-finding, review, comparison, or planning preparation, one compact review note naming the explanation class, source reference, and blocked downstream claim or effect is enough. Plain wording remains ordinary unless it changes bounded use, source relation, evidence, gate, assurance, work, decision, or a neighboring claim governed by another FPF pattern.

**Load-bearing use.** Open the fuller explanation review only when the rendering will guide work or reliance, be externally relied on, be disputed, cross context, affect person or team status, or be cited as evidence, approval, engineering justification, gate, or release reliance.

**Stop condition.** Stop once the explanation class changes no next reader-help, review, source-finding, comparison, or planning-preparation move and blocks no concrete overclaim about source relation, work or reliance, evidence, approval, gate, or release.

**Bounded explanation-use examples.**

| Bounded explanation use | Source-finding check with no downstream claim or effect | Blocked explanation use |
| --- | --- | --- |
| A `SourcePinnedExplanation` or `SourceLinkedExplanationReconstruction` helps navigation, bounded restatement, or source inspection with pins and trace visible. | A didactic explanation helps onboarding or helps the team find the source, while operative claims still return to the source-pinned face or `A.10` evidence path. | A fluent explanation is used as assurance, evidence, approval, gate passage, release permission, or work-occurrence evidence. |

**Neighboring project records and governing patterns.** `E.17.ID.CR` governs bounded comparison over a comparative review unit; `A.6.3.CR` or `A.6.3.RT` govern same-entity rewrite or representation change; `A.6.3.CSC` governs a rendering that stays honest only through narrower bounded claim or effect, blocked downstream claim or effect, and reopen to the source `U.Episteme` or source `U.EpistemePublication`; `A.6.4` or `OntologicalReframing` govern changed EntityOfConcern; `A.15` and `A.15.4` govern downstream work or reliance, `B.3` governs assurance and engineering justification, and `A.20` or `A.21` govern gate-bearing claim or effect.

**Common wrong escalations and boundary transfers.** Do not use this profile to hide new claims, bridge-comparison load, action-selection pressure, or gate-bearing guidance inside helpful prose. If the rendering is really a bounded comparison, apply `E.17.ID.CR`; if it is only same-entity rewriting or representation shift, apply `A.6.3.CR` or `A.6.3.RT`; if it is a deliberately coarsened rendering whose narrower bounded claim or effect, blocked downstream claim or effect, and source-bearing reopen now govern the case, apply `A.6.3.CSC`; if it is already making world, work or reliance, assurance, or gate-bearing claims, leave `E.17.EFP` for the more exact downstream FPF pattern or project-side record.

**Generated-explanation repaired case.** Use this case when a generated explanation is being relied on beyond reader help. The first E.17.EFP move is to classify the rendering as source-pinned rendering, source-linked reconstruction, didactic retelling, or speculative retelling. The profile only states the explanation relation, source-finding state, source references, bounded explanation-reader use, blocked downstream use, and reopen condition for the current rendering. The explanation becomes usable for an operative claim only when an `A.10`-governed evidence path maps that claim to the exact source passage, carrier path, or project-side FPF kind and reference named by value that carries, supports, or exposes the source basis for it in the relying context. If the operative claim would raise assurance, release confidence, safety, trust, gate passage, work occurrence, work authorization, approval, or permission, apply the direct owner: `B.3` for assurance, `A.21` for gate decision, `A.15`/`A.15.1` for work, `A.2.8.PER` for a strong grant, exercise, weak non-prohibition/non-violation finding, or permission conflict, `A.2.8` for an obligation/recommendation/prohibition commitment, `A.2.9` for the issuing act, or another source relation that carries, supports, or exposes the source basis for the operative claim. If the map or project-side FPF kind and reference named by value is missing, keep only a prospective repair request, source-gap note, or narrower explanation-use note; if operative reliance is still attempted, the applicable `A.10`, `B.3`, `A.21`, or other relation governing the asserted use can return evidence-needed, abstain, or no-bounded-current-use. Do not open an `A.10` path for ordinary reader help; otherwise the generated explanation remains reader help, not approval, permission, authorization, evidence, assurance, gate passage, release reliance, or work-occurrence evidence.

**Common wrong first interpretation.** A fluent, confident, source-linked, or reliable-looking explanation is treated as evidence. First honest entry: classify the explanation rendering and use it for reader help or source-finding; only an operative claim with an A.10 evidence path or another source relation that carries, supports, or exposes the source basis for the operative claim can carry downstream reliance.

Negative result: if a generated explanation says "reliable" but no operative claim maps to a source relation, the E.17.EFP result is source-finding only or reader help only. If an attempted downstream reliance is still raised, the receiving `A.10`, `B.3`, `A.21`, or other relation named by value can return evidence-needed or no-bounded-current-use for that attempted reliance. It is not weak evidence by style, confidence, fluency, or citation-like wording.

**Generated-retelling survival.** A generated retelling preserves only the reader help, source-finding cue, quoted source pins, explicitly repeated source relation, and explicitly repeated bounded-use boundary that remain inspectable in that retelling. It does not become or preserve the source `U.Episteme`, source `U.EpistemePublication`, evidence path, assurance, gate passage, decision status, permission, or source replacement merely by fluency, completeness-looking wording, or citation-like links. If the generated retelling compresses, omits, strengthens, or changes source claims, treat the result as a new explanation-use case, a narrower-use rendering under `A.6.3.CSC`, or reader help only.

**Derivative rendering and adaptation source-link rule.** A fork, adaptation, abridged guide, translated rendering, generated explanation, tutorial, access-format conversion, or other derivative rendering of a source `U.Episteme` or source `U.EpistemePublication` can improve access or teaching, but it is not equivalent to the source by usefulness, fluency, or local adoption. It can expose or cite a project-side FPF kind and reference named by value, but the bounded source relation belongs to the exposed value and source relation, not to the explanation rendering as a face. If the derivative rendering will guide work or reliance, `A.10` maps every operative claim being relied on to the exact source passage, carrier path, or project-side FPF kind and reference named by value that evidences it; if the map or exact value is absent, only a prospective repair request, explicit source-gap note, or prospective evidence-work plan can be created. If simplification or format change narrows bounded use, forbids downstream use, or requires return to the source-bearing side, use `A.6.3.CSC` rather than treating the derivative as ordinary explanation.

**Explanation-rendering identity over revision and regeneration.** A generated, translated, revised, or regenerated explanation-facing rendering is not the same explanation rendering merely because it uses the same source face, prompt, template, carrier, or title. For use beyond ordinary reader help, the rendering names the preserved source references, changed claims, generation or production relation when present, and bounded use for this rendering. A translation or adaptation preserves bounded use only when the operative claims and source links survive the change; otherwise it becomes a new explanation-use case, a narrower-use rendering under `A.6.3.CSC`, or reader help only.

**Placement.** Profile governed by `E.17.0` and `E.17` review.
**Builds on.** `E.17.0 U.MultiViewDescribing`; `E.17` MVPK; `A.7`; `E.10.D2`; `A.6.B`; `F.9`; `F.18`.
**Coordinates with.** `ConservativeRetextualization`; `RepresentationSchemeTransition`; `E.17.ID.CR ComparativeReviewUnit`; `A.6.4`; `A.10`; `A.15`; `A.15.4`; `B.3`; `A.20`; `A.21`; `A.2.8`; `A.2.8.PER`; `A.2.9`.

