# Figures and Markdown delivery contract

## Choose figures by question

| Question | Recommended figure | Integrity check |
|---|---|---|
| How do group means differ? | Raw observations with mean and 95% confidence interval | Show all small-sample observations; define the interval method and n |
| Which means differ? | Tukey signed-difference interval plot | State subtraction direction; include zero reference and adjusted p |
| How do conversion rates differ? | Rate dots with Wilson 95% intervals | Show denominators; label the omnibus test without invented pairwise stars |
| Why choose this K? | Elbow and silhouette side by side | Mark the selection while retaining the actual silhouette maximum |
| Where are clusters? | PCA PC1–PC2 scatter with explained variance on axes | Plot all observations using final cluster assignments, not teacher labels |
| How much variance is retained? | Contribution bars and cumulative line | Match retention thresholds to the computed cumulative ratios |
| What characterizes each cluster? | Heatmap of standardized cluster means | State the zero reference; high recency means inactivity, not necessarily a favorable score |

Use a white background, restrained categorical colors and a stable color/shape mapping across cluster figures. Standardized heatmap values need a zero-centered diverging map; raw units belong in a center table. A profile name such as “price sensitive” is an interpretation unless price response was actually measured.

Reuse all relevant supplied observations. Explain any analytically justified exclusion and its count. With tiny groups, raw points are more informative than smooth distribution estimates. Prefer readable direct labels to excessive annotations.

For report-quality figures, export requested raster/vector formats, record raster DPI, and inspect the final renders. If the scientific-figure skill is used, complete its applicable alignment, PDF font and collision audits; preserve reports separately from deliverable figures. Fix label clipping, lines crossing text, incorrect color keys and unreadable legends before delivery. Automated checks do not replace visual review.

## Markdown shape

Use this sequence as needed, omitting unrequested branches:

1. Data sources, sheet mapping, variables, units and preprocessing.
2. Research question, H0/H1 and alpha for each inferential test.
3. Actual computed tables, test statistics, degrees of freedom, p, uncertainty and multiplicity method.
4. K-selection evidence, final parameters, counts and original-scale centers.
5. PCA contributions, retained dimensions and correctly bounded interpretation.
6. Requested figures beside the claims they support, with captions defining n and intervals.
7. Findings, material interpretation limits, and links to actual outputs and runnable code if supplied.

Separate chat delivery links from references inside the saved report. Chat links may require absolute paths while portable Markdown normally uses project-relative image paths. If an explicit host rule also requires absolute image references inside saved documents, resolve them and disclose the portability limitation. Spaces, parentheses, Unicode and URL-encoded paths need explicit verification. A Markdown image tag references a separate file; it does not store the image bytes inside the Markdown. If a self-contained file is required, agree on a supported embedding or packaging format rather than claiming links are embedded assets.

Verify every local image and output link against the report's directory or absolute target. Render the Markdown in an available viewer and inspect all images. If rendering is unavailable, report link verification separately and do not call it a visual render check. For a portable bundle, also reopen the copied/unpacked package in another directory.

## Reproducibility and scope

Keep analysis settings and results in one reusable script or structured output, and populate both figures and prose from that source where practical. Cross-check counts, sums of squares and contribution sums. Save sufficient precision in CSV/JSON and present small p values in scientific notation rather than zero.

Prefer CLI arguments or paths resolved relative to the script, optional dependency paths and font discovery. Do not publish private paths, assignment files or a whole installed third-party skill. A missing library should trigger an early, specific environment check, not repeated failure of a long plotting job.

Only claim the stages actually executed: inspecting a classification sheet is not training a classifier, and classifying a synthetic risk segment does not validate future churn prediction. Update an existing user-designated report in place while preserving unrelated edits.
