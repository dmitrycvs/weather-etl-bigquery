from google.cloud import bigquery
import pandas as pd


client = bigquery.Client()
table_id = "weather-etl-449512.weather_ds.weather_data"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
    skip_leading_rows=1,
    ignore_unknown_values=True,
)

df = pd.read_csv("datasets/GlobalWeatherRepository.csv")
job = client.load_table_from_dataframe(df, table_id, job_config=job_config)

job.result()

print("CSV data was loaded successfully!")
