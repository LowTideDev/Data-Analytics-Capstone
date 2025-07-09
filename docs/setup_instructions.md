# Setup Instructions

This project provides chunked CSV and JSON files. When you are ready to analyze the data, follow these high-level steps:

1. Create a Python virtual environment (`python3 -m venv .venv` and `source .venv/bin/activate`).
2. Install common data libraries such as `pandas`, `numpy`, `matplotlib`, and `seaborn`.
3. Combine all `games_part_*.csv` files into a single `games.csv` and merge the
   `games_json_part_*.json` files into `games.json`. Keep these merged files
   locally in a folder listed in `.gitignore` (for example `output/`) and do not
   commit them to GitHub due to their size. If you prefer, you may merge the
   parts directly into a `pandas` DataFrame without writing to disk.
4. Use JupyterLab or your preferred IDE to explore the consolidated data.

These instructions mirror the earlier setup script but avoid executing commands automatically. Adjust the steps to suit your environment.
