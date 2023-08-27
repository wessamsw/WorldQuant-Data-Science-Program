# DECISION TREE
features = X_train.columns
importances = <yourModel eg final_model_dt>.named_steps["decisiontreeclassifier"].feature_importances_
feat_imp = pd.Series(importances, index=features).sort_values()
feat_imp.head()

# sample output
plan_configuration        0.004189
land_surface_condition    0.008599
foundation_type           0.009967
position                  0.011795
ground_floor_type         0.013521
dtype: float64


# LOGISTIC REG
features = model_lr.named_steps["onehotencoder"].get_feature_names()
importances = model_lr.named_steps["logisticregression"].coef_[0]
feat_imp = pd.Series(np.exp(importances), index=features).sort_values()
feat_imp.head()

# sample output
superstructure_Brick, cement mortar    0.345719
foundation_type_RC                     0.364478
roof_type_RCC/RB/RBC                   0.415979
ground_floor_type_RC                   0.527756
caste_household_Kumal                  0.543642
dtype: float64



# horizontal bar chart
feat_imp.plot(kind="barh")
plt.xlabel("importance")
plt.ylabel("Label")
plt.title("Feature Importance");


