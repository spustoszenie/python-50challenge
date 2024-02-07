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

