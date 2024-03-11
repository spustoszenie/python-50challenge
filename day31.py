# Longest Word
# Write a function that has one parameter and takes a list of words as an argument. 
# The function returns the longest word from the list. Name the function longest_word. 
# The function should return the longest word and the number of letters in that word.
# For example, if you pass [‘Java, ‘JavaScript’, ‘Python’], your function should return
# [10, JavaScript] as the longest word.

programming_langs = ['Java','JavaScript','Python']
def longest_word(lista_slow: list):
    najdluzesze = ''

    for i in lista_slow:
        if len(i) > len(najdluzesze):
            najdluzesze = i
         
    liczba_liter = len(najdluzesze)

    suma_sumarum = [ liczba_liter, najdluzesze]
    return suma_sumarum

print(longest_word(programming_langs))
