# Strings to Integers
# Write a function called convert_add that takes a list of strings as an argument and converts it to integers and sums the list. 
# For example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and summed to 9

list = ['1','3','5']

def convert_add(lista):
    int_lista = []
    for i in lista:
        int_lista.append(int(i))

    suma_listy = sum(int_lista)
    return suma_listy

print(convert_add(list))
