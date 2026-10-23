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

## workflow-to-skill

将已验证、值得复用的工作流蒸馏为 Codex 技能，检查后发布到用户指定的仓库。包含简洁中文技能说明和对应中英文文档；保留现有本地修改与远端更新，过滤个人资料和密钥。

可在完成实用工作流后调用 `$workflow-to-skill`；若希望后续自动整理发布，可在本机指引中给予持续授权。它只在智能体工作期间执行，不是后台发布程序。

## statistical-modeling-report

适用于已提供的Excel/CSV课程或建模数据：单因素方差分析与校正后的事后比较、卡方独立性检验、K-means聚类和PCA降维。按请求输出统计判断、中文或用户指定语言的图表，以及检查图片链接的Markdown报告。保留原始数据，明确K选择指标冲突、教师标签排除、不确定性和非因果解释。

这是指令型工作流，不是固定数据计算器，也不自带绘图库；不覆盖时间趋势回归或监督分类。只执行请求的阶段，“学习数据”不等于运行全部模型。Python实现通常需要在隔离环境提供pandas、openpyxl、NumPy、SciPy、statsmodels、scikit-learn和Matplotlib；使用可用科研绘图技能时，遵循其独立的绘制与质检要求。

将`skills/statistical-modeling-report`复制到个人技能目录，保留已有同名修改。示例：“使用 $statistical-modeling-report 分析这些Excel工作表，把计算结果与图片整理到Markdown报告。”可携带报告需同时包含图片资源；链接存在不等于渲染已通过目视检查。


## himcm-latex-profile

[中文说明](skills/himcm-latex-profile/README.zh-CN.md) · [English documentation](skills/himcm-latex-profile/README.md)

基于已有MCM/ICM英文项目适配HiMCM，显式检查25页解答上限和另附AI报告。仅含指令，不转载第三方模板或脚本，实际论文仍需编译和逐页检查。
