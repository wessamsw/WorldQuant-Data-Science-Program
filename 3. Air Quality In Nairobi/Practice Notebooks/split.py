# percentage ---> 90% (0.9), 80% (0.8) ...
cutoff_test = int(len(y) * <percentage>)
y_train = y.iloc[:cutoff_test]
y_test = y.iloc[cutoff_test:]
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

# sample output
y_train shape: (1533,)
y_test shape: (171,)
