import math

# rounding function
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to