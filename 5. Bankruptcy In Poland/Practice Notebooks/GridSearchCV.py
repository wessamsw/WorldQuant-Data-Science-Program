import libraries

# Range of hyperparameters
params = {
    "simpleimputer__strategy": ["mean", "median"],
    "randomforestclassifier__n_estimators": range(25, 100, 25),
    "randomforestclassifier__max_depth": range(10, 50, 10)
}

# Using `GridSearchCV`
model = model = GridSearchCV(
    clf,
    param_grid=params,
    cv=5,
    n_jobs=-1,
    verbose=1
)

# Fit your model
model.fit(X_train_over, y_train_over)

# cross_validation results
results = pd.DataFrame(model.cv_results_)
cv_results.head(5)
