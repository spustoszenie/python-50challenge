# Add Under_Score
# Create three functions. The first called add_hash takes a string and adds a hash # between the words. 
# The second function called add_underscore removes the hash (#) and replaces it with an underscore "_" 
# The third function called remove_underscore, removes the underscore and replaces it with nothing. 
# if you pass ‘Python’ as an argument for the three functions, and you call them at the same time like:
# print(remove_underscore(add_underscore(add_hash('Python'))))
# it should return ‘Python’.

costam = "Jestem hardcorem haha"

def add_hash(addhash: str):
    slowa = addhash.split(' ')   
    added_hash = '#'.join(slowa)
    return added_hash

def add_underscore(underscore: str):
    slowa = underscore.split('#')
    add_underscore = '_'.join(slowa)
    return add_underscore

def remove_underscore(coscos: str):
    slowa = coscos.split('_')
    add_space = ' '.join(slowa)
    return add_space

print(remove_underscore(add_underscore(add_hash(costam))))
print(remove_underscore(add_underscore(add_hash('Python'))))

############# ADD HASH LIST COMPREHENSION ############
# costam = "Jestem hardcorem haha"

# def add_hash(addhash: str):
#     slowa = costam.split(' ')
#     added_hash = '#'.join([word for word in slowa])
#     return added_hash

# print(add_hash(costam))

