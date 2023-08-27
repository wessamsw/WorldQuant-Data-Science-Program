""" """

import imports


# contingency table
contingency_table = Table2x2(data.values)

# chi-square test
chi_square_test = contingency_table.test_nominal_association()

# odds ratio
odds_ratio = contingency_table.oddsratio.round(1)

# summary...
summary = contingency_table.summary()
