# to run this script type python assignment_3.py
# I created this script using 1 variable; over_under_list 
# then created a loop that compared the number inside the variable "over_under_list" to 25.
# Based on the comparison, it either decided if the numbers inside the variable was either "over" or "under" 25
over_under_list = [1,45,32,21,5,17,43,93]
for num in over_under_list:
    print(num)
    if num > 25:
        print("over")
    else:
        print("under")
    