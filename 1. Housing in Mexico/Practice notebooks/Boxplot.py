import matplotlib.pyplot as plt

plt.boxplot(df["area_m2"])
plt.xlabel("Area [sq meters]")
plt.title("Distribution of Home Sizes")
