# Teacher’s Salary
# A school has asked you to write a program that will calculate teachers' salaries. 
# The program should ask the user to enter the teacher’s name, the number of periods taught in a month, and the rate per period. 
# The monthly salary is calculated by multiplying the number of periods by the monthly rate.
# The current monthly rate per period is $20. If a teacher has more than 100 periods in a month, everything above 100 is overtime. 
# Overtime is $25 per period. For example, if a teacher has taught 105 periods, their monthly gross salary should be 2,125. 
# Write a function called your_salary that calculates a teacher’s gross salary. The function should return the teacher’s name, periods taught, and gross salary. 
# Here is how you should format your output:
# Teacher: John Kelly,
# Periods: 105
# Gross salary:2,125

def salary():
    while True:
        teacher = input("Enter teacher's name: ")
        if teacher == 'stop':
            break

        lessons = float(input("Enter number of lessons: "))

        if lessons <= 100:
            standard_salary = 20*lessons
            print(f'Teacher: {teacher}\nPeriods: {lessons},\nSalary: {standard_salary}')
        else:
            extra_hours_salary = (lessons-100)*25+2000 
            print(f'Teacher: {teacher}\nPeriods: {lessons},\nSalary: {extra_hours_salary}')
salary()
