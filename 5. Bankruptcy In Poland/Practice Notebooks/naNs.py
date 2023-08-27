import libraries

nans_by_col = df.isna().sum()
print("nans_by_col shape:", nans_by_col.shape)
nans_by_col.head()

  # Sample output
  nans_by_col shape: (96,)
  bankrupt    0
  feat_1      0
  feat_2      0
  feat_3      0
  feat_4      0
  dtype: int64
