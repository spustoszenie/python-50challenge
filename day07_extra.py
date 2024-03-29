# Dictionary of names
# You are given a list of names, and you are asked to write a code that returns all the names that start with ‘S’. 
# Your code should return a dictionary of all the names that start with S and how many times they appear in the dictionary. Here is a list below:
# names = ["Joseph","Nathan", "Sasha", "Kelly","Muhammad", "Jabulani", "Sera”, "Patel", "Sera”]
# Your code should return: {“Sasha”: 1, “Sera”: 2}

names = ['Józio', 'Natka', 'Sasha', 'Kaja', 'Ali', 'Abdullah', 'Sara', 'Patelson', 'Sara']

def policzenie_powtorzen_dla_litery(X):
    licznik_imion = {}

    for imie in names:
        if imie.startswith(X):
            if imie in licznik_imion:
                licznik_imion[imie] += 1
            else:
                licznik_imion[imie] = 1

    return licznik_imion

# Wywołanie funkcji i wydrukowanie wyniku
wynik = policzenie_powtorzen_dla_litery('S')
print(wynik)
