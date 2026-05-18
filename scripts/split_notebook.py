"""Split Education_Market_Opportunity_Model.ipynb into three focused notebooks."""
import json
import uuid
import copy
import os

NB_PATH = r"c:\Users\shahu\Documents\OneDrive\OPEN CLASSROOMS\PROJET 2\Education Market Opportunity Model\notebooks\Education_Market_Opportunity_Model.ipynb"
OUT_DIR = r"c:\Users\shahu\Documents\OneDrive\OPEN CLASSROOMS\PROJET 2\Education Market Opportunity Model\notebooks"
DATA_DIR = r"c:\Users\shahu\Documents\OneDrive\OPEN CLASSROOMS\PROJET 2\Education Market Opportunity Model\data"

with open(NB_PATH) as f:
    nb = json.load(f)

src_cells = nb["cells"]


# â”€â”€ helpers â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

def uid():
    return str(uuid.uuid4())[:8]

def code_cell(source):
    return {"cell_type": "code", "execution_count": None,
            "id": uid(), "metadata": {}, "outputs": [],
            "source": source}

def md_cell(source):
    return {"cell_type": "markdown", "id": uid(),
            "metadata": {}, "source": source}

def clean(cell):
    """Deep-copy a cell and strip outputs."""
    c = copy.deepcopy(cell)
    if c["cell_type"] == "code":
        c["outputs"] = []
        c["execution_count"] = None
    return c

