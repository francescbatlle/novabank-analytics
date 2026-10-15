-- Staging model for customers: reads the raw Parquet file and cleans it.
-- Materialized as a table so it does not depend on the file path at query time.
{{ config(materialized='table') }}

select
    customer_id,
    cast(signup_date as date) as signup_date,
    country as country_code,
    acquisition_channel,
    plan
from read_parquet('../../data/raw/customers.parquet')
 