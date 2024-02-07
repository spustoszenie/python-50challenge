# Are They Equal?
# Write a function called equal_strings. The function takes two strings as arguments and compares them. 
# If the strings are equal (if they have the same characters and have equal length), it should return True, if they are not, it should return False. 
# For example, ‘love’ and ‘evol’ should return True.

raz = 'love'
lol = 'evol'
trzy = 'loove'
def equal_string(jeden,dwa):
    return len(sorted(jeden)) == len(sorted(dwa))

sprawdzenie = equal_string(raz,lol)
        
if sprawdzenie:
    print('równe')
else:
    print('różne')

sprawdzenie = equal_string(raz,trzy)
        
if sprawdzenie:
    print('równe')
else:
    print('różne')

