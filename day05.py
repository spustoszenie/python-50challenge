# My Discount
# Create a function called my_discount. The function takes no arguments but asks the user to input the price and the discount (percentage) of the product. 
# Once the user inputs the price and discount, it calculates the price after the discount.
# The function should return the price after the discount. For example, if the user enters 150 as price and 15% as the discount, your function should return 127.5.

def my_discount():
    cena = int(input("Podaje cenę: "))
    znizka = int(input("Podaj ile procent rabatu otrzymasz: "))
    rabat = cena * (znizka * 0.01)
    cena_ostateczna = cena - rabat
    return cena_ostateczna
print(my_discount())
