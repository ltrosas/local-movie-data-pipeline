with transforms as (
  select
    id,
    title,
    TO_DATE(released, 'DD Mon YYYY') as released,
    country,
    cast(split_part(runtime, ' ', 1) as int) as runtime_mins,
    genre,
    director,
    actors
  from raw.movies_raw_api
)

select * from transforms