import libraries

class_report = classification_report(y_test, model.predict(X_test))
print(class_report)
