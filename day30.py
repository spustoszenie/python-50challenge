# Most Repeated Name
# Write a function called repeated_name that finds the most repeated name in the following list.

name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
def most_repeated_name(lista_imion: list):
    podliczenie = {}
    for i in lista_imion:
        if i in podliczenie:
            podliczenie[i] += 1
        else:
            podliczenie[i] = 1
    najczestsze_imie = max(podliczenie)
    print(najczestsze_imie)

most_repeated_name(name)
