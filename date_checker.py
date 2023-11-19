#This little program takes 2 inputs (month and day) and compares them to a specific date (February 18) to determine
#if the date is before 2/18 then 'Before' gets printed, if the date is after 2/18 it will print 'After'', otherwise it will printe special.

month = int(input())
day = int(input())

if ((month < 2) and (day <= 31) or ((month == 2) and (day <= 17)):
    print("Before")
elif ((month >= 2) and (day >= 19)) or (month > 2) :
    print("After")
else:
    print("Special")