WITH orders AS (
    SELECT * FROM {{ ref('stg_orders') }}
)
SELECT
    order_id,
    customer_id,
    order_date,
    amount_usd,
    CASE WHEN amount_usd > 100 THEN 'HIGH_VALUE' ELSE 'STANDARD' END AS order_tier
FROM orders
