# Count the Dots
# Write a function called count_dots. This function takes a string separated by dots as a parameter and counts how many dots are in the string. 
# For example, ‘h.e.l.p.’ should return 4 dots, and ‘he.lp.’ should return 2 dots.

def count_dots(s):
    kropki = []
    for i in s:
        if i == '.':
            kropki.append(i)
    stringkropek = ''.join(map(str, kropki))
    return stringkropek

print(count_dots('h.e.l.p.'))
