with raw as (
    SELECT string_field_0, string_field_1, string_field_2       -- Avoid SELECT * to protect staging models from raw schema drift and ensure a stable contract

    from {{ source('raw', 'order_corrections')}}
    ),

cleaned as(
    SELECT
        string_field_0 as order_id,
        string_field_1 as corrected_service_type,
        string_field_2 as corrected_status
    from raw
    where string_field_0 != 'order_id'
)

SELECT * from cleaned