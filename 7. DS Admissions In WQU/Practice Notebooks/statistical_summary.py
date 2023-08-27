""" """

import imports
import load
import aggregate


mean = <ndf_Name>.describe()["mean"]
std = <ndf_Name>.describe()["std"]


# sum...
exp_days = <no_of_days>
sum_mean = mean * exp_days
sum_std = std * math.sqrt(exp_days)
