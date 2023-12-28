# A script to check if a password is valid based on the following rules:
# 1. Must be a string between 8 and 12 characters (inclusive) long.
# 2. Must contain at least 3 lowercase letters.
# 3. Must contain at least 2 uppercase letters.
# 4. Must contain at least 1 digit.

#Taking input from user as the password to check for validity.

password = str(input()) 
 
count_lower = 0
count_upper = 0
count_digit = 0
 
 
if (len(password)  >= 8) and (len(password) <= 12):
    for characters in password:
        if characters >= 'A' and characters <= 'Z':
            count_upper = count_upper + 1
        elif characters >= 'a' and characters <= 'z':
            count_lower = count_lower + 1
        elif characters >= '0' and characters <= '9':
            count_digit = count_digit + 1
else:
    print("Password is not long enough")
  
# print(count_upper)
# print(count_lower)   

if count_lower >= 3 and count_upper >= 2 and count_digit >= 1:
    print('Valid')
else:
    print('Invalid')