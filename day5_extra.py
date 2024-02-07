
def obecnosc(x):
    boys = 0
    girls = 0
    for i in students:

        if i.lower() == 'male':
            boys += 1
        elif i.lower() == 'female':
            girls += 1
        else:
            pass
    # print(boys)
    # print(girls)
    macie_tuple = [('Male', boys), ('Female', girls)]
    print(macie_tuple)
    return macie_tuple
students = ['Male','Female','Female','male','Male','Female','Female','male','Male','Female','male','male','Female']
print(obecnosc(students))