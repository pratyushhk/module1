import pandas as pd
from sqlalchemy import create_engine

def main():
    engine = create_engine("postgresql://root:root@pgdatabase:5432/taxi")  

    green_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet"
    zones_url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"

    df_green = pd.read_parquet(green_url)

     
    int_cols = ["VendorID","PULocationID","DOLocationID","RatecodeID","passenger_count","payment_type","trip_type"]
    present = [c for c in int_cols if c in df_green.columns]
    df_green[present] = df_green[present].astype("Int64")

     
    df_green.head(0).to_sql("green_taxi_data", engine, if_exists="replace", index=False)

     
    chunk_size = 10000
    for i in range(0, len(df_green), chunk_size):
        df_green.iloc[i:i+chunk_size].to_sql(
            "green_taxi_data",
            engine,
            if_exists="append",
            index=False,
            method="multi",
        )

     
    df_zones = pd.read_csv(zones_url, dtype={
        "LocationID": "Int64",
        "Borough": "string",
        "Zone": "string",
        "service_zone": "string"
    })
    df_zones.to_sql("zones_data", engine, if_exists="replace", index=False)

if __name__ == "__main__":
    main()
