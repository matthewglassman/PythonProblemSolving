#A script that checks to see if a pattern indicates a telemarketer is calling or not and whether to answer the call accordingly.

first_digit = int(input())
second_digit = int(input())
third_digit = int(input())
fourth_digit = int(input())

if ((first_digit == 8 or first_digit == 9) and
    (second_digit == third_digit) and 
    (fourth_digit == 8 or fourth_digit == 9)):
    print("Ignore")
else:
    print("Answer")
 