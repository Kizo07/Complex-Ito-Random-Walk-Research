# Status

- Active task: `TASK-009`
- Owner: Codex (user-authorized direct exception)
- State: in progress — Milestones 1-6 complete; manuscript assembled and
  rendered (paper/phase6)
- Allowed writes: project directory only
- Conda environment: `phase3-paper` (Python 3.12.13)
- Scope: Phase 6 — financial applications of the one-phase Euler framework;
  selected problem P1: stochastic correlation with exact bounded kernels
- Root deliverables: `PHASE_6_FINANCE_APPLICATION_PROBLEM_LIST.md`,
  `PHASE_6_LITERATURE_REVIEW.md` (incl. §5a),
  `PHASE_6_MILESTONE_{1..6}_*.md`,
  `phase6_{correlation,joint,fk,corridor,ou}.py`,
  `tests/test_phase6_*.py` (77/77 pass), six milestone notebooks,
  `phase6_figures/`
- Publication project: `paper/phase6/` — `index.qmd` (12-page manuscript,
  theorem-led), `references.bib` (25 entries), `RESEARCH_NOTES.md`
  (novelty boundary + claim-to-evidence matrix),
  `notebooks/phase6_correlation_paper.ipynb` (executed, 16.7 s, seed
  20260727, all checks within tolerance),
  `output/exact-bounded-correlation.pdf` + `.html` (rendered clean, no
  unresolved references)
- Key results: exact kernels + first-passage laws; exact correlation
  derivatives incl. new pay-at-hit closed form; measure-change invariance;
  DDS variance-clock reduction with sign theorem; deterministic FK clock
  law (|z|<1 vs MC); corridor occupation with atom separation (arcsine
  anchor 5e-4); OU-driver classification with kappa->0 anchors
- Next candidates: leverage extension; estimation/calibration study;
  independent academic review (per project convention, opencode GLM 5.2);
  obtain van Emmerich preprint + HU-Berlin thesis full text
- Blockers: none
- Git branch: `phase-4-technical-paper`
- Git publication actions: out of scope unless separately requested
