import pandas as pd
import json, glob, re

# --- Load CSV Parts ---
csv_parts = sorted(glob.glob('games_part_*.csv'), key=lambda f: int(re.search(r'\d+', f).group()))
df = pd.concat((pd.read_csv(f) for f in csv_parts), ignore_index=True)

# Normalize column names (lowercase, snake_case)
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

# --- Load JSON Records (optional enrichment) ---
records = {}
json_parts = sorted(glob.glob('games_json_part_*.json'), key=lambda f: int(re.search(r'\d+', f).group()))
for fp in json_parts:
    with open(fp) as f:
        records.update(json.load(f))

def parse_owner_range(r):
    if pd.isnull(r): return None
    # If already a number (int or float), return as int
    if isinstance(r, (int, float)):
        return int(r)
    # Now, handle as string
    r_str = str(r).replace(",", "")
    # Match ranges like "10000 - 20000", "10000 .. 20000", etc.
    match = re.match(r'(\d+)\s*[\-–.]+\s*(\d+)', r_str)
    if match:
        low, high = map(int, match.groups())
        return (low + high) // 2
    # Try just parsing as a single integer string
    try:
        return int(r_str)
    except:
        return None

df['estimated_owners_mid'] = df['estimated_owners'].apply(parse_owner_range)

# --- Parse release_date as datetime ---
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
df = df[df['release_date'].notnull()]  # Only drop *truly* missing dates

# --- Feature Engineering ---
df['release_year'] = df['release_date'].dt.year
df['release_month'] = df['release_date'].dt.month
df['release_quarter'] = df['release_date'].dt.to_period('Q').astype(str)
df['total_reviews'] = df[['positive', 'negative']].sum(axis=1)
df['review_ratio'] = df['positive'] / df['total_reviews'].replace(0, pd.NA)
df['main_genre'] = df['genres'].fillna('').str.split(',').str[0].str.strip()

# --- Optional: Add Metacritic from JSON if available ---
df['metacritic'] = df['appid'].map(lambda x: records.get(str(x), {}).get('metacritic'))

# --- Only drop totally broken/meaningless records ---
df = df[df['price'] >= 0]  # Negative prices are nonsense

# --- Final selection of columns for Tableau ---
columns_to_keep = [
    'appid', 'name', 'price', 'release_date',
    'release_year', 'release_month', 'release_quarter',
    'estimated_owners', 'estimated_owners_mid', 'positive', 'negative',
    'total_reviews', 'review_ratio', 'main_genre', 'genres', 'metacritic'
]
df_out = df[columns_to_keep]

# --- Export ---
df_out.to_csv("steam_cleaned_for_tableau.csv", index=False)
print("Exported: steam_cleaned_for_tableau.csv")
