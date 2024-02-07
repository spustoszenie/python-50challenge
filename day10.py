# Hide my Password

# Write a function called hide_password that takes no parameters. The function takes an input (a password) from a user and returns a hidden password. 
# For example, if the user enters ‘hello’ as a password the function should return ‘****’ as a password and tell the user that the password is 4 characters long.


def hidefunction():
    haslo = input("Podaj haslo : ")
    hide_pass = [ '*' for i in haslo ]
    hide_pass = ''.join(hide_pass)
    pass_length = 0
    for i in haslo:
        pass_length += 1
    return (f"Password {hide_pass} is {pass_length} characters long. ")

print(hidefunction())
