-- 1) Preview cleaned data
SELECT * FROM sales_cleaned LIMIT 10;

-- 2) Total sales by category
SELECT
    category,
    ROUND(SUM(total_amount), 2) AS total_sales
FROM sales_cleaned
GROUP BY category
ORDER BY total_sales DESC;

-- 3) Total sales by city
SELECT
    city,
    ROUND(SUM(total_amount), 2) AS total_sales
FROM sales_cleaned
GROUP BY city
ORDER BY total_sales DESC;

-- 4) Orders count by month
SELECT
    order_month,
    COUNT(order_id) AS orders_count
FROM sales_cleaned
GROUP BY order_month
ORDER BY order_month;