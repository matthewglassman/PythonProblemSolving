#A problem using conditional statements to take an order and sum the calories of the items.

#Gather user item order and set to a variable

burger_choice = int(input())
sides_choice = int(input())
#drink_choice = int(input())
#dessert_choice = int(input())

burger_calories = 0
sides_calories = 0
#drink_calories = 0
#dessert_calories = 0

#Get burger_calories
if burger_choice == 1:
    burger_calories = 461
elif burger_choice == 2:
    burger_calories = 431
elif burger_choice == 3:
    burger_calories = 420
elif burger_choice == 4:
    burger_calories = 0

#Get sides_calories
if sides_choice== 1:
    sides_calories = 100
elif sides_choice == 2:
    sides_calories = 57
elif sides_choice == 3:
    sides_calories = 70
elif sides_choice == 4:
    sides_calories = 0


total_calories = burger_calories + sides_calories

print(total_calories)