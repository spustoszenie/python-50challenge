# Zero Both ends
# Write a function called zeroed code that takes a list of numbers as an argument. The code should zero (0) the first and the last number in the list. 
# For example, if the input is [2, 5, 7, 8, 9], your code should return [0, 5, 7, 8, 0].

lista1 = [2,5,7,8,9]

def zeroed(lista_cyferek):
    zero = lista_cyferek.insert(0,0)
    zero_append = lista_cyferek.append(0)

zeroed(lista1)
print(lista1)
