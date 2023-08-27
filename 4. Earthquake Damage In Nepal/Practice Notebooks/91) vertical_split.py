X = df.drop(columns="severe_damage")    # feature matrix: all columns apart from severe_damage
y = df["severe_damage"]       # target vector
print("X shape:", X.shape)
print("y shape:", y.shape)

# sample output
X shape: (76533, 11)
y shape: (76533,)
