# Project Memory - Education Market Opportunity Model

## Project Overview
- **Type:** Data Science / EDA + Scoring project (Open Classrooms - Projet 2)
- **Data Source:** World Bank EdStats dataset
- **Policy:** Follows GLOBAL_POLICY.md v1.16 from `C:\Users\shahu\Documents\coding_agent_policies\`
- **Created:** 2026-02-11

## Project Names
- **Current name:** Education Market Opportunity Model
- **GitHub repo:** Education-Market-Opportunity-Model
- **Previous name:** Education System Analysis (renamed 2026-05-18)

## Key Files
- `notebooks/01_data_loading.ipynb` — Data loading, country/year filtering, saves parquets
- `notebooks/02_processing.ipynb` — Merge, fill rate, trends, correlation analysis, saves consolidated table
- `notebooks/03_scoring_results.ipynb` — Imputation, scoring, top 20 results
- `data/EdStatsData.csv` — Primary dataset (312 MB, excluded from git)
- `outputs/Indicators.xlsx` — Manually curated indicator selection (required input)
- `reports/Academy_International_Market_Analysis.pptx` — Presentation deck

## Recent Changes

### 2026-05-18 - Project rename
- Renamed from Education System Analysis to Education Market Opportunity Model
- GitHub repo renamed to Education-Market-Opportunity-Model
- Monolithic notebook renamed to Education_Market_Opportunity_Model.ipynb

### 2026-05-17 - Portfolio preparation
- Split monolithic notebook into 3 focused notebooks (pipeline approach)
- Added pyproject.toml, poetry.lock, requirements.txt
- Added comprehensive README with full methodology
- Cleaned up outputs, removed old notebooks and generated files
- Moved Indicators.xlsx to outputs/, renamed presentation to reports/

### 2026-02-11 - Audit cleanup and refactoring
- Removed unused data files (EdStatsFootNote, EdStatsCountrySeries, EdStatsCountry)
- Vectorized imputation, simplified year filtering, eliminated redundant CSV reload
- Notebook: 41 cells (down from 53), all outputs verified identical

### 2026-02-11 - Project setup and policy enforcement
- Initialized git repository and pushed to GitHub
- Created `.gitignore` (excludes large CSVs, checkpoints, Python artifacts)
- Created `CHANGELOG.md` and `PROJECT_MEMORY.md` per GLOBAL_POLICY.md
