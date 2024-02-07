def convert_add(lista):
    int_lista = []
    for i in lista:
        int_lista.append(int(i))

    suma_listy = sum(int_lista)
    return suma_listy

list = ['1','3','5']

print(convert_add(list))


