getstring = input("Please type in some words and I will tell you how many you typed.   ")

#The number of words can be found by counting the number of spaces and adding 1 more than that number. 
totalnumofwords = getstring.count(" ") + 1

#Print the total to the screen
print(totalnumofwords)