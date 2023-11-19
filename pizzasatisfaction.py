#This little script takes two integer inputs and determines the level of pizza satisfaction for the user based on the following criteria:

# User will be absolutely satisfied if the pizza she gets has a width of 
#  3 units and an extra-cheesiness of at least 95%
# User will be fairly satisfied if the pizza she gets has a width of 
# 1 unit and an extra-cheesiness of at most 50%
# User will be very satisfied with any other pizza she receives.

pizza_width = int(input())
cheesiness =  int(input())

if ((pizza_width == 3 and cheesiness >= 95)):
    print("C.C. is absolutely satisfied with her pizza.")
elif ((pizza_width == 1 and cheesiness <= 50)):
    print("C.C. is fairly satisfied with her pizza.")
else:
    print("C.C. is very satisfied with her pizza.")
