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
