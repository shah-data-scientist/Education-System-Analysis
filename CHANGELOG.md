# Changelog

All notable changes to this project will be documented in this file.

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Changed
- Renamed project from **Education System Analysis** to **Education Market Opportunity Model**
- Renamed GitHub repository to `Education-Market-Opportunity-Model`
- Renamed local project folder accordingly
- Updated `pyproject.toml` package name and description
- Updated `README.md` title and description to reflect new name

## [2026-05-17] — Reviewed before portfolio creation v1

### Added
- Split monolithic notebook into 3 focused notebooks: `01_data_loading`, `02_processing`, `03_scoring_results`
- `pyproject.toml`, `poetry.lock`, `requirements.txt` for reproducible environment
- `pyarrow` dependency for inter-notebook parquet data transfer
- `reports/Academy_International_Market_Analysis.pptx` — renamed and relocated from `outputs/`
- Comprehensive `README.md` with full methodology, indicators, scoring formula, and top 20 results
- `data/processed/` excluded via `.gitignore` (generated parquet intermediates)

### Changed
- Moved `Indicators.xlsx` from `data/` to `outputs/` (it is a curated input, not raw data)
- Notebook TOC added; fragmented code cells merged; duplicate filter lines removed

### Removed
- Old notebooks: `notebooks/OLD/` folder, `Project 2 FINAL.ipynb`, `Untitled.ipynb`
- Redundant outputs: generated CSVs, `desktop.ini`, `environment.yaml`, `REX.docx`, `outputs/P2+...pdf`
- `.to_csv()` save calls for intermediate outputs that were not consumed downstream

## [2026-02-11] — Audit cleanup and refactoring

### Removed
- Unused data files: `EdStatsFootNote.csv`, `EdStatsCountrySeries.csv`, `EdStatsCountry.csv`
- Unused output files: `choice and conso of indicators.xlsx`, `corr_flat_table.csv`, `missing_matrix.png`
- Backup notebook `Education_System_Analysis_backup.ipynb`
- Dead code cells: `!pip install pycountry`, loads of 3 unused CSVs and their markdown descriptions
- Redundant CSV reload (`indicator_data_original`) — reuses existing `indicator_data` variable

### Changed
- Vectorized imputation loop (row-wise interpolate/ffill/bfill instead of groupby iteration)
- Simplified year-filtering logic (direct column selection instead of multi-step drop/add)
- Updated Data Overview markdown to reflect 2 tables instead of 5
- Renumbered data section headings after removing 3 unused datasets

### Added
- Initial project setup with notebooks, data files, and outputs
- `.gitignore` configured per GLOBAL_POLICY.md (excludes large CSVs, checkpoints, Python artifacts)
- `CHANGELOG.md` and `PROJECT_MEMORY.md` created per GLOBAL_POLICY.md
