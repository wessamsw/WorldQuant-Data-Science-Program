# splitting data into feature matrix and target vector

target = "price_aprox_usd"  # <--- vector
features = ["surface_covered_in_m2", "lat", "lon", "borough"]   # <--- matrix
X_train = df[features]  # training data
y_train = df[target]    # " " " "

# The vector is what we are trying to predict using the matrix
# In this case we are trying to predict the price of a property
# using the features in the matrix
