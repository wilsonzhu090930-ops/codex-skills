---
name: statistical-modeling-report
description: Use when supplied Excel or CSV data require one-way ANOVA with post-hoc comparisons, chi-square independence tests, or K-means and PCA, especially coursework or modeling reports with figures and Markdown results. Not for time-trend regression or supervised classification.
metadata:
  short-description: "分析组间差异、独立性与客户聚类并生成图文报告"
---

# Statistical modeling report

Turn supplied tables into traceable statistical decisions and a coherent report. Execute only the analyses and deliverables requested; a request to learn the data starts with inspection, not a full modeling run.

## 1. Establish the data contract

Inspect every relevant sheet and supplied assignment/notes. Resolve sheet numbers to actual names; identify the independent observation, variable types, units, group definitions, counts and provenance. Report missing values, repeated rows and duplicate identifiers separately. Preserve source files.

Confirm whether a categorical column is an observed outcome, a synthetic generation label or a teacher-only reference. Define grouped categories explicitly; do not treat an identifier as a predictor. Use the available spreadsheet/PDF skills for those file operations when applicable.

If only summary results are supplied, distinguish verified recomputation from transcription. Exact counts suffice for a contingency test; refitting clustering/PCA or drawing real sample projections requires the feature data. For ANOVA/post-hoc work, check whether raw data or sufficient group summaries support the chosen method. Mark unavailable results explicitly rather than reconstructing observations from teacher answers.

## 2. Run the requested branches

- **One-way ANOVA:** record the grouping rule, alpha, H0 (equal population means), H1 (at least one differs), group n/mean/sample SD, F with degrees of freedom and p. Assess independence from design and normality/variance assumptions with attention to small samples; a non-significant diagnostic is not proof. When the omnibus result is significant and comparisons are requested, use Tukey HSD/Tukey–Kramer under the common-variance model; report signed mean differences, simultaneous intervals and adjusted p values. If that model is unsuitable, select and label a justified alternative and compatible post-hoc procedure. Include eta-squared when useful, without a causal interpretation.
- **Chi-square independence:** use observed counts, not percentages, in a contingency table. State H0/H1, expected counts, chi-square, df and p. Assess sparse expectations before relying on the approximation. An omnibus association and descriptive rate ranking do not establish every pairwise difference; perform pairwise comparisons only when requested, with multiplicity control.
- **K-means:** use specified substantive numeric features, excluding IDs and reference labels. Standardize with a recorded convention; specify candidate K values, n_init and seed. Compute SSE and mean silhouette on the same standardized space. Explain disagreement between the elbow and silhouette maximum instead of declaring a universally optimal K. Final-fit parameters may differ from the scan only when documented. Inverse-transform centers, count members and name profiles from measured features; cluster IDs and colors are arbitrary.
- **PCA:** fit to the same documented standardized features. Report individual and cumulative explained-variance ratios and the retained dimension rule. Color the projection by the actual clustering output, retaining all observations. Explain that explained variance is neither prediction accuracy nor proof that projection preserves all cluster geometry. Interpret components from computed loadings only.

Compute using full precision, round only for presentation, and never copy reference-answer scores as newly measured results.

## 3. Figures and report

When figures or a consolidated report are requested, read [the delivery contract](references/report-and-figures.md). Reuse an established plotting language; otherwise follow the available scientific-figure skill's selection rules. Invoke that skill for publication/report figure generation when available, without copying its implementation into this package.

Check runtime imports early. Use isolated or project-local dependencies under the host's rules; keep scripts parameterized and select an installed CJK font rather than embedding a personal machine path. Do not expose private data in shared examples.

Deliver a Markdown file plus its real figure assets when requested. Link checks, statistical verification and visual checks are separate completion evidence; state exactly which passed. Preserve the user's requested scope, language and existing report path.
