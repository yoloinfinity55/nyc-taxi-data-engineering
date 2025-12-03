select
    payment_type,
    count(*) as total_trips,
    sum(total_amount) as total_revenue,
    avg(trip_distance) as avg_distance
from {{ ref('stg_trips') }}
group by 1
order by 3 desc
