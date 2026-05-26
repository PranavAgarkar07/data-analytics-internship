# Data Dictionary

## Dataset: Retail Store Sales

| Column | Type | Description | Business Relevance |
|--------|------|-------------|-------------------|
| Transaction ID | string | Unique identifier for each transaction | Primary key, used for tracking individual purchases |
| Customer ID | string | Identifier for the customer | Helps analyze customer-level behavior and repeat purchases |
| Category | string | Product category (e.g. Patisserie, Milk Products) | Useful for sales breakdown by department |
| Item | string | Name of the product purchased | Identifies which products are selling |
| Price Per Unit | float | Cost of one unit of the item | Used to calculate revenue and pricing strategy |
| Quantity | integer | Number of units bought | Helps understand order volume and bulk buying patterns |
| Total Spent | float | Total amount spent (Price × Quantity) | Core revenue metric |
| Payment Method | string | How the customer paid | Can reveal payment preferences and fees |
| Location | string | Online or In-store | Channel performance comparison |
| Transaction Date | datetime | When the purchase happened | Enables time-based analysis (trends, seasonality) |
| Discount Applied | boolean | Whether a discount was applied | Understands discount usage and its impact on revenue |
| Year | integer | Calendar year extracted from Transaction Date | Enables year-over-year sales comparison |
| Month | integer | Calendar month (1–12) extracted from Transaction Date | Reveals monthly trends and seasonal patterns |
| Weekday | string | Day of the week (e.g. Monday) extracted from Transaction Date | Identifies day-of-week buying patterns |
