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