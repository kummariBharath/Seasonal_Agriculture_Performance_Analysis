# 🌾 Seasonal Agriculture Performance Analysis

<p align="center">
  <b>Data-driven analysis of agricultural performance across crops, seasons, states, and districts.</b>
</p>

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="45"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="45"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" width="45"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/matplotlib/matplotlib-original.svg" width="45"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original.svg" width="45"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?logo=numpy&logoColor=white"/>
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-orange"/>
  <img src="https://img.shields.io/badge/Seaborn-Visualization-4C72B0"/>
  <img src="https://img.shields.io/badge/Google%20Colab-Notebook-F9AB00?logo=googlecolab&logoColor=white"/>
</p>

---

## 📌 Project Overview

**Seasonal Agriculture Performance Analysis** is a data analysis project that explores agricultural performance across different **crops, seasons, states, and districts**.

The project uses Python-based data analysis and visualization techniques to understand:

- 🌱 Crop productivity
- 📈 Agricultural yield
- 💰 Revenue and profitability
- 💧 Water efficiency
- 🌦️ Seasonal performance
- 🗺️ State and district performance
- 🦠 Disease and pest risk
- 🔗 Relationships between agricultural variables

The goal is to transform raw agricultural data into **meaningful insights that can support better agricultural decision-making**.

---

# 🎯 Project Objectives

The major objectives of this project are:

1. Identify the **highest- and lowest-performing crops**.
2. Compare agricultural performance across different **seasons**.
3. Analyze agricultural performance across **states and districts**.
4. Identify crops with the highest **profitability**.
5. Analyze **yield performance**.
6. Evaluate **water efficiency** across crops.
7. Identify crops with higher **disease and pest risk**.
8. Study relationships between important agricultural variables.
9. Create meaningful visualizations to communicate findings.
10. Generate practical recommendations from the analysis.

---

# 📊 Dataset

The dataset contains agricultural records representing different farms, crops, seasons, locations, environmental conditions, costs, revenue, yield, water usage, and disease/pest risk.

### Dataset Size

| Property | Value |
|---|---:|
| Rows | 4,000 |
| Columns | 28 |
| Missing Values Initially | 120 |
| Duplicate Rows | 0 |
| States | 8 |
| Crops | 8 |
| Seasons | 3 |
| Irrigation Methods | 4 |

---

## 🌱 Crops Covered

The dataset contains the following crops:

- Rice
- Wheat
- Maize
- Cotton
- Pulses
- Groundnut
- Chilli
- Sugarcane

---

## 🌦️ Seasons Covered

The analysis includes:

- **Kharif**
- **Rabi**
- **Zaid**

---

## 🗺️ States Covered

The dataset includes agricultural records from:

- Andhra Pradesh
- Maharashtra
- Telangana
- Karnataka
- Gujarat
- Tamil Nadu
- Punjab
- Madhya Pradesh

---

# 🧾 Dataset Variables

The dataset contains variables from multiple agricultural categories.

### 🌾 Farm & Location Information

- `Farm_ID`
- `State`
- `District`
- `Crop`
- `Season`
- `Irrigation_Method`

### 🌦️ Environmental Conditions

- `Rainfall_mm`
- `Avg_Temperature_C`
- `Humidity_pct`
- `Sunlight_Hours_Day`

### 🌱 Soil & Nutrients

- `Soil_pH`
- `Soil_Moisture_pct`
- `Nitrogen_kg_ha`
- `Phosphorus_kg_ha`
- `Potassium_kg_h`

### 🧪 Agricultural Inputs

- `Fertilizer_kg_ha`
- `Pesticide_Litre_ha`
- `Seed_Quality_Score`

### 📈 Production & Yield

- `Yield_Tonnes_Ha`
- `Production_Tonnes`

### 💰 Financial Metrics

- `Market_Price_INR_Tonne`
- `Total_Cost_INR`
- `Revenue_INR`
- `Profit_INR`

### 💧 Water Usage

- `Water_Used_m3`
- `Water_Efficiency_t_per_1000m3`

### 🦠 Risk

- `Disease_Pest_Risk_pct`

---

# 🛠️ Technologies & Tools

<p align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="45"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="45"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" width="45"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/matplotlib/matplotlib-original.svg" width="45"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original.svg" width="45"/>
</p>

| Tool | Purpose |
|---|---|
| 🐍 Python | Core programming language |
| 🐼 Pandas | Data loading, cleaning, grouping and analysis |
| 🔢 NumPy | Numerical computing |
| 📊 Matplotlib | Data visualization |
| 🎨 Seaborn | Statistical visualization and correlation heatmap |
| 📓 Google Colab | Development environment |
| 📗 Excel | Dataset storage |

