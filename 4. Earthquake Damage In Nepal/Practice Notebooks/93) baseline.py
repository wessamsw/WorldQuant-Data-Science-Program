acc_baseline = y_train.value_counts(normalize=True).max()   # normalize gives you the relative freq
print("Baseline Accuracy:", round(acc_baseline, 2))

# sample output
Baseline Accuracy: 0.55