def notebook(cells):
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Education System Analysis",
                "language": "python",
                "name": "education-system-analysis",
            },
            "language_info": {"name": "python", "version": "3.11.9"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


# â”€â”€ shared setup code â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

SETUP = """\
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
import pycountry
import os

pd.set_option('display.max_columns', None)

# Find data directory (works from project root or notebooks/)
if os.path.isdir('data'):
    drive_data_path = os.path.abspath('data')
elif os.path.isdir('../data'):
    drive_data_path = os.path.abspath('../data')
else:
    raise FileNotFoundError('Cannot find data directory')

outputs_path = os.path.join(os.path.dirname(drive_data_path), 'outputs')
processed_path = os.path.join(drive_data_path, 'processed')
os.makedirs(processed_path, exist_ok=True)

os.chdir(drive_data_path)\
"""


# â”€â”€ Notebook 1: Data Loading & Preprocessing â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# Source cells 0-15  (imports â†’ year range filtering)
# Cell index map (41-cell notebook):
#  0  code  imports+setup   â†’ replaced by SETUP
#  1  md    Project Context â†’ kept
#  2  md    TOC             â†’ skipped (per-notebook intro replaces it)
#  3  md    Data Overview
#  4  md    Indicator Data section
#  5  code  load EdStatsSeries
#  6  code  keep relevant columns
#  7  md    Indicator Selection
#  8  code  filter indicator_data by codes_to_keep
#  9  md    Indicator Values section
# 10  code  load EdStatsData
# 11  md    Country Filtering
# 12  code  country filter code
# 13  code  missing values plot
# 14  md    Year Range Filtering
# 15  code  keep 2010-2024

nb1 = []
nb1.append(md_cell(
    "# Notebook 1 â€” Data Loading & Preprocessing\n\n"
    "Loads the raw World Bank EdStats data, filters to valid ISO countries "
    "and the 2010â€“2024 window, and saves cleaned datasets for the next notebook.\n\n"
    "**Outputs saved to `data/processed/`:**\n"
    "- `indicator_data.parquet`\n"
    "- `indicator_values.parquet`"
))
nb1.append(code_cell(SETUP))

# Project Context (cell 1), then cells 3-15 (skip the old TOC at index 2)
nb1.append(clean(src_cells[1]))
for i in range(3, 16):
    nb1.append(clean(src_cells[i]))

# Save step
nb1.append(md_cell("## Save Processed Data\n\nPersist cleaned datasets to `data/processed/` for Notebook 2."))
nb1.append(code_cell(
    "indicator_data.to_parquet(os.path.join(processed_path, 'indicator_data.parquet'), index=False)\n"
    "indicator_values.to_parquet(os.path.join(processed_path, 'indicator_values.parquet'), index=False)\n"
    "print('Saved indicator_data and indicator_values to data/processed/')"
))

with open(os.path.join(OUT_DIR, "01_data_loading.ipynb"), "w") as f:
    json.dump(notebook(nb1), f, indent=1)
print("Written 01_data_loading.ipynb")


# â”€â”€ Notebook 2: Processing & Analysis â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# Source cells 16-27  (merge â†’ correlation flatten+enrich)
# 16  md   Analysis of Consolidated Data
# 17  md   Processing 3: Merge
# 18  code merge
# 19  md   Processing 4: Fill Rate
# 20  code fill rate
# 21  code indicator selection
# 22  md   Processing 5: Trend Visualisation
# 23  code melt + groupby
# 24  code plot function + loop
# 25  md   Processing 6: Correlation
# 26  code correlation matrix
# 27  code flatten + enrich

nb2 = []
nb2.append(md_cell(
    "# Notebook 2 â€” Processing & Analysis\n\n"
    "Merges the cleaned datasets, evaluates indicator fill rates, "
    "visualises trends, and performs correlation analysis to remove redundant indicators.\n\n"
    "**Input:** `data/processed/indicator_data.parquet`, `data/processed/indicator_values.parquet`  \n"
    "**Output saved to `data/processed/`:** `consolidated_table.parquet`"
))
nb2.append(code_cell(SETUP))
nb2.append(code_cell(
    "# Load processed data from Notebook 1\n"
    "indicator_data = pd.read_parquet(os.path.join(processed_path, 'indicator_data.parquet'))\n"
    "indicator_values = pd.read_parquet(os.path.join(processed_path, 'indicator_values.parquet'))\n"
    "print(f'indicator_data: {indicator_data.shape}')\n"
    "print(f'indicator_values: {indicator_values.shape}')"
))

for i in range(16, 28):
    nb2.append(clean(src_cells[i]))

# Save step
nb2.append(md_cell("## Save Consolidated Table\n\nPersist the processed table to `data/processed/` for Notebook 3."))
nb2.append(code_cell(
    "consolidated_table.to_parquet(os.path.join(processed_path, 'consolidated_table.parquet'), index=False)\n"
    "print('Saved consolidated_table to data/processed/')"
))

with open(os.path.join(OUT_DIR, "02_processing.ipynb"), "w") as f:
    json.dump(notebook(nb2), f, indent=1)
print("Written 02_processing.ipynb")


# â”€â”€ Notebook 3: Scoring & Results â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# Source cells 28-40  (remove redundants â†’ conclusion)
# 28  code remove redundant indicators
# 29  md   Processing 7: Missing Value Treatment
# 30  code imputation (before/after msno + head)
# 31  md   Processing 8: Reshape
# 32  code melt + pivot
# 33  code missing values check reshaped
# 34  md   Processing 9: Education Potential Score
# 35  code score computation + dropna  â† starts with sklearn import â†’ strip it
# 36  md   Processing 10: Top 20 Countries
# 37  code bar chart
# 38  code line chart
# 39  code stacked area chart
# 40  md   Conclusion

nb3 = []
nb3.append(md_cell(
    "# Notebook 3 â€” Scoring & Results\n\n"
    "Imputes missing values, reshapes data, computes the composite "
    "Education Potential Score (0â€“100) for each country, and identifies "
    "the top 20 markets for Academy's expansion.\n\n"
    "**Input:** `data/processed/consolidated_table.parquet`"
))
nb3.append(code_cell(SETUP + "\nfrom sklearn.preprocessing import MinMaxScaler"))
nb3.append(code_cell(
    "# Load consolidated table from Notebook 2\n"
    "consolidated_table = pd.read_parquet(os.path.join(processed_path, 'consolidated_table.parquet'))\n"
    "print(f'consolidated_table: {consolidated_table.shape}')\n"
    "consolidated_table.head()"
))

for i in range(28, 41):
    c = clean(src_cells[i])
    # Remove the duplicate sklearn import from the score cell (now in setup)
    if c["cell_type"] == "code":
        src = "".join(c["source"])
        if src.lstrip().startswith("from sklearn.preprocessing import MinMaxScaler"):
            lines = src.split("\n")
            lines = [l for l in lines if l.strip() != "from sklearn.preprocessing import MinMaxScaler"]
            while lines and not lines[0].strip():
                lines.pop(0)
            c["source"] = "\n".join(lines)
    nb3.append(c)

with open(os.path.join(OUT_DIR, "03_scoring_results.ipynb"), "w") as f:
    json.dump(notebook(nb3), f, indent=1)
print("Written 03_scoring_results.ipynb")


# â”€â”€ Create processed/ directory â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
os.makedirs(os.path.join(DATA_DIR, "processed"), exist_ok=True)
print("Created data/processed/")
print("\nDone. Run the notebooks in order: 01 â†’ 02 â†’ 03")
