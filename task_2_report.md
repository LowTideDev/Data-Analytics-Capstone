# Task 2 Project Report — Steam Games Analysis

## A. Proposal Overview

### A1. Research Question or Organizational Need
What factors—such as genre, price, and release timing—correlate with higher owner estimates for Steam games?

### A2. Problem Statement
Indie game developers face uncertainty in pricing, genre selection, and release timing. Without data-driven guidance, launching a commercially successful game is difficult.

### A3. Literature Review
- Cite 3 relevant industry or academic sources on game marketing, pricing psychology, or seasonal trends.
- Focus on Steam-specific developer strategies or statistical trends in game sales if available.

### A4. Proposed Solution
Conduct a regression and clustering analysis on Steam game metadata to identify variables most strongly correlated with owner estimates.

### A5. Expected Outcomes
- Clean dataset and summary statistics.
- Predictive model using linear regression.
- Game classification by ownership tiers using clustering.
- Actionable genre/price/timing guidance for indie devs.

---

## B. Project Justification (Management Perspective)

### B1. Stakeholders
Indie game developers, publishers, marketing consultants.

### B2. Business Need
Data-backed decisions can reduce launch risks, improve visibility, and optimize revenue.

### B3. Intended Use
Provide a visual and statistical playbook: when and how to release games for maximum reach.

### B4. Project Deliverables
- Clean dataset
- Regression and clustering outputs
- 2–3 core visualizations
- Recommendation summary for indie devs

### B5. Limitations
- Dataset is historical and may not capture new trends or viral effects.
- Estimated owners are not exact; proxies used.

### B6. Criteria for Success
- Completion of model with ≥0.6 test score (regression R² or classification accuracy)
- Visualizations meet clarity and rubric thresholds
- Findings align with stakeholder needs (actionable guidance)

---

## C. Design of Data Analytics Solution

### C1. Hypothesis
Games priced in the $5–$20 range and released in Q4 have higher owner counts than others.

### C2. Analytical Method
Linear regression to predict `estimated_owners_mid` from price, genre, release month.
K-means clustering to group games by popularity profiles.

### C2A. Justification
Regression captures numeric relationship; clustering reveals ownership tiers.

### C3. Tools & Environment
- Python
- Jupyter Notebook
- Pandas, scikit-learn, matplotlib, seaborn

### C4. Model Validation
- Regression: mean absolute error (MAE), R²
- Logistic classifier: accuracy, confusion matrix
- Clustering: silhouette score, cluster counts

### C4A. Justification
These metrics evaluate model performance and interpretability.

### C5. Practical Significance
If strong correlations or patterns emerge, developers can strategically plan pricing and release timing.

### C6. Visual Communication
- Histogram of game prices and ownership
- Heatmap of genre vs ownership
- Regression scatterplot with trendline
- Cluster plot (e.g. PCA-reduced)

---

## D. Description of Dataset

### D1. Source of Data
Steam game metadata: [Kaggle Steam Dataset], includes CSVs and JSONs with game features.

### D2. Appropriateness of Dataset
Contains relevant variables (price, release date, genre, owners) tied directly to the research question.

### D3. Data Collection Methods
- Downloaded CSV and JSON files
- Combined in memory, no new disk writes

### D4. Data Preparation
- Cleaned missing/invalid fields
- Converted release_date to datetime
- Created `release_month`, `release_year`, and `main_genre` columns
- Used `get_dummies()` for genre encoding

### D5. Data Limitations
- Owner counts are estimated, not exact
- Genres are primary only; multi-genre effects may be diluted
- No player behavior or revenue data included

---

## E. Summary of Results

### E1. Data Overview
Basic statistics for price and ownership after cleaning:

```
count  111321.000000          1.113210e+05
mean        7.060261          6.816324e+04
std        12.563365          9.212538e+05
min         0.000000          0.000000e+00
25%         0.990000          1.000000e+04
50%         3.990000          1.000000e+04
75%         9.990000          1.000000e+04
max       999.980000          1.500000e+08
```

Top genres:

```
Single-player                 98556
Steam Achievements            47065
Steam Cloud                   24326
Full controller support       20980
Multi-player                  19079
Family Sharing                17593
Partial Controller Support    12568
PvP                           11996
Steam Trading Cards           10076
Co-op                          9905
```

Price ranges:

```
$0-5      67136
$5-10     22910
$10-30    19017
$30+       2031
```

Recent releases by year:

```
2021    12376
2022    13979
2023    15543
2024    20583
```

### E2. Modeling Performance
- Linear regression MAE: **121686.86**
- Classification accuracy: **0.856**
- Cluster distribution:

```
cluster
0    91367
2    19161
1      793
```

### E3. Practical Insights
- **Genres**: Games in popular genres such as Action or RPG tend to show higher average owner counts.
- **Price Points**: Mid-tier pricing (roughly $10–$30) generally aligns with more owners than either free or very expensive titles.
- **Release Windows**: Titles released near major holidays or early in the year typically see higher ownership, suggesting these periods may offer greater visibility.


