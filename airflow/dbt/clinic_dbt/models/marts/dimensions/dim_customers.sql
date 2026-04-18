with customers as (
    SELECT *
    FROM {{ ref("stg_customers")}}
)

SELECT customer_id,name, email, signup_date
FROM customers