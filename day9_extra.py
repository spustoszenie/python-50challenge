def zeros_last(listeczka):
    for i in reversed(listeczka):
        if i == 0:
            listeczka.remove(i)
        else:
            listeczka.sort()
    return listeczka

wow = [1,4,6,0,7,0,9]
print(zeros_last(wow))