xyz = [2,4,67,7]

def swap_value(jakiestambyleco):
    pierwszy = jakiestambyleco[0]
    ostatni = jakiestambyleco[-1]
    jakiestambyleco[0] = ostatni
    jakiestambyleco[-1] = pierwszy
    return jakiestambyleco

print(swap_value(xyz))