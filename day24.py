# Average Calories
# Create a function called average_calories that calculates the average calories intake of a user. 
# The function should ask the user to input their calories intake for any number of days and once they hit ‘done’ it should calculate and return the average intake.

def average_calories():
    calories = []
    while True:
        user_input = input("Podaj liczbę kalori: ")
        if user_input == 'done':
            suma = sum(calories)
            average_cal = suma / len(calories)
            return round(average_cal , 2)
        else:
            calories.append(int(user_input))
print(average_calories())
