# Usage Guide

This guide shows how to set up a local Python environment, install the project dependencies, and load the dataset for analysis.

## 1. Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Install dependencies
Install the required packages using the provided `requirements.txt` file:
```bash
pip install -r requirements.txt
```

## 3. Launch Jupyter
Once the dependencies are installed, start Jupyter to work with the notebooks:
```bash
jupyter lab  # or: jupyter notebook
```

## 4. Load the dataset chunks in memory
Within your notebook or a Python shell, read the CSV and JSON files without writing a new combined file:
```python
import pandas as pd
import json, glob

csv_parts = sorted(glob.glob('games_part_*.csv'))
df = pd.concat((pd.read_csv(fp) for fp in csv_parts), ignore_index=True)

json_parts = sorted(glob.glob('games_json_part_*.json'))
all_json = {}
for fp in json_parts:
    with open(fp) as f:
        all_json.update(json.load(f))
```
The variable `df` holds the merged CSV data and `all_json` contains the JSON records. Both are kept only in memory so the repository stays small.
