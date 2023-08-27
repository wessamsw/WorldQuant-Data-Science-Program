roof_pivot = pd.pivot_table(
    df, index="roof_type", values="severe_damage", aggfunc=np.mean    # roof_type: column in table
).sort_values(by="severe_damage")
roof_pivot
