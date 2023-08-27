import libraries
import 1_import
import 2_explore

# 6
# Histogram from the "AGE" column 
# in df_small_biz with 10 bins
df_small_biz["AGE"].hist(bins=10)
plt.xlabel("Your x_Label")
plt.ylabel("Your y_Label")
plt.title("Your Title");

# 7
# Variance for all the features in df_small_biz, 
# create Series top_ten_var with 10 features with largest variance
top_ten_var = df_small_biz.var().sort_values().tail(10)
top_ten_var

# 8
# trimmed variance for the features in df_small_biz
# not include the top and bottom 10% of observations
top_ten_trim_var = df_small_biz.apply(trimmed_var, limits=(0.1, 0.1)).sort_values().tail(10)
top_ten_trim_var

# 9
# create a horizontal bar chart of top_ten_trim_var
fig = px.bar(
    x=top_ten_trim_var,
    y=top_ten_trim_var.index,
    title="High Var Feat"
)
fig.update_layout(xaxis_title="Your x_label", yaxis_title="Your y_label")

# 10
# Create list: high_var_cols, 
# with the column names of the five features 
# with the highest trimmed variance
high_var_cols = top_ten_trim_var.tail(5).index.to_list()
high_var_cols
