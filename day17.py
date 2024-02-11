# User Name Generator
# Write a function called user_name, that creates a username for the user. The function should ask a user to input their name.
# The function should then reverse the name and attach a randomly issued number between 0 – 9 at the end of the name.

import random
def user_name():
    user_input = input("Enter username: ")
    reversed_name1 = ''.join(reversed(user_input))
    randomnum = random.randint(0,9)
    return reversed_name1 + str(randomnum)

print(user_name())