---


# 🧹 1. Data Loading & Inspection

The dataset was loaded using Pandas.

```python
import pandas as pd

df = pd.read_excel("seasonal_agriculture_performance_dataset.xlsx")
```

Initial inspection was performed using:

```python
df.head()
df.shape
df.columns
df.info()
df.describe()
```

The dataset was also checked for:

* Missing values
* Duplicate records
* Categorical distributions
* Numerical statistics
* Potential outliers

---

# 🧽 2. Data Cleaning

The dataset initially contained **120 missing values** across:

* `Rainfall_mm`
* `Soil_Moisture_pct`
* `Yield_Tonnes_Ha`

Median imputation was used to handle the missing numerical values.

```python
df["Rainfall_mm"] = df["Rainfall_mm"].fillna(
    df["Rainfall_mm"].median()
)

df["Soil_Moisture_pct"] = df["Soil_Moisture_pct"].fillna(
    df["Soil_Moisture_pct"].median()
)

df["Yield_Tonnes_Ha"] = df["Yield_Tonnes_Ha"].fillna(
    df["Yield_Tonnes_Ha"].median()
)
```

### Why Median?

Median was selected because it is less affected by extreme values compared with the mean.

After cleaning:

```python
df[[
    "Rainfall_mm",
    "Soil_Moisture_pct",
    "Yield_Tonnes_Ha"
]].isnull().sum()
```

was used to verify that the missing values had been handled.

---

# 🌱 3. Crop Performance Analysis

Crop performance was evaluated using:

* Average Yield
* Average Production
* Average Revenue
* Average Profit

```python
crop_analysis = df.groupby("Crop")[[
    "Yield_Tonnes_Ha",
    "Production_Tonnes",
    "Revenue_INR",
    "Profit_INR"
]].mean().sort_values(
    "Profit_INR",
    ascending=False
)
```

This analysis makes it possible to compare the overall performance of different crops.

### Key Finding

**Sugarcane recorded the highest average profit among the analyzed crops.**

**Wheat recorded the lowest average profit.**

---

# 🌦️ 4. Seasonal Performance Analysis

Agricultural performance was compared across:

* Kharif
* Rabi
* Zaid

```python
season_analysis = df.groupby("Season")[[
    "Yield_Tonnes_Ha",
    "Production_Tonnes",
    "Revenue_INR",
    "Profit_INR"
]].mean().sort_values(
    "Profit_INR",
    ascending=False
)
```

Yield was also analyzed independently:

```python
yield_by_season = df.groupby(
    "Season"
)["Yield_Tonnes_Ha"].mean().sort_values(
    ascending=False
)
```

### Key Finding

Among the analyzed seasons:

**Kharif had the highest average yield.**

---

# 🗺️ 5. State-Level Analysis

State-level performance was analyzed using average:

* Yield
* Profit

```python
state_analysis = df.groupby("State")[[
    "Yield_Tonnes_Ha",
    "Profit_INR"
]].mean().sort_values(
    "Profit_INR",
    ascending=False
)
```

### Key Findings

* 🥇 **Punjab** had the highest average yield.
* 📉 **Andhra Pradesh** had the lowest average yield.

This comparison helps identify geographical differences in agricultural productivity.

---

# 📍 6. District-Level Analysis

District performance was analyzed to identify differences within the dataset.

### Average Yield

```python
yield_by_district = df.groupby(
    "District"
)["Yield_Tonnes_Ha"].mean().sort_values(
    ascending=False
)
```

### Average Profit

```python
profit_by_district = df.groupby(
    "District"
)["Profit_INR"].mean().sort_values(
    ascending=False
)
```

### Key Finding

**Warangal recorded the highest average profit, while Krishna recorded the lowest average profit among the analyzed districts.**

---

# 💰 7. Financial Analysis

Financial performance was analyzed using:

* Total Cost
* Revenue
* Profit

```python
financial_by_crop = df.groupby("Crop")[[
    "Total_Cost_INR",
    "Revenue_INR",
    "Profit_INR"
]].mean().sort_values(
    "Profit_INR",
    ascending=False
)
```

This analysis helps understand which crops generate stronger financial returns.

### Key Finding

**Sugarcane had the highest average profit.**

**Wheat had the lowest average profit.**

---

# 📈 8. Profit Outlier Analysis

Profit contained several extreme values.

Instead of automatically removing them, an **IQR-based outlier analysis** was performed.

