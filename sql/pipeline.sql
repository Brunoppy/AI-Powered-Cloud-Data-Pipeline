
-- BigQuery SQL Script to create a sales table and perform aggregation
CREATE OR REPLACE TABLE marketplace_dataset.sales (
    order_id STRING,
    product_id STRING,
    quantity INT64,
    price FLOAT64,
    sale_date DATE
);

-- Example query: total sales by day
SELECT
    sale_date,
    SUM(quantity * price) AS total_sales
FROM
    marketplace_dataset.sales
GROUP BY sale_date
ORDER BY sale_date;
