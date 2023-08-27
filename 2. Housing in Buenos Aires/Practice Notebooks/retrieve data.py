# retrieve intercept
intercept = model.named_steps["ridge"].intercept_

# retrieve coefficients
coefficients = model.named_steps["ridge"].coef_

# retrieve names
features = model.named_steps["onehotencoder"].get_feature_names()

# create a series of names and values
feat_imp = pd.Series(coefficients, index=features)
feat_imp

# sample output
surface_covered_in_m2               291.654156
lat                                 478.901375
lon                               -2492.221814
borough_Benito Juárez             13778.188880
borough_Iztacalco                   405.403127
borough_Azcapotzalco               2459.288646
borough_Coyoacán                   3737.561001
borough_Álvaro Obregón             3275.121061
borough_Iztapalapa               -13349.017448
borough_Cuauhtémoc                 -350.531990
borough_Tláhuac                  -14166.869486
borough_Miguel Hidalgo             1977.314718