```text
Q1 = -148,731.75
Q3 = 216,187.75
IQR = 364,919.50
Lower Bound = -696,111
Upper Bound = 763,567
```

The analysis identified **404 statistical outliers**.

These included both:

* High-profit observations
* High-loss observations

The outliers were retained because an outlier is not automatically an error.

For example, a farm with unusually high revenue may legitimately produce an unusually high profit, while another farm may legitimately experience a large loss.

---

# 💧 9. Water Efficiency Analysis

Water efficiency was analyzed using:

```python
water_by_crop = df.groupby("Crop")[
    "Water_Efficiency_t_per_1000m3"
].mean().sort_values(
    ascending=False
)
```

### What does Water Efficiency mean?

The metric:

**Tonnes per 1,000 m³**

represents the amount of agricultural production obtained from every **1,000 cubic meters of water used**.

A higher value indicates better water-use efficiency.

### Key Findings

* 💧 **Sugarcane** had the highest average water efficiency.
* 💧 **Cotton** had the lowest average water efficiency.

---

# 🦠 10. Disease & Pest Risk Analysis

Disease and pest risk was analyzed across crops.

```python
risk_by_crop = df.groupby("Crop")[
    "Disease_Pest_Risk_pct"
].mean().sort_values(
    ascending=False
)
```

### Key Findings

* ⚠️ **Wheat** had the highest average disease & pest risk.
* 🛡️ **Sugarcane** had the lowest average disease & pest risk.

The differences between crops were relatively small, so the results should be interpreted as comparative patterns rather than dramatic differences.

---

# 🔗 11. Correlation Analysis

Correlation analysis was used to investigate relationships between numerical agricultural variables.

```python
correlation_matrix = df.select_dtypes(
    include="number"
).corr()
```

The correlation matrix was then examined for important relationships.

---

## 📊 Important Correlations

### Yield & Water Efficiency

```text
Correlation ≈ 0.913
```

This represents a **very strong positive relationship** in this dataset.

---

### Yield & Production

```text
Correlation ≈ 0.883
```

This represents a **strong positive relationship**.

---

### Profit & Revenue

```text
Correlation ≈ 0.887
```

This represents a **very strong positive relationship**.

---

### Yield & Profit

```text
Correlation ≈ 0.488
```

This represents a **moderate positive relationship**.

---

### Rainfall & Yield

```text
Correlation ≈ 0.031
```

This indicates almost no linear relationship in this dataset.

---

### Fertilizer & Yield

```text
Correlation ≈ 0.000
```

This indicates almost no linear relationship in this dataset.

---

### Market Price & Yield

```text
Correlation ≈ -0.383
```

This represents a moderate negative relationship.

---

## ⚠️ Important Note About Correlation

**Correlation does not imply causation.**

For example, a strong correlation between two variables does not automatically mean that one variable directly causes the other.

Correlation only describes the strength and direction of a linear relationship in the analyzed data.

---

# 🌡️ 12. Correlation Heatmap

A correlation heatmap was created using Seaborn.

```python
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap of Agricultural Variables")
plt.show()
```

The heatmap provides a visual overview of relationships between numerical variables.

---

# 📊 13. Key Visualizations

The project includes visualizations for:

### 🌱 Crop Analysis

* Average Profit by Crop
* Average Yield by Crop
* Water Efficiency by Crop
* Disease & Pest Risk by Crop

### 🌦️ Seasonal Analysis

* Average Yield by Season
* Average Profit by Season

### 🗺️ Geographic Analysis

* Average Yield by State
* Average Profit by District

### 🔗 Relationship Analysis

* Correlation Matrix
* Correlation Heatmap

---

# 🏆 Key Findings

| Analysis Area                | Finding        |
| ---------------------------- | -------------- |
| 💰 Highest Profit Crop       | Sugarcane      |
| 💰 Lowest Profit Crop        | Wheat          |
| 🌾 Highest Yield State       | Punjab         |
| 🌾 Lowest Yield State        | Andhra Pradesh |
| 💧 Highest Water Efficiency  | Sugarcane      |
| 💧 Lowest Water Efficiency   | Cotton         |
| 🦠 Highest Disease/Pest Risk | Wheat          |
| 🛡️ Lowest Disease/Pest Risk | Sugarcane      |
| 🌦️ Highest Yield Season     | Kharif         |
| 📍 Highest District Profit   | Warangal       |
| 📍 Lowest District Profit    | Krishna        |

---

# 💡 Recommendations

Based on the analysis, the following recommendations can be considered:

