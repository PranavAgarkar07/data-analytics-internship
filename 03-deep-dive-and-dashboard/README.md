# Task 3: Deep-Dive Analysis & Interactive Dashboarding

## Overview
Deep-dive analysis of retail store sales data (11,362 transactions, 2022-2025) with an interactive Looker Studio dashboard. Focuses on category performance, channel comparison, and discount impact.

## KPIs Defined
| KPI | Value | Formula |
|-----|-------|---------|
| Total Revenue | $1,472,998 | SUM(Total Spent) |
| Avg Order Value | $129.64 | AVG(Total Spent) |
| Total Orders | 11,362 | COUNT(Transaction ID) |
| Unique Customers | 25 | COUNT DISTINCT(Customer ID) |
| Avg Quantity/Order | 5.54 | AVG(Quantity) |
| Discount Rate | 33.5% | AVG(Discount Applied) |

## Deep-Dive: Segmentation Analysis
- **Category performance**: Butchers top ($197K), Milk Products bottom ($170K)
- **Channel comparison**: Online ($749K) vs In-store ($723K) — nearly 50/50
- **Payment methods**: Cash ($513K), Credit Card ($481K), Digital Wallet ($478K)
- **Discount impact**: Orders with discount ($130.72 AOV) vs without ($129.10 AOV) — no significant difference

## Key Finding
Discounts do not meaningfully increase order value. The business is giving away margin with no return, suggesting the discount strategy needs revision.

## Live Dashboard
[Click here to view](https://datastudio.google.com/reporting/6d915618-eda6-4099-8c61-50f0c915d20a)

## Deliverables
| File | Description |
|------|-------------|
| `data/retail_store_clean.csv` | Cleaned dataset for dashboard |
| `scripts/analysis.py` | Python analysis script |
| `reports/analysis_report.txt` | Full analysis report |
| `reports/kpi_summary.csv` | KPI table |
| `reports/category_performance.csv` | Category breakdown |
| `reports/location_category.csv` | Online vs In-store by category |
| `reports/payment_segments.csv` | Payment method analysis |
| `reports/monthly_trend.csv` | Monthly revenue/orders |
| `reports/discount_impact.csv` | Discount effectiveness |
