def check_duplicates(lista):
    duplicates = set()
    for i in lista:
        if lista.count(i) > 1:
            duplicates.add(i)

    if duplicates:
        return duplicates
    else:
        return 'No duplicates'


fruits = ['apple','orange','banana','apple']
names = ['Yoda','Moses','Joshua','Mark']

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