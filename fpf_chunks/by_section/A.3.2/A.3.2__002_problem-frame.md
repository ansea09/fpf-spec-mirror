---
chunk_kind: "child"
pattern_id: "A.3.2"
pattern_title: "U.MethodDescription: Description Episteme for a Way of Doing"
section_id: "A.3.2:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.2/A.3.2__002_problem-frame.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.3.2 — U.MethodDescription: Description Episteme for a Way of Doing"
  - "A.3.2:1 — Problem frame"
line_start: 7058
line_end: 7093
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.22"
  - "A.3.1"
  - "A.6.1"
  - "A.6.5"
  - "B.1.5"
  - "B.3"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.28"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.18"
  - "F.9"
  - "U.Method"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "claim-bearing episteme"
  - "exact U.Method EntityOfConcern"
  - "method-description membership"
  - "representation versus publication versus plan versus Work"
  - "same method versus equivalent descriptions"
  - "substantive way-of-doing claim"
---

### A.3.2:1 - Problem frame

Use this pattern when engineers need reusable claims about how one method is carried out and must keep those claims distinct from the representation, publication, approval, plan, or actual work through which the method is discussed or enacted. In FPF terms, decide whether an already identified `U.Episteme` is a `U.MethodDescription`: whether its exact `EntityOfConcern` is one admitted `U.Method` and its claims say something substantive about that method as a way of doing.

**Plain reading.** A method description is the knowledge object whose claims say how one identified method is done. Code, text, or a diagram may represent those claims; a publication occurrence may make an edition available; neither fact decides membership.

Recognizable working moments include:

* a maintenance team comparing a revised procedure with the method used to plan the next service window;
* a clinical team selecting a triage guideline while keeping guideline claims, approval, and patient-specific work separate;
* a production-planning team comparing scheduling-method claims while the MILP representation and solver runs change.

Use it when the working question is:

* which admitted `U.Method` is the exact `EntityOfConcern`;
* which claim states the method's transformation or enactment concern, applicability, precondition, effect, bound, or internal composition;
* which work or decision should rely on those claims, and whether the claims are adequate for that receiving use;
* which `C.29` representation corresponds to the claims, which publication occurrence makes the selected edition available, which publication form expresses that edition, and which `U.PresentationCarrier` bears the form, when those distinctions affect the work;
* whether the exact EntityOfConcern references resolve to the same A.3.1-reidentified method, and, as a separate question, whether the claim contents are equivalent for the receiving use; when effective `U.ReferenceScheme` values differ, an exact F.9 Bridge can establish only the current `SenseCell` correspondence and admitted use, not method identity or claim equivalence.

**Primary EntityOfConcern.** The exact `EntityOfConcern` is the admitted `U.Method` being described. `U.MethodDescription` is the same `U.Episteme` individual already identified through `C.2.1`; the dependent kind adds a membership judgment, not another described entity or another identity rule.

**Primary working reader.** An engineer or researcher who must rely on reusable claims about a method before planning, enactment, comparison, audit, or revision.

**Primary working concern.** Identify the claim-bearing episteme and exact method first, then judge separately whether the claims are adequate for the current work or decision.

**Primary viewpoint.** The practitioner selecting, comparing, or revising method descriptions while method identity and the surrounding representation and publication relations remain explicit.

**First useful move.** Name the exact `U.Method`, then point to at least one claim that says how that method is done. Name the work or decision that will use the claim. Evaluate adequacy for that receiving use separately from membership.

**What goes wrong if missed.** A visible file or diagram is classified by its form, a mere mention is mistaken for a description, or an episteme about a relation structure among several methods is treated as if it described one composite method. Planning, enactment, audit, and review then rely on the wrong governed object.

**What this buys.** The project can identify, compare, revise, and reuse method descriptions while keeping the described `U.Method`, `RelationSignature`, `OperationAlgebra`, C.29 representations, publication occurrences and forms, presentation carriers, work plans, work occurrences, and evidence under their own governing patterns.

**Not this pattern when.** Do not infer membership from words such as `algorithm`, `program`, `proof`, `workflow`, `process`, `procedure`, `recipe`, or `model`. Recover the current claim and exact governed object. If no admitted `U.Method` is the exact `EntityOfConcern`, or the episteme makes no substantive claim about its way of doing, this membership rule does not apply. Use the governing pattern for the actual method, selected structure, formal substrate, `RelationSignature`, `OperationAlgebra`, work plan, work occurrence, evidence use, or publication use.

