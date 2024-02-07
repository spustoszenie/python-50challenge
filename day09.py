def biggest_odd(string):
    lista_ze_stringa = []
    for i in string:
        lista_ze_stringa.append(i)
    max_z_listy = max(lista_ze_stringa)
    return max_z_listy

string = '23596'
print(biggest_odd(string))