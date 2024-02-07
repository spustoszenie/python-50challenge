# Duplicate Names
# Write a function called check_duplicates that takes a list of strings as an argument. The function should check if the list has any duplicates. 
# If there are duplicates, the function should return the duplicates. If there are no duplicates, the function should return "No duplicates". 
# For example, the list of fruits below should return apple as a duplicate and list of names should return "no duplicates".

fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']


def check_duplicates(lista):
    duplicates = set()
    for i in lista:
        if lista.count(i) > 1:
            duplicates.add(i)

    if duplicates:
        return duplicates
    else:
        return 'No duplicates'

print(check_duplicates(fruits))
print(check_duplicates(names))

# samo sprawdzenie czy występują duplikaty bez ich drukowania 

# def has_duplicates(lst):
#     for i in lst:
#         if lst.count(i) > 1:
#             return True
#     return False

# my_list = [1, 2, 3, 1, 2, 4]
# if has_duplicates(my_list):
#     print("Lista zawiera duplikaty.")
# else:
#     print("Brak duplikatów w liście.")
