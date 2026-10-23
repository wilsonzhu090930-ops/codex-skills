# Codex Skills

[English](README.md) · 简体中文

从实际 Codex 工作流中整理出的可复用技能。

## skill-summary-zh

将 Codex 技能列表中的英文说明蒸馏为一行简洁中文，区分相近技能的用途，保留原有名称、正文、调用规则和工具依赖。

- 安装/更新技能后检查新说明；也支持一次性检查已有技能。
- 每条说明至多 28 字符，保留必要的技术名词。
- 先预览、备份，再修改；逐项验证，并提供防覆盖的回滚。
- 区分“文件已修改”和“界面已刷新”，不靠修改应用数据库或目录缓存伪造完成状态。
- 脚本不调用模型、不联网、不读取账号或密钥；翻译计划由 Codex 根据技能内容生成。

### 安装

把 `skills/skill-summary-zh` 整个目录放入 Codex 的个人 skills 目录，例如 `~/.codex/skills/`。遇到同名技能先检查，勿覆盖已有修改。脚本需要 Python 3.10+ 和 PyYAML，建议在独立虚拟环境安装本仓库 `requirements.txt`。

对 Codex 说：

> 使用 skill-summary-zh，把刚安装技能的显示说明改成简洁中文，并逐项检查。

### 安装后自动使用

技能已声明安装/更新后的自动适用条件。要在本机稳定执行，可让 Codex 按 `references/installation-rule.md` 将规则追加到你授权的 AGENTS.md。之后 **Codex 代为安装或更新技能时** 会执行翻译步骤。

这不是后台监听器：通过其他程序安装技能后，仍需让 Codex 再运行一次检查。插件更新可能替换本地翻译；本技能不会自行改动插件市场目录或应用数据库。若旧说明留在界面缓存中，会明确报告尚未验证。

### 验证与回滚

```bash
python -m unittest discover -s tests -v
python skills/skill-summary-zh/scripts/localize.py scan --root /path/to/skills
python skills/skill-summary-zh/scripts/localize.py apply --plan plan.json --backup /path/to/new-backup --dry-run
python skills/skill-summary-zh/scripts/localize.py verify --plan plan.json
python skills/skill-summary-zh/scripts/localize.py restore --backup /path/to/backup --dry-run
```

本仓库不包含个人账号信息、机器路径、技能清单、密钥或其他项目的源码。欢迎通过问题单和拉取请求改进翻译质量与跨版本兼容性。
