 # Create DF called 'damage_by_vdcmun' 
 # group DF by "vdcmun_id" 
 # calculating mean of the "severe_damage" column. 
 # Be sure to sort from highest to lowest proportion
damage_by_vdcmun = (
    df.groupby("vdcmun_id")["severe_damage"].mean().sort_values(ascending=False)
).to_frame()
damage_by_vdcmun


# Line plot
plt.plot(damage_by_vdcmun.values, color="blue")
plt.xticks(range(len(damage_by_vdcmun)), labels=damage_by_vdcmun.index)
plt.yticks(np.arange(0.0, 1.1, 0.2))
plt.xlabel("Mun ID")
plt.ylabel("% Households")
plt.title("Damage by Municipality");
