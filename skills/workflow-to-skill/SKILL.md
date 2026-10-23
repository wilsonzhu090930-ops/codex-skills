---
name: workflow-to-skill
description: Distill a proven, reusable workflow into a Codex skill and publish it to the user's designated skills repository. Use when the user asks to save or distill a workflow as a skill, or a successful reusable workflow is identified under an explicit standing publication instruction. Verify behavior and publication; retain the original task's scope.
metadata:
  short-description: 将实用工作流蒸馏为技能并验证发布
---

# Distill and publish a workflow

Capture the reusable method, rather than the conversation that produced it. A standing publication instruction permits publishing suitable skills to the specified repository; it does not authorize unrelated service access or changes to other repositories.

## Select the method

A workflow is worth capturing when it has clear triggers, repeatable steps, useful checks, and non-obvious guidance supported by a successful run. Start from evidence in the completed task. A single proven method can qualify; an untested idea remains a draft. Finish the user's main task before distilling it unless creating the skill is itself the task.

Inspect the target repository's existing skills first. Improve an overlapping skill instead of adding a second name for the same behavior. Ordinary chat, a one-off command and general advice usually do not warrant a skill.

## Package it

1. Extract inputs, essential decisions, procedure, failure handling and completion evidence. Replace personal paths, identities and task-specific values with parameters. Keep credentials and private data out of all files, examples, Git history and logs.
2. Create `skills/<short-name>/SKILL.md` with a focused name and trigger description. Keep the operational instructions concise. Add scripts only for repeatable transformations, and references only for details that should load conditionally.
3. Include `agents/openai.yaml` with a concise Chinese `short_description` that distinguishes the skill from its neighbors. Preserve existing invocation policies when updating. If `$skill-summary-zh` is installed, use it to verify the explanation.
4. Add corresponding English and Chinese repository documentation with matching capabilities and limitations. Preserve the repository's established language-switch links and layout.
5. Publish original instructions and authorized resources. If a third-party implementation is needed, check its license and attribution rather than copying installed vendor skills wholesale. Do not include a local machine's configuration or full skill inventory.

## Validate and install

Validate skill metadata, local links and script entrypoints. Run the tests warranted by the behavior; use synthetic fixtures for filesystem changes, backups and restoration. Verify that any published executable helper actually runs. For an instruction-only skill, inspect its trigger boundaries, steps and completion checks without inventing a runtime test result.

Install the resulting skill locally when requested or covered by the user's standing instruction. Preserve existing local edits, back up updates, and complete installation-time summary localization. Do not enable background jobs, hooks or new account integrations simply to make the skill discoverable.

## Publish under the user's authorization

Use the repository explicitly designated by the user; keep the destination in their local instructions rather than hardcoding their identity into this reusable skill. Inspect the remote branch and working tree before publishing.

- For an additive, validated skill in the user's own collection, a normal commit to the repository's established default branch is appropriate if authorized by their standing instruction.
- Use a separate branch and pull request for substantial restructuring or changes that could disrupt existing skills. Attach every created PR to the current chat using the app's artifact tool when available.
- Preserve concurrent remote changes. Never force-push or change repository permissions to bypass a publishing failure.
- Prefer the connected GitHub tools; if they lack write capability, an existing authorized Git credential route may be used. If new login or broader permissions are required, report the exact blocker and let the user perform the necessary authorization.
- Read the published file or commit back from GitHub before saying publication is complete. Report the skill link, actual validation performed, and any material remaining limitations. Do not promise a particular contribution-calendar result.

Installing this skill does not create a background publisher. It runs during agent work within the user's standing instruction or explicit request.
