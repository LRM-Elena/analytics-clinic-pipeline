SELECT order_id, 
       sum(amount) as total_paid,
       count (*) as payment_count,
       min(payment_date) as first_payment_date,
       max(payment_date) as last_payment_date,
from {{ ref("stg_payments")}}
group by order_id
