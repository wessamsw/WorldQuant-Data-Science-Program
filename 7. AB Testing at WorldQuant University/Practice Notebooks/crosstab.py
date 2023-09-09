""" """

import imports


data = pd.crosstab(
    index=<yourDataFrame>["group"],
    columns=<yourDataFrame>["admissionsQuiz"],
    normalize=False
)
