---
name: skill-summary-zh
description: Localize Codex skill-list summaries into concise, distinguishable Chinese after installing or updating skills, or when the user requests Chinese skill explanations. Use automatically as the final verification step of a skill installation or update; also handle explicit inventory, localization and verification requests. Preserve names, instructions and invocation policies.
metadata:
  short-description: 将技能列表说明翻译成一行简洁中文
---

# Chinese skill summaries

Use this after a skill install/update, or when the user asks to localize the skill list. Complete the localization before reporting that installation is finished. This is an agent workflow, not a background daemon: installs by another program are discovered only when the agent next checks them.

## Scope and inventory

1. Identify the exact newly installed/updated skill folders. For a full inventory, inspect the user's skills roots and confirmed installed plugin directories. Do not interpret an entire downloaded marketplace as installed skills.
2. Run `python scripts/localize.py scan --root <skills-root>`; repeat `--root` for other explicit roots. A single skill folder is also accepted. The helper requires PyYAML. Use the user's established Python environment; install dependencies into an isolated environment if needed.
3. Read each target's original `description`, relevant instructions, and UI metadata. A Chinese word appearing somewhere does not prove a mixed or mostly English explanation is localized. Check the whole displayed summary, including already-Chinese summaries that are too long.

## Distill the explanation

Write one natural Chinese line, usually 12–24 and at most 28 characters (including Latin identifiers). Keep necessary technical names such as Git, PDF and DOI. Use a concrete action plus the distinctive object or method. Distinguish neighbors, for example:

- Paper translation: 保留原版式，逐页翻译论文 PDF
- Paper deep reading: 用推导和实例讲透一篇论文
- Reference checking: 逐条核验作者、年份与 DOI
- Scientific plots: 制作并审查投稿用科学图表

Keep the skill's name and instructions in their original language. Translate UI explanations, not the model-routing description or the operational rules. Avoid generic labels like “帮助你完成任务”.

## Apply and verify

Create a JSON plan with explicit skill-folder paths:

```json
[{"path": "/path/to/skills/example", "summary": "按需求和规范审查代码改动"}]
```

1. Preview with `python scripts/localize.py apply --plan plan.json --backup <new-backup-dir> --dry-run`.
2. Apply with the same command without `--dry-run`. It backs up originals and changes only `interface.short_description` in `agents/openai.yaml`. Existing names, prompts, policies, dependencies, comments outside that field and SKILL.md bytes remain intact. Missing UI files are created with only the intended summary.
3. Run `python scripts/localize.py verify --plan plan.json`. Inspect every result, the translated count and unresolved targets. The script does not translate text on its own: the agent supplies the reviewed Chinese plan.
4. Distinguish file verification from live UI verification. If old English remains, locate the actual installed source and inspect supported metadata/cache-refresh behavior. Do not blindly edit marketplace catalogs, application databases, temporary plugin copies or other installations. Do not alter caches merely to make a check appear green. If the app cannot be inspected or refreshed, report that specific limitation; never claim visible completion from a file-only check.
5. For rollback, use `python scripts/localize.py restore --backup <backup-dir> --dry-run`, then restore. Later file edits cause rollback to stop rather than overwrite them.

Plugin updates can replace localized files. Re-run this workflow after updates. Do not install a watcher, schedule a job or enable hooks without a separate request.

## Automatic local use

Being installed makes this skill discoverable; it does not intercept every downloader. If the user requests automatic use on this computer, add the short integration rule in [references/installation-rule.md](references/installation-rule.md) to an authorized local AGENTS.md, preserving existing content. That rule makes agent-managed installs call this skill before completion. Do not publish that machine's AGENTS.md, account data, inventories or absolute local paths with the skill.
