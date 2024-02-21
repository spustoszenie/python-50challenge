# Sort Words
# Write a function called sort_words that takes a string of words as an argument, removes the whitespaces, and returns a list of letters sorted in alphabetical order. 
# Letters will be separated by commas. All letters should appear once in the list. This means that you sort and remove duplicates. 
# For example ‘love life’ should return as ['e,f,i,l,o,v'].

def sort_words(words: str):
    unikalne = list(set(words))
    bez_spacji = []
    for i in unikalne:
        if i != ' ':
            bez_spacji.append(i)
    posortowane = sorted(bez_spacji)
    po_przecinku = ','.join(posortowane)

    return po_przecinku

print(sort_words('love life'))
