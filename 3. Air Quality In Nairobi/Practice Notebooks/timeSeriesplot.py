import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(15, 6))
y.plot(xlabel="Date", ylabel="PM2.5 Level", title="Dar es Salaam PM2.5 Levels", ax=ax);

# Don't delete the code below 👇
plt.savefig("images/3-5-5.png", dpi=150)
