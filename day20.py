# Capitalize First Letter
# Write a function called capitalize. This function takes a string as an argument and capitalizes the first letter of each word. 
# For example, ‘i like learning’ becomes ‘I Like Learning’.

def capitalize(gora: str):
    return gora.title()   # aby zadziałał print poza funkcją, musi być return

print(capitalize("i Like learning!"))

def capitalize(gora: str):
    print(gora.title())     

capitalize("i Like learning!")
