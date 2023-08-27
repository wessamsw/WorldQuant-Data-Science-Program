# create bar chart using
# severe damage column which
# contains two classes
df["severe_damage"].value_counts(normalize=True).plot(
    kind="bar", xlabel="Severe Damage", ylabel="Relative Frequency", title="Class Balance"
);
