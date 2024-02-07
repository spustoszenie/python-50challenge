# Odd and Even
# Write a function called odd_even that has one parameter and takes a list of numbers as an argument. 
# The function returns the difference between the largest even number in the list and the smallest odd number in the list. 
# For example, if you pass [1,2,4,6] as an argument the function should return 6 -1= 5.

lista_num = [3,2,4,6,56]

def add_even(numerki):
    parzyste = []
    nieparzyste = []
    for i in numerki:
        if i % 2 == 0:
            parzyste.append(i)
        else:
            nieparzyste.append(i)

    roznica = max(parzyste) - min(nieparzyste)
    return roznica

print(add_even(lista_num))
