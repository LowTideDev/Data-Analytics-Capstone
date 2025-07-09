# Environment Setup

This repository has no code or requirements yet. Below is a sample setup script to create a Python virtual environment, install common data‑analysis packages, and merge the dataset pieces.

```bash
#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate

pip install pandas numpy matplotlib seaborn jupyterlab

python - <<'PY'
import pandas as pd, glob, json

csv_files = sorted(glob.glob('games_part_*.csv'))
if csv_files:
    df = pd.concat((pd.read_csv(f) for f in csv_files), ignore_index=True)
    df.to_csv('games.csv', index=False)

json_files = sorted(glob.glob('games_json_part_*.json'))
merged = {}
for fp in json_files:
    with open(fp) as f:
        merged.update(json.load(f))
if merged:
    with open('games.json', 'w') as f:
        json.dump(merged, f)
PY

jupyter lab
```

This script mirrors the original assistant response and can be adjusted as needed.
