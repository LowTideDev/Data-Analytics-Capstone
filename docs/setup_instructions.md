# Setup Instructions

This project provides chunked CSV and JSON files. When you are ready to analyze the data, follow these high-level steps:

1. Create a Python virtual environment (`python3 -m venv .venv` and `source .venv/bin/activate`).
2. Install common data libraries such as `pandas`, `numpy`, `matplotlib`, and `seaborn`.
3. Read all `data/raw/games_part_*.csv` files with pandas and concatenate them into a single DataFrame in memory. Similarly combine the `data/raw/games_json_part_*.json` files using `json` or pandas. Do not create a large combined file in the repository.
4. Use JupyterLab or your preferred IDE to explore the in-memory DataFrame and dictionary.

These instructions mirror the earlier setup script but avoid executing commands automatically. Adjust the steps to suit your environment.
