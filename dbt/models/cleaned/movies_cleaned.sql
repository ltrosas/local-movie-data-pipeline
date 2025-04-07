{{ config(materialized='table') }}

with cleaned as (
  select
    id,
    title,
    genre,
    cast(release_year as varchar) as release_year,
    rating
  from public.movies_raw
)

select * from cleaned