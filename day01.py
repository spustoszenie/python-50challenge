# Division and Square-root
# Write a function called divide_or_square that takes one argument (a number), and returns the square root of the number if it is divisible by 5, returns its remainder if it is not divisible by 5. 
# For example, if you pass 10 as an argument, then your function should return 3.16 as the square root.

import math
def divide_or_square(x):
    y = math.sqrt(x)
    return y

number = int(input("What do you wanna to root ?"))
print(divide_or_square(number))
