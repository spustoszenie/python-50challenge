# Tuple of Student Sex
# You work for a school and your boss wants to know how many female and male students are enrolled in the school. 
# The school has saved the students in a list. Your task is to write a code that will count how many males and females are in the list. 
# Your code should return a list of tuples. The list above should return:
# [(‘Male’,7), (‘female’,6)]


students = ['Male', 'Female', 'female', 'male', 'male', 'male','female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
        
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
print(obecnosc(students))
