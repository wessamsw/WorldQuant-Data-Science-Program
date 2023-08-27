lr_train_acc = accuracy_score(y_train, model_lr.predict(X_train))
lr_val_acc = model_lr.score(X_val, y_val)

print("Logistic Regression, Training Accuracy Score:", lr_train_acc)
print("Logistic Regression, Validation Accuracy Score:", lr_val_acc)

# sample output
Logistic Regression, Training Accuracy Score: 0.6515042628948486
Logistic Regression, Validation Accuracy Score: 0.6536878552296335
