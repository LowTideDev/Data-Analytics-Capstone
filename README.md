# Data Analytics Capstone

This repository stores a Steam games dataset split into multiple files along with reference documents from WGU.

The data is provided in 5 CSV chunks (`games_part_*.csv`) and 23 JSON pieces (`games_json_part_*.json`). You will need to combine these parts before analysis.

## Project Completion Plan

1. **Merge the datasets** – concatenate the CSV files into `games.csv` and merge the JSON pieces into `games.json`.
2. **Clean and transform** – parse dates, convert numerical fields, and handle missing values.
3. **Explore** – generate summary statistics and visualizations to understand distributions and correlations.
4. **Model** – build predictive or clustering models depending on your goals.
5. **Report results** – document your methodology and findings in a notebook or report.

For additional background, see the documents in the `docs/` folder.

## Example Starting Script

```bash
#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate
pip install pandas numpy matplotlib seaborn jupyterlab
python - <<'PY'
import pandas as pd, glob, json

csv_files = sorted(glob.glob('games_part_*.csv'))
df = pd.concat((pd.read_csv(f) for f in csv_files), ignore_index=True)
df.to_csv('games.csv', index=False)

json_files = sorted(glob.glob('games_json_part_*.json'))
merged = {}
for fp in json_files:
    with open(fp) as f:
        merged.update(json.load(f))
with open('games.json', 'w') as f:
    json.dump(merged, f)
PY
jupyter lab
```

This script installs common data-analysis packages, merges the dataset chunks, and launches Jupyter Lab for exploration. Adjust the steps as needed for your environment.
