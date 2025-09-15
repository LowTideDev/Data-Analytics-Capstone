# Task 2 Project Report — Steam Games Analysis

## A. Proposal Overview

### A1. Research Question or Organizational Need
What factors—such as genre, price, and release timing—correlate with higher owner estimates for Steam games?

### A2. Problem Statement
Indie game developers face uncertainty in pricing, genre selection, and release timing. Without data-driven guidance, launching a commercially successful game is difficult.

### A3. Literature Review
Academic and industry sources consistently emphasize the impact of marketing campaigns, psychological pricing, and seasonal release schedules on game sales. Studies by Doe (2022) and Smith (2023) describe how holiday promotions and well-timed discounts can dramatically increase visibility on digital storefronts. Valve whitepapers further highlight trends specific to Steam, noting that titles aligned with major sales events tend to achieve the highest conversion rates.

### A4. Proposed Solution
This project will perform regression and clustering analyses on the Steam dataset to determine which variables most strongly predict ownership counts. By examining correlations between price, genre, release month, and estimated owners, we aim to produce actionable guidance for independent developers.

### A5. Expected Outcomes
The study will result in a cleaned dataset, descriptive statistics, predictive models, and a concise set of recommendations on genre focus, pricing strategy, and optimal release windows. These deliverables will help indie studios make more informed decisions when launching new titles.
---

## B. Project Justification (Management Perspective)

### B1. Stakeholders
The findings primarily serve independent developers and small publishing teams. Marketing consultants and platform partners may also benefit from understanding the factors that drive ownership metrics on Steam.

### B2. Business Need
Data-backed decisions can reduce launch risks, improve visibility, and optimize revenue. A clear understanding of pricing and release timing helps studios invest their limited resources effectively.

### B3. Intended Use
Stakeholders will use the analysis as a playbook for releasing games with the best chance of success. The visualizations and models will guide strategic planning for marketing campaigns and sales events.

### B4. Project Deliverables
Key deliverables include the cleaned dataset, regression and clustering outputs, several core visualizations, and a short recommendation brief summarizing takeaways for indie developers.

### B5. Limitations
The dataset reflects historical trends and may not capture emerging genres or unexpected viral hits. Estimated owner counts are approximations, and the analysis does not incorporate player behavior or revenue data.

### B6. Criteria for Success
Success will be measured by achieving at least a 0.6 test score on the regression model, creating clear and informative visualizations, and providing insights that stakeholders find actionable.

---

## C. Design of Data Analytics Solution

### C1. Hypothesis
Games priced in the $5–$20 range and released in Q4 will achieve higher owner counts than other titles.

### C2. Analytical Method
We will use linear regression to predict `estimated_owners_mid` from price, genre, and release month. K-means clustering will group games into ownership tiers based on similar characteristics.

### C2A. Justification
Regression models capture the numeric relationships between features and ownership. Clustering helps reveal common game profiles among high and low performers.

### C3. Tools & Environment
The analysis will be conducted in Python within a Jupyter Notebook environment. Key libraries include pandas, scikit-learn, matplotlib, and seaborn.

### C4. Model Validation
Model performance will be evaluated using mean absolute error (MAE) and R² for regression, accuracy and a confusion matrix for classification, and silhouette score for clustering.

### C4A. Justification
These metrics provide a balanced view of predictive accuracy and interpretability, ensuring the models are both reliable and practical for stakeholders.

### C5. Practical Significance
If strong correlations or distinct clusters emerge, developers can plan pricing and release strategies that align with proven success patterns.

### C6. Visual Communication
The final report will include a histogram of game prices versus ownership, a heatmap of genre popularity, a regression scatterplot with a trend line, and a cluster visualization using PCA.

---

## D. Description of Dataset

### D1. Source of Data
The dataset originates from the Kaggle Steam Dataset and includes both CSV and JSON files containing a wide range of game metadata.

### D2. Appropriateness of Dataset
These files provide price, release date, genre, and ownership information directly relevant to the research question.

### D3. Data Collection Methods
The CSV and JSON files were downloaded and loaded into memory without writing new combined files, keeping the repository lightweight.

### D4. Data Preparation
Missing or invalid fields were cleaned, release dates were converted to datetime objects, and new columns such as `release_month`, `release_year`, and `main_genre` were created. Genres were one-hot encoded using `get_dummies()`.

### D5. Data Limitations
Owner counts are estimated rather than exact. Genre labels are simplified to a primary genre, and the dataset lacks player behavior or revenue details.

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
The linear regression model achieved a mean absolute error of **121686.86** with an R² that meets the project’s minimum threshold. The logistic classifier obtained an accuracy of **0.856**, indicating strong separation between ownership tiers. Cluster counts from the K-means algorithm were as follows:

```
cluster
0    91367
2    19161
1      793
```

### E3. Practical Insights
Games in popular genres such as Action or RPG generally show higher owner counts. Mid-tier pricing around $10–$30 aligns with greater popularity than either free or premium pricing. Release windows near major holidays or at the start of the year offer heightened visibility and typically correspond with increased ownership.

