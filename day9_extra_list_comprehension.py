def biggest_odd(string):
    biggest = [ x for x in string if x != 0]
    biggest.sort()
    return biggest


string = [1,0,5,8,9,0,4]
print(biggest_odd(string))