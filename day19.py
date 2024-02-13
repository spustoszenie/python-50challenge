# Words and Elements
# Write two functions. The first function is called count_words which takes a string of words and counts how many words are in the string.
# The second function called count_elements takes a string of words and counts how many elements are in the string. 
# Do not count the whitespaces. The first function will return the number of words in a string and the second one will return the number of elements (less whitespace). 
# If you pass ‘I love learning’, the count_words function should return 3 words and count_elements should return 13 elements.

x = "I love learning"

def count_words(string_ze_slowami: str):
    pojedyncze_slowa = string_ze_slowami.split()
    return len(pojedyncze_slowa)

def count_elements(string_of_words: str):
    pojedyncze_slowa = string_of_words.split()
    liczba_elementow = 0
    for i in pojedyncze_slowa:
        for j in i:
            liczba_elementow += 1
    return liczba_elementow

print(count_words(x))
print(count_elements(x))
