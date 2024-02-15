# List of Tuples
# Write a function called make_tuples that takes two lists, equal lists, and combines them into a list of tuples. 
# For example, if list a is [1,2,3,4] and list b is [5,6,7,8], your function should return [(1,5), (2,6), (3,7), (4,8)].

a = [1,2,3,4]
b = [5,6,7,8]

def make_tuples(pierwsza: list, druga: list):
    combined_list = []
    secik1 = (pierwsza[0],druga[0])
    secik2 = (pierwsza[1],druga[1])
    secik3 = (pierwsza[2],druga[2])
    secik4 = (pierwsza[3],druga[3])
    combined_list = [secik1,secik2,secik3,secik4]
    print(combined_list)
make_tuples(a,b)

#####################  II SPOSÓB    #############################

def make_tuples(pierwsza: list, druga: list):
    combine = zip(pierwsza,druga)
    combined_list = list(combine)
    return combined_list
print(make_tuples(a,b))

#####################  III SPOSÓB    #############################

def make_tuples(pierwsza: list, druga: list):
    combined_list = []
    for i in range(len(pierwsza)):
        secik = (pierwsza[i],druga[i])
        combined_list.append(secik)
    return(combined_list)
print(make_tuples(a,b))
