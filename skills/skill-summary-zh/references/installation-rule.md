# Installation integration

Append this rule only when the user requests automatic localization. Preserve other AGENTS.md content and avoid duplicating an existing equivalent rule:

> After installing or updating any Codex skill, invoke `$skill-summary-zh` on the affected skill folders before reporting completion. Review the entire displayed summary, distill English explanations into concise Chinese, preserve names/instructions/policies, and verify every changed file. Report UI-refresh limitations separately. Do not start a watcher or silently modify marketplace catalogs.

This applies to installs performed by the agent in the instruction's scope. It does not monitor filesystem changes from other applications. For those, run the skill explicitly afterward.
