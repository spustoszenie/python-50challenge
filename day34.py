# Just Digits
# In this challenge, copy the text below and save it as a CSV file. Save it in the same folder as your Python file. Save it as python.csv.
# Write a function called just_digits that reads the text from the CSV file and returns only digit elements from the file. 
# Your function should return 1991, 2, 200, 3, 2008 as a list of strings.

import csv
import re

def tylko_cyfry():
    cyfry = []
    with open('python.csv', 'r') as plik_csv:
        czytnik = csv.reader(plik_csv)
        for wiersz in czytnik:
            for element in wiersz:
                wyciagniete_cyfry = re.findall(r'\d+', element)
                cyfry.extend(wyciagniete_cyfry)
    return cyfry

print(tylko_cyfry())
