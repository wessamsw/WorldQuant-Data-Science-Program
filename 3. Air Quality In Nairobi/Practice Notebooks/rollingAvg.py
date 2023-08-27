import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(15, 6))
y.rolling(168).mean().plot(ax=ax, xlabel="Date", ylabel="PM2.5 Level", title="Dar es Salaam PM2.5 Levels, 7-Day Rolling Average");
# --> 168 == num of hours in a week

# Don't delete the code below 👇
plt.savefig("images/3-5-6.png", dpi=150)
