import libraries

# Compressed file --> dict
with gzip.open("<filePath>", "r") as f:
    taiwan_data = json.load(f)

# Extracting keys from a dict
taiwan_data_keys = taiwan_data.keys()
print(taiwan_data_keys)

  # Sample output
  dict_keys(['schema', 'metadata', 'observations'])

# Counting number of observations
len(taiwan_data["observations"])

# Length / no. of each observation
len(taiwan_data["observations"][0])
