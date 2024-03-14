# Password Validator
# Write a function called password_validator. The function asks the user to enter a password. 
# A valid password should have at least one upper letter, one lower letter, and one number. 
# It should not be less than 8 characters long. When the user enters a password, the function should check if the password is valid. 
# If the password is valid, the function should return the valid password. 
# If the password is not valid, the function should tell the users the errors in the password and prompt the user to enter another password. 
# The code should only stop once the user enters a valid password. (use while loop).

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
