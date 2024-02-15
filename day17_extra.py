# Sort by Length
# names = [ "Peter", "Jon", "Andrew"]
# Write a function called sort_length that takes a list of strings as an argument, and sorts the strings in ascending order according to their length. 
# For example, the list above should return: 
# ['Jon', 'Peter', 'Andrew']
# Do not use the built-in sort functions

names = [ "Peter", "Jon", "Andrew"]

def sort_length(lista_stringow :list):
    sort = sorted(lista_stringow, key=len)
    return sort

print(sort_length(names))

############ ZAKAZ FUNKCJI SORT!!!!!!!! #############

names = [ "Peter", "Jon", "Andrew"]

def sort_length(lista_stringow :list):
    len1 = []
    len2 = []
    len3 = []
    len4 = []
    len5 = []
    len6 = []
    len7 = []
    for i in lista_stringow:
        if len(i) == 1:
            len1.append(i)
        elif len(i) == 2:
            len2.append(i)
        elif len(i) == 3:
            len3.append(i)
        elif len(i) == 4:
            len4.append(i)
        elif len(i) == 5:
            len5.append(i)
        elif len(i) == 6:
            len6.append(i)
        elif len(i) == 7:
            len7.append(i)
    posortowana = len1 + len2 + len3 + len4 + len5 + len6 + len7
    return posortowana
  
print(sort_length(names))
