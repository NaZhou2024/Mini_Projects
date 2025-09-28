# 📊 Financials Data Analysis with R

This project explores a **Company Financials Dataset** from Kaggle using techniques in **data importing, cleaning, exploratory data analysis (EDA), and visualization**. The final output includes a `.qmd` (Quarto) notebook and an HTML report showcasing insights gained through a structured EDA approach.

---

## 📁 Project Components

- **Dataset:** `financials.csv` (Kaggle)
- **Notebook:** `.qmd` file for analysis
- **Output:** HTML report with narrative, code, and visuals
- **Tools:** R, `ggplot2`, `tidyverse`, `skimr`, `janitor`, `lubridate`, `quarto`

---

## 🔍 Part 1: Data Importing & Preparation

### ✅ Data Importing
- Imported the CSV dataset using an **absolute local path**.
- Ensured no import errors and correct structure.
- Used appropriate libraries for data wrangling (`readr`, `dplyr`).

### 🧹 Data Cleaning (5 pts)
- Cleaned column names with `janitor::clean_names()`.
- Identified columns with dollar values (e.g., "Gross Sales", "Units Sold").
- Used `lapply()` to remove `$`, `,`, and replaced `"-"` with `NA`.
- Converted cleaned columns to numeric types.
- Treated missing values in `Profit` and `Discount` columns as `0`, assuming missing = none.

### 🔁 Data Transformation
- Converted `Date` to "Year-Month" format using `lubridate`.
- Created new variables for grouped summaries by time, product, and country.

### 🧼 Code Quality & Efficiency
- Code is modular, well-commented, and efficient.
- Each data step is clearly explained for reproducibility.

---

## 📊 Part 2: Exploratory Data Analysis

### 📈 Descriptive Statistics
- Used `skimr::skim()` and `summary()` to profile the dataset.

### 💡 Initial Insights
- Noted trends such as peak sales in October and December 2014.
- Highlighted troughs in September 2013 and March 2014 for sales and profit.

### 🔗 Correlation Analysis
- Generated pairwise correlation plots for:
  - Selected financial metrics
  - Grouped by country and product

### 📉 EDA Visualizations
- Used `ggplot2` to create:
  - Monthly trend lines for sales and profit
  - Product-level and country-level comparisons across multiple metrics
- Used `pivot_longer()` for reshaping data for visual clarity.

---

## 📈 Part 3: Data Visualization

### 🌟 Visualization Quality
- All plots are clear, well-styled, and effectively communicate trends.
- Applied consistent color themes using `theme_minimal()` and `scale_color_brewer()`.

### 📊 Appropriate Chart Types
- Used:
  - Line charts for trend analysis
  - Correlation matrices
  - Faceted plots for grouped comparisons

### 🏷 Annotations & Labels
- All plots include:
  - Titles
  - Axis labels
  - Legends
  - Clean, readable formatting

---

## 📄 Part 4: Documentation & Presentation

### 💬 Code Documentation
- Each code block is preceded by comments explaining the logic and purpose.

### 📑 Report / Presentation
- HTML report generated from `.qmd` file via Quarto.
- Clearly structured narrative accompanying code and plots.

### 🗣 Speaking
- Presentation includes confident explanation of:
  - Cleaning logic
  - EDA findings
  - Data limitations and next steps

---

## 📌 Key Takeaways

- **Sales & Profit Trends**: Highest in Oct/Dec 2014; lowest in Mar/Nov.
- **Product Insights**: Paseo leads across all financial metrics.
- **Country Patterns**: U.S. dominates in sales, COGS, and gross sales.
- **Correlations**: High positive correlations between Sales, COGS, and Gross Sales.

---

## 📎 Getting Started

1. Clone this repo or download the `.qmd` and `financials.csv` files.
2. Open the `.qmd` file in RStudio.
3. Click **Render** to generate the HTML report.
4. Explore insights via embedded visuals and summaries.

---

## 📚 Dependencies

Install required R packages:

```r
install.packages(c("tidyverse", "janitor", "skimr", "lubridate", "ggplot2"))
