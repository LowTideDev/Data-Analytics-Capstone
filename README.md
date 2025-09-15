# Data Analytics Capstone – Steam Games Market Analysis

## Project Summary
This repository houses the deliverables for a Western Governors University (WGU) data analytics capstone that explores Steam store metadata. The project investigates how factors such as genre, price, release timing, and player sentiment relate to estimated owner counts. The workstream includes cleaning and merging fragmented exports, performing exploratory and predictive analysis, and packaging insights for independent game developers.

## Dataset Source & License
- **Origin:** [Steam Store Games](https://www.kaggle.com/datasets/nikdavis/steam-store-games) dataset curated by Nik Davis on Kaggle.
- **License:** Creative Commons Zero v1.0 Universal (CC0 1.0). The dataset is redistributed here for educational purposes only.
- **Included files:** Five CSV segments named `games_part_*.csv` and 23 JSON fragments named `games_json_part_*.json`. Keep these pieces split inside the repository; merge them only in-memory within your analysis environment.

## Repository Structure
```
.
├── docs/                       # Background notes, setup guides, and project documentation
├── visualizations/             # Tableau workbooks and packaged dashboards
├── steam_analysis_cleaned.ipynb# Primary exploratory & modeling notebook
├── export_for_tableau.py       # Utility script for generating Tableau-ready extracts
├── task_2_report.md            # Final written report (Task 2 submission)
├── Task2 Report Template.docx  # Blank template provided by WGU
├── games_part_*.csv            # Tabular data split into manageable chunks
├── games_json_part_*.json      # Supplemental JSON attributes split by part
├── steam_cleaned_for_tableau.csv # Curated dataset exported for visualization tools
└── requirements.txt            # Python dependencies for replicating the analysis
```
Additional reference materials (feedback, rubrics, HTML exports) are stored at the repository root for completeness.

## Environment Setup
1. **Create and activate a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Launch Jupyter Lab or Notebook**
   ```bash
   jupyter lab   # or: jupyter notebook
   ```
4. **Load the dataset chunks in memory** (do not write merged files back to disk)
   ```python
   import pandas as pd, glob, json

   csv_parts = sorted(glob.glob("games_part_*.csv"))
   df = pd.concat((pd.read_csv(path) for path in csv_parts), ignore_index=True)

   json_parts = sorted(glob.glob("games_json_part_*.json"))
   json_records = {}
   for path in json_parts:
       with open(path) as f:
           json_records.update(json.load(f))
   ```

## Example Analysis Workflow
1. **Profiling:** Inspect column data types, summarize missingness, and standardize date and price formats.
2. **Feature engineering:** Derive indicators such as seasonal release windows, discounted price flags, and genre buckets.
3. **Exploratory analysis:** Generate descriptive statistics and visualizations (e.g., price vs. ownership scatterplots, genre heat maps).
4. **Modeling:** Train regression models to estimate owner counts and clustering algorithms to segment games by performance traits.
5. **Insight packaging:** Export cleaned tables with `export_for_tableau.py`, refresh Tableau dashboards in `visualizations/`, and document takeaways in the final report.

## Key Deliverables
- 📄 **Final Report:** [`task_2_report.md`](task_2_report.md) (Markdown summary of methodology and findings). A formatted HTML export is also available at [`Task 2 — D195 Data Analytics Capstone.html`](Task%202%20%E2%80%94%20D195%20Data%20Analytics%20Capstone.html).
- 📓 **Analysis Notebook:** [`steam_analysis_cleaned.ipynb`](steam_analysis_cleaned.ipynb) containing data preparation, exploratory analysis, and modeling steps.
- 📊 **Visualizations:** Tableau workbook at [`visualizations/gamesbyprice.twb`](visualizations/gamesbyprice.twb) with packaged dashboards derived from the curated dataset. Additional Tableau artifacts reside alongside it for version history.

For deeper background on project scope and environment recommendations, consult the documents in the [`docs/`](docs/README.md) directory.
