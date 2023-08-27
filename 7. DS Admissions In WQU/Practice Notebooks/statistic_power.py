""" """

import imports


chi_square_power = GofChisquarePower()
group_size = math.ceil(chi_square_power.solve_power(
    effect_size=0.5,  # medium --> 0.5; small --> 0.2; large --> 0.8
    alpha=0.05,
    power=0.8
))
