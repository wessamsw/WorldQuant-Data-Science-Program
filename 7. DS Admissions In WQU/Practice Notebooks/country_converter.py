""" """

import load

# Instantiate `CountryConverter`
cc = CountryConverter()

# Create new columns      ... full country names
<df_Name>["country_name"] = cc.convert(
    <df_Name>["country_iso2"], to="name_short"
)

#                         ... three letter abbv country names
<df_Name>["country_iso3"] = cc.convert(
    <df_Name>["country_iso2"], to="ISO3"
)
