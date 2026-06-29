"""
ApexPlanet Data Analytics - Task 3
Deep-Dive Analysis & Interactive Dashboarding
Using retail_store_sales_clean.csv from Task 1
"""

import pandas as pd
import os

CSV_PATH = '/home/pranav/Desktop/projects/Internship/data-analytics/01-data-wrangling/data/retail_store_sales_clean.csv'
OUT_DIR = '/home/pranav/Desktop/projects/Internship/data-analytics/03-deep-dive-and-dashboard'

df = pd.read_csv(CSV_PATH)
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])

# Feature engineering
age_bins = [0, 25, 35, 50, 100]
age_labels = ['Youth (18-25)', 'Young Adult (26-35)', 'Adult (36-50)', 'Senior (51+)']

df['Quarter'] = df['Month'].apply(lambda m: (m - 1) // 3 + 1)
df['Month_Name'] = df['Transaction Date'].dt.strftime('%b')
df['Revenue_per_Unit'] = (df['Total Spent'] / df['Quantity']).round(2)

# --- 1. Save cleaned dataset for Looker Studio ---
clean_path = os.path.join(OUT_DIR, 'data', 'retail_store_clean.csv')
df.to_csv(clean_path, index=False)

# --- 2. KPIs ---
kpi = {}
kpi['Total_Revenue'] = df['Total Spent'].sum()
kpi['AOV'] = df['Total Spent'].mean()
kpi['Total_Orders'] = len(df)
kpi['Total_Customers'] = df['Customer ID'].nunique()
kpi['Avg_Quantity'] = df['Quantity'].mean()
kpi['Discount_Rate'] = df['Discount Applied'].mean() * 100
kpi['Online_vs_InStore'] = df['Location'].value_counts().to_dict()
kpi['Revenue_by_Category'] = df.groupby('Category')['Total Spent'].sum().sort_values(ascending=False).to_dict()
kpi['Revenue_by_Location'] = df.groupby('Location')['Total Spent'].sum().to_dict()

# --- 3. Deep-dive: Segmentation ---

# Category performance
cat_perf = df.groupby('Category').agg(
    Revenue=('Total Spent', 'sum'),
    AOV=('Total Spent', 'mean'),
    Orders=('Transaction ID', 'count'),
    Discount_Usage=('Discount Applied', 'mean')
).round(2).sort_values('Revenue', ascending=False)

# Location x Category cross-segment
loc_cat = df.groupby(['Location', 'Category']).agg(
    Revenue=('Total Spent', 'sum'),
    Orders=('Transaction ID', 'count'),
    AOV=('Total Spent', 'mean')
).round(2)

# Payment method analysis
pay_seg = df.groupby('Payment Method').agg(
    Revenue=('Total Spent', 'sum'),
    Orders=('Transaction ID', 'count'),
    AOV=('Total Spent', 'mean')
).round(2).sort_values('Revenue', ascending=False)

# Monthly trend
monthly = df.groupby(['Year', 'Month', 'Month_Name']).agg(
    Revenue=('Total Spent', 'sum'),
    Orders=('Transaction ID', 'count'),
    AOV=('Total Spent', 'mean')
).round(2).reset_index()
monthly = monthly.sort_values(['Year', 'Month'])

# Discount impact
discount_analysis = df.groupby('Discount Applied').agg(
    Revenue=('Total Spent', 'sum'),
    Orders=('Transaction ID', 'count'),
    AOV=('Total Spent', 'mean'),
    Avg_Qty=('Quantity', 'mean')
).round(2)

# --- 4. Save reports ---
kpi_df = pd.DataFrame([kpi])
kpi_df.to_csv(os.path.join(OUT_DIR, 'reports', 'kpi_summary.csv'), index=False)
cat_perf.to_csv(os.path.join(OUT_DIR, 'reports', 'category_performance.csv'))
loc_cat.to_csv(os.path.join(OUT_DIR, 'reports', 'location_category.csv'))
pay_seg.to_csv(os.path.join(OUT_DIR, 'reports', 'payment_segments.csv'))
monthly.to_csv(os.path.join(OUT_DIR, 'reports', 'monthly_trend.csv'), index=False)
discount_analysis.to_csv(os.path.join(OUT_DIR, 'reports', 'discount_impact.csv'))

# --- 5. Report ---
report = f"""======================================================================
TASK 3: DEEP-DIVE ANALYSIS & INTERACTIVE DASHBOARDING
Dataset: retail_store_sales_clean.csv
======================================================================

DATA OVERVIEW
-------------
Rows: {len(df):,}
Columns: {len(df.columns)}
Date Range: {df['Transaction Date'].min().date()} to {df['Transaction Date'].max().date()}
Nulls: 0 (dataset already cleaned)

======================================================================
CORE KPIs
---------
Total Revenue:       ${kpi['Total_Revenue']:,.2f}
Avg Order Value:     ${kpi['AOV']:,.2f}
Total Orders:        {kpi['Total_Orders']:,}
Unique Customers:    {kpi['Total_Customers']}
Avg Quantity/Order:  {kpi['Avg_Quantity']:.2f}
Discount Rate:       {kpi['Discount_Rate']:.1f}% of orders had a discount

Revenue by Location:
"""
for loc, rev in kpi['Revenue_by_Location'].items():
    report += f"  {loc:15s}: ${rev:>10,.2f}\n"

report += "\nRevenue by Category:\n"
for cat, rev in kpi['Revenue_by_Category'].items():
    report += f"  {cat:40s}: ${rev:>10,.2f}\n"

report += f"""
======================================================================
DEEP-DIVE: SEGMENTATION ANALYSIS
======================================================================

1. CATEGORY PERFORMANCE
{cat_perf.to_string()}

2. LOCATION x CATEGORY CROSS-SEGMENT
{loc_cat.to_string()}

3. PAYMENT METHOD ANALYSIS
{pay_seg.to_string()}

4. DISCOUNT IMPACT
{discount_analysis.to_string()}

5. MONTHLY TREND (First 6 months)
{monthly[['Year','Month','Month_Name','Revenue','Orders','AOV']].head(6).to_string()}
======================================================================

Files saved:
  data/retail_store_clean.csv          - Cleaned dataset (for Google Sheets)
  reports/kpi_summary.csv             - KPI table
  reports/category_performance.csv     - Category performance
  reports/location_category.csv        - Location x Category segments
  reports/payment_segments.csv         - Payment method analysis
  reports/monthly_trend.csv            - Monthly trends
  reports/discount_impact.csv          - Discount analysis
======================================================================
"""

report_path = os.path.join(OUT_DIR, 'reports', 'analysis_report.txt')
with open(report_path, 'w') as f:
    f.write(report)

print(report)
