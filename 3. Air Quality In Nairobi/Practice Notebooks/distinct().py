# Determine no. of sites in collection
sites = dar.distinct("metadata.site")     # dar ---> variable holding collection
sites

# Sample output
[11, 23]

# count no. of docs at a prticular site
# using count_documents()
dar.count_documents({"metadata.site": 23})

# Sample output
60020
