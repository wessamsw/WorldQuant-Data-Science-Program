""" """

import imports
import crosstab


# `build_contingency_bar` function
def build_contingency_bar():
    # side-by-side bar chart
    fig = px.bar(
        data_frame=data,
        barmode="group",
        title="TITLE"
    )
    # Set axis labels
    fig.update_layout(xaxis_title="XTITLE", yaxis_title="YTITLE")
    return fig

# Display
cb_fig = build_contingency_bar()
cb_fig.write_image("images/7-5-16.png", scale=1, height=500, width=700)

cb_fig.show()
