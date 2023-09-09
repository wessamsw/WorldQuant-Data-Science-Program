""" """

import imports
import connect
import mongo_instance


exp = Experiment(repo=client, db="yourDatabase", collection="yourCollection")
exp.reset_experiment()
result = exp.run_experiment(days=exp_days, assignment=True)
