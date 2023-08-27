import libraries

acc_train = model.score(X_train, y_train)
acc_test = model.score(X_test, y_test)

print("Model Training Accuracy:", round(acc_train, 4))
print("Model Test Accuracy:", round(acc_test, 4))

  # Sample output
  Model Training Accuracy: 1.0
  Model Test Accuracy: 0.9764
