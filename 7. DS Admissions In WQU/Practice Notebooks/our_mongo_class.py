""" """

import imports


class MongoRepository:
    """Repository for interacting with MongoDB database.

    Params
    ----------
    client : `pymongo.MongoClient`
        Default, `MongoClient(host='localhost', port=<portNumber>)`.
    db : str
        Default, `'<yourDatabase>'`.
    collection : str
        Default, `<yourCollection>'`.

    Attributes
    ----------
    collection : pymongo.collection.Collection
        All data will be extracted from and loaded to this collection.
    """

    # `__init__` method
    def __init__(
        self, 
        client=MongoClient(host="localhost", port=<portNumber>), 
        db="'<yourDatabase>'",
        collection="`<yourCollection>'"
    ):
        self.collection = client[db][collection]

    # `find_by_date` method
    def find_by_date(self, date_string):
      
        # Convert `date_string` to datetime object
        start = pd.to_datetime(date_string, format="%Y-%m-%d")
        
        # Offset `start` by 1 day
        end = start + pd.DateOffset(days=1)
        
        # Create PyMongo query for no-quiz applicants b/t `start` and `end`
        query = {"createdAt": {"$gte": start, "$lt": end}, "admissionsQuiz": "incomplete"}
        
        # Query collection, get result
        result = self.collection.find(query)
        
        # Convert `result` to list
        observations = list(result)
        
        # REMOVE}
        return observations

      
    # `update_applicants` method
    def update_applicants(self, observations_assigned):
        n = 0
        n_modified = 0
    
        for doc in observations_assigned:
            result = self.collection.update_one(
            filter={"_id": doc["_id"]},
            update={"$set": doc}
            )
            n += result.matched_count
            n_modified += result.modified_count
        transaction_result = {"n": n, "nModified": n_modified}
        return transaction_result

      
    # `assign_to_groups` method
    def assign_to_groups(self, date_string):
      
        # get observations
        observations = self.find_by_date(date_string)
        
        # Shuffle `observations`
        random.seed(42)
        random.shuffle(observations)

        # Get index position of item at observations halfway point
        idx = len(observations) // 2

        # Assign first half of observations to control group
        for doc in observations[:idx]:
            doc["inExperiment"] = True
            doc["group"] = "no email (control)"

        # Assign second half of observations to treatment group
        for doc in observations[idx:]:
            doc["inExperiment"] = True
            doc["group"] = "email (treatment)"

        # Update collections
        result = self.update_applicants(observations)
        return result

    # `find_exp_observations` method
    def find_exp_observations(self):
        result = self.collection.find({"inExperiment": True})
        return list(result)
