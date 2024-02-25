# Middle Figure
# Write a function called middle_figure that takes two parameters a, and b. The two parameters are strings. 
# The function joins the two strings and finds the middle element.
# If the combined string has a middle element, the function should return the element, otherwise, return ‘no middle figure’. 
# Use ‘make love’ as an argument for a and ‘not wars’ as an argument for b. 
# Your function should return ‘e’ as the middle element. Whitespaces should be removed.

abc = "make love"
xyz = "not wars"

def middle_figgure(a:str, b:str):
    joined = a+b
    bez_spacji = joined.replace(' ', '')
    
    if len(bez_spacji) / 2 == 0:
        print(" no middle figure")
    else:
        srodkowy = int(len(bez_spacji) / 2 - 0.5)
        return bez_spacji[srodkowy]

print(middle_figgure(abc, xyz))
