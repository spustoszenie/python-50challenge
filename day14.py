# Flatten the List
# Write a function called flat_list that takes one argument, a nested list. 
# The function converts the nested list into a one-dimension list. For example [[2,4,5,6]] should return [2,4,5,6]

nested_list = [[2,4,5,6]]

def flat_list(zagniezdzona):
    final_list = []
    for i in zagniezdzona:
        for j in i:
            final_list.append(j)
    return final_list

print(flat_list(nested_list))
