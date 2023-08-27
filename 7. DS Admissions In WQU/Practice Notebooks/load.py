""" Loading into a data frame """

import aggregate

# aggregated by nationality
<df_Name> = pd.DataFrame(result).rename(
  {"_id": "country_iso2"}, axis="columns").sort_values("count")



# aggregated by sign up
<ndf_Name> = (
    pd.DataFrame(result)
    .rename({"_id": "date", "count": "new_users"}, axis=1)
    .set_index("date")
    .sort_index()
    .squeeze()
)
