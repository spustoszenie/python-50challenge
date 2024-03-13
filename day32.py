def password_validator():
    
    while True:
        password = input("Enter password: ")
        if len(password) < 8:
            print("Password is too short!")
            pass
        elif password == password.lower():
            print("Złe hasło, użyj wielkiej litery!")
            pass
        elif password == password.upper():
            print("Złe hasło, brakuje małej litery!!!")
            pass
        elif not any(char.isdigit() for char in password):
            print("brakuje cyferki!")
            pass
        else:
            print(f'Twoje hasło to : {password}')
            return password
        
password_validator()
