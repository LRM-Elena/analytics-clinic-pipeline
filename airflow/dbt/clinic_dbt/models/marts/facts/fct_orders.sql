with orders as (
    SELECT *
    FROM {{ref("int_orders_corrected")}}
),

payments as (
    SELECT *
    from {{ ref("int_payments")}}
),

customers as (
    SELECT *
    FROM {{ ref("dim_customers")}}
),

final as (SELECT o.order_id, o.customer_id, 
                 c.name, c.email,
                 o. order_date, o.service_type, o.status as order_status,
                 coalesce(p.total_paid,0) as total_paid, p.payment_count, p.last_payment_date,
                 CASE                                                                                         --- flags
                    when coalesce(p.total_paid,0) > 0 THEN TRUE
                    ELSE FALSE
                 END as is_paid,
                 CASE
                    WHEN o.status = 'completed' and coalesce(p.total_paid,0) > 0 THEN TRUE 
                    ELSE FALSE 
                 END as is_fulfilled
FROM orders o
LEFT JOIN payments p on o.order_id = p.order_id
LEFT JOIN customers c on o.customer_id = c.customer_id
)

SELECT * from final