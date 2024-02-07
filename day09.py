# Biggest Odd Number
# Create a function called biggest_odd that takes a string of numbers and returns the biggest odd number in the list. 
# For example, if you pass ‘23569’ as an argument, your function should return 9.

string = '23596'

def biggest_odd(string):
    lista_ze_stringa = []
    for i in string:
        lista_ze_stringa.append(i)
    max_z_listy = max(lista_ze_stringa)
    return max_z_listy

print(biggest_odd(string))
