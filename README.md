## Project Summary

Steam Marketplace Performance Analytics is a Western Governors University Data Analytics capstone that investigates how pricing, release timing, and product positioning influence player adoption on Valve's Steam platform. The project combines exploratory data analysis, feature engineering, and predictive modeling to surface actionable insights for product and marketing stakeholders.

### Dataset Provenance

All gameplay and storefront metadata come from the Kaggle [**Steam Store Games**](https://www.kaggle.com/datasets/nikdavis/steam-store-games) dataset (Creative Commons CC0 1.0). The CSV and JSON partitions included here mirror the original files so peers can fully reproduce the cleaning and modeling pipeline while respecting Kaggle's redistribution terms.

## Repository Structure

```
.
├── docs/                        # Consolidated documentation moved out of the project root
│   ├── README.md                # Index of supporting guides
│   ├── analysis_guidelines.md   # Workflow reference for the capstone
│   ├── data_overview.md         # Data dictionary for CSV and JSON sources
│   ├── environment_setup.md     # Scripted environment bootstrap instructions
│   ├── final_report.md          # Submitted Task 2 report summarizing the analysis
│   └── setup_instructions.md    # Manual setup checklist
├── notebooks/
│   └── steam_analysis.ipynb     # Primary exploratory & modeling notebook
├── visualizations/
│   └── gamesbyprice.twb         # Tableau dashboard used in the submission
├── export_for_tableau.py        # Utility script for generating Tableau-ready extracts
├── games_part_*.csv             # Tabular data split into manageable chunks
├── games_json_part_*.json       # Supplemental JSON attributes split by part
├── steam_cleaned_for_tableau.csv # Curated dataset exported for visualization tools
└── requirements.txt             # Python dependencies for replicating the analysis
```
Supporting artifacts such as faculty feedback, rubric exports, and the HTML rendering of the final report remain at the root alongside the raw dataset partitions for archival completeness.

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
- 📄 **Final Report:** [`docs/final_report.md`](docs/final_report.md) (Markdown summary of methodology and findings). A formatted HTML export is also available at [`Task 2 — D195 Data Analytics Capstone.html`](Task%202%20%E2%80%94%20D195%20Data%20Analytics%20Capstone.html).
- 📓 **Analysis Notebook:** [`notebooks/steam_analysis.ipynb`](notebooks/steam_analysis.ipynb) containing data preparation, exploratory analysis, and modeling steps.
- 📊 **Visualizations:** Tableau workbook at [`visualizations/gamesbyprice.twb`](visualizations/gamesbyprice.twb) with packaged dashboards derived from the curated dataset. Additional Tableau artifacts reside alongside it for version history.

For deeper background on project scope and environment recommendations, consult the documents in the [`docs/`](docs/README.md) directory.

## Licensing
- **Code:** Released under the [MIT License](LICENSE). This applies to all scripts, notebooks, and other source code in the repository.
- **Data:** The Steam dataset is redistributed exactly as provided in Kaggle's [**Steam Store Games**](https://www.kaggle.com/datasets/nikdavis/steam-store-games) release and remains covered by the Creative Commons CC0 1.0 Universal dedication documented in [DATA_LICENSE](DATA_LICENSE).
