-- Business question: How many customers are there in each country?
SELECT
    country,
    COUNT(*) AS customer_count,
    SUM(total_orders) AS total_orders
FROM customers
GROUP BY country
ORDER BY customer_count DESC;

-- Business question: Which customers have placed at least five orders?
SELECT
    customer_id,
    first_name,
    last_name,
    total_orders
FROM customers
WHERE total_orders >= 5
ORDER BY total_orders DESC;
