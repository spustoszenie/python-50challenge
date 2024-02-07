def your_vat():
    while True:
        try:
            cena = float(input("Podaj cenę: "))
            vat = float(input('Podaj VAT  (w procentach): '))
            cena_z_vat = cena + cena * vat * 0.01
            print(cena_z_vat)
        except ValueError:
            pass

your_vat()