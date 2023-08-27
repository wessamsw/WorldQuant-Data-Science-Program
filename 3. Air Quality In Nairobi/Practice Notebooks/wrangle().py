# Wrangle function
# Extract PM2.5 readings
# from collection site with
# most readings
# Localize time
# Remove outliers
# Resample data to provide PM2.5 readings
# for each hour
# impute missing values
# return series
def wrangle(collection):
    results = collection.find(
        {"metadata.site": 11, "metadata.measurement": "P2"},
        projection={"P2": 1, "timestamp": 1, "_id": 0},   # ---> focus/ limit to only "P2" and timestamp
    )

    df = pd.DataFrame(results).set_index("timestamp")
    
    # Localize time
    df.index = df.index.tz_localize("UTC").tz_convert("Africa/Dar_es_Salaam")
    
    # Remove outliers
    df = df[df["P2"] < 100]
    
    # Resample to 1hour period, fill in missing values
    y = df["P2"].resample("1H").mean().fillna(method='ffill')
    
    return y
  
# Using wrangle()
y = wrangle(dar)
y.head()

# sample output
timestamp
2018-01-01 03:00:00+03:00    9.456327
2018-01-01 04:00:00+03:00    9.400833
2018-01-01 05:00:00+03:00    9.331458
2018-01-01 06:00:00+03:00    9.528776
2018-01-01 07:00:00+03:00    8.861250
Freq: H, Name: P2, dtype: float64
