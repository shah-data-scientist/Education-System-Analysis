# Changelog

All notable changes to this project will be documented in this file.

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

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
