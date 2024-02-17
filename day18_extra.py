# Add and Reverse
# Write a function called add_reverse. This function takes two lists as argument and adds each corresponding number, and reverses the outcome. 
# For example, if you pass [10, 12, 34] and [12, 56, 78]. Your code should return [112, 22, 68]. 
# If the two lists are not of equal lengths, the code should return a message that "the lists are not of equal lengths".


pierwsza = [10,12,34,1]
druga = [12,56,78,1]

def add_reverse(pierwsza: list, druga: list):
    suma = []
    if len(pierwsza) != len(druga):
        print("Listy są różnej długości... Kończymy teatrzyk!")
    else:
        for i in range(len(pierwsza)):
            suma.append(pierwsza[i]+druga[i])
        print(suma)
        odwrocona = list(reversed(suma))
        return odwrocona

print(add_reverse(pierwsza,druga))

#### Moim zdaniem jest błąd w rozwiązaniu... albo nie rozumiem co to znaczy "reverses the outcome"
# reverses outcome != reverse list ??
# suma = [22,68,112]
# rozwiązanie to [112, 22, 68]...


# Przykład dla 4 elementów:
# suma = [22, 68, 112, 2]
# wynik z rozwiązania : [2, 68, 22, 112]   raczej błąd...
# moje: [2, 112, 68, 22]
