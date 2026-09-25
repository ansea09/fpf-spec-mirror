---
chunk_kind: "child"
pattern_id: "B.5.TC"
pattern_title: "Compare Theoretical Accounts for a Working Question"
section_id: "B.5.TC:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.TC/B.5.TC__012_sota-echoing.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "B.5.TC — Compare Theoretical Accounts for a Working Question"
  - "B.5.TC:11 — SoTA-Echoing"
line_start: 45572
line_end: 45583
dependencies:
  - "B.5.RA"
  - "B.5.RR"
  - "B.5.TU"
  - "C.11.DUA"
  - "C.28"
  - "C.29.1"
  - "C.29.2"
  - "C.29.3"
  - "F.0.2"
keywords:
---

### B.5.TC:11 - SoTA-Echoing

For comparing what different mathematical accounts let a practitioner compute, **adopt** the operation-based comparison illustrated by Fong and Spivak's *Seven Sketches in Compositionality* (2019), §2.5.2–§2.5.3. Reachability and cost use different operations for combining steps and choosing among alternatives. Against comparison by shared route terminology, this makes the lost answer and composition condition visible in :4.3 and :5.1. The finite compatibility example is a construction here. Reopen its application when the quantity or allowed composition changes. [Author manuscript](https://arxiv.org/pdf/1803.05316).

For physical formulations that may agree, **adopt** the constructive comparison in Sussman and Wisdom's *Structure and Interpretation of Classical Mechanics*, second edition (2015), §1.6: derive the equations under the stated force and potential assumptions. This answers more than a numerical fit and often costs less than a new simulation. Against selecting a formulation solely by familiarity, preserve the advantage of coordinates adapted to constraints. Sections :4.3–:4.4 and :5.2 separate that choice from numerical approximation. Reopen when interactions, constraints or the requested result change. [Publisher's text](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/9579/sicm_edition_2.zip/chapter001.html).

For comparing causal uses, **adopt** intervention construction from Pearl's *Causal inference in statistics: An overview* (2009), §3.2.1, and **adapt** it here to expose the particular consequence on which two accounts disagree. Agreement in the observed distribution, a serious comparator for prediction, can leave that intervention consequence undecided. This changes :4.4 and :5.3. C.28 supplies the broader causal method. Reopen when the causal premises or intended intervention change. [Author's paper](https://ftp.cs.ucla.edu/pub/stat_ser/r350.pdf).

For prediction, a serious alternative to choosing a single account is combining predictive distributions. Yao, Vehtari, Simpson and Gelman's stacking method (2018) chooses weights through predictive performance when the candidate set need not contain the data-generating model. **Adapt** that question-relative choice into :4.5's permission to retain combinations. **Reject** using such predictive weights as a verdict about causal mechanism or mathematical equivalence; those are different comparison questions. The statistical method remains with its domain, including its scoring and validation conditions. Reopen when prediction under another distribution or a different use is required. [Authors' paper](https://sites.stat.columbia.edu/gelman/research/published/stacking.pdf).

This pattern combines these constructive contributions into a common comparison method. Its first result is the comparison obtained under the stated conditions.

