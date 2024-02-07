def my_discount():
    cena = int(input("Podaje cenę: "))
    znizka = int(input("Podaj ile procent rabatu otrzymasz: "))
    rabat = cena * (znizka * 0.01)
    cena_ostateczna = cena - rabat
    return cena_ostateczna
print(my_discount())