# Same in Reverse
# Write a function called same_in_reverse that takes a string and checks if the string reads the same in reverse. 
# If it is the same, the code should return True if not, it should return False.
# For example, ‘dad’ should return True, because it reads the same in reverse.

cos = "dad"

def same_in_reverse(cos: str):
    reversed_string = ""
    for i in reversed(cos):
        reversed_string += i
    return cos == reversed_string
    
print(same_in_reverse(cos))
