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
