""" """

import imports
import load


# `build_nat_choropleth` function
<df_Name>["count_pct"] = (<df_Name>["count"] / <df_Name>["count"].sum()) * 100


def build_nat_choropleth():
    fig = px.choropleth(
        data_frame= <df_Name>,
        locations="country_iso3",
        color="count_pct",
        projection="natural earth",
        color_continuous_scale=px.colors.sequential.Oranges,
        title="Title"
    )
    return fig

# Display image
nat_fig = build_nat_choropleth()
nat_fig.write_image("images/7-5-4.png", scale=1, height=500, width=700)

nat_fig.show()
