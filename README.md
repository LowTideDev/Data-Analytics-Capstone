# Data Analytics Capstone

This repository stores a Steam games dataset split into multiple files along with reference documents from WGU.

## Usage

### 1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

Install the required packages using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 3. Launch Jupyter

Once the dependencies are installed, start Jupyter to work with the notebooks:

```bash
jupyter lab  # or: jupyter notebook
```

### 4. Load the dataset chunks in memory

Within your notebook or a Python shell, read the CSV and JSON files without writing a new combined file to disk:

```python
import glob
import json
import pandas as pd

csv_parts = sorted(glob.glob('games_part_*.csv'))
df = pd.concat((pd.read_csv(fp) for fp in csv_parts), ignore_index=True)

json_parts = sorted(glob.glob('games_json_part_*.json'))
all_json = {}
for fp in json_parts:
    with open(fp) as f:
        all_json.update(json.load(f))
```

The variable `df` holds the merged CSV data and `all_json` contains the JSON records. Both structures stay in memory so the repository remains small.

## Dataset Contents

The data is provided in 5 CSV chunks (`games_part_*.csv`) and 23 JSON pieces (`games_json_part_*.json`). Merge these pieces only within your analysis environment (for example, using pandas) so that no large combined file needs to be committed to the repo.
The raw data originates from the public Kaggle dataset "Steam Store Games" (https://www.kaggle.com/datasets/nikdavis/steam-store-games) released under the CC0 1.0 license. It is provided here solely for educational use.

## Project Completion Plan

1. **Load the datasets in memory** – use pandas to concatenate the CSV parts and combine the JSON pieces inside your analysis environment. Avoid writing a single large file back into the repository.
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
# work with `df` directly; avoid writing a large combined CSV to disk

json_files = sorted(glob.glob('games_json_part_*.json'))
merged = {}
for fp in json_files:
    with open(fp) as f:
        merged.update(json.load(f))
# `merged` now holds all JSON records in memory
PY
jupyter lab
```

This script installs common data-analysis packages, loads the dataset chunks into memory, and launches Jupyter Lab for exploration. Adjust the steps as needed for your environment.
