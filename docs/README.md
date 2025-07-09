# DAC Dataset Repository

This repository contains chunked CSV and JSON files for a Steam games dataset as well as reference documents.

The dataset is divided into multiple parts to keep file sizes manageable (approx. 1 GB total).

## Folder Structure
- `games_part_*.csv` – five CSV chunks with detailed metadata about each game.
- `games_json_part_*.json` – 23 JSON chunks containing similar information keyed by app ID.
- `.docx` and `.html` files – capstone references and forms from WGU.

1. **Combine the dataset** – merge the CSV parts into `games.csv` and the JSON parts into `games.json`.
2. **Clean the data** – parse numerical fields, convert dates, and normalize text.
3. **Explore and analyze** – perform any statistical or machine‑learning tasks required by your project.

See `docs/setup_instructions.md` for setup guidance.
The repository's top-level `README.md` also outlines a quick plan and example
script for getting started.



