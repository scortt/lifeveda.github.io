---
layout: default
title: lifeveda.github.io
description: Project overview, structure plan, and publishing workflow for lifeveda.github.io.
---

# lifeveda.github.io

This repository powers **https://scortt.org**.

Current focus areas:

- Investing and price action analysis
- US / China stock notes
- Daily review pages (for example `MES/`)
- Selected history / gaming / learning notes

## Structure Plan (Current)

Use this layout going forward to keep new content organized:

- Root `*.md`
  - Evergreen pages and legacy single-page analyses
  - Examples: `PriceAction.md`, `AAPL.md`, `EIforP.md`
- `MES/`
  - Dated MES / ES daily reviews
- `ChinaStock/<ticker>/`
  - Dated Chinese stock analyses grouped by ticker
- `hottake/`
  - Short-form notes
- `_layouts/`, `_includes/`, `assets/`
  - Jekyll templates and shared assets

## Naming Conventions

- MES daily review: `MES/YYYYMMDD_daily.md`
  - Example: `MES/20260225_daily.md`
- China stock dated analysis: `ChinaStock/<ticker>/YYYYMMDD.md`
  - Example: `ChinaStock/000792/20260225.md`

## Publishing Workflow (Manual Navigation)

When publishing a new article:

1. Check new/modified files with `git status --short` and `git diff --name-status`.
2. Include required untracked article files and related assets in the commit.
3. Convert article content to bilingual Chinese-English format (CN/EN paired sections).
4. Update navigation pages:
   - `index.md` (`last_modified_at` + `Latest Updates`)
   - `PriceAction.md` for `MES/` daily reviews
   - `stock-analysis.md` and `stock-codes.md` for China stock entries
5. Verify `.md` links are published as `.html`.
6. Commit and push only intended files.

## Bilingual Content Standard

- Keep YAML front matter valid
- Keep links, code spans, and chart URLs intact
- Prefer embedded TradingView chart image + a clickable TradingView link
- Keep Chinese and English content aligned section-by-section

## Repository Hygiene

- Backup files stay local and should not be committed (for example `PriceActionbak`)
- Temporary noise is ignored via `.gitignore`
- Do not mix unrelated drafts into a publish commit

## Key Entry Points

- Site homepage: `index.md`
- Stock index: `stock-analysis.md`
- Ticker directory: `stock-codes.md`
- Jekyll config: `_config.yml`
