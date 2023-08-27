# df1.shape before dropping NaNs ---> (12834, 6)

df1.dropna(inplace=True)  # drop rows with null values
df1.shape

# Output
(11551, 6)
