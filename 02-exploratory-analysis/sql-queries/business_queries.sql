-- Q1 Which product categories make the most money?
SELECT
    category,
    ROUND(SUM(total_spent)::numeric, 2) AS total_revenue,
    COUNT(*) AS transaction_count,
    ROUND(AVG(total_spent)::numeric, 2) AS avg_transaction_value
FROM sales
GROUP BY category
ORDER BY total_revenue DESC
LIMIT 5;

-- Q2 How does revenue change month by month?
SELECT
    TO_CHAR(transaction_date, 'YYYY-MM') AS month,
    ROUND(SUM(total_spent)::numeric, 2) AS monthly_revenue,
    COUNT(*) AS transactions,
    ROUND(AVG(total_spent)::numeric, 2) AS avg_order_value
FROM sales
GROUP BY TO_CHAR(transaction_date, 'YYYY-MM')
ORDER BY month;

-- Q3 What are the top 10 best-selling items?
SELECT
    item,
    category,
    SUM(quantity) AS total_units_sold,
    ROUND(SUM(total_spent)::numeric, 2) AS total_revenue
FROM sales
GROUP BY item, category
ORDER BY total_units_sold DESC
LIMIT 10;

-- Q4 Is Online or In-store performing better?
SELECT
    location,
    ROUND(SUM(total_spent)::numeric, 2) AS total_revenue,
    COUNT(*) AS transaction_count,
    ROUND(AVG(total_spent)::numeric, 2) AS avg_transaction_value,
    SUM(quantity) AS total_units_sold,
    ROUND(SUM(total_spent) * 100.0 / (SELECT SUM(total_spent) FROM sales), 2) AS revenue_pct
FROM sales
GROUP BY location;

-- Q5 Which payment method do customers prefer?
SELECT
    payment_method,
    COUNT(*) AS usage_count,
    ROUND(SUM(total_spent)::numeric, 2) AS total_revenue,
    ROUND(AVG(total_spent)::numeric, 2) AS avg_transaction_value,
    ROUND(AVG(quantity), 1) AS avg_items_per_transaction
FROM sales
GROUP BY payment_method
ORDER BY usage_count DESC;

-- Q6 Do discounts actually change how much people spend?
SELECT
    discount_applied,
    COUNT(*) AS transaction_count,
    ROUND(AVG(total_spent)::numeric, 2) AS avg_order_value,
    ROUND(SUM(total_spent)::numeric, 2) AS total_revenue,
    ROUND(AVG(quantity), 1) AS avg_quantity
FROM sales
GROUP BY discount_applied;

-- Q7 How many new customers are we getting each month?
SELECT
    TO_CHAR(first_purchase, 'YYYY-MM') AS acquisition_month,
    COUNT(*) AS new_customers
FROM (
    SELECT
        customer_id,
        MIN(transaction_date) AS first_purchase
    FROM sales
    GROUP BY customer_id
) AS first_orders
GROUP BY acquisition_month
ORDER BY acquisition_month;

-- Q8 Which day of the week brings in the most revenue?
SELECT
    weekday,
    ROUND(SUM(total_spent)::numeric, 2) AS total_revenue,
    COUNT(*) AS transaction_count,
    ROUND(AVG(total_spent)::numeric, 2) AS avg_transaction_value,
    ROUND(SUM(total_spent) * 100.0 / (SELECT SUM(total_spent) FROM sales), 2) AS revenue_share_pct
FROM sales
GROUP BY weekday
ORDER BY total_revenue DESC;

-- Q9: Which cities have the highest-spending customers? (JOIN demo)
-- JOIN connects sales transactions with customer demographics
SELECT
    c.city,
    c.membership,
    ROUND(SUM(s.total_spent)::numeric, 2) AS total_revenue,
    COUNT(DISTINCT c.customer_id) AS customer_count,
    ROUND(SUM(s.total_spent) / COUNT(DISTINCT c.customer_id), 2) AS revenue_per_customer
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
GROUP BY c.city, c.membership
ORDER BY total_revenue DESC;

-- Q10: How does membership tier affect spending? (JOIN + GROUP BY)
SELECT
    c.membership,
    COUNT(DISTINCT c.customer_id) AS customer_count,
    ROUND(AVG(s.total_spent)::numeric, 2) AS avg_order_value,
    ROUND(SUM(s.total_spent)::numeric, 2) AS total_revenue,
    ROUND(AVG(s.quantity), 1) AS avg_items_per_order
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
GROUP BY c.membership
ORDER BY total_revenue DESC;
