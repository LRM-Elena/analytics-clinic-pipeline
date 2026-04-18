with orders AS (
    SELECT * 
    FROM {{ ref( "stg_orders")}}
),

corrections as (
    SELECT * 
    FROM {{ ref( "stg_order_corrections")}}
),

final as (
    SELECT o.order_id, o.customer_id, o.order_date,
    coalesce(c.corrected_service_type, o.service_type) as service_type,          --- COALESCE() - Returns first non-null value
    coalesce(c.corrected_status, o.status) as status
    FROM orders o LEFT JOIN corrections c
        ON o.order_id = c.order_id                                      --- tab before ON cannot be ommitted
)
    
SELECT * from final


