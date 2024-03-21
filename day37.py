# Count the Vowels
# Create a function called count_the_vowels. The function takes one argument, a string, and returns the number of vowels in the string. 
# For example, ‘hello’ should return 2 vowels. 
# If a vowel appears in a string more than once it should be counted as one. 
# For example, ‘saas’ should return 1 vowel. Your code should count lowercase and uppercase vowels.

def licznik_samogłosek(slowo: str):
    samogloski = ['a','e','i','o','u','y']
    znalezione_samogloski_z_malej = []
    znalezione_samogloski_z_duzej = []
    counter_unikalne = 0
    counter_unikalne_duze = 0
    counter_unikalne_male = 0
    for i in samogloski:
        if i.lower() in slowo:
            counter_unikalne += 1
            counter_unikalne_male += 1
            if i.lower() not in znalezione_samogloski_z_malej:
                znalezione_samogloski_z_malej.append(i)
                
        elif i.upper() in slowo:
            counter_unikalne += 1
            counter_unikalne_duze += 1
            if i.upper() not in znalezione_samogloski_z_duzej:
                znalezione_samogloski_z_duzej.append(i)
    
    total = 0
    for i in slowo:
        if i.lower() in samogloski:
            total += 1

    if not znalezione_samogloski_z_duzej and not znalezione_samogloski_z_malej:
        return "Nie znaleziono samoglosek"
    else:
        return f'Znalezione samogłoski z małej: {znalezione_samogloski_z_malej}, \nZ dużej: {znalezione_samogloski_z_duzej}, \nLiczba wszystkich unikalnych samogłosek {counter_unikalne}, \nUnikalne małe samogłoski {counter_unikalne_male}, \nUnikalne duże samogłoski {counter_unikalne_duze}, \nWszystkie samogłoski: {total}'
        
print(licznik_samogłosek('heeeeelloUI'))
