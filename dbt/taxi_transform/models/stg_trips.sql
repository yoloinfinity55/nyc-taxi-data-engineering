-- We use the read_parquet function to load the file directly
select * 
from read_parquet('/Users/minijohn/Dev/nyc_taxi_portfolio/data_lake/raw/yellow_tripdata_*.parquet')
