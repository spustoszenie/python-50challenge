def word_index(strings_list):
        najdluzszy = max(strings_list, key=len)
        index_najdluzszego = strings_list.index(najdluzszy)
        # print(najdluzszy)
        # print(index_najdluzszego)
        return index_najdluzszego

word1 = ['Hate','remorse','vengance']
word2 = ['Love','Hate']

print(word_index(word2))