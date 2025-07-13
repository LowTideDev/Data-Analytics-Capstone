# Task 2 Project Proposal — Steam Games Analysis

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

