{{ config(materialized='table') }}

with transforms_time as (
  select
    id,
    title,
    year,
    released,
    country,
    runtime,
    cast(split_part(runtime, ' ', 1) as float)/60 as runtime_hours,
    genre,
    director,
    actors
  from public.movies_raw_api
)

select * from transforms_time