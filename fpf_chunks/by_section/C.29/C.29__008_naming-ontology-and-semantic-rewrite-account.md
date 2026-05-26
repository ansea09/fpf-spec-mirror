---
chunk_kind: "child"
pattern_id: "C.29"
pattern_title: "Mathematical Lens Adequacy (MLA)"
section_id: "C.29:6"
section_title: "Naming, ontology, and semantic-rewrite account"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29/C.29__008_naming-ontology-and-semantic-rewrite-account.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "C.29 — Mathematical Lens Adequacy (MLA)"
  - "C.29:6 — Naming, ontology, and semantic-rewrite account"
line_start: 49585
line_end: 49630
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.4"
  - "A.19"
  - "A.3.3"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18.1"
  - "C.19.1"
  - "C.26"
  - "C.27"
  - "C.28"
  - "C.29"
  - "E.10"
  - "E.10.SEMIO"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.19"
  - "E.8"
  - "E.9"
  - "F.9"
  - "G.10"
  - "G.2"
  - "G.5"
  - "G.9"
keywords:
  - "LensSupportPosture"
  - "coarse-graining"
  - "invariants"
  - "learned lens"
  - "lens mapping mode"
  - "lost structure"
  - "mathematical lens"
  - "ontology smuggling"
  - "preserved structure"
  - "rival lens"
  - "scale window"
  - "stop condition"
  - "structure-preserving representation"
  - "validation posture"
---

### C.29:6 - Naming, ontology, and semantic-rewrite account

#### C.29:6.1 - Name

Name: `C.29 — Mathematical Lens Adequacy (MLA)`.

Abbreviation: `MLA` = **Mathematical Lens Adequacy**. No prior temporary code is reused; the pattern code, card prefix, reference prefix, and checklist IDs use only `MLA`.

The stable name is `Mathematical Lens Adequacy` because `C.29` governs adequacy for a declared use, not strength on an unnamed scale. Plain prose can still say that a useful mathematical lens compresses many cases while preserving declared distinctions; load-bearing use is recovered through `CandidateMathObject`, `LensMappingMode`, `PreservedStructure`, `LostStructure`, `LensSupportPosture`, and `StopCondition`.

#### C.29:6.1a - C.29-local naming guard

`MLA.*` instruments are `C.29`-local unless separately admitted. They are not `U.*` kinds, not durable FPF record families, and not substitutes for `U.Kind`, `KindSignature`, `KindBridge`, `BridgeCard`, `EvidenceGraph`, `ChoiceResult`, `U.WorkPlan`, `U.Work`, or assurance records.

Do not mint `LensKind`, `MathematicalLensKind`, `MLAQuality`, `MLACompliance`, or `MLARecord` from `C.29` use.

When one `C.29` application needs a mathematical-lens name to become reusable outside that application, use `F.18` local-first naming; when it quantifies over a class of described entities, use `C.3` Kind-CAL; when it creates or reuses a durable concept or record family, use `F.8` mint/reuse and `E.9` design-rationale support.

#### C.29:6.2 - Tempting wrong names rejected

| Tempting name | Reason rejected |
|---|---|
| `Mathematical Ontology Principle` | Smuggles the metaphysical claim `C.29` rejects. |
| `Single-Foundation Math Posture` | Would collapse plural lens families into one foundation claim; C.29 instead tests each selected family by declared mapping, local use, and recoverable loss. |
| `Math Metaphor Adequacy` | Too narrow and too vague; the selected answer is structure-preserving representation, not mere metaphor. |
| `Quantum-Like Generalization` | Misplaces the general pattern under one special lens. |
| `Category-Theoretic Bridge Pattern` | Over-privileges category theory; MLA is broader. |

#### C.29:6.3 - Ontology guard selected for FPF

> A physical, organizational, or epistemic phenomenon is not directly identified with a mathematical object; it is represented through a mathematical object by an explicitly declared mapping that preserves some structures and loses others.

#### C.29:6.4 - E.10.SEMIO recoveries applied

| Earlier wording risk | Recovered wording in `C.29` |
|---|---|
| `source` / `target` | Use `source-basis document`, `Basis used`, `describedEntityRef`, `receiving FPF pattern`, `BridgeRefSet`, or exact pattern reference as appropriate. |
| raw source intake as evidence | Recovered as source-basis text, not authority. Selected content is integrated through `C.29:13a`, `C.29:13`, and the field/checklist rows that carry its live claim. |
| `structure-preserving identification` | Rewritten to `structure-preserving representation / mapping` unless direct equivalence is explicitly the `LensMappingMode`. |
| Slash compounds such as `Dynamics/TransitionLaw?` | Rewritten as `DynamicsRef?` / `TransitionLawRef?`. |
| Procedure-like pattern-control language | Rewritten as `pattern application`, `Disposition`, `BridgeRefSet`, `C28ApplicationRef`, or `C28SupportRecordRef` only when that exact neighboring-pattern application or support record is live. |
| `ExportPolicy` | Split into `admissibleUse`, `nonAdmissibleUse`, and optional `ExportPolicyRef?`. |
| free strength qualifier | Replace with exact adequacy fields, evidence or scale basis, support posture, and stop-condition wording. |
| `model`, `lens`, `math` as prestige heads | Recovered as `CandidateMathObject`, `LensMappingMode`, `PreservedStructure`, `LostStructure`, and `LensSupportPosture`. |
| Causal or assurance implications | Recovered as `CausalUseDisposition?` and `AssuranceUseDisposition?`, with `C.28`, `A.10`, `B.3`, and G-patterns as neighboring governors. |

