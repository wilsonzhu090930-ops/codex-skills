# HiMCM LaTeX profile

English · [简体中文](README.zh-CN.md)

An instruction-only skill for adapting an existing English MCM/ICM LaTeX project to HiMCM: Summary Sheet, readable 12-point type, headers, anonymity, a 25-page solution gate and an appended AI-use report. Official rules override the dated 2026 reference.

Copy this folder into your agent's skills directory. Supply an English LaTeX project and a working compiler/PDF inspection toolchain. Optionally use the separately installed [mathmodel-latex-skill](https://github.com/wangling-miao/mathmodel-latex-skill). No upstream templates or scripts are redistributed; its repository license was absent when checked. This independent profile is not endorsed by COMAP.

Example: “Use himcm-latex-profile to adapt my English paper to the current HiMCM rules and check the solution PDF with an explicit 25-page limit.”

The AI report is exempt from the solution limit, but remains in the final single PDF. The profile checks instructions and workflow; compilation and all-page visual verification are still required on each real paper. No compiled HiMCM demonstration or exact official Summary Sheet rendering has been verified for this release.
