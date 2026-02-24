# 📊 Vibe Coding Prompts: Data Analysis

> Copy-paste these prompts into your AI-Native IDE to analyze and visualize data
> without writing a single line of code yourself!

---

## 📈 Data Visualization

### Sales Dashboard from CSV

```
I have a CSV file called "sales.csv" in the current directory. Please:

1. Read the CSV and show me a quick summary (shape, columns, data types, missing values)
2. Create a comprehensive visual dashboard saved as "dashboard.png" with:
   - Top-left: Monthly revenue trend (line chart)
   - Top-right: Revenue by category (horizontal bar chart)
   - Bottom-left: Top 10 products by sales volume (bar chart)
   - Bottom-right: Sales distribution (histogram)
3. Use a dark theme matching this color palette:
   - Background: #0a0e17
   - Primary: #00ff88
   - Secondary: #c084fc
   - Accent: #ff6b9d
4. Add proper titles, labels, and a main title "Sales Analytics Dashboard"
5. Also print key insights to the terminal:
   - Total revenue, average order value
   - Best/worst performing month
   - Top 3 categories

Use pandas + matplotlib. If the CSV doesn't exist, generate sample sales data
with 1000 rows first, then create the dashboard.
```

### Survey Results Analyzer

```
Create a Python script that analyzes survey results:

1. Generate sample survey data (200 respondents) with fields:
   - age, gender, satisfaction (1-5), recommend (yes/no), comments
2. Produce these visualizations (save as separate PNG files):
   - Age distribution histogram with KDE curve
   - Satisfaction score breakdown (stacked bar by gender)
   - Recommendation rate pie chart
   - Satisfaction vs Age scatter plot with trend line
   - Word cloud from comments (use wordcloud library)
3. Generate a summary report in Markdown with:
   - Response rate statistics
   - Average satisfaction by demographic
   - Key findings and recommendations
4. Use a professional color scheme

Use pandas, matplotlib, seaborn. Install missing packages if needed.
```

---

## 🔍 Exploratory Data Analysis

### Auto-EDA Report

```
Build a Python script that performs automatic exploratory data analysis:

1. Accept any CSV file as input (command-line argument)
2. Generate a comprehensive EDA report including:
   - Dataset overview (rows, columns, memory usage)
   - Data type analysis for each column
   - Missing value heatmap
   - Numerical columns: distribution plots, box plots, descriptive stats
   - Categorical columns: value counts, bar charts
   - Correlation matrix heatmap with annotations
   - Outlier detection using IQR method
3. Save all charts to an "eda_output/" directory
4. Generate an HTML report that combines all findings
5. Print a quick executive summary to terminal

Use pandas, matplotlib, seaborn. Handle edge cases (empty columns,
single-value columns, mixed types).
```

---

## 🏠 Real-World Analysis

### Personal Finance Tracker

```
Create a personal finance analysis tool:

1. Generate 6 months of sample transaction data (CSV):
   - date, description, amount, category (food, transport, rent, etc.)
2. Analysis and visualizations:
   - Monthly spending trend (line chart)
   - Spending by category (donut chart)
   - Daily spending heatmap (calendar-style)
   - Budget vs Actual comparison (grouped bar chart)
   - Savings rate over time
3. Identify patterns:
   - Highest spending day of the week
   - Most expensive category
   - Month-over-month change percentage
4. Generate a "Financial Health Report" in Markdown
5. Flag unusual transactions (> 2 standard deviations from category mean)

Use pandas + matplotlib. Make charts publication-quality.
```

---

## 💡 Tips for Data Analysis Prompts

| Tip                                   | Why                                                 |
| ------------------------------------- | --------------------------------------------------- |
| **Describe the data format**          | "CSV with columns: date, amount, category"          |
| **Ask for sample data generation**    | So the script works even without real data          |
| **Specify chart style**               | "Dark theme" or "publication quality"               |
| **Request both visual + text output** | Charts for presentation, stats for details          |
| **Ask for error handling**            | "Handle missing values gracefully"                  |
| **Iterate on insights**               | After first run: "Drill deeper into the Q3 anomaly" |

---

<p align="center">
  📚 Learn the full Vibe Coding methodology at <a href="https://www.hoppypy.com/en/learn/python-vibe/01-choose-your-weapon">HoppyPy</a>
</p>
