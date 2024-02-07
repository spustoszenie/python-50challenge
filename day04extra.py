# Index of the Longest Word
# Write a function called word_index that takes one argument, a list of strings and returns the index of the longest word in the list. 
# If there is no longest word (if all the strings are of the same length), the function should return zero (0).


words1 = ["Hate", "remorse", "vengeance"]   # this list below should return 2.
words2 = ["Love", "Hate"]                   # this list below, shoul return zero (0)

def word_index(strings_list):
        najdluzszy = max(strings_list, key=len)
        index_najdluzszego = strings_list.index(najdluzszy)
        # print(najdluzszy)
        # print(index_najdluzszego)
        return index_najdluzszego

word1 = ['Hate','remorse','vengance']
word2 = ['Love','Hate']

print(word_index(word2))
