# test type 1
X_test = pd.read_csv("filePath.csv", index_col="b_id")
y_test_pred = pd.Series(final_model_dt.predict(X_test))
y_test_pred[:5]

  # sample output
  0    1
  1    1
  2    1
  3    1
  4    0
  dtype: int64


# test type 2
test_acc = model.score(X_test, y_test)
print("Test Accuracy:", round(test_acc, 2))
  
  # sample output
  Test Accuracy: 0.72
    

# test type 3
acc_train = accuracy_score(y_train, model_lr.predict(X_train))
acc_test = model_lr.score(X_test, y_test)

print("LR Training Accuracy:", acc_train)
print("LR Validation Accuracy:", acc_test)

  # sample output
  LR Training Accuracy: 0.717985042664646
  LR Validation Accuracy: 0.7218817948211109
