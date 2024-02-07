def register_check(register):
    present = 0
    for i in register.values():
        if i == 'yes':
            present += 1
    return present

register = {'Michael':'yes', 'John':'no','Peter':'yes','Mary':'yes'}

print(register_check(register))