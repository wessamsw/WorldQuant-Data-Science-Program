""" Using the aggregate method() """

import imports


# aggregate by nationality
result = <collectionName>.aggregate(
    [
        {
            "$group": {"_id": "$countryISO2", "count": {"$count": {}}}
        }
    ]
)


# aggregate by sign-up
result = <yourCollection>.aggregate(
    [
        {
            "$match": {"admissionsQuiz": "incomplete"}
        },
        {
            "$group": {
                "_id": {"$dateTrunc": {"date": "$createdAt", "unit": "day"}},
                "count": {"$sum": 1}
            }
        }
    ]
)
