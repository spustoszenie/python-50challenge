# What’s My Age?
# Write a function called your_age. This function asks a student to enter their name and then it returns their age. 
# For example, if a user enters Peter as their name, your function should return, ‘Hi, Peter, you are 27 years old. 
# This function reads data from the database (dictionary below). 
# If the name is not in the dictionary, your code should tell the user that their name is not in the dictionary, and ask them for their age. 
# Your code should then add the name and age to the dictionary of names_age below. Once added your code should return to the user ‘Hi, (added name), you are (added age) years old’. 
# Remember to convert the input from user to lowercase letters.


names_age = {"jane": 23, "kerry": 45, "tim": 34, 'peter': 27}

def what_is_my_age(names_age: dict):
    name = input("What is your name? ").lower()
    for i in names_age:
        if i == name:
            print(f'Hi, {i}, you are {names_age[i]} years old.')
            return

    new_user = input("I don't know you! What is your age? ").lower()
    names_age[name] = int(new_user)
    print(f'Hi {name}, you are {new_user} years old')
    print(names_age)

what_is_my_age(names_age)

# Wersja 2:
names_age = {"jane": 23, "kerry": 45, "tim": 34, 'peter': 27}

def what_is_my_age(names_age: dict):
    name = input("What is your name?")
    if name in names_age:
        print(f'Hi, {name}, you are {names_age[name]} years old.')
    else:
        new_user = input("I don't know you! What is your age?")
        names_age[name] = int(new_user)


what_is_my_age(names_age)
