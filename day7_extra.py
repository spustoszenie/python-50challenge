names = ['Józio', 'Natka', 'Saszka', 'Kaja', 'Ali', 'Abdullah', 'Sara', 'Patelson', 'Sara']

def wyluskanie_imion_na_dana_litere(X):
    imiona = []
    for i in names:
        if i.startswith(X):
            imiona.append(i)
    return imiona

def policzenie_powtorzen():
    licznik_imion = {}
    lista_imion_na_litere = wyluskanie_imion_na_dana_litere('s')

    for i in lista_imion_na_litere:
        if i in licznik_imion:
            licznik_imion[i] += 1
        else:
            licznik_imion[i] = 1

    return licznik_imion

# Wywołanie funkcji i wydrukowanie wyniku
wynik = policzenie_powtorzen(x)
print(wynik)

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




