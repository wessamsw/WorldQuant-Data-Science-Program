import libraries

# Wrangle function
def wrangle(filePath):
    # Open compressed file, load to dict
    with gzip.open(filePath, "r") as f:
        data = json.load(f)
        
    # Dictionary --> DataFrame, set index
    df = pd.DataFrame().from_dict(data["observations"]).set_index("id")
    
    return df
