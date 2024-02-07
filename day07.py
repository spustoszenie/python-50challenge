# A String Range
# Write a function called string_range that takes a single number and returns a string of its range. 
# The string characters should be separated by dots(.) 
# For example, if you pass 6 as an argument, your function should return ‘0.1.2.3.4.5’


def string_range(ran):
    dot_string = []
    for i in range(ran):
        dot_string.append(i)
        dot_string.append('.')
    jeden_string = ''.join(map(str, dot_string))
    bezkropkinakoncu_slicing = jeden_string[:-1]
    return bezkropkinakoncu_slicing
    
print(string_range(6))
