# Codex Skills

English · [简体中文](README.zh-CN.md)

Reusable skills distilled from practical Codex workflows.

## skill-summary-zh

Turn English explanations in the Codex skill list into concise, distinguishable Chinese summaries while preserving skill names, instructions, invocation policies and tool dependencies.

- Check new summaries after skill installation or updates, or inventory existing skills on request.
- Keep each explanation to at most 28 characters, retaining necessary technical names.
- Preview, back up, apply, verify every target, and restore without overwriting later edits.
- Distinguish verified file changes from a refreshed UI. Do not manufacture success by editing application databases or catalog caches.
- The helper does not call models, make network requests or read credentials. Codex prepares the reviewed translation plan from the skill's content.

### Installation

Copy the entire `skills/skill-summary-zh` folder into your personal Codex skills directory, such as `~/.codex/skills/`. Inspect existing folders with the same name rather than overwriting local changes. The helper requires Python 3.10+ and PyYAML; install this repository's `requirements.txt` in an isolated virtual environment.

Ask Codex:

> Use skill-summary-zh to translate the newly installed skill explanations into concise Chinese and verify every result.

### Automatic use after installation

The skill declares installation and update workflows as triggers. For reliable local use, ask Codex to append the rule in `references/installation-rule.md` to an authorized AGENTS.md. Agent-managed skill installations and updates will then include localization before completion.

This is not a background watcher. Skills installed through another application require a later check in Codex. Plugin updates can replace local translations. This skill does not automatically edit marketplace catalogs or application databases; it reports stale UI metadata as an unverified condition.

### Verification and rollback

```bash
python -m unittest discover -s tests -v
python skills/skill-summary-zh/scripts/localize.py scan --root /path/to/skills
python skills/skill-summary-zh/scripts/localize.py apply --plan plan.json --backup /path/to/new-backup --dry-run
python skills/skill-summary-zh/scripts/localize.py verify --plan plan.json
python skills/skill-summary-zh/scripts/localize.py restore --backup /path/to/backup --dry-run
```

This repository contains no personal account information, machine paths, skill inventories, credentials or source code from other projects. Contributions through issues and pull requests are welcome, especially improvements to summary quality and compatibility.

## workflow-to-skill

Distill proven workflows into reusable Codex skills, validate their behavior, and publish to the user's designated repository under an explicit request or standing authorization. Includes concise Chinese UI explanations and matching English/Chinese documentation. Preserve private data, existing local edits and concurrent remote changes.

Invoke `$workflow-to-skill` after a successful reusable workflow, or establish a local standing instruction for future agent work. This is not a background watcher or publisher.

## statistical-modeling-report

Use for supplied Excel/CSV coursework requiring one-way ANOVA with corrected post-hoc comparisons, chi-square independence tests, or K-means and PCA. Produces the requested statistical decisions, Chinese or user-language figures, and a Markdown report with verified asset links. It preserves source data and handles conflicting K-selection metrics, teacher-label exclusion, uncertainty and non-causal interpretation.

This is an instruction-only workflow, not a fixed-data calculator or bundled plotting library. It does not cover time-trend regression or supervised classification. Execute only requested stages; inspecting data does not imply permission to generate every analysis. Python implementations typically need pandas, openpyxl, NumPy, SciPy, statsmodels, scikit-learn and Matplotlib in an isolated environment. Use an available scientific-figure skill for its own rendering and QA requirements.

Copy `skills/statistical-modeling-report` into your personal skills directory without overwriting existing edits. Example: “Use $statistical-modeling-report to analyze these Excel sheets and consolidate the computed results and figures into a Markdown report.” Portable reports need their image assets as well as the Markdown file; link verification alone is not visual rendering verification.
