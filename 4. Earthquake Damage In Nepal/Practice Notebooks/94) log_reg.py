model_lr = make_pipeline(
    OneHotEncoder(use_cat_names=True),
    LogisticRegression(max_iter=<1000-3000>)   #max_iter: varies: suppresses the 'ConvergenceWarning'
)
# Fit model to training data
model_lr.fit(X_train, y_train)
