with raw as (
    SELECT customer_id, name, email, signup_date
    from {{ source('raw', 'raw_customers')}}
)

SELECT customer_id, name, email, signup_date
from raw
