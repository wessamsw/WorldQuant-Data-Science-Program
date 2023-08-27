import libraries
import 1_import

# 1
# Percentage of respondents in df that are business owners, 
# assign result to the variable pct_biz_owners. 
# Review documentation regarding "HBUS" column
# https://sda.berkeley.edu/sdaweb/docs/scfcomb2019/DOC/hcbkfx0.htm

pct_biz_owners = sum(df["HBUS"]) / (sum(df["HBUS"] == 0) + sum(df["HBUS"]))
print("% of business owners in df:", pct_biz_owners)

# 2
# DataFrame df_inccat showing normalized frequency 
# for income categories for business owners and non-business owners

inccat_dict = {
    1: "0-20",
    2: "21-39.9",
    3: "40-59.9",
    4: "60-79.9",
    5: "80-89.9",
    6: "90-100",
}

df_inccat = (
    df["INCCAT"]
    .replace(inccat_dict)
    .groupby(df["HBUS"])
    .value_counts(normalize=True)
    .rename("frequency")
    .to_frame()
    .reset_index()
)

df_inccat

# 3
# Seaborn, create a side-by-side bar chart of df_inccat

sns.barplot(
    x="INCCAT",
    y="frequency",
    hue="HBUS",
    data=df_inccat,
    order=inccat_dict.values()
)
plt.xlabel("<Your x_Title>")
plt.ylabel("<Your y_Title>")
plt.title("<Your Title>");

# 4
# create a scatter plot that shows "HOUSES" vs. "DEBT"

sns.scatterplot(x=df["DEBT"] / 1e6, y=df["HOUSES"] / 1e6, palette="deep")
plt.xlabel("Household Debt")
plt.ylabel("Home Value")
plt.title("Home Value vs. Household Debt");

# 5
# New DataFrame df_small_biz containing 
# only business owners whose income is below $500,000

mask = (df["HBUS"]) & (df["INCOME"] < 500_000)
df_small_biz = df[mask]
