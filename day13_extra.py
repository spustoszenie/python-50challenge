Pyramid of Snakes
Write a function called Python_snakes that takes a number as an argument and creates the following shape, using the number’s range: (hint: Use the loops and emoji library. 
If you pass 4 as argument, your code should print the following
  🐍
 🐍🐍
🐍🐍🐍


from emoji import emojize

def python_snake(nu :int):
    for i in range( nu):
        for j in range(nu, i, -1):
            print(end=" ")
        for k in range(0, i):
            print(emojize(':snake:'), end=" ")
        print("\n")

python_snake(7)
