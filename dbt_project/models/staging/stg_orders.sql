WITH source AS (
    SELECT * FROM raw_orders
)
SELECT
    id AS order_id,
    customer_id,
    order_date,
    status AS order_status,
    amount_cents / 100.0 AS amount_usd
FROM source
WHERE id IS NOT NULL
