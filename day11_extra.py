# Swap Values
# Write a function called swap_values. This function takes a list of numbers and swaps the first element with the last element.
# For example, if you pass [2, 4,67, 7] as a parameter, your function should return
# [7, 4, 67, 2].

xyz = [2,4,67,7]

def swap_value(jakiestambyleco):
    pierwszy = jakiestambyleco[0]
    ostatni = jakiestambyleco[-1]
    jakiestambyleco[0] = ostatni
    jakiestambyleco[-1] = pierwszy
    return jakiestambyleco

print(swap_value(xyz))
