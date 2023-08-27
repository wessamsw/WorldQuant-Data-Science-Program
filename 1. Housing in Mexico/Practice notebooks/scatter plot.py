import matplotlib.pyplot as plt

plt.scatter(x=homes_by_state["area_m2"], y=homes_by_state["price_usd"])
plt.xlabel("Area [sq meters]")
plt.ylabel("Price [USD]")
plt.title("Rio Grande do Sul: Price vs. Area");