### 1. 🌱 Focus on High-Performing Crops

Crops with stronger profitability and efficiency can be considered where local agricultural conditions are suitable.

### 2. 💧 Improve Water Management

Lower water-efficiency crops should be examined for opportunities to improve irrigation and water utilization.

### 3. 🗺️ Investigate Regional Differences

The difference between higher-performing and lower-performing states/districts can be studied further to understand the underlying factors.

### 4. 🦠 Strengthen Pest & Disease Management

Crops with comparatively higher disease and pest risk may benefit from stronger monitoring and preventive management.

### 5. 💰 Consider Profit Alongside Yield

A crop with high yield is not necessarily the most profitable.

Production cost, market price, revenue, and other factors should also be considered.

### 6. 📊 Use Multiple Metrics Together

Agricultural decisions should consider:

```text
Yield
+
Profit
+
Water Efficiency
+
Disease/Pest Risk
+
Location
+
Season
```

rather than relying on a single metric.

---

# 📌 Final Project Summary

This project demonstrates how Python can be used to transform agricultural data into meaningful insights.

The analysis covered:

```text
Data Loading
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Crop Performance
      ↓
Seasonal Performance
      ↓
State & District Analysis
      ↓
Financial Analysis
      ↓
Water Efficiency
      ↓
Disease & Pest Risk
      ↓
Correlation Analysis
      ↓
Visualization
      ↓
Insights & Recommendations
```

The results show that agricultural performance varies across crops, seasons, and geographical regions.

**Sugarcane** performed strongly in terms of average profit and water efficiency, while **Punjab** recorded the highest average yield among states. **Wheat** showed the lowest average profit and the highest average disease/pest risk in the analysis.

Overall, the project demonstrates the importance of combining **productivity, profitability, water efficiency, risk, season, and location** when evaluating agricultural performance.

---

# 📁 Project Structure

```text
Seasonal-Agriculture-Performance-Analysis/
│
├── 📊 seasonal_agriculture_performance_dataset.xlsx
│
├── 📓 Seasonal_Agriculture_Performance_Analysis.ipynb
│
├── 📖 README.md
│
└── 📄 Seasonal_Agriculture_Performance_Analysis_Revision_Guide.docx
```

---

# 🚀 How to Run the Project

## 1. Clone the Repository

```bash
git https://github.com/kummariBharath/Seasonal_Agriculture_Performance_Analysis/tree/main
```

## 2. Open the Notebook

Open:

```text
https://colab.research.google.com/drive/1DFaq-gbqOZsqWgLnm7jq58ML1oqCnj3i?usp=sharing
```

using:

* Google Colab
* Jupyter Notebook
* JupyterLab

## 3. Install Required Libraries

If necessary:

```bash
pip install pandas numpy matplotlib seaborn openpyxl
```

## 4. Load the Dataset

Make sure the Excel dataset is available in the expected location.

Then run the notebook cells from top to bottom.

---

# 📚 Skills Demonstrated

This project demonstrates practical skills in:

* Python programming
* Pandas DataFrames
* NumPy
* Data cleaning
* Missing-value handling
* GroupBy operations
* Aggregation
* Sorting
* Exploratory Data Analysis (EDA)
* Statistical analysis
* Outlier analysis
* Correlation analysis
* Data visualization
* Matplotlib
* Seaborn
* Business-style insight generation
* Data storytelling

---

# 🧠 Python Concepts Used

Some important Python/Pandas concepts used in this project include:

```python
pd.read_excel()
df.head()
df.shape
df.columns
df.info()
df.describe()
df.isnull()
df.fillna()
df.groupby()
.mean()
.sort_values()
.idxmax()
.idxmin()
```

These operations form the foundation of many real-world data-analysis workflows.

---

# 📈 Future Improvements

Possible future improvements include:

* Interactive dashboards using Power BI or Tableau
* Interactive visualizations using Plotly
* More advanced statistical analysis
* Predictive yield modeling
* Crop profitability prediction
* Machine learning models
* Seasonal forecasting
* Geographic visualization
* Automated reporting
* Feature engineering
* Model evaluation

---

# 👨‍💻 Author

**Bharath Kummari**

Aspiring Data Analyst | Python | Data Visualization | Data Science

---

# ⭐ Project Status

```text
🟢 Completed
```

The core exploratory analysis, visualization, insights, and recommendations have been completed.

---

# ⭐ If You Found This Project Useful

If you found this project interesting or useful, consider giving the repository a ⭐.

Thanks for checking out the project! 🌾📊

```
