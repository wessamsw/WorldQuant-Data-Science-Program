# Wrangle function:
# read in a csv file
# apartments in <cityName> < $100000
# remove outliers
# separate columns
# create new columns from existing
# take care of highly null columns
# low and high cardinality
# Leakage
# multicolinearity

def wrangle(filepath):
    # Read CSV file
    df = pd.read_csv(filepath)
    
    # Subset data: Apartments in <cityName>, less than 100,000
    mask_ba = df["place_with_parent_names"].str.contains(<cityName>)
    mask_apt = df["property_type"] == "apartment"
    mask_price = df["price_aprox_usd"] < 100_000
    df = df[mask_ba & mask_apt & mask_price]

    # Subset data: Remove outliers for "surface_covered_in_m2"
    low, high = df["surface_covered_in_m2"].quantile([0.1, 0.9])
    mask_area = df["surface_covered_in_m2"].between(low, high)
    df = df[mask_area]
    
    # split lat-lon column
    df[["lat", "lon"]] = df["lat-lon"].str.split(",", expand=True).astype(float)
    df.drop(columns="lat-lon", inplace=True)
    
    # Extract newColumnName
    df[<newColumnName>] = df["place_with_parent_names"].str.split("|", expand=True)[1]
    df.drop(columns="place_with_parent_names", inplace=True)
    
    # Drop feature with high null count
    df.drop(columns=["surface_total_in_m2", "price_usd_per_m2", "floor", "rooms", "expenses"], inplace=True)
    
    # Drop low- and high- categorical variables
    df.drop(columns=["operation", "property_type", "currency", "properati_url"], inplace=True)
    
    # Drop leaky columns
    df.drop(columns=["price", "price_aprox_local_currency", "price_per_m2"], inplace=True)
    
    # Drop columns with multi-colinerlity
    #df.drop(columns=["surface_total_in_m2", "rooms"], inplace=True)
    
    return df
  
  
test1.isnull().sum() / len(test1)   # check for highly null columns
test1.select_dtypes("object").nunique()   # check for low- and high- categorical variables
