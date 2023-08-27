import libraries
import 1_import
import 2_explore
import 3_explore
import 4_split
import model

# 16
# DataFrame xgb containing mean values 
# of the features in X for the 3 clusters 
# in your final_model
labels = final_model.named_steps["kmeans"].labels_
xgb = X.groupby(labels).mean()
xgb

# 17
# create side-by-side bar chart from xgb 
# showing mean of the features in X 
# for each of the clusters in your final_model
fig = px.bar(
    xgb,
    barmode="group",
    title="Your Title"
)
fig.update_layout(xaxis_title="Your x_label", yaxis_title="Your y_label")

# 18
# Create a PCA transformer, 
# reduce the dimensionality of X to 2, 
# and then put the transformed data into a DataFrame
pca = PCA(n_components=2, random_state=42)

X_t = pca.fit_transform(X)

X_pca = pd.DataFrame(X_t, columns=["PC1", "PC2"])

# 19
# create a scatter plot of X_pca using seaborn
fig = px.scatter(
    data_frame=X_pca,
    x="PC1",
    y="PC2",
    color=labels.astype(str),
    title="PCA Representation of Clusters"
)
fig.update_layout(xaxis_title="PC1", yaxis_title="PC2")
