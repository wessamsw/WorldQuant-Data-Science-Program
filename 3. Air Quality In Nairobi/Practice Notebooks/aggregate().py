# Determine which collection
# has the most sensor readings
# $ --> introduces sth new
result = dar.aggregate(
    [
        {"$group": {"_id": "$metadata.site", "count": {"$count": {}}}}
    ]
)
readings_per_site = list(result)
readings_per_site

# sample output
[{'_id': 23, 'count': 60020}, {'_id': 11, 'count': 138412}]
