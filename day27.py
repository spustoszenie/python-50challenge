# Unique Numbers
# Write a function called unique_numbers that takes a list of numbers as an argument. 
# Your function is going to find all the unique numbers in the list. It will then sum up the unique numbers.
# You will calculate the difference between the sum of all the numbers in the original list and the sum of unique numbers in the list. 
# If the difference is an even number, your function should return the original list. 
# If the difference is an odd number, your function should return a list with unique numbers only. 
# For example [1, 2, 4, 5, 6, 7, 8, 8] should return [1, 2, 4, 5, 6, 7, 8, 8].

numerki = [1,2,8,8]
def unikalne_numery(lista_numerow: list):
    unikalne = set(lista_numerow)
    lista_unikalnych = list(unikalne)
    suma_unikalnych = sum(lista_unikalnych)
    total_sum = sum(numerki)
    roznica = total_sum - suma_unikalnych

    if roznica % 2 == 0:
        return lista_numerow
    else:
        return lista_unikalnych

print(unikalne_numery(numerki))
