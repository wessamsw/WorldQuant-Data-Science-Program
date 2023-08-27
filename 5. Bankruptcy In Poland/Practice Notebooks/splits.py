import libraries

# Feature matrix and Target vector
target = "bankrupt"
X = df.drop(columns="bankrupt")
y = df[target]


# Training and test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
