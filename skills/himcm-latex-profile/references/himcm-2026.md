# HiMCM 2026 rules and English-template adaptation

Verified online 2026-10-23. Recheck before final submission and after official updates. Current-year live rules take precedence over older tips or community templates.

## Official sources

- [2026 Rules and Instructions](https://contest.comap.com/highschool/contests/himcm/instructions.html), sections IV and VI: solution preparation and submission.
- [Procedures and Tips](https://contest.comap.com/highschool/contests/himcm/flyers/HiMCM-MidMCM_TipsArticle.pdf), V20251027, pages 5–6: format and page size. Older administrative details can differ from live 2026 rules.
- [AI Policy](https://contest.comap.com/undergraduate/contests/mcm/flyer/Contest_AI_Policy.pdf), v102025, linked from the HiMCM rules.
- [Official Summary Sheet DOCX](https://contest.comap.com/highschool/contests/himcm/flyers/HiMCM_Summary.docx), linked by the rules. Download and inspect its actual fields at template-generation time. The rule audit did not render this DOCX; exact field arrangement is not yet verified. Never describe the MCM template sheet as official HiMCM formatting.

## Apply these rules

| Requirement | Implementation |
| --- | --- |
| English, readable font at least 12 pt including summary; US Letter or A4 | Explicitly configure font and page size; check actual output. Avoid small captions, references, table text and header defaults. |
| Summary Sheet first, then up to 24 solution pages | Adapt English MCM/ICM base; no separate decorative cover. HiMCM problems are A or B, not MCM/ICM A–F. |
| 25-page limit includes Summary, TOC, references, notes, letters/memos and ordinary appendices | Check the entire solution-only `main.pdf` with `--max-pages 25`. A TOC is encouraged and counts. No required minimum length. |
| AI report appended after solution; unlimited and excluded | Build separately and append afterwards. Never relocate substantive results or ordinary appendices into the exemption. |
| Team control number and page number at top of every solution page | Inspect first-page styles, landscape and appendix pages. Keep consistent headers in AI report as a local convention. |
| No student, advisor, institution or identifying details other than control number | Inspect text, letters, acknowledgements, graphics and PDF metadata. Distinguish cited institutions from team identity. |
| Single PDF named with control number, less than 20MB | Final `<control-number>.pdf`; strictly below 20,000,000 bytes as conservative implementation. No separate programs, databases or software submissions. |

Margins, Times New Roman, exact section ordering, keyword count and three-line tables are design choices, not official requirements in these sources. Present clear assumptions with justifications, model construction and tests, results, relevant sensitivity analysis, strengths and weaknesses, conclusions and sources. Do not hide material weaknesses for persuasive effect. Render and inspect all pages; script success alone is insufficient.

## Build and check

Use `templates/mcm-icm/` and its local build configuration. Run environment check with `--contest mcm-icm --use-ref-bib`; this selects the available English toolchain, not MCM contest rules. Run citation/cross-reference checks, compile, then visually inspect.

The script's page-limit default is None. Therefore a bare `check_pdf.py main.pdf` does not enforce any page cap. Explicitly run:

```bash
python scripts/check_pdf.py main.pdf --max-pages 25 --max-size-mb 20
```

This `main.pdf` is the solution only. Preserve it as the auditable page-count artifact. Merge the AI report after the verified solution and inspect the merged file for byte size, order, anonymity and readability; do not impose 25 pages on the AI-inclusive total. The checker uses a broad identity keyword scan: manually review hits and PDF metadata. Use a real PDF parser or Poppler for final page count rather than relying on the regex fallback.

## AI disclosure

The linked policy covers language polishing, translation, coding assistance, auto-completion and embedded AI, as well as other AI use. Disclose actual models/tools and purposes inline and in the solution references, and append `Report on Use of AI Tools`. Record version/date where known and human verification. Keep accurate usage logs; never reconstruct fictional prompts or outputs.

Policy examples show exact queries and complete outputs for conversational tools, a translation-use statement without full input query for translation, and a description of code auto-completion. Follow the actual use case and current policy. Verify generated material and citations; preserve human responsibility for reasoning and conclusions.

## Contest boundaries

Window: November 4, 2026 15:00 EST through November 17 20:00 EST. Submission due November 17 21:00 EST. Asia/Shanghai equivalents: November 5 04:00, November 18 09:00 and November 18 10:00 respectively. Freeze edits at the work deadline; the extra submission hour is not editing time.

During the contest, no human assistance from outside the team and no posting/sharing problems or partial/complete work. Follow the AI disclosure policy for AI assistance. This skill does not authorize public uploads, messages or automatic submission.

## 本地适配说明

以 MCM/ICM 英文模板为基础，按 HiMCM 当年规则适配摘要页、12磅字体、页眉和匿名。解答PDF显式检查25页；AI报告另附并排除计页，合并后检查最终体积和完整性。中文CUMCM模板不用于此流程。
