# Return Indexes
# Write a function called index_position. 
# This function takes a string as a parameter and returns the positions or indexes of all lower letters in the string. 
# For example, ‘LovE’ should return [1,2].

def index_position(jakis_string: str):
    low_letters = []
    indeksiki = []
    for i in jakis_string:
        if i.islower():
            low_letters.append(i)

    for i in range(len(jakis_string)):
        if jakis_string[i] in low_letters:
            indeksiki.append(i)
    return indeksiki
    
print(index_position("LovE"))


#### Wersja z enumerate:

def index_position (a):
    idex = []
    for i, item in enumerate(a):
        if item.islower():
        idex.append(i)
    return idex
    
print(index_position('LovE'))
