# Any Number of Arguments
# Write a function called any_number that can receive any number of arguments (integers and floats) and return the average of those integers. 
# If you pass 12, 90, 12, 34 as arguments your function should return 37.0 as average. 
# If you pass 12, 90 your function should return 51.0 as average.


def any_number(*n: float|int):
    sumka = sum(n)
    liczba_argumentow = 0   
    for i in n:
        liczba_argumentow += 1
    srednia = sumka / liczba_argumentow
    zaokraglenie = round(srednia,2)
    return zaokraglenie

print(any_number(2,5,1))
