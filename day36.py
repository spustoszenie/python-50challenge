# Count String
# Write a function called count that takes one argument a string, and returns a dictionary of how many times each element appears in the string. 
# For example, ‘hello’ should return:
# {‘h’:1,’e’: 1,’l’:2, ‘o’:1}.

def count_string(stringg :str):
    counter = {}
    for i in stringg:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    return counter

print(count_string('hello'))
