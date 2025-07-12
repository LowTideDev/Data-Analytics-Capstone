# Analysis Guidelines

The goal of the capstone is to explore the Steam games data and produce meaningful insights. Here is a high‑level workflow:

1. **Ingest** – Use the steps from `setup_instructions.md` to load the chunked dataset into an in-memory DataFrame (and dictionary for the JSON). Avoid creating consolidated files in the repo.
2. **Clean** – Handle missing values, parse numbers from strings (e.g., owner ranges), and convert dates with `pd.to_datetime`.
3. **Enrich** – Engineer features such as release year, price tiers, or review ratios.
4. **Visualize** – Create histograms, bar charts, and correlation plots using `matplotlib` or `seaborn`.
5. **Model** – Depending on your objectives, you may build clustering models, price predictors, or simple recommender systems.
6. **Report** – Summarize findings in a notebook or PDF and link the methods back to the WGU capstone requirements.

Feel free to extend these steps as your project evolves.
