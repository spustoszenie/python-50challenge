def only_floats(a,b):
    if type(a) == float and type(b) == float:
        return 2
    elif type(a) == float or type(b) == float:
        return 1
    else:
        return 0

print(only_floats(12.1,23))
print(only_floats(23,12.1))