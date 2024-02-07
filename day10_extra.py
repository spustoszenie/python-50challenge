# A Thousand Separator

# Your new company has a list of figures saved in a list. The issue is that these numbers have no separator. The numbers are saved in the following format:
# [1000000, 2356989, 2354672, 9878098].
# You have been asked to write a code that will convert each of the numbers in the list into a string. Your code should then add a comma on each number as a thousand separator for readability. 
# When you run your code on the above list, your output should be:
# [ '1,000,000', '2,356,989', '2,354,672', '9,878,098’]
# Write a function called convert_numbers that will take one argument, a list of numbers above.


po_tysiackroc = ['1000000', '2356989', '245158', '65958751']

def convert_number(byleco):
    for i in byleco:
        print(i)
        z_kropkami = ''
        for index, j in enumerate(reversed(i), start=1):
            z_kropkami = j + z_kropkami
            if index % 3 == 0 and index != len(i) and (index+1) % 3 != 0:
                z_kropkami = '.' + z_kropkami
        print(z_kropkami)

convert_number(po_tysiackroc)
