with raw as (
    SELECT payment_id, order_id, amount, currency, payment_date, payment_method
    from {{ source('raw', 'raw_payments')}}
)

SELECT payment_id, order_id, amount, currency, payment_date, payment_method
from raw
