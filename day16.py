# Sum the List
# Write a function called sum_list with one parameter that takes a nested list of integers as an argument and returns the sum of the integers. 
# For example, if you pass [[2, 4, 5, 6], [2, 3, 5, 6]] as an argument your function should return a sum of 33.

lista = [[2,4,5,6],[2,3,5,6]]
def sum_list(zakotwionalista: list):
    sumka = 0
    for i in zakotwionalista:
        for j in i:
            sumka += j
    return sumka

print(sum_list(lista))
