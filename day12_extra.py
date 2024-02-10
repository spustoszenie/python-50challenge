# Your Age in Minutes
# Write a function called age_in_minutes that tells a user how old they are in minutes. 
# Your code should ask the user to enter their year of birth, and it should return their age in minutes (by subtracting their year of birth to the current year).
# Here are things to look out for:
# a. The user can only input a 4-digit year of birth. For example, 1930 is a valid year. 
# However, entering any number longer or less than 4 digits long should render input invalid. Notify the user to input a four digits number.
# b. If a user enters a year before 1900, your code should tell the user that input is invalid. If the user enters the year after the current year, the code should tell the user, to input a valid year.
# The code should run until the user inputs a valid year.
# Your function should return the user's age in minutes. For example, if someone enters 1930, as their year of birth your function should return:
# You are 48,355,200 minutes old.

def age_in_minutes():
    
    while True:
        data_urodzenia = input("What is your year of birth ? (enter only 4 digits) : ")
        if data_urodzenia.isdigit() == False:
            print("Ech.. only 4 digits tzn same cyfry... ech...")
        elif len(data_urodzenia ) != 4:
            print ("Invalid input, dude WTF?!")
        elif int(data_urodzenia) > 2024:
            print("No na pewno... jeszcze raz")
        elif int(data_urodzenia) < 1900:
            print("Jesteś trupem, hahaha!")
        else:
            ile_lat = 2024 - int(data_urodzenia)
            wiek_w_minutach = ile_lat*60*24*365
            return wiek_w_minutach

print(age_in_minutes())

##########   Bonus datetime   ########

from datetime import datetime

def age_in_minutes():
    rok_urodzenia = int(input("Podaj rok urodzenia: "))
    miesiac_urodzenia = int(input("Podaj miesiac urodzenia: "))
    dzien_urodzenia = int(input("Podaj dzien urodzenia: "))
    data_uro_dokladnie = datetime(rok_urodzenia,miesiac_urodzenia,dzien_urodzenia)
    teraz = datetime.now()
    wiek_w_minutach = (teraz - data_uro_dokladnie).total_seconds() / 60
    return wiek_w_minutach

print(age_in_minutes())
