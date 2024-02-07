def add_even(numerki):
    parzyste = []
    nieparzyste = []
    for i in numerki:
        if i % 2 == 0:
            parzyste.append(i)
        else:
            nieparzyste.append(i)

    roznica = max(parzyste) - min(nieparzyste)
    return roznica

lista_num = [3,2,4,6,56]
print(add_even(lista_num))