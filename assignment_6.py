# to run this script type python assignment_6.py
# Similar to assigment 5 we are once again defining a function that will be used over and over again with the exception of dividing the list into 2; "even" numbered names and "odd" numbered names. 
# We then replaced the the first letter of the even numbered names with the letter "b" and the the odd numbered names with the letter "c".
# After I set a perimeter on how to determine if each name was even or odd by seeing if the amount of letters were divisible by 2 without any remainder.
# If they were, they were considered even. If they weren't then they were odd.
# I then made a loop for the program to run down the entire list of name to determine which was even and odd.
# I then had it print both odd and even list of names and returned the even_list. 
# After I turned the even_list into a variable and printed it.
names_list = ["bob", "jimmy", "max b", "bernie", "jordan","future hendrix"]

def separate(lst_names):
    even_lst = []
    odd_lst = []

    for name in names_list:
        if len(name) % 2 == 0:  #len is even
            even_lst.append(("b"+name[1:]))
        else:
            odd_lst.append((name[:-1]+"c"))

    print(even_lst)
    print(odd_lst)
    return even_lst

even_list = separate(names_list)
print(even_list)