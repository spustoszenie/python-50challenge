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
