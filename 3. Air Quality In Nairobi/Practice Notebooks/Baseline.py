from sklearn.metrics import mean_absolute_error

y_train_mean = y_train.mean()
y_pred_baseline = [y_train_mean] * len(y_train)
mae_baseline = mean_absolute_error(y_train, y_pred_baseline)

print("Mean P2 Reading:", y_train_mean)
print("Baseline MAE:", mae_baseline)

# sample output
Mean P2 Reading: 8.617582545265433
Baseline MAE: 4.07658759405218
