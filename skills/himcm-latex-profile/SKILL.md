---
name: himcm-latex-profile
description: Adapt an English MCM/ICM LaTeX paper to HiMCM rules and inspect solution-page limits, summary sheets, headers, anonymity and AI-report separation. Use for HiMCM formatting and submission preparation, with current official rules taking precedence over dated guidance.
---

# HiMCM English LaTeX profile

Read [the dated official-rule reference](references/himcm-2026.md) before applying this profile. Recheck the live official rules for the requested year. This is an independent instruction-only adaptation, not an official COMAP template or a bundled LaTeX implementation.

## Inputs and dependencies

Use an existing English MCM/ICM LaTeX project as the base. If the separately installed [mathmodel-latex-skill](https://github.com/wangling-miao/mathmodel-latex-skill) is available, its `templates/mcm-icm/` provides that base. Its CUMCM templates are not used for this workflow. Upstream scripts and templates are not redistributed here: the upstream repository did not provide a repository license when checked on 2026-10-24. Obtain and assess upstream resources independently. This profile also works with another user-supplied English project and equivalent PDF inspection tools.

## Workflow

1. Identify contest year, problem and team control number. Use placeholders when unknown. HiMCM 2026 has problems A/B; do not inherit MCM/ICM A–F.
2. Inspect the current official Summary Sheet and adapt the English project to it. Use at least 12-point readable type and US Letter or A4. Put team number and page number at the top of every solution page, including page one. Do not retain MCM/ICM branding on a HiMCM sheet.
3. Keep Summary, TOC, complete solution, references, letters and ordinary appendices in a solution-only `main.pdf`. Make any AI-use report separately, then append it to the checked solution. No separate decorative cover.
4. Check references and cross-references, compile the project with its existing toolchain, render and inspect every page. Fix clipped equations, tables, awkward breaks and unreadable figures. Do not reduce type below the minimum to fit the page budget. Confirm actual assumptions and limitations; invent no evidence or citations.
5. If using the separately installed upstream checker, run from its root:

   ```bash
   python scripts/check_pdf.py <project>/main.pdf --max-pages 25 --max-size-mb 20
   ```

   Its page limit has no default, so always supply `--max-pages 25` for the solution. With another checker, enforce the equivalent explicit limit. Do not apply the 25-page cap to an AI-inclusive total. For an already merged file, verify the actual report boundary and check the entire preceding solution, never an arbitrary first-25-page slice.
6. Merge the actual AI disclosure after the solution. Check final `<control-number>.pdf` is strictly below 20,000,000 bytes as a conservative local size gate; upstream's `--max-size-mb 20` alone measures MiB and permits equality. Inspect anonymity and metadata in the entire file. Treat keyword hits as review items and suppress only verified false positives.
7. Report solution-page count, total-file size, compilation/visual checks performed, official sources and remaining gaps. Freeze edits at the official work deadline. Submission or public sharing is a separate authorized action.

## Verification limits

A page-count/keyword script cannot prove font size, header placement, official Summary Sheet fidelity, complete anonymity, or AI-report boundaries. Use a real PDF parser or Poppler for final count and manual rendering for layout. This profile was validated as instructions; it has not been demonstrated on a compiled HiMCM paper. The official Summary Sheet DOCX still requires inspection when generating the project.
