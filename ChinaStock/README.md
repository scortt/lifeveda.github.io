---
layout: default
title: ChinaStock Directory Notes
description: Maintenance notes for dated Chinese stock analysis pages.
---

# ChinaStock Directory Notes

This folder stores Chinese stock analyses in ticker subdirectories.

## Directory Structure

- `ChinaStock/<ticker>/YYYYMMDD.md`
- Example: `ChinaStock/000792/20260225.md`

## Article Format

- Use YAML front matter
- Prefer bilingual Chinese-English article content
- Prefer embedded TradingView chart image + clickable TradingView link
- Keep links and ticker/date naming consistent

## Navigation Updates

When adding a new China stock article, also update:

- `../index.md` (`Latest Updates`)
- `../stock-analysis.md` (`Chinese Stocks`)
- `../stock-codes.md` (ticker table + latest updates list)
