def hidefunction():
    haslo = input("Podaj haslo : ")
    hide_pass = [ '*' for i in haslo ]
    hide_pass = ''.join(hide_pass)
    pass_length = 0
    for i in haslo:
        pass_length += 1
    return (f"Password {hide_pass} is {pass_length} characters long. ")

print(hidefunction())


