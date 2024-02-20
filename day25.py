# All the Same
# Create a function called all_the_same that takes one argument, a string, a list, or a tuple and checks if all the elements are the same. 
# If the elements are the same, the function should return True. If not, it should return False. For example, [‘Mary’, ‘Mary’, ‘Mary’] should return True.

x = ['Mary','Mary','Mary']
y = ['Mary','Mary','Mary', 'Johny']
def all_the_same(str_list_tuple):
    for i in range(len(str_list_tuple)):
        if str_list_tuple[i] != str_list_tuple[i - 1]:
            return False
        else:
            return True
        
print(all_the_same(x))
print(all_the_same(y))
