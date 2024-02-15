# Unpack A Nest
# Nested_list = [[12, 34, 56, 67], [34, 68, 78]]
# Write a code that generates a list of the following numbers from the nested list above – 34, 67, 78. 
# Your output should be another list:
# [34, 67, 78]. The list output should not have duplicates.



nested_list = [[12,34,56,67],[34,68,78]]

def find_numbers_in_nested_list(nested_list: list):
    znaleziska = []
    for i in nested_list:
        if 34 in i:
            znaleziska.append(34)
        if 67 in i:
            znaleziska.append(67)
        if 78 in i:
            znaleziska.append(78)
    znaleziska_na_set = set(znaleziska)
    lista_bez_duplikatow = list(znaleziska_na_set)
    print(lista_bez_duplikatow)

find_numbers_in_nested_list(nested_list)
