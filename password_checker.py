# A script to check if a password is valid based on the following rules:
# 1. Must be a string between 8 and 12 characters (inclusive) long.
# 2. Must contain at least 3 lowercase letters.
# 3. Must contain at least 2 uppercase letters.
# 4. Must contain at least 1 digit.

#Taking input from user as the password to check for validity.

password = str(input()) 
 
for characters in password:
    if (len(password)  >= 8) and (len(password) <= 12):
        print('Good')
    else:
        print('Bad')
   