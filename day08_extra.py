# List of Prime Numbers
# Write a function called prime_numbers. This function asks a user to enter a number (integer) as an argument and returns a list of all the prime numbers within its range. 
# For example, if user enters 10, your code should return [2, 3, 5, 7] as prime numbers.
    
def prime_numbers():
    liczba = int(input("Podaj cyferkę, lub liczbę : "))
    liczby_pierwsze = []

    for i in range(2, liczba):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            liczby_pierwsze.append(i)

    return liczby_pierwsze

print(prime_numbers())
