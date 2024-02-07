# User Name Generator
# Write a function called user_name that generates a username from the user’s email. 
# The code should ask the user to input an email and the code should return everything before the @ sign as their user name. 
# For example, if someone entersben@gmail.com, the code should return ben as their username.

def user_name():
    email = input("Podaj mi no tu adresik e-mail: ")
    username = email.split('@')
    return username[0]
print(f"Twój username to {user_name()}")

# Ale to trochę za łatwo i za szybko, także teraz z użyciem samego split
def user_name():
    email = input("Podaj mi no tu adresik e-mail: ")
    username, domena = email.split('@')
    return username
print(f"Twój username to {user_name()}")
