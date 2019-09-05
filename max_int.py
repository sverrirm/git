# Design an algorithm that finds the maximum positive integer input by a user.  
# The user repeatedly inputs numbers until a negative value is entered.



    # Do not change this line

max_int = 0
in_num = 0

while 1:
    in_num = num_int = int(input("Input a number: "))

    if in_num > max_int:
        max_int = in_num
    if in_num < 0:
        break


        
print("The maximum is", max_int)    # Do not change this line

