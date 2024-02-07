names = ['kerry','dickson','John','Mary','carol','Rose','adam']

def print_lower_names(names):
    low_names = []
    for i in names:
        if i.islower():
            low_names.append(i)
    low_names.sort()
    low_tuple = tuple(low_names)
    return low_tuple

print(print_lower_names(names))
