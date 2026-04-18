with raw as (
    SELECT order_id, customer_id, order_date, service_type, status
    from {{ source('raw', 'raw_orders')}}
)

SELECT order_id, customer_id, order_date, service_type, status
from raw