def string_range(ran):
    dot_string = []
    for i in range(ran):
        dot_string.append(i)
        dot_string.append('.')
    jeden_string = ''.join(map(str, dot_string))
    bezkropkinakoncu_slicing = jeden_string[:-1]
    return bezkropkinakoncu_slicing
    
print(string_range(6))
