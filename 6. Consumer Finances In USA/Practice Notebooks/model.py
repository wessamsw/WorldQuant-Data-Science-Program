import libraries
import 1_import
import 2_explore
import 3_explore
import 4_split

# 12
# Iteratively build and train a K-Means 
# model where n_clusters ranges [2, 12]

n_clusters = range(2, 13)
inertia_errors = []
silhouette_scores = []

# Use for loop
for k in n_clusters:
    # Build
    model = make_pipeline(StandardScaler(), KMeans(n_clusters=k, random_state=42))
    # Train
    model.fit(X)
    # Calculate inertia
    inertia_errors.append(model.named_steps["kmeans"].inertia_)
    # Calculate silhouette score
    silhouette_scores.append(
        silhouette_score(X, model.named_steps["kmeans"].labels_)
    )

print("Inertia:", inertia_errors[:10])
print()
print("Silhouette Scores:", silhouette_scores[:3])

# 13
# Line plot showing values of 
# inertia_errors as a function of n_clusters

fig = px.line(
    x=n_clusters, y=inertia_errors, title="Your Title"
)
fig.update_layout(xaxis_title="Your x_label", yaxis_title="Your y_label")

# 14
# Line plot showing values of 
# silhouette_scores as a function of n_clusters

fig = px.line(
    x=n_clusters, y=silhouette_scores, title="Your Title"
)
fig.update_layout(xaxis_title="Your x_label", yaxis_title="Your y_label")

# 15
# Build and train a new k-means model
# n_clusters: 3
# random state: 42

final_model = make_pipeline(
    StandardScaler(),
    KMeans(n_clusters=3, random_state=42)
)
final_model.fit(X)
